#!/usr/bin/env python3
"""Empress FINAL — ultracode panel synthesis (judge tally v3c 8, v3a 5, v3b 5).

BASE (v3c, heraldry-framed): the literal Salt-glyph doctrine — gold belt as
circle-on-bar ,===(o)===, with ONE central circle dead on the axis; the
readable lotus-arm (red sleeve curve to a c( hand, blue bloom at heart
level); the open low cradle hand; the (¡) infant in the green belly; the
disc+crescent revolving moons; and v3c's quiet corner heraldry — the
pelican feeding its brood (LL), the white double-eagle heater shield
holding the Moon (LR), Secret Rose + fish — everything centered.

GRAFT 1 (v3a): the luminous warm-white/cream CROWN-AND-HAIR mass — fanned
'''''''-arc veil rows around the head (the Harris scan's dominant color
note) — plus a small clear cream head gazing down under the crown.

GRAFT 2 (v3b): full-bleed enveloping vegetal field (smooth clump-noise
green masses, no black voids or dark pockets) and the luminous teal waters
band with the white \\¡/ fleur-de-lis carpet.

FIX 3: axis discipline — cross, orb, face, heart, belt circle, belly
infant, rose ALL dead on col 23.
FIX 4: moon-phase CROWN — waxing , ) / full (o) / waning ( , trio between
the horns, Maltese cross above.

Emits drafts/03-empress-final-art-lg.txt + drafts/03-empress-final-lg-classes.json
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
MIRROR = str.maketrans("()/\\[]{}<>`´,.", ")(\\/][}{><´`,.")


def P(r, c, s, cls):
    for i, ch in enumerate(s):
        if ch != " " and 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls


def PB(r, c, s, cls):
    """Place including spaces: spaces punch a 1-cell breathing halo."""
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


def PL(block, r0, c0, cls, bg=True):
    for dr, line in enumerate(block.splitlines()):
        if line:
            (PB if bg else P)(r0 + dr, c0, line, cls)


FLOOR_TOP = 27

# ---------------------------------------------------------------- 1. field
# GRAFT 2 (v3b): smooth 2-d clump noise (1:2 cell aspect baked into v)
# modulates density — soft rounded masses closing in around the figure,
# NO black voids. Inside the Daleth dome the growth thins to a pale
# sky-haze so the crowned head breathes against the Gate of Heaven.
A_CY, A_CX, A_RY, A_RX = 13.0, 23.0, 12.5, 19.5
for r in range(FLOOR_TOP):
    for c in range(W):
        u = c * 0.30
        v = r * 0.60
        n = math.sin(u + 1.3 * math.sin(v * 0.9)) \
            * math.cos(v * 0.8 + 0.9 * math.sin(u * 0.7))
        dens = 0.78 + 0.22 * n
        cls = "field"
        e = ((c - A_CX) / A_RX) ** 2 + ((r - A_CY) / A_RY) ** 2
        in_dome = e < 0.90 and r < 11
        if in_dome:
            dens *= 0.85
            cls = "arch"
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if h >= dens * 100:
            continue
        if in_dome:
            ch = ":" if h % 5 == 0 else ("·" if h % 3 else "'")
        elif dens > 0.90:
            ch = ";" if h % 3 else ":"
        elif dens > 0.74:
            ch = ":" if h % 3 else ";"
        elif dens > 0.62:
            ch = "·" if h % 3 else ":"
        else:
            ch = "," if h % 2 else "·"
        if cls == "field" and n > 0.55 and (r * 11 + c * 7) % 23 == 0:
            ch = "(" if c < AXIS else ")"
        P(r, c, ch, cls)

# ---------------------------------------------------------------- 2. arch
# The Door of Daleth: faint flank strokes shouldering the pale dome.
for r, c in ((3, 7), (4, 6), (5, 5)):
    P(r, c, "/", "arch")
    P(r, 46 - c, "\\", "arch")

# ---------------------------------------------------------------- 3. reeds
# Deep blue reed-trunks at both edges (v3c), fronds converging up top.
for r in range(FLOOR_TOP):
    sway = 1 if (r // 3) % 2 else 0
    P(r, 0, "({" if r % 2 else "{(", "reeds")
    P(r, 2 + sway, ")" if r % 3 else "}", "reeds")
    P(r, 44 - sway, "(" if r % 3 else "{", "reeds")
    P(r, 45, "})" if r % 2 else ")}", "reeds")
for r, c in ((0, 7), (1, 9), (0, 12), (2, 6)):
    P(r, c, "\\", "reeds")
    P(r, 46 - c, "/", "reeds")

# ---------------------------------------------------------------- 4. waters
# GRAFT 2 (v3b): luminous teal band of the waters of Universal Life.
for r in range(FLOOR_TOP, H):
    for c in range(W):
        P(r, c, "~-·-"[(c + r * 3) % 4], "floor")

# ---------------------------------------------------------------- 5. throne
# Twisted ropes of blue flame reading as blades of grass, flanking her.
for r in range(3, 17):
    PM(r, 10, "({" if r % 2 else "{(", "throne")
PM(2, 7, "S(", "throne")

# birds of Venus at the throne tops: sparrow left, dove right (mirrored).
PMB(1, 8, " ,v> ", "bird")

# ---------------------------------------------------------------- 6. moons
# BASE (v3c): disc+crescent revolving moons — waning upper right, waxing
# mid left (the one she faces).
PB(5, 37, "  _,--,_ ", "moon")
PB(6, 36, " (::::;( )", "moon")
PB(7, 36, " (::::;(_)", "moon")
PB(8, 37, "  `-,,-´ ", "moon")

PB(11, 1, " _,--,_  ", "moon")
PB(12, 0, "( );::::) ", "moon")
PB(13, 0, "(_);::::) ", "moon")
PB(14, 1, " `-,,-´  ", "moon")

# ---------------------------------------------------------------- 7. hair
# GRAFT 1 (v3a): luminous cream veil-fans arcing around the head, the
# scan's dominant note; the right lobe fuller, both clear of the moons.
PL("""  ,~-,,
 (''''';,
('''''''),
(''''''',)
(''''''),
 `-,,''')""", 2, 9, "hair")
PL("""  ,,-~,
 ,''''',
(''''''')
(''''''),
`,'''')
 `-,,')""", 2, 29, "hair")

# ---------------------------------------------------------------- 8. crown
# FIX 4: the moon-phase Crown of Isis — waxing ,) / full (o) / waning (,
# between the horns; Maltese cross above; green orb-body band below.
# Cross + at 23; full-moon o at 23; trio symmetric 18-19 / 22-24 / 27-28.
PB(0, 21, "  +  ", "cross")
P(0, 13, "\\", "crown")
P(0, 33, "/", "crown")
PB(1, 13, " \\_               _/ ", "crown")
P(1, 18, ",)", "moon")
P(1, 22, "(o)", "moon")
P(1, 27, "(,", "moon")
PB(2, 16, " `\\,,(;:;),,/´ ", "crown")
PB(3, 18, "  `,;;;,´  ", "crown")

