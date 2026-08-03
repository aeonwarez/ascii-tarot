#!/usr/bin/env python3
"""Fool candidate v3b — VORTEX-DOMINANT strategy (ultracode panel, composer B).

The card is a color event first: a full-bleed Archimedean spiral of banded
rainbow light (warm yellow core at the winged sun -> orange -> blue -> red ->
violet outward), coil lines traced glyph-by-glyph, band interiors dithered
and lit from the core. The horned green figure leaps at the center of the
light, smaller than the baseline, dissolving into the color. Dove upper left,
tiger lunging at his trailing leg, crocodile in the Nile strip below, grapes
and coin-heap on the right, butterfly on the coil.

Emits:
  drafts/00-fool-v3b-art-lg.txt        47x32 art, full-bleed
  drafts/00-fool-v3b-lg-classes.json   per-cell color classes (art coords)
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
    """Blank-inclusive place: spaces in s punch holes (occlusion halo)."""
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


def PL(block, r0, c0, cls):
    for dr, line in enumerate(block.splitlines()):
        P(r0 + dr, c0, line, cls)


def CLEAR(r0, r1, c0, c1):
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            canvas[r][c] = " "
            classes[r][c] = None


def hsh(r, c, salt=0):
    x = r * 49157 + c * 98317 + salt * 12289 + 7919
    x = (x ^ (x >> 7)) * 2654435761 & 0xFFFFFFFF
    x ^= x >> 11
    return x % 1000


# ---- 1. THE RAINBOW VORTEX (the hero) --------------------------------
# Spiral center = the winged sun at the groin (r10.5, c23): the 0=All
# radiating.  Visual coords correct the 1:2 cell (vy doubled).
CY, CX = 10.5, 23.0
BW = 6.5                       # coil pitch in visual units
BANDS = ["vy", "vo", "vb", "vr", "vv", "vv", "vv", "vv"]
DENS = [910, 880, 840, 800, 760, 740, 710, 680]         # fill per-mil, lit core
POOLS = {
    "vy": "''··,,**'·;'",
    "vo": ";;::''..;':;",
    "vb": "~~··''--~·:~",
    "vr": "::;;\"\"··:;.:",
    "vv": ";;::'',,··;'",
}

for r in range(H):
    for c in range(W):
        vx = c - CX
        vy = (r - CY) * 2.0
        rad = math.hypot(vx, vy)
        th = math.atan2(vy, vx)
        tfrac = (th / (2 * math.pi)) % 1.0
        u = rad / BW + tfrac
        band = min(int(u), len(BANDS) - 1)
        frac = u - int(u)
        cls = BANDS[band]
        if u >= 1.0 and frac < 0.14:
            # the coil line: one continuous PALE spiral swirling through the
            # colored bands (the prismatic ring of light)
            dyn = vy / rad if rad else 0.0
            if abs(dyn) > 0.93:
                # dash the near-horizontal runs so they curve, not bar
                if c % 2:
                    P(r, c, POOLS[cls][hsh(r, c, 7) % len(POOLS[cls])], cls)
                    continue
                g = "-" if dyn < 0 else "_"
            elif abs(dyn) > 0.55:
                g = ("/" if vx < 0 else "\\") if dyn < 0 else \
                    ("\\" if vx < 0 else "/")
            else:
                g = "(" if vx < 0 else ")"
            P(r, c, g, "ring0" if u < 4.0 else "ring1")
        elif hsh(r, c) < DENS[band]:
            if cls in ("vy", "vo") and hsh(r, c, 3) < 45:
                P(r, c, "*", "dew")            # dew-diamonds in the warm light
            else:
                pool = POOLS[cls]
                P(r, c, pool[hsh(r, c, 7) % len(pool)], cls)

# ---- 2. the Nile strip along the bottom ------------------------------
for r in range(29, 32):
    for c in range(W):
        canvas[r][c] = " "
        classes[r][c] = None
        k = hsh(r, c, 11)
        if k < 780:
            canvas[r][c] = "~~--·''~"[hsh(r, c, 13) % 8]
            classes[r][c] = "water"

# ---- 3. the crocodile (Sebek) half in the water ----------------------
PB(27, 6, " ,--,___,--,___,-o-,_ ", "croc")
PB(28, 3, " ~<=´ ;; `´ ;;; `´ ;; ,==> ", "croc")
P(29, 8, "`v´`v´ `v´ `v´`v´", "croc")

# ---- 4. grapes (upper right) + coin-heap (right) ---------------------
PB(2, 39, " ,o,o, ", "grapes")
PB(3, 38, " (o,o,o) ", "grapes")
PB(4, 39, " `o`o´ ", "grapes")
PB(7, 39, " ,-,-, ", "coins")
PB(8, 38, " (o(o(o) ", "coins")
PB(9, 38, " (o(o(o) ", "coins")
PB(10, 39, " `-`-´ ", "coins")

# ---- 5. the dove ascending, upper left near the open hand ------------
PB(2, 7, " __ ", "dove")
PB(3, 6, " <(´\\_ ", "dove")

# ---- 6. the butterfly riding the coil, left --------------------------
PB(8, 4, " }v{ ", "fly")

# ---- 7. THE FIGURE: horned, leaping, arms flung wide -----------------
# gold head, tilted back, Bacchus horn-curls + cap
PB(3, 18, " ,     , ", "gold")
PB(4, 19, " ´ /¡\\ ` ", "gold")
PB(5, 20, " (o_o) ", "gold")
# arms: left more level, right flung higher (the leap's tilt)
PB(3, 34, " w ", "gold")                       # right hand, open
PB(4, 9, " w ", "gold")                        # left hand, open
PB(4, 31, " ,==´ ", "fool")
PB(5, 28, " ,==´ ", "fool")
PB(6, 26, " ,=´ ", "fool")
PB(4, 10, " `==, ", "fool")
PB(5, 14, " `==, ", "fool")
PB(6, 18, " `=, ", "fool")
# torso, green, dissolving into the light
PB(6, 20, " |;;;| ", "fool")
PB(7, 19, " (;;;;;) ", "fool")
PB(8, 20, " );;;( ", "fool")
PB(9, 19, " (;;;;;) ", "fool")
# the winged sun at the groin — the spiral's own center
PB(10, 18, "  <=(o)=>  ", "sun")
# legs: left leading long, right trailing bent — mid-stride
PB(11, 20, " /; ", "fool")
PB(12, 18, " /; ", "fool")
PB(13, 16, " /; ", "fool")
PB(14, 14, " /; ", "fool")
PB(15, 12, " /; ", "fool")
PB(11, 23, " ;\\ ", "fool")
PB(12, 25, " ;\\ ", "fool")
PB(13, 27, " ;\\ ", "fool")
PB(14, 29, " ;= ", "fool")
# golden shoes: right higher (trailing kick), left on point below
PB(16, 8, " ,==´ ", "gold")
PB(15, 31, " `==, ", "gold")

# ---- 8. flower dangling from the sun, between the legs ---------------
PB(12, 22, " ¡ ", "flower")
PB(13, 22, " ¡ ", "flower")
PB(14, 21, " ,v, ", "flower")

# ---- 9. the tiger lunging at his trailing leg ------------------------
PB(16, 32, " ,´)_ ", "tiger")
PB(17, 30, " <o´;;`, ", "tiger")
PB(18, 31, " );;;;;) ", "tiger")
PB(19, 30, " (;;;;;( ", "tiger")
PB(20, 31, " `)´`)´ ", "tiger")

# ---- 10. the vulture (Maut), a tiny mark upper right corner ----------
P(0, 42, "‾v´", "gold")

# ---- 11. signature ---------------------------------------------------
PB(31, 0, " aw ", "sig")

# ---- invariant guards: every row inked; some row reaches col 46 ------
for r in range(H):
    if all(ch == " " for ch in canvas[r]):
        P(r, AXIS, "·", "vv")
if not any(row[W - 1] != " " for row in canvas):
    P(14, W - 1, "·", "vv")

# ---- emit ------------------------------------------------------------
art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "00-fool-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "00-fool-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
