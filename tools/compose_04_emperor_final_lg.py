#!/usr/bin/env python3
"""Emperor FINAL — panel synthesis (judge tally v3a 7 · v3b 7 · v3c 4).

BASE (v3a, chosen by 2 of 3 judges): the Sulphur-glyph figure skeleton —
the brocade TRIANGLE (bright /-\\ edges closed by the gold overline base)
from crown to lap over the CROSS of the legs (horizontal folded-leg bar
given real dithered mass + vertical pale shin on col 23 down to the bare
foot), the <+> Maltese cross over the crimson orb at the navel. The glyph
is protected by a 1-cell breathing gap along the / \\ edges.
GRAFT 1 (v3b): the near-full-bleed dense scarlet flame field (90%+, angular
^ tongues, thin dark rim kept around the silhouette) and the white light
shaft — parallel '/' rays bursting from the TOP-RIGHT corner, occluded by
the right ram capital, re-emerging as a wide band landing on the raised
gold ram's-head sceptre and right shoulder ('/' from upper right is the
correct slant; v3c's '\\' was wrong).
GRAFT 2 (v3b): the throne architecture — pale spiral-horn ram capitals on
dark stone posts, gold =((:*:))= star-disk medallions on the arm rails,
lattice throne-back in the side slots; the pale-gold heater shield with
double-headed eagle + crimson disk, low left.
GRAFT 3 (v3c): the four-point gold crown, the clearest white Lamb and Flag
(staff + pennant) low right, and a few of C's angular flame tongues at the
margins.
KEEP: bees + fleur-de-lys + looping arrow-tipped lines as robe brocade,
sun-glow disk behind the head, dark-red pavement with fleur marks, gaze
tipped to his left (toward the Empress), 'aw' signature.

Emits:
  drafts/04-emperor-final-art-lg.txt       47x32 art, full-bleed
  drafts/04-emperor-final-lg-classes.json  per-cell color classes
"""
import json, os

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
    P(r, int(2 * AXIS) - (c + len(s) - 1), s.translate(MIRROR)[::-1], cls)


def PMB(r, c, s, cls):
    PB(r, c, s, cls)
    PB(r, int(2 * AXIS) - (c + len(s) - 1), s.translate(MIRROR)[::-1], cls)


# ---------------------------------------------------------------- 1. field
# GRAFT 1 (v3b): full-bleed scarlet fire, dense — a WALL of flame red with
# angular ^ tongues, no black emptiness anywhere.
for r in range(27):
    for c in range(W):
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if h % 17 == 0:
            P(r, c, "^", "flames")
        elif h % 23 == 0:
            P(r, c, "/" if c < 23 else "\\", "flames")
        elif r < 8:
            if h < 90:
                P(r, c, "'·::;·"[h % 6], "field")
        elif r < 18:
            if h < 93:
                P(r, c, ";:·,;·;:"[h % 8], "field")
        else:
            if h < 94:
                P(r, c, ";:,;;·:,;;"[h % 10], "field")

# ---------------------------------------------------------------- 2. dais
# KEEP: dark-red pavement; fleur marks added at the end.
P(27, 0, "=" * W, "floor")
for r in range(28, H):
    for c in range(W):
        h = (r * 31 + c * 17) % 10
        if h < 9:
            P(r, c, ";;:,;;;:,;"[h], "floor")

# ---------------------------------------------------------------- 3. sun
# KEEP: gold sun-glow disk behind the crowned head (Sol exalted in Aries),
# v3b's star dither; the head punches through it.
SY, SX = 3.0, 20.0
for r in range(0, 8):
    for c in range(10, 31):
        dx = (c - SX) / 9.0
        dy = (r - SY) * 2.0 / 9.0
        if dx * dx + dy * dy <= 1.0:
            h = (r * 41 + c * 13) % 100
            if h < 82:
                P(r, c, "*'·*''"[h % 6], "sunrays")
P(0, 14, "\\", "sunrays")
P(0, 26, "/", "sunrays")
# thin gold geometry-rays cutting down-left from the sun (Harris's ray
# lines); the throne post crosses over them
for r, c in ((5, 12), (6, 11), (7, 9), (8, 8), (9, 7), (10, 5),
             (11, 4), (12, 2)):
    P(r, c, "/", "sunrays")

