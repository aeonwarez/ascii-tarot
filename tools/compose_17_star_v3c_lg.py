#!/usr/bin/env python3
"""Star v3c — SPIRAL-FIELD DOMINANT (ultracode panel, composer C).

Thesis: EVERYTHING in the frame spirals — a single procedural spiral
field whirls out of the great heptagram (upper-left) and sweeps across
the whole card as cosmic motion; the rose celestial globe (the stage,
centered on col 23) carries its own whirl around the second star; the
figure is a kneeling S-curve seen from behind, hair spiralling into the
sky, a long drape arc framing her right side. The ONE rigid rectilinear
read is the silver cup's dead-straight | | stream falling onto the
junction of land and water, kept in a quiet zone so the spiral-vs-
straight contrast is the hero.

Emits:
  drafts/17-star-v3c-art-lg.txt        47x32 art, full-bleed
  drafts/17-star-v3c-lg-classes.json   per-cell color classes (art coords)
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]


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


def hsh(r, c):
    return (r * 37 + c * 59 + (r * c) % 13) % 100


def arc_glyph(dx, dy, h=0):
    """Directional stroke for a CCW arc around a center; dy pre-scaled 2x."""
    ta = math.atan2(dy, dx) + math.pi / 2.0     # tangent, CCW
    sx, sy = math.cos(ta), math.sin(ta) / 2.0   # back to screen aspect
    ang = math.degrees(math.atan2(sy, sx)) % 180.0
    if ang < 22 or ang >= 158:
        return "~" if int(dx) % 2 else "-"      # wavy, never a dash run
    if ang < 68:
        return "\\"
    if ang < 112:
        return "(" if dx < 0 else ")"
    return "/"


# ------------------------------------------------- 1. spiral sky field
# One Archimedean spiral whirling CCW out of the great star's core.
# Arms are CONTINUOUS directional strokes (solid core, dotted fringe);
# gaps carry only quiet star-dust. Two quiet zones protect the rigid
# stream (lower-left) and the strip under the kneeling figure.
SR, SC = 2.5, 7.0          # spiral center = the great heptagram
PERIOD, ARMW = 6.5, 3.0    # arm spacing / arm width (radial cells)


def quiet(r, c):
    if r >= 16 and c <= 15:            # silver cup + rigid stream zone
        return True
    if r == 25 and 14 <= c <= 36:      # strip under the kneeling base
        return True
    return False


for r in range(0, 26):
    for c in range(W):
        h = hsh(r, c)
        if quiet(r, c):
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
                P(r, c, arc_glyph(dx, dy, h), "sky")  # solid stroke core
            elif t < 0.78:
                if h < 74:
                    ch = arc_glyph(dx, dy, h) if h % 4 == 0 else ",·.'"[h % 4]
                    P(r, c, ch, "sky")
            else:
                if h < 34:
                    P(r, c, "·.·,"[h % 4], "sky")
        else:                                   # between arms: quiet dust
            if h < 20:
                P(r, c, "·" if h % 2 else ".", "sky")

# ------------------------------------------------- 2. the globe (STAGE)
# Huge dithered rose sphere, center on the axis, lit from the upper
# left (the great star side), dense lower-right limb, soft rim ramp so
# the silhouette reads without an outline.
CX, CY, A, B = 23.0, 15.0, 17.0, 9.5
for r in range(H):
    for c in range(W):
        dxn, dyn = (c - CX) / A, (r - CY) / B
        rr = dxn * dxn + dyn * dyn
        if rr > 1.0:
            continue
        h = hsh(r, c)
        # star-studded heavens: sparse white points on the sphere
        if (r * 17 + c * 31) % 61 == 0:
            P(r, c, "·", "babalon")
            continue
        d = math.hypot(c - 12.0, 2.0 * (r - 9.0)) / 13.0   # light dist
        # on black, light = MORE ink: bright dense upper-left where the
        # great star shines, thinning to a soft shadow lower-right
        if rr > 0.84:                                       # limb band
            ch = ";" if h < 85 else ":"
        elif d < 0.95:                                      # lit by the star
            ch = ";" if h < 70 else "':"[h % 2]
        elif d < 1.50:
            ch = ";" if h < 72 else ":"
        else:                                               # soft far shadow
            ch = ";" if h < 55 else (":" if h < 85 else ".")
        if ch != " ":
            P(r, c, ch, "globe")
# the whirl ON the globe: pale arcs curling CCW around the second star,
# contained to the sphere's lit upper-left so the rose still dominates
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

# ------------------------------------------------- 3. the great star
# Seven-pointed A.'.A.'. heptagram, upper-left, spinning CCW: one ray
# straight up, NONE straight down; ray pairs UL/UR, L/R, LL/LR; tips
# curl trailing the spin.
PB(0, 3, " `,   '   ,  ", "star")
PB(1, 3, "  `. \\|/ ,´  ", "star")
PB(2, 1, " ·--=((o))=--· ", "star")
PB(3, 3, "  ,´ / \\ `.  ", "star")
PB(4, 3, " ´  ´   `  `, ", "star")

# ------------------------------------------------- 4. second star on globe
PB(8, 9, "  \\¡/  ", "babalon")
PB(9, 8, " -((o))- ", "babalon")
PB(10, 9, "  /¡\\  ", "babalon")
P(8, 15, "´", "babalon")               # CCW curl on the upper-right ray

# ------------------------------------------------- 5. Nuith, from behind
# Kneeling S-curve mass, silver body, halo-punched. Hair whorl at the
# crown; shoulders; spine curving left; hips/buttocks; folded kneeling
# legs at the shore. Visual mass balanced on col 23.
PB(4, 20, " ,(@@), ", "nuith")                    # hair whorl (behind)
PB(5, 19, " (´;;`) ", "nuith")                    # nape / falling hair
PB(6, 18, " ,;;;;;;, ", "silver")                 # shoulders
PB(7, 18, " (;;;;;;;) ", "silver")
PB(8, 18, " (;;;;;;;) ", "silver")
PB(9, 17, " );;;;;;( ", "silver")                 # spine curves left
PB(10, 17, " (;;;;;;) ", "silver")
PB(11, 16, " );;;;;( ", "silver")                 # waist pinch
PB(12, 16, " (;;;;;) ", "silver")
PB(13, 15, " (;;;;;;;) ", "silver")               # hips
PB(14, 15, " (;;;;;;;;) ", "silver")
PB(15, 14, " (;;;;;;;;;) ", "silver")             # buttocks
PB(16, 14, " (;;;;;;;;;;) ", "silver")
PB(17, 14, " );;;;;;;;;;) ", "silver")            # haunch
PB(18, 15, " );;;;;;;;;;`, ", "silver")           # thigh toward the knee
PB(19, 16, " `;;;;;;;;;;;), ", "silver")
PB(20, 17, " (;;;;;;;;;;;;) ", "silver")
PB(21, 17, " (;;;;;;;;;;;;;) ", "silver")         # folded shin
PB(22, 18, " `;;;;;;;;;;;;´) ", "silver")
PB(23, 19, " `--;;;;;;;--´ ", "silver")           # kneeling base
PB(24, 27, " (:) ", "silver")                     # sole of the foot
# spine highlight (sheen)
P(8, 22, "'", "nuith")
P(10, 21, "'", "nuith")
P(12, 20, "'", "nuith")
# raised right arm arching to the golden cup overhead
P(5, 27, ",´", "silver")
P(4, 28, "/", "silver")
P(3, 29, ",´", "silver")
P(2, 31, "-´", "silver")
# left arm sweeping down to the lowered silver cup
P(7, 17, ",", "silver")
P(8, 16, "´", "silver")
P(9, 16, ",", "silver")
P(10, 15, "(", "silver")
P(11, 14, "(", "silver")
P(12, 13, "(", "silver")
P(13, 12, "(", "silver")
P(14, 11, "(", "silver")

# ------------------------------------------------- 6. golden cup, raised
# Held overhead, tipped left, pouring the milk of the stars onto her
# own crown in a curved cascade (painted AFTER the head so it lands on
# the hair); the tiny star-seed tumbles out clockwise.
PB(0, 28, " ,--, ", "gold")
PB(1, 27, " (~~~_) ", "gold")
PB(2, 28, " `--´ ", "gold")
P(0, 35, "x", "babalon")               # star-seed, CW tumble
P(1, 36, "`,", "babalon")
PB(2, 25, " (( ", "gold")              # curved cascade to the crown
PB(3, 24, " (( ", "gold")
P(4, 24, "´", "gold")
P(3, 27, "·", "babalon")
P(2, 24, "·", "babalon")
P(4, 27, "¡", "babalon")

# hair whirling up into the clouds (right of the great star)
P(3, 16, ",~´", "nuith")
P(2, 18, "_,´", "nuith")
# the long drape arc framing her right side, crown to shore (Harris's
# blue sweep): a continuous ribbon two strokes thick, halo-punched
PB(6, 26, " ), ", "nuith")
PB(7, 27, " )) ", "nuith")
PB(8, 28, " )) ", "nuith")
PB(9, 28, " )) ", "nuith")
PB(10, 28, " )) ", "nuith")
PB(11, 27, " )) ", "nuith")
PB(12, 26, " )) ", "nuith")
PB(13, 26, " )) ", "nuith")
PB(14, 27, " )) ", "nuith")
PB(15, 28, " )) ", "nuith")
PB(16, 29, " )) ", "nuith")
PB(17, 30, " )) ", "nuith")
PB(18, 31, " )), ", "nuith")
PB(19, 32, " )), ", "nuith")
PB(20, 33, " )), ", "nuith")
PB(21, 34, " `), ", "nuith")
PB(22, 35, " `~, ", "nuith")
PB(23, 36, " `-, ", "nuith")

# ------------------------------------------------- 7. shore + witnesses
# Pyramid City on the horizon across the Sea of Binah (left)
P(22, 0, "-~·-~·-~", "water")                     # far sea horizon
PB(23, 0, " ,^,/\\, ", "pyramid")
PB(24, 0, " ´:`´:`` ", "pyramid")
# the sea, left
P(25, 0, "~.~^~.~^~.", "water")
P(26, 0, ".~^~.~^~.~", "water")
P(27, 0, "~.~^~.~^~", "water")
P(28, 0, ".~^~.~^~", "water")
P(29, 0, "~.~^~.~", "water")
P(30, 0, ".~^~.~^", "water")
P(31, 0, "~.~^~.~^", "water")
# crystalline earth: faceted seven-sided solids, shaded planes
P(26, 12, "_,/\\.___,/\\,____./\\,__,/\\._/\\,_", "crystal")
P(27, 12, "/:·\\/\\:/<:>\\:/·\\/\\::/<>\\/::\\/\\:/\\", "crystal")
P(28, 12, "\\/´`\\/;;\\/´‾\\/::\\/´`\\/;;\\/`´\\/:\\", "crystal")
P(29, 12, "/\\::/<>\\/:·\\/\\;/<:>\\/::\\/\\·:/\\;/", "crystal")
P(30, 12, "\\/;;\\/´`\\/::\\/`´\\/;;\\/´`\\/::\\/´`", "crystal")
P(31, 9, "_/\\:_/::\\_/;;\\_/:·\\_/::\\_/;\\_/:\\_/", "earth")
# dark red roses, right shore
P(24, 40, ",o,", "rose")
P(25, 37, ",o,", "rose")
P(25, 43, ",o,", "rose")
# butterflies, liberated souls, right sky
PB(12, 41, " }v{ ", "fly")
PB(19, 40, " }v{ ", "fly")
PB(7, 42, " }v{ ", "fly")

# ------------------------------------------------- 8. silver cup + THE
# one rigid rectilinear stream — painted LAST so nothing breaks it.
PB(15, 7, " .--. ", "silver")
PB(16, 6, " ( ~~ ) ", "silver")
PB(17, 7, " `--´ ", "silver")
for r in range(18, 28):
    PB(r, 8, " | | ", "silver")
P(28, 8, "·¡:¡·", "silver")                       # the splash at the junction

# ------------------------------------------------- sig
P(30, 2, "aw", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "17-star-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "17-star-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
