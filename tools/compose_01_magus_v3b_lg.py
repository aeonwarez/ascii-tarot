#!/usr/bin/env python3
"""Magus v3b — ultracode panel candidate B: CADUCEUS-SPINE DOMINANT.

The full-height golden caduceus is the hero: winged head spanning the top
with the dove descending in its circle, rod on col 23 running from below
the figure's feet to the card bottom, piercing the indigo Binah womb.
The Mercury-glyph youth (serpent horns above, foot-wings below, swastika
attitude) is overlaid on the spine; eight juggled objects ring him 4/4;
white Kether V behind the torso tapering to the feet; Ape of Thoth
groping up lower-right.

Emits:
  drafts/01-magus-v3b-art-lg.txt       47x32 art, full-bleed
  drafts/01-magus-v3b-lg-classes.json  per-cell color classes (art coords)
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
# glowing white Kether V behind the torso; indigo Binah womb below.
# Full-bleed dithered ground -- never black emptiness.
FKA = "'\"'·\"'"       # kether ramp (bright)
FLI = "·''::"          # lilac ramp
FIN = ";x;:;%"         # indigo ramp (dense dark)

for r in range(H):
    for c in range(W):
        dx = c - AXIS
        h = (r * 53 + c * 31 + (r * c) % 17) % 100
        if in_v(r, c):
            hw = v_halfw(r)
            edge = abs(dx) >= hw - 1.5
            cls = "lilac" if (edge or r >= 16) else "kether"
            if h < 94:
                ramp = FLI if cls == "lilac" else FKA
                P(r, c, ramp[h % len(ramp)], cls)
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
        cov = 88 if r <= 10 else (85 if not low else 74)
        if h < cov:
            if h % 7 == 3:                 # sparkle in the weave
                g, cls = "·", "rays" if not low else "web"
            P(r, c, g, cls)

# crisp V edges: lilac strands the form-lines never cross
for r in range(3, 20):
    hw = v_halfw(r)
    P(r, int(round(AXIS - hw)) - 1, "\\", "lilac")
    P(r, int(round(AXIS + hw)) + 1, "/", "lilac")
# crisp womb-triangle edges: pale web lines framing the dark pyramid
for r in range(21, H):
    hw = (r - 19) * 1.0 + 0.5
    P(r, int(round(AXIS - hw)) - 1, "/", "web")
    P(r, int(round(AXIS + hw)) + 1, "\\", "web")


# ---------------------------------------------------------------- web
def wline(r0, c0, r1, c1, cls="web"):
    """Pale form-line; only crosses field/rays/indigo, never the V."""
    steps = max(abs(r1 - r0), abs(c1 - c0)) * 2
    for i in range(steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        rr, cc = int(round(r)), int(round(c))
        if not (0 <= rr < H and 0 <= cc < W):
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
    if classes[13][c] in (None, "field", "rays"):
        P(13, c, "-", "web")
# lower fan birthing out of the womb apex
wline(20, 23, 31, 2)
wline(20, 23, 31, 10)
wline(20, 23, 31, 36)
wline(20, 23, 31, 44)

# faint arc at the very bottom, birthing form
P(29, 17, "_,,--~~~--,,_", "lilac")

# ---------------------------------------------------------------- foot-wing sweeps
# great golden bands sweeping from the feet to the lower corners:
# solid diagonal corridors, dithered gold, bright upper edge
for r in range(20, 28):
    cl = 21.0 - 2.4 * (r - 19)
    for c in range(W):
        d = c - cl
        if -2.4 <= d <= 2.4:
            h = (r * 41 + c * 13) % 100
            g = "´" if d > 1.4 else ("=" if h < 55 else ";")
            P(r, c, g, "gold")
for r in range(20, 26):
    cr = 25.0 + 2.4 * (r - 19)
    for c in range(W):
        d = c - cr
        if -2.4 <= d <= 2.4:
            h = (r * 41 + c * 13) % 100
            g = "`" if d < -1.4 else ("=" if h < 55 else ";")
            P(r, c, g, "gold")

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
# golden androgynous youth in swastika attitude, centered on col 23
# head + winged helmet
PB(4, 17, " <´ ", "wings")
PB(4, 26, " `> ", "wings")
PB(4, 20, " ,;;;, ", "figure")
PB(5, 20, " (´·`) ", "figure")
# torso
PB(6, 19, " (;;;;;) ", "figure")
PB(7, 19, " (;;;;;) ", "figure")
PB(8, 20, " );;;( ", "figure")
PB(9, 20, " (;;;) ", "figure")
PB(10, 19, " (;;;;;) ", "figure")
PB(11, 19, " (;;;;;) ", "figure")
PB(12, 20, " );;;( ", "figure")
# left arm raised high (viewer left), open hand + fingers
PB(5, 16, " ,=´", "figure")
PB(4, 13, " ,=´", "figure")
PB(3, 11, " \\¡/ ", "figure")
# right arm bent down, open hand
P(7, 27, "`=,_", "figure")
PB(8, 30, "\\, ", "figure")
PB(9, 28, " \\¡/ ", "figure")
# left leg: thigh horizontal to high knee, shin descending back in
PB(13, 13, " (;;;;;;´", "figure")
PB(14, 14, " \\;, ", "figure")
PB(15, 16, " \\;, ", "figure")
PB(16, 17, " \\;, ", "figure")
PB(17, 18, " \\; ", "figure")
# right leg: thigh descending to low knee, shin back in
P(13, 25, ";;;\\", "figure")
PB(14, 26, " ;;\\ ", "figure")
PB(15, 28, " ;;) ", "figure")
PB(16, 27, " ,;/ ", "figure")
PB(17, 25, " ,;/ ", "figure")
# feet together over the rod, serpent-strap ankles, toes pointed
PB(18, 19, " (;;;;;) ", "figure")
P(18, 20, "s", "serpent")
P(18, 26, "s", "serpent")
PB(19, 20, " \\;;;/ ", "figure")
PB(20, 21, " \\;/ ", "figure")
# foot wings flaring at the ankles
P(18, 15, "<==´", "wings")
P(18, 27, "`==>", "wings")

# ---------------------------------------------------------------- ape of thoth
PB(21, 37, " ,m, ", "ape")
PB(22, 36, " /; ", "ape")
PB(23, 35, " ,(o´, ", "ape")
PB(24, 35, " (;;;;;) ", "ape")
PB(25, 35, " );;;;(_, ", "ape")
PB(26, 36, " U´`U  `c ", "ape")

# ---------------------------------------------------------------- garnish
P(19, 10, "·*·", "sun")      # sunburst behind the left foot-wing

# ---------------------------------------------------------------- sig
P(30, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "01-magus-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "01-magus-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
