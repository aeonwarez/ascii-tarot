#!/usr/bin/env python3
"""Moon FINAL — ultracode panel synthesis (judge tally v3b 8, v3c 6, v3a 4).

BASE (v3b): the perspective skeleton. The scene is an hourglass pinched at
the horizon gap (r11): the pale cone of tainted light widens UP to the dark
waning moon (pale, sickly — the deck's only genuinely pale one), the ROAD
widens DOWN toward the viewer with converging /-\\ edges and foreshortened
cross-dashes (sparse far, contiguous near); the blood stream narrows to a
single cell at the gate and widens to the pool. EXACTLY NINE red s-shaped
Yod drops in the 3+3+2+1 taper (asserted; stream marks are a distinct glyph
class so they never read as a tenth drop).

GRAFT 1 (v3c): the heavy TOWERS OF NAMELESS DREAD — [#######] / |%#%#%|
black dithered masses with the lit '!' window — on dense dithered summits,
replacing v3b's thin turret stacks; the flanks are solid mass, not outline.
GRAFT 2 (v3a): the shaped Anubis figures — snout `=>` toward the way, ankh
'o'/'+' at the outer hand, planted staves — with v3c's jackals at their feet.
GRAFT 3 (v3c): Khephra the checkered scarab bearing the gold *@@@* sun,
inside v3b's larger gold aura ring. The ONLY warmth in the card lives here.

Everything mirrors about AXIS = 23.0 via PM/PMB; dither is hashed on
|c - AXIS| so the texture itself cannot drift. Indigo/black dominant,
starless-but-textured sky, full-bleed.

Emits:
  drafts/18-moon-final-art-lg.txt       47x32 art, full-bleed
  drafts/18-moon-final-lg-classes.json  per-cell color classes (art coords)
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
        return 8.5
    if cl <= 3:
        return 7.5
    if cl <= 10:
        return 6.5           # plateau the towers stand on
    if cl <= 14:
        return 7.0
    return max(7.0, PINCH - (21.5 - cl) / 1.2)   # inner slope = cone wall


# ------------------------------------------------------------- 1. sky
# midnight, starless but textured: sparse indigo grain, mirrored; the top
# corners thicken into the dark masses behind the towers (never outline).
for r in range(0, 20):
    for dx in range(0, 24):
        h = hsh(r, dx)
        cov = 13
        if r <= 7 and dx >= 20:
            cov = 34                     # corner masses behind the towers
        elif r <= 7 and dx >= 17:
            cov = 26
        if h < cov:
            SYM(r, dx, "·,;'"[h % 4] if cov > 13 else "·,·'"[h % 4], "tower")

# ------------------------------------------------------------- 2. mountains
# denser than v3b: the barren flanks are solid dithered MASS (the graft-1
# fix), darkest toward the borders, jagged only at the ridge cap.
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
            if h < 92:
                SYM(r, dx, "^^\\;"[h % 4], "tower")
        elif r >= 17:                    # ground band under the guardians
            if h < 82:
                SYM(r, dx, ";%:;"[h % 4], "tower")
        else:
            cov = 86 if cl <= 3 else 84  # heavy dithered mass
            if h < cov:
                SYM(r, dx, ";;%;%:"[h % 6], "tower")

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
# blood stream, narrowing to one cell at the gap (glyphs ;:%; — never 's',
# so the stream can never read as a tenth drop)
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
# pale sickly waning orb nested in the mouth of the V; gold rim, dim heart
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
# GRAFT 1: the Towers of Nameless Dread — heavy black dithered masses with
# the lit '!' slit window, planted on the summit plateau. They must outweigh
# the guardians below.
PMB(0, 6, " ,^, ", "tower")
PMB(1, 5, " /###\\ ", "tower")
PMB(2, 4, " /##%##\\ ", "tower")
PMB(3, 3, " [#######] ", "tower")
PMB(4, 4, " |%#%#%| ", "tower")
PMB(5, 4, " |#% %#| ", "tower")
PM(5, 8, "!", "cone")                          # the ghost-lit slit window
PMB(6, 4, " |%#%#%| ", "tower")
PMB(7, 4, " |#%#%#| ", "tower")
PMB(8, 3, " (#%#%#%#) ", "tower")

# ------------------------------------------------------------- 8. Anubis
# GRAFT 2: the shaped guardians — snout toward the way, ankh at the outer
# hand, staff planted at the road's edge — heads clear of the tower base.
PMB(9, 8, " /\\ ", "anubis")                   # ears
PMB(10, 6, " (;;;=> ", "anubis")               # skull + snout toward the path
PMB(11, 7, " );;( ", "anubis")                 # neck / collar
PMB(12, 6, " (;;;;)-, ", "anubis")             # shoulders + arm to the staff
PMB(13, 7, " |;;;;| ", "anubis")
PMB(14, 7, " (;;;;) ", "anubis")
PMB(15, 6, " /;;;;;\\ ", "anubis")             # kilt flare
PMB(16, 7, " );;;;( ", "anubis")
PMB(17, 7, " |;;;;| ", "anubis")
PMB(18, 8, " );;(", "anubis")                  # shin (no tail halo: the road
PM(19, 8, ",/", "anubis")                      #  edge at col 13 stays whole)
PM(19, 11, ",/", "anubis")                     # striding feet
# outer arm + the hanging mercury/ankh sigil
PM(13, 6, "/", "anubis")
PM(14, 6, "|", "anubis")
PM(15, 6, "o", "cone")
PM(16, 6, "+", "cone")
# the staff (planted, drawn last so body halos never break it)
PM(9, 14, "\u00a1", "anubis")
for r in range(10, 20):
    PM(r, 14, "|", "anubis")

# ------------------------------------------------------------- 9. jackals
# GRAFT 2b: the jackals on watch at the guardians' feet (v3c's read).
PMB(17, 0, "  _,^,  ", "jackal")               # arched back + ears
PMB(18, 0, " (;;;=>  ", "jackal")              # watching the path
PMB(19, 0, "  \u00b4U`U\u00b4 ", "jackal")     # legs on the mound

# ------------------------------------------------------------- 10. flame
P(15, 23, "\u00a1", "flame")
PB(16, 21, " /\u00a1\\ ", "flame")
PB(17, 20, " /;\u00a1;\\ ", "flame")
PB(18, 19, " (;%\u00a1%;) ", "flame")
PB(19, 19, " {;%%%;} ", "flame")

# ------------------------------------------------------------- 11. the pool
# ripple streaks, mirrored; blood tinge spreading from the stream's mouth
for r in range(20, 32):
    for dx in range(0, 24):
        h = hsh(r * 3, dx // 4)
        cov = 56 if r == 20 else 44
        if h < cov:
            ch = "\u203e" if r == 20 and h % 5 == 0 else ("-" if h % 3 else "~")
            SYM(r, dx, ch, "water")
PM(20, 17, "~-", "blood")
PM(21, 15, "-~", "blood")
# aura: v3b's larger gold glow ring, re-centered on the scarab-sun
ACY, ARY, ARX = 26.6, 5.0, 10.8
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
# GRAFT 3: Khephra the checkered scarab bearing the gold *@@@* sun disk —
# the single warm point in the card, inside the aura ring.
def PC(r, s, cls):
    P(r, 23 - len(s) // 2, s, cls)


def PCB(r, s, cls):
    PB(r, 23 - len(s) // 2, s, cls)


PC(24, ",*@@@*,", "sun")
PC(25, "`*@@@*\u00b4", "sun")
P(25, 19, "\\", "scarab")                      # mandibles raised to the disk
P(25, 27, "/", "scarab")
PCB(26, "\\,(;),/", "scarab")                  # head between mandibles
PCB(27, "({;x;})", "scarab")                   # thorax, checkered
PCB(28, "({;x;x;})", "scarab")                 # wing case + legs
PCB(29, "({;x;})", "scarab")                   # abdomen
PCB(30, "\u00b4/,|,\\`", "scarab")             # hind legs + tail

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
with open(os.path.join(DRAFTS, "18-moon-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "18-moon-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
