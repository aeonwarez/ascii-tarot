#!/usr/bin/env python3
"""Magus v3c — ultracode panel candidate C: JUGGLING-ORBIT dominant.

The eight objects flung WIDE in a balanced ring around the card (stylus,
phoenix-torch, 8-star disk, double-wand on the left; scroll, winged egg,
cup, dagger on the right), the golden Mercury-glyph figure smaller at the
centered hub: serpent-horns above, wide foot-wings below, bound feet on
the caduceus rod that runs col 23 top to bottom. Winged disk + descending
dove at top, white Kether V behind the torso, teal ray-fan field, indigo
Binah wedge below the feet with golden ribbon arcs sweeping to the lower
corners, the Ape of Thoth groping up the right arc.

Emits:
  drafts/01-magus-v3c-art-lg.txt       47x32 art, full-bleed
  drafts/01-magus-v3c-lg-classes.json  per-cell color classes (art coords)
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23.0

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]
MIRROR = str.maketrans("()/\\[]{}<>`´", ")(\\/][}{><´`")


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


# ------------------------------------------------------------- Kether V
# White wedge behind head/torso, point down near the hips. Form-lines
# never enter it.
def v_width(r):
    return 1.0 + 11.0 * (15 - r) / 13.0


def in_v(r, c):
    if not (2 <= r <= 15):
        return False
    return abs(c - AXIS) < v_width(r)


# --------------------------------------------------------- ray-fan field
# Teal fan radiating from the winged disk at top center; indigo Binah
# wedge + depths below the feet.
def wedge_half(r):
    return 1.0 + (r - 18) * 1.35


for r in range(H):
    for c in range(W):
        dx = c - AXIS
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        # Binah wedge below the feet: dense indigo
        if r >= 19 and abs(dx) <= wedge_half(r):
            if h < 90:
                P(r, c, ";;:;"[h % 4] if h % 23 else "%", "indigo")
            continue
        # lower side depths: quieter indigo
        if r >= 21:
            if h < 68:
                P(r, c, ";:·;"[h % 4], "indigo")
            continue
        # Kether V: bright white light, edged in lilac; calm halo around
        # the figure silhouette so the small gold hub pops
        if in_v(r, c):
            w = v_width(r)
            cov = 26 if (18 <= c <= 28 and 3 <= r <= 15) else 66
            if w - abs(dx) < 1.0:
                P(r, c, "\\" if dx < 0 else "/", "lilac")
            elif h < cov:
                P(r, c, "'·'\""[h % 4], "kether")
            continue
        # the fan: angular sectors alternating field / rays
        dy = 2.0 * r + 1.0
        ang = math.atan2(dx, dy)
        sec = int((ang + math.pi / 2) / (math.pi / 14.0))
        if sec % 2 == 0:
            if h < 64:
                P(r, c, "'·';"[h % 4], "rays")
        else:
            if h < 88:
                P(r, c, ";:;:"[h % 4], "field")

# ------------------------------------------------------ web form-lines
def wline(r0, c0, r1, c1, cls):
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        rr, cc = int(round(r)), int(round(c))
        if not (0 <= rr < H and 0 <= cc < W) or in_v(rr, cc):
            continue
        dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99
        g = "|" if abs(dc) < 0.35 else ("\\" if dc > 0 else "/")
        if abs(dc) > 2.5:
            g = "-"
        P(rr, cc, g, cls)


wline(9, 0, 22, 46, "web")
wline(9, 46, 22, 0, "web")
wline(31, 23, 20, 2, "web")
wline(31, 23, 20, 44, "web")
wline(31, 23, 26, 0, "web")
wline(31, 23, 26, 46, "web")

# ------------------------------------------- golden ribbon arcs (motion)
PM(18, 20, ",´", "gold")
PM(19, 15, "_,==´", "gold")
PM(20, 10, "_,==´", "gold")
PM(21, 5, "_,==´", "gold")
PM(22, 1, ",==´", "gold")
PM(23, 0, "=´", "gold")
# inner fainter pair
PM(20, 17, "_,-´", "caduceus")
PM(21, 13, "_,-´", "caduceus")
PM(22, 9, "_,-´", "caduceus")
PM(23, 5, "_,-´", "caduceus")
PM(24, 2, ",-´", "caduceus")

# ----------------------------------------------- bottom arc birthing form
P(30, 14, "_,-------", "lilac")
P(30, 24, "-------,_", "lilac")
P(31, 12, ",´", "lilac")
P(31, 32, "`,", "lilac")

# ------------------------------------------------------- caduceus rod
for r in range(2, 32):
    P(r, 23, "|", "caduceus")

# --------------------------------------------- winged disk + dove (top)
PM(0, 1, "<~==--,__,---~==--,_", "wings")
PM(1, 3, "`~==--´", "wings")
PB(0, 19, " ,(´V`), ", "gold")
P(0, 23, "V", "dove")
PB(1, 20, " `,¡,´ ", "gold")
P(1, 23, "¡", "dove")

# --------------------------------------------- serpents (lemniscate horns)
# figure-8 above the head, heads curling outward: left wears the Isis
# throne (¡), right the plain crown (^); the rod threads the cross
P(1, 13, "¡", "serpent")
P(1, 32, "^", "serpent")
PB(2, 12, " <o~ ", "serpent")
PB(2, 16, " ,~~, ", "serpent")
PB(2, 26, " ,~~, ", "serpent")
PB(2, 31, " ~o> ", "serpent")
PB(3, 20, " `,x,´ ", "serpent")
P(3, 19, "s", "serpent")
P(3, 27, "S", "serpent")

# ------------------------------------------------- the eight objects
# LEFT ring, top to bottom: stylus / phoenix torch / 8-star disk / double wand
PB(4, 7, " O=\\ ", "obj")          # stylus, nib down-right
PB(5, 9, " \\ ", "obj")
PB(6, 10, " · ", "obj")
PB(8, 5, " )*( ", "flame")         # phoenix torch
PB(9, 5, " (%) ", "flame")
PB(10, 5, " `|´ ", "obj")
PB(11, 6, " | ", "obj")
PB(13, 4, " ,--, ", "gold")        # disk of Mercury, 8-fold star
PB(14, 3, " (;;;) ", "gold")
P(14, 6, "*", "sun")
PB(15, 4, " `--´ ", "gold")
PB(17, 2, " O===O ", "obj")        # wand of double power
PB(18, 5, " ` ", "obj")
# RIGHT ring, top to bottom: scroll / winged egg / cup / dagger
PB(4, 37, " ,----, ", "obj")       # papyrus scroll
PB(5, 36, " O_‾‾‾_O ", "obj")
PB(7, 33, "  (o)  ", "egg")        # winged orphic egg
P(7, 33, "<~", "wings")
P(7, 38, "~>", "wings")
PB(10, 37, " c`--´o ", "obj")      # two-handled Grecian cup
PB(11, 38, " \\;;/ ", "obj")
PB(12, 39, " _¡_ ", "obj")
PB(14, 40, " ` ", "obj")           # dagger, flung outward
PB(15, 36, " o+===> ", "obj")

# ---------------------------------------------------------- the figure
# raised hand (viewer-left) + arm, two cells thick
PB(3, 14, " \\¡/ ", "figure")
PB(4, 15, " \\;, ", "figure")
PB(5, 17, " `;, ", "figure")
# topknot, face + winged helmet
PB(4, 21, " ,;, ", "figure")
PB(5, 20, " (´v`) ", "figure")
P(5, 19, "~", "wings")
P(5, 27, "~", "wings")
# shoulders + torso (dithered gold, contiguous mass)
PB(6, 19, " ,(;;;), ", "figure")
PB(7, 19, " (;;;;;) ", "figure")
PB(8, 20, " );;;( ", "figure")
PB(9, 20, " (;;;) ", "figure")
PB(10, 19, " (;;;;;) ", "figure")
# down arm (viewer-right); P, not PB, so the shoulder edge survives
P(7, 27, "`=;", "figure")
P(8, 30, "`;o", "figure")
# legs: left straight on the rod, right bent out (swastika thrust)
PB(11, 20, " (;| ", "figure")
PB(12, 20, " ;;| ", "figure")
PB(13, 20, " ;;| ", "figure")
PB(14, 20, " ;;| ", "figure")
PB(15, 20, " `;| ", "figure")
PB(11, 25, " `=;,_ ", "figure")
PB(12, 28, " ;) ", "figure")
PB(13, 27, " ;/ ", "figure")
PB(14, 26, " ;/ ", "figure")
PB(15, 25, " ;/ ", "figure")
# foot-wings (the Mercury arrowhead), bound ankles, toe on the rod
PMB(16, 15, " _,~ ", "wings")
PMB(17, 13, " <=e=´ ", "wings")
PB(16, 20, " `,x,´ ", "figure")
PB(17, 21, " ,V, ", "figure")

# ------------------------------------- sunburst behind the left foot-wing
P(15, 11, "·", "sun")
P(16, 10, "*", "sun")
P(16, 12, "·", "sun")
P(17, 11, "*", "sun")

# ------------------------------------------------------- Ape of Thoth
PB(21, 40, " ,o ", "ape")          # raised fist, groping up
PB(22, 39, " /´ ", "ape")
PB(23, 37, " (o´) ", "ape")        # head tilted up at the Magus
PB(24, 36, " ,(;;)´ ", "ape")
PB(25, 36, " (;;;( ", "ape")
PB(26, 36, " ´L`L ", "ape")
PB(27, 38, " `c_,´ ", "ape")

# ---------------------------------------------------------------- sig
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "01-magus-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "01-magus-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
