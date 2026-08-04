#!/usr/bin/env python3
"""Compositor for Atu VIII Adjustment — panel candidate v3c (balance dominant).

Equilibrium made visible is the hero: the great scales hanging by long chains
from the crown of Maat — glass-bubble pans with alpha (left) and omega (right)
— plus the balanced corner spheres of light and dark (colors swapped across
the axis) and the feathered ray curtain. The masked figure is the still
fulcrum, poised on the point of her own sword upon the bottom dome.
PERFECT SYMMETRY: left/right via PM/PMB about AXIS=23; top/bottom via
crown<->dome, top spheres<->bottom spheres, pylons up<->spikes down.

Vertical layout follows the scan: crown 0-2, ribbed column 3-4, drop 5,
mask 6, face 7, shoulders 8, pommel 9, hands 10, guard 11, pans 13-18,
shelf 17, spikes 19-25, toe 27, point 28, dome 28-31.

Emits drafts/08-adjustment-v3c-art-lg.txt + drafts/08-adjustment-v3c-lg-classes.json
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


def PMswap(r, c, s, cls_l, cls_r):
    """Mirror pair with swapped classes (light<->dark across the axis)."""
    P(r, c, s, cls_l)
    ms = s.translate(MIRROR)[::-1]
    P(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls_r)


def PMBswap(r, c, s, cls_l, cls_r):
    PB(r, c, s, cls_l)
    ms = s.translate(MIRROR)[::-1]
    PB(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls_r)


def line_over(r0, c0, r1, c1, cls, ch=None, skip=0):
    """Straight ray, slope-appropriate glyphs, overwrites (fg over bg)."""
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(skip, steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        rr, cc = int(round(r)), int(round(c))
        if not (0 <= rr < H and 0 <= cc < W):
            continue
        if ch:
            g = ch
        elif r1 == r0:
            g = "~"
        else:
            ratio = (c1 - c0) / (r1 - r0)
            if abs(ratio) > 2.6:
                g = "~"
            elif abs(ratio) < 0.35:
                g = "|"
            else:
                g = "\\" if ratio > 0 else "/"
        P(rr, cc, g, cls)


# ---- 1. ground: pale chartreuse field + fine blue harlequin lattice ----
# Mirror-exact: everything keyed on adx = |c - 23|. Dense — no black gaps.
for r in range(H):
    for c in range(W):
        adx = abs(c - 23)
        v1 = (adx + 2 * r) % 6 == 0
        v2 = (adx - 2 * r) % 6 == 0
        if v1 or v2:
            if v1 and v2:
                P(r, c, "x", "lattice")
            elif v1:
                P(r, c, "\\" if c < 23 else "/", "lattice")
            else:
                P(r, c, "/" if c < 23 else "\\", "lattice")
            continue
        h = (adx * 7 + r * 13) % 100
        if h < 90:
            P(r, c, ";':·;,':"[h % 8], "ground")

# ---- 2. harlequin diamonds: dark canopy across the top + edge columns ---
PM(0, 8, "<>", "harle")
PM(0, 11, "<>", "harle")
PM(0, 14, "<>", "harle")
PM(0, 17, "<>", "harle")
PM(1, 14, "<:>", "harle")
PM(2, 13, "<>", "harle")
PM(2, 16, "<>", "harle")
PM(3, 17, "<>", "harle")
PM(16, 1, "<>", "harle")
PM(20, 2, "<>", "harle")
PM(24, 1, "<>", "harle")

# ---- 3. feathered curtain of rays, far edges, faint + symmetric ----
for r in range(5, 26):
    PM(r, 0, "'|·"[r % 3], "rays")
    if r % 2 == 0:
        PM(r, 2, "(", "rays")
    else:
        PM(r, 1, "·", "rays")

# ---- 4. the concealed vesica: pan bottoms -> toe point (upper = chains) --
line_over(19, 2, 28, 20, "rays", ch="\\")
line_over(19, 44, 28, 26, "rays", ch="/")
line_over(18, 4, 27, 21, "rays", ch="\\")
line_over(18, 42, 27, 25, "rays", ch="/")
line_over(18, 12, 27, 22, "rays", ch="\\")
line_over(18, 34, 27, 24, "rays", ch="/")

# ---- 5. the throne: upper pylons, dark shelf, inverted spikes ----
PMB(4, 15, " /\\ ", "spike")
PMB(5, 14, " /%%\\ ", "spike")
PMB(6, 14, " |%%| ", "spike")
PMB(7, 14, " |%%| ", "spike")
PMB(8, 14, " (%%) ", "spike")
P(17, 15, "=" * 17, "spike")            # shelf behind her hips
PMB(19, 6, " (%%%) ", "spike")          # inverted spikes under the pans
PMB(20, 6, " |%%%| ", "spike")
PMB(21, 7, " (%) ", "spike")
PMB(22, 7, " |%| ", "spike")
PMB(23, 8, " | ", "spike")
PMB(24, 8, " | ", "spike")
PMB(25, 8, " ¡ ", "spike")

# ---- 6. corner spheres of light and darkness (swapped across the axis) --
# top corner masses (deep blue, both sides)
PMB(0, 0, "&&&&%;: ", "sphb")
PMB(1, 0, "&&&%;: ", "sphb")
PMB(2, 0, "&&%;· ", "sphb")
PMB(3, 0, "&%;· ", "sphb")
PMB(4, 0, "%;· ", "sphb")
# top sphere pair: blue left <-> green right
PMBswap(1, 7, " ,%%', ", "sphb", "sphg")
PMBswap(2, 6, " (%%%;·) ", "sphb", "sphg")
PMBswap(3, 7, " `%;·´ ", "sphb", "sphg")
# small second pair: green left <-> blue right
PMBswap(4, 11, " ,%%, ", "sphg", "sphb")
PMBswap(5, 11, " `;·´ ", "sphg", "sphb")
# bottom sphere pair: green left <-> blue right (top/bottom counterchange)
PMBswap(26, 4, " ,%%', ", "sphg", "sphb")
PMBswap(27, 3, " (%%%;·) ", "sphg", "sphb")
PMBswap(28, 4, " `%;·´ ", "sphg", "sphb")
# small lower pair: blue left <-> green right
PMBswap(28, 11, " ,%%, ", "sphb", "sphg")
PMBswap(29, 11, " `;·´ ", "sphb", "sphg")
# bottom corner masses (deep blue, both sides)
PMB(29, 0, "%%;: ", "sphb")
PMB(30, 0, "&%%;: ", "sphb")
PMB(31, 0, "&&%%;: ", "sphb")

# ---- 7. wings: solid blue fans from her shoulders, radial pleats ----
WING = {8: (16, 19), 9: (14, 19), 10: (12, 19), 11: (11, 17), 12: (11, 18),
        13: (12, 18), 14: (13, 17), 15: (15, 17)}
for r, (c0, c1) in WING.items():
    for c in range(c0, c1 + 1):
        if (r * 5 + c * 3) % 17 == 0:
            continue                     # diaphanous pinholes
        dr = r - 7.5
        dc = (21.0 - c) / 2.0
        ratio = dc / dr
        g = "|" if ratio < 0.4 else ("/" if ratio < 1.3 else "~")
        PM(r, c, g, "wings")

# ---- 8. chains: crown -> pan rims, long mirrored cascades ----
OUTER = [(2, 17), (3, 15), (4, 13), (5, 11), (6, 10), (7, 9), (8, 8),
         (9, 7), (10, 6), (11, 5), (12, 5), (13, 4), (14, 4), (15, 3)]
INNER = [(3, 19), (4, 19), (5, 18), (6, 17), (7, 17), (8, 16), (9, 16),
         (10, 15), (11, 15), (12, 15), (13, 14), (14, 14), (15, 14)]
for i, (r, c) in enumerate(OUTER + INNER):
    PM(r, c, "Ss"[i % 2], "chains")

# ---- 9. the great pans + glass bubbles, alpha left / omega right ----
PMB(13, 4, " ,·‾‾‾·, ", "bubble")
PB(14, 3, "('·'@'·')", "bubble")
PB(14, 35, "('·'w'·')", "bubble")
PMB(15, 4, " `·,_,·´ ", "bubble")
PMB(16, 1, " o===========o ", "pan")
PMB(17, 2, " \\%%%%%%%%%/ ", "pan")
PMB(18, 4, " `%%%%%´ ", "pan")

# ---- 10. crown of Maat: winged top, ribbed column, hanging drop ----
PB(0, 19, " ,%&&&%, ", "crown")
PB(1, 17, " (&&&&&&&&&) ", "crown")
PB(2, 18, " `%%[&]%%´ ", "crown")
PB(3, 20, " [%&%] ", "crown")
PB(4, 20, " [%&%] ", "crown")
PB(5, 21, " (o) ", "crown")

# ---- 11. the masked head ----
PB(6, 19, " <(¡%¡)> ", "mask")
PB(7, 20, " `,·,´ ", "skin")

# ---- 12. the robe: tall tapering gown, mirrored dither, lit center ----
ROBE = {8: 9, 9: 9, 10: 9, 11: 9, 12: 9, 13: 11, 14: 11, 15: 11, 16: 11,
        17: 9, 18: 9, 19: 7, 20: 7, 21: 7, 22: 5, 23: 5, 24: 5, 25: 3,
        26: 3, 27: 3}
for r, w in ROBE.items():
    c0 = 23 - w // 2
    row = ["("] + [None] * (w - 2) + [")"]
    for i in range(1, w - 1):
        adx = abs(c0 + i - 23)
        h = (adx * 11 + r * 17) % 10
        row[i] = ";" if h < 5 else (":" if h < 8 else "'")
    PB(r, c0 - 1, " " + "".join(row) + " ", "robe")
    if 12 <= r <= 21 and r % 2 == 0:     # pale center-light on the gown
        PM(r, 22, "'", "figure")
# harlequin chequer marks on the gown
PM(13, 20, "x", "harle")
PM(15, 21, "x", "harle")
PM(17, 20, "x", "harle")

# ---- 13. the sword: pommel, hands, crescent guard, blade on the axis ----
PB(9, 21, " (o) ", "sword")
PB(10, 20, " m'¡'m ", "skin")
P(10, 23, "¡", "sword")
PB(11, 18, " o´‾‾‾‾‾`o ", "sword")
for r in range(12, 28):
    P(r, 23, "|", "sword")

# ---- 14. the bottom dome the point rests on (answer to the crown) ----
PB(28, 18, " ,%&&&&&%, ", "sphb")
PB(29, 16, " (%%&&&&&&&%%) ", "sphb")
PB(30, 14, " (%%%&&&&&&&&&%%%) ", "sphb")
PB(31, 13, " %%%&&&&&&&&&&&&&%%% ", "sphb")
P(28, 23, "¡", "sword")                  # the point, touching the dome

# ---- 15. signature ----
PB(31, 0, " aw ", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
# symmetry audit: occupied cells should mirror about col 23 (sig row exempt)
asym = sum(1 for r in range(H - 1) for c in range(W)
           if (canvas[r][c] != " ") != (canvas[r][46 - c] != " "))
print(f"[symmetry] mismatched occupancy cells (rows 0-30): {asym}")

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "08-adjustment-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "08-adjustment-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
