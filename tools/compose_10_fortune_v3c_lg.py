#!/usr/bin/env python3
"""Atu X Fortune — panel candidate v3c (strategy C: COSMOS DOMINANT).

The cosmic clock is the hero: the firmament band of great distorted
five-pointed stars (gold + blue) across the top with its pendant fringe,
orange Jupiter-lightnings lancing down the whole card and striking the
falling Typhon, and the whirlpool of blue-violet plumes drawn out by the
spin filling the field. The ten-spoked wheel (hub dead on col 23, rim a
2:1 ellipse) and the three tawny-gold riders are the mechanism within it:
bright-gold Sphinx crowning with the upright sword, cool grey-gold
Hermanubis with blue-grey back-plates rising on the left, warm red-gold
croc-headed Typhon falling head-down on the right.

Emits:
  drafts/10-fortune-v3c-art-lg.txt        47x32 art, full-bleed
  drafts/10-fortune-v3c-lg-classes.json   per-cell color classes
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
    """Place including spaces (spaces punch a 1-cell breathing halo)."""
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


# ------------------------------------------------------------- geometry
HUB_R, HUB_C = 17.0, 23.0          # the motionless axle, dead on the axis
RIM_RY, RIM_RX = 6.2, 12.2         # 2:1 wide ellipse (cells are 1:2)
BAND_H = 5                         # star firmament rows 0..4, fringe row 5


def wheel_norm(r, c, pad_x=0.0, pad_y=0.0):
    nx = (c - HUB_C) / (RIM_RX + pad_x)
    ny = (r - HUB_R) / (RIM_RY + pad_y)
    return nx * nx + ny * ny


# ------------------------------------------------- 1. whirlpool of plumes
# Spiral bands about the hub: plume (light) / field (mid) / dusk (dark),
# counter-clockwise twist. SWIRL is 2x the band period so the atan2 seam
# is invisible. Interior of the wheel thinned so the spokes read.
PERIOD = 5.0
SWIRL = 2 * PERIOD
RAMPS = {
    "plume": (97, "~s~c~;"),
    "field": (88, ";:·';~"),
    "dusk":  (72, ":.·,;."),
}
ORDER = ["plume", "field", "dusk"]

for r in range(BAND_H + 1, H):
    for c in range(W):
        dx = c - HUB_C
        dy = 2.0 * (r - HUB_R)
        d = math.hypot(dx, dy)
        th = math.atan2(dy, dx) % (2 * math.pi)
        v = d + SWIRL * th / (2 * math.pi)
        cls = ORDER[int(v / PERIOD) % 3]
        cov, ramp = RAMPS[cls]
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if wheel_norm(r, c) < 0.82:     # calm the wheel face
            if h >= 34:
                continue
            P(r, c, "·'.:"[h % 4], "dusk")
            continue
        if h >= cov:
            continue
        t = (v % PERIOD) / PERIOD
        ch = ramp[0] if (cls == "plume" and t < 0.45) else ramp[h % len(ramp)]
        P(r, c, ch, cls)

# ------------------------------------------------- 2. star firmament band
# sparse deep-blue dither behind the stars
for r in range(BAND_H):
    for c in range(W):
        h = (r * 53 + c * 31) % 100
        if h < 16:
            P(r, c, "·" if h % 2 else ":", "field")

# the great central compass-star of Nuit (gold), dead on the axis
PB(0, 19, " `,\\¡/,´ ", "starsg")
PB(1, 17, " ~==<(*)>==~ ", "starsg")
PB(2, 20, " ´/¡\\` ", "starsg")
# flanking gold five-pointed stars (distorted), mirrored
PM(1, 6, "¡", "starsg")
PM(2, 4, "`=*=´", "starsg")
PM(3, 4, "/ \\", "starsg")
# blue stars between, mirrored
PMB(2, 12, " \\¡/ ", "starsb")
PMB(3, 12, " <*> ", "starsb")
# half-stars cut by the frame edge + small sparks
PM(1, 0, "*=~", "starsg")
PM(0, 9, "*", "starsb")
PM(3, 17, "*", "starsb")
PM(4, 8, "*", "starsg")
PM(0, 15, "·", "starsb")
PM(4, 20, "'", "starsb")
# faint facet lines of the cosmic clockwork between the stars
PM(0, 5, "\\", "starsb")
PM(4, 2, "/", "starsb")
PM(4, 13, "\\", "starsb")
PM(3, 9, "'", "starsb")

# pendant fringe under the firmament (gold/blue drops on an orange rule)
for c in range(W):
    if c % 2 == 0:
        P(5, c, "v", "starsg" if (c // 2) % 2 == 0 else "starsb")
    else:
        P(5, c, "‾", "bolt")

# ------------------------------------------------- 3. the triangle behind
# apex-up, the hub in its center; skip inside the wheel so only the apex
# fragments and the lower reaches emerge (as in the painting).
def tri_line(r0, c0, r1, c1):
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = int(round(r0 + (r1 - r0) * i / steps))
        c = int(round(c0 + (c1 - c0) * i / steps))
        if wheel_norm(r, c, 0.8, 0.4) < 1.0:
            continue
        if r <= 10 and 13 <= c <= 33:   # keep the Sphinx/sword zone clean
            continue
        g = "/" if (c1 - c0) < 0 else "\\"
        P(r, c, g, "tri")


tri_line(6, 22, 29, 2)
tri_line(6, 24, 29, 44)
for c in range(3, 44, 2):
    P(29, c, "_", "tri")

# ------------------------------------------------- 4. Jupiter-lightnings
def bolt(c0, r0, r1, ph=0):
    offs = [0, 0, 1, 1, 1, 0, 0, -1, -1, -1]
    prev = None
    for i, r in enumerate(range(r0, r1 + 1)):
        cc = c0 + offs[(i + ph) % len(offs)]
        g = "|" if prev is None or cc == prev else ("\\" if cc > prev else "/")
        prev = cc
        if wheel_norm(r, cc, 1.0, 0.6) < 1.0:
            continue
        if r == r1:
            g = "v"
        P(r, cc, g, "bolt")


bolt(2, 6, 29, 0)
bolt(7, 6, 26, 4)
bolt(12, 6, 9, 6)       # short stub above the wheel's shoulder
bolt(17, 6, 28, 2)
bolt(29, 6, 28, 7)
bolt(33, 6, 25, 5)      # strikes the falling Typhon's back
bolt(39, 6, 21, 1)      # strikes the falling Typhon's flank
bolt(44, 6, 30, 3)

# ------------------------------------------------- 5. the ten-spoked wheel
# rim cells collected so they can be re-stamped over the riders' punched
# halos later (riders occlude, but the rim must stay continuous elsewhere)
def rim_cells():
    cells = []
    for r in range(11, 24):
        dyn = (r - HUB_R) / RIM_RY
        if abs(dyn) > 1:
            continue
        x = RIM_RX * math.sqrt(1 - dyn * dyn)
        cl, cr = int(round(HUB_C - x)), int(round(HUB_C + x))
        if abs(dyn) < 0.55:
            cells += [(r, cl, "("), (r, cr, ")")]
        elif abs(dyn) < 0.85:
            if dyn < 0:
                cells += [(r, cl, "/"), (r, cr, "\\")]
            else:
                cells += [(r, cl, "\\"), (r, cr, "/")]
        else:
            if dyn < 0:
                cells += [(r, cl, ","), (r, cr, ",")]
            else:
                cells += [(r, cl, "`"), (r, cr, "´")]
    for c in range(11, 36):
        dxn = (c - HUB_C) / RIM_RX
        if abs(dxn) > 1:
            continue
        y = RIM_RY * math.sqrt(1 - dxn * dxn)
        if abs(dxn) < 0.72:
            cells += [(int(round(HUB_R - y)), c, "="),
                      (int(round(HUB_R + y)), c, "=")]
    return cells


RIM = rim_cells()
for r, c, g in RIM:
    P(r, c, g, "wheel")

# ten spokes: vertical pair + 4 mirrored pairs (36 deg apart)
for k in range(10):
    th = math.radians(270 + 36 * k)
    dr, dc = math.sin(th) * RIM_RY, math.cos(th) * RIM_RX
    slope = dr / dc if abs(dc) > 1e-6 else 99.0
    if abs(slope) > 2.0:
        g = "|"
    elif abs(slope) < 0.28:
        g = "-"
    else:
        g = "\\" if slope > 0 else "/"
    t = 0.34
    while t <= 0.88:
        rr = int(round(HUB_R + t * dr))
        cc = int(round(HUB_C + t * dc))
        P(rr, cc, g, "wheel")
        t += 0.07

# the motionless axle: rayed sun-hub, dead on col 23
P(16, 22, "\\¡/", "hub")
P(17, 20, "=<(*)>=", "hub")
P(18, 22, "/¡\\", "hub")

# ------------------------------------------------- 6. Sphinx + the sword
# bright-gold couchant Sphinx crowning the summit, facing left, haunches
# right (as Harris paints her), the sword upright between the forepaws.
PB(6, 14, " ,=o=, ", "sphinx")
PB(7, 14, " (o·;) ", "sphinx")
PB(7, 24, " _,--,_ ", "sphinx")
PB(8, 13, " ,(;;);;;;;;;;;;;;,_ ", "sphinx")
PB(9, 13, " (;;;;;;;;;;;;;;;;;;) ", "sphinx")
PB(10, 16, " ,U´ ", "sphinx")
PB(10, 24, " `U, ", "sphinx")
PB(10, 28, " (;;) ", "sphinx")
PB(6, 21, "     ", "sphinx")     # calm halo so the sword tip reads
PB(7, 21, "  ", "sphinx")
PB(7, 24, " ", "sphinx")
P(6, 23, "!", "sword")
P(7, 23, "|", "sword")
P(8, 23, "|", "sword")
P(9, 22, "=+=", "sword")
P(10, 23, "¡", "sword")

# ------------------------------------------------- 7. Hermanubis (rising)
# cool grey-gold ape climbing the left rim, blue-grey plates on his back
PB(12, 5, " ,(o), ", "herm")
PB(13, 5, " (;;;,_=´ ", "herm")
PB(14, 4, " (;;;;) ", "herm")
PB(15, 4, " (;;;;) ", "herm")
PB(16, 4, " (;;;;) ", "herm")
PB(17, 5, " (;;;;) ", "herm")
PB(18, 5, " (;;;) ", "herm")
PB(19, 6, " );;,_ ", "herm")
PB(20, 7, " `;;;_,´ ", "herm")
PB(21, 6, " c,;;´ ", "herm")
PB(22, 5, " (,` ", "herm")
PB(23, 4, " `c´ ", "herm")
P(13, 3, "(=", "plate")
P(14, 2, "((=", "plate")
P(15, 2, "((=", "plate")
P(16, 2, "((=", "plate")
P(17, 3, "((=", "plate")
P(18, 4, "(=", "plate")

# ------------------------------------------------- 8. Typhon (falling)
# warm red-gold croc-headed Typhon head-down on the right, leg hooked
# over the upper rim, snout open at the bottom, ankh + hook in hand
PB(12, 29, " _,,´ ", "typhon")
PB(13, 31, " ,;;),_ ", "typhon")
PB(14, 35, " (;;;, ", "typhon")
PB(15, 36, " );;;) ", "typhon")
PB(16, 36, " (;;;;) ", "typhon")
PB(17, 37, " );;;) ", "typhon")
PB(18, 37, " (;;;;) ", "typhon")
PB(19, 37, " );;;) ", "typhon")
PB(20, 36, " ,;;;;( ", "typhon")
PB(21, 35, " /;;;;) ", "typhon")
PB(22, 35, " (;;(;( ", "typhon")
PB(23, 34, " );)`;;, ", "typhon")
PB(24, 33, " ,(;;), ", "typhon")
PB(25, 32, " (o;;( ", "typhon")
PB(26, 31, " <;==( ", "typhon")
PB(27, 30, " <_=<´ ", "typhon")
# the inverted ankh (loop below) and the long hook
P(26, 38, "+", "typhon")
P(27, 38, "o", "typhon")
P(22, 42, "c", "typhon")
P(23, 42, "\\", "typhon")
P(24, 43, "\\", "typhon")
P(25, 43, "\\", "typhon")
P(26, 44, "\\", "typhon")
P(27, 44, "\\", "typhon")
# lightning tips re-struck on his body after the halo punch
P(14, 34, "v", "bolt")
P(21, 34, "v", "bolt")
P(24, 39, "v", "bolt")

# rim re-stamp: restore rim continuity where the riders' breathing halos
# punched it, without ever overwriting an actual rider glyph
BG = (None, "field", "plume", "dusk", "tri", "bolt")
for r, c, g in RIM:
    if classes[r][c] in BG:
        P(r, c, g, "wheel")

# ------------------------------------------------- 9. signature
P(31, 2, "aw", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "10-fortune-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "10-fortune-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
