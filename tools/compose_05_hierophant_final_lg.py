#!/usr/bin/env python3
"""Hierophant FINAL — ultracode panel synthesis (base v3b; tally b9 c6 a3).

Merge recipe:
  BASE  v3b: dense dithered scarlet robe mass, luminous speckled indigo
        Nuit field (density extended into the bottom third), gold crown,
        tri-color three-ring wand (scarlet/green/pale-yellow), blessing
        hand, mirrored elephants, center-low sworded Scarlet Woman.
  GRAFT v3a: the LARGE twin-triangle gold hexagram at v3a's scale — both
        triangles enclose the whole seated body, mirrored about col 23,
        drawn BEHIND the figure with occlusion breaks (robe, oriel, bull,
        woman, elephants all punch it).
  GRAFT v3c: the chest read — a quiet panel carved from the robe dither
        holding the pale PENTAGRAM v-points with the \\o/ dancing Child of
        Horus, concentric with the hexagram on the axis.
  GRAFT v3c: oriel behind the head (red rose ,*@*, + snake/dove curls),
        the explicit bull head (o;;;o) beneath the seated figure, gold
        throne-platform lines, crisper compact Scarlet Woman.
  FIX:  figure deep scarlet (robe class), orange kept to thin trim; nine
        nails across the oriel top.

Emits:
  drafts/05-hierophant-final-art-lg.txt       47x32 art, full-bleed
  drafts/05-hierophant-final-lg-classes.json  per-cell color classes
"""
import json, math, os

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


