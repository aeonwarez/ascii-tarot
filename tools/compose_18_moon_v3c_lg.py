#!/usr/bin/env python3
"""Moon v3c — ATMOSPHERE DOMINANT (ultracode panel, composer C).

The dark field itself is the hero: starless indigo/black midnight (sparse
symmetric grain, dense cloaked mountain masses), the pale sinister waning
moon as a dithered crescent MASS (dense gold top arc, dark swirled orb), a
pale V of tainted light converging down to the flame-point (the recession
that cures wallpaper-flatness), exactly NINE Yod-shaped blood drops
(asserted), twin Anubis with staves, jackals on watch, red/blue bell-waves
in the blood-tinged pool, and the SINGLE warm point of the card: the gold
aura + sun borne by Khephra the scarab at the very bottom.

Everything mirrors about AXIS = 23.0: sprites via PM/PMB, dither hashed on
min(c, 46-c) so the texture itself cannot drift off the axis.

Emits:
  drafts/18-moon-v3c-art-lg.txt       47x32 art, full-bleed
  drafts/18-moon-v3c-lg-classes.json  per-cell color classes (art coords)
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
    ms = s.translate(MIRROR)[::-1]
    P(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def PMB(r, c, s, cls):
    PB(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    PB(r, int(2 * AXIS) - (c + len(s) - 1), ms, cls)


def PC(r, s, cls):
    """Place centered on the axis (odd length keeps the middle on col 23)."""
    P(r, 23 - len(s) // 2, s, cls)


def PCB(r, s, cls):
    PB(r, 23 - len(s) // 2, s, cls)


def hx(r, cs, salt=0):
    """Well-mixed symmetric dither hash (linear hashes stripe at this size)."""
    v = ((r + 3 + salt) * 73856093) ^ ((cs + 7) * 19349663) ^ (salt * 83492791)
    return (v >> 4) % 100


# ------------------------------------------------------------ geometry
WATER_TOP = 23
MOON_CY, MOON_CX, MOON_RY, MOON_RX = 3.0, 23.0, 3.3, 8.5
CONE_TOP, CONE_APEX = 6, 19


def cone_hw(r):
    return 0.6 + 8.0 * (CONE_APEX - r) / (CONE_APEX - CONE_TOP)


def in_moon(r, c, pad=0.0):
    dy = (r - MOON_CY) / (MOON_RY + pad)
    dx = (c - MOON_CX) / (MOON_RX + 2.0 * pad)
    return dx * dx + dy * dy <= 1.0


def in_cone(r, c):
    return CONE_TOP <= r <= CONE_APEX and abs(c - AXIS) <= cone_hw(r)


# ------------------------------------------- 1. the starless indigo field
# Sparse black-flecked sky above; thick cloaked mountain masses flanking.
# The contrast (near-black sky vs dense flanks vs pale cone) is the card.
for r in range(0, WATER_TOP):
    for c in range(W):
        if in_moon(r, c, pad=0.25) or in_cone(r, c):
            continue
        cs = min(c, 46 - c)
        h = hx(r, cs)
        if r <= 8:
            d = 8 if cs >= 4 else 20          # near-black sky, edged capes
        else:
            d = 42                             # barren mountain mass
            if cs <= 3:
                d += 16                        # darkest at the borders
        if r >= 19:
            d = 50                             # the ground shelf
        if h >= d:
            continue
        deep = r >= 9 and h % 3 == 0
        P(r, c, ";" if deep else ",.·'"[h % 4], "tower")

# ------------------------------------------------------- 2. the pale cone
# The V of tainted light converging from moon-width down to the flame-point.
for r in range(CONE_TOP, CONE_APEX + 1):
    hw = cone_hw(r)
    cl = int(math.ceil(AXIS - hw))
    cr = int(math.floor(AXIS + hw))
    for c in range(cl + 1, cr):
        cs = min(c, 46 - c)
        h = hx(r, cs, salt=1)
        edge_d = min(c - cl, cr - c)
        if h < (64 if edge_d <= 2 else 44):
            P(r, c, "·'':"[h % 4], "cone")
    P(r, cl, "\\", "cone")
    P(r, cr, "/", "cone")
# one pair of dotted road-lines converging inside the V (depth, not lattice)
for r in range(9, 18, 2):
    hw2 = cone_hw(r) * 0.42
    P(r, int(round(AXIS - hw2)), "·", "cone")
    P(r, int(round(AXIS + hw2)), "·", "cone")

# ----------------------------------------------------- 3. the waning moon
# Offset-ellipse crescent: pale-gold arc = outer disk minus a smaller disk
# shifted down. It tapers naturally around the top; the dark orb hangs
# beneath it with the blood swirl coiled through near-black.
for r in range(0, 8):
    for c in range(14, 33):
        dyo = (r - MOON_CY) / MOON_RY
        dxo = (c - MOON_CX) / MOON_RX
        d2o = dxo * dxo + dyo * dyo
        if d2o > 1.10:
            continue
        canvas[r][c] = " "
        classes[r][c] = None
        dyi = (r - (MOON_CY + 1.15)) / (MOON_RY - 0.7)
        dxi = (c - MOON_CX) / (MOON_RX - 0.9)
        d2i = dxi * dxi + dyi * dyi
        cs = min(c, 46 - c)
        h = hx(r, cs, salt=2)
        if d2o <= 1.0 and d2i > 1.0:
            P(r, c, "%;%:"[h % 4], "moon")     # SOLID waning crescent mass
        elif d2i <= 1.0:
            if d2i >= 0.72 and dyi > 0.15:
                if h < 42:                     # faint lower limb of the orb
                    P(r, c, "'·,"[h % 3], "moon")
            elif h < 18:
                P(r, c, "·'"[h % 2], "cone")   # sickly orb-light
# the blood swirl locked in the dark of the orb
PM(3, 20, "‾~", "blood")
PM(4, 19, "~‾", "blood")
P(5, 21, ",~‾~,", "blood")

# ------------------------------------------------ 4. the nine Yod drops
# EXACTLY nine, Crowley is specific: 3 + 3 falling with the convergence,
# then 1 + 1 + 1 down the axis to the flame. Wide punched halos so each
# red drop hangs alone in the pale light.
DROPS = [(8, 19), (8, 23), (8, 27),
         (10, 20), (10, 23), (10, 26),
         (12, 23), (14, 23), (16, 23)]
for r, c in DROPS:
    PB(r, c - 2, "  ¡  ", "blood")
    for rr in (r - 1, r + 1):
        if 0 <= rr < H and canvas[rr][c] != "¡":
            canvas[rr][c] = " "
            classes[rr][c] = None
# the blood-tinge trickling on down into the flame
P(17, 23, ":", "blood")
P(18, 23, ":", "blood")

# --------------------------------------------------- 5. the black towers
# Dense structural masses on the barren summits, mirrored about the axis.
PMB(0, 6, " ,^, ", "tower")
PMB(1, 5, " /###\\ ", "tower")
PMB(2, 4, " /##%##\\ ", "tower")
PMB(3, 3, " [#######] ", "tower")
PMB(4, 4, " |%#%#%| ", "tower")
PMB(5, 4, " |#% %#| ", "tower")
PM(5, 8, "!", "cone")                          # the ghost-lit slit window
PMB(6, 4, " |%#%#%| ", "tower")
PMB(7, 4, " |#%#%#| ", "tower")
PMB(8, 3, " (#%#%#%#) ", "tower")
PMB(9, 2, " /%#%#%#%#\\ ", "tower")
# jagged ridge running off the summit toward the border
PM(3, 0, ",^,", "tower")
PM(8, 0, "^;,", "tower")
PM(11, 4, "^", "tower")
PM(14, 2, "^,", "tower")
PM(17, 5, "^", "tower")

# ------------------------------------------------------- 6. twin Anubis
# Jackal-headed guardians before the towers, staves planted, facing center.
PMB(8, 11, " ,^,_ ", "anubis")
PMB(9, 11, " (o==> ", "anubis")
PMB(10, 12, " `|;| ", "anubis")
PMB(11, 11, " (;;;) ", "anubis")
PMB(12, 11, " |;;;| ", "anubis")
PMB(13, 11, " |;;;|= ", "anubis")
PMB(14, 11, " (;;;) ", "anubis")
PMB(15, 12, " |;;| ", "anubis")
PMB(16, 12, " |;;| ", "anubis")
PMB(17, 12, " /;;\\ ", "anubis")
PMB(18, 12, " |  | ", "anubis")
PMB(19, 12, " U  U ", "anubis")
# the staves (T-finial; ¡ belongs to the nine drops alone)
PM(7, 17, "T", "anubis")
for r in range(8, 19):
    PM(r, 17, "|", "anubis")
# pale mercury sign at the outer hand
PM(12, 8, "o", "cone")
PM(13, 8, "+", "cone")

# ---------------------------------------------------------- 7. jackals
PMB(20, 6, " _,^, ", "jackal")
PMB(21, 5, " (;;;=> ", "jackal")
PMB(22, 6, " ´U`U´ ", "jackal")

# ------------------------------------------------------ 8. flame-point
# The cone's apex: the path's terminus above the pool, red core in orange.
P(19, 23, "!", "flame")
PCB(20, "/;!;\\", "flame")
PCB(21, "/;;!;;\\", "flame")
PCB(22, "(;;;!;;;)", "flame")
P(21, 23, "!", "blood")
P(22, 23, "!", "blood")

# ------------------------------------------------------------ 9. water
for r in range(WATER_TOP, H):
    for c in range(W):
        cs = min(c, 46 - c)
        k = (cs + 2 * r) % 5
        if k == 0:
            P(r, c, "-", "water")
        elif k == 3:
            P(r, c, "·", "water")

# ------------------------------------------- 10. aura + sun + scarab
# The ONLY warmth in the card: the gold aura-pool, the sun disk, and
# Khephra bearing it up through midnight.
A_CY, A_CX, A_RY, A_RX = 27.3, 23.0, 4.5, 10.8
for r in range(WATER_TOP, H):
    for c in range(W):
        dy = (r - A_CY) / A_RY
        dx = (c - A_CX) / A_RX
        d2 = dx * dx + dy * dy
        if d2 > 1.0:
            continue
        cs = min(c, 46 - c)
        h = hx(r, cs, salt=3)
        if d2 >= 0.86:
            ch = "(" if dx < -0.4 else (")" if dx > 0.4 else
                                        ("-" if dy < 0 else "_"))
            P(r, c, ch, "aura")
        elif h < 30:
            P(r, c, "·'"[h % 2], "aura")
        else:
            canvas[r][c] = " "
            classes[r][c] = None

# the blood tinge spreading into the serum of the pool (after the aura
# pass, which clears/overwrites its own interior)
PM(23, 18, "~-", "blood")
PM(24, 15, "-~", "blood")

# bell-waves, red and blue, rolling in from the borders
PMB(24, 3, " ,·, ", "wavered")
PMB(25, 3, " (;) ", "wavered")
PMB(26, 2, " (;:;) ", "wavered")
PMB(27, 2, " |;:;| ", "wavered")
PMB(28, 1, " /;;:;;\\ ", "wavered")
PMB(29, 0, " ´·, ,·` ", "wavered")
PMB(25, 7, " ,·, ", "waveblue")
PMB(26, 7, " (;) ", "waveblue")
PMB(27, 6, " (;:;) ", "waveblue")
PMB(28, 6, " |;:;| ", "waveblue")
PMB(29, 5, " /;;:;;\\ ", "waveblue")
PMB(30, 4, " ´·, ,·` ", "waveblue")

# the sun disk, and Khephra with mandibles raised around it
PC(24, ",*@@@*,", "sun")
PC(25, "`*@@@*´", "sun")
P(25, 19, "\\", "scarab")
P(25, 27, "/", "scarab")
PCB(26, "\\,(;),/", "scarab")
PCB(27, "({;x;})", "scarab")
PCB(28, "({;x;x;})", "scarab")
PCB(29, "({;x;})", "scarab")
PCB(30, "´/,|,\\`", "scarab")

# ------------------------------------------------------------ signature
PB(31, 1, " aw ", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
ycount = sum(1 for r in range(H) for c in range(W)
             if canvas[r][c] == "¡" and classes[r][c] == "blood")
assert ycount == 9, f"drop count {ycount} != 9"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "18-moon-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "18-moon-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
