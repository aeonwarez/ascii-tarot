#!/usr/bin/env python3
"""Chariot FINAL — ultracode panel synthesis (judge tally v3a 8 / v3b 7 / v3c 3).

Merge recipe (all three judges converged): v3b's chassis — the densest,
least-empty body with the best King (lit star-studded amber armour mass,
plate seams, lowered visor slit, grey crab crest on col 23, massive
pauldrons, scarlet cloak edges, (==) capped russet pillars, scalloped
squiggle-trimmed blue canopy, scarlet wheel bulk with (o) hubs, full-bleed
nimbus field) — with v3a's LARGE Grail transplanted onto the axis: the wide
2:1 multi-row ellipse, blue Oo rim (ring class, amethyst/violet — never
amber), pale moon-sea whorl, red @ radiant heart with revolving rays,
cradled in pale hands, halo-punched so the cup is the FIRST read. From v3c:
the blue crescent Moon at the car base under the Grail, and the sphinx
counterchange discipline (dark %-dithered outer pair vs light open-glyph
inner pair, paw row U%U on the amber dais). Throned at rest: no reins, no
motion, everything mirrored about col 23.

Emits:
  drafts/07-chariot-final-art-lg.txt       47x32 art
  drafts/07-chariot-final-lg-classes.json  per-cell class grid
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
# (v3b) concentric pale/blue rings, recentred on the Grail heart (r14,c23).
CY, CX = 14.0, 23.0
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


hoop(14.0, 23.0, 6.75, 13.5, "glow")
hoop(14.0, 23.0, 11.25, 22.5, "glow")
hoop(14.0, 23.0, 15.75, 31.5, "glow")

# ------------------------------------------------- 2. the scarlet wheels
# (v3b) tall spoked ellipses flanking, seen nearly edge-on as in the scan.
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
    # rim: outline + solid fill between the radial passes at the sides
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
# (v3b) russet (==) caps, continuous shafts down to the car rail.
PM(4, 8, "(==)", "pillar")
PM(4, 13, "(==)", "pillar")
for r in range(5, 20):
    PM(r, 9, "||", "pillar")
    PM(r, 14, "||", "pillar")
# the car front rail (russet); sphinx wings will overlap it
PB(20, 13, "=====================", "pillar")
PB(21, 14, "===================", "pillar")

# ------------------------------------------------- 4. the starry canopy
# (v3b) deep blue, scalloped, white squiggle (ABRACADABRA) trim
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
# (v3b sprites, v3c counterchange law: dark %-dithered outer pair, light
# open-glyph inner pair, paw row U%U on the amber dais)
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
# (v3b) one lit amber MASS, drawn ON TOP with a one-cell halo punch.
# Shoulders r6-8, chest, elbow flare r11-13, rounded knees r14-18,
# folded shins r19, base r20. The Grail will punch its center clear.
HW = {6: 7, 7: 9, 8: 9, 9: 9, 10: 9, 11: 8, 12: 9, 13: 10,
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
# ten Stars of Assiah: rosette studs on amber that survives the Grail punch
for rr, cc in [(7, 17), (7, 29), (8, 15), (8, 31), (9, 19), (9, 27),
               (10, 16), (10, 30), (16, 12), (16, 34)]:
    if classes[rr][cc] == "armour":
        P(rr, cc, "*", "rosette")

# ------------------------------------------------- 8. the Holy Grail
# (v3a transplant — the hero read) wide 2:1 ellipse dead on the axis:
# amethyst-blue Oo ring, pale moon-sea whorl, red radiant core with
# revolving rays. Halo-punched clear of the armour so it floats luminous.
GCY, GCX = 14.6, 23.0
GRX, GRY = 9.0, 4.5
for r in range(10, 20):
    for c in range(12, 35):
        ndx = (c - GCX) / GRX
        ndy = (r - GCY) / GRY
        t = math.hypot(ndx, ndy)
        if t > 1.12 or abs(ndy) > 1.0:
            continue
        canvas[r][c] = " "                # breathing halo punch
        classes[r][c] = None
        if t > 1.03:                      # 1.03: keeps the ( ) waist columns
            continue
        h = (r * 53 + c * 29) % 100
        if t > 0.90:                      # rim outline, angle-aware
            if abs(ndy) > 0.85:
                ch = "-" if r < GCY else "_"
            elif abs(ndy) > 0.5:
                ch = ("/" if r < GCY else "\\") if c < 23 else ("\\" if r < GCY else "/")
            else:
                ch = "(" if c < 23 else ")"
            P(r, c, ch, "ring")
        elif t > 0.66:                    # blue ring body — dense, luminous
            P(r, c, "Oo;O"[h % 4], "ring")
        elif t > 0.48:                    # pale moon-sea whorl — always filled
            P(r, c, "·~'·"[h % 4], "glow")
        else:                             # red radiant core — solid, rayed
            ang = math.atan2(ndy, ndx)
            k = ang / (math.pi / 4.0)
            frac = abs(k - round(k))
            if t < 0.20:
                P(r, c, "@", "core")
            elif frac < 0.20:
                P(r, c, "-\\|/"[int(round(k)) % 4], "core")
            else:
                P(r, c, "*%;*"[h % 4], "core")
# scrolled handles curling at the rim sides
PM(14, 13, ",", "ring")
PM(15, 13, "(", "ring")
PM(16, 13, "`", "ring")

# ------------------------------------------------- 9. pale hands + Moon
# hands cupped under the bowl, fingers riding up onto the blue rim
PMB(17, 13, " ,ww(", "hands")
PMB(18, 15, " `ww=,", "hands")
# (v3c graft) the blue crescent Moon he rides, at the car base
PB(19, 19, "`~-,_,-~´", "canopy")

# ------------------------------------------------- sig
P(31, 2, "aw", "sig")

# ------------------------------------------------- emit
assert len(canvas) == H and all(len(row) == W for row in canvas)
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "07-chariot-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "07-chariot-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