# ---------------------------------------------------------------- 9. head
# GRAFT 1: small clear cream head, gazing gently down; eye dot on col 23.
PB(4, 20, " ,´‾`, ", "face")
PB(5, 20, " (;·,) ", "face")
PB(6, 20, " `-,-´ ", "face")

# ---------------------------------------------------------------- 10. torso
# BASE (v3c): passionate red blouse; the heart-bee * dead on col 23.
PB(7, 18, " ,(;;·;;), ", "blouse")
PB(8, 16, " ,(;;;;*;;;;), ", "blouse")
PB(9, 16, " (;·;;;;;;;·;) ", "blouse")
PB(10, 16, " (;;;;*;;;;;;) ", "blouse")
PB(11, 17, " );;;;;;;;;;( ", "blouse")
P(7, 22, ")(", "face")  # neckline V between the shoulders, on the axis

# ---------------------------------------------------------------- 11. lotus
# The blue lotus of Isis lifted before the heart, stems bunched down to
# the c( hand; red puffed sleeve on her right (the Salt bar's left arc).
PB(8, 12, " ,--, ", "blouse")
PB(9, 10, " (;;;) ", "blouse")
PB(10, 10, " (;;;;) ", "blouse")
PB(11, 11, " `-,,´ ", "blouse")
PB(5, 15, " ,v, ", "lotus")
PB(6, 14, " (v¡v) ", "lotus")
P(7, 17, "\\|", "stems")
P(8, 17, ")(", "stems")
PB(9, 16, " c( ", "face")

