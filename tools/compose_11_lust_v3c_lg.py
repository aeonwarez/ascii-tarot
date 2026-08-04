#!/usr/bin/env python3
"""Lust v3c — BEAST DOMINANT (ultracode panel, composer C).

The great seven-headed lion-serpent is the hero: a tawny golden mass
sweeping the whole lower-left, its seven distinct head silhouettes
(angel, man of valour, lion-serpent, saint, satyr, woman, poet)
clustered upper-left, the serpent tail sweeping up the right to a
sun-ringed head biting the crescent, grey saints trampled under the
great paws. Babalon rides astride as its guiding will — spine on the
axis (col 23), head thrown back, golden hair cascading down the right
edge — and the flaming Grail raised in her right hand is its crown and
the card's light. Deep purple ground, ten rose rayed circles scattered,
teal new-Aeon burst + tawny serpent-horn band across the top.

Emits:
  drafts/11-lust-v3c-art-lg.txt       47x32 art, full-bleed
  drafts/11-lust-v3c-lg-classes.json  per-cell color classes
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


def hsh(r, c):
    return (r * 37 + c * 59 + (r * c) % 13) % 100


# ------------------------------------------------------------------ sky
# pale dawn strip behind the serpent band, rows 0-2
for r in range(0, 3):
    for c in range(W):
        h = hsh(r, c)
        if h < 55:
            canvas[r][c] = "·-'"[h % 3]
            classes[r][c] = "sky"

# ---------------------------------------------------------------- field
# deep purple ground rows 3-31, dusk deepening toward the base; lit
# faintly around the raised Grail (the card's light source).
GY, GX = 4.0, 25.0
for r in range(3, H):
    for c in range(W):
        h = hsh(r, c)
        cls = "dusk" if (r >= 25 or (r >= 22 and c <= 2)) else "field"
        d = math.hypot(c - GX, 2.0 * (r - GY))
        if d < 8.5 and h < 26:
            canvas[r][c] = "'"
            classes[r][c] = "flame"
            continue
        if h < 87:
            ramp = ",.;:" if cls == "dusk" else "·:;,;:"
            canvas[r][c] = ramp[h % len(ramp)]
            classes[r][c] = cls

# --------------------------------------------------- serpent-horn band
# tawny serpents writhing across the dawn strip, broken by the burst
PB(0, -1, "~s~o~~s~,~o~s~~ ", "serpents")
PB(1, -1, ",~o<~~s~~o<~s ", "serpents")
PB(0, 32, " ~s~o~~,~s~o~~~", "serpents")
PB(1, 33, " s~~o<~s~~o<~", "serpents")

# ---------------------------------------------------------------- burst
# teal new-Aeon light breaking the band at top centre
PB(0, 14, " `\\`\\ \\ ", "burst")
PB(0, 26, " / /´/´ ", "burst")
PB(1, 16, " ~*=~ ", "burst")
PB(1, 27, " ~=*~ ", "burst")

# -------------------------------------------------------------- circles
# the ten latent Sephiroth: rose rayed circles, scattered, no Tree order
def circle(r, c):
    PB(r - 1, c + 1, " ¡ ", "circles")
    PB(r, c - 1, " <(o)> ", "circles")


circle(5, 1)     # upper-left pair, on the purple corner
circle(9, 1)
circle(2, 15)    # flanking the burst, on the band
circle(2, 32)
circle(6, 29)    # beside the Grail
circle(11, 37)   # under the sun-ring
circle(10, 19)   # over her shoulder, left of the arm
circle(17, 43)   # right edge
circle(30, 35)   # among the trampled saints (redrawn after them)

# ------------------------------------------------------------- sun-ring
# the lion-serpent's tail-head: gold sun ring, serpent biting the moon
PB(5, 36, " `\\¡/´ ", "beast")
PB(6, 34, " ,=´‾‾`=, ", "beast")
PB(7, 33, " <=(", "beast")
P(7, 37, "C", "face")
P(7, 38, "<e,", "serpents")
PB(7, 41, ")=> ", "beast")
PB(8, 36, " ,/¡\\, ", "beast")
# tail: banded serpent sweeping down the right edge from the ring
PB(9, 41, " `\\s, ", "serpents")
PB(10, 42, " )ss) ", "serpents")
PB(11, 43, " (ss, ", "serpents")
PB(12, 43, " )ss; ", "serpents")
PB(13, 43, " (ss, ", "serpents")
PB(14, 42, " `sss ", "serpents")
PB(15, 42, " ,ss´ ", "serpents")

# ---------------------------------------------------------------- beast
# the great tawny mass: forequarters + mane sweep the lower-left,
# flank bridges under the rider, haunch fills the lower-right corner.
EDGE_A = {3: 17, 4: 18, 5: 18, 6: 18, 7: 17, 8: 17, 9: 16, 10: 16,
          11: 15, 12: 15, 13: 15, 14: 16, 15: 17, 16: 18, 17: 19,
          18: 20, 19: 20, 20: 21, 21: 21, 22: 21, 23: 20, 24: 20,
          25: 21, 26: 21, 27: 21}
# left bound: the mass narrows at the top so the purple corner (and its
# two rayed circles) shows, as in the scan
LMIN = {3: 6, 4: 6, 5: 6, 6: 4, 7: 4, 8: 4, 9: 7, 10: 7}
FLANK_R = {18: 28, 19: 29, 20: 30, 21: 31, 22: 32, 23: 33, 24: 34}
HAUNCH_L = {21: 43, 22: 42, 23: 41, 24: 40, 25: 39, 26: 38, 27: 37}

for r in range(3, 28):
    for c in range(W):
        h = hsh(r, c)
        zone = None
        if LMIN.get(r, 0) <= c <= EDGE_A.get(r, -1):
            if 24 <= r <= 27 and 10 <= c <= 12:
                zone = None            # gap between the forelegs
            else:
                zone = "fore"
        if zone is None and r in FLANK_R and EDGE_A.get(r, -1) < c <= FLANK_R[r]:
            zone = "flank"
        if zone is None and r in HAUNCH_L and c >= HAUNCH_L[r]:
            zone = "haunch"
        if zone is None:
            continue
        if zone == "fore":
            p = (c * 2 + r * 3) % 7
            if p < 2:
                canvas[r][c] = ")"
                classes[r][c] = "mane"
            elif p == 3:
                canvas[r][c] = "("
                classes[r][c] = "mane"
            elif h < 94:
                canvas[r][c] = ";s;:"[h % 4]
                classes[r][c] = "beast"
        elif zone == "flank":
            p = (c + r * 2) % 6
            if p == 0:
                canvas[r][c] = "~"
                classes[r][c] = "mane"
            elif h < 86:
                canvas[r][c] = ";s:;"[h % 4]
                classes[r][c] = "beast"
        else:  # haunch
            p = (c * 2 - r) % 6
            if p < 2:
                canvas[r][c] = "("
                classes[r][c] = "mane"
            elif h < 90:
                canvas[r][c] = ";,;:"[h % 4]
                classes[r][c] = "beast"

# ---------------------------------------------------------- seven heads
# distinct silhouettes clustered on the upper-left mass, drawn on top
# 1. lion-serpent, topmost, jaws open to the right (mane-dark outline,
#    pale teeth/eye so it separates from the golden mass)
PB(3, 8, " ,cOOOc, ", "mane")
PB(4, 8, " (o´,==<´ ", "mane")
P(4, 10, "o", "face")
P(4, 13, "==<", "face")
PB(5, 8, " (;`ww=<, ", "mane")
P(5, 14, "=<", "face")
PB(6, 8, " `(;;;)´ ", "mane")
# 2. angel, haloed, serene (left of the lion crown)
PB(3, 4, " ,-, ", "face")
PB(4, 4, "(´i`)", "face")
# 3. man of valour: crested helm + visor
PB(6, 1, " ,=\\ ", "face")
PB(7, 1, " (o< ", "face")
PB(8, 1, " `-´ ", "face")
# 4. crowned bearded saint (centre of the cluster)
PB(7, 7, " vVv ", "beast")
PB(8, 6, " (o,o) ", "face")
PB(9, 6, " (;w;) ", "face")
PB(10, 7, " `ww´ ", "beast")
# 5. satyr: horns + goatee
PB(7, 13, " \\,/ ", "beast")
PB(8, 13, " (e) ", "face")
PB(9, 13, " `w´ ", "face")
# 6. the calm woman, gazing out
PB(11, 1, " ,-´-, ", "face")
PB(12, 1, "(´o-o`)", "face")
PB(13, 1, " `,-,´ ", "face")
# 7. the poet, laurelled, mouth open in song
PB(11, 8, " ,=, ", "face")
PB(12, 8, " (´o`) ", "face")
PB(13, 9, " `-´ ", "face")

# --------------------------------------------------------------- saints
# grey bloodless saints trampled at the base, grouped like Shin
PB(24, 27, " ,=, ", "saints")
PB(25, 27, " (-·-) ", "saints")
PB(25, 22, " ,=, ", "saints")
PB(26, 22, " (-·-) ", "saints")
PB(26, 32, " ,=, ", "saints")
PB(27, 32, " (-·-) ", "saints")
PB(27, 25, " (-·-) ", "saints")
PB(28, 29, " (-·-) ", "saints")
for r in range(28, 31):
    for c in range(22, 37):
        if canvas[r][c] == " " or classes[r][c] in ("dusk", "field"):
            h = hsh(r, c)
            if h < 52:
                canvas[r][c] = ";w:"[h % 3]
                classes[r][c] = "saints"
# grey drape trampled between the forelegs
PB(24, 9, " ,w, ", "saints")
PB(25, 9, " (ww) ", "saints")
PB(26, 9, " `w´ ", "saints")

# fur running off the bottom-left edge behind the paw
for r in range(28, H):
    for c in range(0, 4):
        h = hsh(r, c)
        if h < 80:
            canvas[r][c] = ";s,:"[h % 4]
            classes[r][c] = "beast" if h % 3 else "mane"

# ----------------------------------------------------------------- paws
# great front paws (over the saints' edge) + rear paw lower-right
PB(28, 4, " ,=OOOO=, ", "beast")
PB(29, 4, " (o(o(o(o) ", "beast")
PB(30, 5, " V V V V ", "reins")
PB(29, 15, " ,=OOOO=, ", "beast")
PB(30, 15, " (o(o(o(o) ", "beast")
PB(31, 16, " V V V V ", "reins")
PB(28, 38, " ,=OOO=, ", "beast")
PB(29, 39, " (o(o(o) ", "beast")
PB(30, 40, " V V V ", "reins")

# ----------------------------------------------------------------- hair
# huge golden hair sweeping from her thrown-back head down the right
HAIR = {9: (28, 33), 10: (30, 34), 11: (30, 35), 12: (31, 37),
        13: (31, 39), 14: (32, 40), 15: (32, 41), 16: (33, 42),
        17: (33, 41), 18: (33, 42), 19: (34, 42), 20: (34, 42),
        21: (35, 42), 22: (35, 41), 23: (36, 41), 24: (37, 40),
        25: (38, 39)}
for r, (a, b) in HAIR.items():
    for c in range(a, b + 1):
        h = hsh(r, c)
        p = (c * 3 + r) % 8
        if p < 2:
            ch = "s"
        elif p == 2:
            ch = ")"
        elif p == 3:
            ch = "("
        elif p == 4:
            ch = "S"
        elif h >= 94:
            continue
        else:
            ch = ";';"[h % 3]
        canvas[r][c] = ch
        classes[r][c] = "hair"

# -------------------------------------------------------------- babalon
# riding astride, leaning back, spine on the axis (col 23)
def CL(r, c0, c1):
    """Punch a dark halo so the rider separates from ground and fur."""
    for c in range(c0, c1 + 1):
        if 0 <= r < H and 0 <= c < W:
            canvas[r][c] = " "
            classes[r][c] = None


for r in range(7, 9):         # right of the raised arm
    CL(r, 26, 27)
for r in range(12, 16):       # either side of the torso
    CL(r, 17, 18)
    CL(r, 28, 29)
CL(16, 27, 28)
CL(17, 27, 28)
# near leg over the beast's shoulder
PB(17, 12, " ,=;;;;", "babalon")
PB(18, 11, " /;;;/ ", "babalon")
PB(19, 11, " (;;/ ", "babalon")
PB(20, 11, " );;| ", "babalon")
PB(21, 11, " (;;| ", "babalon")
PB(22, 12, " `;;( ", "babalon")
PB(23, 13, " \\==, ", "babalon")
# torso, arched back, centred on col 23
PB(12, 21, " ,;;;) ", "babalon")
PB(13, 19, " (;;;;;;) ", "babalon")
PB(14, 20, " );;;;( ", "babalon")
PB(15, 19, " (;;;;) ", "babalon")
PB(16, 18, " (;;;;;) ", "babalon")
PB(17, 18, "(;;;;;;)", "babalon")
# left (carnal) arm reaching down to the reins (P, not PB: it must sit
# flush against the torso wall without punching it)
P(14, 19, ",(", "babalon")
P(15, 18, "(;", "babalon")
P(16, 18, "\\,", "babalon")
# right (spiritual) arm raised to the Grail: one solid lifted line
PB(6, 22, " ,\\", "babalon")
PB(7, 23, " |; ", "babalon")
PB(8, 23, " |; ", "babalon")
PB(9, 23, " (;; ", "babalon")
PB(10, 24, " );; ", "babalon")
PB(11, 24, " (;( ", "babalon")
# head thrown back in ecstasy, face to the sky (drawn over the hair)
PB(9, 27, ",=´, ", "hair")
PB(10, 27, "(´o‾) ", "babalon")
PB(11, 28, "\\_,´ ", "babalon")

# ---------------------------------------------------------------- reins
# red reins: line to the withers + the loop hanging from her hand
PB(14, 12, " ,=´ ", "reins")
PB(15, 14, " ,=´ ", "reins")
for r, c, ch in [(17, 18, "("), (17, 21, ")"), (18, 17, "("), (18, 21, ")"),
                 (19, 17, "("), (19, 21, ")"), (20, 18, "\\"), (20, 21, "/"),
                 (21, 19, "\\"), (21, 20, "/")]:
    P(r, c, ch, "reins")

# late circle: right of her waist, on top of the hair edge (as the scan
# lets the rose circles ride over the flowing masses)
circle(16, 29)

# ---------------------------------------------------------------- grail
# the flaming Holy Grail, raised, blazing — the card's climax
PB(0, 22, " ¡¡ ", "flame")
PB(1, 21, " ,¡*¡, ", "flame")
PB(2, 20, " (%%%%%%%) ", "flame")
P(2, 21, "(", "grail")
P(2, 29, ")", "grail")
PB(3, 21, " \\%%%%%/ ", "flame")
P(3, 22, "\\", "grail")
P(3, 28, "/", "grail")
PB(4, 22, " `\\;;/´ ", "grail")
PB(5, 23, " `U´ ", "grail")
P(6, 25, "¡", "grail")

# ------------------------------------------------------------------ sig
P(31, 1, "aw", "sig")

# ----------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "11-lust-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "11-lust-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
