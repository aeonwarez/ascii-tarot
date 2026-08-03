#!/usr/bin/env python3
"""Hierophant v3a — panel candidate A: NESTED-GEOMETRY DOMINANT.

The hero read: a great golden HEXAGRAM enclosing the whole seated body
(macrocosm), a pale PENTAGRAM on the breast holding the glad dancing
Child of Horus (microcosm), both dead-centered and near-concentric on
the axis (col 23). Supporting structure kept small and mirrored: oriel
window (snake/dove/rose/nine nails) behind the crowned head, throne
posts + elephants flanking, the bull of Taurus beneath, the sword-armed
Scarlet Woman low center, four New-Aeon Kerubs in the corners, all on a
dithered dark-indigo Nuit starfield.

Emits:
  drafts/05-hierophant-v3a-art-lg.txt       47x32 art, full-bleed
  drafts/05-hierophant-v3a-lg-classes.json  per-cell color classes
"""
import json
import os

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


def L(r0, c0, r1, c1, cls, ch=None):
    """Line with slope-appropriate glyphs, always draws (overwrites bg)."""
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
        P(int(round(r)), int(round(c)), g, cls)


# ------------------------------------------------------------ 1. Nuit field
# dithered dark-indigo ground with sparse pale stars; never black emptiness
for r in range(H):
    for c in range(W):
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if h < 42:
            canvas[r][c] = "···.·.:'"[h % 8]
            classes[r][c] = "field"
        if (r * 13 + c * 17) % 71 == 0:
            canvas[r][c] = "'"
            classes[r][c] = "stars"
        if (r * 29 + c * 31) % 157 == 0:
            canvas[r][c] = "*"
            classes[r][c] = "stars"

# ------------------------------------------------------------ 2. oriel window
# arched stained window behind the head; diaphanous, lit from behind
PMB(1, 15, " _,-´ ", "oriel")            # arch shoulders (mirrored)
PB(1, 20, "-----", "oriel")              # arch top flat
PM(2, 14, "/", "oriel")
PM(3, 13, "/", "oriel")
PM(4, 13, "|", "oriel")
PM(5, 13, "|", "oriel")
PM(6, 13, "L", "oriel")
for r in range(2, 4):                    # diaphanous inner light (upper only)
    for c in range(15, 32):
        if (r * 7 + c * 5) % 5 == 0:
            P(r, c, "·", "oriel")
# nine nails fixing the window across the top (Yesod / the Moon)
for c in range(15, 32, 2):
    P(0, c, "¡", "nails")
# snake curling the left frame
P(2, 14, "s", "snake")
P(3, 13, "S", "snake")
P(4, 12, "s", "snake")
P(5, 12, "´", "snake")
# dove on the right frame
P(2, 32, "w", "dove")
P(2, 33, "´", "dove")
# five-petal rose in blossom behind the headdress
P(1, 23, "@", "rose")
P(2, 21, "@", "rose")
P(2, 25, "@", "rose")
P(3, 19, "@", "rose")
P(3, 27, "@", "rose")

# ------------------------------------------------------------ 4. dais + floor
P(26, 5, "[", "throne")
P(26, 41, "]", "throne")
for c in range(6, 41):
    P(26, c, "=", "throne")
for c in range(3, 44):
    P(27, c, "=" if c % 3 else "·", "throne")
for r in range(28, H):
    for c in range(W):
        h = (r * 41 + c * 23) % 100
        if h < 74:
            canvas[r][c] = ".,:;"[h % 4]
            classes[r][c] = "olive" if h % 9 == 0 else "throne"
        else:
            canvas[r][c] = " "
            classes[r][c] = None