# ---------------------------------------------------------------- 12. cradle
# Her left arm: red puffed sleeve, then the flesh curve out and LOW, the
# open hand hovering in over the pregnant belly (the Salt bar's right arc).
PB(8, 27, " ,--, ", "blouse")
PB(9, 28, " (;;), ", "blouse")
PB(10, 31, " ), ", "face")
PB(11, 31, " ,) ", "face")
P(12, 29, ",,-´", "face")

# ---------------------------------------------------------------- 13. belt
# The Salt glyph made literal: ONE gold circle riding the bar, o on 23.
PB(12, 17, " ,===(o)===, ", "belt")

# ---------------------------------------------------------------- 14. skirt
# Mater Triumphans: the great green pregnant curve, infant ¡ on col 23,
# banded drape sweeping right as in the scan.
PB(13, 17, " ,;;;;;;;;;, ", "skirt")
PB(14, 16, " (;;;;(¡);;;;) ", "skirt")
PB(15, 15, " (;;;;;;;;;;;;;), ", "skirt")
PB(16, 14, " (;;;;;;;;;;;;;;;), ", "skirt")
PB(17, 13, " (;;;;;;;;;;);::;:;) ", "skirt")
PB(18, 13, " (;;;;;;;;;;;);::;;) ", "skirt")
PB(19, 14, " `,;;;;;;;;;);::;,´ ", "skirt")
PB(20, 15, "  );;;;;;;;);::;(  ", "skirt")
PB(21, 16, "  `,;;;;;;;;;,,´  ", "skirt")

# ---------------------------------------------------------------- 15. pelican
# BASE (v3c) LOWER LEFT: the white Pelican bent to feed its brood.
PB(20, 2, " ,~,     _,, ", "pelican")
PB(21, 1, " ( ´),  ,~´;) ", "pelican")
PB(22, 2, "  ),`v,;;;;)  ", "pelican")
PB(23, 2, "  (;;;;;;;;(  ", "pelican")
PB(24, 1, " ,(´o´o`o),´  ", "pelican")
PB(25, 2, " `--,,,--´  ", "pelican")

# ---------------------------------------------------------------- 16. shield
# BASE (v3c) LOWER RIGHT: heater shield, white double eagle, Moon in beaks.
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

# ---------------------------------------------------------------- 17. rose
# The Secret Rose at the foot of the throne, o and ¡ dead on col 23;
# two tiny fish adore it from the waters.
PB(25, 19, " _,(o),_ ", "rose")
PB(26, 19, " `,(¡),´ ", "rose")
PB(26, 14, " >o> ", "fleur")
PB(26, 28, " <o< ", "fleur")
P(27, 19, "~", "stems")
P(27, 23, "~", "stems")
P(27, 27, "~", "stems")

# ---------------------------------------------------------------- 18. carpet
# GRAFT 2 (v3b): white fleur-de-lis carpet over the teal waters.
P(28, 7, "\\¡/", "fleur")
P(28, 37, "\\¡/", "fleur")
P(29, 17, "\\¡/", "fleur")
P(29, 27, "\\¡/", "fleur")
P(30, 3, "\\¡/", "fleur")
P(30, 41, "\\¡/", "fleur")

# ---------------------------------------------------------------- 19. sig
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "03-empress-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "03-empress-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
