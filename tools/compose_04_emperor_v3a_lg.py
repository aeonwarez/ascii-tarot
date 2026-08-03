#!/usr/bin/env python3
"""Emperor v3a — SULPHUR-GLYPH SILHOUETTE DOMINANT (panel candidate A).

The geometric Sulphur-glyph body is the hero, unmistakable at a glance:
head + arms an upright TRIANGLE (dense scarlet brocade mass with bright
orange /-\\ edges widening from the crowned head to the lap, closed by an
overline base), crossed bare legs the CROSS below (pale-skin vertical shin
down the axis crossed by the folded leg's horizontal bar with a pointed
foot) — the alchemical glyph of Sulphur made flesh, frontal, crowned,
gaze tilted to his left toward the Empress. Figure/ground separation by
VALUE: the field is a dense scarlet dither, the cross is pale skin, the
regalia gold, every sprite halo-punched. Support: angular fire spikes,
the diagonal white light shaft from the UPPER RIGHT (Harris's traditional
placement — noted against Crowley's Tzaddi swap) catching the raised
ram-sceptre, ram-head throne capitals, 16-point star disks on the throne
arms, gold sun disk behind the head, red-eagle shield with crimson disk
low left, Lamb and Flag couchant low right, dark pavement + fleurs.

Emits drafts/04-emperor-v3a-art-lg.txt + drafts/04-emperor-v3a-lg-classes.json
"""
import json, os

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


# ------------------------------------------------- 1. scarlet flame field
# DENSE full bleed — the card burns; no black emptiness.
FIELD_RAMP = ";;:;;·;:;;';;:;"
for r in range(28):
    for c in range(W):
        h = (r * 37 + c * 61 + (r * c) % 17) % 100
        if h < 96:
            cls = "flames" if (r * 13 + c * 29) % 19 < 5 else "field"
            P(r, c, FIELD_RAMP[h % len(FIELD_RAMP)], cls)

# ------------------------------------------------- 2. dark red pavement
for r in range(28, H):
    for c in range(W):
        h = (r * 53 + c * 31 + (r + c) % 11) % 100
        if h < 94:
            P(r, c, ";:,;.:"[h % 6], "floor")
P(28, 0, "_" * W, "floor")


# ------------------------------------------------- 3. angular fire spikes
def spike(tip_r, base_r, cx):
    for r in range(tip_r, base_r + 1):
        t = (r - tip_r) / max(1, base_r - tip_r)
        hw = int(round(t * 2))
        if hw == 0:
            P(r, cx, "^", "flames")
        else:
            P(r, cx - hw, "/" + ";" * (2 * hw - 1) + "\\", "flames")


for tip, base, cx in [
    (4, 10, 4), (6, 12, 8), (9, 15, 2),
    (5, 11, 42), (8, 14, 44),
    (16, 20, 11), (16, 20, 35),
    (21, 26, 15), (21, 26, 31),
    (17, 21, 38), (15, 19, 6), (15, 19, 40),
]:
    spike(tip, base, cx)

# ------------------------------------------------- 4. gold sun + crown rays
# Sol exalted in Aries: gold disk behind the head, set a little left.
for r in range(0, 7):
    for c in range(11, 30):
        v = ((c - 20.0) / 8.5) ** 2 + ((r - 3.2) / 3.1) ** 2
        if v <= 1.0:
            P(r, c, '"' if v < 0.4 else ("'" if v < 0.75 else "·"),
              "sunrays")
P(0, 14, "\\/\\/\\/", "sunrays")
P(0, 27, "\\/\\/\\/", "sunrays")

# ------------------------------------------------- 5. ram throne capitals
PMB(0, 2, " _,,--,_ ", "ram")
PMB(1, 1, " ((@)) `, ", "ram")
PMB(2, 1, " `((´,;;;) ", "ram")
PMB(3, 2, "  `´ `--´ ", "ram")

# ------------------------------------------------- 6. white light shaft
# Diagonal beam descending from the UPPER RIGHT, landing on the hand that
# raises the ram-sceptre into it.
for r in range(0, 10):
    cs = 45.5 - 2.1 * r
    for dc in range(-3, 4):
        c = int(round(cs)) + dc
        if 0 <= c < W and classes[r][c] != "ram":
            P(r, c, "\\" if abs(dc) <= 1 else ("'" if abs(dc) == 2 else "·"),
              "light")
# Harris paints PARALLEL bands: a second, narrower streak that the raised
# sceptre head will punch through (the crozier lifted into the light).
for r in range(0, 7):
    cs = 38.0 - 2.1 * r
    for dc in range(-1, 2):
        c = int(round(cs)) + dc
        if 0 <= c < W and classes[r][c] != "ram":
            P(r, c, "\\" if dc == 0 else "'", "light")

