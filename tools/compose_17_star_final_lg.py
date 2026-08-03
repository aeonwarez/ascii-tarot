#!/usr/bin/env python3
"""Star FINAL — ultracode panel synthesis (judge tally v3a 7, v3c 7, v3b 4).

BASE (v3a): the stage-scale rose globe centered on the axis (col 23),
density-ramped directional dither + limb darkening + rim hoop; the rigid
| | silver stream (the ONLY pure vertical) landing at the land/water
junction; the shaded crystal facet band; axis discipline.
GRAFT 1 (v3b): the figure kit — larger kneeling Nuith from behind
(hair-knot head, cyan hair whirl rising, raised-arm chain to the gold
cup, dithered S-curve torso) painted ON TOP of the globe with a 1-2 cell
halo punched around her silhouette so the occlusion boundary resolves.
GRAFT 2 (v3c): the living spiral field — indigo spiral strokes over the
corners and upper field, the )) drape sweeping down the right of the
globe, ~-~ shore waves — the whole field spirals against the one stream.
FIX 3: handedness per the Harris scan — gold cup TOP-RIGHT pours its
curved cascade onto her own crown; silver cup LOWER-LEFT feeds the
rigid stream. FIX 4: all three stars are real 7-point heptagrams
(3 upper rays, 2 side, 2 lower — none straight down).

Emits:
  drafts/17-star-final-art-lg.txt        47x32 art, full-bleed
  drafts/17-star-final-lg-classes.json   per-cell color classes
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]


def P(r, c, s, cls):
    """Paint string s at (r, c); spaces are transparent."""
    for i, ch in enumerate(s):
        if ch != " " and 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls


def PB(r, c, s, cls):
    """Paint with halo: spaces in s ERASE (1-cell breathing room)."""
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


def hsh(r, c):
    return (r * 37 + c * 59 + (r * c) % 13) % 100


def arc_glyph(dx, dy):
    """Directional stroke for a CCW arc around a center; dy pre-scaled 2x."""
    ta = math.atan2(dy, dx) + math.pi / 2.0     # tangent, CCW
    sx, sy = math.cos(ta), math.sin(ta) / 2.0   # back to screen aspect
    ang = math.degrees(math.atan2(sy, sx)) % 180.0
    if ang < 22 or ang >= 158:
        return "~" if int(dx) % 2 else "-"
    if ang < 68:
        return "\\"
    if ang < 112:
        return "(" if dx < 0 else ")"
    return "/"


# ------------------------------------------------- 1. spiral sky field (v3c)
# One Archimedean spiral whirling CCW out of the great star's core sweeps
# the whole field; a quiet zone protects the silver cup + rigid stream.
SR, SC = 2.5, 7.0
PERIOD, ARMW = 6.5, 3.0

for r in range(0, 25):
    for c in range(W):
        h = hsh(r, c)
        if r >= 15 and c <= 15:                # cup + rigid stream zone
            if h < 14:
                P(r, c, "·", "sky")
            continue
        dx = c - SC
        dy = 2.0 * (r - SR)
        d = math.hypot(dx, dy)
        th = math.atan2(dy, dx)
        phase = (d - PERIOD * th / (2 * math.pi)) % PERIOD
        if (r * 13 + c * 29) % 53 == 0:
            P(r, c, "'", "star")               # white star-dust
            continue
        if phase < ARMW:                        # inside an arm
            t = phase / ARMW
            if t < 0.45:
                P(r, c, arc_glyph(dx, dy), "sky")
            elif t < 0.78:
                if h < 74:
                    ch = arc_glyph(dx, dy) if h % 4 == 0 else ",·.'"[h % 4]
                    P(r, c, ch, "sky")
            else:
                if h < 34:
                    P(r, c, "·.·,"[h % 4], "sky")
        else:                                   # between arms: quiet dust
            if h < 20:
                P(r, c, "·" if h % 2 else ".", "sky")

# ------------------------------------------------- 2. the GLOBE (v3a base)
# The stage. Ellipse centered on the axis, A=20.5 x B=10.25 (2:1 baked
# in): cols ~3..43, rows ~4..23. Lit upper-left toward the great star,
# dense rose mass on the lower-right limb, faint spiral banding.
CX, CY, A, B = 23.0, 13.5, 20.5, 10.25
LR, LC = 6.5, 12.0
for r in range(H):
    for c in range(W):
        dx, dy = (c - CX) / A, (r - CY) / B
        rr = dx * dx + dy * dy
        if rr > 1.0:
            continue
        canvas[r][c] = " "                      # clear sky inside the sphere
        classes[r][c] = None
        l = math.hypot((c - LC) / (2 * A), (r - LR) / B)
        shade = 0.62 * l + 0.45 * rr
        d = math.sqrt(rr)
        th = math.atan2(dy, dx)
        shade += 0.10 * math.sin(3.0 * th + 7.0 * d)
        h = ((r * 5 + c * 3 + (r * c) % 5) % 11) / 11.0
        if shade < 0.20:
            ch = "'" if h < 0.60 else "·"
        elif shade < 0.38:
            ch = "·" if h < 0.50 else "."
        elif shade < 0.60:
            ch = ":" if h < 0.55 else "."
        elif shade < 0.85:
            ch = ";" if h < 0.60 else ":"
        else:
            ch = ";" if h < 0.75 else "%"
        if ch != " ":
            P(r, c, ch, "globe")

# rim hoop: crisp sphere boundary riding the ellipse edge
for r in range(H):
    dyn = (r - CY) / B
    s = 1 - dyn * dyn
    if s < 0:
        continue
    x = A * math.sqrt(s)
    cl, cr = int(round(CX - x)), int(round(CX + x))
    if abs(dyn) > 0.90:
        ch = "-" if dyn < 0 else "_"
        for c in range(cl + 2, cr, 2):
            P(r, c, ch, "globe")
    elif abs(dyn) > 0.55:
        P(r, cl, "/" if dyn < 0 else "\\", "globe")
        P(r, cr, "\\" if dyn < 0 else "/", "globe")
    else:
        P(r, cl, "(", "globe")
        P(r, cr, ")", "globe")

# the whirl ON the globe (v3c): pale arcs curling CCW around the second
# star, contained to the sphere's lit upper-left
GR, GC = 9.0, 12.0
for r in range(H):
    for c in range(W):
        dxn, dyn = (c - CX) / A, (r - CY) / B
        if dxn * dxn + dyn * dyn > 0.72 or r > 15:
            continue
        dx = c - GC
        dy = 2.0 * (r - GR)
        d2 = math.hypot(dx, dy)
        if d2 > 9.0 or d2 < 2.2:
            continue
        phase = (d2 - 5.0 * math.atan2(dy, dx) / (2 * math.pi)) % 5.0
        if phase < 0.95 and hsh(r, c) < 55:
            P(r, c, arc_glyph(dx, dy), "babalon")

# star-dust speckles on the sphere (Harris dusts the rose with white)
for r, c in [(7, 35), (9, 39), (11, 36), (13, 38), (17, 37), (20, 31)]:
    P(r, c, "'", "babalon")

# ------------------------------------------------- 3. shore
# Sea of Binah (left, v3c living waves) meets the crystalline earth; the
# rigid stream lands at the junction (~col 12-14).
for r in range(25, H):
    for c in range(W):
        canvas[r][c] = " "
        classes[r][c] = None
# sea horizon full width behind her kneel
for c in range(W):
    k = (c * 3 + 1) % 5
    ch = "~" if k == 0 else ("·" if k == 2 else ("-" if k == 3 else " "))
    if ch != " ":
        P(25, c, ch, "water")
# the sea, left, whirling wave rows (v3c)
P(26, 0, "~.~^~.~^~.~^~.~", "water")
P(27, 0, ".~^~.~^~.~^~.~", "water")
P(28, 0, "~.~^~.~^~.~^~", "water")
P(29, 0, ".~^~.~^~.~^~", "water")
P(30, 0, "~.~^~.~^~.~^", "water")
# Pyramid City far across the sea, tiny
PB(25, 3, " ,^,^, ", "pyramid")
PB(26, 2, " /:¡::\\ ", "pyramid")
# crystalline earth: seven-sided solids, facets shaded light/dark (v3a)
P(26, 15, ",_,/\\,__,/\\_,__,/\\,_,/\\,_,/\\,_", "crystal")
P(27, 14, "/'::\\/;;\\/':\\/‾;\\/'::\\/;'\\/::\\", "crystal")
P(28, 13, "/':;;\\/'‾\\/;::\\/':\\/;;'\\/‾:\\/;:\\", "crystal")
P(29, 13, "\\;/'\\/::;\\/';;\\/:'\\/‾;:\\/';\\/;'/", "crystal")
P(30, 14, "`\\/;:'\\/‾'\\/:;\\/';:\\/:‾\\/;;\\/´", "crystal")
# mauve earth underline, full-bleed to the corner
P(31, 0, "~.~^~.~^~.~^~", "water")
P(31, 13, "_,;:;,_,:;:,_,;:;,_,:;:,_,;:;,_,:_", "earth")

# ------------------------------------------------- 4. the great star
# TRUE heptagram: 3 upper rays (\ | /), 2 side (= =), 2 lower (/ \) —
# none straight down — tips curled trailing the CCW spin.
PB(0, 3, " `,   '   ,  ", "star")
PB(1, 3, "  `. \\|/ ,´  ", "star")
PB(2, 1, " ·--=((o))=--· ", "star")
PB(3, 3, "  ,´ / \\ `.  ", "star")
PB(4, 3, " ´  ´   `  `, ", "star")

# ------------------------------------------------- 5. star ON the globe
# second heptagram whirling on the sphere: 3 up, 2 side, 2 down, curls
PB(8, 10, " \\'/ ", "babalon")
PB(9, 7, " ·-((o))-· ", "babalon")
PB(10, 9, " ,/ \\, ", "babalon")
P(7, 14, "´", "babalon")
P(11, 8, ",", "babalon")

# ------------------------------------------------- 6. NUITH (v3b kit)
# From behind, kneeling against the globe, whirling: hair-knot head,
# cyan hair whirl rising, S-curve torso, )) drape (v3c) down her right.
# Entries are (row, col, string, class, halo): halo 2 = strong punch
# (silhouette masses), halo 1 = weak 1-cell clearance (ribbons, arms).
FIG = [
    # cyan hair whirl rising up-left toward the vortex
    (3, 15, "_,--~", "nuith", 1),
    (4, 17, ",-;´", "nuith", 1),
    # hair-knot head seen from behind + nape
    (4, 22, ",cCc,", "nuith", 2),
    (5, 22, "c;;;c", "nuith", 2),
    (6, 23, "`;´", "silver", 2),
    # curved gold cascade landing on her own crown (+ babalon droplets)
    (2, 26, "((", "gold", 1),
    (3, 25, "((", "gold", 1),
    (1, 26, "'", "babalon", 1),
    (2, 24, "·", "babalon", 1),
    (3, 28, "¡", "babalon", 1),
    # raised arm chain, shoulder to the gold cup
    (6, 27, ",´", "silver", 1),
    (5, 29, "/", "silver", 1),
    (4, 30, "/", "silver", 1),
    (3, 31, ",-´", "silver", 1),
    # S-curve torso mass: shoulders right, waist left, hips back right
    (7, 22, "(;;´;;;)", "silver", 2),
    (8, 21, "(;;;´;;)", "silver", 2),
    (9, 20, "(;;;;´;)", "silver", 2),
    (10, 19, ");;;;;(", "silver", 2),
    (11, 18, "(;;;;;)", "silver", 2),
    (12, 18, "(;;;´;)", "silver", 2),
    (13, 18, "(;;;;´;;)", "silver", 2),
    (14, 17, "(;;;;;´;;)", "silver", 2),
    (15, 17, "(;;;;;;´;;)", "silver", 2),
    (16, 16, "(;;;;;;;;;)", "silver", 2),
    (17, 16, ");;;;;;;;(", "silver", 2),
    (18, 16, ");;;;;´;;),", "silver", 2),
    (19, 16, "`;;;;;;;;;),", "silver", 2),
    (20, 16, "(;;;;;;;;;;)", "silver", 2),
    (21, 17, "`;;;;;;;;;;´)", "silver", 2),
    (22, 18, "`--;;;;;;--´", "silver", 2),
    (23, 26, "(::)", "silver", 2),
    # lowered arm reaching down-left to the silver cup
    (12, 16, "(", "silver", 1),
    (13, 15, "(", "silver", 1),
    (14, 13, ",´", "silver", 1),
    (15, 11, ",´", "silver", 1),
    # the )) drape whirling down her right side to the shore (v3c)
    (7, 30, "),", "nuith", 1),
    (8, 31, "))", "nuith", 1),
    (9, 32, "))", "nuith", 1),
    (10, 32, "))", "nuith", 1),
    (11, 31, "))", "nuith", 1),
    (12, 31, "))", "nuith", 1),
    (13, 31, "))", "nuith", 1),
    (14, 31, "))", "nuith", 1),
    (15, 31, "))", "nuith", 1),
    (16, 32, "))", "nuith", 1),
    (17, 32, "))", "nuith", 1),
    (18, 33, ")),", "nuith", 1),
    (19, 34, ")),", "nuith", 1),
    (20, 35, ")),", "nuith", 1),
    (21, 36, "`),", "nuith", 1),
    (22, 37, "`~,", "nuith", 1),
    (23, 38, "`-,", "nuith", 1),
    # the veil pooling on the shore at her kneel (fills the dead band)
    (24, 30, "`~;,__,;~´", "nuith", 1),
]

# figure cells, then the halo punch. Strong halo (masses): adjacent ring
# cleared to ' ', outer horizontal ring softened to '.' where the globe
# dither sat — the occlusion boundary resolves and she never blends into
# the globe. Weak halo (ribbons/arms): 1-cell side clearance only, so
# the drape stays hugged by the globe dither instead of a dead canyon.
cells = set()
strong = set()
for r, c, s, cls, st in FIG:
    for i, ch in enumerate(s):
        if ch != " ":
            cells.add((r, c + i))
            if st == 2:
                strong.add((r, c + i))
for (r, c) in strong:
    for dr in (-1, 0, 1):
        for dc in (-2, -1, 0, 1, 2):
            rr_, cc_ = r + dr, c + dc
            if not (0 <= rr_ < H and 0 <= cc_ < W) or (rr_, cc_) in cells:
                continue
            if abs(dc) == 2:
                if classes[rr_][cc_] in ("globe", "babalon"):
                    canvas[rr_][cc_] = "."
                    classes[rr_][cc_] = "globe"
            else:
                canvas[rr_][cc_] = " "
                classes[rr_][cc_] = None
for (r, c) in cells - strong:
    for cc_ in (c - 1, c, c + 1):
        if 0 <= cc_ < W and (r, cc_) not in cells:
            canvas[r][cc_] = " "
            classes[r][cc_] = None
for r, c, s, cls, st in FIG:
    P(r, c, s, cls)
# sheen highlights tracing the spine
P(9, 23, "'", "nuith")
P(11, 21, "'", "nuith")
P(13, 22, "'", "nuith")
P(15, 23, "'", "nuith")

# ------------------------------------------------- 7. gold cup, raised
# TOP-RIGHT per the scan, tipped, pouring the milk of the stars in a
# CURVED cascade onto her own crown; hand of the raised arm grips it.
# Painted after the figure so no halo bites the bowl.
PB(0, 27, " _,--, ", "gold")
PB(1, 27, "(~~~o) ", "gold")
PB(2, 28, "`-,-´ ", "gold")
# star-seed tumbling CLOCKWISE out of the cup (third heptagram, tiny)
PB(1, 35, " \\'/ ", "babalon")
PB(2, 34, " -(o)-. ", "babalon")
PB(3, 35, " / \\ ", "babalon")
P(4, 39, ",", "babalon")

# ------------------------------------------------- 8. witnesses
PB(12, 41, " }v{ ", "fly")
PB(18, 42, " }v{ ", "fly")
PB(24, 40, " }v{ ", "fly")
PB(26, 40, " ,o, ", "rose")
PB(27, 43, " ,o, ", "rose")
PB(28, 38, " ,o, ", "rose")

# ------------------------------------------------- 9. silver cup + THE
# one rigid rectilinear stream, painted LAST so nothing breaks it,
# landing on the junction of land and water.
PB(16, 8, " ,--, ", "silver")
PB(17, 7, " ( ~~ ) ", "silver")
PB(18, 8, " `)(´ ", "silver")
for r in range(19, 28):
    PB(r, 9, " | | ", "silver")
PB(28, 8, " ¡·:·¡ ", "silver")

# ------------------------------------------------- sig
PB(30, 1, " aw ", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "17-star-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "17-star-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
