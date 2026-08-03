#!/usr/bin/env python3
"""Star v3a — GLOBE-AS-STAGE dominant (ultracode panel, composer A).

The huge rose celestial sphere IS the field: a 41x21-cell dithered
ellipse (2:1 aspect baked in) centered on the axis, lit from the great
star upper-left, dark on the lower-right limb, with faint spiral bands.
Nuith kneels SMALLER in front of it, seen from behind, S-curve torso,
one arm arched overhead to the gold cup (curved cascade onto her own
crown), the other reaching down to the silver cup whose dead-straight
rectilinear stream is the ONLY straight thing in the frame. Three true
heptagrams: great star UL (CCW), star whirling on the globe, star-seed
tumbling CW out of the gold cup. Shore: sea of Binah, faceted crystals,
Pyramid City, roses, butterflies.

Emits:
  drafts/17-star-v3a-art-lg.txt        47x32 art, full-bleed
  drafts/17-star-v3a-lg-classes.json   per-cell color classes
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


# ------------------------------------------------------------- sky field
# Indigo cosmos swirling around the globe: sparse curved-stroke dust so
# no corner reads as dead black. Rows 0..25 (shore repaints 25+).
SCY, SCX = 13.5, 23.0
for r in range(26):
    for c in range(W):
        dx = c - SCX
        dy = 2.0 * (r - SCY)
        th = math.atan2(dy, dx)
        h = (r * 43 + c * 17 + (r * c) % 7) % 100
        if h >= 30:
            continue
        # tangent-direction curved strokes: the field spirals
        tt = (th + math.pi / 2) % math.pi
        if tt < math.pi / 6 or tt > 5 * math.pi / 6:
            ch = "~" if h % 3 == 0 else "·"
        elif tt < math.pi / 2:
            ch = "`" if h % 3 == 0 else ("." if h % 3 == 1 else "·")
        else:
            ch = "´" if h % 3 == 0 else ("," if h % 3 == 1 else "·")
        P(r, c, ch, "sky")

# bold sweep arcs upper-right + around the great star (Harris's vortices)
P(0, 30, "_,.--~--.,_", "sky")
P(1, 36, "`~-.,_", "sky")
P(2, 42, "`~,", "sky")
P(0, 13, ",~-.,", "sky")
P(1, 13, "`~,", "sky")

# ------------------------------------------------------------- the GLOBE
# The stage. Ellipse center on the axis, A=20.5 cols x B=10.25 rows
# (2:1 baked in): spans cols ~3..43, rows ~4..23. Lit upper-left toward
# the great star; dense rose mass on the lower-right limb; faint spiral
# banding for the celestial traceries.
CX, CY, A, B = 23.0, 13.5, 20.5, 10.25
LR, LC = 6.5, 12.0
for r in range(H):
    for c in range(W):
        dx, dy = (c - CX) / A, (r - CY) / B
        rr = dx * dx + dy * dy
        if rr > 1.0:
            continue
        # lighting: distance from the light point + limb darkening
        l = math.hypot((c - LC) / (2 * A), (r - LR) / B)
        shade = 0.62 * l + 0.45 * rr
        # faint spiral banding (the whirling constellation traceries)
        d = math.sqrt(rr)
        th = math.atan2(dy, dx)
        shade += 0.10 * math.sin(3.0 * th + 7.0 * d)
        h = ((r * 5 + c * 3 + (r * c) % 5) % 11) / 11.0
        if shade < 0.20:
            ch = "'" if h < 0.60 else ("·" if h < 0.92 else " ")
        elif shade < 0.38:
            ch = "·" if h < 0.50 else ("." if h < 0.97 else " ")
        elif shade < 0.60:
            ch = ":" if h < 0.55 else "."
        elif shade < 0.85:
            ch = ";" if h < 0.60 else ":"
        else:
            ch = ";" if h < 0.75 else "%"
        if ch != " ":
            P(r, c, ch, "globe")

# rim hoop: crisp sphere boundary riding the ellipse edge
for r in range(H):
    dyn = (r - CY) / B
    s = 1 - dyn * dyn
    if s < 0:
        continue
    x = A * math.sqrt(s)
    cl, cr = int(round(CX - x)), int(round(CX + x))
    if abs(dyn) > 0.90:
        ch = "-" if dyn < 0 else "_"
        for c in range(cl + 2, cr, 2):
            P(r, c, ch, "globe")
    elif abs(dyn) > 0.55:
        P(r, cl, "/" if dyn < 0 else "\\", "globe")
        P(r, cr, "\\" if dyn < 0 else "/", "globe")
    else:
        P(r, cl, "(", "globe")
        P(r, cr, ")", "globe")

# ------------------------------------------------------------- shore
# Sea of Binah (left) meets the crystalline earth (right); the junction
# sits where the rigid stream lands (~col 12-14).
for r in range(25, H):
    for c in range(W):
        canvas[r][c] = " "
        classes[r][c] = None
for r in range(26, H):
    for c in range(0, 16):
        k = (c + r * 3) % 4
        ch = "~" if k == 0 else ("·" if k == 1 else ("-" if k == 2 else " "))
        if ch != " ":
            P(r, c, ch, "water")
# the sea horizon runs the full width behind her and the crystals
for c in range(W):
    k = (c * 3 + 1) % 5
    ch = "~" if k == 0 else ("·" if k == 2 else ("-" if k == 3 else " "))
    if ch != " ":
        P(25, c, ch, "water")
# Pyramid City far across the sea, tiny
PB(25, 5, " ,^,^, ", "pyramid")
PB(26, 4, " /:¡::\\ ", "pyramid")
# crystalline earth: seven-sided solids, facets shaded light/dark
P(26, 15, ",_,/\\,__,/\\_,__,/\\,_,/\\,_,/\\,_", "crystal")
P(27, 14, "/'::\\/;;\\/':\\/‾;\\/'::\\/;'\\/::\\", "crystal")
P(28, 13, "/':;;\\/'‾\\/;::\\/':\\/;;'\\/‾:\\/;:\\", "crystal")
P(29, 13, "\\;/'\\/::;\\/';;\\/:'\\/‾;:\\/';\\/;'/", "crystal")
P(30, 14, "`\\/;:'\\/‾'\\/:;\\/';:\\/:‾\\/;;\\/´", "crystal")
# mauve earth underline, full-bleed to the corner
P(31, 0, "~.~^~.~^~.~^~", "water")
P(31, 13, "_,;:;,_,:;:,_,;:;,_,:;:,_,;:;,_,:_", "earth")

# ------------------------------------------------------- the great star
# 7 rays (one straight up, none straight down), tips curled CCW.
PB(0, 1, " `,  \\ ' /    ", "star")
PB(1, 1, "  `.  \\|/  ,´ ", "star")
PB(2, 0, " ·--=((o))=--· ", "star")
PB(3, 1, "  ,´  /|\\  `. ", "star")
PB(4, 1, " ´   / ¡ \\   `", "star")
PB(5, 3, "  ,´   `,  ", "star")

# ---------------------------------------------- star whirling ON globe
# second heptagram, spinning on the sphere itself, spiral tracery arms
PB(8, 9, "  \\'/  ", "star")
PB(9, 7, " ·-((o))-· ", "star")
PB(10, 9, "  /,\\  ", "star")
P(8, 16, "´", "babalon")
P(10, 6, ",", "babalon")
P(11, 12, "`--·", "babalon")
P(7, 8, "·--´", "babalon")

# --------------------------------------------------- gold cup, raised
# tipped, pouring the milk of the stars onto her own crown: CURVED fall
PB(2, 26, " ,__, ", "gold")
PB(3, 25, " (____\\ ", "gold")
# curved cascade swinging down-left onto her crown
PB(4, 22, " ,(´ ", "gold")
PB(5, 21, " (: ", "gold")
P(5, 24, "'", "gold")
# star-seed tumbling CLOCKWISE out of the cup (third heptagram, tiny)
PB(2, 34, " \\'/ ", "babalon")
PB(3, 33, " -(o)-, ", "babalon")
PB(4, 34, " / \\ ", "babalon")
P(5, 37, ".", "babalon")

# ------------------------------------------------------------ the figure
# Nuith from behind, kneeling small against the globe, whirling.
# Head r6-7, shoulders right (c24), waist left (c21), hips right (c24):
# the S-curve. Kneel resolves onto the shore at r22-23.
# hair whirling up-left into the clouds that hide the Abyss
PB(5, 15, " ~,´ ", "nuith")
PB(6, 13, " ~,´ ", "nuith")
PB(7, 12, " `~, ", "nuith")
# head seen from behind: hair whorl cap
PB(6, 19, " ,cCc, ", "nuith")
PB(7, 19, " (;;;;) ", "nuith")
# raised arm arching overhead to the gold cup, hand at its foot
PB(4, 27, " (´ ", "silver")
PB(5, 27, " ( ", "silver")
PB(6, 26, " ( ", "silver")
PB(7, 25, " ,´ ", "silver")
# shoulders + back: S-curve torso
PB(8, 18, " ,(;;;;;)´ ", "silver")
PB(9, 18, " (;;;;;;;) ", "silver")
PB(10, 17, " );;;;;;( ", "silver")
PB(11, 16, " (;;;;;;) ", "silver")
PB(12, 16, " );;;;;;( ", "silver")
PB(13, 17, " `,;;;;;;`, ", "silver")
PB(14, 18, " (;;;;;;;;) ", "silver")
PB(15, 18, " );;;;;;;;( ", "silver")
PB(16, 18, " (;;;;;;;;;) ", "silver")
PB(17, 17, " (;;;;;;;;;;) ", "silver")
PB(18, 16, " `,;;;;;;;;;;) ", "silver")
PB(19, 16, " ,;;;;;;;;;;;`, ", "silver")
PB(20, 15, " ,;;;;;;;;;;;;;,_ ", "silver")
PB(21, 14, " (;;;;;;;;;;;;;;;;`, ", "silver")
PB(22, 14, " `--´`--,;;;;;;;;;;) ", "silver")
PB(23, 20, " `--,;;;;,--´ ", "silver")
# hair tail whirling down the right side of her back: a thick blue river
PB(9, 28, "),_ ", "nuith")
PB(10, 27, " );, ", "nuith")
PB(11, 26, " );, ", "nuith")
PB(12, 26, " );; ", "nuith")
PB(13, 28, ");; ", "nuith")
PB(14, 29, "`;, ", "nuith")
PB(15, 29, " );; ", "nuith")
PB(16, 30, "`;, ", "nuith")
PB(17, 30, " );; ", "nuith")
PB(18, 30, " `;, ", "nuith")
PB(19, 31, " `;~,_ ", "nuith")
PB(20, 33, " `~;,_ ", "nuith")
# the drape pouring off her kneel into the crystal field
P(23, 34, "`~,_", "nuith")
P(24, 36, "`~,_", "nuith")
P(25, 38, "`~,", "nuith")
# left arm reaching down to the silver cup
PB(10, 15, " ( ", "silver")
PB(11, 14, " ( ", "silver")
PB(12, 12, " `, ", "silver")
PB(13, 11, " ( ", "silver")
PB(14, 10, " `, ", "silver")
PB(15, 9, " ) ", "silver")
PB(16, 9, " (, ", "silver")

# ------------------------------------------- silver cup + RIGID stream
# The one straight thing in the card. Painted late: nothing breaks it.
PB(17, 8, " ,--, ", "silver")
PB(18, 7, " ( ~~ ) ", "silver")
PB(19, 8, " `)(´ ", "silver")
for r in range(20, 28):
    PB(r, 9, " | | ", "silver")
PB(28, 8, " ,|_|, ", "silver")

# ------------------------------------------------------------ witnesses
PB(21, 41, " }v{ ", "fly")
PB(24, 40, " }v{ ", "fly")
PB(18, 42, " }v{ ", "fly")
PB(26, 40, " ,o, ", "rose")
PB(27, 43, " ,o, ", "rose")
PB(28, 39, " ,o, ", "rose")

# ------------------------------------------------------------------ sig
P(30, 2, "aw", "sig")

# ----------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert all(len(row) == W for row in canvas)

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "17-star-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "17-star-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
