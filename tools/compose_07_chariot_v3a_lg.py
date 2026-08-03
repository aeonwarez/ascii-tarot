#!/usr/bin/env python3
"""Chariot v3a — panel candidate A, GRAIL DOMINANT.

The glowing amethyst-blue Grail with its red radiant core is the hero read
at the exact center (r13, col 23) — a large luminous 2:1 disk-cup cradled
in pale hands — with the amber armoured Charioteer a dark frame around it.
Throne at perfect rest: frontal, symmetric, sealed, still. Swirl nimbus
field is centered ON THE GRAIL so every background ring orbits the cup.

Layout (rows): canopy+crab 0-2 · helmet 2-5 · pauldrons/chest 5-9 ·
grail 9-17 (wheels 10-16 flanking) · hands 15-17 · lap/car 17-19 ·
sphinxes 20-26 · dais 27-31.

Emits:
  drafts/07-chariot-v3a-art-lg.txt       47x32 art, full-bleed
  drafts/07-chariot-v3a-lg-classes.json  per-cell color classes
"""
import json, math, os

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


def PC(r, s, cls, punch=True):
    """Center s (odd length, symmetric padding) on the axis. Cannot drift."""
    assert len(s) % 2 == 1, f"PC needs odd-length sprite: {s!r}"
    (PB if punch else P)(r, 23 - len(s) // 2, s, cls)


# ------------------------------------------------------------- swirl field
# Nimbus rings orbit the GRAIL center (13, 23) — grail-dominant read.
CY, CX = 13.0, 23.0
EDGES = [11.0, 15.5, 20.0, 24.5, 29.0, 33.5]
for r in range(H):
    for c in range(W):
        dx = c - CX
        dy = 2.0 * (r - CY)
        d = math.hypot(dx, dy) + 2.5 * (math.atan2(dy, dx) % (2 * math.pi)) / (2 * math.pi)
        bi = 0
        while bi < len(EDGES) and d >= EDGES[bi]:
            bi += 1
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        if bi % 2 == 0:                       # pale band
            if h < 44:
                P(r, c, "·'`,"[h % 4], "field")
        else:                                 # mid-blue band
            if h < 74:
                P(r, c, ";:·,"[h % 4], "swirl")


def ring(cy, cx, ry, rx, cls):
    """Pale hoop riding a band boundary (the Harris nimbus rings)."""
    for r in range(H):
        dyn = (r - cy) / ry
        s = 1 - dyn * dyn
        if s < 0:
            continue
        x = rx * math.sqrt(s)
        cl, cr = int(round(cx - x)), int(round(cx + x))
        if abs(dyn) > 0.93:
            ch = "-" if dyn < 0 else "_"
            for c in range(cl + 1, cr, 2):
                P(r, c, ch, cls)
        elif abs(dyn) > 0.55:
            P(r, cl, "/" if dyn < 0 else "\\", cls)
            P(r, cr, "\\" if dyn < 0 else "/", cls)
        else:
            P(r, cl, "(", cls)
            P(r, cr, ")", cls)


ring(13.0, 23.0, 6.8, 14.0, "glow")
ring(13.0, 23.0, 9.6, 19.5, "glow")
ring(13.0, 23.0, 12.6, 25.5, "glow")

# ------------------------------------------------------------------- dais
for c in range(W):
    P(27, c, "=" if (c * 7) % 11 else ",", "dais")
for r in range(28, H):
    for c in range(W):
        h = (r * 31 + c * 17 + (r * c) % 7) % 100
        if h < 86:
            P(r, c, ";=:·"[h % 4], "dais")

# ----------------------------------------------------------------- wheels
# Scarlet spoked wheels, 2:1 wider than tall (1:2 cells), hub level with
# the grail, rims reaching the card edge. Mirrored by PM — cannot drift.
for r, c, s in [
    (10, 2, "_,-===-,_"),
    (11, 1, "/;;\\,|,/;;\\"),
    (12, 0, "(;;-,\\|/,-;;)"),
    (13, 0, "[==-=(o)=-==]"),
    (14, 0, "(;;-´/|\\`-;;)"),
    (15, 1, "\\;;/'|'\\;;/"),
    (16, 2, "`-,===,-´"),
]:
    PM(r, c, s, "wheel")

# ---------------------------------------------------------------- pillars
# Outer pillars pass IN FRONT of the wheels (as in the painting); inner
# pillars only show above the pauldrons before vanishing behind the figure.
for r in range(3, 19):
    PM(r, 9, "|)", "pillar")
for r in range(3, 6):
    PM(r, 15, "|)", "pillar")

# ----------------------------------------------------------------- canopy
# Deep blue band rows 0-2, white squiggle (the ABRACADABRA scribble) row 1,
# scalloped bottom edge row 2, drape tails curving down at the sides.
for c in range(W):
    h = (c * 13 + 5) % 100
    P(0, c, ";;:;"[h % 4], "canopy")
    P(1, c, ";:;;"[h % 4], "canopy")
for c in range(W):
    ph = (c + 3) % 8
    P(2, c, "\\" if ph == 0 else ("_" if ph < 4 else ("/" if ph == 4 else "‾")), "canopy")
for c in range(1, 46):
    if c % 5:
        P(1, c, "s~w~e~m~"[c % 8], "squig")
for c in (4, 10, 36, 42):
    P(0, c, "·", "squig")
PM(3, 0, "(;;,", "canopy")
PM(4, 0, "`(;", "canopy")

# ------------------------------------------------------- crab crest (grey)
PC(0, " \\o/,\\o/ ", "crab")
PC(1, " <(:¡:)> ", "crab")

# ------------------------------------------------- helmet + lowered visor
PC(2, "  ,-=-,  ", "armour")
PC(3, " (;;;;;) ", "armour")
PC(4, " [=---=] ", "visor")
PC(5, " `(;;;)´ ", "armour")

# ------------------------------------------- pauldrons + chest (rows 5-9)
PMB(5, 12, " ,===,_ ", "armour")
CHEST_HW = {6: 10, 7: 10, 8: 9, 9: 8}
for r, hw in CHEST_HW.items():
    for c in range(23 - hw, 23 + hw + 1):
        if c == 23 - hw:
            P(r, c, "(", "armour")
        elif c == 23 + hw:
            P(r, c, ")", "armour")
        else:
            h = (r * 41 + c * 23) % 100
            P(r, c, ";;:;;;"[h % 6], "armour")
PM(6, 16, "(", "armour")
PM(7, 17, "(", "armour")

# ------------------------------------------------------------------- arms
# No leading-space punches: the wheel rims live one cell to the left.
for r, c, s in [
    (8, 13, "(;;|"),
    (9, 13, "(;;|"),
    (10, 13, "|;;|"),
    (11, 13, "|;;("),
    (12, 13, "|;;("),
    (13, 13, "(;;|"),
    (14, 13, "`(;;,"),
]:
    PM(r, c, s, "armour")

# ------------------------------------------------------- lap + car + moon
PMB(17, 12, " ,;;( ", "armour")
PB(18, 13, " (;;;;;;;=x=;;;;;;;) ", "armour")
PC(19, "L,_________________________,7", "pillar", punch=False)
P(19, 21, "(,_,)", "canopy")            # the Moon he is seated upon

# ------------------------------------------- rosette studs (ten, mirrored)
for r, c in [(5, 15), (6, 17), (7, 20), (8, 16), (9, 21)]:
    PM(r, c, "*", "rosette")

# ------------------------------------------------------------------ grail
# Hero read. Blue ring, pale moon-sea glow band, red radiant core with
# revolving rays. 2:1 wider than tall. Halo-punched so it floats luminous.
GRX, GRY = 9.0, 4.6
for r in range(8, 19):
    for c in range(13, 34):
        ndx = (c - 23.0) / GRX
        ndy = (r - 13.0) / GRY
        t = math.hypot(ndx, ndy)
        if t > 1.0:
            continue
        h = (r * 53 + c * 29) % 100
        if t > 0.90:                      # rim outline, angle-aware
            if abs(ndy) > 0.85:
                ch = "-" if r < 13 else "_"
            elif abs(ndy) > 0.5:
                ch = ("/" if r < 13 else "\\") if c < 23 else ("\\" if r < 13 else "/")
            else:
                ch = "(" if c < 23 else ")"
            P(r, c, ch, "ring")
        elif t > 0.66:                    # blue ring body — dense, luminous
            P(r, c, "Oo;O"[h % 4], "ring")
        elif t > 0.45:                    # pale moon-sea whorl — always filled
            P(r, c, "·~'·"[h % 4], "glow")
        else:                             # red radiant core — solid, rayed
            ang = math.atan2(ndy, ndx)
            k = ang / (math.pi / 4.0)
            frac = abs(k - round(k))
            if t < 0.18:
                P(r, c, "@", "core")
            elif frac < 0.20:
                P(r, c, "-\\|/"[int(round(k)) % 4], "core")
            else:
                P(r, c, "*%;*"[h % 4], "core")

# ------------------------------------------------------------- pale hands
# Cupped under the disk, fingers riding up onto the blue rim.
PMB(16, 13, " (ww=, ", "hands")
PM(17, 16, "`ww=,", "hands")

# --------------------------------------------------------------- sphinxes
# Inner pair PALE (sphinxl), outer pair DARK (sphinxd) — counterchanged.
for r, s in [
    (20, "   ,-,  ,\\ "),
    (21, "  ((o)) (;| "),
    (22, "  |\\:/| |;| "),
    (23, "  ,(:), |;| "),
    (24, " ,(:::),(;| "),
    (25, " (:::::::)| "),
    (26, " U´(:::)`U  "),
]:
    PMB(r, 12, s[:11], "sphinxl")
for r, s in [
    (20, " ,v,    ,\\ "),
    (21, " (o;( ,(;\\ "),
    (22, " `(;;,(;;;| "),
    (23, "  (;;;);;;| "),
    (24, " ,(;;;;;;;( "),
    (25, " |;(;;;;;;| "),
    (26, " U`U´(;;;)´ "),
]:
    PMB(r, 1, s[:11], "sphinxd")

# -------------------------------------------------------------------- sig
P(30, 2, "aw", "sig")

# ------------------------------------------------------------------- emit
assert len(canvas) == H
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "07-chariot-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "07-chariot-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
