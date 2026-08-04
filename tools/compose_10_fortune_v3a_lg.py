#!/usr/bin/env python3
"""Atu X Fortune — panel candidate v3a (strategy A: WHEEL DOMINANT).

The great ten-spoked wheel is the hero structure: a clean 2:1-wide golden
ellipse rim (hub dead on col 23, rayed sun) with ten even spokes, the purple
apex-up triangle behind it holding the motionless axle. The three riders read
as attributes on the rim: bright-gold Sphinx crowning the summit with the
sword upright between its paws; cool grey-gold Hermanubis (blue-grey plated
back) ascending the LEFT outside the rim, gripping it hand and foot; warm
red-gold croc-headed Typhon falling head-down on the RIGHT, struck by
lightnings. Above, a firmament of great gold stars mixed with blue ones; the
whole set in a blue-violet whirlpool of plume bands; Kaph's six-rayed fist
turns the wheel from below.

Emits:
  drafts/10-fortune-v3a-art-lg.txt       47x32 art
  drafts/10-fortune-v3a-lg-classes.json  per-cell class grid
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


# ------------------------------------------------------------- wheel geometry
# Hub dead on the axis; rim a 2:1-wide ellipse (cells are 1:2).
HUBR, HUBC = 16.0, 23.0
RX, RY = 14.0, 7.0          # rim spans cols 9..37, rows 9..23


def rho(r, c):
    dx = (c - HUBC) / RX
    dy = (r - HUBR) / RY
    return math.hypot(dx, dy)


STAR_H = 5                   # rows 0..4 = firmament band

# ------------------------------------------------------------- plume whirlpool
# Spiral arms of plume / field / dusk winding about the hub, drawn out by the
# spin; interior of the wheel kept calm so the spokes read.
for r in range(STAR_H, H):
    for c in range(W):
        dx = c - HUBC
        dy = 2.0 * (r - HUBR)
        d = math.hypot(dx, dy)
        th = math.atan2(dy, dx) % (2 * math.pi)
        p = (d - 7.0 * th / (2 * math.pi)) % 7.0
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        q = rho(r, c)
        if q < 0.82:
            if h < 15:
                P(r, c, "·", "dusk")
            continue
        if p < 2.8:
            if h < 88:
                P(r, c, "~~´~,~"[h % 6] if p > 0.5 else "~", "plume")
        elif p < 5.2:
            if h < 66:
                P(r, c, ";:·'"[h % 4], "field")
        else:
            if h < 52:
                P(r, c, "·,;."[h % 4], "dusk")

# ------------------------------------------------------------- triangle (tri)
# Great apex-up triangle behind the wheel, the hub in its center. Drawn only
# where it clears the rim; the wheel and riders occlude the rest.
TA_R, TA_C = 5.0, 23.0        # apex
TB_R = 27.0                   # base row
TB_HALF = 21.0
for r in range(6, int(TB_R)):
    t = (r - TA_R) / (TB_R - TA_R)
    xo = TB_HALF * t
    for cc, ch in ((TA_C - xo, "/"), (TA_C + xo, "\\")):
        ci = int(round(cc))
        if 0 <= ci < W and (rho(r, ci) > 1.03 or rho(r, ci) < 0.80):
            P(r, ci, ch, "tri")
for c in range(2, 45):
    if rho(27, c) > 1.03:
        P(27, c, "_", "tri")

# ------------------------------------------------------------- lightnings
# A curtain of orange bolts lancing down from the star band; the right-hand
# ones strike the falling Typhon. Kept outside the rim (the wheel occludes).
def bolt(pts):
    for i in range(len(pts) - 1):
        (r0, c0), (r1, c1) = pts[i], pts[i + 1]
        steps = max(abs(r1 - r0), abs(c1 - c0), 1)
        for k in range(steps + 1):
            r = int(round(r0 + (r1 - r0) * k / steps))
            c = int(round(c0 + (c1 - c0) * k / steps))
            if not (0 <= r < H and 0 <= c < W) or rho(r, c) < 1.06:
                continue
            dc = c1 - c0
            g = "|" if dc == 0 else ("\\" if dc > 0 else "/")
            if k == steps and i == len(pts) - 2:
                g = "v"
            P(r, c, g, "bolt")


bolt([(5, 3), (9, 1), (14, 3), (19, 1), (24, 3), (29, 1)])
bolt([(5, 8), (8, 6), (10, 8)])
bolt([(5, 15), (8, 17), (11, 15)])
bolt([(20, 5), (24, 7), (28, 5), (31, 7)])
bolt([(5, 31), (8, 29), (11, 31)])
bolt([(5, 36), (8, 38), (11, 36)])
bolt([(5, 41), (9, 44), (13, 45)])
bolt([(5, 44), (10, 46), (15, 44), (20, 46), (25, 44), (29, 42)])
bolt([(23, 39), (27, 41), (31, 39)])
bolt([(24, 14), (28, 12), (31, 14)])
bolt([(25, 27), (28, 29), (31, 27)])

# ------------------------------------------------------------- the firmament
# rows 0..3: great gold stars mixed with blue, on star-dust; row 4: fringe.
for r in range(0, STAR_H - 1):
    for c in range(W):
        h = (r * 41 + c * 23 + (r * c) % 7) % 100
        if h < 32:
            P(r, c, "·,'."[h % 4], "starsb")


def gstar(r, c):  # 5x3 great gold star, centred (r, c)
    PB(r - 1, c - 2, " \\¡/ ", "starsg")
    PB(r, c - 2, "<=*=>", "starsg")
    PB(r + 1, c - 2, " /¡\\ ", "starsg")


def bstar(r, c):  # 3x3 blue star
    PB(r - 1, c - 1, "\\¡/", "starsb")
    PB(r, c - 1, "=*=", "starsb")
    PB(r + 1, c - 1, "/¡\\", "starsb")


bstar(1, 8)
bstar(1, 38)
bstar(2, 17)
bstar(2, 29)
gstar(1, 23)
gstar(2, 11)
gstar(2, 35)
gstar(1, 3)
gstar(1, 43)
P(0, 15, "*", "starsg")
P(0, 31, "*", "starsg")
P(3, 20, "*", "starsb")
P(3, 26, "*", "starsb")
# fringe of pendant rays under the star band
for c in range(0, W):
    if c % 2 == 0:
        P(4, c, "v", "starsg")
    else:
        P(4, c, "·", "starsb")

# ------------------------------------------------------------- the wheel
# rim band: outer edge directional glyphs, inner fill dense gold
for r in range(H):
    for c in range(W):
        q = rho(r, c)
        if not (0.84 <= q <= 1.06):
            continue
        dx = c - HUBC
        dy = 2.0 * (r - HUBR)
        ang = math.atan2(-dy, dx)  # visual angle, y up
        s, co = math.sin(ang), math.cos(ang)
        if abs(s) < 0.38:
            g = "(" if co < 0 else ")"        # bold paren side-arcs
        elif q > 0.97:
            if abs(s) > 0.86:
                g = "="
            else:
                g = ("\\" if co > 0 else "/") if s > 0 else ("/" if co > 0 else "\\")
        else:
            g = "o;o:"[(r * 31 + c * 17) % 4]
        P(r, c, g, "wheel")

# ten even spokes from the hub to the rim (deduped cells, even angles)
for k in range(10):
    th = math.radians(90 + 36 * k)
    ex, ey = RX * math.cos(th), -RY * math.sin(th)
    ratio = abs(ey) / max(abs(ex), 1e-6)
    if ratio > 1.4:
        g = "|"
    elif ratio < 0.28:
        g = "-"
    else:
        g = "\\" if (ex > 0) == (ey > 0) else "/"
    seen = set()
    for i in range(31):
        t = 0.36 + (0.80 - 0.36) * i / 30
        r = int(round(HUBR + t * ey))
        c = int(round(HUBC + t * ex))
        if (r, c) in seen:
            continue
        seen.add((r, c))
        P(r, c, g, "wheel")

# the rayed sun-hub — the axle moveth not (visual centre col 23)
PB(15, 21, " \\¡/ ", "hub")
PB(16, 20, " =(*)= ", "hub")
PB(17, 21, " /¡\\ ", "hub")

# ------------------------------------------------------ Hermanubis (L, rising)
# slender grey-gold ape climbing OUTSIDE the left rim: hand gripping the rim
# upper-left, body hugging the arc, foot on the rim lower-left, tail curling.
PB(10, 6, " ,(o´) ", "herm")
PB(11, 4, " ((·))__,(´ ", "herm")
PB(12, 1, " (;;;), ", "herm")
PB(13, 1, " (;;;;) ", "herm")
PB(14, 1, " (;;;;) ", "herm")
PB(15, 1, " (;;;;) ", "herm")
PB(16, 1, " (;;;;) ", "herm")
PB(17, 1, " );;;( ", "herm")
PB(18, 2, " (;;;, ", "herm")
PB(19, 3, " );;;)_ ", "herm")
PB(20, 5, " `);_,)´ ", "herm")
PB(21, 5, " ,(´ ", "herm")
PB(22, 4, " (_, ", "herm")
PB(23, 4, " `-c´ ", "herm")
# the plated back (blue-grey armour rows on his outer side)
for r, c, s in ((12, 3, "::"), (13, 3, "::"), (14, 3, "::"),
                (15, 3, "::"), (16, 3, "::"), (17, 3, "::")):
    P(r, c, s, "plate")

# ------------------------------------------------------- Typhon (R, falling)
# warm red-gold crocodile-headed Typhon plunging head-down OUTSIDE the right
# rim: feet up gripping the rim, body down the arc, croc snout at the bottom,
# hook + ankh in his hands.
PB(11, 30, " ,(,_ ", "typhon")
PB(12, 34, " ,(;;)_ ", "typhon")
PB(13, 37, " ,(;;), ", "typhon")
PB(14, 38, " (;;;;) ", "typhon")
PB(15, 38, " );;;;( ", "typhon")
PB(16, 38, " (;;;;) ", "typhon")
PB(17, 38, " );;;;( ", "typhon")
PB(18, 37, " (;;;;) ", "typhon")
PB(19, 36, " );;;( ", "typhon")
PB(20, 34, " (;;;,´ ", "typhon")
PB(21, 32, " _);;)´ ", "typhon")
PB(22, 32, " (;;( ", "typhon")
PB(23, 31, " );;) ", "typhon")
PB(24, 29, " ,(o;), ", "typhon")
PB(25, 25, " <;==;;)´ ", "typhon")
PB(26, 27, " ´v´v´ ", "typhon")
PB(26, 36, " (, ", "typhon")
PB(27, 34, " ,+  ´\\ ", "typhon")
# Jupiter's bolts strike the faller (stamped after him, tips at his back)
P(14, 45, "v", "bolt")
P(22, 37, "v", "bolt")

# --------------------------------------------------- Sphinx + sword (summit)
# bright-gold Sphinx couchant atop the wheel, dead on the axis; the steel
# sword upright between its lion-paws (drawn last, riding in front).
PB(4, 21, " ,¡, ", "sphinx")
PB(5, 20, " ,(;), ", "sphinx")
PB(6, 19, " ((o·o)) ", "sphinx")
PB(7, 16, " ,(;;(;;;);;), ", "sphinx")
PB(8, 15, " (;;;(;;;;;);;;) ", "sphinx")
PB(9, 16, " (;;),   ,(;;) ", "sphinx")
PB(7, 22, " ¡ ", "sword")
PB(8, 22, " | ", "sword")
P(9, 22, "=+=", "sword")

# --------------------------------------------- Kaph: the six-rayed fist below
PB(28, 21, " \\¡/ ", "hub")
PB(29, 20, " (mmm) ", "hub")
PB(30, 21, " /¡\\ ", "hub")

# ------------------------------------------------------------------ signature
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "10-fortune-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "10-fortune-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
