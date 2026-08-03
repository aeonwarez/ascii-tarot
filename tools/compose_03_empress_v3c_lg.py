#!/usr/bin/env python3
"""Empress v3c — ultracode panel candidate C: HERALDRY-FRAMED.

Strategy: the pelican-feeding-its-young (lower left), the white double-eagle
shield holding the Moon (lower right) and the Secret Rose (bottom centre) are
balanced as three clear corner reads around a CALMER central figure; the base
register is a structured carpet of fleurs-de-lis + fish over green waters.
Crowley's cure governs: "disregard the parts, concentrate upon the whole" —
the field is one soft vegetal mass, the props stay small and quiet, and the
arms + belly + crown carry the figure.

Reads (Harris scan): profile goddess facing left dead on col 23, moon-horn
crown + green orb + Maltese cross, pale winged headdress, red blouse, blue
lotus to the heart, arm cradling the pregnant green skirt, gold zodiac belt,
waning moon upper right / waxing mid left, twisted blue throne-flames with
sparrow + dove, faint Daleth arch.

Emits drafts/03-empress-v3c-art-lg.txt + drafts/03-empress-v3c-lg-classes.json
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
    """Place including spaces: spaces punch a breathing halo."""
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


FLOOR_TOP = 28

# ---------------------------------------------------------------- 1. field
# One soft vegetal MASS, spring green, dithered — no rays, no black holes.
RAMP = ";;::··,;·"


def hsh(r, c):
    return (r * 37 + c * 59 + (r * c) % 13) % 100


for r in range(FLOOR_TOP):
    for c in range(W):
        h = hsh(r, c)
        if h >= 52:
            continue
        ch = RAMP[h % len(RAMP)]
        if h % 29 == 0:
            ch = "(" if (r + c) % 2 else ")"       # a leaf-curl now and then
        P(r, c, ch, "field")

# ---------------------------------------------------------------- 2. arch
# The Door of Daleth: a faint pale arch behind her, airy sky inside.
# Rim kept to the dome crest only — no diagonal rain down the sides.
A_CY, A_CX, A_RY, A_RX = 14.0, 23.0, 13.5, 17.5
for r in range(FLOOR_TOP):
    for c in range(W):
        if r > A_CY:
            continue
        e = ((c - A_CX) / A_RX) ** 2 + ((r - A_CY) / A_RY) ** 2
        if e < 0.88:                                # inside: clear + airy sky
            canvas[r][c] = " "
            classes[r][c] = None
            h = hsh(r, c)
            if h < (30 if r >= 8 else 24):
                P(r, c, "·'·:"[h % 4], "arch")
        elif e < 1.10 and r <= 6 and (r + c) % 2:   # crest rim, sparse
            dx = c - A_CX
            g = "‾" if abs(dx) < 9 else ("\\" if dx > 0 else "/")
            P(r, c, g, "arch")

# ---------------------------------------------------------------- 3. reeds
# Deep blue reed-trunks at both edges, full height, gentle curls;
# dark fronds converging at the top corners like the painting's canopy.
for r in range(FLOOR_TOP):
    sway = 1 if (r // 3) % 2 else 0
    P(r, 0, "({" if r % 2 else "{(", "reeds")
    P(r, 2 + sway, ")" if r % 3 else "}", "reeds")
    P(r, 44 - sway, "(" if r % 3 else "{", "reeds")
    P(r, 45, "})" if r % 2 else ")}", "reeds")
for r, c in ((0, 7), (1, 9), (0, 12), (1, 13), (2, 6)):
    P(r, c, "\\", "reeds")
    P(r, 46 - c, "/", "reeds")

# ---------------------------------------------------------------- 4. floor
# Green-tinged waters of Universal Life: structured teal wave register.
for r in range(FLOOR_TOP, H):
    for c in range(W):
        k = (c + r * 3) % 4
        ch = "~" if k == 0 else ("·" if k == 1 else ("-" if k == 2 else " "))
        canvas[r][c] = ch
        classes[r][c] = "floor" if ch != " " else None

# ---------------------------------------------------------------- 5. throne
# Twisted ropes of blue flame reading as blades of grass, flanking her.
for r in range(3, 15):
    P(r, 10, "({" if r % 2 else "{(", "throne")
    P(r, 35, "})" if r % 2 else ")}", "throne")
P(2, 10, "S(", "throne")
P(2, 35, ")S", "throne")

# birds of Venus at the throne tops: sparrow left, dove right
PB(1, 8, " ,v>  ", "bird")
PB(1, 33, "  <v, ", "bird")

# ---------------------------------------------------------------- 6. moons
# Waning upper right; waxing mid left (the one she faces). Dithered disks.
PB(5, 37, "  _,--,_ ", "moon")
PB(6, 36, " (::::;( )", "moon")
PB(7, 36, " (::::;(_)", "moon")
PB(8, 37, "  `-,,-´ ", "moon")

PB(11, 1, " _,--,_  ", "moon")
PB(12, 0, "( );::::) ", "moon")
PB(13, 0, "(_);::::) ", "moon")
PB(14, 1, " `-,,-´  ", "moon")

# ---------------------------------------------------------------- 7. hair
# The pale winged headdress: two big contiguous flame-lobes sweeping
# out-down from behind the horns to the shoulders (right one fuller).
PB(2, 11, " _,, ", "hair")
PB(3, 10, " ,;;;;`, ", "hair")
PB(4, 9, " ,;;;;;;( ", "hair")
PB(5, 8, " (;;;;;;;( ", "hair")
PB(6, 9, " );;;;;;) ", "hair")
PB(7, 10, " `,;;,-´ ", "hair")
PB(2, 31, " ,,_ ", "hair")
PB(3, 28, " ,;;;;`, ", "hair")
PB(4, 27, " );;;;;;`, ", "hair")
PB(5, 28, " );;;;;;;, ", "hair")
PB(6, 27, " (;;;;;;;;) ", "hair")
PB(7, 28, " `-;;;;,-´ ", "hair")

# ---------------------------------------------------------------- 8. crown
# Maltese cross over the green orb between wide moon-horns (antimony echo).
PB(0, 21, "  +  ", "cross")
PB(1, 14, " \\_    ,(o),    _/ ", "crown")
PB(2, 16, " `\\,,(;:;),,/´ ", "crown")
PB(3, 18, "  `,;;;,´  ", "crown")

# ---------------------------------------------------------------- 9. head
# Profile facing left, gazing gently down.
PB(4, 19, "  ,´·)  ", "face")
PB(5, 19, "  (,,(  ", "face")
PB(6, 20, "  );(  ", "face")

# ---------------------------------------------------------------- 10. torso
# Passionate red blouse, broad soft shoulders; tiny bee/domino marks.
PB(7, 18, " ,(;;·;;), ", "blouse")
PB(8, 16, " ,(;;;;*;;;;), ", "blouse")
PB(9, 16, " (;·;;;;;;;·;) ", "blouse")
PB(10, 16, " (;;;;*;;;;;;) ", "blouse")
PB(11, 17, " );;;;;;;;;;( ", "blouse")

# ---------------------------------------------------------------- 11. lotus
# The blue lotus of Isis lifted to the heart; stems to her right hand.
PB(4, 16, " ,v, ", "lotus")
PB(5, 15, " (v¡v) ", "lotus")
P(6, 17, "\\|", "stems")
P(7, 17, "\\|", "stems")
P(8, 17, ")(", "stems")
PB(9, 16, " c( ", "face")

# left arm curving LOW to cradle the belly (the Salt-glyph bar):
# one flowing curve from the right shoulder down and in to an open hand
PB(9, 29, " \\, ", "face")
PB(10, 30, " ), ", "face")
PB(11, 30, " ,) ", "face")
PB(12, 27, " ,-´ ", "face")

# ---------------------------------------------------------------- 12. belt
PB(12, 17, " ,===(o)===, ", "belt")

# ---------------------------------------------------------------- 13. skirt
# Mater Triumphans: the great green pregnant curve, faint infant inside.
PB(13, 17, " ,;;;;;;;;;, ", "skirt")
PB(14, 16, " (;;;;(¡);;;;) ", "skirt")
PB(15, 15, " (;;;;;;;;;;;;;), ", "skirt")
PB(16, 14, " (;;;;;;;;;;;;;;;), ", "skirt")
PB(17, 13, " (;;;;;;;;;;);::;:;) ", "skirt")
PB(18, 13, " (;;;;;;;;;;;);::;;) ", "skirt")
PB(19, 14, " `,;;;;;;;;;);::;,´ ", "skirt")
PB(20, 15, "  );;;;;;;;);::;(  ", "skirt")
PB(21, 16, "  `,;;;;;;;;;,,´  ", "skirt")

# ---------------------------------------------------------------- 14. pelican
# LOWER LEFT hero: the white Pelican bent to feed its brood from her breast:
# curved neck left, bill down to the breast, wing sweeping up-right, nest.
PB(20, 2, " ,~,     _,, ", "pelican")
PB(21, 1, " ( ´),  ,~´;) ", "pelican")
PB(22, 2, "  ),`v,;;;;)  ", "pelican")
PB(23, 2, "  (;;;;;;;;(  ", "pelican")
PB(24, 1, " ,(´o´o`o),´  ", "pelican")
PB(25, 2, " `--,,,--´  ", "pelican")

# ---------------------------------------------------------------- 15. shield
# LOWER RIGHT hero: heater shield, white double eagle, Moon in its beaks.
PB(20, 32, " ,=======, ", "shield")
PB(21, 32, " |       | ", "shield")
PB(22, 32, " |       | ", "shield")
PB(23, 32, " `,     ,´ ", "shield")
PB(24, 33, "  \\   /  ", "shield")
PB(25, 34, "   `-´   ", "shield")
P(21, 34, ">,", "eagle")
P(21, 36, "(o)", "moon")
P(21, 39, ",<", "eagle")
P(22, 34, ",\\;¡;/,", "eagle")
P(23, 36, ")¡(", "eagle")

# ---------------------------------------------------------------- 16. rose
# The Secret Rose at the foot of the throne; two tiny fish adore it.
PB(25, 19, " _,(o),_ ", "rose")
PB(26, 19, " `,(¡),´ ", "rose")
PB(26, 14, " >o> ", "fleur")
PB(26, 27, " <o< ", "fleur")

# ---------------------------------------------------------------- 17. carpet
# Structured base register: fleur-de-lis diamonds + fish over the waters.
for c0 in (4, 14, 30, 40):
    P(29, c0, ",¡,", "fleur")
for c0 in (9, 22, 35):
    P(30, c0, "<¡>", "fleur")
P(29, 24, "<o<", "fleur")
P(30, 3, ">o>", "fleur")
P(30, 42, "<o<", "fleur")

# ---------------------------------------------------------------- 18. sig
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "03-empress-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "03-empress-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
