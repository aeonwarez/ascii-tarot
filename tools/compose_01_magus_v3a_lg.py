#!/usr/bin/env python3
"""Magus v3a — composer A: MERCURY-GLYPH FIGURE DOMINANT.

The swastika-motion body is the hero, drawn LARGE (rows 2-20): serpent-horns
above the head, wide stylized foot-wings below sweeping to both borders (the
arrowhead of the Mercury glyph), raised viewer-left arm / bent viewer-right
arm, straight left leg / bent right knee — nothing at rest. The eight juggled
objects orbit TIGHT around him, 4 left / 4 right. Kether white V behind the
torso narrowing to the feet; Binah indigo wedge widening below, caduceus rod
down col 23; teal ray-fan field kept QUIET so the gold figure owns the card;
Ape of Thoth groping up the right wing.

Emits:
  drafts/01-magus-v3a-art-lg.txt       47x32 art, full-bleed
  drafts/01-magus-v3a-lg-classes.json  per-cell color classes (art coords)
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


# ------------------------------------------------------------- kether V
# White wedge behind head/torso, widest at the top, apex at the feet.
def v_half(r):
    if not (2 <= r <= 18):
        return None
    return 0.5 + 14.0 * (18 - r) / 16.0


def in_v(r, c):
    h = v_half(r)
    return h is not None and abs(c - AXIS) <= h


# ------------------------------------------------------------- ray field
# QUIET teal fan from above top-center; indigo takes over toward the bottom.
FAN_R, FAN_C = -4.0, 23.0
for r in range(H):
    for c in range(W):
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if in_v(r, c):
            hw = v_half(r)
            t = abs(c - AXIS) / hw if hw > 0.01 else 0
            if t < 0.85:
                if h % 17 == 0:
                    P(r, c, "*", "kether")
                elif h % 13 == 0:
                    P(r, c, "#", "kether")
                else:
                    P(r, c, "\":\"'\":"[h % 6], "kether")
            else:
                P(r, c, ";:;:"[h % 4], "lilac")
            continue
        dx = c - FAN_C
        dy = 2.0 * (r - FAN_R)
        th = math.atan2(dx, dy)
        band = int((th + math.pi) * 10.0 / math.pi)
        ind = max(0, (r - 15) * 10) + (abs(c - 23) * max(0, r - 19)) // 4
        if h < ind:
            if r >= 23 and h % 7 == 0:
                P(r, c, "·", "lilac")
            else:
                P(r, c, ";:;,"[h % 4], "indigo")
            continue
        cov = 64 - r
        if band % 2 == 0:
            cov += 8
        if h < cov:
            cls = "rays" if band % 2 == 0 else "field"
            P(r, c, ";:·'"[h % 4], cls)

# a few crisp fan rays give the Harris burst without global noise
def line(r0, c0, r1, c1, cls, ch=None, skip=("kether", "lilac")):
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        rr, cc = int(round(r)), int(round(c))
        if not (0 <= rr < H and 0 <= cc < W):
            continue
        if classes[rr][cc] in skip or (skip and in_v(rr, cc)):
            continue
        if ch:
            g = ch
        else:
            dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99
            g = "|" if abs(dc) < 0.35 else ("\\" if dc > 0 else "/")
        P(rr, cc, g, cls)


for tr, tc in ((2, 0), (6, 0), (11, 0), (16, 0),
               (2, 46), (6, 46), (11, 46), (16, 46)):
    line(0, 23, tr, tc, "rays")

# faint crossing form-lines in the mid field (never inside the V)
line(6, 1, 21, 14, "web")
line(6, 45, 21, 32, "web")
line(15, 0, 10, 46, "web")
for c in range(1, 46, 4):
    if classes[13][c] in (None, "field", "rays", "indigo"):
        P(13, c, "-", "web")

# pale-gold rays fanning up from the bottom point (Binah birthing light)
for tr, tc in ((20, 2), (26, 0), (20, 44), (26, 46)):
    line(31, 23, tr, tc, "obj")

# ------------------------------------------------------------- binah wedge
for r in range(20, H):
    hw = 0.7 * (r - 20) + 0.4
    for c in range(W):
        if abs(c - AXIS) <= hw:
            h = (r * 31 + c * 17) % 100
            P(r, c, ";%;&;%"[h % 6] if h < 96 else "&", "indigo")
# faint arc at the very bottom, birthing form out of the dark
PB(30, 18, " _,-‾-,_ ", "lilac")

# ------------------------------------------------------------- caduceus rod
for r in range(19, H):
    P(r, 23, "|", "caduceus")
P(31, 22, "=", "caduceus")
P(31, 24, "=", "caduceus")

# ------------------------------------------------------------- winged disk
# caduceus head: wings span the full top; oval disk with the descending dove
PMB(0, 0, "<^=,_´=~=,_‾=,", "wings")
PMB(1, 2, " ‾´‾`=,_ ", "wings")
PB(0, 18, ",==(\\v/)==,", "gold")
P(0, 22, "\\v/", "dove")
PB(1, 19, "`==,·,==´", "gold")
P(1, 23, "·", "dove")

# ------------------------------------------------------------- serpents
# twined horns above his head; left head Isis-throne, right head crown
PM(2, 19, ",sS(", "serpent")
PM(3, 15, ",sS´", "serpent")
PB(4, 9, " ¡e( ", "serpent")
PB(4, 33, " )e^ ", "serpent")

# ------------------------------------------------------------- foot wings
# the wide Mercury-glyph arrowhead: swept dithered masses to both borders
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

# faint sunburst behind the left foot-wing (Mercury heralds the Sun)
P(14, 3, "*", "gold")
P(13, 1, "·", "gold")
P(14, 6, "·", "gold")
P(15, 2, "·", "gold")

# ------------------------------------------------------------- the figure
# raised viewer-left hand first (arm crosses under the serpent)
PB(2, 9, " \\¡/ ", "gold")
PB(3, 11, " ;´ ", "figure")
PB(4, 14, " ,=´ ", "figure")
PB(5, 17, " ,´ ", "figure")
# head: gold face on col 23, punched clear of the serpents
PB(3, 20, " ,‾, ", "gold")
PB(4, 20, " ,´‾`, ", "gold")
PB(5, 20, " (´·`) ", "gold")
# torso, dithered gold, lit by the V behind (bright rims)
PB(6, 18, " (;';;';;) ", "figure")
PB(7, 18, " (;;;;;;;) ", "figure")
PB(8, 19, " (;;;;;) ", "figure")
PB(9, 19, " (;;;;;) ", "figure")
PB(10, 20, " );;;( ", "figure")
PB(11, 19, " (;;;;;) ", "figure")
# bent viewer-right arm, elbow out, hand holding the threads at the hip
PB(7, 27, " `=, ", "figure")
PB(8, 28, " ;) ", "figure")
PB(9, 27, " ,;/ ", "figure")
PB(10, 26, " o== ", "gold")
# hips split into the two legs — swastika thrust
PB(12, 18, " (;;;;;;;) ", "figure")
PB(12, 27, "=,_ ", "figure")
PB(13, 19, " |;;) ", "figure")
PB(13, 26, " ;;=,_ ", "figure")
PB(14, 19, " |;;| ", "figure")
PB(14, 29, " (;;) ", "figure")
PB(15, 19, " (;;| ", "figure")
PB(15, 28, " ,;;/ ", "figure")
PB(16, 20, " ;;| ", "figure")
PB(16, 26, " ;;/ ", "figure")
PB(17, 20, " ;;| ", "figure")
PB(17, 25, " ;/ ", "figure")
PB(18, 20, " ;; ", "figure")
PB(18, 23, ";, ", "figure")
# feet together on the rod, chained; winged heels; serpent strap
PB(19, 19, " \\;,;/ ", "gold")
P(19, 18, "<", "wings")
P(19, 26, ">", "wings")
P(18, 25, "s", "serpent")
P(20, 23, "x", "gold")

# ------------------------------------------------------------- 8 objects
# LEFT: stylus, wand of double power, phoenix-wand torch, star disk
PB(2, 4, " ~==´ ", "obj")
PB(5, 2, " o===o ", "obj")
PB(7, 4, " ,&, ", "flame")
PB(8, 4, " (%) ", "flame")
PB(9, 5, " ¡ ", "obj")
PB(10, 4, " ·-· ", "sun")
PB(11, 3, " ,(*), ", "sun")
PB(12, 4, " `·´ ", "sun")
# RIGHT: scroll, winged egg, two-handled cup, dagger
PB(2, 36, " ,==, ", "obj")
PB(3, 36, " (@)/ ", "obj")
PB(7, 30, " <(o)> ", "egg")
P(7, 31, "<", "wings")
P(7, 35, ">", "wings")
PB(9, 36, " c(_)o ", "obj")
PB(10, 37, " `-´ ", "obj")
PB(12, 37, " <==+ ", "obj")

# ------------------------------------------------------------- ape of thoth
PB(20, 41, " ,¡ ", "ape")
PB(21, 40, " ,\\( ", "ape")
PB(22, 40, " (e´) ", "ape")
PB(23, 40, " /;;,) ", "ape")
PB(24, 39, " (;;;/ ", "ape")
PB(25, 39, " /,/\\, ", "ape")
PB(26, 40, " ´  `~ ", "ape")

# ------------------------------------------------------------- signature
P(31, 2, "aw", "sig")

# ------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "01-magus-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "01-magus-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
