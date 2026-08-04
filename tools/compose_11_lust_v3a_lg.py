#!/usr/bin/env python3
"""Lust v3a — ultracode panel candidate A (strategy: RIDER DOMINANT).

Babalon astride is the hero figure: golden, reclining-ecstatic on the
Beast's back, head thrown back upper-right, immense golden hair flowing
down the right edge, raised right arm lifting the flaming Grail high on
the axis, red reins looping from her left hand. Her spine/hips pinned to
col 23; the seven-headed Beast sweeps the lower-left mass; ten rose rayed
circles scatter the deep-purple field; grey saints trampled at the base.

House style after compose_fool_final_lg.py: hash-dithered field, dense
dithered masses (never open outlines), halo-punched PB sprites on top.

Emits:
  drafts/11-lust-v3a-art-lg.txt       47x32 art, full-bleed
  drafts/11-lust-v3a-lg-classes.json  per-cell color classes (art coords)
"""
import json, os

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


# ---------------------------------------------------------------- sky strip
# Pale dawn strip behind the serpent-horn band (rows 0-2).
for r in range(0, 3):
    for c in range(W):
        h = (r * 41 + c * 29) % 100
        if h < 38:
            canvas[r][c] = "·'‾"[h % 3] if r < 2 else "-·-"[h % 3]
            classes[r][c] = "sky"

# ---------------------------------------------------------------- field
# Deep purple mottled ground, rows 3-31 (masses overwrite). Dense — the
# ground is a painted violet, not black emptiness.
for r in range(3, H):
    for c in range(W):
        h = (r * 53 + c * 31 + (r * c) % 11) % 100
        if h >= 85:
            continue
        h2 = (r * 17 + c * 7) % 100
        cls = "dusk" if h2 < 20 else "field"
        canvas[r][c] = ":;·,':;.;:"[(h + c % 3 + r % 2) % 10]
        classes[r][c] = cls

