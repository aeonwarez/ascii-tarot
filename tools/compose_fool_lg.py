#!/usr/bin/env python3
"""Compositor for the large Fool card per drafts/00-fool-fable5-prompt.md,
corrected against the Harris scan (reference/00-fool-card.jpg):

The figure is the GREEN MAN (green suit, golden face/shoes, tiny gold horn
curls) in a wide tip-toe stance, arms flung up; three great pale rainbow
RINGS interlock around him on a golden dewdrop field; white dove diving
upper left, orange tiger clinging to his right leg, green crocodile along
the bottom, grapes over a pile of pale-blue coin-orbs on the right,
butterfly on the ring, gold sun disk at the groin.

Emits:
  drafts/00-fool-art-lg.txt        47x32 art, full-bleed
  drafts/00-fool-lg-classes.json   per-cell color classes (art coords)
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]


def P(r, c, s, cls):
    for i, ch in enumerate(s):
        if ch != " " and 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls


def PB(r, c, s, cls):
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


def PL(block, r0, c0, cls):
    for dr, line in enumerate(block.splitlines()):
        P(r0 + dr, c0, line, cls)


def CLEAR(r0, r1, c0, c1):
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            canvas[r][c] = " "
            classes[r][c] = None


def ellipse(cy, cx, ry, rx, cls):
    """Thin ring outline, aspect already in rx/ry, slope-aware glyphs."""
    for r in range(H):
        dyn = (r - cy) / ry
        s = 1 - dyn * dyn
        if s < 0:
            continue
        x = rx * math.sqrt(s)
        cl, cr = int(round(cx - x)), int(round(cx + x))
        if abs(dyn) > 0.93:
            ch_l, ch_r = ("-", "-") if dyn < 0 else ("_", "_")
            for c in range(cl, cr + 1, max(2, (cr - cl) // 5 or 2)):
                P(r, c, ch_l, cls)
        elif abs(dyn) > 0.55:
            P(r, cl, "/" if dyn < 0 else "\\", cls)
            P(r, cr, "\\" if dyn < 0 else "/", cls)
        else:
            P(r, cl, "(", cls)
            P(r, cr, ")", cls)


# ---- 1. the golden dewdrop field + blue sky corners ----
for r in range(H):
    for c in range(W):
        k = (r * 13 + c * 7) % 29
        if k == 0:
            P(r, c, "·", "bg")
        elif k == 11:
            P(r, c, "'", "bg")
P(0, 0, "::.", "sky"); P(1, 0, ":.", "sky"); P(2, 0, ".", "sky")
P(0, 44, ".::", "sky"); P(1, 45, ".:", "sky"); P(2, 46, ".", "sky")

# ---- 2. three great interlocking rings (pale rainbow, the vortex) ----
ellipse(14.0, 22.0, 12.5, 21.0, "ring0")
ellipse(15.0, 24.0, 10.0, 17.0, "ring1")
ellipse(11.5, 23.0, 7.0, 12.0, "ring2")

# ---- 3. grapes over the pile of coin-orbs, right side ----
CLEAR(5, 14, 38, 46)
P(5, 40, ",o,o,", "grapes")
P(6, 39, "(o,o,o)", "grapes")
P(7, 40, "`o´o´", "grapes")
P(9, 40, ",-,-,", "coins")
P(10, 39, "(o(o(o)", "coins")
P(11, 38, "(o(o(o(o)", "coins")
P(12, 39, "(o(o(o)", "coins")
P(13, 40, "`-`-´", "coins")

# ---- 4. the green man: wide tip-toe stance, arms flung up-out ----
CLEAR(2, 5, 15, 31)                      # head + arms halo
CLEAR(6, 13, 17, 29)                     # torso halo
P(2, 21, ",", "gold"); P(2, 23, "/\\", "gold"); P(2, 26, ",", "gold")
P(3, 20, "(´", "gold"); P(3, 22, "(oo)", "gold"); P(3, 26, "`)", "gold")
P(4, 21, "`(~´)´", "gold")               # curled mustache
# arms sweeping up-out from the shoulders
P(5, 20, "_/", "fool"); P(5, 25, "\\_", "fool")
P(4, 17, ",=´", "fool"); P(3, 15, ",´", "fool")
P(4, 28, "`=,", "fool"); P(3, 30, "`,", "fool")
# torso, muscled
P(6, 20, "|;;;;|", "fool")
P(7, 20, "(;;;;)", "fool")
P(8, 21, ");;(", "fool")
P(9, 20, "(;;;;)", "fool")
P(10, 20, "|;;;;|", "fool")
P(11, 20, "(;;;;;)", "fool")
# the sun disk at the groin
PB(12, 19, " .=(o)=. ", "sun")
# legs: wide stance, tip-toe
P(13, 19, "/", "fool"); P(13, 27, "\\", "fool")
P(14, 18, "/;", "fool"); P(14, 26, ";\\", "fool")
P(15, 17, "/;", "fool"); P(15, 27, ";\\", "fool")
P(16, 16, "/;", "fool"); P(16, 28, ";\\", "fool")
P(17, 15, "/;", "fool"); P(17, 29, ";\\", "fool")
P(18, 14, "/;", "fool"); P(18, 30, ";\\", "fool")
P(19, 13, "/;", "fool"); P(19, 31, ";\\", "fool")
P(20, 12, "/;", "fool"); P(20, 32, ";\\", "fool")
P(21, 11, ";/", "fool"); P(21, 33, "\\;", "fool")
P(22, 10, ";/", "fool"); P(22, 34, "\\;", "fool")
# golden shoes, on point
PB(23, 7, " ,==´ ", "gold")
PB(23, 34, " `==, ", "gold")
# twin flower dangling beneath the sun
P(14, 23, "¡", "flower"); P(15, 23, "¡", "flower")
P(16, 22, ",v,", "flower")

# ---- 5. the white dove diving, upper left ----
PB(5, 9, " __    ", "dove")
PB(6, 8, " <(´\\_ ", "dove")

# ---- 6. the butterfly riding the ring, left ----
PB(11, 4, " }v{ ", "fly")

# ---- 7. the orange tiger clinging to his right leg, mouth at the calf --
CLEAR(16, 21, 34, 44)
P(16, 36, ",,´)", "tiger")
P(17, 34, "<,o.(_", "tiger")
P(18, 36, "`==´;;`,", "tiger")
P(19, 37, ");;;;;;)", "tiger")
P(20, 36, "(;;;;;;(", "tiger")
P(21, 37, "`))´`))´", "tiger")

# ---- 8. the crocodile along the bottom ----
CLEAR(25, 27, 5, 41)
P(25, 8, ",--,___,--, ___,-o-,_", "croc")
P(26, 5, "~<=´ ;; `´ ;;; `´ ;; ,==>", "croc")
P(27, 8, "`v´`v´ `v´ `v´`v´", "croc")

# ---- 9. ring0 re-crossing IN FRONT of the crocodile (the weave) ----
for r in range(24, 27):
    dyn = (r - 14.0) / 12.5
    s = 1 - dyn * dyn
    if s >= 0:
        x = 21.0 * math.sqrt(s)
        P(r, int(round(22 - x)), "\\", "ring0")
        P(r, int(round(22 + x)), "/", "ring0")

# ---- 10. ground line + signature ----
P(28, 3, "_,.-·-.,_,.-·-.,_,.-·-.,_,.-·-.,_,.-·-.,_", "bg")
P(30, 2, "aw", "sig")

# ---- emit ----
art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "00-fool-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "00-fool-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
