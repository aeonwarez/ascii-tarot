#!/usr/bin/env python3
"""Moon v3a — ULTRACODE panel candidate A: ARCHITECTURAL-SYMMETRY dominant.

The whole card is a strict mirror about col 23. Every field hashes on
|c - AXIS| so the dither itself is bilaterally symmetric; every sprite is
placed with PM/PMB mirror helpers (only the 'aw' signature breaks the
mirror). Structure, top to bottom:

  rows 0-6   dark waning moon (gold crescent rim, pale globe, red swirl)
             nested in the top of the V, sinister starless sky each side
  rows 0-8   two black towers of nameless dread, PMB-mirrored, dithered
  rows 6-20  barren indigo mountain masses vs the DENSE pale cone of
             tainted light; converging edges = the receding path
             (depth, not wallpaper)
  rows 8-16  EXACTLY NINE Yod drops of blood (3 + 3 + 1 + 1 + 1)
  rows 8-18  twin Anubis with staffs, PMB-mirrored; jackals at their feet
  rows 17-20 the flame-point where the path converges, on the pool
  rows 20-22 blood-tinged pool rim
  rows 21-31 water band: aura ring, gold sun, scarab beneath, red/blue
             bell-waves mirrored each side

Emits drafts/18-moon-v3a-art-lg.txt + drafts/18-moon-v3a-lg-classes.json
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


def hsh(r, dx):
    """Mirror-symmetric hash: depends on row and |c - AXIS| only."""
    return (r * 37 + dx * 59 + (r * dx) % 13) % 100


# ---------------------------------------------------------------- sky
# rows 0-5: the abyss of night. Starless but textured — sparse indigo
# grit, a touch denser in the corners (the dark masses behind the towers).
for r in range(0, 6):
    for c in range(W):
        dx = abs(c - 23)
        h = hsh(r, dx)
        cov = 14
        if dx >= 19 and r <= 4:
            cov = 34                       # corner masses
        if h < cov:
            P(r, c, "·" if h % 3 else "'", "tower")

# ---------------------------------------------------------------- field
# rows 6-20: mountain masses vs the pale cone. The cone half-width w(r)
# shrinks with r -> converging \ / edges = the path receding to the gap.
def cone_w(r):
    return max(1.2, 8.5 - (r - 6) * 7.5 / 13.0)


MOUNT = ";;;:::,;;:"
CONE = "'·'''·,''"
for r in range(6, 21):
    w = cone_w(r)
    icl, icr = int(round(23.0 - w)), int(round(23.0 + w))
    for c in range(W):
        dx = abs(c - 23)
        h = hsh(r, dx)
        if c == icl:
            P(r, c, "\\", "cone")
        elif c == icr:
            P(r, c, "/", "cone")
        elif icl < c < icr:                # cone of tainted light: PALE MASS
            if h < 76:
                P(r, c, CONE[h % len(CONE)], "cone")
        else:                              # barren mountain mass
            if h < 82:
                P(r, c, MOUNT[h % len(MOUNT)], "tower")
            if (r * 5 + dx * 3) % 31 == 0:
                P(r, c, "^", "tower")      # jagged ridge grit

# ---------------------------------------------------------------- water
# rows 21-31: the still serum-sea. Horizontal strokes, mirror-symmetric.
for r in range(21, H):
    for c in range(W):
        dx = abs(c - 23)
        k = (dx * 2 + r * 7) % 9
        if r % 2 == 1 and (dx + r * 3) % 7 < 2:
            P(r, c, "-", "water")
        elif k == 4:
            P(r, c, "·", "water")

# ---------------------------------------------------------------- moon
# waning moon nested in the top of the V: dense gold crescent along the
# top rim, pale sphere below, red swirl through the middle. Interior
# cells are cleared so no sky grit shows through the globe.
MRY, MRX, MCY = 3.5, 8.2, 3.0
for r in range(0, 8):
    for c in range(13, 34):
        dxn = (c - 23.0) / MRX
        dyn = (r - MCY) / MRY
        nr = dxn * dxn + dyn * dyn
        h = hsh(r, abs(c - 23))
        if nr > 1.06:
            if nr <= 1.5 and r <= 4:       # clear halo so no grit hugs it
                canvas[r][c] = " "; classes[r][c] = None
            continue
        if nr > 0.52:
            if r <= 3 or nr > 0.82:        # dense gold waning crescent
                P(r, c, "%%%%;%"[h % 6], "moon")
            elif h < 92:
                P(r, c, ",", "cone")       # pale under-limb
            else:
                canvas[r][c] = " "; classes[r][c] = None
        elif h < 78:
            P(r, c, "·" if h % 3 else "'", "cone")
        else:
            canvas[r][c] = " "; classes[r][c] = None
# the blood swirl inside the globe (mirror-symmetric arcs)
P(2, 20, "~,~·~,~", "blood")
P(3, 19, ",~~·~·~~,", "blood")
P(4, 21, "`~·~´", "blood")

# ---------------------------------------------------------------- towers
# black towers of nameless dread, PMB-mirrored about the axis.
PMB(0, 6, " ,^, ", "tower")
PMB(1, 4, " ,/;;;\\, ", "tower")
PMB(2, 3, " /;;;;;;;\\ ", "tower")
PMB(3, 3, " (;;%;%;;) ", "tower")
PMB(4, 3, " T[;;;;;]T ", "tower")
PMB(5, 4, " |;%o%;| ", "tower")
PMB(6, 4, " |;;;;;| ", "tower")
PMB(7, 4, " (;;;;;) ", "tower")
PMB(8, 3, " ,;;;;;;;, ", "tower")

# ---------------------------------------------------------------- anubis
# twin jackal-headed guardians flanking the path, staff at the inner hand.
PMB(8, 11, " /\\ ", "anubis")              # ear
PMB(9, 9, " (;;;=> ", "anubis")            # skull + snout toward the path
PMB(10, 10, " );;( ", "anubis")            # neck / collar
PMB(11, 9, " (;;;;)-, ", "anubis")         # shoulders + arm to the staff
PMB(12, 10, " |;;;;| ", "anubis")
PMB(13, 10, " (;;;;) ", "anubis")
PMB(14, 9, " /;;;;;\\ ", "anubis")         # kilt flare
PMB(15, 10, " );;;;( ", "anubis")
PMB(16, 10, " |;;;;| ", "anubis")
PMB(17, 11, " );;( ", "anubis")
PMB(18, 10, " ,/ ,/ ", "anubis")           # striding feet
# outer arm + the hanging mercury sigil
PM(12, 9, "/", "anubis")
PM(13, 9, "|", "anubis")
PM(14, 9, "o", "cone")
PM(15, 9, "+", "cone")
# the staff (full height, gripped at r11)
PM(8, 17, "¡", "anubis")
for r in range(9, 19):
    PM(r, 17, "|", "anubis")

# ---------------------------------------------------------------- jackals
PMB(17, 2, " ,\\;;;=> ", "jackal")
PMB(18, 3, " ´| |` ", "jackal")

# ---------------------------------------------------------------- yods
# EXACTLY NINE blood drops: 3 + 3 + 1 + 1 + 1, converging with the cone.
# Each is halo-punched so it pops off the pale cone dither.
for r_y, c_y in [(8, 19), (8, 23), (8, 27),
                 (10, 20), (10, 23), (10, 26),
                 (12, 23), (14, 23), (16, 23)]:
    PB(r_y, c_y - 1, " ¡ ", "blood")

# ---------------------------------------------------------------- flame
# the flame-point where the path converges, rising off the pool.
P(17, 23, "¡", "flame")
PB(18, 21, " /;\\ ", "flame")
PB(19, 20, " /;%;\\ ", "flame")
P(19, 23, "%", "blood")
PB(20, 19, " (;;%;;) ", "flame")
P(20, 23, "%", "blood")

# ---------------------------------------------------------------- pool
# blood-tinged pool rim the scarab crosses beneath.
for dxp in range(4, 10):
    PM(20, 23 - dxp, "-", "water")
PM(21, 12, "(_", "water")
PM(21, 15, "~~", "wavered")
PM(21, 18, "~", "wavered")
PM(22, 15, "_", "water")
PM(22, 17, "_", "water")
PM(22, 19, "_", "water")

# ---------------------------------------------------------------- aura
# gold ring around the scarab-sun (the halo in the deep).
def ring(cy, cx, ry, rx, cls):
    import math
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


# ---------------------------------------------------------------- bells
# red/blue bell-waves, two per side, mirrored; the aura ring is drawn
# AFTER them so the gold circle stays legible where they meet.
PM(22, 4, ",-,", "wavered")
PM(23, 3, "/", "wavered"); PM(23, 7, "\\", "wavered")
PM(24, 2, "/", "wavered"); PM(24, 8, "\\", "wavered")
PM(25, 1, "/", "wavered"); PM(25, 9, "\\", "wavered")
PM(23, 4, ",-,", "waveblue")
PM(24, 3, "/", "waveblue"); PM(24, 7, "\\", "waveblue")
PM(25, 2, "/", "waveblue"); PM(25, 8, "\\", "waveblue")

PM(25, 10, ",-,", "wavered")
PM(26, 9, "/", "wavered"); PM(26, 13, "\\", "wavered")
PM(27, 8, "/", "wavered"); PM(27, 14, "\\", "wavered")
PM(28, 7, "/", "wavered"); PM(28, 15, "\\", "wavered")
PM(29, 6, "/", "wavered"); PM(29, 15, "\\", "wavered")
PM(30, 4, "_,´", "wavered")
PM(26, 10, ",-,", "waveblue")
PM(27, 9, "/", "waveblue"); PM(27, 13, "\\", "waveblue")
PM(28, 8, "/", "waveblue"); PM(28, 14, "\\", "waveblue")
PM(29, 7, "/", "waveblue"); PM(29, 14, "\\", "waveblue")

# the gold ring, on top of the waves; faint warm dither inside it
ring(27.5, 23.0, 3.7, 8.4, "aura")
for r in range(24, H):
    for c in range(15, 32):
        dxn = (c - 23.0) / 8.4
        dyn = (r - 27.5) / 3.7
        if dxn * dxn + dyn * dyn < 0.8 and hsh(r, abs(c - 23)) < 16:
            P(r, c, "·", "aura")

# ---------------------------------------------------------------- sun
# the gold sun borne through midnight — the single warm point.
PB(24, 19, " ,@@@@@, ", "sun")
PB(25, 19, " `@@@@@´ ", "sun")

# ---------------------------------------------------------------- scarab
# Khephra beneath the water, mandibles gripping the disk.
PB(26, 19, " \\`(·)´/ ", "scarab")
PB(27, 19, " =(;%;)= ", "scarab")
PB(28, 19, " =(;;;)= ", "scarab")
PB(29, 19, " /(;;;)\\ ", "scarab")
P(30, 21, "´", "scarab"); P(30, 23, "v", "scarab"); P(30, 25, "`", "scarab")

# ---------------------------------------------------------------- sig
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
n_yods = sum(1 for r in range(H) for c in range(W)
             if canvas[r][c] == "¡" and classes[r][c] == "blood")
assert n_yods == 9, f"yod count {n_yods} != 9"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "18-moon-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "18-moon-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
