#!/usr/bin/env python3
"""Compositor for the large Moon card per drafts/18-moon-fable5-prompt.md,
corrected against the Harris scan (reference/18-moon-card.jpg):

Huge pale moon orb top center (red swirl inside), flanked by two hooded
indigo towers on cloak-hills; a pale V-cone of light widens from the moon
and narrows DOWNWARD to a flame-point; nine crimson Yods fall inside it;
twin Anubis with staffs guard the ways, black jackals at their feet; below
the waterline, red-and-blue bell-waves flank a gold aura ring where the
scarab Khephra bears the sun disk through midnight.

Strict bilateral symmetry via the PM mirror helper (axis col 23).

Emits:
  drafts/18-moon-art-lg.txt        47x32 art, full-bleed
  drafts/18-moon-lg-classes.json   per-cell color classes (art coords)
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


def PM(r, c, s, cls):
    """Paint s at (r,c) AND its mirrored twin across the axis."""
    P(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    mc = int(2 * AXIS) - (c + len(s) - 1)
    P(r, mc, ms, cls)


def PB(r, c, s, cls):
    for i, ch in enumerate(s):
        if 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls if ch != " " else None


def PMB(r, c, s, cls):
    """Mirrored paint where spaces ERASE (halo built into the sprite)."""
    PB(r, c, s, cls)
    ms = s.translate(MIRROR)[::-1]
    mc = int(2 * AXIS) - (c + len(s) - 1)
    PB(r, mc, ms, cls)


def PL(block, r0, c0, cls, mirror=False, bg=False):
    fn = PMB if (mirror and bg) else (PM if mirror else P)
    for dr, line in enumerate(block.splitlines()):
        fn(r0 + dr, c0, line, cls)


# ---- 1. the great moon orb, top center, red serpent-swirl inside ----
P(0, 17, "_,,--‾‾--,,_", "moon")
P(1, 14, ",-´          `-,", "moon")
P(2, 13, "(    ,~·~~·-,   )", "moon")
P(3, 13, "(   `-~~·~´     )", "moon")
P(2, 18, ",~·~~·-,", "blood")
P(3, 17, "`-~~·~´", "blood")
P(4, 14, "`-,          ,-´", "moon")
P(5, 17, "‾``--,,--´´‾", "moon")

# ---- 2. hooded indigo towers on cloak-hills (mirrored) ----
TOWER = """\
 ,--,_
(:¡::,`,
 |::::| `,
 |:¡::|   `,
 |::::|    `,
,´:::::`,   `,
|:::::::|,   `,
(:::::::::`--,_`,"""
PL(TOWER, 1, 2, "tower", mirror=True)
PM(9, 1, "(::::::::::::,_", "tower")
PM(10, 0, "(:::::::::::::::`,_", "tower")

# ---- 3. the V-cone of tainted light: wide at the moon, narrowing down --
for r in range(6, 22):
    t = (r - 6) / 15.0
    lx = int(round(17 + t * 5.0))
    rx = int(round(29 - t * 5.0))
    P(r, lx, "\\", "cone")
    P(r, rx, "/", "cone")

# ---- 4. exactly NINE crimson Yods falling inside the cone ----
for r, c in [(7, 21), (7, 25), (9, 23), (11, 21), (11, 25),
             (13, 23), (15, 22), (15, 24), (17, 23)]:
    P(r, c, ",", "blood")

# ---- 5. twin Anubis with staffs, guarding the ways (mirrored, with
#         built-in halo so the tower cloaks break behind them) ----
ANUBIS = """\
   ,/\\,
  <´-:(
    );;(
   |;==;|
   (;;;;(
    );;(
   ´|  |` """
PL(ANUBIS, 9, 8, "anubis", mirror=True, bg=True)
PM(8, 17, "¡", "anubis")
for r in range(9, 16):
    PM(r, 17, "|", "anubis")
PM(16, 16, "´`", "anubis")
PMB(13, 6, " +o ", "blood")          # the Mercury sign in hand

# ---- 6. black jackals at their feet, on watch (mirrored, haloed) ----
PMB(17, 2, " ,^,  ", "jackal")
PMB(18, 1, " >o´)\\, ", "jackal")
PMB(19, 2, " ´´ `` ", "jackal")

# ---- 7. dark ground under towers and gods (mirrored) ----
PM(16, 0, "_,,__,´‾`,_", "tower")
PM(17, 0, ":::::::::::,_", "tower")
PM(18, 0, "::", "tower")
PM(20, 0, "‾‾--,,__", "tower")

# ---- 8. the flame-point where the cone lands ----
P(19, 22, ",¡,", "flame")
P(20, 21, "(´¡`)", "flame")
P(21, 20, "(:´¡`:)", "flame")

# ---- 9. the pool: waterline + red/blue bell-waves clear of the aura ----
P(22, 0, "-" * 47, "water")
PM(23, 1, ",-,", "wavered")
PM(24, 0, "/   \\", "wavered")
PM(25, 0, "´    `,", "wavered")
PM(24, 5, ",-,", "waveblue")
PM(25, 4, "/   \\", "waveblue")
PM(26, 3, "´     `,", "waveblue")
PM(27, 1, ",-,", "wavered")
PM(28, 0, "/   \\_", "wavered")
PM(29, 3, ",-,", "waveblue")
PM(30, 2, "/   \\", "waveblue")
PM(27, 8, "--", "water"); PM(29, 9, "--", "water")

# ---- 10. the gold aura ring; Khephra bears the sun through midnight ----
P(23, 17, "_,,--‾‾--,,_", "aura")
P(24, 15, ",-´           `-,", "aura")
P(25, 14, "(                 )", "aura")
P(26, 14, "(                 )", "aura")
P(27, 15, "`-,           ,-´", "aura")
P(28, 17, "‾``--,,--´´‾", "aura")
P(24, 21, "_(o)_", "sun")
P(25, 20, "\\,(¡),/", "scarab")
P(26, 21, "´)¡(`", "scarab")
P(27, 21, ",´ `,", "scarab")

# ---- 11. bottom waterline + signature woven in ----
P(31, 0, "-" * 47, "water")
P(31, 3, "aw", "sig")

# ---- emit ----
art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "18-moon-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "18-moon-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
