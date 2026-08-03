#!/usr/bin/env python3
"""Panel candidate A (figure-dominant) for Atu 0 The Fool.

Strategy: the leaping horned figure LARGE and central; a tight rainbow
vortex coils around him like a whirlwind he generates. The whole field is
a banded Archimedean spiral of colored light (warm core vy/vo -> vb ->
vr -> vv outward) -- no cell of the field reads as black emptiness.
Below, a strip of Nile water with the crocodile; dove rising by the left
hand, tiger lunging at his right leg, grapes + coins in the right margin.

Emits:
  drafts/00-fool-v3a-art-lg.txt       47x32 art, full-bleed
  drafts/00-fool-v3a-lg-classes.json  per-cell color classes (art coords)
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
    """Like P but spaces ERASE (1-cell breathing halo baked into sprites)."""
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


def ellipse(cy, cx, ry, rx, cls):
    for r in range(H):
        dyn = (r - cy) / ry
        s = 1 - dyn * dyn
        if s < 0:
            continue
        x = rx * math.sqrt(s)
        cl, cr = int(round(cx - x)), int(round(cx + x))
        if abs(dyn) > 0.55:
            P(r, cl, "/" if dyn < 0 else "\\", cls)
            P(r, cr, "\\" if dyn < 0 else "/", cls)
        else:
            P(r, cl, "(", cls)
            P(r, cr, ")", cls)


# ================= 1. THE VORTEX FIELD (color is the hero) =================
# Banded Archimedean spiral centred on the figure's heart. Band colors move
# warm core -> orange -> blue -> red -> violet outward. Each band gets a
# flow-stroke ring line at its centre and a dithered density fill elsewhere,
# denser toward the warm core so the middle glows.
CY = 11.5
BW = 2.6                             # band width in row-units (cells are 1:2)
BAND = ["vy", "vy", "vo", "vb", "vr", "vv"]
RAMP = {                             # dense fill, heavier toward the core
    "vy": ";:;*';:;",
    "vo": ";:';·;:",
    "vb": ";:·':.·",
    "vr": ":;.·:,·",
    "vv": ":·,;'.·",
}
WATER_TOP = 26


def flow_char(dx, dy, rr):
    """Ring-line stroke. Arcs only -- ( ) - _ -- so the figure keeps
    exclusive use of / and \\ and never gets mimicked by the field."""
    u = dy / max(rr, 1e-6)
    if abs(u) > 0.72:
        return "-" if dy < 0 else "_"
    return "(" if dx < 0 else ")"


for r in range(H):
    for c in range(W):
        if r >= WATER_TOP:
            h = (r * 5 + c * 2) % 11
            ch = "~" if h < 3 else "-" if h < 5 else "·" if h < 8 else ","
            P(r, c, ch, "water")
            continue
        dx, dy = c - AXIS, r - CY
        rr = math.sqrt((dx / 2.0) ** 2 + dy * dy)
        th = math.atan2(dy, dx / 2.0)
        sval = rr - BW * (th / (2 * math.pi))
        bi = max(0, int(sval // BW))
        cls = BAND[min(bi, len(BAND) - 1)]
        frac = (sval % BW) / BW
        u = abs(dy) / max(rr, 1e-6)
        # ring-line: side arcs get a wide window, low-ink -/_ arcs a narrow
        # one so the tops/bottoms of the rings never open into black gaps
        lo, hi = (0.40, 0.56) if u > 0.72 else (0.32, 0.68)
        if lo <= frac < hi and rr > 2.0:
            P(r, c, flow_char(dx, dy, rr), cls)
        else:
            ramp = RAMP[cls]
            P(r, c, ramp[(r * 31 + c * 11) % len(ramp)], cls)
        if cls == "vy" and r < 14 and (r * 61 + c * 23) % 53 == 5:
            P(r, c, "*", "dew")            # dew-diamonds in the warm core

# ================= 2. GRAPES (upper right) + COINS (right) =================
P(3, 40, ",o,o,", "grapes")
P(4, 39, "(o,o,o)", "grapes")
P(5, 40, "`o,o´", "grapes")
P(6, 42, "`o´", "grapes")
P(8, 41, ",-,-,", "coins")
P(9, 40, "(o(o(o)", "coins")
P(10, 40, "(o(o(o)", "coins")
P(11, 41, "`-`-´", "coins")

# ================= 3. THE FIGURE (large, ecstatic, axis col 23) ============
# head: gold horned face tilted back, pale cone between the horns.
# Cleared halo so the face reads against the dense field.
CLEAR(0, 4, 17, 29)
P(0, 16, ",´", "gold")
P(0, 22, "/¡\\", "flower")             # cone tip
P(0, 29, "`,", "gold")
P(1, 18, "(`", "gold")
P(1, 21, "/;·;\\", "flower")           # pale cone
P(1, 27, "´)", "gold")
P(2, 20, "(´o·o`)", "gold")            # wide staring eyes, tiny nose
P(3, 21, "`,O,´", "gold")              # mouth open, singing -- head thrown back
P(4, 22, "\\_/", "gold")               # jaw seen from below
# open hands, fingers spread, flung wide + high
PB(1, 9, " \\¡/ ", "fool")
PB(1, 33, " \\¡/ ", "fool")
# arms sweeping down-in from the hands to the shoulders (thick strokes)
PB(2, 9, " `=,  ", "fool")
PB(3, 11, " `==,  ", "fool")
PB(4, 14, " `==,_ ", "fool")
PB(2, 33, "  ,=´ ", "fool")
PB(3, 30, "  ,==´ ", "fool")
PB(4, 26, " _,==´ ", "fool")
# torso: green, dithered, broad chest -> pinch waist -> hips
PB(5, 19, " |;;;;;| ", "fool")
PB(6, 19, " (;;;;;) ", "fool")
PB(7, 19, " (;;;;;) ", "fool")
PB(8, 19, "  );;;(  ", "fool")
PB(9, 19, " (;;;;;) ", "fool")
PB(10, 19, " (;;;;;) ", "fool")
PB(11, 18, " (;;;;;;;) ", "fool")
PB(12, 18, " (;;;;;;;) ", "fool")
# the golden winged sun at the groin (0 = All)
PB(13, 17, " (;", "fool")
P(13, 20, "<=", "gold")
P(13, 22, "(o)", "sun")
P(13, 25, "=>", "gold")
PB(13, 27, ";) ", "fool")
# legs: wide ecstatic leap, 4-wide thighs -> 3-wide calves, tip-toe
PB(14, 15, " /;;; ", "fool"); PB(14, 26, " ;;;\\ ", "fool")
PB(15, 14, " /;;; ", "fool"); PB(15, 27, " ;;;\\ ", "fool")
PB(16, 13, " /;;; ", "fool"); PB(16, 28, " ;;;\\ ", "fool")
PB(17, 12, " /;;; ", "fool"); PB(17, 29, " ;;;\\ ", "fool")
PB(18, 11, " /;;; ", "fool"); PB(18, 30, " ;;;\\ ", "fool")
PB(19, 10, " /;; ", "fool"); PB(19, 32, " ;;\\ ", "fool")
PB(20, 9, " /;; ", "fool"); PB(20, 33, " ;;\\ ", "fool")
PB(21, 8, " /; ", "fool"); PB(21, 35, " ;\\ ", "fool")
PB(22, 7, " ;/ ", "fool"); PB(22, 36, " \\; ", "fool")
# golden shoes, on point, toes out
PB(23, 4, " ,==´ ", "gold")
PB(23, 37, " `==, ", "gold")
# the blossom dangling below the sun, between the legs
PB(15, 22, " ¡ ", "flower")
PB(16, 22, " ¡ ", "flower")
PB(17, 21, " ,*, ", "flower")

# ================= 4. THE DOVE rising by the left hand =====================
PB(3, 4, " ,// ", "dove")
PB(4, 2, " <(´;( ", "dove")
PB(5, 4, " `\\_, ", "dove")

# ================= 5. THE BUTTERFLY (psyche), left field ===================
PB(8, 3, " }v{ ", "fly")

# ================= 6. THE TIGER lunging at his right thigh =================
PB(14, 36, " ,^, ", "tiger")
P(15, 32, "<o,(", "tiger")
PB(16, 34, " `);;`, ", "tiger")
PB(17, 35, " (;=;=;) ", "tiger")
PB(18, 36, " `);;;( ", "tiger")
PB(19, 37, " ´`)`) ", "tiger")

# ================= 7. THE CROCODILE in the Nile below ======================
PB(27, 5, " ,-o-,___,--,___,--, ", "croc")
PB(28, 3, " <;==´;;`´;;;`´;;`=,~ ", "croc")
PB(29, 7, " `v´`v´`v´`v´ ", "croc")

# ================= 8. signature ============================================
P(30, 2, "aw", "sig")

# ================= sanity + emit ===========================================
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "00-fool-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "00-fool-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
