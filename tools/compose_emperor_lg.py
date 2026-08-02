#!/usr/bin/env python3
"""Compositor for Atu IV The Emperor, per drafts/04-emperor-fable5-prompt.md
and the Harris scan: PROFILE crowned king facing left, red patterned robe,
ram-headed sceptre raised in the right hand, orb-and-Maltese-cross at the
navel, CROSSED bare legs (the Sulphur glyph: triangle over cross), two great
Himalayan rams behind the throne, 16-point star disks on the throne arms,
sun-glow upper left, gold double-eagle shield with crimson disk lower left,
the white Lamb and Flag couchant lower right, angular flame-spikes all
around, fleur-de-lis floor marks.

Emits drafts/04-emperor-art-lg.txt + drafts/04-emperor-lg-classes.json
"""
import json, os

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


# ---- 1. the flame field: angular fire tongues + sun rays upper left ----
for r, c in [(2, 2), (4, 5), (7, 1), (9, 4), (12, 2), (15, 1), (18, 3),
             (21, 2), (10, 44), (13, 45), (16, 43), (19, 45), (22, 44),
             (8, 45), (24, 1), (24, 45)]:
    P(r, c, "^", "flames")
P(1, 1, "\\ | /", "sunrays")
P(2, 0, "-- --", "sunrays")
P(3, 1, "/ | \\", "sunrays")
for r, c, s in [(5, 0, "/"), (6, 2, "/"), (5, 8, "\\"), (6, 7, "\\")]:
    P(r, c, s, "sunrays")

# ---- 2. the two great rams behind the throne ----
PB(1, 3, " ,,--,__ ", "ram")
PB(2, 2, " ((@),´ ,`, ", "ram")
PB(3, 3, " `´ )__ ) ) ", "ram")
PB(4, 4, "  `--´`´ ", "ram")
PB(1, 33, " __,--,, ", "ram")
PB(2, 32, " ,´, `,((@)) ", "ram")
PB(3, 32, " ( ( __( `´ ", "ram")
PB(4, 33, "  `´`--´  ", "ram")

# ---- 3. crown + head in profile facing left ----
PB(4, 18, " \\¡/\\¡/ ", "crown")
PB(5, 18, " [====] ", "crown")
PB(6, 17, " ,´·-,| ", "face")
PB(7, 17, " (,;;,| ", "face")

# ---- 4. the ram-headed sceptre raised into the light ----
PB(4, 27, " ,(@) ", "sceptre")
P(5, 29, "|", "sceptre")
P(6, 29, "|", "sceptre")
P(7, 29, "|", "sceptre")
# the diagonal shaft of white light from the upper right
P(0, 43, "\\\\", "light")
P(1, 40, "\\\\", "light")
P(2, 37, "\\\\", "light")
P(3, 33, "\\\\", "light")

# ---- 5. the robe: red with gold bee/fleur pattern, Sulphur triangle ----
PB(8, 15, " ,(;·;;´;), ", "robe")
PB(9, 14, " (;;¡;;;·;;), ", "robe")
PB(10, 13, " (;·;;;¡;;;;;), ", "robe")
PB(11, 13, " (;;;;·;;;·;;;) ", "robe")
PB(12, 12, " (;;¡;;;;;;;¡;;) ", "robe")
PB(13, 12, " (;;;;·;;;;;;;;) ", "robe")
# right arm holding the sceptre shaft
P(8, 27, "(", "skin"); P(9, 26, "(", "skin")
P(10, 25, "`,", "skin")
# ---- 6. orb and Maltese cross at the navel ----
PB(12, 20, " + ", "cross")
PB(13, 19, " (o) ", "orb")
P(13, 17, ",´", "skin"); P(13, 23, "`,", "skin")

# ---- 7. the 16-point star disks on the throne arms ----
PB(11, 4, " -¡- ", "star")
PB(12, 3, " =(*)= ", "star")
PB(13, 4, " -¡- ", "star")
PB(11, 38, " -¡- ", "star")
PB(12, 37, " =(*)= ", "star")
PB(13, 38, " -¡- ", "star")

# ---- 8. the crossed bare legs: the CROSS beneath the triangle ----
PB(14, 13, " ,;;;;;;;;;;;, ", "robe")
PB(15, 14, " (__,,--––--,_ ".replace("–", "-"), "robe")
P(15, 15, "__,,--", "skin")
PB(16, 15, " ,--´\\ ", "skin")
PB(16, 21, "`--,_ ", "skin")
PB(17, 13, " ,-´   \\  ", "skin")
PB(17, 24, " `--,_ ", "skin")
PB(18, 19, "  \\ ", "skin")
PB(19, 19, " | \\ ", "skin")
PB(20, 19, " | | ", "skin")
PB(21, 19, " | | ", "skin")
PB(22, 19, " | | ", "skin")
PB(23, 18, " (__) ", "skin")

# ---- 9. the shield: gold, double-headed eagle, crimson disk ----
PB(19, 3, " ,======, ", "shield")
PB(20, 3, " |´     `| ", "shield")
P(20, 6, "(o)", "orb")
PB(21, 3, " |,/\\¡/\\,| ", "eagle")
PB(22, 3, " | >(¡)< | ", "eagle")
PB(23, 4, " \\ /||\\ / ", "eagle")
PB(24, 4, "  \\    /  ", "shield")
PB(25, 5, "   `--´   ", "shield")

# ---- 10. the Lamb and Flag, couchant at his feet ----
PB(21, 33, "     ,/ ", "lamb")
PB(22, 31, "  ,--,´|> ", "lamb")
PB(23, 30, " (´o )=,´ ", "lamb")
PB(24, 30, " (,,(___), ", "lamb")
PB(25, 31, "  ´´  ´´ ", "lamb")

# ---- 11. floor bands + fleur-de-lis marks ----
P(26, 0, "=" * 47, "floor")
P(28, 0, "-" * 47, "floor")
P(27, 4, "¡,", "fleur"); P(27, 40, "¡,", "fleur")
P(29, 9, "¡,", "fleur"); P(29, 35, "¡,", "fleur")
P(30, 20, "¡,", "fleur")
P(31, 0, "=" * 47, "floor")
P(31, 3, "aw", "sig")

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "04-emperor-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "04-emperor-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
