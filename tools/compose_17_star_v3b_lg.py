#!/usr/bin/env python3
"""Star v3b — FIGURE-DOMINANT candidate (ultracode panel, composer B).

The kneeling, whirling Nuith is the hero: nude, seen from BEHIND, one arm
arched overhead to the golden cup, torso an S-curve of flowing diagonal
strokes, a silver sash/hair ribbon whirling down her right side and
curling at the shore. The rose celestial globe is a big dithered backdrop
mass centered on the axis behind her. Everything in the frame spirals
(sky bands, sash, cascade, star-ray curls) EXCEPT the lower silver cup's
dead-straight rectilinear stream, painted last so nothing breaks it.

Emits:
  drafts/17-star-v3b-art-lg.txt        47x32 art, full-bleed
  drafts/17-star-v3b-lg-classes.json   per-cell color classes (art coords)
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


# ------------------------------------------------- 1. whirling sky field
# Spiral arc bands radiating from behind the figure (cell aspect baked
# in): the cosmos in motion, never dead black. Globe overwrites its
# ellipse afterwards; shore rows overwrite the bottom.
for r in range(0, 24):
    for c in range(W):
        dx = c - 23.0
        dy = 2.0 * (r - 12.0)
        d = math.hypot(dx, dy)
        th = math.atan2(dy, dx)
        ph = (d - 5.5 * th / (2 * math.pi)) % 5.0
        h = (r * 53 + c * 31 + (r * c) % 7) % 100
        if ph < 0.9:                       # band core: the cloud sweep
            if h < 92:
                P(r, c, ",´'·,´"[h % 6], "sky")
        elif ph < 2.2:                     # band shoulder
            if h < 76:
                P(r, c, "·''·"[h % 4], "sky")
        elif h < 55:                       # between sweeps: starry haze
            P(r, c, "·.··"[h % 4], "sky")

# ------------------------------------------------- 2. the rose globe
# Backdrop mass: big dithered sphere centered on the axis, lit upper-left
# (toward the great star), limb-darkened lower-right. No outline hoop.
CX, CY, A, B = 23.0, 13.0, 17.5, 9.2
LR, LC = 7.5, 15.0
for r in range(H):
    for c in range(W):
        dx, dy = (c - CX) / A, (r - CY) / B
        rr = dx * dx + dy * dy
        if rr > 1.0:
            continue
        canvas[r][c] = " "
        classes[r][c] = None
        d = math.hypot((c - LC) / A, (r - LR) / B)
        s = 0.50 * d + 0.62 * rr
        t = ((r * 5 + c * 3) % 11) / 11.0
        if rr > 0.85:
            ch = (":" if t < 0.45 else ";") if s < 0.62 else \
                 (";" if t < 0.80 else ":")
        elif s < 0.30:
            ch = ":" if t < 0.50 else ("·" if t < 0.85 else "'")
        elif s < 0.55:
            ch = ":" if t < 0.70 else "·"
        elif s < 0.80:
            ch = ":" if t < 0.55 else (";" if t < 0.85 else ".")
        elif s < 1.02:
            ch = ";" if t < 0.60 else ":"
        else:
            ch = ";" if t < 0.80 else ":"
        P(r, c, ch, "globe")

# star-dust speckles on the sphere (Harris dusts the rose with white)
for r, c in [(7, 32), (8, 35), (10, 33), (11, 37), (13, 33), (14, 36),
             (16, 30), (17, 33), (9, 17), (13, 15), (18, 20)]:
    P(r, c, "'", "babalon")

# ------------------------------------------------- 3. sea / horizon
for r in range(24, H):
    for c in range(0, 13):
        k = (c + r * 3) % 4
        ch = "~" if k == 0 else ("·" if k == 1 else ("-" if k == 2 else " "))
        if ch != " ":
            P(r, c, ch, "water")

# Pyramid City across the sea, on the horizon
PB(22, 1, " ,^, ", "pyramid")
PB(23, 0, " /:·\\/\\, ", "pyramid")

# ------------------------------------------------- 4. crystalline shore
# Facet-shaded seven-sided solids: light plane (·) left, dark plane (;)
# right, diamond lattice, slashes only (nothing vertical but THE stream).
row24 = ("_,/\\.__,/\\,_" * 4)[:34]
row25 = ("/··;;\\" * 7)[:34]
row26 = ("\\·::;/" * 7)[:34]
row27 = ("/·;;\\·" * 7)[:34]
row28 = ("\\·;/" * 9)[:34]
P(24, 13, row24, "crystal")
P(25, 13, row25, "crystal")
P(26, 13, row26, "crystal")
P(27, 13, row27, "crystal")
P(28, 13, row28, "crystal")
for c in range(13, 47):
    k = (c * 7) % 5
    P(29, c, ":;·;:"[k], "earth")
    P(30, c, "·:;:·"[(k + 2) % 5], "earth")
    P(31, c, ":·;·:"[(k + 4) % 5], "earth")

# ------------------------------------------------- 5. the great star
# Seven rays (up, UL, UR, L, R, DL, DR — none straight down), tips
# curled counterclockwise. The A.'.A.'. sigil in its cloud spiral.
PB(0, 3, " ,   \\ ' / ", "star")
PB(1, 2, " `.  \\|/  ,´ ", "star")
PB(2, 0, "·--=((o))=--· ", "star")
PB(3, 2, " ,´  / \\  `. ", "star")
PB(4, 1, " ´   /   \\ ", "star")
PB(5, 4, " ,     `, ", "star")
# cloud spiral hugging it
P(6, 1, "`-.,_", "sky")
P(7, 5, "`-,", "sky")

# ------------------------------------------------- 6. star ON the globe
PB(9, 8, "  \\¡/  ", "babalon")
PB(10, 6, " ·-((o))-· ", "babalon")
PB(11, 8, " ,/ \\, ", "babalon")
P(8, 13, "´", "babalon")
P(12, 6, "`,", "babalon")
# whirl streaks on the globe face around it
P(12, 12, "_,-´", "globe")
P(8, 7, "`-,", "globe")

# ------------------------------------------------- 7. NUITH, from behind
# hair whirling up-left into the clouds (clear of the great star's rays)
PB(3, 14, " _,--~ ", "silver")
PB(4, 16, " ,-;;´ ", "silver")
P(2, 16, "_,-", "sky")
# crown + head (back of head: hair mass) + nape
PB(4, 22, " ,cCc, ", "silver")
PB(5, 22, " c;;;c ", "silver")
PB(6, 22, " `);´ ", "silver")
# torso: S-curve of flowing diagonal strokes, halo-punched over globe
PB(7, 20, " (;;´;;;) ", "nuith")
PB(8, 20, " (;´;;;) ", "nuith")
PB(9, 19, " (;´;;;) ", "nuith")
PB(10, 19, " );;;;( ", "nuith")
PB(11, 19, " (;;´;;) ", "nuith")
PB(12, 19, " (;;;´;;) ", "nuith")
PB(13, 19, " (;;;;´;;;) ", "nuith")
PB(14, 18, " (;;;;;´;;;) ", "nuith")
PB(15, 18, " (;;;;;;´;;) ", "nuith")
PB(16, 17, " (;;;;;;;;) ", "nuith")
PB(17, 16, " (;;;;;´;;) ", "nuith")
PB(18, 15, " (;;;;´;;) ", "nuith")
PB(19, 14, " (;;;;´;) ", "nuith")
# knee down on the shore, shin sweeping back right, foot tucked
PB(20, 13, " (;;;;) ", "nuith")
PB(21, 13, " (;;;,_ ", "nuith")
PB(22, 14, " `;;;;;;,__ ", "nuith")
PB(23, 16, " `--;;;;--´ ", "nuith")
# raised arm arching from right shoulder over to the golden cup
PB(6, 27, " ,´ ", "nuith")
PB(5, 29, " / ", "nuith")
PB(4, 30, " / ", "nuith")
PB(3, 31, " ,-´ ", "nuith")
# lowered arm reaching down-left to the silver cup
PB(12, 17, " ( ", "nuith")
PB(13, 16, " ( ", "nuith")
PB(14, 15, " ( ", "nuith")
PB(15, 13, " ,´ ", "nuith")
PB(16, 11, " ,´ ", "nuith")
P(17, 13, "(", "nuith")

# ------------------------------------------------- 8. the whirling sash
# silver ribbon over her right side, flaring and curling at the shore —
# the "whirling swastika of motion"
RIBBON = [(8, 29), (9, 29), (10, 28), (11, 28), (12, 29), (13, 30),
          (14, 31), (15, 32), (16, 33), (17, 34), (18, 35), (19, 35),
          (20, 34)]
for r, outer in RIBBON:
    if outer <= 29:
        P(r, outer - 2, ";;)", "silver")   # hugging the body: no seam
    else:
        P(r, outer - 3, "(;;)", "silver")  # flared free ribbon: both edges
P(7, 29, "),", "silver")
P(21, 30, "`;;;,´", "silver")
P(22, 29, "`;;;,", "silver")
P(23, 31, "`-;,)", "silver")

# ------------------------------------------------- 9. golden cup, raised
PB(0, 28, " _,--,_ ", "gold")
PB(1, 27, " (o_____) ", "gold")
PB(2, 28, " `-,--´ ", "gold")
# curved cascade of star-milk onto her own crown
P(2, 26, "((", "gold")
P(3, 25, "((", "gold")
P(2, 24, "'", "gold")
P(3, 22, "'", "gold")
# star-seed tumbling clockwise out of the cup
P(1, 38, "x", "babalon")
P(2, 39, ",", "babalon")

# ------------------------------------------------- 10. silver cup + THE
# one rigid rectilinear stream, painted last: nothing breaks it
PB(17, 8, " .--. ", "silver")
PB(18, 7, " ( ~~ ) ", "silver")
PB(19, 8, " `)(´ ", "silver")
PB(20, 9, " |¡| ", "silver")
for r in range(21, 28):
    PB(r, 8, " | | ", "silver")
P(28, 9, "¡·¡", "silver")

# ------------------------------------------------- 11. witnesses
PB(15, 41, " }v{ ", "fly")
PB(20, 40, " }v{ ", "fly")
PB(23, 36, " }v{ ", "fly")
PB(25, 41, " ,o, ", "rose")
PB(27, 42, " ,o, ", "rose")
PB(26, 37, " ,o, ", "rose")
# small whorl galaxies (the painting's spiral eddies)
P(18, 3, "@", "sky")
P(15, 43, "@", "sky")
# sweep arcs framing the edges so no column reads dead black
P(4, 42, "`-,", "sky")
P(6, 44, "`,", "sky")
P(10, 44, "(", "sky")
P(12, 45, ")", "sky")
P(18, 44, "(", "sky")
P(10, 1, "(", "sky")
P(14, 0, ")", "sky")
P(17, 1, "`,", "sky")
# scattered stars
P(0, 20, "+", "star")
P(6, 15, "·", "star")
P(3, 43, "·", "star")
P(8, 44, ".", "star")
P(16, 2, "·", "star")
P(23, 42, "·", "star")

# ------------------------------------------------- 12. signature
PB(31, 1, " aw ", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert len(canvas) == H and all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "17-star-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "17-star-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