# ------------------------------------------------------------ 5. the bull
# broad brown mass beneath the throne, lit from above; horns + eyes flank
for r in range(19, 26):
    for c in range(9, 38):
        dx = (c - 23) / 14.0
        dy = (r - 22.4) / 4.0
        if dx * dx + dy * dy <= 1.0:
            h = (r * 31 + c * 43) % 100
            if h < 94:
                canvas[r][c] = "'':;" [h % 4] if r <= 20 else ";;:;,;" [h % 6]
                classes[r][c] = "bull"
# (the bull's head — horns, eyes, nostrils — is drawn AFTER the figure,
# since it sits forward beneath his knees; see step 9b)

# ------------------------------------------------------------ 6. HEXAGRAM
# macrocosm: two interlocked triangles enclosing the whole seated body
L(2, 23, 19, 3, "hex")                   # up-triangle
L(2, 23, 19, 43, "hex")
L(19, 3, 19, 43, "hex")
L(7, 3, 7, 43, "hex")                    # down-triangle
L(7, 3, 24, 23, "hex")
L(7, 43, 24, 23, "hex")
P(2, 23, "^", "hex")                     # apexes + starry side points
P(24, 23, "v", "hex")
P(7, 3, "*", "hex")
P(7, 43, "*", "hex")
P(19, 3, "*", "hex")
P(19, 43, "*", "hex")

# ------------------------------------------------------------ 7. elephants
# Taurean elephant heads flanking the seat (after hexagram: they punch it)
PMB(9, 0, " ,--, ", "eleph")
PMB(10, 0, "( (o) ", "eleph")            # great ear + eye
PMB(11, 0, "( ) ( ", "eleph")            # ear fold, trunk falling
PMB(12, 0, " ) v( ", "eleph")            # tusk + trunk
PMB(13, 0, " (  ) ", "eleph")            # trunk curling in
PMB(14, 0, "  )(  ", "eleph")
PMB(15, 0, "  ´`  ", "eleph")

# ------------------------------------------------------------ 8. the figure
# robe: heavy SOLID scarlet vestments, orange trim, olive embroidery
HALF = {7: 6, 8: 7, 9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8,
        16: 9, 17: 10}
for r, half in HALF.items():
    c0, c1 = 23 - half, 23 + half
    for c in range(c0, c1 + 1):
        h = (r * 53 + c * 29) % 100
        if c == c0:
            canvas[r][c] = "("
            classes[r][c] = "orange"
        elif c == c1:
            canvas[r][c] = ")"
            classes[r][c] = "orange"
        elif c <= c0 + 1 or c >= c1 - 1:
            canvas[r][c] = ";"
            classes[r][c] = "orange"
        elif h % 11 == 0:
            canvas[r][c] = "#%"[h % 2]
            classes[r][c] = "olive"
        else:
            # lit from upper-left: lighter weave there, denser lower-right
            canvas[r][c] = (";:;;" if (r + c) > 32 else ";:::")[h % 4]
            classes[r][c] = "robe"
# crown of Osiris over the rose, on the axis
PB(3, 21, "/¡¡¡\\", "crown")
PB(4, 21, "((¡))", "crown")
# the face: benignant yet sly
PB(5, 20, "(´o·o`)", "face")
PB(6, 21, "(`~´)", "face")
# right arm raised with the three-ringed wand (viewer left)
PB(8, 11, " ,===", "orange")
PB(2, 10, "(O)", "ringr")                # Horus — scarlet
PB(3, 10, "(O)", "ringg")                # Isis — green
PB(4, 10, "(O)", "ringy")                # Osiris — pale yellow
for r in range(5, 10):
    P(r, 11, "|", "wand")
P(9, 10, "(", "face")                    # hand gripping the staff
P(9, 12, ")", "face")
# left arm giving the blessing: two fingers up, two down (viewer right)
P(8, 31, "==", "orange")
P(7, 34, "¡¡", "face")
PB(8, 33, "(´´)", "face")
P(9, 34, ",,", "face")

