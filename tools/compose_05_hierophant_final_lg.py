#!/usr/bin/env python3
"""Hierophant FINAL — SCAN REVISION (base: shipped final; ground truth:
reference/05-hierophant-card.jpg, the Harris scan that arrived after the
card was synthesized).

What the scan corrected:
  WARMTH DOMINATES. The painting is flooded with orange/amber. The robe
        is now a huge ORANGE/GOLD mass with a scarlet core (was: scarlet
        with orange trim), and it cascades in skirt-falls past the bull
        down to the dais. Indigo survives only as shadow slots between
        the warm masses + the starry gaps.
  ELEPHANTS ARE LARGE. The flanking elephants are big warm orange-brown
        masses (eleph retuned #c8874a), rows 8-20 hard against both
        frame edges, eye/ear/trunk carved in dark throne-brown. They sit
        UNDER the hexagram, whose gold edges cross over them exactly as
        the thin geometry lines cross the beasts in the painting.
  CORNER KERUBS ARE MASK-FACES. Upper-left a bird-skull mask, upper-
        right a golden mask-face (kerub retuned #d8c090), lower-left the
        pale bull-head, lower-right the white curly fleece.
  WAND AT THE BREAST. The three interlaced Aeon rings (scarlet/green/
        pale-yellow kept) top a dark key-shaft held in the fist at the
        chest, as in the scan; the blessing hand drops to hip height.

Kept from the shipped final: the large twin-triangle gold hexagram
enclosing the body (broken behind the figure), the chest pentagram with
the \\o/ dancing Child, crown + face, oriel with rose/snake/dove and
nine nails, the sworded Scarlet Woman with her crescent, the bull
beneath, the starry field in the remaining gaps, the 'aw' signature.

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
# Indigo Nuit night, now SHADOW rather than ground: the warm masses drawn
# on top of it cover most of the card (as in the scan), so the field only
# survives in the slots between masses and the corner gaps. Radial glow
# behind the oriel kept; sparse pale stars throughout.
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

# ---------------------------------------------------------------- oriel
# Window behind the head: dense lit-from-behind lattice, arch frame,
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

# ------------------------------------------------------------- elephants
# SCAN: the elephants are LARGE warm orange-brown masses filling the
# flanks edge to edge, rows 8-20 — not small grey heads. Dithered and lit
# (lighter crowns, denser flanks), eye/ear/trunk carved in dark brown.
# Drawn BEFORE the hexagram so its gold edges cross over them, exactly as
# the thin geometry lines cross the beasts in the painting.
ELEF = {8: (0, 8), 9: (0, 10), 10: (0, 11), 11: (0, 11), 12: (0, 11),
        13: (0, 10), 14: (1, 10), 15: (1, 10), 16: (2, 9), 17: (2, 9),
        18: (3, 9), 19: (3, 8), 20: (4, 8)}
for r, (c0, c1) in ELEF.items():
    for a0, a1 in ((c0, c1), (46 - c1, 46 - c0)):
        for c in range(a0, a1 + 1):
            if c == a0:
                ch = "("
            elif c == a1:
                ch = ")"
            else:
                mc = min(c, 46 - c)                # mirror-symmetric dither
                h = (r * 31 + mc * 17) % 12
                ch = "'';;:;;;';;:"[h] if r <= 12 else ";;:;;;;:;;;;"[h]
            P(r, c, ch, "eleph")
PM(10, 2, "·o", "throne")                      # eye
PM(11, 7, "c", "throne")                       # ear curl
PM(15, 5, "))", "throne")                      # trunk, curling down and in
PM(16, 6, "))", "throne")
PM(17, 6, "))", "throne")
PM(18, 5, "))", "throne")
PM(19, 4, "((", "throne")
PM(20, 5, "((´", "throne")

# ------------------------------------------------------------- hexagram
# The LARGE macrocosm kept at full scale: up-triangle apex behind the
# crown to a base at row 19, down-triangle chord at row 7 to an apex
# behind the bull. Drawn OVER the elephants (painting-true), BEHIND the
# figure and everything that follows; the oriel group is sacred.
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
# Gold platform lines at the card foot (the posts are gone — the scan's
# robe mass swallows the seat).
PB(30, 13, "L" + "=" * 19 + "7", "throne")     # dais the Woman stands on
PB(31, 9, "L" + "=" * 27 + "7", "throne")

# ---------------------------------------------------------------- bull
# Broad dithered bull beneath the throne + the EXPLICIT head read: horns
# sweeping wide, forelock, brow, then the (o;;;o) eyes dead center.
PMB(20, 8, " ,===~´ ", "bull")                 # horns
PB(20, 18, " ,;;;;;;,  ", "bull")              # forelock bridging the bases
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
# SCAN: the vestments are a huge ORANGE/GOLD mass with a SCARLET core —
# warmth dominates, and the mass is wider at every row than the shipped
# final. Olive embroidery flecks; hem x-band.
ROWS = {8: (16, 30), 9: (15, 31), 10: (15, 31), 11: (15, 31),
        12: (14, 32), 13: (14, 32), 14: (14, 32), 15: (13, 33),
        16: (13, 33), 17: (12, 34), 18: (12, 34), 19: (11, 35)}
for r, (c0, c1) in ROWS.items():
    for c in range(c0, c1 + 1):
        if c == c0:
            P(r, c, "(", "orange")
        elif c == c1:
            P(r, c, ")", "orange")
        elif (r * 7 + c * 11) % 23 == 0:
            P(r, c, "x", "olive")
        else:
            if r <= 13:                        # scan: SCARLET shoulders and
                scarlet = abs(c - 23) >= 5     # upper sleeves, amber chest
            else:                              # (the panel glows between)
                scarlet = abs(c - 23) <= 3     # red central fold
            ch = ":" if c % 5 == 2 else ";"
            P(r, c, ch, "robe" if scarlet else "orange")
for c in range(13, 35, 4):                     # hem embroidery
    P(19, c, "x", "olive")

# skirt-falls: the robe cascades past the bull down to the dais, flanking
# the Scarlet Woman — the bottom of the card is full-bleed warm, with
# indigo surviving only in the shadow slits beside her.
SKIRT = {21: (9, 13), 22: (9, 13), 23: (8, 13), 24: (8, 13), 25: (9, 15),
         26: (9, 16), 27: (9, 16), 28: (9, 16), 29: (10, 16)}
for r, (c0, c1) in SKIRT.items():
    for a0, a1 in ((c0, c1), (46 - c1, 46 - c0)):
        for c in range(a0, a1 + 1):
            if c == a0:
                P(r, c, "(", "orange")
            elif c == a1:
                P(r, c, ")", "orange")
            else:
                cls = "robe" if (min(c, 46 - c) + r) % 7 == 0 else "orange"
                P(r, c, ":" if c % 4 == 2 else ";", cls)

# right arm (viewer left): the three-ring wand held at the BREAST as in
# the scan — interlaced Aeon rings (TOP scarlet Horus, green Isis, pale
# yellow Osiris) over a dark key-shaft dropping to the fist.
P(8, 15, "(O)", "ringr")
P(9, 14, "(O)", "ringg")
P(9, 17, "(O)", "ringy")
for r in (10, 11, 12):
    P(r, 16, "|", "throne")                    # dark shaft on the orange
PB(13, 14, " (=) ", "face")                    # the fist
P(14, 16, "'", "throne")

# left hand (viewer right): dropped to hip height as in the scan, palm
# open before the right elephant — two fingers up, two down, the blessing
PB(15, 33, " ¡ ¡ ", "face")
PB(16, 32, " (===) ", "face")
PB(17, 33, " , , ", "face")

# crown of Osiris (gold) with the rose blossoming at the crest above it;
# then the benignant-yet-sly face
PB(2, 21, " ,¡, ", "crown")
PB(3, 20, " |(¡)| ", "crown")
PB(4, 20, " |(¡)| ", "crown")
PB(5, 20, " <===> ", "crown")
PB(6, 20, " (o_o) ", "face")
PB(7, 20, " `,_,´ ", "face")

# ---------------------------------------------------------------- penta
# The chest read — carve a quiet panel out of the robe dither at breast
# height, then the pale pentagram v-points holding the glad dancing Child
# of Horus, concentric with the hexagram on the axis.
for r in range(9, 14):
    for c in range(19, 28):
        if classes[r][c] in ("robe", "orange", "olive"):
            P(r, c, "'", "orange")
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
# The Scarlet Woman at her center-low station before the bull: pale,
# militant, sword upright to her right hand, crescent moon in her left
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
# SCAN: the corners hold sizable MASK-FACES, not tiny marks. Upper-left
# the bird-skull mask (dark eye socket, hooked beak); upper-right the
# golden mask-face (hollow eyes, straight nose); lower-left the pale
# bull-head; lower-right the white curly fleece.
PB(0, 0, ",--,_ ", "kerub")                    # UL: bird-skull mask
PB(1, 0, "(';;;;,_ ", "kerub")
PB(2, 0, "(;';;;;;) ", "kerub")
PB(3, 0, "((o);;;;) ", "kerub")
PB(4, 0, " `,);;;;) ", "kerub")
PB(5, 0, "  V(;;;´ ", "kerub")
PB(6, 0, "   `-´ ", "kerub")
P(3, 2, "o", "field")                          # dark eye socket

PB(0, 40, " _,--, ", "kerub")                  # UR: golden mask-face
PB(1, 39, " (';;;;)", "kerub")
PB(2, 38, " (;o;;;o)", "kerub")
PB(3, 38, " (;;;|;;)", "kerub")
PB(4, 38, " (;;;‾;;)", "kerub")
PB(5, 39, " (;;;;;)", "kerub")
PB(6, 40, " `;;;´ ", "kerub")
P(2, 41, "o", "field")                         # hollow eyes
P(2, 45, "o", "field")

PB(26, 0, "(‾,  ,‾) ", "kerub")                # LL: pale bull-head, horns
PB(27, 0, " (';;') ", "kerub")
PB(28, 0, "(o;;;;o) ", "kerub")
PB(29, 0, " (;;;;) ", "kerub")
PB(30, 0, " (¡;;¡) ", "kerub")                 # nostril slits
P(28, 1, "o", "field")                         # dark eyes
P(28, 6, "o", "field")

PB(26, 39, " ,csc, ", "dove")                  # LR: white curly fleece
PB(27, 38, " (scscs)", "dove")
PB(28, 38, " (co;oc)", "dove")
PB(29, 38, " (scscs)", "dove")
PB(30, 39, " `csc´ ", "dove")
P(28, 41, "o", "field")                        # dark eye-holes in the wool
P(28, 43, "o", "field")

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
