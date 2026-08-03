#!/usr/bin/env python3
"""Hierophant v3c — SHRINE-SYMMETRY dominant (ultracode panel, composer C).

The whole card is the shrine: mirrored elephants flanking the throne bench,
the four Kerubs in the corners (eagle UL, angel UR, bull LL, lion LR), the
oriel window of snake/dove/rose/nine-nails behind the head, all framing a
smaller enthroned figure. Nested geometry kept legible: great hexagram about
the body, chest-pentagram holding the dancing child; Scarlet Woman with
sword + moon centered low before the dais steps.

Emits:
  drafts/05-hierophant-v3c-art-lg.txt       47x32 art, full-bleed
  drafts/05-hierophant-v3c-lg-classes.json  per-cell classes (art coords)
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23.0

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]
MIRROR = str.maketrans("()/\\[]{}<>`´,.L7", ")(\\/][}{><´`,.7L")


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


def pc(r, s, cls):
    """Place centered on the axis (odd-length strings sit dead on col 23)."""
    PB(r, 23 - len(s) // 2, s, cls)


# ------------------------------------------------------------- 1. field
# Dark indigo Nuit ground: dithered, denser toward the card edges so the
# shrine glows against the deep of night; sparse pale stars.
for r in range(H):
    for c in range(W):
        d = math.hypot(c - 23, 2.0 * (r - 12))
        cov = min(52, 26 + 0.7 * d)
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if h >= cov:
            continue
        if (r * 11 + c * 7) % 41 == 0:
            P(r, c, "*", "stars")
        else:
            P(r, c, "·,':"[h % 4], "field")

# ------------------------------------------------------------- 2. oriel
# lit-from-behind window: dense checker lattice reads as glowing glass
# (drawn first; crown/face occlude the center)
for r in range(2, 7):
    for c in range(16, 31):
        P(r, c, "·" if (r + c) % 2 else "'", "oriel")
# arch outline: crest curve with the rose set into it, heavier flanks
PM(1, 16, "_,-´(", "oriel")
PM(2, 15, "((", "oriel")
PM(3, 15, "(:", "oriel")
PM(4, 14, "(:", "oriel")
PM(5, 14, "|:", "oriel")
PM(6, 14, "|:", "oriel")
# nine nails across the top (Yesod / the Moon) — exactly nine
for c in range(15, 32, 2):
    P(0, c, "¡", "nails")
# five-petal rose in blossom, set into the arch crest
pc(1, ",*@*,", "rose")
# snake curling the left arch frame
PB(1, 12, " ~e ", "snake")
P(2, 14, "s", "snake")
P(3, 13, "s", "snake")
P(4, 12, "s", "snake")
P(5, 12, "s", "snake")
P(6, 13, "s", "snake")
# dove on the right arch frame
PB(1, 30, " __ ", "dove")
PB(2, 30, " <(´\\_ ", "dove")

# ------------------------------------------------------------- 3. throne
# bench slab the figure sits on + dais steps at the card foot
PB(14, 14, "[" + "=" * 17 + "]", "throne")
PB(26, 13, "L" + "=" * 19 + "7", "throne")
PB(27, 9, "L" + "=" * 27 + "7", "throne")

# ------------------------------------------------------------- 4. hexagram
# macrocosm about the whole seated body; over field/slab, under the figure.
# Never slice the oriel/snake/dove — skip those cells.
SACRED = {"oriel", "snake", "dove", "nails", "rose"}


def HX(r, c, ch):
    if 0 <= r < H and 0 <= c < W and classes[r][c] not in SACRED:
        P(r, c, ch, "hex")


for i in range(1, 13):                    # up triangle: apex (4,23)
    off = round(1.25 * i)
    HX(4 + i, 23 - off, "/")
    HX(4 + i, 23 + off, "\\")
for c in range(9, 38):                    # its base
    HX(16, c, "_")
for i in range(1, 13):                    # down triangle: apex (18,23)
    off = round(1.25 * i)
    HX(18 - i, 23 - off, "\\")
    HX(18 - i, 23 + off, "/")
for c in range(9, 38):                    # its base
    HX(6, c, "‾")
HX(18, 23, "v")                           # bottom star point
HX(11, 14, "X")                           # side star points (line crossings)
HX(11, 32, "X")

# ------------------------------------------------------------- 5. elephants
# Taurean elephant heads flanking the bench, mirrored about the axis:
# outer ear flap, domed brow, eye, trunk descending inward
PMB(13, 4, " _,--,_ ", "eleph")
PMB(14, 2, " ,(;;;;;;), ", "eleph")
PMB(15, 1, " ((;o;;;;;), ", "eleph")
PMB(16, 1, " ((;;;;;(;( ", "eleph")
PMB(17, 2, " `--´ (;( ", "eleph")
PMB(18, 7, " `(;´ ", "eleph")

# ------------------------------------------------------------- 6. the bull
# of Taurus beneath the seat: wide horns, brow, eyes, muzzle
PM(15, 16, ",c(", "bull")
PB(15, 19, " ;;;;;;; ", "bull")
PB(16, 19, " (o;;;o) ", "bull")
PB(17, 20, " (;·;) ", "bull")

# ------------------------------------------------------------- 7. figure
# robe block (scarlet), orange edges, olive embroidery; sloped shoulders
ROBE = {6: (18, 28), 7: (17, 29), 8: (17, 29), 9: (17, 29), 10: (17, 29),
        11: (17, 29), 12: (16, 30), 13: (15, 31)}
for r, (a, b) in ROBE.items():
    for c in range(a, b + 1):
        P(r, c, ";", "robe")
for r in range(6, 14):
    a, b = ROBE[r]
    P(r, a, "," if r == 6 else "(", "orange")
    P(r, b, "," if r == 6 else ")", "orange")
for r, (a, b) in ROBE.items():
    for c in range(a + 1, b):
        if (r * 7 + c * 11) % 9 == 0:
            P(r, c, ":", "olive")
P(6, 22, "(_)", "orange")                 # collar
# sleeves reaching to wand grip (viewer left) and blessing hand (right)
PB(7, 12, " ,;;;;", "robe")
PB(8, 10, " ,;;;", "robe")
PB(7, 30, ";;;, ", "robe")
PB(8, 33, ";;, ", "robe")
# crown of Osiris (gold, plumes flanking the cone) + face, halo-punched
PB(2, 19, " (,¡,) ", "crown")
PB(3, 19, " ((¡)) ", "crown")
PB(4, 20, " (´·`) ", "face")
PB(5, 20, " `,-´ ", "face")
# chest pentagram (pale) holding the glad dancing child (microcosm)
P(8, 23, "*", "penta")
PB(9, 18, " <´", "penta")
PB(9, 26, "`> ", "penta")
PB(10, 19, " \\ ", "penta")
PB(10, 25, " / ", "penta")
PB(11, 19, " v", "penta")
PB(11, 26, "v ", "penta")
PB(9, 21, " \\o/ ", "child")
PB(10, 22, " ¡ ", "child")
PB(11, 21, " / \\", "child")
P(11, 25, ",", "child")                   # right-foot sandal strap ("To Go")
# three-ringed wand (right hand, viewer left): scarlet / green / pale yellow
PB(3, 9, " (o) ", "ringr")
PB(4, 9, " (o) ", "ringg")
PB(5, 9, " (o) ", "ringy")
P(6, 11, "|", "wand")
P(7, 11, "|", "wand")
P(8, 11, "|", "wand")
PB(9, 9, " (¡) ", "face")
# blessing hand (left hand, viewer right): two fingers up, two down
P(8, 36, "¡", "face")
P(8, 38, "¡", "face")
PB(9, 35, " (;;) ", "face")
P(10, 36, ",", "face")
P(10, 38, ",", "face")

# ------------------------------------------------------------- 8. the woman
# Scarlet Woman, pale + militant, sword upright, crescent moon in hand
pc(19, ",(·),", "woman")
pc(20, ",(;;;),", "woman")
pc(21, "(;;;)", "woman")
pc(22, "(;;;)", "woman")
pc(23, "(;;;;;)", "woman")
pc(24, "(;;;;;)", "woman")
pc(25, "(_,_)", "woman")
P(17, 19, "¡", "sword")
P(18, 19, "|", "sword")
P(19, 19, "|", "sword")
P(20, 18, "-+-", "sword")
P(21, 19, "¡", "sword")
PB(19, 27, " ,´ ", "moon")
P(20, 27, "((", "moon")
PB(21, 27, " `, ", "moon")

# ------------------------------------------------------------- 9. Kerubs
# New-Aeon corners: eagle UL, angel UR, bull LL, lion LR
PB(0, 0, ",~,", "kerub")
PB(1, 0, "((o>", "kerub")
PB(2, 0, " `v>", "kerub")
PB(0, 42, " ,·, ", "kerub")
PB(1, 40, " <(··)> ", "kerub")
PB(2, 42, " `-´ ", "kerub")
PB(29, 0, "c,_,o", "kerub")
PB(30, 0, "(o·o)", "kerub")
PB(31, 0, " `-´ ", "kerub")
PB(29, 41, " ,%%, ", "kerub")
PB(30, 40, " (%o%) ", "kerub")
PB(31, 41, " `~´ ", "kerub")

# ------------------------------------------------------------- 10. sig
P(31, 8, "aw", "sig")

# ------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "05-hierophant-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "05-hierophant-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
