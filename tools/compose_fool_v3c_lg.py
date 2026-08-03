#!/usr/bin/env python3
"""Fool v3c — mandala-balanced compositor (ultracode panel, composer C).

Strategy: the horned green figure leaps dead-center on the axis; the
rainbow vortex is a full-field MANDALA of concentric dithered color bands
(warm vy core -> vo -> vb -> vr -> vv outward, gentle spiral twist) with
pale ring arcs riding the band boundaries. Each creature sits in its own
orbital band, radially arranged: dove upper-left (vr), grapes upper-right
(vr), butterfly left (vb), coins right (vb), tiger inner lower-right at
his leg, crocodile below in the Nile water strip.

Emits:
  drafts/00-fool-v3c-art-lg.txt       47x32 art, full-bleed
  drafts/00-fool-v3c-lg-classes.json  per-cell color classes (art coords)
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]


def P(r, c, s, cls):
    for i, ch in enumerate(s):
        if ch != " " and 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls


def PB(r, c, s, cls):
    """Place including spaces (spaces punch a halo hole)."""
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


def C(r, s, cls, halo=True):
    """Center string on the axis (col 23), halo-punching by default."""
    s2 = " " + s + " " if halo else s
    (PB if halo else P)(r, AXIS - len(s2) // 2, s2, cls)


def CLEAR(r0, r1, c0, c1):
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            canvas[r][c] = " "
            classes[r][c] = None


# ---------------------------------------------------------------- vortex
# Mandala field: concentric elliptical bands about the figure's center,
# cell aspect 1:2 baked in (dy doubled), gentle spiral twist.
CY, CX = 13.0, 23.0
SWIRL = 3.0
EDGES = [9.0, 15.0, 20.5, 26.0]          # vy | vo | vb | vr | vv
BANDS = [
    ("vy", 92, "*''*"),                   # bright warm core
    ("vo", 88, ":'':"),
    ("vb", 84, ":.:·"),
    ("vr", 82, ";,;,"),
    ("vv", 78, ":··."),
]


def field(r, c):
    dx = c - CX
    dy = 2.0 * (r - CY)
    d = math.hypot(dx, dy)
    th = math.atan2(dy, dx) % (2 * math.pi)   # seam on the right horizontal
    return d + SWIRL * th / (2 * math.pi)


def calm(r, c):
    """Quiet zone between the legs so the flower + dew read clean."""
    return 11 <= r <= 21 and 17 <= c <= 29


for r in range(H):
    for c in range(W):
        d = field(r, c)
        bi = 0
        while bi < len(EDGES) and d >= EDGES[bi]:
            bi += 1
        cls, cov, ramp = BANDS[bi]
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if calm(r, c):
            if h >= 70:
                continue
            P(r, c, "'·'·"[h % 4], cls)
            continue
        # rim lighting: each band glows along its inner edge
        inner = EDGES[bi - 1] if bi else 0.0
        outer = EDGES[bi] if bi < len(EDGES) else 34.0
        t = (d - inner) / (outer - inner)
        if t < 0.28:
            cov += 8
        elif t > 0.8:
            cov -= 12
        if h >= cov:
            continue
        # dew-diamonds sparkle in the warm core bands
        if bi <= 1 and (r * 11 + c * 7) % 29 == 0:
            P(r, c, '"', "dew")
            continue
        ch = ramp[0] if t < 0.28 else ramp[h % len(ramp)]
        P(r, c, ch, cls)

# pale ring arcs riding the band boundaries (the interlocking hoops)
def ring(cy, cx, ry, rx, cls):
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


ring(13.0, 23.0, 11.8, 23.5, "ring0")     # great hoop, exits the frame
ring(13.0, 23.0, 9.2, 18.5, "ring0")      # outer hoop, vb/vr boundary
ring(13.0, 23.0, 6.2, 12.6, "ring1")      # inner hoop, vo/vb boundary

# ---------------------------------------------------------------- water
for r in range(28, H):
    for c in range(W):
        k = (c + r * 3) % 4
        ch = "~" if k == 0 else ("·" if k == 1 else ("-" if k == 2 else " "))
        canvas[r][c] = ch
        classes[r][c] = "water" if ch != " " else None

# ---------------------------------------------------------------- croc
PB(25, 9, " ,-o-,__,--,__,--,_ ", "croc")
PB(26, 6, " <~==;;;;)==;;;;)==,_´ ", "croc")
PB(27, 8, " `v´`v´  `v´`v´  `v´ ", "croc")

# ---------------------------------------------------------------- grapes
PB(3, 36, "  ,o,  ", "grapes")
PB(4, 35, " (o(o) ", "grapes")
PB(5, 34, " (o(o(o) ", "grapes")
PB(6, 35, " `o`o´ ", "grapes")

# ---------------------------------------------------------------- coins
PB(9, 39, "  ,-,  ", "coins")
PB(10, 37, " (o)(o) ", "coins")
PB(11, 36, " (o)(o)(o) ", "coins")
PB(12, 37, " (o)(o) ", "coins")
PB(13, 38, " `-´`-´ ", "coins")

# ---------------------------------------------------------------- dove
PB(3, 7, " __ ", "dove")
PB(4, 5, " <(´\\_ ", "dove")

# ---------------------------------------------------------------- butterfly
PB(12, 4, " }v{ ", "fly")

# ---------------------------------------------------------------- figure
# head: horns + cap peak + gold face
C(1, "´(  /^\\  )`", "gold")
C(2, "\\(o.o)/", "gold")
C(3, "`(~)´", "gold")
# arms flung up-out: open hands high, forearms slanting to the shoulders
PB(2, 11, " \\'/ ", "gold")
PB(2, 31, " \\'/ ", "gold")
PB(3, 13, " `_ ", "fool")
PB(3, 30, " _´ ", "fool")
PB(4, 15, " `=_ ", "fool")
PB(4, 27, " _=´ ", "fool")
# torso (green, dithered)
C(5, "/;;;;;;;\\", "fool")
C(6, "(;;;|;;;)", "fool")
C(7, "(;:;;;:;)", "fool")
C(8, "\\;;;;;/", "fool")
C(9, "(;;;;;;;)", "fool")
# winged sun at the groin
C(10, "<=(*)=>", "sun")
# flower dangling between the legs
C(11, "¡", "flower")
C(12, "¡", "flower")
PB(13, 21, " , ", "flower")
PB(13, 24, " ` ", "flower")
PB(14, 20, " * ", "flower")
PB(14, 25, " * ", "flower")
# legs: wide leaping stance, 1 col/row outward
for i in range(11):
    PB(11 + i, 19 - i, " /; ", "fool")
    PB(11 + i, 24 + i, " ;\\ ", "fool")
# golden shoes, on point
PB(22, 6, " ,==´ ", "gold")
PB(22, 35, " `==, ", "gold")

# ---------------------------------------------------------------- tiger
# drawn AFTER the figure: mouth adjacent to the right thigh, never
# slicing it. Rearing up-left, orange with = stripes.
PB(14, 32, " ,-,_ ", "tiger")
PB(15, 31, " <´o)=), ", "tiger")
PB(16, 32, " (;==;=( ", "tiger")
PB(17, 33, " );==;) ", "tiger")
PB(18, 34, " ´U´ U´ ", "tiger")

# ---------------------------------------------------------------- sig
P(30, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "00-fool-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "00-fool-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
