#!/usr/bin/env python3
"""Emperor v3B — THRONE-ARCHITECTURE dominant (ultracode panel, composer B).

The ram-headed throne and the regalia of rule framed foremost: pale
Himalayan wild-ram capitals (double-spiral horns) atop dark stone throne
posts, arm rails carrying 16-point star-disk medallions at their outer
ends, red lattice throne-back, the gold four-point crown + sun glow, the
ram-headed sceptre raised toward the diagonal white light shaft from the
upper right, the Maltese-cross orb at the navel, the pale-gold heater
shield with the double-headed eagle + crimson disk lower left, the white
Lamb and Flag couchant lower right — the Emperor seated WITHIN the
architecture, his body still tracing the Sulphur glyph (triangle of
head+arms over the cross of the legs), everything on a full-bleed
scarlet flame field with angular fire blades. No black emptiness.

Emits:
  drafts/04-emperor-v3b-art-lg.txt       47x32 art, full-bleed
  drafts/04-emperor-v3b-lg-classes.json  per-cell color classes
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
# Full-bleed scarlet fire (Mars in Aries). Dense dither — the Harris card
# is a WALL of flame red, no black emptiness anywhere.
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

# ---------------------------------------------------------------- dais
# Dark-red stone platform; fleur marks added at the end.
P(27, 0, "=" * W, "floor")
for r in range(28, H):
    for c in range(W):
        h = (r * 31 + c * 17) % 10
        if h < 9:
            P(r, c, ";;:,;;;:,;"[h], "floor")

# ---------------------------------------------------------------- sun
# Gold sun-glow disk behind the crowned head (Sol exalted in Aries).
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
P(0, 20, "|", "sunrays")
P(0, 26, "/", "sunrays")
# two long gold geometry-rays cutting down-left from the sun (Harris's
# thin ray lines); the throne post crosses over them
for r, c in ((5, 12), (6, 11), (7, 9), (8, 8), (9, 7), (10, 5),
             (11, 4), (12, 2)):
    P(r, c, "/", "sunrays")

# ---------------------------------------------------------------- light
# The diagonal white shaft from the UPPER RIGHT. Drawn BEFORE the ram +
# post so the architecture occludes it (light passes behind the throne,
# re-emerging beneath to strike the raised sceptre).
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

# ---------------------------------------------------------------- throne
# The architecture of rule. Stone posts both sides (dark red silhouette
# against the bright field), lattice throne-back, arm rails with the
# 16-point star-disk medallions at their outer ends.
for r in range(5, 12):
    P(r, 5, "[::]", "floor")
for r in range(6, 12):
    P(r, 38, "[::]", "floor")                  # right post starts lower —
                                               # the finial + light own row 5

# ram capitals atop the posts: double-spiral horns outward, muzzles
# resting down-inward. Left ram; right ram set a shade lower + inward so
# the light shaft bursts over it from the corner.
PB(1, 1, "  _,,--,_  ", "ram")
PB(2, 0, " ((@))';;;,_ ", "ram")
PB(3, 0, " ((@));;;;;;) ", "ram")
PB(4, 1, "  `´(;;o;;;) ", "ram")
PB(5, 3, "   `;;,;;´ ", "ram")
PB(1, 36, " _,,--,_  ", "ram")
PB(2, 34, " ,;;;';((@)) ", "ram")
PB(3, 34, " (;;;;;;((@)) ", "ram")
PB(4, 35, " `;;o;;;)`´ ", "ram")

# lattice throne-back in the slots beside the figure (skip the light)
for r in range(6, 25):
    for c in list(range(9, 18)) + list(range(29, 38)):
        if (r + 2 * c) % 5 == 0 and classes[r][c] not in ("light", "floor"):
            P(r, c, "x", "floor")

# arm rails + 16-point star-disk medallions (gold), outer mid-card
PMB(12, 0, " ,`\\¡/´, ", "star")
PMB(13, 0, "=((:*:))=", "star")
PMB(14, 0, " `,/¡\\,´ ", "star")

# ---------------------------------------------------------------- blades
# Angular fire tongues (the scan's red grass-flames), clear of the props.
def spike(r, c):
    P(r, c, "^", "flames")
    P(r + 1, c - 1, "/;\\", "flames")
    P(r + 2, c - 1, ";;;", "flames")


for r, c in ((7, 2), (8, 44), (16, 3), (17, 43), (19, 14), (21, 17),
             (20, 29), (18, 33), (24, 14), (22, 28), (16, 32)):
    spike(r, c)

# ---------------------------------------------------------------- figure
# Crown: four points + gold band, dead on the axis.
pc(1, "¡ ¡ ¡ ¡", "crown")
pc(2, "[=====]", "crown")
# face: frontal, bearded, the gaze turned to his left (toward the
# Empress) — pupil set left
pc(3, " (,o·;,) ", "face")
pc(4, " (;,‾,;) ", "face")
pc(5, " `(v;v)´ ", "face")
pc(6, " <=====> ", "crown")                    # gold collar

# robe: the Sulphur TRIANGLE — apex at the head, hem at row 15. Deep red
# mass, halo-punched out of the field, dense gold pattern-work on top.
for r in range(7, 16):
    hw = 3 + (r - 7)
    c0, c1 = 23 - hw, 23 + hw
    row = "(" + "".join(
        ";" if (r * 7 + c * 11) % 23 % 3 else ":"
        for c in range(c0 + 1, c1)) + ")"
    PB(r, c0 - 1, " " + row + " ", "robe")
# looping lines ending in arrowheads, bees, fleurs-de-lys (pattern-work)
P(8, 22, "&", "pattern")
P(9, 19, "6e", "pattern"); P(9, 26, "s", "pattern")
P(10, 18, "ce", "pattern"); P(10, 27, "e6", "pattern")
P(11, 20, "&", "pattern"); P(11, 28, "c", "pattern")
P(12, 16, "6", "pattern"); P(12, 27, "s", "pattern"); P(12, 30, "&", "pattern")
P(13, 17, "e>", "pattern"); P(13, 27, "<e", "pattern")
P(14, 14, "s", "pattern"); P(14, 21, "&", "pattern"); P(14, 29, "6", "pattern")
P(15, 17, "ce", "pattern"); P(15, 25, "e>", "pattern")
P(11, 17, "¡", "fleur"); P(13, 31, "¡", "fleur"); P(15, 13, "¡", "fleur")

# right arm raised out of the triangle; the ram-headed sceptre lifts
# INTO the light shaft where it emerges beneath the right ram
PB(7, 26, " (;;;) ", "robe")                   # rising sleeve
PB(7, 30, " (=) ", "skin")                     # the gripping hand
P(6, 34, "/", "sceptre")
PB(5, 34, " ,(@) ", "sceptre")                 # ram's-head finial, in the light
P(8, 30, "/", "sceptre")                       # shaft continuing down
P(9, 29, "/", "sceptre")
P(0, 38, "·", "light")                         # corner sparkle over the ram
P(0, 40, "·", "light")

# the Maltese-cross orb at the navel (government established)
PB(10, 22, " + ", "cross")
PB(11, 21, " (o) ", "orb")
PB(12, 20, " (==) ", "skin")                   # the cupped left hand

# ---------------------------------------------------------------- legs
# The CROSS beneath the triangle. Vertical shin first (crossed UNDER),
# then the horizontal thigh drawn over it, then the planted foot.
for r in range(17, 25):
    pc(r, " (;;;) ", "skin")
PB(16, 11, " ,;;;;;;;;;;;;;;;;;;, ", "skin")
PB(17, 10, " (;;;;;;;;;;;;;;;;;;;;=, ", "skin")
PB(18, 11, " `';;,__,;;;;,__,;;(,,> ", "skin")
pc(25, " (;;;) ", "skin")
PB(26, 19, " (,,;;;) ", "skin")

# ---------------------------------------------------------------- shield
# Pale-gold heater shield, crimson disk above the double-headed eagle.
PB(19, 1, ",=========,", "shield")
PB(20, 1, "|'       '|", "shield")
P(20, 5, "(o)", "orb")                         # the crimson disk (red tincture)
PB(21, 1, "|,/\\ ¡ /\\,|", "eagle")
PB(22, 1, "|( >(¡)< )|", "eagle")
PB(23, 1, "| (;;¡;;) |", "eagle")
PB(24, 1, " \\,\\;|;/,/ ", "eagle")
PB(25, 2, " \\;;;;;/ ", "shield")
PB(26, 3, "  `-,-´  ", "shield")

# ---------------------------------------------------------------- lamb
# The Lamb and Flag couchant at his feet — the tamed ram, haloed, the
# banner staff leaning across it.
PB(22, 33, " ,--, ", "crown")                  # gold halo
PB(23, 32, " (´o),;;;,_ ", "lamb")
PB(24, 31, " (;;(;;;;;;;) ", "lamb")
PB(25, 32, " ´´ `´´ `´ ", "lamb")
for r, c in ((25, 35), (24, 36), (23, 37), (22, 38), (21, 39)):
    P(r, c, "/", "sceptre")                    # the banner staff
P(20, 40, "=>", "crown")                       # the pennant

# ---------------------------------------------------------------- fleurs
PB(29, 5, " \\¡/ ", "fleur")
PB(30, 6, " ¡ ", "fleur")
PB(29, 38, " \\¡/ ", "fleur")
PB(30, 39, " ¡ ", "fleur")

# ---------------------------------------------------------------- sig
PB(31, 1, " aw ", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "04-emperor-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "04-emperor-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
