#!/usr/bin/env python3
"""Atu X Fortune — panel candidate v3b (strategy: RIDERS DOMINANT).

The three gunas are the hero read: the bright-gold Sphinx reclining atop the
wheel with the sword upright on the axis (Sulphur), the cool grey-gold
Hermanubis with blue-grey back-plates climbing the LEFT rim (Mercury), the
warm red-gold crocodile-headed Typhon falling head-down on the RIGHT with
inverted ankh + crook (Salt). The ten-spoked wheel is the frame that carries
them — drawn small enough that both side-riders live OUTSIDE the rim and
only grip its edge, so the golden circle stays closed. Hub (rayed sun) dead
on col 23; blue-violet plume whirlpool full-bleed; star band of gold+blue
distorted stars issuing orange lightnings; faint purple apex-up triangle.

Emits:
  drafts/10-fortune-v3b-art-lg.txt       47x32 art
  drafts/10-fortune-v3b-lg-classes.json  per-cell class grid
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23.0

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]
MIRROR = str.maketrans("()/\\[]{}<>`´,.", ")(\\/][}{><´`,.")

BG = {None, "field", "plume", "dusk", "tri"}   # classes bolts/spokes may cover


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
    ms = s.translate(MIRROR)[::-1]
    P(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def PMB(r, c, s, cls):
    PB(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    PB(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def PBGC(r, c, ch, cls):
    """Place only over background classes (weaves behind solids)."""
    if 0 <= r < H and 0 <= c < W and classes[r][c] in BG:
        canvas[r][c] = ch
        classes[r][c] = cls


# ------------------------------------------------------------ 1. whirlpool
# Blue-violet plume field drawn out by the spin, centered on the hub.
CY, CX = 15.5, 23.0
SWIRL = 6.0
RY, RX = 6.5, 13.0        # outer rim: rows 9..22, cols 10..36 (2:1 ellipse)
RY2, RX2 = 5.1, 10.2      # inner rim edge
BAND_IN, BAND_OUT = 9.9, 13.4


def dist(r, c):
    dx = c - CX
    dy = 2.0 * (r - CY)
    return math.hypot(dx, dy), math.atan2(dy, dx) % (2 * math.pi)

BANDCH = {
    "plume": "~-;,",
    "field": ";:·,",
    "dusk":  "·,.:",
}
BANDCOV = {"plume": 82, "field": 76, "dusk": 58}

for r in range(H):
    for c in range(W):
        d, th = dist(r, c)
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if d < BAND_IN:
            # inside the rim: quiet deep violet so the spokes read
            if h < 30:
                P(r, c, "·," [h % 2], "dusk")
            continue
        dd = d + SWIRL * th / (2 * math.pi)
        bi = int(dd / 4.6) % 3
        cls = ("plume", "field", "dusk")[bi]
        t = (dd % 4.6) / 4.6
        cov = BANDCOV[cls] + (8 if t < 0.3 else 0)
        if h >= cov:
            continue
        ch = BANDCH[cls][0] if t < 0.3 else BANDCH[cls][h % 4]
        P(r, c, ch, cls)

# ------------------------------------------------------ 2. star firmament
# Distorted five-pointed stars, great gold ones mixed with blue, over the
# top band; a fringe of pendant points below them.
# great gold star dead on the axis (the sword rises into it)
PB(0, 19, " __\\¡/__ ", "starsg")
PB(1, 18, " ==<(*)>== ", "starsg")
PB(2, 19, " ‾/;¡;\\‾ ", "starsg")
# flanking gold stars
PB(0, 6, " \\¡/ ", "starsg")
PB(1, 5, " <(*)> ", "starsg")
PB(2, 6, " /¡\\ ", "starsg")
PB(0, 36, " \\¡/ ", "starsg")
PB(1, 35, " <(*)> ", "starsg")
PB(2, 36, " /¡\\ ", "starsg")
# blue stars between
PB(0, 12, " ·+· ", "starsb")
PB(1, 29, " >+< ", "starsb")
PB(0, 31, " ·+· ", "starsb")
PB(1, 12, " >+< ", "starsb")
PB(0, 1, " + ", "starsb")
PB(0, 43, " + ", "starsb")
PB(1, 44, " ·+ ", "starsb")
PB(1, 2, " +· ", "starsb")
# fringe of pendant points (the firmament's lower edge)
for c in range(W):
    if c % 3 == 1:
        P(3, c, "v", "starsg" if (c // 3) % 2 == 0 else "starsb")
    elif c % 3 == 0:
        P(3, c, "‾", "starsb")

# ---------------------------------------------------- 3. triangle (behind)
# Apex-up triangle, hub in its center; visible only outside the wheel.
for r in range(4, 27):
    fc = 23.0 - (r - 4) * 20.0 / 23.0
    for cc, ch in ((fc, "/"), (2 * AXIS - fc, "\\")):
        ci = int(round(cc))
        d, _ = dist(r, ci)
        if d > 13.8:
            PBGC(r, ci, ch, "tri")
for c in range(4, 43, 2):
    PBGC(27, c, "_", "tri")

# ------------------------------------------------------------- 4. wheel
# the rim as a dense golden band (annulus fill over the field)
for r in range(9, 23):
    for c in range(9, 38):
        d, _ = dist(r, c)
        if BAND_IN <= d <= BAND_OUT and classes[r][c] in BG:
            h = (r * 31 + c * 17 + (r + c) % 7) % 100
            P(r, c, "oo;oo:" [h % 6], "wheel")


def rim(ry, rx, top, bot, cls, arcs=True):
    # column-march for the shallow top/bottom arcs
    if arcs:
        for c in range(int(CX - rx), int(CX + rx) + 1):
            dxn = (c - CX) / rx
            s = 1 - dxn * dxn
            if s <= 0:
                continue
            y = ry * math.sqrt(s)
            slope = 0.5 * abs(dxn) / max(math.sqrt(s), 1e-6)
            if slope < 0.5:
                P(int(round(CY - y)), c, top, cls)
                P(int(round(CY + y)), c, bot, cls)
    # row-march for the steep sides
    for r in range(int(CY - ry) + 1, int(CY + ry) + 1):
        dyn = (r - CY) / ry
        s = 1 - dyn * dyn
        if s <= 0:
            continue
        x = rx * math.sqrt(s)
        cl, cr = int(round(CX - x)), int(round(CX + x))
        if abs(dyn) < 0.6:
            P(r, cl, "(", cls)
            P(r, cr, ")", cls)
        elif dyn < 0:
            P(r, cl, "/", cls)
            P(r, cr, "\\", cls)
        else:
            P(r, cl, "\\", cls)
            P(r, cr, "/", cls)


rim(RY, RX, "‾", "_", "wheel")
rim(RY2, RX2, "-", "-", "wheel", arcs=False)

# ten spokes, one dead vertical top + bottom, mirrored pairs
for k in range(10):
    a = math.radians(k * 36.0)
    sa, ca = math.sin(a), math.cos(a)
    ratio = abs(2 * sa) / max(abs(ca), 1e-6)
    if ratio < 0.7:
        g = "|"
    elif ratio > 3.2:
        g = "-"
    else:
        g = "/" if (sa > 0) == (ca > 0) else "\\"
    for t in [i / 20.0 for i in range(10, 21)]:
        rr = int(round(CY - t * RY2 * ca))
        cc = int(round(CX + t * RX2 * sa))
        PBGC(rr, cc, g, "wheel")

# the motionless hub: rayed sun dead on the axis
PB(14, 20, " ,\\¡/, ", "hub")
PB(15, 19, " =<(*)>= ", "hub")
PB(16, 20, " `/¡\\´ ", "hub")

# ------------------------------------------------- 5. Sphinx (Sulphur, gold)
# Reclining atop the wheel, head left of the axis (as in the scan), lion
# body sweeping right, the SWORD upright dead on col 23 between the paws.
PB(3, 14, " ,-^-, ", "sphinx")
PB(4, 13, " /(o·o)\\ ", "sphinx")
PB(5, 13, " ,(;;;), ", "sphinx")
PB(5, 25, " __,--,_ ", "sphinx")
PB(6, 13, " (;;;;;;`-,__,--´;;;;;;;`, ", "sphinx")
PB(7, 13, " (;;;;;;;;;;;;;;;;;;;;;;;;) ", "sphinx")
PB(8, 17, " _,UU,¡,UU;;;;;;;)_U´ ", "sphinx")
# the sword: tip in the fringe, haloed blade on the axis, guard at the paws
P(3, 23, "|", "sword")
PB(4, 22, " | ", "sword")
PB(5, 22, " | ", "sword")
PB(6, 22, " | ", "sword")
P(7, 22, "<", "sword")
P(7, 23, "+", "sword")
P(7, 24, ">", "sword")
P(8, 23, "¡", "sword")

# --------------------------------------- 6. Hermanubis (Mercury, grey-gold)
# Plate carapace on his back first, body over it: climbing OUTSIDE the
# left rim, arm up gripping the wheel, dog-ape head raised, foot on the rim.
P(11, 2, "((", "plate")
P(12, 1, "c((", "plate")
P(13, 1, "c((", "plate")
P(14, 1, "c((", "plate")
P(15, 1, "c((", "plate")
P(16, 2, "((", "plate")
PB(10, 4, " ,--, ", "herm")
PB(10, 10, " ,-´) ", "herm")
PB(11, 4, " (o;=´ ", "herm")
PB(12, 4, " (;;;), ", "herm")
PB(13, 4, " (;;;;) ", "herm")
PB(14, 4, " (;;;;) ", "herm")
PB(15, 4, " );;;( ", "herm")
PB(16, 4, " (;;;;) ", "herm")
PB(17, 5, " );;,_) ", "herm")
PB(18, 6, " (;;;) ", "herm")
PB(19, 6, " );;=) ", "herm")
PB(20, 5, " `;,´ ", "herm")
PB(21, 3, " (c,_ ", "herm")

# ------------------------------------------- 7. Typhon (Salt, red-gold)
# Falling head-down on the RIGHT: tail coiled about the rim above, body
# descending outside the rim, croc head down, inverted ankh + crook below.
PB(9, 30, " _,o-, ", "typhon")
PB(10, 31, " (o,o( ", "typhon")
PB(11, 34, " ),;;, ", "typhon")
PB(12, 36, " );;;) ", "typhon")
PB(13, 37, " (;;;) ", "typhon")
PB(14, 37, " (;;;) ", "typhon")
PB(15, 37, " (;;;) ", "typhon")
PB(16, 37, " (;;;( ", "typhon")
PB(17, 36, " );;;) ", "typhon")
PB(18, 35, " (;;;( ", "typhon")
PB(19, 33, " (;;=( ", "typhon")
PB(20, 31, " ,(;;) ", "typhon")
PB(21, 29, " (;;,´ ", "typhon")
PB(22, 28, " (o;;;( ", "typhon")
PB(23, 28, " `v;;/ ", "typhon")
PB(24, 29, " `v´ ", "typhon")
# arms + implements: inverted ankh (inner), crook (outer)
PB(23, 25, " ), ", "typhon")
PB(24, 25, " -+- ", "typhon")
PB(25, 26, " o ", "typhon")
PB(21, 36, " \\, ", "typhon")
PB(22, 37, " \\, ", "typhon")
PB(23, 38, " _7 ", "typhon")
PB(24, 39, " | ", "typhon")
PB(25, 39, " | ", "typhon")

# --------------------------------------------- 8. Kaph: the turning fist
PB(24, 21, " \\¡/ ", "hub")
PB(25, 20, " =(m)= ", "hub")
PB(26, 21, " /¡\\ ", "hub")

# ------------------------------------------------------- 9. lightnings
def bolt(r0, c0, n, cls="bolt"):
    c = float(c0)
    for i in range(n):
        r = r0 + i
        ph = i % 6
        if ph < 3:
            g = "\\"
            c += 0.45
        else:
            g = "/"
            c -= 0.45
        PBGC(r, int(round(c)), g, cls)
    PBGC(r0 + n, int(round(c)), "v", cls)


bolt(4, 2, 24)
bolt(4, 7, 6)
bolt(4, 12, 6)
bolt(4, 31, 4)    # strikes Typhon's coil on the rim
bolt(4, 34, 6)    # strikes Typhon's shoulder
bolt(4, 38, 16)   # lances down along Typhon, weaving behind his body
bolt(4, 41, 10)
bolt(4, 44, 24)
bolt(16, 43, 10)

# ---------------------------------------------------------------- sig
P(30, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "10-fortune-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "10-fortune-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
