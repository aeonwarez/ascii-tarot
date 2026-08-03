#!/usr/bin/env python3
"""Priestess v3c — ARCHITECTURE-SYMMETRIC strategy (ultracode panel, composer C).

The throne and the two pillars (Mercy/Severity) framed strongly at the flanks,
the veil of light STRETCHED BETWEEN THEM: sagging net lines anchored at the
pillars converge into the crescent Moon-cup; two ray-fans (crown + cup) cross
them into diamonds; teal sweep-wedges + deep-blue field dither fill every gap
so the veil IS the fill. Strict mirror discipline via PM/PMB about AXIS=23.
Figure = moon-phase crown, latticed torso, up-sweeping arm bands ending in
teal spiral curls, wide scrolled cup, and a latticed TENT-throne dissolving
to the base. Structured garden register below: crystals L, concave flower L,
pine cone, WHITE camel dead center on a pale mound, grapes, gold spiral
shell R, pyramid + dodecahedron far R.

Emits:
  drafts/02-priestess-v3c-art-lg.txt       47x32 art
  drafts/02-priestess-v3c-lg-classes.json  per-cell classes
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
    """Place including spaces: spaces punch a breathing halo."""
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


def CLR(r, c):
    if 0 <= r < H and 0 <= c < W:
        canvas[r][c] = " "
        classes[r][c] = None


def ray(r0, c0, r1, c1, cls):
    """Straight veil ray; crossings with opposite-slope rays become lattice x;
    near-horizontal stretches are dashed so they stay airy."""
    steps = max(abs(r1 - r0), abs(c1 - c0), 1)
    for i in range(int(steps) + 1):
        t = i / steps
        rr = int(round(r0 + (r1 - r0) * t))
        cc = int(round(c0 + (c1 - c0) * t))
        if not (0 <= rr < H and 0 <= cc < W):
            continue
        dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99.0
        if abs(dc) > 3.2:
            if cc % 2:
                continue
            g = "-"
        elif abs(dc) < 0.35:
            g = "|"
        else:
            g = "\\" if dc > 0 else "/"
        cur = canvas[rr][cc]
        if cur == " ":
            canvas[rr][cc] = g
            classes[rr][cc] = cls
        elif cur in "\\/|" and g in "\\/|" and cur != g:
            canvas[rr][cc] = "x"
            classes[rr][cc] = "lattice"


def sag(r_edge, depth, cls, c0=3, c1=43):
    """Net line anchored at the pillars, sagging toward the center (the veil
    stretched between them, pulled down into the cup). Flats are dashed."""
    span = AXIS - c0

    def rf(c):
        u = (c - AXIS) / span
        return r_edge + depth * (1 - u * u)

    for c in range(c0, c1 + 1):
        rr = int(round(rf(c)))
        if not (0 <= rr < H):
            continue
        slope = (rf(c + 1) - rf(c - 1)) / 2.0
        if slope > 0.28:
            g = "\\"
        elif slope < -0.28:
            g = "/"
        elif abs(slope) > 0.10:
            if c % 2:
                continue
            g = "-"
        else:
            g = "_"
        cur = canvas[rr][c]
        if cur == " ":
            canvas[rr][c] = g
            classes[rr][c] = cls
        elif cur in "\\/|" and g in "\\/" and cur != g:
            canvas[rr][c] = "x"
            classes[rr][c] = "lattice"


# ================================================================ 1. VEIL
# fan A: rays from the crown origin up/out to the top + upper sides
OA_R, OA_C = 6.0, 23.0
for tc in (3, 9, 15):
    ray(OA_R, OA_C, 0, tc, "veil")
    ray(OA_R, OA_C, 0, 46 - tc, "veil")
for tr in (1, 4, 8):
    ray(OA_R, OA_C, tr, 0, "veil")
    ray(OA_R, OA_C, tr, 46, "veil")
# fan B: rays from the cup origin down/out to the base + lower sides
OB_R, OB_C = 12.0, 23.0
for tc in (2, 8, 14, 19):
    ray(OB_R, OB_C, 31, tc, "veil")
    ray(OB_R, OB_C, 31, 46 - tc, "veil")
for tr in (15, 18, 21, 24, 27, 30):
    ray(OB_R, OB_C, tr, 0, "veil")
    ray(OB_R, OB_C, tr, 46, "veil")
# fan C: the webbing gathered from her chest down into the cup's scroll ends
for tr, tc in ((11.5, 6), (11.7, 12), (11.9, 17)):
    ray(6.5, 23, tr, tc, "veil")
    ray(6.5, 23, tr, 46 - tc, "veil")
# the stretched net: sag lines anchored at the pillars, dipping into the cup
sag(2, 8.5, "lattice")
sag(4, 7.0, "lattice")
sag(6, 5.5, "lattice")
sag(8, 4.0, "lattice")
sag(10, 2.5, "lattice")
sag(12, 1.5, "lattice")
sag(15, 2.5, "lattice")
sag(19, 2.0, "lattice")
# star-points caught in the net intersections (mirrored pairs)
for r, c in [(4, 12), (7, 7), (10, 15), (15, 6), (19, 10), (24, 16)]:
    P(r, c, "*", "veil")
    P(r, 46 - c, "*", "veil")

# ============================================================ 2. TEAL SWEEPS
# upper fan lobes (her sweeping sleeves/aura) + lower emerald wedges
for r in range(0, 7):
    for c in range(3, 44):
        if canvas[r][c] != " ":
            continue
        dx = abs(c - 23)
        if dx < 5:
            continue
        dy = 2.0 * (5.5 - r) + 1.0
        ang = math.degrees(math.atan2(dy, dx))
        if 12 <= ang <= 58:
            h = (r * 41 + c * 13) % 100
            if h < 62:
                canvas[r][c] = ";:·;"[h % 4]
                classes[r][c] = "wings"
# teal swirl spill into the very top corners, inside the pillar caps
for r in range(0, 6):
    for cl in range(3, 11):
        for c in (cl, 46 - cl):
            if canvas[r][c] != " ":
                continue
            h = (r * 37 + c * 17) % 100
            if h < 48:
                canvas[r][c] = ";:·;"[h % 4]
                classes[r][c] = "wings"
for r in range(13, 29):
    for c in range(3, 44):
        if canvas[r][c] != " ":
            continue
        dx = abs(c - 23)
        if dx < 6:
            continue
        dy = 2.0 * (r - 12)
        if dy <= 0:
            continue
        ang = math.degrees(math.atan2(dy, dx))
        if 30 <= ang <= 52:
            h = (r * 41 + c * 13) % 100
            if h < 58:
                canvas[r][c] = ";:·;"[h % 4]
                classes[r][c] = "wings"

# bright under-arm webbing: pale glimmer where the veil is most radiant
for r in range(5, 13):
    for c in range(3, 44):
        if canvas[r][c] != " ":
            continue
        dx = abs(c - 23)
        if not (4 <= dx <= 17):
            continue
        h = (r * 29 + c * 23) % 100
        if h < 55:
            canvas[r][c] = "·'·."[h % 4]
            classes[r][c] = "veil"

# ============================================================ 3. FIELD FILL
# deep-blue ground glimmer everywhere else; pale shore across the base rows
for r in range(H):
    for c in range(W):
        if canvas[r][c] != " ":
            continue
        h = (r * 53 + c * 31 + (r * c) % 17) % 100
        if r >= 28:
            if h < 52:
                canvas[r][c] = "·-.·"[h % 4]
                classes[r][c] = "veil" if h % 3 else "field"
            continue
        d = math.hypot((c - 23) / 23.0, (r - 13) / 13.0)
        cov = 36 - 16 * min(d, 1.1)
        if h < cov:
            canvas[r][c] = "·.·'"[h % 4]
            classes[r][c] = "field"

# ============================================================ 4. PILLARS
# Mercy + Severity: three-wide flank columns, capital + base
PM(0, 0, "T==", "pillar")
for r in range(1, 21):
    PM(r, 0, "|::" if r % 2 else "|:·", "pillar")
PM(21, 0, "|==", "pillar")

# upper-corner swirl strokes riding the teal lobes
PM(0, 8, ",~~-,_", "wings")
PM(1, 13, "`~-,_", "wings")

# ============================================================ 5. THE FIGURE
# radiant halo punched around the head
for r in range(0, 4):
    for c in range(19, 28):
        CLR(r, c)
# torso first (arms land onto the shoulders afterwards)
PB(3, 21, " )·( ", "figure")
PB(4, 20, " (x|x) ", "figure")
PB(5, 19, " (xx|xx) ", "figure")
PB(6, 19, " (xx|xx) ", "figure")
PB(7, 19, " )xx|xx( ", "figure")
PB(8, 20, " )x|x( ", "figure")
PB(9, 20, " (x|x) ", "figure")
PB(10, 20, " )x|x( ", "figure")
PB(11, 20, " (xxx) ", "figure")
# crown of Isis: glow rays, waxing-full-waning, the face beneath
PB(0, 20, " ·\\¡/· ", "crown")
PB(1, 20, " )(O)( ", "crown")
PB(2, 20, " (´·`) ", "figure")
# gold-green aura caught at the halo's rim
PM(0, 18, "'", "crown")
PM(0, 19, "`", "crown")
PM(1, 18, "·", "crown")
PM(1, 19, "·", "crown")
PM(2, 19, "·", "crown")
PM(3, 20, "'", "crown")


# up-sweeping arm bands: a cleared channel holding a 2-row pale band
def arm_row(cc):
    t = (cc - 8) / 11.0
    return 2.3 + t * (5.3 - 2.3)


for cc in range(8, 20):
    rlow = int(round(arm_row(cc) + 0.45))
    for r_ in range(rlow - 2, rlow + 2):
        CLR(r_, cc)
        CLR(r_, 46 - cc)
prev = None
for cc in range(8, 20):
    rlow = int(round(arm_row(cc) + 0.45))
    nxt = int(round(arm_row(cc + 1) + 0.45))
    glow = "," if nxt != rlow else "_"
    ghigh = "`" if (prev is not None and prev != rlow) else "-"
    for r_, ch in ((rlow, glow), (rlow - 1, ghigh)):
        for c_, g_ in ((cc, ch), (46 - cc, ch.translate(MIRROR))):
            if 0 <= r_ < H:
                canvas[r_][c_] = g_
                classes[r_][c_] = "figure"
    prev = rlow
# teal spiral curls at the hands
PMB(1, 4, " ,--, ", "wings")
PMB(2, 3, " ((@), ", "wings")
PMB(3, 4, " `-´ ", "wings")

# ============================================================ 6. THE CUP
# wide crescent lyre/bow across her lap, scrolled ends, one clean curve
PB(12, 5, " ,c@C=" + "~" * 25 + "=C@c, ", "cup")
PB(13, 10, " `--," + "_" * 17 + ",--´ ", "cup")

# ============================================================ 7. TENT-THRONE
# latticed skirt widening to the base: folds every 4 cols, x-mesh between;
# the lowest rows dissolve into the net (holes, soft edges, no hard hemline)
for r in range(14, 25):
    hw = r - 10
    lc, rc = 23 - hw, 23 + hw
    dissolve = r >= 22
    if not dissolve:
        CLR(r, lc - 1)
        CLR(r, rc + 1)
    for c in range(lc, rc + 1):
        if dissolve and (r * 7 + c * 5) % 4 == 0:
            continue
        if c == lc:
            g = "x" if dissolve else "/"
        elif c == rc:
            g = "x" if dissolve else "\\"
        elif abs(c - 23) % 4 == 0:
            g = "|"
        else:
            g = "x" if (r + c) % 2 == 0 else "'"
        canvas[r][c] = g
        classes[r][c] = "figure"
# the hidden Book of Mysteries under the lyre; inverted crescent on the base
P(14, 22, "[=]", "cup")
P(21, 22, "/‾\\", "cup")

# ============================================================ 8. GARDEN
# pale mound beneath the camel
PB(26, 16, " ,.:::::::::., ", "figure")
# far-left crystals (lavender)
P(22, 1, ",^,", "crystal")
P(23, 0, "/:·:\\", "crystal")
P(24, 0, "<::::>", "crystal")
P(25, 0, "`\\::/´", "crystal")
P(26, 1, ",<>,", "crystal")
P(27, 0, "<:::>", "crystal")
P(28, 1, "`<>´", "crystal")
# concave-petal flower (receptive, Binah) left of the camel
PB(22, 7, " ,-, ,-, ", "flower")
PB(23, 6, " ((´)(`)) ", "flower")
PB(24, 6, " `,(@),´ ", "flower")
PB(25, 6, " ((,·,)) ", "flower")
PB(26, 7, " `-´`-´ ", "flower")
# green pine cone below
PB(27, 7, " ,(:), ", "cone")
PB(28, 6, " ((:::)) ", "cone")
PB(29, 6, " (:::::) ", "cone")
PB(30, 7, " `(:)´ ", "cone")
# the WHITE camel, dead center (gimel), standing on the mound
PB(23, 17, " o,__,^,_ ", "camel")
PB(24, 18, " (:::::::) ", "camel")
PB(25, 19, " ||   || ", "camel")
# purple grapes (Dionysus) at the camel's flank
PB(26, 28, " ,o, ", "grapes")
PB(27, 26, " ,o(o)o, ", "grapes")
PB(28, 26, " (o)o(o) ", "grapes")
PB(29, 27, " `o(o´ ", "grapes")
# the gold ten-band spiral shell (force, Chokmah), sweeping right
PB(21, 33, " _,,--~´ ", "shell")
PB(22, 31, " ,-~´,-~´ ", "shell")
PB(23, 30, " ,´,-´,-´ ", "shell")
PB(24, 29, " (,´,-´ ", "shell")
PB(25, 29, " ((@),´ ", "shell")
PB(26, 30, " `-´`~,_ ", "shell")
PB(27, 31, " `~--,_ ", "shell")
# rose pyramid + faceted dodecahedron, far right
PB(22, 41, " ,^, ", "pyramid")
PB(23, 40, " /:·\\ ", "pyramid")
PB(24, 39, " /;;::\\ ", "pyramid")
PB(25, 40, " ,-<>-, ", "crystal")
P(26, 40, "<:{}::>", "crystal")
PB(27, 40, " `<::>´", "crystal")
PB(28, 41, " `<>´ ", "crystal")

# small crystal shards anchoring the bottom corners
P(29, 0, ",<>,", "crystal")
P(30, 0, "`::´", "crystal")
P(29, 43, ",<>,", "crystal")
P(30, 43, "`::´", "crystal")

# ============================================================ 9. SIGNATURE
P(31, 2, "aw", "sig")

# ============================================================ 10. EMIT
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "02-priestess-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "02-priestess-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