# ------------------------------------------------------------ 9. PENTAGRAM
# microcosm on the breast: a dark star-shaped window punched into the
# scarlet mass, pale star outline + the dancing child popping inside
PB(9, 22, "   ", "penta")
PB(10, 21, "     ", "penta")
PB(11, 18, "           ", "penta")
PB(12, 19, "         ", "penta")
PB(13, 19, "         ", "penta")
PB(14, 20, "       ", "penta")
PB(15, 18, "   ", "penta")               # dark caps so the points pop
PB(15, 26, "   ", "penta")
P(9, 23, "*", "penta")                   # top point
P(10, 22, "/", "penta")
P(10, 24, "\\", "penta")
P(11, 17, "*=--´", "penta")              # side points + upper bars
P(11, 25, "`--=*", "penta")
P(12, 19, "\\", "penta")
P(12, 27, "/", "penta")
P(13, 19, "/", "penta")
P(13, 27, "\\", "penta")
P(14, 20, "/", "penta")
P(14, 22, "/", "penta")
P(14, 24, "\\", "penta")
P(14, 26, "\\", "penta")
P(15, 19, "*", "penta")                  # bottom points
P(15, 27, "*", "penta")
# the glad dancing Child of Horus inside
P(11, 23, "o", "child")
P(12, 21, "<(¡)>", "child")
P(13, 22, "/", "child")
P(13, 24, "\\", "child")
P(13, 25, "=", "olive")                  # right-foot sandal strap ("To Go")

# ------------------------------------------------------- 9b. the bull's head
# forward beneath his knees: horns arcing out, punched eyes, nostrils
PMB(17, 10, " ,=´ ", "bull")             # horn tips sweeping up-out
PMB(18, 12, " ,-( ", "bull")
PMB(19, 15, " ( ", "bull")
PMB(20, 14, " (o) ", "bull")             # eyes, halo-punched to pop
PMB(23, 17, " o ", "bull")               # nostrils beside the skirt hem

# ------------------------------------------------------------ 10. the woman
# Scarlet Woman, pale, militant: vertical sword + the Moon crescent
P(15, 18, "¡", "sword")                  # blade point-up
P(16, 18, "|", "sword")
P(17, 18, "|", "sword")
P(18, 17, "=+=", "sword")                # guard
P(19, 18, "|", "sword")
PB(17, 20, "  (:)  ", "woman")           # head
PB(18, 20, " ,(:), ", "woman")           # shoulders
P(18, 26, "-", "woman")
P(17, 27, "C", "moon")                   # the Moon crescent, raised
P(19, 19, "-", "woman")                  # arm to the sword grip
PB(19, 20, " (:::) ", "woman")
PB(20, 20, " (:::) ", "woman")
PB(21, 20, "  ):(  ", "woman")
PB(22, 20, " /:::\\ ", "woman")
PB(23, 19, " /:::::\\ ", "woman")
P(24, 21, "¡", "woman")                  # feet apart — hexagram point between
P(24, 25, "¡", "woman")

# ------------------------------------------------------------ 11. Kerubs
# New-Aeon corners: eagle UL, angel UR, bull LL, lion LR
PB(0, 0, ",-,  ", "kerub")               # eagle
PB(1, 0, "((o> ", "kerub")
PB(2, 0, " ))´ ", "kerub")
PB(0, 42, " ,·, ", "kerub")              # angel
PB(1, 42, "<(:)>", "kerub")
PB(2, 42, " /:\\ ", "kerub")
PB(29, 0, ",´`, ", "kerub")              # bull
PB(30, 0, "(oo) ", "kerub")
PB(31, 0, "`==´ ", "kerub")
PB(29, 42, ",ww, ", "kerub")             # lion
PB(30, 42, "(o~o)", "kerub")
PB(31, 42, "`(=)´", "kerub")

# ------------------------------------------------------------ 12. signature
P(31, 4, "aw", "sig")

# ------------------------------------------------------------ emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "05-hierophant-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "05-hierophant-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
