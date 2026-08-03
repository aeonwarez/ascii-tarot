#!/usr/bin/env python3
"""Hierophant v3b — ultracode panel composer B: ENTHRONED-FIGURE DOMINANT.

The priest-king on the bull foremost: crown of Osiris, heavy scarlet
vestments with orange/olive embroidery, three-ring wand raised in the
RIGHT hand (viewer left), two-up-two-down blessing in the LEFT (viewer
right). Weight and ritual stillness, frontal on col 23. Supporting
structure mirrored about the axis: hexagram enclosing the body, chest
pentagram + dancing child, Scarlet Woman with sword low center, bull of
Taurus beneath, elephants + throne posts flanking, oriel window (snake,
dove, rose, nine nails) behind the head, four Kerubs in the corners, all
on a dithered indigo Nuit star-field.

Emits:
  drafts/05-hierophant-v3b-art-lg.txt       47x32 art, full-bleed
  drafts/05-hierophant-v3b-lg-classes.json  per-cell color classes
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


def line(r0, c0, r1, c1, cls, ch=None):
    """Straight segment, slope-appropriate glyphs, OVERWRITES the field."""
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        if ch:
            g = ch
        else:
            dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99
            g = "|" if abs(dc) < 0.35 else ("\\" if dc > 0 else "/")
        rr, cc = int(round(r)), int(round(c))
        if 0 <= rr < H and 0 <= cc < W:
            P(rr, cc, g, cls)


# ---------------------------------------------------------------- field
# Dark indigo Nuit night, dithered so it never reads as black emptiness.
# Radial glow behind the oriel (the window is lit from behind), dimming
# outward; sparse pale stars in the outer dark.
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
            if h < 76:
                P(r, c, ";:,·::,;"[h % 8], "field")
        if (r * 13 + c * 7 + r * c) % 71 == 0:
            P(r, c, "*", "stars")

# ---------------------------------------------------------------- hexagram
# The macrocosm enclosing his whole seated body. Up-triangle apex behind
# the crown, down-triangle apex behind the bull; the crossings and chords
# stay visible either side of the figure.
line(3, 23, 19, 5, "hex")          # up-tri left edge
line(3, 23, 19, 41, "hex")         # up-tri right edge
line(19, 5, 19, 41, "hex", "-")    # up-tri base chord
line(23, 23, 7, 5, "hex")          # down-tri left edge
line(23, 23, 7, 41, "hex")         # down-tri right edge
line(7, 5, 7, 41, "hex", "-")      # down-tri top chord
for pr, pc in ((7, 5), (7, 41), (19, 5), (19, 41)):
    P(pr, pc, "*", "hex")

# ---------------------------------------------------------------- oriel
# Arched stained window behind his head, diaphanous, lit from behind.
PM(1, 16, ",------", "oriel")
P(1, 23, "-", "oriel")
PM(2, 15, "(", "oriel")
PM(3, 14, "(", "oriel")
PM(4, 13, "|", "oriel")
PM(5, 13, "|", "oriel")
PM(6, 12, "(", "oriel")
# interior glow (kept quiet so it doesn't read as static)
for r in range(2, 6):
    for c in range(16, 31):
        if canvas[r][c] == " " and (r * 5 + c * 3) % 9 < 2:
            P(r, c, "'", "oriel")
# the SNAKE curls the left frame
for (r, c), g in zip(((2, 14), (3, 13), (4, 12), (5, 12), (6, 11)),
                     "sSsSs"):
    P(r, c, g, "snake")
# the DOVE inside the right of the window
PB(3, 27, " <(´\\ ", "dove")
# exactly NINE nails across the top (Yesod / the Moon)
for c in (7, 11, 15, 19, 23, 27, 31, 35, 39):
    P(0, c, "¡", "nails")
# five-petal ROSE blossoming behind the crown
for r, c in ((0, 22), (0, 24), (1, 20), (1, 26), (2, 19), (2, 27)):
    P(r, c, "*", "rose")

# ---------------------------------------------------------------- throne
# Chunky dark-brown armrests flanking the seat, mirrored low so they
# carry weight without caging the head.
PM(12, 13, ",--", "throne")
for r in range(13, 17):
    PM(r, 13, "[::", "throne")
PM(17, 13, "L::", "throne")

# ---------------------------------------------------------------- elephants
# Taurean elephant heads flanking, trunks curling down. Mirrored L/R.
PMB(12, 0, " ,--,_ ", "eleph")
PMB(13, 0, " ((·o) ", "eleph")
PMB(14, 0, " ((_,) ", "eleph")
PMB(15, 0, "  U )( ", "eleph")
PMB(16, 0, "    (( ", "eleph")
PMB(17, 0, "    )) ", "eleph")
PMB(18, 0, "    (´ ", "eleph")

# ---------------------------------------------------------------- bull
# The bull of Taurus beneath the throne, head centered on the axis,
# great horns sweeping wide; the Scarlet Woman will stand before its face.
PMB(20, 8, " ,===~´ ", "bull")
PB(20, 18, " ,;;;;;;, ", "bull")     # forelock bridging the horn bases
PMB(21, 13, " (;; ", "bull")
for r, (c0, c1) in ((21, (16, 30)), (22, (15, 31)), (23, (15, 31)),
                    (24, (16, 30)), (25, (18, 28))):
    for c in range(c0, c1 + 1):
        h = (r * 29 + c * 13) % 10
        if r == 21:
            P(r, c, "'';''·''''"[h], "bull")
        else:
            P(r, c, ";;:;;;:;;;"[h], "bull")
P(22, 17, "o", "bull")
P(22, 29, "o", "bull")
P(25, 19, "o", "bull")
P(25, 27, "o", "bull")

# ---------------------------------------------------------------- figure
# Heavy vestments: dithered scarlet mass, orange edges, olive embroidery.
ROWS = {7: (17, 29), 8: (16, 30), 9: (16, 30), 10: (16, 30), 11: (16, 30),
        12: (16, 30), 13: (16, 30), 14: (16, 30), 15: (16, 30),
        16: (15, 31), 17: (14, 32), 18: (14, 32), 19: (13, 33)}
for r, (c0, c1) in ROWS.items():
    for c in range(c0, c1 + 1):
        if c == c0:
            P(r, c, "(", "orange")
        elif c == c1:
            P(r, c, ")", "orange")
        elif c == c0 + 1 or c == c1 - 1:
            P(r, c, ":", "orange")
        elif (r * 7 + c * 11) % 23 == 0:
            P(r, c, "x", "olive")
        elif r == 7:
            P(r, c, "'", "robe")
        else:
            P(r, c, ";", "robe")
# hem embroidery
for c in range(15, 32, 4):
    P(19, c, "x", "olive")

# right arm (viewer left) raising the three-ring wand
PB(9, 12, " ,==(;", "orange")
PB(10, 9, " `===(", "orange")
P(11, 8, "(=)", "face")
for r in range(3, 11):
    P(r, 9, "|", "wand")
P(12, 9, "'", "wand")
P(1, 8, "(O)", "ringr")
P(2, 6, "(O)", "ringg")
P(2, 10, "(O)", "ringy")

# left hand (viewer right): two fingers up, two down — the blessing
PB(9, 29, ";)=,", "orange")
P(8, 34, "¡", "face")
P(8, 36, "¡", "face")
P(9, 33, "(===)", "face")
P(10, 34, ",", "face")
P(10, 36, ",", "face")

# crown of Osiris: tall cone + flanking plumes, gold
PB(1, 21, " ,¡, ", "crown")
PB(2, 20, " |(¡)| ", "crown")
PB(3, 20, " |(¡)| ", "crown")
PB(4, 20, " <===> ", "crown")
# the face: benignant yet sly
PB(5, 20, " (o_o) ", "face")
PB(6, 20, " `,_,´ ", "face")

# ---------------------------------------------------------------- penta
# The microcosm on his breast: pentagram holding the dancing child,
# drawn line-on-robe (no halo punch) so the chest stays a solid mass.
# First a quieter woven chest panel so the pale star pops off the robe.
for r in range(9, 14):
    for c in range(19, 28):
        if classes[r][c] in ("robe", "olive"):
            P(r, c, "'", "robe")
P(9, 22, ",¡,", "penta")
P(10, 19, "<=´", "penta")
P(10, 25, "`=>", "penta")
P(11, 20, "\\", "penta")
P(11, 26, "/", "penta")
P(12, 20, "\\", "penta")
P(12, 26, "/", "penta")
P(13, 21, "v", "penta")
P(13, 25, "v", "penta")
P(13, 23, "+", "penta")
P(11, 22, "\\o/", "child")
P(12, 22, "/", "child")
P(12, 24, "\\", "child")
P(12, 25, ",", "child")           # the right-foot sandal strap: To Go

# ---------------------------------------------------------------- woman
# The Scarlet Woman, girt with a sword, carrying the moon-bow. Militant.
PB(22, 21, " ,o, ", "woman")
PB(23, 19, " /(:::)\\ ", "woman")
PB(24, 20, " (:::) ", "woman")
PB(25, 20, " ):::( ", "woman")
PB(26, 20, " (:::) ", "woman")
PB(27, 20, " /:::\\ ", "woman")
PB(28, 20, " (:::) ", "woman")
PB(29, 19, " /:::::\\ ", "woman")
PB(30, 20, " ´ | | ` ", "woman")
# the sword, vertical, point up, haloed so it pops off the bull
P(20, 27, "^", "sword")
for r in range(21, 24):
    PB(r, 26, " |", "sword")
P(24, 26, "=", "sword")
P(24, 28, "=", "sword")
P(24, 27, "+", "sword")
# the moon as a crescent bow in her right hand
P(22, 17, ",", "moon")
PB(23, 16, " ( ", "moon")
PB(24, 16, " ( ", "moon")
P(25, 17, "`", "moon")

# ---------------------------------------------------------------- kerubs
# New-Aeon corners: EAGLE ul, ANGEL ur, BULL ll, LION lr.
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

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "05-hierophant-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "05-hierophant-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