# ---------------------------------------------------------------- 4. light
# GRAFT 1 (v3b): white shaft from the TOP-RIGHT corner — parallel '/' rays
# drawn BEFORE the ram capital + post so the architecture occludes them;
# the band re-emerges beneath and lands on the sceptre + right shoulder.
def ray(r0, c0, r1, c1):
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = int(round(r0 + (r1 - r0) * i / steps))
        c = int(round(c0 + (c1 - c0) * i / steps))
        P(r, c, "/", "light")


ray(0, 46, 11, 32)
ray(0, 45, 11, 31)
ray(0, 44, 11, 30)
ray(0, 43, 11, 29)
P(0, 40, "·", "light")
P(1, 38, "·", "light")

# ---------------------------------------------------------------- 5. throne
# GRAFT 2 (v3b): dark stone posts, pale spiral-horn ram capitals, lattice
# throne-back in the side slots.
for r in range(5, 12):
    P(r, 5, "[::]", "floor")
for r in range(6, 12):
    P(r, 38, "[::]", "floor")

PB(1, 1, "  _,,--,_  ", "ram")
PB(2, 0, " ((@))';;;,_ ", "ram")
PB(3, 0, " ((@));;;;;;) ", "ram")
PB(4, 1, "  `´(;;o;;;) ", "ram")
PB(5, 3, "   `;;,;;´ ", "ram")
PB(1, 36, " _,,--,_  ", "ram")
PB(2, 34, " ,;;;';((@)) ", "ram")
PB(3, 34, " (;;;;;;((@)) ", "ram")
PB(4, 35, " `;;o;;;)`´ ", "ram")

for r in range(6, 25):
    for c in list(range(9, 18)) + list(range(29, 38)):
        if (r + 2 * c) % 5 == 0 and classes[r][c] not in (
                "light", "floor", "sunrays", "ram"):
            P(r, c, "x", "floor")

# ---------------------------------------------------------------- 6. spikes
# GRAFT 3 (v3c): angular flame tongues at the margins.
def spike(rtop, c, h):
    P(rtop, c, "^", "flames")
    for i in range(1, h):
        off = (i + 1) // 2
        P(rtop + i, c - off, "/", "flames")
        P(rtop + i, c + off, "\\", "flames")


for rt, c, h in [(7, 2, 3), (9, 44, 3), (16, 3, 4), (17, 43, 4),
                 (23, 14, 3), (22, 28, 3), (16, 34, 3), (25, 29, 2)]:
    spike(rt, c, h)

# ---------------------------------------------------------------- 7. FIGURE
# BASE (v3a) with v3c's crown. Crown: four gold points + band, dead on 23.
PB(0, 18, "  ¡v¡v¡v¡  ", "crown")
PB(1, 17, "  [=======]  ", "crown")
# face: frontal, bearded, the gaze tipped to his left (toward the Empress)
PB(2, 19, "  (o·,)  ", "face")
PB(3, 19, "  (;;;)  ", "face")
PB(4, 20, "  );(  ", "face")
PB(5, 18, "  <=====>  ", "crown")               # gold collar

# the TRIANGLE: head+arms one widening brocade mass, bright /-\ edges,
# 1-cell breathing gap so the glyph pops out of the dense field
ROBE_TOP, ROBE_BOT = 6, 14
for r in range(ROBE_TOP, ROBE_BOT + 1):
    half = int(round(4 + (r - ROBE_TOP) * 10 / 8))
    lo, hi = 23 - half, 23 + half
    body = []
    for c in range(lo + 1, hi):
        h = (r * 41 + c * 67 + (r * c) % 13) % 100
        body.append(";%;;&;;;"[h % 8])
    PB(r, lo - 1, " /" + "".join(body) + "\\ ", "robe")
    P(r, lo, "/", "cross")
    P(r, hi, "\\", "cross")
