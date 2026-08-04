#!/usr/bin/env python3
"""Atu VIII Adjustment — panel candidate v3b (strategy: FIGURE DOMINANT).

The masked dancing Harlequin poised on the point of her own sword is the
hero read: slender, on tiptoe on the blade tip, both hands on the hilt,
blue mask, diaphanous blue wing-fans alive at the shoulders, green-gold
sheath robe. Scales and the concealed vesica are her attributes. The
card's law is PERFECT SYMMETRY, left/right AND top/bottom: everything
mirrored about AXIS=23 with PM/PMB; crown above <-> dome below, top
sphere pairs <-> bottom sphere pairs, up-spikes <-> down-spikes, pans
straddling the vertical middle.

Emits:
  drafts/08-adjustment-v3b-art-lg.txt       47x32 art, full-bleed
  drafts/08-adjustment-v3b-lg-classes.json  per-cell color classes
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


def PMB(r, c, s, cls):
    PB(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    PB(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def ray(r0, c0, r1, c1, cls, ch=None):
    """Mirrored straight ray with slope-appropriate glyphs, overwriting."""
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = int(round(r0 + (r1 - r0) * i / steps))
        c = int(round(c0 + (c1 - c0) * i / steps))
        if ch:
            g = ch
        elif r1 == r0:
            g = "~"
        else:
            s = (c1 - c0) / (r1 - r0)
            g = "|" if abs(s) < 0.35 else ("~" if abs(s) > 2.4 else
                                           ("\\" if s > 0 else "/"))
        PM(r, c, g, cls)


# ---------------------------------------------------------------- 0 ground
# pale chartreuse ground: a dense full-bleed wash (mirror-symmetric),
# heavy glyphs so the cells carry the colour — no black emptiness
for r in range(H):
    for c in range(W):
        a = abs(c - 23)
        h = (r * 31 + a * 17 + (r * a) % 7) % 100
        if h < 90:
            P(r, c, ";:·'"[h % 4], "ground")

# ---------------------------------------------------------------- 1 lattice
# fine blue harlequin net over the chartreuse ground, symmetric about the
# axis: tall diamonds ~6 cols wide x 6 rows (2:1 tall in render, as scanned)
for r in range(H):
    for c in range(W):
        dp = (r + (c - 23)) % 6 == 0
        dm = (r - (c - 23)) % 6 == 0
        if dp and dm:
            P(r, c, "x", "lattice")
        elif dp:
            P(r, c, "/", "lattice")
        elif dm:
            P(r, c, "\\", "lattice")

# ---------------------------------------------------------------- 2 curtain
# pale feathered curtain at the extreme edges, faint and symmetric
for r in range(4, 28, 4):
    PM(r, 0, "(", "rays")
for r in range(5, 27, 3):
    PM(r, 1, "'", "rays")

# ---------------------------------------------------------------- 3 harle
# green harlequin diamonds: dense band up top around the crown, echo band
# at the bottom, sparse accents down the side lattice
for r, c in [(0, 14), (0, 17), (1, 15), (1, 18), (2, 17), (0, 11), (2, 13)]:
    PM(r, c, "<>", "harle")
for r, c in [(30, 8), (31, 11), (30, 12)]:
    PM(r, c, "<>", "harle")
for r, c in [(16, 2), (19, 4), (22, 2), (25, 4)]:
    PM(r, c, "<>", "harle")

# ---------------------------------------------------------------- 4 spheres
# the poles she adjudicates: blue and green, mirrored L/R AND top/bottom.
# big blue quarter-spheres tucked into all four corners
for r, row in enumerate([";;;::·", ";;::·", ";::", ";·"]):
    PM(r, 0, row, "sphb")
for r, row in enumerate([";·", ";::", ";;::·", ";;;::·"]):
    PM(28 + r, 0, row, "sphb")
# blue pair (outer) + dark green pair (inner), top
PM(1, 7, ",'':;", "sphb")
PM(2, 7, ";:;:·", "sphb")
PM(2, 12, ",'::;", "sphg")
PM(3, 12, ";;:;·", "sphg")
# and mirrored below
PM(28, 12, ",'::;", "sphg")
PM(29, 12, ";;:;·", "sphg")
PM(29, 7, ",'':;", "sphb")
PM(30, 7, ";:;:·", "sphb")

# ---------------------------------------------------------------- 5 wings
# diaphanous blue wing-fans from her shoulders, alive — the dancer's
# poise. A bounded fan region radiating from the shoulder, stippled so it
# stays gauzy, glyphs following the radial direction.
ORR, ORC = 6.5, 20.5
for r in range(5, 14):
    for c in range(3, 20):
        dx = ORC - c
        dy = 2.0 * (r - ORR)
        if dx <= 0.5:
            continue
        d = math.hypot(dx, dy)
        if not (3.0 <= d <= 16.5):
            continue
        ang = math.atan2(dy, dx)
        if not (-0.18 <= ang <= 1.30):
            continue
        if (r * 13 + c * 7 + (r * c) % 5) % 12 >= 11:
            continue
        a = abs((r - ORR) / (c - ORC))
        g = "~" if a < 0.35 else ("/" if a < 1.2 else "(")
        PM(r, c, g, "wings")

# ---------------------------------------------------------------- 6 spikes
# the throne: dark green spike-pyramids, points up above, points down
# below the pans — Law and Limitation, four of them, mirrored, solid
PM(3, 13, "¡", "spike")
PM(4, 12, ";;;", "spike")
PM(5, 12, ";;;", "spike")
PM(6, 11, ";;;;;", "spike")
PM(7, 11, ";;;;;", "spike")
PM(8, 10, ";;;;;;;", "spike")
PM(9, 10, ";;;;;;;", "spike")
for i, (c0, w) in enumerate([(4, 9), (5, 8), (6, 7), (7, 6), (8, 6),
                             (9, 5), (10, 4), (11, 3), (12, 2)]):
    PM(17 + i, c0, ";" * w, "spike")
PM(26, 12, "v", "spike")

# ---------------------------------------------------------------- 7 vesica
# the concealed diamond, lower arms: pan-bottoms -> toe-point, a pale
# line crossing the dark spikes (upper arms are the chains themselves,
# crown-tip -> pans)
ray(16, 6, 27, 22, "rays", "\\")

# ---------------------------------------------------------------- 8 chains
# the great chains, crown of Maat down-out to the two pans
for r0, c0, r1, c1 in [(2, 19, 13, 3), (3, 20, 13, 10)]:
    steps = r1 - r0
    for i in range(steps + 1):
        r = r0 + i
        c = int(round(c0 + (c1 - c0) * i / steps))
        PM(r, c, "s", "chains")

# ---------------------------------------------------------------- 9 pans
# dark pans in perfect equilibrium, pale glass bubbles riding them:
# alpha LEFT, omega RIGHT
PMB(11, 4, "  ,~-~,  ", "bubble")
PMB(12, 3, " (:'·':) ", "bubble")
PMB(13, 3, " (:···:) ", "bubble")
PMB(14, 1, " ,=========, ", "pan")
PMB(15, 2, " \\:::::::/ ", "pan")
PMB(16, 3, "  `===='  ", "pan")
P(12, 7, "x", "mask")          # alpha
P(12, 39, "w", "mask")         # omega

# ---------------------------------------------------------------- 10 dome
# the dark dome at bottom center the blade-point touches — the crown's
# mirror below, completing the top/bottom balance
PB(28, 20, "  ,:·:,  ", "crown")
PB(29, 17, " (::;;;::) ", "crown")
PB(30, 15, " (:::;;;;;:::) ", "crown")
PB(31, 13, " (::::;;;;;;;::::) ", "crown")

# ---------------------------------------------------------------- 11 robe
# the green-gold sheath, a dancer's line: shoulders -> hips -> tiptoe
PB(7, 19, " (:;·;:) ", "robe")
PB(8, 18, " (;;:·:;;) ", "robe")
PB(9, 18, " (;;;·;;;) ", "robe")
PB(10, 17, " (;;;;·;;;;) ", "robe")
PB(11, 17, " (;;;:·:;;;) ", "robe")
PB(12, 16, " (;;;:;·;:;;;) ", "robe")
PB(13, 16, " (;;::;·;::;;) ", "robe")
PB(14, 16, " (;:;:;·;:;:;) ", "robe")
PB(15, 17, " (;;:;·;:;;) ", "robe")
PB(16, 17, " (;:;:·:;:;) ", "robe")
PB(17, 17, " (;;:;·;:;;) ", "robe")
PB(18, 18, " (;;:·:;;) ", "robe")
PB(19, 18, " (;:;·;:;) ", "robe")
PB(20, 18, " (;;:·:;;) ", "robe")
PB(21, 19, " (;:·:;) ", "robe")
PB(22, 19, " (:;·;:) ", "robe")
PB(23, 19, " (;:·:;) ", "robe")
PB(24, 20, " (:·:) ", "robe")
PB(25, 20, " (;·;) ", "robe")
# pale vertical highlight streaks down the robe
for r in (12, 14, 16, 18, 20):
    PM(r, 20, "'", "figure")

# ---------------------------------------------------------------- 12 head
# crown of Maat, orb hanging beneath, the blue Harlequin mask, bare chin
PB(0, 19, " ,==¡==, ", "crown")
PB(1, 19, " (:::::) ", "crown")
PB(2, 20, " (:::) ", "crown")
PB(3, 20, " `,o,´ ", "crown")
P(3, 23, "o", "sword")
PB(4, 20, " ,===, ", "mask")
PB(5, 20, " (=·=) ", "mask")
PB(6, 21, " )·( ", "skin")

# ---------------------------------------------------------------- 13 sword
# pommel ball at the breast, both hands wrapped below it, crescent guard,
# the blade a clean vertical on col 23 down to the point she stands on
P(8, 22, "(o)", "sword")
P(9, 21, "(mmm)", "skin")
P(10, 18, "c==,_", "sword")
P(10, 23, "¡", "sword")
P(10, 24, "_,==C", "sword")
# feet on tiptoe hugging the blade, poised on the very point
PB(26, 20, "  ) (  ", "skin")
PB(27, 21, "  ¡  ", "sword")
for r in range(11, 27):
    P(r, 23, "|", "sword")

# ---------------------------------------------------------------- 14 sig
P(31, 5, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "08-adjustment-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "08-adjustment-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