# ------------------------------------------------- 8. eagle shield (low L)
PB(20, 2, " ,=======, ", "shield")
PB(21, 2, " |:(@@):,| ", "shield")
P(21, 5, "(@@)", "orb")                   # the crimson disk (red tincture)
PB(22, 2, " |<¡\\/¡>| ", "shield")
P(22, 4, "<¡\\/¡>", "eagle")              # double-headed eagle displayed
PB(23, 2, " |;/||\\;| ", "shield")
P(23, 4, ";/||\\;", "eagle")
PB(24, 3, " \\;;¡;;/ ", "shield")
P(24, 7, "¡", "eagle")
PB(25, 4, " \\;;;/ ", "shield")
PB(26, 5, " \\;/ ", "shield")
PB(27, 6, " v ", "shield")

# ------------------------------------------------- 9. Lamb & Flag (low R)
for r, c in [(23, 39), (22, 40), (21, 41), (20, 42), (19, 43)]:
    P(r, c, "/", "lamb")                  # banner staff
PB(17, 43, " ,=, ", "lamb")
PB(18, 43, " |=> ", "lamb")               # pennant
PB(23, 33, " ,‾,;;;;;;, ", "lamb")
PB(24, 32, " (´o(;;;;;;;) ", "lamb")
PB(25, 32, " (;;(;;;;;;;) ", "lamb")
PB(26, 33, " ‾´´‾‾´´‾ ", "lamb")

# ------------------------------------------------- 10. THE FIGURE (on top)
# crown: four gold points + jewelled band, dead on col 23
PB(1, 18, "  \\¡/¡\\¡/  ", "crown")
PB(2, 18, "  [=·=·=]  ", "crown")
# face: frontal, gaze tilted to his left, bearded
PB(3, 19, "  (o·,)  ", "face")
PB(4, 19, "  (;;;)  ", "face")
PB(5, 20, "  );(  ", "face")

# the TRIANGLE: head+arms one widening brocade mass, bright /-\ edges
ROBE_TOP, ROBE_BOT = 6, 14
for r in range(ROBE_TOP, ROBE_BOT + 1):
    half = int(round(4 + (r - ROBE_TOP) * 10 / 8))
    lo, hi = 23 - half, 23 + half
    body = []
    for c in range(lo + 1, hi):
        h = (r * 41 + c * 67 + (r * c) % 13) % 100
        body.append(";%;;&;;;"[h % 8])
    PB(r, lo - 2, "  /" + "".join(body) + "\\  ", "robe")
    P(r, lo, "/", "pattern")
    P(r, hi, "\\", "pattern")
# the closed BASE of the triangle (the lap) — the glyph must read
PB(15, 7, "  " + "‾" * 29 + "  ", "pattern")
# robe brocade: bees *, fleur ¡, loops-with-arrowheads e> (directed energy)
for r, c, s in [(7, 21, "e>"), (8, 18, "*"), (8, 26, "*"), (9, 19, "e>"),
                (10, 17, "¡"), (10, 27, "e>"), (11, 15, "*"), (11, 28, "¡"),
                (12, 17, "e>"), (12, 27, "*"), (13, 13, "¡"), (13, 30, "e>"),
                (14, 16, "*"), (14, 28, "¡"), (13, 20, "*"), (14, 22, "e>")]:
    P(r, c, s, "pattern")
# left hand + orb-and-Maltese-cross at the navel (on the axis)
P(10, 22, "<+>", "cross")
PB(11, 19, "  (@@@)  ", "orb")
PB(12, 19, "  (;;;)  ", "skin")
# right hand + ram-headed sceptre raised into the light shaft
PB(1, 32, "  ,--,  ", "sceptre")
PB(2, 31, "  ((@)  ", "sceptre")
PB(3, 32, "  `¡´  ", "sceptre")
for r, c in [(4, 32), (5, 31), (6, 30), (7, 29), (8, 28)]:
    P(r, c, "/", "sceptre")
PB(9, 25, " (;) ", "skin")

# the CROSS: pale vertical shin down the axis...
for r in range(16, 26):
    PB(r, 19, "  (;" + "':"[r % 2] + ";)  ", "skin")
# ...crossed by the folded leg's horizontal bar, knee left, foot right
PB(18, 10, " ,;;, ", "skin")
PB(19, 10, "  ," + ";" * 21 + ",  ", "skin")
PB(20, 10, "  (" + ";" * 21 + ")  ", "skin")
PB(21, 31, "  `;=´  ", "skin")
# the bare foot on the pavement
PB(26, 17, "  ,(;;;;;),  ", "skin")
PB(27, 18, "  `‾‾‾‾‾´  ", "skin")

# ------------------------------------------------- star disks + throne
# Drawn after the figure so the triangle's halo cannot chew the disks.
PMB(11, 2, " ,--¡--, ", "star")
PMB(12, 1, " ((:*:)) ", "star")
PMB(13, 2, " `--¡--´ ", "star")
PMB(14, 3, " |::| ", "floor")
PMB(15, 3, " |::| ", "floor")
PMB(16, 3, " |::| ", "floor")

# ------------------------------------------------- 11. fleurs + signature
PB(29, 5, " ,¡, ", "fleur")
PB(29, 38, " ,¡, ", "fleur")
P(30, 22, ",¡,", "fleur")
P(31, 2, "aw", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "04-emperor-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "04-emperor-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