# ---------------------------------------------------------------- serpents
# Tawny serpent-horn band across the top, parted by the burst (c17-29).
for c in range(W):
    if 17 <= c <= 29:
        continue
    P(0, c, "~s‾_"[(c // 2) % 4], "serpents")
    if (c * 13 + 5) % 100 < 55:
        P(1, c, "_‾s~"[(c // 2 + 1) % 4], "serpents")
PB(1, 13, " ~s6> ", "serpents")
PB(1, 29, " <6s~ ", "serpents")

# ---------------------------------------------------------------- burst
# Teal new-Aeon light fanning from just above the Grail flame.
for r, c, ch in [
    (0, 17, "\\"), (0, 20, "'"), (0, 23, "|"), (0, 26, "'"), (0, 29, "/"),
    (1, 18, "`"), (1, 19, "\\"), (1, 21, "·"), (1, 23, "|"), (1, 25, "·"),
    (1, 27, "/"), (1, 28, "´"),
    (2, 17, "~"), (2, 19, "´"), (2, 20, "`"), (2, 26, "´"), (2, 27, "`"),
    (2, 29, "~"), (0, 21, "·"), (0, 25, "·"), (3, 17, "·"), (3, 29, "·"),
]:
    P(r, c, ch, "burst")

# ---------------------------------------------------------------- circles
# Ten luminous rose rayed circles, scattered (NOT in Tree order).
def circle_big(r, c):
    PB(r, c, " ·'· ", "circles")
    PB(r + 1, c - 1, " -(*)- ", "circles")


def circle_small(r, c):
    PB(r, c + 1, " ' ", "circles")
    PB(r + 1, c, " (*) ", "circles")


circle_big(4, 1)        # upper left, on the purple beside the mane
circle_small(3, 13)     # between cluster and burst
circle_big(5, 28)       # right of the Grail cup
circle_small(3, 35)     # above the sun-ring
circle_small(9, 43)     # right edge below the tail
circle_small(12, 18)    # between Beast and her torso
circle_small(14, 30)    # beside her left arm
circle_small(21, 24)    # below her calf
circle_big(25, 16)      # low, on the flank-side purple
# tenth circle sits ON the hair — drawn after the hair fill below.

# ---------------------------------------------------------------- beast
# Great tawny lion-serpent mass, lower left: cascading mane arcs radiating
# from the head-cluster heart (r8,c10), 1:2 cell aspect baked in.
BEAST_SPAN = {
    3: (3, 13), 4: (1, 17), 5: (0, 18), 6: (0, 18), 7: (0, 19),
    8: (0, 19), 9: (0, 19), 10: (0, 18), 11: (0, 17), 12: (0, 16),
    13: (0, 16), 14: (0, 20), 15: (0, 20), 16: (0, 19), 17: (0, 18),
    18: (0, 16), 19: (0, 16), 20: (0, 17), 21: (0, 17), 22: (0, 16),
    23: (0, 15), 24: (0, 15), 25: (0, 14), 26: (0, 14), 27: (1, 20),
    28: (1, 21), 29: (1, 21), 30: (2, 21),
}
import math
for r, (cl, cr) in BEAST_SPAN.items():
    for c in range(cl, cr + 1):
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if h >= 96:
            continue
        d = math.hypot((c - 10) * 1.0, (r - 8) * 2.0)
        k = int(d * 0.75) % 4
        if k == 0:
            ch = ")" if c >= 10 else "("
            cls = "mane"
        elif k == 2:
            ch = "s" if h % 3 else "S"
            cls = "beast"
        elif k == 3:
            ch = "%" if h < 30 else "s"
            cls = "beast"
        else:
            ch = ";" if h % 2 else "s"
            cls = "beast"
        canvas[r][c] = ch
        classes[r][c] = cls
    # silhouette: a bright mane contour along the flank edge
    if r >= 14:
        canvas[r][cr] = ")"
        classes[r][cr] = "mane"

# ---------------------------------------------------------------- paws
# Two great forepaws with heavy toes, trampling.
PB(27, 1, " ,‾,‾,‾, ", "mane")
PB(28, 1, " |o|o|o| ", "beast")
PB(29, 1, " |o|o|o| ", "beast")
PB(30, 1, " ´‾´‾´‾´ ", "mane")
PB(27, 12, " _,‾,‾,‾,_ ", "mane")
PB(28, 11, " (o|o|o|o) ", "beast")
PB(29, 11, " (o|o|o|o) ", "beast")
PB(30, 12, " ´‾´‾´‾´‾ ", "mane")

# ---------------------------------------------------------------- 7 heads
# The head-cluster upper-left: seven distinct silhouettes on the mane.
# 1. LION on top, facing right, jaw open
PB(4, 5, " ,c%&%c,_ ", "mane")
PB(5, 4, " (%%(e´‾~=< ", "beast")
PB(6, 5, " `%%%)~<´ ", "mane")
# 2. ANGEL — tiny winged face on the mane, left of the lion
PB(6, 0, " <¡> ", "face")
# 3. SAINT — crowned, bearded, the cluster's heart
PB(7, 8, " _¡_ ", "face")
PB(8, 7, " (e-e) ", "face")
PB(9, 7, " (www) ", "face")
# 4. SATYR — horned goat profile, right of the saint
PB(8, 14, " v´v ", "face")
PB(9, 14, " (e< ", "face")
# 5. POET — laurel-sprig face below the saint
PB(10, 7, " ¡e) ", "face")
# 6. MAN OF VALOUR — helmed slit-face
PB(11, 8, " [e] ", "face")
# 7. ADULTEROUS WOMAN — large calm face, lower left
PB(10, 1, " ,--, ", "face")
PB(11, 0, " (´-`) ", "face")
PB(12, 0, " (,_,) ", "face")
PB(13, 1, " `--´ ", "face")

# ---------------------------------------------------------------- tail
# Lion-serpent tail sweeping the upper right: gold sun-ringed serpent
# head biting the crescent, a thick coil running off the right edge.
PB(3, 43, " ,ss( ", "serpents")
PB(4, 41, " ,ss(‾ ", "serpents")
PB(5, 40, " ,ss( ", "serpents")
PB(5, 34, " `·\\'/·´ ", "serpents")
PB(6, 33, " =(%6e<(= ", "serpents")
PB(7, 34, " ,·/,\\·, ", "serpents")

# ---------------------------------------------------------------- hair
# Immense golden hair from her thrown-back head down the right edge.
HAIR_SPAN = {
    11: (33, 39), 12: (33, 43), 13: (34, 46), 14: (34, 46), 15: (35, 46),
    16: (35, 46), 17: (36, 46), 18: (36, 46), 19: (37, 46), 20: (37, 46),
    21: (37, 46), 22: (38, 46), 23: (38, 46), 24: (37, 46), 25: (37, 46),
    26: (36, 46), 27: (36, 46), 28: (37, 46), 29: (38, 46), 30: (40, 46),
}
for r, (cl, cr) in HAIR_SPAN.items():
    for c in range(cl, cr + 1):
        h = (r * 31 + c * 47) % 100
        if h >= 93:
            continue
        wave = int(1.5 * math.sin(r * 0.55 + c * 0.4))
        k = (c * 2 - r + wave) % 6
        ch = "(;)s;·"[k]
        canvas[r][c] = ch
        classes[r][c] = "hair"
    # bright contour strand on the inner edge of the fall of hair
    canvas[r][cl] = "("
    classes[r][cl] = "hair"

# tenth rayed circle, rose on the gold hair (as in the scan)
circle_small(18, 43)

# ---------------------------------------------------------------- saints
# Grey bloodless saints trampled at the base, group shaped like Shin.
PB(26, 20, " ,·, ", "saints")
PB(27, 19, " (-_-) ", "saints")
PB(27, 25, " ,·, ", "saints")
PB(28, 25, " (·_·) ", "saints")
PB(26, 31, " ,·, ", "saints")
PB(27, 30, " (-_-) ", "saints")
PB(29, 19, " `;,;;,;;,;´ ", "saints")
P(30, 22, ";·;", "saints")

# ---------------------------------------------------------------- babalon
# The rider, drawn ON TOP: golden, ecstatic, spine/hips on col 23.
# Dense % flesh so she pops against the stringy beast/hair texture.
# thrown-back head, pale face to the sky upper-right, chin high;
# punched halo above so the profile reads against the field
PB(9, 29, "      ", "face")
PB(10, 29, "  ,´o ", "face")
PB(11, 28, " (%%‾´ ", "face")
PB(12, 28, " (´ ", "babalon")
# torso reclining: shoulder r12 -> chest -> waist -> hips on the axis
PB(12, 24, " ,%%( ", "babalon")
PB(13, 23, " /%%%%) ", "babalon")
PB(14, 22, " /%%%´ ", "babalon")
PB(15, 20, " ,%%%%%( ", "babalon")
PB(16, 19, " (%%%%%%) ", "babalon")
PB(17, 15, " ,%%%%%%%´ ", "babalon")
# bent left leg: knee up-left, calf sweeping back down-right, pointed foot
PB(18, 13, " ,%%%´ ", "babalon")
PB(19, 13, " (%%\\ ", "babalon")
PB(20, 15, " `%%\\ ", "babalon")
PB(21, 17, " `%%\\ ", "babalon")
PB(22, 19, " `%%\\ ", "babalon")
PB(23, 21, " `%\\ ", "babalon")
PB(24, 23, " \\e´ ", "babalon")
# raised right arm: from the Grail base down to the shoulder
PB(8, 22, " \\% ", "babalon")
PB(9, 23, " \\% ", "babalon")
PB(10, 24, " \\% ", "babalon")
PB(11, 25, " \\%, ", "babalon")
# left (carnal) arm falling to the reins
P(14, 28, ")", "babalon")
P(15, 28, ")", "babalon")
P(16, 28, ")", "babalon")
P(17, 28, ")", "babalon")
P(18, 28, ")", "babalon")
PB(19, 26, " `w, ", "babalon")

# ---------------------------------------------------------------- grail
# The flaming Holy Grail, raised high — the card's light source.
P(1, 21, "'", "flame")
P(1, 25, "'", "flame")
PB(2, 20, " ,*^*, ", "flame")
PB(3, 19, " \\*@*/ ", "flame")
P(4, 15, "~", "flame")
P(4, 29, "~", "flame")
P(6, 16, "·", "flame")
P(6, 28, "·", "flame")
PB(4, 17, " (@@@@@@@) ", "grail")
PB(5, 17, " (@@@@@@@) ", "grail")
PB(6, 18, " \\@@@@@/ ", "grail")
P(7, 20, "`\\", "grail")
P(7, 22, "w", "babalon")
P(7, 23, "/´", "grail")

# ---------------------------------------------------------------- reins
# Red reins from her left hand, the long loop hanging by the flank.
P(19, 24, "-~", "reins")
P(20, 27, "(", "reins")
P(20, 29, "\\", "reins")
P(21, 27, "(", "reins")
P(21, 30, ")", "reins")
P(22, 26, "(", "reins")
P(22, 30, ")", "reins")
P(23, 26, "(", "reins")
P(23, 30, ")", "reins")
P(24, 27, "(", "reins")
P(24, 29, ")", "reins")
P(25, 28, "U", "reins")

# ---------------------------------------------------------------- sig
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "11-lust-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "11-lust-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
