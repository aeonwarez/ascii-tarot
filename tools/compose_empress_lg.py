#!/usr/bin/env python3
"""Compositor for Atu III The Empress, per drafts/03-empress-fable5-prompt.md
and the Harris scan: PROFILE goddess facing left (painting corrects the
prompt's "frontal"), moon-phase crown with green orb + Maltese cross, white
headdress sweeping behind, red patterned blouse, blue lotus to the heart,
arm cradling the pregnant green-skirted belly (Salt glyph), gold zodiac
belt; the Daleth arch and blue reed-trees behind; waning moon upper right,
waxing lower left; white pelican with brood lower left, double-eagle shield
lower right, secret rose + fleur-de-lis floor.

Emits drafts/03-empress-art-lg.txt + drafts/03-empress-lg-classes.json
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


def PL(block, r0, c0, cls, bg=False):
    for dr, line in enumerate(block.splitlines()):
        (PB if bg else P)(r0 + dr, c0, line, cls)


# ---- 1. blue reed-trees at the edges (Daleth arch hints painted last) --
for r in range(0, 15):
    w = "){(" if r % 2 else "(}{"
    P(r, 0, w[: 2 + (r % 2)], "reeds")
    P(r, 44, w[: 2 + ((r + 1) % 2)], "reeds")
for r in range(15, 22):
    P(r, 0, "({", "reeds"); P(r, 45, "})", "reeds")
# sparrow (left reed) and dove (right reed)
PB(1, 3, " ,v> ", "bird")
PB(2, 39, " <v, ", "bird")

# ---- 2. the crown: Maltese cross over green orb between moon-horns ----
PB(2, 19, "  +  ", "cross")
PB(3, 17, " \\,(o),/ ", "crown")
PB(4, 18, " `,¡,´  ", "crown")

# ---- 3. head in profile facing left + sweeping white headdress ----
PB(5, 18, " ,´·) ", "face")
PB(6, 18, " (,,( ", "face")
PB(4, 24, "`~--,_", "hair")
PB(5, 23, " )   `~-,_ ", "hair")
PB(6, 23, " `~-,_   `, ", "hair")
PB(7, 24, "   `-,)  ", "hair")

# ---- 4. torso: red blouse, lotus to the heart, Salt-glyph arms ----
PB(7, 16, " ,(;·;), ", "blouse")
PB(8, 15, " (;;·;;;), ", "blouse")
PB(9, 15, " (;·;;;·;) ", "blouse")
PB(10, 15, " (;;;·;;;) ", "blouse")
# blue lotus lifted to the heart, green stems
PB(6, 12, " ,v, ", "lotus")
PB(7, 12, " (¡) ", "lotus")
P(8, 13, "\\|", "stems")
P(9, 13, ")(", "stems")
# left arm curving low to cradle the belly
P(10, 24, ",_", "face")
P(11, 25, "`-,", "face")
P(12, 25, ",-´", "face")

# ---- 5. the pregnant belly / great green skirt + gold zodiac belt ----
PB(11, 14, " ==(o)== ", "belt")
PB(12, 13, " ,;;;;;;;, ", "skirt")
PB(13, 12, " (;;;;;;;;;)_ ", "skirt")
PB(14, 11, " (;;;;;;;;;;;;`, ", "skirt")
PB(15, 11, " (;;;;;;;;;;;;;;), ", "skirt")
PB(16, 12, " (;;;;;;;;;;;;;;;) ", "skirt")
PB(17, 13, " `,;;;;;;;;;;;;;;) ", "skirt")
PB(18, 14, "  `--,;;;;;;;;;;( ", "skirt")
PB(19, 18, "  (;;;;;;;;;) ", "skirt")
PB(20, 19, "  );;;;;;;( ", "skirt")

# ---- 6. the revolving moons: waning upper right, waxing lower left ----
PB(7, 38, "  _,-,  ", "moon")
PB(8, 37, " (:::( ) ", "moon")
PB(9, 38, " `-,-´  ", "moon")
PB(13, 4, " ,-,_  ", "moon")
PB(14, 3, " ( )::) ", "moon")
PB(15, 4, " `-,-´ ", "moon")

# ---- 7. the twisted blue-flame throne uprights, behind her ----
for r in range(6, 12):
    P(r, 31, ")(" if r % 2 else "}{", "throne")
for r in range(12, 18):
    P(r, 33, ")(" if r % 2 else "}{", "throne")

# ---- 8. the white pelican feeding its brood, lower left ----
PB(20, 2, "  ,--,   ", "pelican")
PB(21, 1, " ( ´o`,  ", "pelican")
PB(22, 2, "  `,  \\_,,~´) ", "pelican")
PB(23, 3, "  `,\\\\\\\\,~´ ", "pelican")
PB(24, 2, " ,(´o´o´o`), ", "pelican")
PB(25, 3, " `--,,,--´ ", "pelican")

# ---- 9. the shield: white double-headed eagle holding the Moon ----
PB(20, 30, " ,=======, ", "shield")
PB(21, 30, " |´)\\¡/(`| ", "shield")
PB(22, 30, " | >(o)< | ", "eagle")
PB(23, 30, " `,/¡{¡\\,´ ", "eagle")
PB(24, 31, " \\     / ", "shield")
PB(25, 32, "  `-,-´  ", "shield")
# Daleth arch hints, over the reeds
P(2, 9, "_,,-", "arch"); P(2, 34, "-,,_", "arch")
P(3, 7, ",´", "arch"); P(3, 38, "`,", "arch")
P(4, 6, "/", "arch"); P(4, 40, "\\", "arch")
P(5, 5, "/", "arch"); P(5, 41, "\\", "arch")

# ---- 10. the Secret Rose + waters + fleur-de-lis and fish floor ----
PB(26, 18, " _,(o),_ ", "rose")
PB(27, 18, " `,(´),´ ", "rose")
P(28, 0, "~-" * 23 + "~", "floor")
P(29, 2, "¡,", "fleur"); P(29, 12, "<o<", "fleur"); P(29, 22, "¡,", "fleur")
P(29, 32, "<o<", "fleur"); P(29, 42, "¡,", "fleur")
P(30, 7, "<o<", "fleur"); P(30, 17, "¡,", "fleur"); P(30, 27, "<o<", "fleur")
P(30, 37, "¡,", "fleur")
P(31, 0, "~" + "-~" * 23, "floor")
P(31, 3, "aw", "sig")

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "03-empress-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "03-empress-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
