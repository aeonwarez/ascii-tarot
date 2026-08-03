#!/usr/bin/env python3
"""Atu VII The Chariot — panel candidate v3c (vehicle-symmetry dominant).

The shrine-on-wheels as a symmetric whole: deep-blue scalloped starry canopy
with white squiggle trim, four russet pillars, two great scarlet spoked
wheels flanking, four counterchanged sphinxes (two dark outer, two light
inner) on an amber dais — framing a smaller amber-armoured King throned
frontal at perfect rest, the glowing Grail (blue ring, red radiant core)
cradled at his lap on the axis. Nimbus-ring swirl field full-bleed behind.

Emits:
  drafts/07-chariot-v3c-art-lg.txt       47x32 art
  drafts/07-chariot-v3c-lg-classes.json  per-cell class grid
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


# ------------------------------------------------------------- nimbus field
# Concentric swirl rings about the Grail heart (r14, c23), 1:2 cells baked.
CY, CX = 14.0, 23.0
EDGES = [7.0, 11.5, 16.0, 20.5, 25.0, 29.5, 34.0]


def field_d(r, c):
    return math.hypot(c - CX, 2.0 * (r - CY))


for r in range(H):
    for c in range(W):
        d = field_d(r, c)
        bi = 0
        while bi < len(EDGES) and d >= EDGES[bi]:
            bi += 1
        pale = bi % 2 == 0
        cls = "field" if pale else "swirl"
        ramp = "·'·:" if pale else ";:;,"
        cov = 50 if pale else 68
        inner = EDGES[bi - 1] if bi else 0.0
        outer = EDGES[bi] if bi < len(EDGES) else 40.0
        t = (d - inner) / (outer - inner)
        if t < 0.25:
            cov += 8
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if h >= cov:
            continue
        ch = ramp[0] if t < 0.25 else ramp[h % len(ramp)]
        P(r, c, ch, cls)


def ring(cy, cx, ry, rx, cls):
    """Pale hoop riding a band boundary."""
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


ring(14.0, 23.0, 12.5, 25.0, "glow")

# ------------------------------------------------------------------- dais
# Amber perspective platform, swirl kept in the low corners.
DAIS = {27: (10, 36), 28: (8, 38), 29: (5, 41), 30: (2, 44), 31: (0, 46)}
for r, (c0, c1) in DAIS.items():
    for c in range(c0, c1 + 1):
        h = (r * 31 + c * 17) % 100
        if r == 27:
            ch = "="
        elif r == 29:
            ch = "=" if h < 60 else ";"
        else:
            ch = ";" if h < 55 else (":" if h < 85 else ",")
        P(r, c, ch, "dais")

# ------------------------------------------------------------------ wheels
# Two great scarlet spoked wheels, tall ellipses like the scan.
WRY, WRX = 6.5, 7.0


def wheel(cy, cx):
    # spokes
    for k in range(12):
        a = math.radians(k * 30)
        for tt in (0.3, 0.45, 0.6, 0.75, 0.88):
            rr = int(round(cy + WRY * tt * math.sin(a)))
            cc = int(round(cx + WRX * tt * math.cos(a)))
            deg = k * 30 % 180
            if deg < 25 or deg > 155:
                g = "-"
            elif 65 < deg < 115:
                g = "|"
            else:
                g = "\\" if (0 < k * 30 < 90 or 180 < k * 30 < 270) else "/"
            P(rr, cc, g, "wheel")
    # rim
    for r in range(H):
        dyn = (r - cy) / WRY
        s = 1 - dyn * dyn
        if s < 0:
            continue
        x = WRX * math.sqrt(s)
        cl, cr = int(round(cx - x)), int(round(cx + x))
        if abs(dyn) > 0.9:
            ch = "-" if dyn < 0 else "_"
            for c in range(cl, cr + 1):
                P(r, c, ch, "wheel")
        elif abs(dyn) > 0.5:
            P(r, cl, "/" if dyn < 0 else "\\", "wheel")
            P(r, cr, "\\" if dyn < 0 else "/", "wheel")
        else:
            P(r, cl, "(", "wheel")
            P(r, cr, ")", "wheel")
    P(int(cy), int(cx) - 1, "(o)", "wheel")


wheel(13.0, 7.0)
wheel(13.0, 39.0)

# ----------------------------------------------------------------- pillars
# Four russet pillars, canopy to car: outer pair crossing the wheels.
for r in range(3, 19):
    PM(r, 9, "(|", "pillar")     # outer  L 9-10   R 36-37
    PM(r, 14, "(|", "pillar")    # inner  L 14-15  R 31-32
# ------------------------------------------------------------------ canopy
# Deep-blue scalloped canopy, white squiggle trim, starry.
for r in range(3):
    for c in range(2, 45):
        h = (r * 53 + c * 29) % 100
        P(r, c, ";" if h < 55 else ":", "canopy")
# stars in the blue
for r, c in [(0, 8), (0, 30), (1, 12), (0, 38), (1, 35), (0, 17)]:
    P(r, c, "*", "squig")
# white squiggle band (the ABRACADABRA thread)
for c in range(3, 44):
    P(1, c, "~~s~~w"[c % 6], "squig")
# scalloped hanging hem
for c in range(2, 45, 3):
    P(2, c, "U", "canopy")
    P(2, c + 1, "´", "canopy")
# side droops falling past the canopy hem
PMB(3, 2, "(;;\\_ ", "canopy")
PMB(4, 2, "`;;\\ ", "canopy")

# ---------------------------------------------------------------- sphinxes
# Four counterchanged Kerubic sphinxes: dark bull L, two light inner, dark
# lioness-eagle R. Drawn over the wheel bottoms, paws on the dais.
# inner light pair (mirrored about the axis)
PMB(19, 12, " \\\\,  ,// ", "sphinxl")
PMB(20, 12, " (\\,-·-,/) ", "sphinxl")
PMB(21, 12, "  |(´:`)|  ", "sphinxl")
PMB(22, 12, "  ((;:;))  ", "sphinxl")
PMB(23, 12, "  |(:::)|  ", "sphinxl")
PMB(24, 12, "  ,(:::),  ", "sphinxl")
PMB(25, 12, "  (:,:,:)  ", "sphinxl")
PMB(26, 12, "   U´ `U   ", "sphinxl")
# dark bull-sphinx, far left
PB(19, 1, "  ,v,  ", "sphinxd")
PB(20, 1, " ,(o&)_  ", "sphinxd")
PB(21, 1, " (&(%&&\\  ", "sphinxd")
PB(22, 1, " <´&%&%&) ", "sphinxd")
PB(23, 1, "  (&&%&&| ", "sphinxd")
PB(24, 1, "  |%&&%&) ", "sphinxd")
PB(25, 1, "  (&&,&&( ", "sphinxd")
PB(26, 1, "  U´  `U  ", "sphinxd")
# dark winged sphinx, far right
PB(19, 37, "  ,^&,  ", "sphinxd")
PB(20, 36, " ,&&&o`) ", "sphinxd")
PB(21, 35, " /&%&&&&( ", "sphinxd")
PB(22, 35, " (&&%&%&&> ", "sphinxd")
PB(23, 36, " |&&%&&&) ", "sphinxd")
PB(24, 36, " (&%&&&| ", "sphinxd")
PB(25, 36, " (&&,&&) ", "sphinxd")
PB(26, 37, " U´  `U ", "sphinxd")

# ------------------------------------------------------------------ figure
# The King, throned frontal on col 23 — smaller than the shrine around him,
# but a DENSE amber mass, halo-punched clear of the field.
# crab crest (Cancer) atop the canopy dip / helmet
PB(1, 19, " `\\(¡)/´ ", "crab")
PB(2, 19, " <(o·o)> ", "crab")
# helmet, visor lowered
PB(3, 19, " ,;===;, ", "armour")
PB(4, 18, " (;", "armour")
P(4, 21, "[===]", "visor")
PB(4, 26, ";)  ", "armour")
PB(5, 19, " `-;=;-´ ", "armour")
# pauldrons + gorget — massive, rounded
PB(6, 14, " ,==o==,", "armour")
PB(6, 25, ",==o==, ", "armour")
P(6, 22, "-;-", "armour")
PB(7, 14, " (;;;;;;)", "armour")
PB(7, 24, "(;;;;;;) ", "armour")
P(7, 23, ";", "armour")
# torso with arms at the sides, solid amber
for r in range(8, 12):
    PMB(r, 15, " |;|(;;;", "armour")
    P(r, 23, ";", "armour")
# forearms turning inward to the cup
PMB(12, 14, " \\;\\;;;;", "armour")
P(12, 23, ";", "armour")
# rosette studs (ten sapphire stars on the amber)
for r, c in [(8, 21), (8, 25), (9, 22), (9, 24), (10, 20), (10, 26),
             (11, 21), (11, 25), (7, 18), (7, 28)]:
    P(r, c, "*", "rosette")
# folded lap / knees, wide and low
PMB(16, 13, ",=(;;;;;;;", "armour")
P(16, 23, ";", "armour")
PMB(17, 12, "(;;;;;;;;;;", "armour")
P(17, 23, ";", "armour")
PMB(18, 13, "`-;;;;;;;;", "armour")
P(18, 23, ";", "armour")
# the Moon he rides, implied at the base of the car
P(19, 19, "`~-,_,-~´", "crab")

# ------------------------------------------------------------------- grail
# The heart: punched clean, blue ring, pale glow, red radiant core.
for r in range(12, 17):
    PB(r, 16, " " * 15, "ring")
P(12, 19, "_,-===-,_", "ring")
P(13, 17, "(;", "ring")
P(13, 19, "·'", "glow")
P(13, 21, "`\\¡/´", "core")
P(13, 26, "'·", "glow")
P(13, 28, ";)", "ring")
P(14, 16, "((;", "ring")
P(14, 19, "·", "glow")
P(14, 20, "=<(@)>=", "core")
P(14, 27, "·", "glow")
P(14, 28, ";))", "ring")
P(15, 17, "(;", "ring")
P(15, 19, ",·", "glow")
P(15, 21, ",/¡\\,", "core")
P(15, 26, "·,", "glow")
P(15, 28, ";)", "ring")
P(16, 19, "`-,===,-´", "ring")
# radiance sparks in the punched halo
for r, c in [(12, 17), (12, 29), (16, 17), (16, 29)]:
    P(r, c, "·", "glow")
# pale hands cupping the bowl
PMB(15, 14, ",c(", "hands")
PMB(16, 15, "`(", "hands")

# --------------------------------------------------------------------- sig
P(30, 2, "aw", "sig")

# -------------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "07-chariot-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "07-chariot-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
