#!/usr/bin/env python3
"""Lust FINAL — ultracode panel synthesis (judge tally v3a 8, v3b 7, v3c 3).

BASE (v3a, rider dominant): the ecstatic-sacred rider-surge — flaming Grail
near the axis (slight off-axis lift, authentic) with the \\w/ hand, golden %
torso-arc sweeping down-right to the red rein U-loop, solid dithered tawny
Beast mass, grey Shin-group saints, hair cascade down the right edge.
GRAFT 1 (v3b): true CUP ANATOMY — flame tongues over bowl over narrow stem
(,@#@, / (@#@#@) / \\%%%%%%%/ / \\%%%/) so the Grail reads as a chalice; and
v3b's dense purple lattice field so the ground is full-bleed, no black.
Also v3b's crisper seven-face cluster on the Beast's crown.
GRAFT 2 (v3c): the wide rayed circle glyph <(o)> at 2:1 cell aspect —
exactly TEN, scattered above and below, NOT in Tree order (asserted); and
v3c's sun-lion emblem <=(C<e,)=> for the serpent tail.
FIX: whole rider shifted +1 col so the figure centroid sits on col 23
(v3a drifted to ~22); the Grail remains the climax and light source.

Emits:
  drafts/11-lust-final-art-lg.txt       47x32 art, full-bleed
  drafts/11-lust-final-lg-classes.json  per-cell color classes (art coords)
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


# ---------------------------------------------------------------- sky strip
# Pale dawn strip behind the serpent-horn band (rows 0-2), denser than v3a
# so the top corners are painted, not black.
for r in range(0, 3):
    for c in range(W):
        h = (r * 41 + c * 29) % 100
        if h < 55:
            canvas[r][c] = "·'‾"[h % 3] if r < 2 else "-·-"[h % 3]
            classes[r][c] = "sky"

# ---------------------------------------------------------------- field
# GRAFT 1b (v3b): dense purple lattice with dusk veins, rows 3-31 — the
# ground is a painted mottled violet, full-bleed, no black emptiness.
for r in range(3, H):
    for c in range(W):
        h = (r * 53 + c * 31 + (r * c) % 7) % 100
        if (r * 7 + c * 11) % 31 < 4:
            canvas[r][c] = ";"
            classes[r][c] = "dusk"
        elif h < 95:
            canvas[r][c] = "·,:;,··:"[h % 8]
            classes[r][c] = "field"

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
    (2, 29, "~"), (0, 21, "·"), (0, 25, "·"), (3, 17, "·"),
]:
    P(r, c, ch, "burst")

# ---------------------------------------------------------------- beast
# Great tawny lion-serpent mass, lower left (v3a): cascading mane arcs
# radiating from the head-cluster heart (r8,c10), 1:2 cell aspect baked in.
BEAST_SPAN = {
    3: (3, 13), 4: (1, 17), 5: (0, 18), 6: (0, 18), 7: (0, 19),
    8: (0, 19), 9: (0, 19), 10: (0, 18), 11: (0, 17), 12: (0, 16),
    13: (0, 16), 14: (0, 20), 15: (0, 20), 16: (0, 19), 17: (0, 18),
    18: (0, 16), 19: (0, 16), 20: (0, 17), 21: (0, 17), 22: (0, 16),
    23: (0, 15), 24: (0, 15), 25: (0, 14), 26: (0, 14), 27: (1, 20),
    28: (1, 21), 29: (1, 21), 30: (2, 21),
}
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
# Two great forepaws with heavy toes, trampling (v3a).
PB(27, 1, " ,‾,‾,‾, ", "mane")
PB(28, 1, " |o|o|o| ", "beast")
PB(29, 1, " |o|o|o| ", "beast")
PB(30, 1, " ´‾´‾´‾´ ", "mane")
PB(27, 12, " _,‾,‾,‾,_ ", "mane")
PB(28, 11, " (o|o|o|o) ", "beast")
PB(29, 11, " (o|o|o|o) ", "beast")
PB(30, 12, " ´‾´‾´‾´‾ ", "mane")

# ---------------------------------------------------------------- 7 heads
# GRAFT 1c (v3b): the crisper seven distinct silhouettes, on the mane.
# 1. LION on top: ears, wide muzzle, open jaw
PB(4, 4, " ,^,_,^, ", "mane")
PB(5, 4, " (o;‾;o) ", "beast")
P(5, 6, "o", "face")
P(5, 10, "o", "face")
PB(6, 5, " \\wvw/ ", "mane")
# 2. ANGEL, small radiant face at the cluster's left shoulder
P(7, 0, "'*'", "face")
PB(8, 0, "(o)", "face")
# 3. SATYR, horned grin at the cluster's right
P(7, 11, "\\", "mane")
P(7, 14, "/", "mane")
PB(8, 10, " (>e) ", "face")
# 4. SAINT, bearded, stern, the cluster's center
PB(9, 5, " ,--, ", "face")
PB(10, 4, " (o¡o) ", "face")
PB(11, 4, " \\vvv/ ", "face")
P(12, 6, "`v´", "face")
# 5. MAN OF VALOUR, helmeted profile
PB(9, 10, " [==] ", "face")
PB(10, 10, " [o<] ", "face")
# 6. ADULTEROUS WOMAN, calm heavy-lidded oval, lower-left
PB(11, 0, ",--,", "face")
PB(12, 0, "(e·e)", "face")
PB(13, 0, "`--´", "face")
# 7. POET, laurel band, dreaming eye (offset so the saint's chin survives)
PB(12, 9, " ,~~, ", "face")
PB(13, 9, " (e_) ", "face")

# ---------------------------------------------------------------- tail
# GRAFT 2b (v3c): the sun-lion emblem — gold rayed ring, lion-serpent head
# biting the crescent — with the tail coiling up to the corner and down
# the right edge to meet the hair (fills v3a's empty right).
PB(4, 40, " ,ss( ", "serpents")
PB(3, 42, " ,ss( ", "serpents")
PB(5, 36, " `\\¡/´ ", "beast")
PB(6, 34, " ,=´‾‾`=, ", "beast")
PB(7, 33, " <=(", "beast")
P(7, 37, "C", "face")
P(7, 38, "<e,", "serpents")
PB(7, 41, ")=> ", "beast")
PB(8, 36, " ,/¡\\, ", "beast")
PB(9, 41, " `\\s, ", "serpents")
PB(10, 42, " )ss) ", "serpents")
PB(11, 43, " (ss, ", "serpents")

# ---------------------------------------------------------------- hair
# Immense golden hair from her thrown-back head down the right edge (v3a).
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

# ---------------------------------------------------------------- saints
# Grey bloodless saints trampled at the base, group shaped like Shin (v3a).
PB(26, 20, " ,·, ", "saints")
PB(27, 19, " (-_-) ", "saints")
PB(27, 25, " ,·, ", "saints")
PB(28, 25, " (·_·) ", "saints")
PB(26, 31, " ,·, ", "saints")
PB(27, 30, " (-_-) ", "saints")
PB(29, 19, " `;,;;,;;,;´ ", "saints")
P(30, 22, ";·;", "saints")

# ---------------------------------------------------------------- circles
# GRAFT 2 (v3c): ten luminous rose rayed circles — the wide <(o)> glyph at
# the 2:1 cell aspect — scattered above and below, NOT in Tree order.
N_CIRCLES = 0


def circle(r, c):
    global N_CIRCLES
    PB(r - 1, c + 1, " ¡ ", "circles")
    PB(r, c - 1, " <(o)> ", "circles")
    N_CIRCLES += 1


circle(2, 7)      # on the band, over the Beast's crown (upper left)
circle(2, 33)     # on the band, right of the burst
circle(3, 29)     # right of the flame tongues
circle(7, 28)     # beside her raised arm
circle(10, 37)    # below the sun-lion emblem
circle(12, 19)    # left of her waist, over the Beast's back
circle(19, 32)    # right of the rein hand, riding the hair edge
circle(16, 42)    # ON the falling hair (as in the scan)
circle(25, 17)    # low, on the flank-side purple
circle(30, 35)    # among the trampled, lower right
assert N_CIRCLES == 10, f"need exactly 10 rayed circles, got {N_CIRCLES}"

# ---------------------------------------------------------------- babalon
# The rider, drawn ON TOP (v3a arc shifted +1 col: figure centroid verified
# on col 23 — v3a drifted to ~22). Dense % flesh so she pops against the
# stringy beast/hair texture. Head drawn LAST with P so torso/arm halos
# cannot punch the face (v3a's `%%‾´` artifact).
PB(9, 31, "    ", "face")  # narrow breathing halo above the thrown-back face
# torso reclining: shoulder r12 -> chest -> waist -> hips across the axis
PB(12, 25, " ,%%( ", "babalon")
PB(13, 24, " /%%%%) ", "babalon")
PB(14, 23, " /%%%´ ", "babalon")
PB(15, 21, " ,%%%%%( ", "babalon")
PB(16, 20, " (%%%%%%) ", "babalon")
PB(17, 16, " ,%%%%%%%´ ", "babalon")
# bent left leg: knee up-left, calf sweeping back down-right, pointed foot
PB(18, 14, " ,%%%´ ", "babalon")
PB(19, 14, " (%%\\ ", "babalon")
PB(20, 16, " `%%\\ ", "babalon")
PB(21, 18, " `%%\\ ", "babalon")
PB(22, 20, " `%%\\ ", "babalon")
PB(23, 22, " `%\\ ", "babalon")
PB(24, 24, " \\e´ ", "babalon")
# raised right arm: from the Grail base down to the shoulder
PB(8, 23, " \\% ", "babalon")
PB(9, 24, " \\% ", "babalon")
PB(10, 25, " \\% ", "babalon")
PB(11, 26, " \\%, ", "babalon")
# left (carnal) arm falling to the reins
P(14, 29, ")", "babalon")
P(15, 29, ")", "babalon")
P(16, 29, ")", "babalon")
P(17, 29, ")", "babalon")
P(18, 29, ")", "babalon")
PB(19, 27, " `w, ", "babalon")
# thrown-back head on top of everything: chin high, pale face to the sky
P(10, 30, " ,´o ", "face")
P(11, 29, " (%%‾´ ", "face")
P(12, 30, "´", "babalon")  # throat line into the shoulder, no doubled paren

# ---------------------------------------------------------------- reins
# Red reins from her left hand, the long loop hanging by the flank (v3a +1).
P(19, 25, "-~", "reins")
P(20, 28, "(", "reins")
P(20, 30, "\\", "reins")
P(21, 28, "(", "reins")
P(21, 31, ")", "reins")
P(22, 27, "(", "reins")
P(22, 31, ")", "reins")
P(23, 27, "(", "reins")
P(23, 31, ")", "reins")
P(24, 28, "(", "reins")
P(24, 30, ")", "reins")
P(25, 29, "U", "reins")

# ---------------------------------------------------------------- grail
# GRAFT 1 (v3b anatomy, v3a heat): the flaming Holy Grail raised high —
# flame tongues over blazing mouth over bowl over narrow stem, the card's
# climax and light source, center c22 (slight off-axis lift, authentic).
PB(1, 20, " ¡#¡ ", "flame")
PB(2, 19, " ,@#@, ", "flame")
PB(3, 18, " (@#@#@) ", "flame")
PB(4, 17, " ,%@@#@@%, ", "grail")
P(4, 20, "@@#@@", "flame")
PB(5, 17, " \\%%%%%%%/ ", "grail")
PB(6, 18, " `\\%%%/´ ", "grail")
P(7, 20, "`\\", "grail")
P(7, 22, "w", "babalon")
P(7, 23, "/´", "grail")
# stray sparks
P(3, 27, "'", "flame")
P(4, 15, "~", "flame")
P(4, 29, "~", "flame")
P(6, 16, "·", "flame")
P(6, 28, "·", "flame")

# ---------------------------------------------------------------- sig
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "11-lust-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "11-lust-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
