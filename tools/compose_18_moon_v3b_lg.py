#!/usr/bin/env python3
"""Moon v3b — ultracode panel candidate B: PATH-RECESSION dominant.

The hero read is the receding blood-tinged road. The scene is an hourglass
pinched at the horizon gap (r11) between the two mountains: the pale cone of
tainted light widens UP from the gap to the dark waning moon (the Harris V,
holding the nine s-yods as they funnel toward the vanishing point), and the
perspective ROAD widens DOWN from the gap toward the viewer — converging
/-\\ edges, foreshortened cross-dashes whose spacing stretches as they near,
and a blood stream that narrows to a single cell at the gap. Twin towers,
Anubis guardians and jackals are strict PMB mirrors about AXIS=23.0; at the
bottom the scarab bears the gold sun inside the aura ring — the one warm
point in an indigo midnight.

Emits:
  drafts/18-moon-v3b-art-lg.txt       47x32 art, full-bleed
  drafts/18-moon-v3b-lg-classes.json  per-cell color classes (art coords)
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
    """Place including spaces (spaces punch a 1-cell breathing halo)."""
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


def hsh(r, c):
    return (r * 37 + c * 59 + (r * c) % 13) % 100


def SYM(r, dx, ch, cls):
    """Mirror-pair texture cell at 23-dx / 23+dx (dx=0 hits the axis once)."""
    P(r, 23 - dx, ch, cls)
    P(r, 23 + dx, ch.translate(MIRROR), cls)


def CLR(r, c):
    canvas[r][c] = " "
    classes[r][c] = None


# ------------------------------------------------------------- geometry
PINCH = 11.0                 # horizon gap row: the hourglass waist


def hw_cone(r):              # rows 7..11: pale V half-width, widening upward
    return 1.5 + 1.2 * (PINCH - r)


def hw_road(r):              # rows 12..19: road half-width, widening downward
    return 1.5 + 1.15 * (r - PINCH)


def skyline(cl):             # left-half mountain top row (cl in 0..21)
    if cl <= 1:
        return 10.0
    if cl <= 3:
        return 9.0
    if cl <= 10:
        return 6.5           # plateau the towers stand on
    if cl <= 14:
        return 7.0
    return max(7.0, PINCH - (21.5 - cl) / 1.2)   # inner slope = cone wall


# ------------------------------------------------------------- 1. sky
# midnight, starless but textured: sparse indigo grain, mirrored
for r in range(0, 20):
    for dx in range(0, 24):
        h = hsh(r, dx)
        if h < 13:
            SYM(r, dx, "·,·'"[h % 4], "tower")

# ------------------------------------------------------------- 2. mountains
for r in range(6, 20):
    for cl in range(0, 22):
        dx = 23 - cl
        if 7 <= r <= PINCH and dx < hw_cone(r):
            continue                     # inside the pale cone
        if r > PINCH and dx < hw_road(r):
            continue                     # inside the road
        sk = skyline(cl)
        if r < sk:
            continue                     # sky above the ridge
        h = hsh(r, cl)
        depth = r - sk
        if depth < 1.0:                  # jagged barren ridge cap
            if h < 88:
                SYM(r, dx, "^^\\;"[h % 4], "tower")
        elif r >= 17:                    # ground band under the guardians
            if h < 82:
                SYM(r, dx, ";%:;"[h % 4], "tower")
        else:
            if h < 76:
                SYM(r, dx, ";;%::;"[h % 6], "tower")

# ------------------------------------------------------------- 3. pale cone
for r in range(7, int(PINCH) + 1):
    hw = hw_cone(r)
    for dx in range(0, int(hw) + 1):
        CLR(r, 23 - dx)
        CLR(r, 23 + dx)
        h = hsh(r, dx)
        if h < 36:
            SYM(r, dx, "·'"[h % 2], "cone")
# cone walls (the converging lines, upper half of the hourglass)
for r in range(7, int(PINCH) + 1):
    wl = int(round(23.0 - hw_cone(r)))
    P(r, wl, "\\", "cone")
    P(r, 46 - wl, "/", "cone")
# horizon notch at the vanishing point
P(int(PINCH), 22, "\u203e", "cone")
P(int(PINCH), 24, "\u203e", "cone")

# ------------------------------------------------------------- 4. the road
for r in range(int(PINCH) + 1, 20):
    hw = hw_road(r)
    for dx in range(0, int(hw) + 1):
        CLR(r, 23 - dx)
        CLR(r, 23 + dx)
        h = hsh(r, dx)
        if h < 36:
            SYM(r, dx, "·'"[h % 2], "cone")
# converging road edges (lower half of the hourglass)
for r in range(int(PINCH) + 1, 20):
    el = int(round(23.0 - hw_road(r)))
    P(r, el, "/", "cone")
    P(r, 46 - el, "\\", "cone")
# foreshortened cross-dashes: spacing stretches as the road nears
for r, ch, step in ((13, "-", 2), (15, "-", 2), (18, "_", 1)):
    hw = hw_road(r)
    for dx in range(2, int(hw), step):
        SYM(r, dx, ch, "cone")
# blood stream, narrowing to one cell at the gap
for r in range(int(PINCH), 20):
    shw = 0.5 + 0.4 * (r - PINCH)
    for dx in range(0, int(shw) + 1):
        h = hsh(r * 7, dx + 3)
        if h < 84:
            SYM(r, dx, ";:%;"[h % 4], "blood")

# ------------------------------------------------------------- 5. nine yods
YODS = [(7, 18), (7, 23), (7, 28),
        (8, 19), (8, 23), (8, 27),
        (9, 20), (9, 26),
        (10, 23)]
assert len(YODS) == 9, "Crowley is specific: nine"
for r, c in YODS:
    P(r, c, "s", "blood")

# ------------------------------------------------------------- 6. the moon
# dark waning orb nested in the mouth of the V; pale gold rim, dim heart
MCY, MRY, MRX = 3.0, 3.4, 8.2
for r in range(0, 7):
    for dx in range(0, 9):
        d = (dx / MRX) ** 2 + ((r - MCY) / MRY) ** 2
        if d > 1.0:
            continue
        CLR(r, 23 - dx)
        CLR(r, 23 + dx)
        h = hsh(r, dx)
        if d > 0.55 and r <= MCY:         # solid gold crescent above
            cov, ramp = 97, "%o%;"
        elif d > 0.55:                    # dimmer lower limb
            cov, ramp = 74, ";::;"
        elif d > 0.24:                    # mid tone
            cov, ramp = 68, ":·:'"
        else:                             # dim swirled heart
            cov, ramp = 48, "·':·"
        if h < cov:
            SYM(r, dx, ramp[h % 4], "moon")
# the red thread swirling through the disc
P(2, 20, ",~\u00b4", "blood")
P(3, 24, "`~,", "blood")
# the great blue arcs sweeping from the moon out over the towers
for ar, ac in ((1, 15), (2, 13), (3, 11), (3, 2), (4, 1), (5, 0)):
    PM(ar, ac, "/", "waveblue")

# ------------------------------------------------------------- 7. towers
PMB(1, 6, " \u00a1 ", "tower")
PMB(2, 5, " /;\\ ", "tower")
PMB(3, 4, " /;%;\\ ", "tower")
PMB(4, 3, " ,{;%;}, ", "tower")
PMB(5, 4, " |;\u00a1;| ", "tower")
PMB(6, 4, " |%;%| ", "tower")
PMB(7, 4, " (;%;) ", "tower")
PMB(8, 3, " ,{;%;}, ", "tower")

# ------------------------------------------------------------- 8. Anubis
PMB(9, 7, " ,\u00a1, ", "anubis")                 # ears
PMB(10, 4, " <\u00b4;o}, ", "anubis")             # jackal head, snout outward
PMB(11, 6, " ,{%%%}, ", "anubis")                 # shoulders
PMB(12, 6, " |%%%|=, ", "anubis")                 # chest, arm to the staff
PMB(13, 6, " |%%%| ", "anubis")                   # torso
PMB(14, 6, " {%%%} ", "anubis")                   # kilt
PMB(15, 6, " /;\u00a1;\\ ", "anubis")             # legs
PMB(16, 6, " |\u00b4 `| ", "anubis")              # shins / feet
PM(9, 13, "\u00a1", "anubis")                     # staff head
for r in range(10, 17):
    PM(r, 13, "|", "anubis")                      # staffs flanking the road

# ------------------------------------------------------------- 9. jackals
PMB(17, 4, " ,_, ", "jackal")                     # arched back
PMB(18, 3, " (;;\u00b4> ", "jackal")              # watching the path
PMB(19, 4, " \u00b4\u00b4\u00b4\u00b4 ", "jackal") # legs on the mound

# ------------------------------------------------------------- 10. flame
P(15, 23, "\u00a1", "flame")
PB(16, 21, " /\u00a1\\ ", "flame")
PB(17, 20, " /;\u00a1;\\ ", "flame")
PB(18, 19, " (;%\u00a1%;) ", "flame")
PB(19, 19, " {;%%%;} ", "flame")

# ------------------------------------------------------------- 11. the pool
# ripple streaks, mirrored
for r in range(20, 32):
    for dx in range(0, 24):
        h = hsh(r * 3, dx // 4)
        cov = 56 if r == 20 else 44
        if h < cov:
            ch = "\u203e" if r == 20 and h % 5 == 0 else ("-" if h % 3 else "~")
            SYM(r, dx, ch, "water")
# aura: the gold glow ring around scarab + sun
ACY, ARY, ARX = 25.8, 5.4, 10.8
for r in range(20, 32):
    for dx in range(0, 12):
        d = (dx / ARX) ** 2 + ((r - ACY) / ARY) ** 2
        h = hsh(r, dx + 50)
        if 0.60 <= d <= 1.04:
            if h < 80:
                SYM(r, dx, "'\u00b7:*"[h % 4], "aura")
        elif d < 0.60 and h < 30:
            SYM(r, dx, "\u00b7'"[h % 2], "aura")
# bell-waves: red outer + blue inner, dithered masses on both sides
PMB(22, 3, " ,;, ", "wavered")
PMB(23, 2, " /;:;\\ ", "wavered")
PMB(24, 1, " /;:;:;\\ ", "wavered")
PMB(25, 0, "/;:;:;:;\\ ", "wavered")
PMB(26, 0, "(;:;:;:;) ", "wavered")
PMB(23, 8, " ,;, ", "waveblue")
PMB(24, 7, " /;:;\\ ", "waveblue")
PMB(25, 6, " /;:;:;\\ ", "waveblue")
PMB(26, 5, " /;:;:;:;\\ ", "waveblue")
PMB(27, 5, " (;:;:;:;) ", "waveblue")
PMB(28, 5, " \u00b4;:;:;:;` ", "waveblue")
# cascading tails to the bottom corners
PMB(29, 1, " ,;, ", "wavered")
PMB(30, 0, "/;:;\\ ", "wavered")
PMB(31, 0, "(;:;) ", "wavered")

# ------------------------------------------------------------- 12. sun+scarab
PB(21, 19, " ,;%%%;, ", "sun")
PB(22, 18, " (%%%%%%%) ", "sun")
PB(23, 19, " `;%%%;\u00b4 ", "sun")
PM(22, 17, "(", "scarab")                         # mandibles hug the disk
PM(23, 18, "\\", "scarab")
PB(24, 19, " \\,(\u00b7),/ ", "scarab")           # head between mandibles
PB(25, 19, " <{%%%}> ", "scarab")                 # thorax + mid legs
PB(26, 19, " <{%%%}> ", "scarab")                 # wing case + legs
PB(27, 20, " `{%}\u00b4 ", "scarab")              # abdomen

# ------------------------------------------------------------- 13. signature
PB(31, 1, " aw ", "sig")

# ------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
n_yods = sum(1 for r in range(H) for c in range(W)
             if canvas[r][c] == "s" and classes[r][c] == "blood")
assert n_yods == 9, f"yod count {n_yods} != 9"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "18-moon-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "18-moon-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
