#!/usr/bin/env python3
"""Emperor v3c — ultracode panel candidate C: FLAME-FIELD DOMINANT.

Scarlet fire fills the whole card edge to edge (Mars in Aries; Sulphur the
fiery element) — a procedural striated flame field with angular spike
tongues — and a single diagonal shaft of WHITE LIGHT descends from the
upper right to the raised ram-headed sceptre. The crowned Emperor reads as
the ORDERED NEGATIVE SPACE within the blaze: a halo-punched Sulphur-glyph
body (brocade triangle of head+arms over the cross of the legs), frontal
on the axis (col 23), gold sun disk cleared out of the fire behind his
head. Ram throne heads flank him, 16-point star disks on the throne arms,
red-eagle shield with crimson disk lower left, the white Lamb and Flag
couchant lower right, dark-red floor with fleur-de-lys.

Emits drafts/04-emperor-v3c-art-lg.txt + drafts/04-emperor-v3c-lg-classes.json
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


def CLEAR(r, c):
    if 0 <= r < H and 0 <= c < W:
        canvas[r][c] = " "
        classes[r][c] = None


# ------------------------------------------------- 1. the scarlet flame field
# Full bleed, dense, diagonally striated so it reads as angular fire;
# brighter toward the top (the sun-lit blaze), deeper red below.
FLOOR_TOP = 28
for r in range(FLOOR_TOP):
    for c in range(W):
        h = (r * 53 + c * 17 + (r * c) % 11) % 100
        if h >= 96:
            continue                       # tiny breathing gaps, no black holes
        s = (2 * r + c) % 7                # down-left diagonal striation
        ch = ";" if s < 3 else (":" if s < 5 else ("'" if s == 5 else "·"))
        bright = (r * 7 + c * 3) % 11 < (5 if r < 9 else 3)
        P(r, c, ch, "flames" if bright else "field")

# angular flame spikes riding the field (the Harris spike-thicket)
def spike(rtop, c, h):
    P(rtop, c, "^", "flames")
    for i in range(1, h):
        off = (i + 1) // 2
        P(rtop + i, c - off, "/", "flames")
        P(rtop + i, c + off, "\\", "flames")

for rt, c, h in [(7, 3, 4), (15, 6, 4), (19, 16, 5), (23, 13, 4),
                 (10, 44, 3), (15, 38, 4), (19, 30, 5), (24, 42, 3),
                 (10, 10, 3), (11, 36, 3), (25, 5, 3), (26, 35, 2),
                 (25, 18, 3), (25, 28, 3), (26, 8, 2), (26, 40, 2)]:
    spike(rt, c, h)

# ------------------------------------------------- 2. gold sun disk (Sol
# exalted in Aries) cleared out of the fire behind the head — the head sits
# in the dark calm core, ringed by gold dither.
for r in range(0, 9):
    for c in range(11, 36):
        dx = (c - 23) / 11.0
        dy = (r - 3.0) / 4.0
        d = dx * dx + dy * dy
        if d < 1.0:
            CLEAR(r, c)
            if d >= 0.12:
                h = (r * 31 + c * 13) % 100
                if h < 6:
                    P(r, c, "*", "sunrays")
                else:
                    P(r, c, ";" if h < 70 else ":", "sunrays")

# ------------------------------------------------- 3. white light shaft (UR)
# Parallel beams from the top-right corner down toward the sceptre head,
# dark margin punched along both edges so the shaft pops from the fire.
for r in range(6):
    ci = int(round(43 - 2.4 * r))
    for dc in range(-4, 5):
        c = ci + dc
        if not (0 <= c < W):
            continue
        if abs(dc) == 4:
            CLEAR(r, c)
        elif abs(dc) == 3:
            P(r, c, "'", "light")
        else:
            P(r, c, "\\", "light")
P(6, 30, "·", "light")
P(7, 29, "·", "light")

# ------------------------------------------------- 4. the ram throne heads
# Himalayan wild rams, great curled horns, flanking the crown.
PB(1, 0, " __,,--,,  ", "ram")
PB(2, 0, ",((@))  `,_ ", "ram")
PB(3, 0, " ((,´, `, ;) ", "ram")
PB(4, 1, " `´`--´´ ", "ram")
PB(5, 36, " ,,--,,__ ", "ram")
PB(6, 35, " _,´  ((@)),", "ram")
PB(7, 34, " (; ,´ `,,)) ", "ram")
PB(8, 36, " ``--´`´ ", "ram")

# ------------------------------------------------- 5. star disks (throne arms)
PMB(12, 2, " `,-¡-,´ ", "star")
PMB(13, 1, " =((*))= ", "star")
PMB(14, 2, " ,´-¡-`, ", "star")

# ------------------------------------------------- 6. crown + head (axis 23)
# Four-point gold crown; the gaze tips to his left (our left) — the eye 'o'
# rides left of the axis — but the mass stays centered.
PB(0, 18, "  ¡v¡v¡v¡  ", "crown")
PB(1, 17, "  [=======]  ", "crown")
PB(2, 18, "  (´o··`)  ", "face")
PB(3, 19, "  `,v,´  ", "face")

# ------------------------------------------------- 7. the robe (the triangle)
# Ordered brocade — the calm negative space inside the blaze. Regular
# striation + a strict grid of gold pattern marks (bees, loops, fleurs).
SPANS = {4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 9,
         11: 10, 12: 10, 13: 11, 14: 12, 15: 12}
for r, hw in SPANS.items():
    inner = "".join(";" if (2 * r + k) % 3 else ":" for k in range(2 * hw - 1))
    PB(r, 23 - hw - 2, "  (" + inner + ")  ", "robe")
# brocade grid: bees e, loops &, fleurs ¡ — every 4th col on odd rows
for r, hw in SPANS.items():
    if r % 2 == 0 or hw < 4:
        continue
    for dc in range(-(hw - 2), hw - 1):
        if (dc + 40) % 4 == 2:
            P(r, 23 + dc, "&e¡"[(r + dc) % 3], "pattern")
# looping arrow-lines of directed energy
P(10, 16, "~>", "pattern")
P(10, 28, "<~", "pattern")

# ------------------------------------------------- 8. sceptre into the light
# Gold diagonal from the chest-held hand up past the crown, spiral
# ram-horn head raised at the foot of the white shaft.
PB(1, 30, "  ,--,  ", "sceptre")
PB(2, 30, "  ((@)  ", "sceptre")
for r, c in ((3, 31), (4, 30), (5, 29), (6, 28), (7, 27)):
    P(r, c, "//", "sceptre")
P(8, 26, "(,,", "skin")

# ------------------------------------------------- 9. orb + Maltese cross
# At the navel, on the axis: government established.
P(11, 22, "\\¡/", "cross")
PB(12, 19, "  ((@))  ", "orb")
P(13, 20, "`,", "skin")
P(13, 24, ",´", "skin")

# ------------------------------------------------ 10. crossed legs (the cross)
# Vertical calf on the axis, horizontal shin crossing at its top — the +
# beneath the triangle. Knee left, toes pointing right, bare foot at floor.
for r in range(16, 24):
    PB(r, 19, "  (;;;)  ", "skin")
PB(24, 18, "  ,;;;;;,  ", "skin")
PB(25, 17, "  (__,,,__)  ", "skin")
PB(15, 9, "  ,--,  ", "skin")
PB(16, 8, "  (;;;;;;;;;;;;;;;;;;;;;)  ", "skin")
PB(17, 11, "  `--;;;;;;;;;;;;;,==>  ", "skin")

# ------------------------------------------------ 11. shield (lower left)
PB(19, 1, " ,=========, ", "shield")
PB(20, 1, " |  ,(@),  | ", "shield")
P(20, 5, ",(@),", "orb")
PB(21, 1, " | \\¡/^\\¡/ | ", "eagle")
PB(22, 1, " | >(:¡:)< | ", "eagle")
PB(23, 1, " `, \\,¡,/ ,´ ", "eagle")
PB(24, 2, "  \\ ´|` /  ", "shield")
PB(25, 3, "   `-,-´   ", "shield")

# ------------------------------------------------ 12. Lamb and Flag (lower R)
PB(21, 40, " ,¡ ", "lamb")
PB(22, 36, " ,--,´|> ", "lamb")
PB(23, 34, " ,(´o )=,´ ", "lamb")
PB(24, 34, " (,,(___), ", "lamb")
PB(25, 35, "  ´´  ´´ ", "lamb")

# ------------------------------------------------ 13. floor + fleur-de-lys
for r in range(FLOOR_TOP, H):
    for c in range(W):
        h = (r * 41 + c * 29) % 100
        if r == FLOOR_TOP:
            ch = "=" if (c * 3 + r) % 7 else ";"
        else:
            if h >= 88:
                continue
            ch = ";" if h % 3 == 0 else ("-" if h % 3 == 1 else "·")
        canvas[r][c] = ch
        classes[r][c] = "floor"
P(29, 5, ",¡,", "fleur")
P(30, 12, ",¡,", "fleur")
P(29, 37, ",¡,", "fleur")
P(30, 30, "´v`", "fleur")          # the faint Aries-horn garnish
P(30, 2, "aw", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "04-emperor-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "04-emperor-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
