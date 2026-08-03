#!/usr/bin/env python3
"""Chariot v3b — ultracode panel composer B: ENTHRONED-FIGURE DOMINANT.

Atu VII per drafts/07-chariot-fable5-prompt.md and the Harris scan
(reference/07-chariot-card.jpg). The amber armoured King foremost: lowered
visor, crab crest, massive rounded pauldrons, seated frontal and STILL on
col 23, cradling the glowing Grail (blue ring, red radiant core) at his lap.
Around him, mirrored with PM/PMB: starry-blue scalloped canopy with white
squiggle trim on four russet pillars, two tall scarlet spoked wheels, four
counterchanged sphinxes (dark bull L / two pale center / dark winged R) on
an amber dais, swirling pale nimbus rings full-bleed behind.

Emits:
  drafts/07-chariot-v3b-art-lg.txt       47x32 art
  drafts/07-chariot-v3b-lg-classes.json  per-cell class grid
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23.0

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]
MIRROR = str.maketrans("()/\\[]{}<>`´,.", ")(\\/][}{><´`,.")


def P(r, c, s, cls):
    for i, ch in enumerate(s):
        if ch != " " and 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls


def PB(r, c, s, cls):
    """Place including spaces (spaces punch a breathing halo)."""
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


def PM(r, c, s, cls):
    P(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    P(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def PMB(r, c, s, cls):
    PB(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    PB(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def C(r, s, cls):
    """Axis-centered halo-punched sprite; odd length keeps col 23 center."""
    assert len(s) % 2 == 1, f"C sprite even width: {s!r}"
    PB(r, 23 - len(s) // 2, s, cls)


# ------------------------------------------------- 1. nimbus swirl field
# Concentric pale/blue rings about the Grail heart (r15, c23), 1:2 cell
# aspect baked in, gentle twist. Innermost pale, deepening outward.
CY, CX = 15.0, 23.0
SWIRL = 2.5
EDGES = [9.0, 13.5, 18.0, 22.5, 27.0, 31.5, 36.0]
BANDS = [
    ("field", 22, "'·'·"),
    ("field", 28, "·'·:"),
    ("swirl", 44, ";:·~"),
    ("field", 34, "·:'·"),
    ("swirl", 55, ";:~:"),
    ("field", 40, "·;·:"),
    ("swirl", 62, ";:~;"),
    ("swirl", 72, ";;:~"),
]


def field_d(r, c):
    dx = c - CX
    dy = 2.0 * (r - CY)
    d = math.hypot(dx, dy)
    th = math.atan2(dy, dx) % (2 * math.pi)
    return d + SWIRL * th / (2 * math.pi)


for r in range(H):
    for c in range(W):
        d = field_d(r, c)
        bi = 0
        while bi < len(EDGES) and d >= EDGES[bi]:
            bi += 1
        cls, cov, ramp = BANDS[bi]
        inner = EDGES[bi - 1] if bi else 0.0
        outer = EDGES[bi] if bi < len(EDGES) else 46.0
        t = (d - inner) / (outer - inner)
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if t < 0.24:
            cov += 8
        if h >= cov:
            continue
        ch = ramp[0] if t < 0.24 else ramp[h % len(ramp)]
        P(r, c, ch, cls)


# pale nimbus hoops riding the band boundaries (the white Harris rings)
def hoop(cy, cx, ry, rx, cls):
    for r in range(H):
        dyn = (r - cy) / ry
        s = 1 - dyn * dyn
        if s < 0:
            continue
        x = rx * math.sqrt(s)
        cl, cr = int(round(cx - x)), int(round(cx + x))
        if abs(dyn) > 0.93:
            ch = "-" if dyn < 0 else "_"
            for c in range(cl + 1, cr, 2):
                P(r, c, ch, cls)
        elif abs(dyn) > 0.55:
            P(r, cl, "/" if dyn < 0 else "\\", cls)
            P(r, cr, "\\" if dyn < 0 else "/", cls)
        else:
            P(r, cl, "(", cls)
            P(r, cr, ")", cls)


hoop(15.0, 23.0, 6.75, 13.5, "glow")
hoop(15.0, 23.0, 11.25, 22.5, "glow")
hoop(15.0, 23.0, 15.75, 31.5, "glow")

# ------------------------------------------------- 2. the scarlet wheels
# Tall spoked ellipses flanking, as in the scan (seen nearly edge-on).
def wheel(cx):
    cy, ry, rc = 17.0, 8.2, 5.6
    # spokes
    for k in range(8):
        a = k * math.pi / 4
        er, ec = 0.82 * ry * math.cos(a), 0.82 * rc * math.sin(a)
        steps = 10
        for i in range(2, steps + 1):
            rr = int(round(cy + er * i / steps))
            cc = int(round(cx + ec * i / steps))
            if abs(ec) < 0.8:
                g = "|"
            elif abs(er) < 0.8:
                g = "-"
            else:
                g = "\\" if (er > 0) == (ec > 0) else "/"
            P(rr, cc, g, "wheel")
    # rim: two radial passes + solid fill between them at the sides
    for r in range(H):
        dyn = (r - cy) / ry
        s = 1 - dyn * dyn
        if s < 0:
            continue
        xo = rc * math.sqrt(s)
        xi = (rc - 1.6) * math.sqrt(s)
        col, cor = int(round(cx - xo)), int(round(cx + xo))
        cil, cir = int(round(cx - xi)), int(round(cx + xi))
        if abs(dyn) > 0.9:
            for c in range(col, cor + 1):
                P(r, c, "=", "wheel")
        else:
            gl = "(" if abs(dyn) < 0.5 else ("/" if dyn < 0 else "\\")
            gr = ")" if abs(dyn) < 0.5 else ("\\" if dyn < 0 else "/")
            P(r, col, gl, "wheel")
            P(r, cor, gr, "wheel")
            for c in range(col + 1, cil + 1):
                P(r, c, ";", "wheel")
            for c in range(cir, cor):
                P(r, c, ";", "wheel")
    P(int(cy), int(cx) - 1, "(o)", "wheel")


wheel(7.0)
wheel(39.0)

# ------------------------------------------------- 3. pillars + car body
PM(4, 8, "(==)", "pillar")
PM(4, 13, "(==)", "pillar")
for r in range(5, 20):
    PM(r, 9, "||", "pillar")
    PM(r, 14, "||", "pillar")
# the car front rail (russet), sphinx wings will overlap it
PB(20, 13, "=====================", "pillar")
PB(21, 14, "===================", "pillar")

# ------------------------------------------------- 4. the starry canopy
# deep blue, scalloped, white squiggle (ABRACADABRA) trim
for c in range(7, 40):
    if c % 3 == 1:
        P(0, c, "wsc~"[(c // 3) % 4], "squig")
    else:
        P(0, c, ";:"[(c * 7) % 2], "canopy")
for c in range(4, 43):
    P(1, c, ";" if (c * 5 + 1) % 4 else ":", "canopy")
for c in range(1, 46):
    P(2, c, ";" if (c * 3 + 2) % 4 else ":", "canopy")
for c in range(1, 46):
    k = (c - 1) % 4
    if k == 0:
        P(3, c, "U", "canopy")
    elif k == 2:
        P(3, c, "w" if (c // 4) % 2 else "s", "squig")
    else:
        P(3, c, "‾", "canopy")
# side drops of the canopy, swooping low at the edges
PMB(4, 1, ";;;U‾U", "canopy")
PMB(5, 2, ";U‾", "canopy")
PM(4, 4, "w", "squig")
PM(5, 3, "s", "squig")

# ------------------------------------------------- 5. the amber dais
for c in range(W):
    P(29, c, "=_,="[(c + 1) % 4], "dais")
    P(30, c, ";=·="[(c * 3) % 4], "dais")
    P(31, c, "=;=·"[(c * 5 + 2) % 4], "dais")

# ------------------------------------------------- 6. the four sphinxes
# counterchanged Kerubs: dark bull L, two pale center, dark winged R
# -- dark bull-sphinx, far left, standing on the dais
PB(21, 4, "v,‾‾‾,v", "sphinxd")
PB(22, 4, "(%o·o%)", "sphinxd")
PB(23, 3, ",&%%%&,\\", "sphinxd")
PB(24, 2, "(%%;%%%%)\\", "sphinxd")
PB(25, 2, "(%;%%;%%%)", "sphinxd")
PB(26, 2, "|%%;%%;%%|", "sphinxd")
PB(27, 2, "|%;%%;%%;|", "sphinxd")
PB(28, 2, "(%%(%%%,%)", "sphinxd")
PB(29, 3, "U%U  U%U", "sphinxd")
# -- pale sphinx pair, center, wings up, frontal faces (mirrored, 8-wide
#    sprites ending at col 22 so the mirror never crosses the axis)
PMB(21, 15, "  \\,  ,/", "sphinxl")
PMB(22, 15, " \\:(··)/", "sphinxl")
PMB(23, 15, " |(;;)'|", "sphinxl")
PMB(24, 15, "(:|''|:)", "sphinxl")
PMB(25, 15, "  '|::|'", "sphinxl")
PMB(26, 15, "  ,|':|,", "sphinxl")
PMB(27, 15, " (:|::|)", "sphinxl")
PMB(28, 15, "|:|'.|:|", "sphinxl")
PMB(29, 15, "U:U  U:U", "sphinxl")
# -- dark winged sphinx, far right (great folded wing)
PB(20, 40, ",^,", "sphinxd")
PB(21, 37, ",&\\\\(´·)", "sphinxd")
PB(22, 36, "(&&\\\\(;;)", "sphinxd")
PB(23, 35, "(%&&\\\\;%)", "sphinxd")
PB(24, 35, "|%&&&\\%%|", "sphinxd")
PB(25, 35, "|%%&&%%;%|", "sphinxd")
PB(26, 35, "(%%;%%;%%)", "sphinxd")
PB(27, 35, "|%;%%;%%;|", "sphinxd")
PB(28, 35, "(%%(%%,%%)", "sphinxd")
PB(29, 36, "U%U  U%U", "sphinxd")

# ------------------------------------------------- 7. the armoured King
# One lit amber MASS, drawn ON TOP with a one-cell halo punch.
# Per-row half-widths from the scan: shoulders r6-8, chest, elbow flare
# r11-13, great rounded knees r14-18, folded shins r19, base r20.
HW = {6: 7, 7: 9, 8: 9, 9: 8, 10: 8, 11: 8, 12: 9, 13: 10,
      14: 11, 15: 11, 16: 11, 17: 11, 18: 10, 19: 9, 20: 8}
for r, hw in HW.items():
    cl, cr = 23 - hw, 23 + hw
    for c in (cl - 1, cr + 1):                    # halo punch
        if 0 <= c < W:
            canvas[r][c] = " "
            classes[r][c] = None
    for c in range(cl, cr + 1):
        if c == cl:
            ch = "," if r == 6 else ("`" if r >= 19 else "(")
        elif c == cr:
            ch = "," if r == 6 else ("´" if r >= 19 else ")")
        else:
            h = (r * 37 + c * 59 + (r * c) % 13) % 12
            dx = abs(c - 23)
            bright = ((8 <= r <= 10 and dx <= 4) or
                      (13 <= r <= 14 and 5 <= dx <= 9))
            if r in (7, 11) and 2 <= dx:
                ch = "=" if h < 7 else ";"          # plate seams
            elif 9 <= r <= 12 and dx == 6:
                ch = "(" if c < 23 else ")"        # arm seam
            elif bright and h < 3:
                ch = "'"
            else:
                ch = ";" if h < 10 else ":"
        canvas[r][c] = ch
        classes[r][c] = "armour"
# helmet: crown r3, lowered visor r4-5, chin over the gorget r6
C(3, " ,c;;;c, ", "armour")
PB(4, 19, " (", "armour"); P(4, 21, "=====", "visor"); PB(4, 26, ") ", "armour")
PB(5, 19, " (", "armour"); P(5, 21, "‾=‾=‾", "visor"); PB(5, 26, ") ", "armour")
C(6, "`=;=´", "armour")
# the grey crab crest, claws up, in front of the canopy dip
C(1, " ,c\\¡/c, ", "crab")
C(2, " ´(;o;)` ", "crab")
# the scarlet cloak falling at the pauldron edges (passion over purity)
for rr in (7, 8, 9, 10):
    PM(rr, 13, "(", "wheel")
# ten Stars of Assiah: rosette studs on the amber
for rr, cc in [(7, 17), (7, 29), (8, 15), (8, 31), (9, 20), (9, 26),
               (10, 17), (10, 29), (14, 13), (14, 33)]:
    if classes[rr][cc] == "armour":
        P(rr, cc, "*", "rosette")

# ------------------------------------------------- 8. the Holy Grail
# blue outer ring, watery moire, red radiant core — the card's heart
GR, GC = 15.0, 23.0


def grail_d(r, c):
    return math.hypot(c - GC, 1.9 * (r - GR))


for r in range(H):
    for c in range(W):
        d = grail_d(r, c)
        if d > 8.7:
            continue
        canvas[r][c] = " "          # halo punch
        classes[r][c] = None
        dx, dyv = c - GC, 1.9 * (r - GR)
        if 5.6 <= d <= 8.0:
            if d < 7.0:
                ch = ";"                            # inner rim, solid blue
            elif dyv < -5.6:
                ch = "-"
            elif dyv > 5.6:
                ch = "_"
            elif abs(dx) > 5.6:
                ch = "(" if dx < 0 else ")"
            else:
                ch = "\\" if dx * dyv > 0 else "/"
            P(r, c, ch, "ring")
        elif 4.2 <= d < 5.6:
            if 4.9 <= d <= 5.3 and (r + c) % 2:
                P(r, c, "~", "ring")
            elif (r * 31 + c * 17) % 100 < 30:
                P(r, c, "·'"[(r + c) % 2], "glow")
        elif d < 4.2:
            if d < 2.2:
                P(r, c, "@", "core")
            else:
                a = math.atan2(dyv, dx) % (2 * math.pi)
                k = a % (math.pi / 4)
                if k < 0.26 or k > (math.pi / 4 - 0.26):
                    sl = abs(math.tan(a)) if abs(math.cos(a)) > 1e-6 else 9
                    ch = "-" if sl < 0.5 else ("|" if sl > 2 else
                                              ("\\" if math.sin(2 * a) > 0 else "/"))
                    P(r, c, ch, "core")
                elif (r * 13 + c * 7) % 100 < 55:
                    P(r, c, ";:*"[(r + c) % 3], "core")
# scrolled handles at the rim sides
PMB(15, 14, "c", "ring")
PMB(16, 14, "c", "ring")
# pale hands cradling the cup from beneath
PMB(17, 14, " ,cc(, ", "hands")
PMB(18, 16, " (,,,´ ", "hands")

# ------------------------------------------------- sig
P(31, 2, "aw", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "07-chariot-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "07-chariot-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