# the closed gold BASE of the triangle (the lap) — the glyph must read
PB(15, 8, " " + "‾" * 29 + " ", "cross")
# KEEP: robe brocade — bees *, fleur ¡, loops-with-arrowheads e>
for r, c, s in [(7, 21, "e>"), (8, 18, "*"), (8, 26, "*"), (9, 19, "e>"),
                (10, 17, "¡"), (10, 27, "e>"), (11, 15, "*"), (11, 28, "¡"),
                (12, 17, "e>"), (12, 27, "*"), (13, 13, "¡"), (13, 30, "e>"),
                (14, 16, "*"), (14, 28, "¡"), (13, 20, "*"), (14, 22, "e>")]:
    P(r, c, s, "pattern")
# left hand + orb-and-Maltese-cross at the navel (on the axis)
P(10, 22, "<+>", "cross")
PB(11, 19, "  (@@@)  ", "orb")
PB(12, 19, "  (;;;)  ", "skin")
# right hand rising toward the sceptre
PB(9, 25, " (;) ", "skin")

# ------------------------------------------------------------- 8. sceptre
# Ram's-head finial raised into the re-emerging light band beneath the
# right ram capital; shaft crossing down over the rim into the hand.
PB(4, 31, " ,--, ", "sceptre")
PB(5, 31, " ((@) ", "sceptre")
P(6, 32, "`¡´", "sceptre")
for r, c in [(7, 31), (8, 30), (9, 29)]:
    P(r, c, "/", "sceptre")

# ---------------------------------------------------------------- 9. legs
# The CROSS beneath the triangle. Vertical pale shin on col 23 first
# (crossed UNDER), then the folded-leg bar with real dithered mass drawn
# over it, then the tucked foot and the bare foot on the pavement.
for r in range(16, 26):
    PB(r, 19, "  (;" + "':"[r % 2] + ";)  ", "skin")
PB(18, 11, " ,;;;;;;;;;;;;;;;;;;;;;, ", "skin")
PB(19, 11, " (;:;;';;:;;;':;;:;;';;=, ", "skin")
PB(20, 12, " `';;,__,;;;;,__,;;,´ ", "skin")
PB(21, 31, "  `;=´  ", "skin")
# the bare foot on the pavement
PB(26, 17, "  ,(;;;;;),  ", "skin")
PB(27, 18, "  `‾‾‾‾‾´  ", "skin")

# --------------------------------------------------------------- 10. shield
# GRAFT 2 (v3b): pale-gold heater shield, crimson disk above the
# double-headed eagle, low left.
PB(19, 1, ",=========,", "shield")
PB(20, 1, "|'       '|", "shield")
P(20, 5, "(o)", "orb")                         # the crimson disk (red tincture)
PB(21, 1, "|,/\\ ¡ /\\,|", "eagle")
PB(22, 1, "|( >(¡)< )|", "eagle")
PB(23, 1, "| (;;¡;;) |", "eagle")
PB(24, 1, " \\,\\;|;/,/ ", "eagle")
PB(25, 2, " \\;;;;;/ ", "shield")
PB(26, 3, "  `-,-´  ", "shield")

# ---------------------------------------------------------------- 11. lamb
# GRAFT 3 (v3c): the white Lamb and Flag couchant, staff + pennant, low right.
PB(21, 40, " ,¡ ", "lamb")
PB(22, 36, " ,--,´|> ", "lamb")
PB(23, 34, " ,(´o )=,´ ", "lamb")
PB(24, 34, " (,,(___), ", "lamb")
PB(25, 35, "  ´´  ´´ ", "lamb")

# --------------------------------------------------------------- 12. stars
# GRAFT 2 (v3b): gold star-disk medallions on the arm rails — drawn after
# the figure so the triangle's halo cannot chew them.
PMB(12, 0, " ,`\\¡/´, ", "star")
PMB(13, 0, "=((:*:))=", "star")
PMB(14, 0, " `,/¡\\,´ ", "star")

# --------------------------------------------------------------- 13. fleurs
PB(29, 5, " \\¡/ ", "fleur")
PB(30, 6, " ¡ ", "fleur")
PB(29, 38, " \\¡/ ", "fleur")
PB(30, 39, " ¡ ", "fleur")
P(30, 22, ",¡,", "fleur")

# ------------------------------------------------------------------ 14. sig
PB(31, 1, " aw ", "sig")

# ----------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "04-emperor-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "04-emperor-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
