#!/usr/bin/env python3
"""Atu VI The Lovers — SYNTHESIS final (judge-panel merge, base v3b).

BASE (v3b, duality dominant): the whole duality machine — dense dark @@
King + gold robe vs pale ''' Queen + red robe, mirrored ermine capes,
converging band fan + pale rays + dark trunks + mauve curtain drapes,
the COMPLETE Cupid (gold wings, blindfold, bow, arrow down col 23), the
hood-ring officiant with ww hands, red dais + gold concealed bow,
full-bleed warmth.
FIX 1 (judge 1): the left flank solidified as the RED lion vs the white
eagle — only the King's robe stays gold; both beast regions are flooded
to their own tincture so no gold-vs-white confusion survives.
GRAFT 2 (v3c): pedestal Lilith/Eve statues (,o, / );( / [_], serpent s
behind Eve) punched ON TOP of the fan corners.
GRAFT 3 (v3c): counterchanged clasp — dark hand & + pale hand o meeting
on the lance — and the explicit grail cup \\_/ with red arrow-rays on
the axis, replacing v3b's cxo clasp + off-axis lance.
GRAFT 4 (v3c): the speckled winged Orphic egg ('s::::S:') with <== ==>
wings and the serpent coil, recentered dead on col 23.

Emits:
  drafts/06-lovers-final-art-lg.txt       47x32 art, full-bleed
  drafts/06-lovers-final-lg-classes.json  per-cell color classes
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23.0

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]
MIRROR = str.maketrans("()/\\[]{}<>`´,.", ")(\\/][}{><´`,.")
# dark-side texture -> pale-side texture (value counterchange)
LIGHTEN = str.maketrans("@%&;#", "'\u00b7:,\"")


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


def KQ(r, c, s, clsL, clsR, lighten=True):
    """King-side sprite + mirrored Queen-side sprite, value-counterchanged."""
    PB(r, c, s, clsL)
    ms = s.translate(MIRROR)[::-1]
    if lighten:
        ms = ms.translate(LIGHTEN)
    PB(r, int(2 * AXIS) - (c + len(s) - 1), ms, clsR)


def hsh(r, c):
    return (r * 53 + c * 31 + (r * c) % 17) % 100


# ------------------------------------------------------------- 1. field
# warm gold-orange full bleed, calmer near the central corridor
for r in range(H):
    for c in range(W):
        h = (r * 37 + c * 59 + (r * c) % 11) % 100
        if 15 <= c <= 31 and r >= 10:
            cov, ramp = 80, "'':;"          # bright glow corridor
        else:
            cov, ramp = 90, ";:;'\u00b7:"
        if h < cov:
            P(r, c, ramp[h % len(ramp)], "field")

# ------------------------------------------- 2. top fan: bands + trunks
# rainbow arch-bands radiating up-out from behind the tent (origin r9.5)
for r in range(0, 9):
    for c in range(W):
        dy = 2.0 * (9.5 - r)
        a = abs(c - AXIS) / dy
        h = (r * 13 + c * 7) % 10
        if a < 0.42:
            continue                       # central corridor: tent/cupid
        ch = "\\" if c < 23 else "/"
        if a < 0.80:
            P(r, c, ch if h else "(", "bands")
        elif a < 1.06:
            P(r, c, ch, "rays")            # pale ray between bands
        elif a < 1.52:
            P(r, c, ch if h else ")", "bands")
        elif a < 1.95:
            if h < 4:
                P(r, c, "'", "field")      # gold wedge
        else:
            P(r, c, "|" if h % 3 else "(", "trunks")

# dark trunks running down both outer edges below the fan
for r in range(8, 20):
    for c in (0, 1, 2, 44, 45, 46):
        h = (r * 31 + c * 17) % 10
        if h < 9:
            P(r, c, "|" if h % 3 else ("(" if c < 23 else ")"), "trunks")
# mauve curtain-drapes inside the trunks (the robe falls down the sides)
for r in range(9, 20):
    for c in (3, 4, 5, 41, 42, 43):
        h = (r * 23 + c * 13) % 10
        if h < 7:
            P(r, c, ")" if c < 23 else "(", "hood")

# ------------------------------------------------------------ 3. carpet
for r in range(28, H):
    for c in range(W):
        k = (c + r * 2) % 4
        if r == 28:
            ch = "=" if c % 2 else ";"
        elif r == 31:
            ch = "\u00b7" if k < 2 else ":"
        else:
            ch = ";" if k == 0 else (":" if k == 2 else ("=" if k == 3 else ";"))
        P(r, c, ch, "carpet")

# ------------------------------------- 4. veil / Kether light + rays
# the white veil falls from under the hood-ring down to the exchange
PB(9, 17, " /':\u00a1:\u00a1:\u00a1:'\\ ", "tent")
PB(10, 18, " `':\u00a1\u00a1\u00a1:'\u00b4 ", "tent")
# silver ray-stripes falling in the corridor between the monarchs
for r in range(11, 15):
    for c in range(20, 28, 2):
        if (r + c) % 3:
            P(r, c, "\u00a1", "rays")

# ------------------------------------------------- 5. arch of swords
# steel blades leaning in toward the apex (left `/`, mirrored `\`)
for (r, c) in [(0, 17), (1, 16), (1, 12), (2, 11), (2, 7), (3, 6)]:
    PM(r, c, "/", "silver")
for (r, c) in [(2, 15), (3, 10), (4, 5)]:
    PM(r, c, "+", "silver")

# ------------------------ 6. the officiant: full mauve annulus hood
# (GRAFT 5 from v3a, judge 3: truest to Harris) \u2014 a solid dithered
# lens r5-7, every cell filled, rim r8 passing IN FRONT of the veil;
# the Enterer's hands emerge at the ring's ends
RAMPS = {5: ":;':", 6: ";%;;", 7: "%%;%"}
for r in (5, 6, 7):
    dyn = (r - 6) / 1.9
    x = 17.5 * math.sqrt(max(0.0, 1 - dyn * dyn))
    for c in range(int(round(23 - x)), int(round(23 + x)) + 1):
        canvas[r][c] = RAMPS[r][hsh(r, c) % 4]
        classes[r][c] = "hood"
for c in range(12, 35):         # near-side rim of the ring
    canvas[8][c] = "%;%,"[hsh(8, c) % 4] if abs(c - 23) < 9 else "%"
    classes[8][c] = "hood"
PB(5, 4, " _,_ ", "statue")     # hands of the Enterer, thrust out
PB(6, 0, " <ww= ", "statue")
PB(5, 38, " _,_ ", "statue")
PB(6, 41, " =ww> ", "statue")
PM(7, 2, "~~", "tent")          # the scroll looped round the arms

# ---------------------------------------------------------- 7. Cupid
PB(0, 19, " ,w\\ /w, ", "bow")
PB(1, 19, " ((=o=)) ", "cupid")
P(1, 27, "%", "bow")            # quiver, THELEMA implied
PB(2, 18, " <===T===> ", "bow")
P(3, 23, "\u00a1", "bow")
P(4, 23, "v", "bow")

# --------------------------- 8. Lilith UL / Eve UR (pedestal statues,
# GRAFT from v3c: drawn ON TOP, halos break the ray-fan behind them)
PB(1, 0, " ,o, ", "statue")     # Lilith: dark, the hip sway
PB(2, 0, " );( ", "statue")
PB(3, 0, " (;) ", "statue")
PB(4, 0, " \u00a1;\u00a1 ", "statue")
PB(5, 0, " [_] ", "statue")
PB(1, 42, " ,o, ", "statue")    # Eve: pale, praying
PB(2, 42, " )\u00a1( ", "statue")
PB(3, 42, " (:) ", "statue")
PB(4, 42, " \u00a1:\u00a1 ", "statue")
PB(5, 42, " [_] ", "statue")
P(0, 44, "s", "serpent")        # the serpent rising behind Eve

# ------------------------------------------- 9. the monarchs (the hero)
# crowns: gold points (Sun) vs silver crescent+orb (Moon)
P(9, 12, "\u00a1\u00a1\u00a1", "crown")
P(10, 11, "[===]", "crown")
P(9, 32, ",o,", "silver")
P(10, 31, "(\u00a1\u00a1\u00a1)", "silver")
# heads: dark King / pale gold Queen (mirrored, counterchanged)
KQ(11, 8, " ,(@@@@@), ", "king", "queen")
KQ(12, 9, " (@@@@@)\u00b4 ", "king", "queen")
# ermine capes, both sides white with tail-marks
PMB(13, 5, " ,=('v''v), ", "ermine")
PMB(14, 4, " ,('v''v'), ", "ermine")
PMB(15, 3, " ('v''v''v) ", "ermine")
PMB(16, 3, " (''v''v'') ", "ermine")
# robes: gold-orange King / red-orange Queen, serpent-and-bee motifs
ROBE = {17: (4, 16), 18: (3, 17), 19: (3, 17), 20: (2, 18), 21: (2, 18),
        22: (1, 19), 23: (1, 19), 24: (1, 19), 25: (1, 19), 26: (1, 19),
        27: (2, 19)}
for r, (c0, c1) in ROBE.items():
    for c in range(c0, c1 + 1):
        h = (r * 7 + c * 11) % 29
        if c == c0:
            chk, chq = "(", ")"
        elif c == c1:
            chk, chq = ")", "("
        elif h == 0:
            chk = chq = "s"
        elif h == 7:
            chk = chq = "e"
        else:
            chk = ";" if (r + c) % 2 else ":"
            chq = ":" if (r + c) % 2 else ";"
        P(r, c, chk, "robek")
        P(r, 46 - c, chq, "robeq")
# inner arms raised, joined on the axis (GRAFT: counterchanged clasp —
# dark hand & + pale hand o meeting on the upright lance)
P(13, 18, ",===", "lance")      # King's red-gloved arm
P(13, 22, "&", "king")          # the dark hand
P(13, 23, "\u00a1", "lance")    # the lance, upright on the axis
P(13, 24, "o", "queen")         # the pale hand
P(13, 25, "===\u00b4", "queen") # the Queen's bare arm
PB(14, 15, " ,==\u00b4 ", "lance")
PB(14, 27, " `==, ", "queen")
P(14, 23, "|", "lance")         # the lance shaft, down the axis

# ------------------- 10. the exchange on the axis (GRAFT from v3c):
# lance shaft -> sheaf of red arrows -> the explicit grail cup \_/
P(15, 23, "|", "lance")
PB(16, 20, " \\\u00a1|\u00a1/ ", "lance")
PB(17, 21, " \\\u00a1/ ", "lance")
PB(18, 20, " (:\u00a1:) ", "grail")
PB(19, 21, " \\_/ ", "grail")
P(20, 23, "\u00a1", "grail")

# ------------------------------------------ 11. counterchanged twins
# white child (King's side) with roses
PB(18, 15, " ,o, ", "childw")
PB(19, 15, " (')/ ", "childw")
PB(20, 15, " ('') ", "childw")
PB(21, 15, " )'( ", "childw")
PB(22, 15, " | | ", "childw")
PB(23, 15, " ' ' ", "childw")
P(21, 12, ",*,", "childw")
P(22, 12, "*,*", "childw")
# black child (Queen's side) with club
PB(18, 27, " (@) ", "childb")
PB(19, 26, " \\(@) ", "childb")
PB(20, 27, " (@\u00b7) ", "childb")
PB(21, 27, " )@( ", "childb")
PB(22, 27, " | | ", "childb")
PB(23, 27, " , , ", "childb")
P(20, 32, ",", "childb")
P(21, 33, "\\", "childb")
P(22, 34, "o", "childb")

# tent-light glow falling down the corridor to the egg: fill only the
# EMPTY cells between heads / twins so the spine never reads black
for r in range(11, 25):
    for c in range(17, 30):
        if canvas[r][c] == " ":
            h = (r * 5 + c * 3) % 4
            P(r, c, "'\u00b7':"[h], "field")

# --------------------------------------------------- 12. lion & eagle
PB(19, 5, " ,&&&, ", "lion")
PB(20, 3, " ,&&&&&&, ", "lion")
PB(21, 2, " (&&(o&&)< ", "lion")
PB(22, 2, " (&&&&&&&)` ", "lion")
PB(23, 1, " )&&&&&&&( ", "lion")
PB(24, 1, " )&&&&&&&( ", "lion")
PB(25, 1, " (&&&&&&&( ", "lion")
PB(26, 2, " (&&)`(&&( ", "lion")
PB(27, 2, " \u00b4U\u00b4  \u00b4U\u00b4 ", "lion")
# tail curling up with the hooked crook
P(20, 1, "c", "lion")
P(21, 1, "|", "lion")
P(22, 1, "|", "lion")
PB(19, 39, " ,\u00b7, ", "eagle")
PB(20, 37, " c((o)\u00b4 ", "eagle")
PB(21, 39, " )ww`, ", "eagle")
PB(22, 38, " (wvwv), ", "eagle")
PB(23, 38, " (vwvwv) ", "eagle")
PB(24, 38, " (wvwvw) ", "eagle")
PB(25, 39, " )vwv( ", "eagle")
PB(26, 39, " (ww)| ", "eagle")
PB(27, 39, " \u00b4L \u00b4L ", "eagle")

# FIX 1: flood the flanks to their own tincture — every non-beast cell
# in each region becomes that beast's ground, so the left flank reads
# as ONE red lion-mass vs the white eagle-mass (only the robe stays
# gold, inboard of the beasts).
for r in range(20, 28):
    for c in range(0, 10):                  # red lion ground
        if classes[r][c] != "lion":
            canvas[r][c] = ";&;:;;&;"[hsh(r, c) % 8]
            classes[r][c] = "lion"
    for c in range(37, 47):                 # white eagle ground
        if classes[r][c] != "eagle":
            canvas[r][c] = "':''\u00b7':'"[hsh(r, c) % 8]
            classes[r][c] = "eagle"

# --------------- 13. the winged Orphic egg + serpent (GRAFT from v3c,
# recentered dead on col 23; the twins stand on the wing sweeps)
PMB(24, 14, " _,=\u00b4 ", "egg")           # wing sweeps under the twins
PB(24, 24, " ,s\u00b4 ", "serpent")         # the serpent's head, rising
PB(25, 16, " <==,':\u00b7:',==> ", "egg")
PB(26, 17, " ('s::::S:') ", "egg")
PB(27, 18, " (':S:s:') ", "egg")
PB(28, 19, " `':\u00b7:'\u00b4 ", "egg")
P(26, 20, "s", "serpent"); P(26, 25, "S", "serpent")
P(27, 22, "S", "serpent"); P(27, 24, "s", "serpent")

# ------------------------------------------- 14. concealed bow + sig
PB(30, 16, "<~~~~=====~~~~>", "bow")
P(31, 2, "aw", "sig")

# -------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "06-lovers-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "06-lovers-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
