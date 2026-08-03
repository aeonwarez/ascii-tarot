#!/usr/bin/env python3
"""Atu VI The Lovers — panel candidate v3b (strategy B: DUALITY DOMINANT).

The hero read is the Hermetic Marriage as opposites resolved: the dark
King (gold crown, red-gloved lance hand, red lion, white child w/ roses)
versus the pale Queen (silver crown, grail hand, white eagle, black child
w/ club) — mirrored GEOMETRY about col 23 with contrasted VALUE (dense
glyphs on the dark side, light glyphs on the pale side). The mauve
hood-arch officiant is a smaller uniting hinge over them, hands out in
the Sign of the Enterer; blindfold Cupid fires down the axis; the
serpent-coiled winged egg sits low on the red dais between the beasts.

Emits:
  drafts/06-lovers-v3b-art-lg.txt       47x32 art, full-bleed
  drafts/06-lovers-v3b-lg-classes.json  per-cell color classes
"""
import json, os

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

# ------------------------------------- 4. tent / Kether light + rays
PB(5, 21, " ,\u00a1, ", "tent")
PB(6, 20, " /:\u00a1:\\ ", "tent")
PB(7, 19, " /:\u00a1:\u00a1:\\ ", "tent")
PB(8, 18, " /\u00a1:\u00a1:\u00a1:\u00a1\\ ", "tent")
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

# ------------------------------------------------ 6. hood-arch officiant
PMB(6, 11, " _,;==\u00b4\u00b4 ", "hood")
PMB(7, 10, " ((;;;;,_ ", "hood")
PMB(8, 9, " ((;;;;;;, ", "hood")
PB(9, 14, "`=;;;,_______,;;;=\u00b4", "hood")
PB(10, 17, "`=,_______,=\u00b4", "hood")
# arms out over the couple, Sign of the Enterer; pale hands + scroll
PMB(9, 6, " ,===,_ ", "hood")
PM(9, 3, ",ww", "statue")
PM(10, 7, "~~", "tent")         # the scroll looped round the arms

# ---------------------------------------------------------- 7. Cupid
PB(0, 19, " ,w\\ /w, ", "bow")
PB(1, 19, " ((=o=)) ", "cupid")
P(1, 27, "%", "bow")            # quiver, THELEMA implied
PB(2, 18, " <===T===> ", "bow")
P(3, 23, "\u00a1", "bow")
P(4, 23, "v", "bow")

# ------------------------------------------------ 8. Lilith UL / Eve UR
PB(1, 1, ",o,", "statue")
PB(2, 1, "(\u00a1(", "statue")
PB(3, 1, " )(", "statue")
PB(4, 1, " ==", "statue")
PB(1, 43, ",o,", "statue")
PB(2, 43, ")\u00a1(", "statue")
PB(3, 43, ")( ", "statue")
PB(4, 43, "== ", "statue")

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
# inner arms raised, joined on the axis: red glove meets pale hand
P(13, 18, ",===c", "lance")
P(13, 23, "x", "queen")
P(13, 24, "o===\u00b4", "queen")
PB(14, 15, " ,==\u00b4 ", "lance")
PB(14, 27, " `==, ", "queen")

# ------------------------------------- 10. the exchange on the axis
# lance (red) held up the King's side; grail (gold) w/ red arrows
P(15, 20, "!", "lance")
for r in range(16, 20):
    P(r, 20, "|", "lance")
P(15, 22, "\u00a1\u00a1\u00a1", "lance")
P(16, 22, "|||", "lance")
P(17, 21, "\\;;;/", "grail")
P(18, 23, "|", "grail")
P(19, 22, ",=,", "grail")

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
            P(r, c, "'·':"[h], "field")

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

# ------------------------------------- 13. winged Orphic egg + serpent
PMB(24, 12, " _,,=\u00b4\u00b4 ", "egg")
PB(25, 19, " ,(\u00b7:\u00b7), ", "egg")
PB(26, 18, " ((:\u00b7:\u00b7:)) ", "egg")
PB(27, 19, " `(\u00b7:\u00b7)\u00b4 ", "egg")
P(25, 17, "<~", "serpent")
P(26, 21, "~~~~~", "serpent")
P(27, 26, "~,", "serpent")

# ------------------------------------------- 14. concealed bow + sig
PB(30, 16, "<~~~~=====~~~~>", "bow")
P(31, 2, "aw", "sig")

# -------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "06-lovers-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "06-lovers-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