def pc(r, s, cls):
    """Place centered on the axis (odd-length strings sit dead on col 23)."""
    PB(r, 23 - len(s) // 2, s, cls)


# ---------------------------------------------------------------- field
# v3b's radial-glow indigo Nuit night: lit behind the oriel, dimming out,
# with the outer dither density EXTENDED into the bottom third so the
# card foot stays as luminous as the crown. Sparse pale stars throughout.
GY, GX = 4.0, 23.0
for r in range(H):
    for c in range(W):
        dx = c - GX
        dy = 2.0 * (r - GY)
        d = math.hypot(dx, dy)
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if d < 10.0:
            if h < 70:
                P(r, c, "''··"[h % 4], "field")
        elif d < 22.0:
            if h < 68:
                P(r, c, "·:·':;"[h % 6], "field")
        else:
            cov = 84 if r >= 21 else 76        # denser bottom third
            if h < cov:
                P(r, c, ";:,·::,;"[h % 8], "field")
        if (r * 13 + c * 7 + r * c) % 71 == 0:
            P(r, c, "*", "stars")

# ---------------------------------------------------------------- oriel
# v3c's window behind the head: dense lit-from-behind lattice, arch frame,
# five-petal red rose set into the crest, snake curling the left frame,
# dove on the right, exactly NINE nails across the top (Yesod / the Moon).
for r in range(2, 7):
    for c in range(16, 31):
        P(r, c, "·" if (r + c) % 2 else "'", "oriel")
PM(1, 16, "_,-´(", "oriel")
PM(2, 15, "((", "oriel")
PM(3, 15, "(:", "oriel")
PM(4, 14, "(:", "oriel")
PM(5, 14, "|:", "oriel")
PM(6, 14, "|:", "oriel")
PB(0, 14, " ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ", "nails")     # nine nails, exactly, on a
                                               # cleared strip so they read
pc(1, ",*@*,", "rose")                         # rose in blossom at the crest
PB(1, 12, " ~e ", "snake")                     # snake curls the left frame
P(2, 14, "s", "snake")
P(3, 13, "s", "snake")
P(4, 12, "s", "snake")
P(5, 12, "s", "snake")
P(6, 13, "s", "snake")
PB(1, 30, " __ ", "dove")                      # dove on the right frame
PB(2, 30, " <(´\\_ ", "dove")

# ------------------------------------------------------------- hexagram
# v3a's LARGE macrocosm: up-triangle apex behind the crown to a base at
# row 19, down-triangle chord at row 7 to an apex behind the bull. Both
# triangles enclose the whole seated body. Drawn BEHIND everything that
# follows; the oriel group is sacred (never sliced through).
SACRED = {"oriel", "snake", "dove", "nails", "rose"}


def HX(r, c, ch):
    if 0 <= r < H and 0 <= c < W and classes[r][c] not in SACRED:
        P(r, c, ch, "hex")


def hex_line(r0, c0, r1, c1, ch=None):
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        if ch:
            g = ch
        elif r1 == r0:
            g = "-"
        else:
            dc = (c1 - c0) / (r1 - r0)
            g = "|" if abs(dc) < 0.35 else ("\\" if dc > 0 else "/")
        HX(int(round(r)), int(round(c)), g)


hex_line(2, 23, 19, 3)                         # up-triangle
hex_line(2, 23, 19, 43)
hex_line(19, 3, 19, 43, "-")
hex_line(7, 3, 7, 43, "-")                     # down-triangle
hex_line(7, 3, 24, 23)
hex_line(7, 43, 24, 23)
for pr, pc_ in ((7, 3), (7, 43), (19, 3), (19, 43)):
    HX(pr, pc_, "*")                           # side star points
HX(2, 23, "^")                                 # apexes (occluded by crown /
HX(24, 23, "v")                                # the Scarlet Woman)
HX(13, 10, "X")                                # woven edge crossings
HX(13, 36, "X")

# ---------------------------------------------------------------- throne
# v3b's chunky armrest posts + v3c's gold platform lines at the card foot
PM(12, 13, ",--", "throne")
for r in range(13, 17):
    PM(r, 13, "[::", "throne")
PM(17, 13, "L::", "throne")
PB(30, 13, "L" + "=" * 19 + "7", "throne")     # dais the Woman stands on
PB(31, 9, "L" + "=" * 27 + "7", "throne")

# ------------------------------------------------------------- elephants
# v3b's Taurean elephant heads flanking, trunks curling down; they punch
# clean breaks in the hexagram edges passing behind them.
PMB(12, 0, " ,--,_ ", "eleph")
PMB(13, 0, " ((·o) ", "eleph")
PMB(14, 0, " ((_,) ", "eleph")
PMB(15, 0, "  U )( ", "eleph")
PMB(16, 0, "    (( ", "eleph")
PMB(17, 0, "    )) ", "eleph")
PMB(18, 0, "    (´ ", "eleph")

# ---------------------------------------------------------------- bull
# v3b's broad dithered bull beneath the throne + v3c's EXPLICIT head read:
# horns sweeping wide, forelock, brow, then the (o;;;o) eyes dead center
# beneath the seated figure.
PMB(20, 8, " ,===~´ ", "bull")                 # horns
PB(20, 18, " ,;;;;;;,  ", "bull")              # forelock bridging the bases
                                               # (trailing halo mirrors the
                                               # hex break left of the horns)
PMB(21, 13, " (;; ", "bull")
for r, (c0, c1) in ((21, (16, 30)), (22, (14, 32)), (23, (14, 32)),
                    (24, (15, 31)), (25, (17, 29))):
    for c in range(c0, c1 + 1):
        h = (r * 29 + c * 13) % 10
        if r == 21:
            P(r, c, "'';''·''''"[h], "bull")
        else:
            P(r, c, ";;:;;;:;;;"[h], "bull")
pc(22, "(o;;;o)", "bull")                      # the explicit bull head

# ---------------------------------------------------------------- figure
# v3b's heavy vestments: dense dithered DEEP SCARLET mass; orange held to
# a single trim column each side; olive embroidery flecks; hem x-band.
ROWS = {8: (17, 29), 9: (16, 30), 10: (16, 30), 11: (16, 30), 12: (16, 30),
        13: (16, 30), 14: (16, 30), 15: (16, 30), 16: (15, 31),
        17: (14, 32), 18: (14, 32), 19: (13, 33)}
for r, (c0, c1) in ROWS.items():
    for c in range(c0, c1 + 1):
        if c == c0:
            P(r, c, "(", "orange")
        elif c == c1:
            P(r, c, ")", "orange")
        elif c == c0 + 1 or c == c1 - 1:
            P(r, c, ":", "robe")               # FIX: scarlet, not orange
        elif (r * 7 + c * 11) % 23 == 0:
            P(r, c, "x", "olive")
        elif r == 8:
            P(r, c, "'", "robe")
        else:
            P(r, c, ";", "robe")
for c in range(15, 32, 4):                     # hem embroidery
    P(19, c, "x", "olive")

# right arm (viewer left) raising the three-ring wand — v3b's tri-color
# rings kept: TOP scarlet (Horus), green (Isis), pale yellow (Osiris)
PB(10, 12, " ,==(;", "robe")
PB(11, 9, " `===(", "robe")
P(12, 8, "(=)", "face")
for r in range(3, 12):
    P(r, 9, "|", "wand")
PB(11, 9, " `===(", "robe")                    # sleeve re-cut over the staff
P(13, 9, "'", "wand")
P(1, 8, "(O)", "ringr")
P(2, 6, "(O)", "ringg")
P(2, 10, "(O)", "ringy")

# left hand (viewer right): two fingers up, two down — the blessing
PB(10, 29, ";)=,", "orange")
P(9, 34, "¡", "face")
P(9, 36, "¡", "face")
P(10, 33, "(===)", "face")
P(11, 34, ",", "face")
P(11, 36, ",", "face")

# crown of Osiris (v3b's gold) shifted one row down so the rose blossoms
# at the crest above it; then the benignant-yet-sly face
PB(2, 21, " ,¡, ", "crown")
PB(3, 20, " |(¡)| ", "crown")
PB(4, 20, " |(¡)| ", "crown")
PB(5, 20, " <===> ", "crown")
PB(6, 20, " (o_o) ", "face")
PB(7, 20, " `,_,´ ", "face")

# ---------------------------------------------------------------- penta
# GRAFT (v3c): the chest read — carve a quiet panel out of the robe dither
# at breast height, then the pale pentagram v-points holding the glad
# dancing Child of Horus, concentric with the hexagram on the axis.
for r in range(9, 14):
    for c in range(19, 28):
        if classes[r][c] in ("robe", "olive"):
            P(r, c, "'", "robe")
P(9, 23, "*", "penta")                         # top point
PB(10, 18, " <´", "penta")                     # side points
PB(10, 26, "`> ", "penta")
PB(11, 19, " \\ ", "penta")
PB(11, 25, " / ", "penta")
PB(12, 19, " v", "penta")                      # bottom v-points
PB(12, 26, "v ", "penta")
PB(10, 21, " \\o/ ", "child")                  # the dancing child
PB(11, 22, " ¡ ", "child")
PB(12, 21, " / \\", "child")
P(12, 25, ",", "child")                        # right-foot sandal strap: To Go

# ---------------------------------------------------------------- woman
# v3c's crisper Scarlet Woman at v3b's center-low station before the bull:
# pale, militant, sword upright to her right hand, crescent moon in her left
pc(23, " ,(·), ", "woman")
pc(24, " ,(;;;), ", "woman")
pc(25, " (;;;) ", "woman")
pc(26, " (;;;) ", "woman")
pc(27, " (;;;;;) ", "woman")
pc(28, " (;;;;;) ", "woman")
pc(29, " (_,_) ", "woman")
PB(21, 16, " ¡", "sword")                      # blade point-up, thin halo so
PB(22, 16, " |", "sword")                      # the bull mass survives it
PB(23, 16, " |", "sword")
P(24, 16, "-+-", "sword")                      # guard (pale pops on brown)
P(25, 17, "¡", "sword")                        # grip
P(23, 29, ",", "moon")                         # the Moon as a compact
P(24, 28, "((", "moon")                        # crescent bow in her left
P(25, 29, "`", "moon")

# ---------------------------------------------------------------- kerubs
# v3b's New-Aeon corners: EAGLE ul, ANGEL ur, BULL ll, LION lr.
PB(0, 0, ",v, ", "kerub")
PB(1, 0, "(o< ", "kerub")
PB(2, 0, " V  ", "kerub")
PB(0, 43, " ,o,", "kerub")
PB(1, 42, " \\¡/", "kerub")
PB(2, 43, " / \\", "kerub")
PB(29, 0, "c-c ", "kerub")
PB(30, 0, "(o= ", "kerub")
PB(29, 42, " ,%,", "kerub")
PB(30, 42, " =o)", "kerub")

# ---------------------------------------------------------------- sig
P(31, 1, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "05-hierophant-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "05-hierophant-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
