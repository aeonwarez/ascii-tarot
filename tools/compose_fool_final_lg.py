#!/usr/bin/env python3
"""Fool FINAL — ultracode-panel synthesis (judges voted v3c 3-0; merged).

Base: v3c mandala field (concentric dithered bands, warm vy core -> vo ->
vb -> vr -> vv rim, spiral twist, pale ring hoops, creatures in orbit,
Nile water strip). Grafts per the judge panel: v3a's large ecstatic figure
(horned gold face thrown back, open singing mouth, thick arms, 4-wide
thighs) redrawn with halo-punched sprites instead of v3a's black-arch
CLEAR; v3b's cleaner dove + coin heap. Fixes: warmer/wider vy core, denser
vr/vv outer bands (no black pockets in corners or the bottom third),
fuller between-legs calm zone, face verified dead on col 23.

Emits:
  drafts/00-fool-final-art-lg.txt       47x32 art, full-bleed
  drafts/00-fool-final-lg-classes.json  per-cell color classes (art coords)
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
    """Place including spaces (spaces punch a 1-cell breathing halo)."""
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


# ---------------------------------------------------------------- vortex
# Mandala field about the winged sun at the groin (r13, c23), cell aspect
# 1:2 baked in, gentle spiral twist. Warm core widened + outer bands
# densified per the judge panel.
CY, CX = 13.0, 23.0
SWIRL = 3.0
EDGES = [10.5, 16.0, 21.0, 26.0]         # vy | vo | vb | vr | vv
BANDS = [
    ("vy", 99, "*'*'"),                   # bright warm core
    ("vo", 96, ";'*:"),
    ("vb", 92, ";:·'"),
    ("vr", 92, ";,;:"),
    ("vv", 92, ";··:"),
]
WATER_TOP = 28


def field(r, c):
    dx = c - CX
    dy = 2.0 * (r - CY)
    d = math.hypot(dx, dy)
    th = math.atan2(dy, dx) % (2 * math.pi)
    return d + SWIRL * th / (2 * math.pi)


def calm(r, c):
    """Quieter zone between the legs so the blossom reads clean."""
    return 14 <= r <= 22 and 18 <= c <= 28


for r in range(H):
    for c in range(W):
        if r >= WATER_TOP:
            continue
        d = field(r, c)
        bi = 0
        while bi < len(EDGES) and d >= EDGES[bi]:
            bi += 1
        cls, cov, ramp = BANDS[bi]
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if calm(r, c):
            if h >= 45:
                continue
            P(r, c, "'·'·"[h % 4], cls)
            continue
        # rim lighting: each band glows along its inner edge
        inner = EDGES[bi - 1] if bi else 0.0
        outer = EDGES[bi] if bi < len(EDGES) else 34.0
        t = (d - inner) / (outer - inner)
        if t < 0.28:
            cov += 6
        if h >= cov:
            continue
        if bi <= 1 and (r * 11 + c * 7) % 29 == 0:
            P(r, c, '"', "dew")
            continue
        ch = ramp[0] if t < 0.28 else ramp[h % len(ramp)]
        P(r, c, ch, cls)


# pale ring hoops riding the band boundaries (the Harris prismatic rings)
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


ring(13.0, 23.0, 11.8, 23.5, "ring0")
ring(13.0, 23.0, 9.2, 18.5, "ring0")
ring(13.0, 23.0, 6.2, 12.6, "ring1")

# ---------------------------------------------------------------- water
for r in range(WATER_TOP, H):
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
PB(3, 37, " ,o,o, ", "grapes")
PB(4, 36, " (o,o,o) ", "grapes")
PB(5, 37, " `o`o´ ", "grapes")

# ---------------------------------------------------------------- coins
# v3b's tight heap (judge graft), mid-right
PB(8, 39, " ,-,-, ", "coins")
PB(9, 38, " (o(o(o) ", "coins")
PB(10, 38, " (o(o(o) ", "coins")
PB(11, 39, " `-`-´ ", "coins")

# ---------------------------------------------------------------- dove
# v3b's form (judge graft), rising by the open left hand
PB(2, 7, " __ ", "dove")
PB(3, 6, " <(´\\_ ", "dove")

# ---------------------------------------------------------------- butterfly
PB(11, 3, " }v{ ", "fly")

# ---------------------------------------------------------------- figure
# v3a's large ecstatic figure, halo-punched (no black-arch CLEAR).
# head: gold horned face thrown back, pale cone between the horns
PB(0, 15, " ,´ ", "gold")
PB(0, 21, " /¡\\ ", "flower")            # cone tip
PB(0, 28, " `, ", "gold")
PB(1, 17, " (` ", "gold")
PB(1, 20, " /;·;\\ ", "flower")          # pale cone
PB(1, 26, " ´) ", "gold")
PB(2, 19, " (´o·o`) ", "gold")           # wide staring eyes
PB(3, 20, " `,O,´ ", "gold")             # mouth open, singing
PB(4, 21, " \\_/ ", "gold")              # jaw seen from below
# open hands, fingers spread, flung wide + high
PB(1, 9, " \\¡/ ", "fool")
PB(1, 33, " \\¡/ ", "fool")
# arms sweeping down-in from the hands to the shoulders
PB(2, 9, " `=,  ", "fool")
PB(3, 11, " `==,  ", "fool")
PB(4, 14, " `==,_ ", "fool")
PB(2, 33, "  ,=´ ", "fool")
PB(3, 30, "  ,==´ ", "fool")
PB(4, 26, " _,==´ ", "fool")
# torso: green, dithered, broad chest -> pinch waist -> hips
PB(5, 19, " |;;;;;| ", "fool")
PB(6, 19, " (;;;;;) ", "fool")
PB(7, 19, " (;;;;;) ", "fool")
PB(8, 19, "  );;;(  ", "fool")
PB(9, 19, " (;;;;;) ", "fool")
PB(10, 19, " (;;;;;) ", "fool")
PB(11, 18, " (;;;;;;;) ", "fool")
PB(12, 18, " (;;;;;;;) ", "fool")
# the golden winged sun at the groin (0 = All)
PB(13, 17, " (;", "fool")
P(13, 20, "<=", "gold")
P(13, 22, "(o)", "sun")
P(13, 25, "=>", "gold")
PB(13, 27, ";) ", "fool")
# legs: wide ecstatic leap, 4-wide thighs -> tapering, tip-toe
PB(14, 15, " /;;; ", "fool"); PB(14, 26, " ;;;\\ ", "fool")
PB(15, 14, " /;;; ", "fool"); PB(15, 27, " ;;;\\ ", "fool")
PB(16, 13, " /;;; ", "fool"); PB(16, 28, " ;;;\\ ", "fool")
PB(17, 12, " /;;; ", "fool"); PB(17, 29, " ;;;\\ ", "fool")
PB(18, 11, " /;;; ", "fool"); PB(18, 30, " ;;;\\ ", "fool")
PB(19, 10, " /;; ", "fool"); PB(19, 32, " ;;\\ ", "fool")
PB(20, 9, " /;; ", "fool"); PB(20, 33, " ;;\\ ", "fool")
PB(21, 8, " /; ", "fool"); PB(21, 35, " ;\\ ", "fool")
PB(22, 7, " ;/ ", "fool"); PB(22, 36, " \\; ", "fool")
# golden shoes, on point, toes out
PB(23, 4, " ,==´ ", "gold")
PB(23, 37, " `==, ", "gold")
# the blossom dangling below the sun, between the legs
PB(15, 22, " ¡ ", "flower")
PB(16, 22, " ¡ ", "flower")
PB(17, 21, " ,*, ", "flower")

# ---------------------------------------------------------------- tiger
# drawn AFTER the figure: mouth at the right thigh, never slicing it
PB(14, 33, " ,-,_ ", "tiger")
PB(15, 32, " <´o)=), ", "tiger")
PB(16, 33, " (;==;=( ", "tiger")
PB(17, 34, " );==;) ", "tiger")
PB(18, 35, " ´U´ U´ ", "tiger")

# ---------------------------------------------------------------- sig
P(30, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "00-fool-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "00-fool-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
