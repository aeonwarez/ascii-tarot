#!/usr/bin/env python3
"""Empress v3b — panel candidate B: VEGETAL-THRONE ENVELOPING.

The whole card is her garden. A full-bleed soft spring-green vegetal field
(rounded clump noise, never rays) wraps a nested figure dead on the axis;
the twisted blue-flame/grass throne ropes rise sinuously at both sides with
the sparrow and dove perched at their tops; the faint sky-blue Arch of
Daleth spans behind her; the revolving waning (upper right) and waxing
(lower left) moons ride in the growth. She: moon-horn Crown of Isis +
Maltese cross, profile facing right (per the Harris scan), great pale
hair-wings, red blouse with bee/domino flecks, blue lotus lifted to the
heart, the other arm curving low to cradle the pregnant belly (Salt glyph:
belly-circle riding the gold zodiac belt-bar), bright green banded skirt
sweeping gently right as she sits. Lower corners quiet: white pelican
feeding its brood (L), pale-gold shield with white double-eagle holding
the Moon (R); Secret Rose + two adoring fish over the teal waters floor.

Emits drafts/03-empress-v3b-art-lg.txt + drafts/03-empress-v3b-lg-classes.json
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
    """Place including spaces (spaces punch a 1-cell breathing halo)."""
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


FLOOR_TOP = 27

# ------------------------------------------------------------ vegetal field
# Soft rounded foliage clumps, full bleed. Smooth 2-d wave noise (1:2 cell
# aspect baked into v) modulates density; the hash dithers it. Clump cores
# get dense ';', rims thin to ',' and "'" — masses, never rays. Inside the
# Daleth dome (upper center) the growth thins to a pale sky-blue haze so
# the crowned head breathes against the Gate of Heaven.
ACY, ACX, ARY, ARX = 12.0, 23.0, 11.0, 20.5
for r in range(FLOOR_TOP):
    for c in range(W):
        u = c * 0.30
        v = r * 0.60
        n = math.sin(u + 1.3 * math.sin(v * 0.9)) \
            * math.cos(v * 0.8 + 0.9 * math.sin(u * 0.7))
        dens = 0.78 + 0.22 * n
        cls = "field"
        dome = ((c - ACX) / ARX) ** 2 + ((r - ACY) / ARY) ** 2
        in_dome = dome < 0.92 and r < 10
        if in_dome:
            dens *= 0.8
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
        # occasional leaf-curl accents at the clump cores
        if cls == "field" and n > 0.55 and (r * 11 + c * 7) % 23 == 0:
            ch = "(" if c < AXIS else ")"
        P(r, c, ch, cls)

# ------------------------------------------------------------ waters floor
for r in range(FLOOR_TOP, H):
    for c in range(W):
        k = (c + r * 3) % 4
        P(r, c, "~-·-"[k], "floor")

# ------------------------------------------------------------ Daleth arch
# Faint sky-blue door-arch spanning behind her; the figure breaks it later.
for r in range(0, 12):
    dyn = (r - ACY) / ARY
    s = 1 - dyn * dyn
    if s <= 0:
        continue
    x = ARX * math.sqrt(s)
    cl, cr = int(round(ACX - x)), int(round(ACX + x))
    if abs(dyn) > 0.93:
        for c in range(cl + 1, cr, 3):
            P(r, c, "‾", "arch")
    elif abs(dyn) > 0.6:
        P(r, cl, "/", "arch")
        P(r, cr, "\\", "arch")
    else:
        P(r, cl, "(", "arch")
        P(r, cr, ")", "arch")

# ------------------------------------------------------------ blue reeds
# Deep-blue reed-trees in the top corners, outside the arch.
for r in range(0, 12):
    for c in (0, 2, 4, 6):
        if ((c - ACX) / ARX) ** 2 + ((r - ACY) / ARY) ** 2 < 1.0:
            continue
        P(r, c, "(" if (r + c) % 2 else ")", "reeds")
        P(r, 46 - c, ")" if (r + c) % 2 else "(", "reeds")

# ------------------------------------------------------------ throne ropes
# Twisted ropes of blue flame reading as grass blades, sinuous S-drift,
# rising through the growth on both sides; born of the waters at the base.
# Halo-punched so the growth never camouflages the rope.
for r in range(3, 25):
    c = int(round(8.5 + 1.8 * math.sin(r * 0.55)))
    tw = " )( " if r % 2 else " }{ "
    PMB(r, c - 1, tw, "throne")
# outward curl at the tops
PMB(2, 6, " ,´ ", "throne")
PMB(1, 5, " ( ", "throne")
# base curls hooking inward toward the waters
PM(25, 12, "`,_", "throne")
PM(26, 14, "`-,", "throne")

# ------------------------------------------------------------ moons
# Revolving moons in the growth: waning upper right, waxing lower left.
PB(4, 37, "  _,-,  ", "moon")
PB(5, 36, " (:::( ) ", "moon")
PB(6, 37, " `-,-´  ", "moon")
PB(13, 2, "  ,-,_  ", "moon")
PB(14, 1, " ( )::) ", "moon")
PB(15, 2, " `-,-´  ", "moon")

# ------------------------------------------------------------ birds
# Sparrow (L) and dove (R) of Venus perched at the throne-rope tops.
PB(0, 5, " ,v> ", "bird")
PB(0, 38, " <v, ", "bird")

# ------------------------------------------------------------ hair-wings
# The great pale head-dress flames: two filled dithered masses sweeping
# out and down from the crown (mirrored about the axis).
PMB(1, 13, " ,,_ ", "hair")
PMB(2, 12, " ,;;,( ", "hair")
PMB(3, 11, " (;·;;( ", "hair")
PMB(4, 10, " (,;;·( ", "hair")
PMB(5, 10, " `,;;;( ", "hair")
PMB(6, 11, " `-,( ", "hair")

# ------------------------------------------------------------ crown
# Maltese cross over the green orb between the moon-horns (antimony echo:
# orb + cross). Visual center col 23.
PB(1, 19, " \\, + ,/ ", "cross")
P(1, 20, "\\,", "crown")
P(1, 25, ",/", "crown")
PB(2, 19, " \\,(o),/ ", "crown")
PB(3, 19, " `,;¡;,´ ", "crown")

# ------------------------------------------------------------ face
# Small crowned head, gaze gently down and to her right; long neck.
PB(4, 20, " (´·) ", "face")
PB(5, 20, " `,,´ ", "face")
PB(6, 21, " )( ", "face")

# ------------------------------------------------------------ torso
# Red blouse, bee/domino flecks in the weave.
PB(7, 18, " ,(;·;;), ", "blouse")
PB(8, 18, " (;;·;;;) ", "blouse")
PB(9, 17, " (;;;·;;;;) ", "blouse")
PB(10, 18, " );;;;;;( ", "blouse")

# ------------------------------------------------------------ lotus
# Blue lotus of Isis lifted to the heart in her right hand; green stems
# bunched down to the cupped hand.
PB(6, 13, " ,v, ", "lotus")
PB(7, 13, " (¡) ", "lotus")
P(8, 14, ")(", "stems")
PB(9, 12, " ,(´, ", "face")

# ------------------------------------------------------------ cradle arm
# Her left arm curves out and low, open hand over the belly (Salt glyph:
# the belly-circle rides the belt-bar).
PB(7, 27, " ,_ ", "face")
PB(8, 28, " `-,_ ", "face")
PB(9, 30, "  `,) ", "face")
PB(10, 29, "  _,´ ", "face")
PB(11, 26, " (,,,´ ", "face")

# ------------------------------------------------------------ zodiac belt
PB(11, 17, " ==*==o==*== ", "belt")

# ------------------------------------------------------------ skirt
# The pregnant belly + great green skirt; banded folds sweep gently right
# (she sits toward the waxing moon side of the garden).
PB(12, 18, " (;;;;;;;;;) ", "skirt")
PB(13, 17, " (;;;;;;;;;;;) ", "skirt")
PB(14, 16, " (;;;;;;;;;;;;;) ", "skirt")
PB(15, 15, " (;;;;;;;;;;;;;;;),, ", "skirt")
PB(16, 14, " (;;;;;;;;;;;;);;;;;, ", "skirt")
PB(17, 14, " (;;;;;;;;;;);;;);;;) ", "skirt")
PB(18, 15, " (;;;;;;;;;);;;);;;) ", "skirt")
PB(19, 16, " `,;;;;;;;;);;;;,-´ ", "skirt")
PB(20, 17, "  `--,,;;;;;,,--´ ", "skirt")
# the faint infant within the belly (Isis bearing Horus)
P(13, 23, "¡", "hair")

# ------------------------------------------------------------ pelican
# White pelican bending to feed its brood from her breast, lower left.
PB(21, 3, "  ,--,  ", "pelican")
PB(22, 2, " ( ´o`, ", "pelican")
PB(23, 3, "  `,\\\\,,~´) ", "pelican")
PB(24, 2, " ,(´o´o`), ", "pelican")
PB(25, 3, " `--,,,--´ ", "pelican")

# ------------------------------------------------------------ eagle shield
# Pale-gold heater shield, white double-headed eagle holding the small
# waxing Moon in its beaks; the o-over-¡ of body + tail hides Venus.
PB(21, 33, " ,=====, ", "shield")
PB(22, 33, " |\\(¡)/| ", "eagle")
PB(23, 33, " |>(o)<| ", "eagle")
PB(24, 33, " `,\\¡/,´ ", "eagle")
PB(25, 34, "  `-´  ", "shield")

# ------------------------------------------------------------ Secret Rose
# At the foot of the throne, over the spreading waters; two fish adore it.
PB(25, 19, " _,(*),_ ", "rose")
PB(26, 20, " `,( ),´ ", "rose")
P(26, 14, "><>", "fleur")
P(26, 29, "<><", "fleur")
# green-tinged waters of Universal Life spreading from the rose
P(27, 18, "~", "stems")
P(27, 22, "~", "stems")
P(27, 26, "~", "stems")

# ------------------------------------------------------------ floor fleurs
P(28, 7, "\\¡/", "fleur")
P(28, 36, "\\¡/", "fleur")
P(29, 17, "\\¡/", "fleur")
P(29, 27, "\\¡/", "fleur")
P(30, 3, "\\¡/", "fleur")
P(30, 41, "\\¡/", "fleur")

# ------------------------------------------------------------ signature
P(31, 2, "aw", "sig")

# ------------------------------------------------------------ emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "03-empress-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "03-empress-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
