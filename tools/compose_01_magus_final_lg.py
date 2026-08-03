#!/usr/bin/env python3
"""Magus FINAL — panel synthesis (base v3b + grafts from v3a/v3c).

BASE (v3b, caduceus-spine dominant): full-width winged caduceus head with
the dove descending in the punched-clean circle; gold rod dead on col 23
from the disk to the bottom edge piercing the indigo Binah womb; serpent
lemniscate x-crossing; swastika-attitude figure; 4/4 object ring; ape
footnote; pleated two-blue radial fan field, near-zero black emptiness.

GRAFT 1 (v3a): the big dithered GOLD FOOT-WING masses — wide mirrored
;;-dithered sweeps in the lower third replacing v3b's thin wing corridors,
reading as lit painterly mass forming the Mercury-glyph arrowhead.

GRAFT 2 (v3c): the explicit Kether V — crisp white diagonals behind the
head/torso — interior FILLED with light white dither (' and .) so it is a
lit wedge, not negative space; form-lines/field strokes stay OUT of it.

FIX 3: 1-cell halo punched around the figure (background classes only) and
background diagonals broken behind him so the Mercury-glyph body pops.
FIX 4: darker indigo depth kept, but upper-fan luminance lifted toward the
scan's teal (field cells promoted to the lighter rays class).

Emits:
  drafts/01-magus-final-art-lg.txt       47x32 art, full-bleed
  drafts/01-magus-final-lg-classes.json  per-cell color classes (art coords)
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


# ---------------------------------------------------------------- regions
def v_halfw(r):
    """Kether V: wide at the shoulders, apex at the feet (r19)."""
    return (20.0 - r) * 0.85


def in_v(r, c):
    return 3 <= r <= 19 and abs(c - AXIS) <= v_halfw(r)


def in_womb(r, c):
    """Binah womb triangle, apex under the feet, widening to the bottom."""
    return r >= 20 and abs(c - AXIS) <= (r - 19) * 1.0 + 0.5


# ---------------------------------------------------------------- field
# Pleated two-tone teal fan radiating from the winged disk (r1, c23);
# lit white Kether V behind the torso (GRAFT 2: light ' . dither, a lit
# wedge, not negative space); indigo Binah womb below. Full-bleed dithered
# ground -- never black emptiness.
FIN = ";x;:;%"          # indigo ramp (dense dark)

for r in range(H):
    for c in range(W):
        dx = c - AXIS
        h = (r * 53 + c * 31 + (r * c) % 17) % 100
        if in_v(r, c):
            # GRAFT 2 interior is filled AFTER the figure halo is punched
            # (below) so the lit wedge runs right up to a 1-cell dark rim
            continue
        if in_womb(r, c):
            if h < 92:
                P(r, c, FIN[h % len(FIN)], "indigo")
            continue
        # pleated fan: dense radial strokes, two blues by wedge parity.
        # Upper field fans from the winged disk; the lower field re-fans
        # upward-out from the womb apex (the Harris bottom fan).
        low = r >= 21
        if low:
            dy = 2.0 * (r - 19) + 0.001
        else:
            dy = 2.0 * (r - 1) + 0.001
        ang = math.atan2(dx, dy)
        wedge = int(round(ang / 0.22))
        adx = dx / dy if dy else 99
        g = "|" if abs(adx) < 0.22 else ("\\" if adx > 0 else "/")
        if wedge % 2:
            cls = "rays" if not low else "field"
        else:
            cls = "field" if not low else "indigo"
        # FIX 4: lift the upper fan toward the scan's teal luminance
        if not low and cls == "field" and h % 3 == 0:
            cls = "rays"
        if low and cls == "indigo" and h % 5 == 0:
            cls = "field"
        cov = 88 if r <= 10 else (85 if not low else 74)
        if h < cov:
            if h % 7 == 3:                 # sparkle in the weave
                g, cls = "·", "rays" if not low else "web"
            P(r, c, g, cls)

# GRAFT 2 edges: the EXPLICIT Kether V -- crisp white diagonals doubled
# with a lilac outer strand; form-lines never cross them
for r in range(3, 20):
    hw = v_halfw(r)
    P(r, int(round(AXIS - hw)), "\\", "kether")
    P(r, int(round(AXIS + hw)), "/", "kether")
    P(r, int(round(AXIS - hw)) - 1, "\\", "lilac")
    P(r, int(round(AXIS + hw)) + 1, "/", "lilac")
# crisp womb-triangle edges: pale web lines framing the dark pyramid
for r in range(21, H):
    hw = (r - 19) * 1.0 + 0.5
    P(r, int(round(AXIS - hw)) - 1, "/", "web")
    P(r, int(round(AXIS + hw)) + 1, "\\", "web")


# ---------------------------------------------------------------- web
def wline(r0, c0, r1, c1, cls="web"):
    """Pale form-line; only crosses field/rays/indigo, NEVER the V."""
    steps = max(abs(r1 - r0), abs(c1 - c0)) * 2
    for i in range(steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        rr, cc = int(round(r)), int(round(c))
        if not (0 <= rr < H and 0 <= cc < W):
            continue
        if in_v(rr, cc):
            continue
        if classes[rr][cc] not in (None, "field", "rays", "indigo"):
            continue
        dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99
        g = "|" if abs(dc) < 0.35 else ("\\" if dc > 0 else "/")
        P(rr, cc, g, cls)


# strands from the disk down the sides
wline(1, 23, 15, 0)
wline(1, 23, 24, 0)
wline(1, 23, 15, 46)
wline(1, 23, 24, 46)
# horizontal form-line mid-field (broken by the V)
for c in range(0, W, 2):
    if classes[13][c] in (None, "field", "rays") and not in_v(13, c):
        P(13, c, "-", "web")
# lower fan birthing out of the womb apex
wline(20, 23, 31, 2)
wline(20, 23, 31, 10)
wline(20, 23, 31, 36)
wline(20, 23, 31, 44)

# faint arc at the very bottom, birthing form
P(29, 17, "_,,--~~~--,,_", "lilac")

# ---------------------------------------------------------------- foot-wings
# GRAFT 1 (from v3a): the wide Mercury-glyph arrowhead -- big mirrored
# ;;-dithered gold masses swept to both borders, lit ,=´ upper edges
WING = [
    (15, 12, " ,=´;;;( "),
    (16, 8, " ,=´;;;;;;( "),
    (17, 5, " ,=´;;;;;;;;;( "),
    (18, 2, " ,=´;;;;;;;;;;;( "),
    (19, 0, " (=;;;;;;;;;;;;;\\ "),
    (20, 0, "(;;;;;;;;;;;;;;\\ "),
    (21, 0, "\\;;=,;;;;;;;;;\\ "),
    (22, 0, " ‾\\;;=,;;;;;=´ "),
    (23, 2, " ‾`==,;,=´ "),
]
for r, c, s in WING:
    PMB(r, c, s, "wings")

# ---------------------------------------------------------------- caduceus rod
# The hero spine: col 23, from inside the disk circle to the card bottom.
for r in range(1, H):
    P(r, 23, "|", "caduceus")

# ---------------------------------------------------------------- winged disk head
# full-width caduceus head: wings, circle, dove descending inside
PM(0, 2, ",,==;;=='''‾´", "gold")
P(0, 18, ",--~~*~~--,", "gold")
P(0, 23, "*", "dove")
PM(1, 0, "<<===;;;===((", "gold")
PM(1, 17, "((", "gold")
PB(1, 19, "  \\,_,/  ", "dove")
P(2, 19, "`--,", "gold")
PB(2, 23, "v", "dove")
P(2, 24, ",--´", "gold")
PM(2, 4, "''‾''", "rays")

# ---------------------------------------------------------------- serpents
# twined lemniscate below the disk, heads curling out as his horns
P(3, 18, ",6´)~x~(`6,", "serpent")
P(2, 17, "¡", "serpent")     # Isis throne headdress, left head
P(2, 29, "+", "serpent")     # plain crown, right head

# ---------------------------------------------------------------- objects (8)
# left: stylus, phoenix wand + flame, star-disk, wand of double power
PB(2, 8, " ,==´ ", "obj")                 # stylus by the raised hand
PB(6, 3, " )*( ", "flame")                # phoenix wand: flame head
PB(7, 4, " `¡´ ", "obj")                  #   and its shaft
PB(11, 2, " ,=*=, ", "sun")               # disk: 8-fold star of Mercury
PB(12, 2, " `---´ ", "sun")
PB(15, 1, " o=¡=o ", "obj")               # wand of double power
# right: scroll, winged egg, cup, dagger
PB(2, 36, " ,===, ", "obj")               # scroll / papyrus
PB(3, 36, " (o__) ", "obj")
P(6, 33, "<", "wings")                    # winged orphic egg
P(6, 34, "(:)", "egg")
P(6, 37, ">", "wings")
PB(9, 37, " o\\_/o ", "obj")              # two-handled Grecian cup
PB(10, 38, " `-´ ", "obj")
PB(13, 39, " <==+o ", "obj")              # dagger / stiletto

# ---------------------------------------------------------------- figure
# golden androgynous youth in swastika attitude, centered on col 23.
# FIX 3: before drawing, punch a 1-cell halo around his whole silhouette
# through the background lattice (background classes only) so the
# Mercury-glyph body pops from the dense field; he is drawn ON TOP.
FIG = [
    # head + winged helmet
    ("PB", 4, 17, " <´ ", "wings"),
    ("PB", 4, 26, " `> ", "wings"),
    ("PB", 4, 20, " ,;;;, ", "figure"),
    ("PB", 5, 20, " (´·`) ", "figure"),
    # torso
    ("PB", 6, 19, " (;;;;;) ", "figure"),
    ("PB", 7, 19, " (;;;;;) ", "figure"),
    ("PB", 8, 20, " );;;( ", "figure"),
    ("PB", 9, 20, " (;;;) ", "figure"),
    ("PB", 10, 19, " (;;;;;) ", "figure"),
    ("PB", 11, 19, " (;;;;;) ", "figure"),
    ("PB", 12, 20, " );;;( ", "figure"),
    # left arm raised high (viewer left), open hand + fingers
    ("PB", 5, 16, " ,=´", "figure"),
    ("PB", 4, 13, " ,=´", "figure"),
    ("PB", 3, 11, " \\¡/ ", "figure"),
    # right arm bent down, open hand
    ("P", 7, 27, "`=,_", "figure"),
    ("PB", 8, 30, "\\, ", "figure"),
    ("PB", 9, 28, " \\¡/ ", "figure"),
    # left leg: thigh horizontal to high knee, shin descending back in
    ("PB", 13, 13, " (;;;;;;´", "figure"),
    ("PB", 14, 14, " \\;, ", "figure"),
    ("PB", 15, 16, " \\;, ", "figure"),
    ("PB", 16, 17, " \\;, ", "figure"),
    ("PB", 17, 18, " \\; ", "figure"),
    # right leg: thigh descending to low knee, shin back in
    ("P", 13, 25, ";;;\\", "figure"),
    ("PB", 14, 26, " ;;\\ ", "figure"),
    ("PB", 15, 28, " ;;) ", "figure"),
    ("PB", 16, 27, " ,;/ ", "figure"),
    ("PB", 17, 25, " ,;/ ", "figure"),
    # feet together over the rod, serpent-strap ankles, toes pointed
    ("PB", 18, 19, " (;;;;;) ", "figure"),
    ("P", 18, 20, "s", "serpent"),
    ("P", 18, 26, "s", "serpent"),
    ("PB", 19, 20, " \\;;;/ ", "figure"),
    ("PB", 20, 21, " \\;/ ", "figure"),
]

# FIX 3 halo: dilate the figure silhouette by 1 cell in all directions and
# clear only background lattice there (never rod/serpent/wings/objects)
BG = {"field", "rays", "web", "kether", "lilac", "indigo"}
mask = set()
for mode, r, c, s, cls in FIG:
    for i, ch in enumerate(s):
        if ch != " " and 0 <= r < H and 0 <= c + i < W:
            mask.add((r, c + i))
for (r, c) in mask:
    for dr in (-1, 0, 1):
        for dc in (-2, -1, 0, 1, 2):
            rr, cc = r + dr, c + dc
            if 0 <= rr < H and 0 <= cc < W and classes[rr][cc] in BG:
                canvas[rr][cc] = " "
                classes[rr][cc] = None

# GRAFT 2 interior (post-halo): the Kether V is a LIT wedge -- near-solid
# light dither of ' and . filling it right up to a 1-cell dark rim around
# head/torso/legs. The thin ARMS keep no rim: in the scan the white strips
# run right behind them (their own PB spaces still punch an in-row halo
# when the figure is drawn on top).
ARM_ROWS = {(3, 11), (4, 13), (5, 16), (7, 27), (8, 30), (9, 28)}
near = set()
for mode, r, c, s, cls in FIG:
    if (r, c) in ARM_ROWS:
        continue
    for i, ch in enumerate(s):
        if ch != " ":
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    near.add((r + dr, c + i + dc))
for r in range(3, 20):
    for c in range(W):
        if not in_v(r, c) or v_halfw(r) - abs(c - AXIS) < 1.0:
            continue
        if (r, c) in near or classes[r][c] is not None:
            continue
        h = (r * 53 + c * 31 + (r * c) % 17) % 100
        if h < 96:
            P(r, c, "'" if h % 4 < 3 else ".", "kether")

for mode, r, c, s, cls in FIG:
    (PB if mode == "PB" else P)(r, c, s, cls)

# ---------------------------------------------------------------- ape of thoth
PB(21, 37, " ,m, ", "ape")
PB(22, 36, " /; ", "ape")
PB(23, 35, " ,(o´, ", "ape")
PB(24, 35, " (;;;;;) ", "ape")
PB(25, 35, " );;;;(_, ", "ape")
PB(26, 36, " U´`U  `c ", "ape")

# ---------------------------------------------------------------- garnish
# sunburst above the left foot-wing (Mercury heralds the Sun)
P(14, 7, "·*·", "sun")
P(13, 10, "·", "sun")
P(15, 9, "·", "sun")

# ---------------------------------------------------------------- sig
P(30, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "01-magus-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "01-magus-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
