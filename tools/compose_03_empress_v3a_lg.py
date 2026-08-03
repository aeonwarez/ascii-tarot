#!/usr/bin/env python3
"""Empress v3a — panel strategy A: FIGURE + SALT-ARMS DOMINANT.

The pregnant goddess is the hero, drawn LARGE and dead on the axis (col 23):
moon-phase Crown of Isis + Maltese cross over the dark orb, pale flame-hair
sweeping both sides, red blouse, blue lotus lifted to the heart in her right
hand, left arm curving low to cradle the rounded green belly (the alchemical
Salt glyph: circle riding the bar of the arms), gold zodiac girdle, great
green skirt sweeping right as in the Harris scan. Everything else recedes:
faint Daleth arch, deep-blue reeds at the edges, small revolving moons,
twisted blue-flame throne with sparrow + dove, quiet pelican / eagle-shield
heraldry in the lower corners, Secret Rose + fish + fleur tapestry at the
foot. Field is soft vegetal dithered MASS, full-bleed — no rays, no void.

Emits drafts/03-empress-v3a-art-lg.txt + drafts/03-empress-v3a-lg-classes.json
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
    """Place including spaces (spaces punch a 1-cell breathing halo)."""
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


def PM(r, c, s, cls):
    P(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    P(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def PL(block, r0, c0, cls, bg=True):
    for dr, line in enumerate(block.splitlines()):
        (PB if bg else P)(r0 + dr, c0, line, cls)


# ------------------------------------------------------------ vegetal field
# Soft leafy MASS, full-bleed: spring-green dither everywhere, a lighter
# sky-blue zone inside the Daleth arch up top, denser green outside it.
FLOOR_TOP = 28


def arch_e(r, c):
    dx = (c - 23.0) / 21.5
    dy = (r - 18.0) / 16.5
    return dx * dx + dy * dy


def calm(r, c):
    """Quiet halo ellipse around head/torso so she reads clean; the
    vegetation closes back in around the skirt and below."""
    dx = (c - 23.0) / 13.0
    dy = (r - 8.0) / 7.5
    return dx * dx + dy * dy < 1.0


for r in range(FLOOR_TOP):
    for c in range(W):
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        e = arch_e(r, c)
        if calm(r, c):
            if h < 21:
                P(r, c, "·'"[h % 2], "field")
        elif e < 1.0 and r <= 11:
            # pale sky inside the arch
            if h < 22:
                P(r, c, "·'·,"[h % 4], "arch")
        elif e < 1.0:
            # vegetation inside the arch (mostly behind the figure)
            if h < 32:
                P(r, c, ";·';,"[h % 5], "field")
        else:
            # dense growth outside the arch, occasional leaf curls
            if h % 19 == 0:
                P(r, c, "()"[c % 2], "field")
            elif h < 62:
                P(r, c, ";:;·';"[h % 6], "field")

# ------------------------------------------------------------ Daleth arch
# The faint Door of Heaven behind her (garnish; drawn sparse over the field).
for r in range(2, 19):
    dy = (r - 18.0) / 16.5
    s = 1 - dy * dy
    if s < 0:
        continue
    x = 21.5 * math.sqrt(s)
    cl, cr = int(round(23 - x)), int(round(23 + x))
    if r % 2 == 0:
        P(r, cl, "(", "arch")
        P(r, cr, ")", "arch")
PM(1, 18, "_,-", "arch")

# ------------------------------------------------------------ blue reeds
# Deep-blue reed-trunks fanning down the edges, as in the scan.
for r in range(0, 17):
    lw = "({" if r % 2 else "((" if r % 3 else "{("
    P(r, 0, lw[: 2], "reeds")
    P(r, 45 - (r % 2), "})" if r % 2 else ")}", "reeds")
for r in range(17, 24):
    P(r, 0, "(" if r % 2 else "{", "reeds")
    P(r, 46, ")" if r % 2 else "}", "reeds")
# fan strands slanting in at the top corners
P(0, 3, "\\", "reeds"); P(1, 4, "\\", "reeds"); P(2, 5, "\\,", "reeds")
P(0, 6, "\\", "reeds"); P(1, 7, "\\", "reeds")
P(0, 43, "/", "reeds"); P(1, 42, "/", "reeds"); P(2, 40, ",/", "reeds")
P(0, 40, "/", "reeds"); P(1, 39, "/", "reeds")

# ------------------------------------------------------------ moons
# waning: grey disc upper right; waxing crescent mid-left (she faces it)
PB(4, 37, "  _,--,_ ", "moon")
PB(5, 37, " (::::::) ", "moon")
PB(6, 37, " `--,--´) ", "moon")
PB(13, 1, " _,-,_ ", "moon")
PB(14, 0, " ( (:::) ", "moon")
PB(15, 1, " `-,--´ ", "moon")

# ------------------------------------------------------------ throne
# twisted blue-flame / grass uprights behind her, birds perched at the tops
for r in range(4, 19):
    t = ("}{", ")(", "}(", "){")[r % 4]
    P(r, 7, t, "throne")
    P(r, 38, t, "throne")
P(6, 7, "s(", "throne")
P(6, 38, ")s", "throne")
PB(2, 5, " ,v>  ", "bird")
PB(3, 7, " )( ", "throne")
PB(2, 36, "  <v, ", "bird")
PB(3, 38, " )( ", "throne")

# ------------------------------------------------------------ floor
for c in range(W):
    P(28, c, "~-"[c % 2], "floor")
    P(31, c, "-~"[c % 2], "floor")
for r in (29, 30):
    for c in range(W):
        h = (r * 31 + c * 7) % 9
        if h == 0:
            P(r, c, "·", "floor")
# fleur-de-lis diamonds + tiny fish adoring the Rose
P(29, 4, "¡,", "fleur"); P(29, 38, "¡,", "fleur")
P(30, 9, "¡,", "fleur"); P(30, 33, "¡,", "fleur")
P(29, 13, ">o>", "fleur"); P(29, 30, "<o<", "fleur")

# ------------------------------------------------------------ Secret Rose
PB(29, 19, " _,(o),_ ", "rose")
PB(30, 20, " `,;,´ ", "rose")
P(30, 15, "~", "floor"); P(30, 29, "~", "floor")

# ------------------------------------------------------------ pelican
# white Pelican feeding her brood, lower LEFT, small and quiet
PB(22, 2, " ,~,     ", "pelican")
PB(23, 1, " ( ´), ", "pelican")
PB(24, 2, " `\\_ \\_,,~, ", "pelican")
PB(25, 3, "  ,\\\\\\,,~´ ", "pelican")
PB(26, 2, " ,(´o´o`), ", "pelican")
PB(27, 3, " `~,,,~´ ", "pelican")

# ------------------------------------------------------------ eagle shield
# white double-headed eagle holding the waxing Moon, lower RIGHT
PB(22, 35, " ,======, ", "shield")
PB(23, 35, " |´)\\;/(`| ", "eagle")
PB(24, 35, " | >", "eagle"); P(24, 39, "(o)", "moon"); PB(24, 42, "< | ", "eagle")
PB(25, 35, " `,/¡{¡\\,´ ", "eagle")
PB(26, 36, "  \\    /  ", "shield")
PB(27, 37, "   `--´   ", "shield")

# ================================================================= FIGURE
# drawn LAST, halo-punched — she sits ON TOP of everything.

# ---- pale flame-hair: two big soft masses filling the upper interior ----
PL("""  ,~-,,
 (''''';,
('''''''),
(''''',,-´
(''''''),
(''''''';,
 `,''''''),
  `-,,''',)
""", 1, 10, "hair")
PL("""  ,,-~,
 ,´'''';,
('''''''';,
(''''''''''),
('''''''',,-´
 `,''''';,
   `-,,''')
""", 1, 26, "hair")

# ---- Crown of Isis: Maltese cross, dark orb, gold moon-horns, cap ----
PB(0, 20, "   +   ", "cross")
PB(1, 16, " \\\\,  (@)  ,// ", "crown")
PB(2, 16, " \\`-,,(;),,-´/ ", "crown")
PB(3, 17, " `-,(;;;),-´ ", "crown")

# ---- head in profile facing left, gazing gently down ----
PB(4, 19, " ,´;;), ", "face")
PB(5, 19, " (;;·(  ", "face")
PB(6, 19, " `,;,(  ", "face")
PB(7, 20, "  );( ", "face")

# ---- torso: red blouse, puffed sleeves, two bees as tiny flecks ----
PB(8, 17, " ,(;;;;;;), ", "blouse")
PB(9, 16, " (;;;;;;;;;;), ", "blouse")
PB(10, 16, " (;;*;;;;;;;;) ", "blouse")
PB(11, 16, " (;;;;;;;;*;;) ", "blouse")
PB(12, 17, " );;;;;;;;;;( ", "blouse")
# left (her right) sleeve puff with the spiral rose, forearm to the fist
PB(9, 12, " ,--, ", "blouse")
PB(10, 11, " (;@;), ", "blouse")
PB(11, 11, " (;;;;) ", "blouse")
PB(12, 12, " `-,,´ ", "blouse")
# ---- the blue lotus lifted to the HEART (Salt: circle over the bar) ----
PB(7, 16, " ,vv, ", "lotus")
PB(8, 16, " (¡¡) ", "lotus")
P(9, 18, "\\|", "stems")
P(10, 18, ")(", "stems")
PB(11, 17, " (,) ", "face")
# ---- right (her left) arm curving LOW to cradle the belly ----
PB(9, 28, " ,~, ", "blouse")
PB(10, 28, " (;;;), ", "blouse")
PB(11, 30, " `,;`, ", "face")
PB(12, 31, "  );;) ", "face")
PB(13, 30, " _,;,´ ", "face")
PB(14, 26, " \\__,,´ ", "face")

# ---- gold zodiac girdle ----
PB(13, 17, " ,==o==o==, ", "belt")

# ---- the great green skirt: pregnant belly + drape sweeping right ----
PB(14, 15, " ,(''''), ", "skirt")
PB(15, 14, " (;''''';;`-, ", "skirt")
PB(16, 13, " (;;''''';;;;;`, ", "skirt")
PB(17, 13, " (;;;'e';;;;);;;;;`, ", "skirt")
PB(18, 13, " (;;;;;;;;;);;;;;;;), ", "skirt")
PB(19, 14, " `,;;;;;;;;);;;;;;;;) ", "skirt")
PB(20, 15, "  `-,;;;;;;);;;;;,-´ ", "skirt")
PB(21, 17, "   `);;;;;;;,-´ ", "skirt")

# ------------------------------------------------------------ signature
P(30, 2, "aw", "sig")

# ------------------------------------------------------------ emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "03-empress-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "03-empress-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
