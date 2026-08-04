#!/usr/bin/env python3
"""Compositor for Atu VIII Adjustment — SYNTHESIS FINAL (ultracode panel merge).

Judge tally: v3c 8, v3a 7, v3b 3 — v3c is the base, grafts from v3a and v3b.

BASE (v3c, balance dominant): the complete equilibrium apparatus — plumed
crown of Maat with the [&] uraeus, blue mask dead on col 23, mirrored
( m' 'm ) hands, the o====o beam with hung dithered pans + glass-bubble
interiors (alpha @ LEFT, omega w RIGHT), S-curve chains, four corner
spheres (dark & masses top, heavy full-bleed bottom sphere), chequer band,
spheres-and-pyramids throne, ray curtain, heavy poles top/bottom.
GRAFT 1 (v3a): explicit SWORD POINT — clean V apex landing ON the bottom
dome — plus the lower-vesica rails (pale converging diagonals from the pans
down to the toe) so toe->pans->crown reads as ONE circuit; machine-verified
mirror-audit assert (glyph-mirrored twins; exempt alpha/omega + signature).
GRAFT 2 (v3a): continuous chartreuse side masses running full height +
pale-blue side lattice — the ground reads bright chartreuse full-bleed.
GRAFT 3 (v3b): the dancer's life — spread blue wing-fans sweeping from
horizontal to steep at her shoulders, crescent crossguard c==,_¡_,==C,
tiptoe feet hugging the blade; she is punched clear with PB halos.

Emits drafts/08-adjustment-final-art-lg.txt
    + drafts/08-adjustment-final-lg-classes.json
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23.0

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]
MIRROR = str.maketrans("()/\\[]{}<>`´,.cC", ")(\\/][}{><´`,.Cc")


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


def PMBswap(r, c, s, cls_l, cls_r):
    """Mirror pair with swapped classes (light<->dark across the axis)."""
    PB(r, c, s, cls_l)
    ms = s.translate(MIRROR)[::-1]
    PB(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls_r)


BG = (None, "ground", "lattice", "harle", "rays")


def rail(r0, c0, r1, c1, cls="rays"):
    """Mirror-exact pale diagonal ('\\' left, '/' right); passes BEHIND
    solid masses — only background classes are overwritten."""
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        rr = int(round(r0 + (r1 - r0) * i / steps))
        cc = int(round(c0 + (c1 - c0) * i / steps))
        if 0 <= rr < H and 0 <= cc < W and cc < 23:
            if classes[rr][cc] in BG:
                P(rr, cc, "\\", cls)
            if classes[rr][46 - cc] in BG:
                P(rr, 46 - cc, "/", cls)


# ---- 1. ground: bright chartreuse full-bleed, no gaps (graft 2) ---------
# Mirror-exact: keyed on adx = |c - 23|. Sides get continuous %% masses
# running full height, dense at the edge and lit inboard; the middle rows
# use lighter glyphs (the scan's luminous middle).
for r in range(H):
    for c in range(W):
        adx = abs(c - 23)
        if adx >= 19 and 4 <= r <= 28:
            g = "%" if (adx >= 21 or (adx * 3 + r * 5) % 4 < 2) else ";"
        else:
            h = (adx * 7 + r * 13) % 8
            g = ("';':·';·" if 10 <= r <= 21 else ";';:;,':")[h]
        P(r, c, g, "ground")

# ---- 2. pale-blue harlequin lattice over the whole field (graft 2) ------
for r in range(H):
    for c in range(W):
        adx = abs(c - 23)
        v1 = (adx + 2 * r) % 6 == 0
        v2 = (adx - 2 * r) % 6 == 0
        if v1 and v2:
            P(r, c, "x", "lattice")
        elif v1:
            P(r, c, "\\" if c < 23 else "/", "lattice")
        elif v2:
            P(r, c, "/" if c < 23 else "\\", "lattice")

# ---- 3. harlequin diamonds: dark canopy across the top + side accents ---
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

# ---- 4. feathered curtain of rays, far edges, faint + symmetric ---------
for r in range(5, 26):
    PM(r, 0, "'|·"[r % 3], "rays")
    if r % 2 == 0:
        PM(r, 2, "(", "rays")
    else:
        PM(r, 1, "·", "rays")

# ---- 5. the throne: upper pylons, dark shelf, inverted spikes -----------
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

# ---- 7. lower vesica rails: pans converging down to the toe (graft 1) ---
# The upper vesica is the chains themselves (crown -> pans); these pale
# rails close the circuit toe -> pans -> crown as one diamond.
rail(19, 3, 26, 20)
rail(19, 12, 26, 21)

# ---- 8. wings: spread blue fans, horizontal to steep (graft 3) ----------
ORR, ORC = 7.5, 21.0                    # radiant origin at her shoulder
for r in range(6, 16):
    for c in range(4, 20):
        dx = ORC - c
        dy = 2.0 * (r - ORR)
        if dx < 1.5:
            continue
        d = math.hypot(dx, dy)
        if not (3.0 <= d <= 17.0):
            continue
        ang = math.atan2(dy, dx)
        if not (-0.20 <= ang <= 1.35):
            continue
        if (r * 5 + c * 3) % 13 == 0:
            continue                    # diaphanous pinholes
        a = abs(dy) / dx
        g = "‾" if a < 0.35 else ("/" if a < 1.4 else "(")
        PM(r, c, g, "wings")

# ---- 9. chains: crown -> pan rims, long mirrored cascades ---------------
OUTER = [(2, 17), (3, 15), (4, 13), (5, 11), (6, 10), (7, 9), (8, 8),
         (9, 7), (10, 6), (11, 5), (12, 5), (13, 4), (14, 4), (15, 3)]
INNER = [(3, 19), (4, 19), (5, 18), (6, 17), (7, 17), (8, 16), (9, 16),
         (10, 15), (11, 15), (12, 15), (13, 14), (14, 14), (15, 14)]
for i, (r, c) in enumerate(OUTER + INNER):
    PM(r, c, "Ss"[i % 2], "chains")

# ---- 10. the great pans + glass bubbles, alpha left / omega right -------
PMB(13, 4, " ,·‾‾‾·, ", "bubble")
PB(14, 3, "('·'@'·')", "bubble")
PB(14, 35, "('·'w'·')", "bubble")
PMB(15, 4, " `·,_,·´ ", "bubble")
PMB(16, 1, " o===========o ", "pan")
PMB(17, 2, " \\%%%%%%%%%/ ", "pan")
PMB(18, 4, " `%%%%%´ ", "pan")

# ---- 11. crown of Maat: winged top, [&] uraeus, ribbed column, drop -----
PB(0, 19, " ,%&&&%, ", "crown")
PB(1, 17, " (&&&&&&&&&) ", "crown")
PB(2, 18, " `%%[&]%%´ ", "crown")
PB(3, 20, " [%&%] ", "crown")
PB(4, 20, " [%&%] ", "crown")
PB(5, 21, " (o) ", "crown")

# ---- 12. the masked head ------------------------------------------------
PB(6, 19, " <(¡%¡)> ", "mask")
PB(7, 20, " `,·,´ ", "skin")

# ---- 13. the robe: tapering gown, mirrored dither, lit center -----------
ROBE = {8: 9, 9: 9, 10: 9, 11: 9, 12: 9, 13: 11, 14: 11, 15: 11, 16: 11,
        17: 9, 18: 9, 19: 7, 20: 7, 21: 7, 22: 5, 23: 5, 24: 5, 25: 3}
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

# ---- 14. tiptoe feet hugging the blade (graft 3) ------------------------
PB(26, 21, " ) ( ", "skin")

# ---- 15. the sword: pommel, hands, crescent guard, blade, V point -------
PB(9, 21, " (o) ", "sword")
PB(10, 20, " m'¡'m ", "skin")
P(10, 23, "¡", "sword")
PB(11, 17, " c==,_¡_,==C ", "sword")    # crescent crossguard (graft 3)
for r in range(12, 27):
    P(r, 23, "|", "sword")
P(27, 23, "V", "sword")                  # the point, landing on the dome

# ---- 16. the bottom dome the point rests on (answer to the crown) -------
PB(28, 18, " ,%&&&&&%, ", "sphb")
PB(29, 16, " (%%&&&&&&&%%) ", "sphb")
PB(30, 14, " (%%%&&&&&&&&&%%%) ", "sphb")
PB(31, 13, " %%%&&&&&&&&&&&&&%%% ", "sphb")

# ---- 17. signature ------------------------------------------------------
PB(31, 0, " aw ", "sig")

# ---------------------------------------------------------------- checks
for r in range(H):
    assert len(canvas[r]) == W
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert canvas[0][23] == "&" and canvas[27][23] == "V", "axis endpoints"

# machine mirror audit (graft 1): every cell must equal its glyph-mirrored
# twin; exempt only alpha/omega and the aw signature.
EXEMPT = {(14, 7), (14, 39)} | {(31, c) for c in range(4)} \
    | {(31, 46 - c) for c in range(4)}
bad = []
for r in range(H):
    for c in range(23):
        if (r, c) in EXEMPT or (r, 46 - c) in EXEMPT:
            continue
        lch, rch = canvas[r][c], canvas[r][46 - c]
        if rch != lch.translate(MIRROR):
            bad.append((r, c, lch, rch))
assert not bad, f"mirror broken at {bad[:8]}"
print("[mirror audit] exact: 0 mismatches (alpha/omega + sig exempt)")

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "08-adjustment-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "08-adjustment-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
