#!/usr/bin/env python3
"""Lust v3b — GRAIL DOMINANT (ultracode panel, composer B).

The flaming Two-in-One cup raised aloft is the hero read: the red-orange
blazing Grail at top-center (slightly off-axis toward her right, authentic),
kundalini flame pouring up through the dawn horizon into the teal new-Aeon
burst at the top edge. Babalon (golden, arched back, spine on col 23) and
the great tawny seven-headed Beast (lower-left mass, cascading mane) are
the offering that bears it. Ten rose rayed circles scattered on the deep
purple ground, red rein loop from her left hand, sun-ringed serpent head
biting the crescent upper-right with the tail sweeping the right edge,
grey bloodless saints trampled in a Shin group at the base.

Emits:
  drafts/11-lust-v3b-art-lg.txt       47x32 art, full-bleed
  drafts/11-lust-v3b-lg-classes.json  per-cell color classes (art coords)
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


# ---------------------------------------------------------------- field
# Deep purple ground, densely dithered (no black emptiness), with darker
# dusk veins — the Harris ground is mottled violet.
for r in range(2, H):
    for c in range(W):
        h = (r * 53 + c * 31 + (r * c) % 7) % 100
        if (r * 7 + c * 11) % 31 < 4:
            P(r, c, ";", "dusk")
        elif h < 95:
            P(r, c, "·,:;,··:"[h % 8], "field")

# ---------------------------------------------------------------- sky
# Pale dawn strip, rows 0-1.
for r in range(2):
    for c in range(W):
        if (c * 7 + r * 5) % 7 != 3:
            P(r, c, "·", "sky")

# dawn horizon under the sky band (broken rule; burst/grail punch through)
for c in range(0, 14, 2):
    P(2, c, "‾", "sky")
for c in range(31, W, 2):
    P(2, c, "‾", "sky")

# ---------------------------------------------------------------- serpents
# The tawny serpent-horns of the Beast wriggling across the top band,
# destroying the old order; broken center where the burst erupts.
P(0, 0, "~s~‾~c~~s~‾~", "serpents")
P(0, 32, "~‾s~~c~‾~s~o~~s", "serpents")
P(1, 0, "·~s~‾~c~,", "serpents")
P(1, 34, "·~s~‾~s~·", "serpents")

# ---------------------------------------------------------------- burst
# Teal new-Aeon light fanning at the top edge, fed by the Grail's flame.
PB(0, 11, " `\\  '  \\ '¡' /  '  /´ ", "burst")
PB(1, 13, " \\  ' \\'¡'/ '  / ", "burst")
P(2, 17, "\\", "burst")
P(2, 25, "/", "burst")

# ---------------------------------------------------------------- circles
# Ten luminous rose rayed circles, scattered NOT in Tree order
# ("as above, so below" — the Sephiroth un-organised, a new Aeon dawning).
def rosette(r, c):
    PB(r, c + 1, " ,·, ", "circles")
    PB(r + 1, c, " (:*:) ", "circles")

def rosette_s(r, c):
    PB(r, c, " ·(*)· ", "circles")

rosette(2, 1)          # upper-left corner
rosette(2, 8)          # upper-left, beside
rosette_s(1, 30)       # upper-right of burst
rosette(7, 29)         # right of her raised arm
rosette_s(3, 31)       # upper-right, under the serpent band
rosette_s(14, 14)      # gap between the Beast's neck and her waist
rosette_s(19, 28)      # below the rein loop
rosette(18, 42)        # right edge, below the tail
rosette_s(24, 31)      # low, right of her leg
rosette_s(26, 33)      # low, among the trampled

# ---------------------------------------------------------------- sun-head
# The lion-serpent's tail head, ringed by a rayed sun, biting the crescent
# moon (upper right); the tail sweeps down the right edge.
P(3, 39, "\\'¡'/", "serpents")
P(4, 38, ",=‾¡‾=,", "serpents")
P(5, 37, "((", "beast")
P(5, 39, "C", "sky")
P(5, 40, "<o~", "beast")
P(5, 43, "))", "beast")
P(6, 38, "`=,_,=´", "serpents")
P(7, 40, "/;\\", "serpents")
# tail: contiguous 2-wide serpent column hugging the right edge
TAIL = [(7, 43), (8, 44), (9, 44), (10, 45), (11, 45), (12, 44),
        (13, 44), (14, 45), (15, 45), (16, 45)]
for i, (r, c) in enumerate(TAIL):
    P(r, c, "(s" if i % 2 else "s(", "serpents")

# ---------------------------------------------------------------- beast
# The great tawny seven-headed lion-serpent: a cascading-mane mass filling
# the lower left, its back sweeping right under her seat. Near-solid,
# with deeper mane curls flowing through.
MASK = {
    4: (0, 12), 5: (0, 13), 6: (0, 13), 7: (0, 14), 8: (0, 15),
    9: (0, 15), 10: (0, 15), 11: (0, 15), 12: (0, 15), 13: (0, 14),
    14: (0, 13), 15: (0, 18), 16: (0, 20), 17: (0, 23), 18: (0, 25),
    19: (0, 26), 20: (0, 28), 21: (0, 30), 22: (0, 30), 23: (0, 29),
    24: (0, 27), 25: (0, 23), 26: (0, 19), 27: (0, 16), 28: (0, 14),
    29: (0, 13), 30: (0, 13), 31: (0, 12),
}
for r, (c0, c1) in MASK.items():
    for c in range(c0, c1 + 1):
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        w = (3 * c + 5 * r) % 11
        if w < 3:
            P(r, c, "(", "mane")
        elif w == 3:
            P(r, c, "{", "mane")
        elif h < 97:
            P(r, c, ";se:w;"[h % 6], "beast")

# ---- the seven heads (distinct silhouettes), crowning the mass upper-left
# 1. LION, on top: ears, wide muzzle, open jaw
PB(4, 4, " ,^,_,^, ", "mane")
PB(5, 4, " (o;‾;o) ", "beast")
P(5, 6, "o", "face")
P(5, 10, "o", "face")
PB(6, 5, " \\wvw/ ", "mane")
# 2. ANGEL, small radiant face at the cluster's left shoulder
P(7, 0, "'*'", "face")
PB(8, 0, "(o)", "face")
# 3. SATYR, horned grin at the cluster's right
P(7, 11, "\\", "mane")
P(7, 14, "/", "mane")
PB(8, 10, " (>e) ", "face")
# 4. SAINT, bearded, stern, the cluster's center
PB(9, 5, " ,--, ", "face")
PB(10, 4, " (o¡o) ", "face")
PB(11, 4, " \\vvv/ ", "face")
P(12, 6, "`v´", "face")
# 5. MAN OF VALOUR, helmeted profile
PB(9, 10, " [==] ", "face")
PB(10, 10, " [o<] ", "face")
# 6. ADULTEROUS WOMAN, calm heavy-lidded oval, lower-left (the big
#    tranquil face in the scan)
PB(11, 0, ",--,", "face")
PB(12, 0, "(e·e)", "face")
PB(13, 0, "`--´", "face")
# 7. POET, laurel band, dreaming eye
PB(12, 8, " ,~~, ", "face")
PB(13, 8, " (e_) ", "face")

# ---- paws with great toes at the base (saints trampled beneath)
PB(27, 1, " _,__,__,_ ", "mane")
PB(28, 0, ",-,,-,,-,,-,", "beast")
PB(29, 0, "(o~)(o~)(o~)(", "beast")
P(30, 1, "v", "reins")
P(30, 5, "v", "reins")
P(30, 9, "v", "reins")
# right forepaw, bottom-right corner
PB(27, 37, " _,__,_ ", "mane")
PB(28, 36, " ,-,,-,,-, ", "beast")
PB(29, 36, " (o~)(o~)( ", "beast")
P(30, 38, "v", "reins")
P(30, 42, "v", "reins")

# ---------------------------------------------------------------- saints
# The grey bloodless saints trampled at the base, the group shaped like
# SHIN — three rising prongs of upturned faces.
PB(25, 17, " ,¡, ", "saints")
PB(25, 23, " ,¡, ", "saints")
PB(25, 29, " ,¡, ", "saints")
PB(26, 17, " (¡) ", "saints")
PB(26, 23, " (¡) ", "saints")
PB(26, 29, " (¡) ", "saints")
PB(27, 17, " (o) ", "saints")
PB(27, 23, " (o) ", "saints")
PB(27, 29, " (o) ", "saints")
PB(28, 16, " (‾·‾) ", "saints")
PB(28, 22, " (·‾·) ", "saints")
PB(28, 28, " (‾·‾) ", "saints")
PB(29, 16, " (e(o(o(e(o(e(o) ", "saints")
PB(30, 17, " ‾-‾-‾-‾-‾-‾-‾ ", "saints")

# ---------------------------------------------------------------- hair
# Babalon's huge golden hair, cascading from her thrown-back head down the
# right edge, widening as it falls. Solid within the band.
for r in range(10, 27):
    t = r - 10
    center = 28.5 + t * 1.05 + 1.3 * math.sin(r * 0.7)
    hw = min(2.0 + t * 0.22, 4.5)
    if r > 24:
        hw -= (r - 24) * 0.9
    for c in range(int(round(center - hw)), int(round(center + hw)) + 1):
        if 0 <= c < W:
            P(r, c, ")s;)sw"[(r * 3 + c) % 6], "hair")
# strands streaming off the skull
P(9, 27, "~s~", "hair")

# ---------------------------------------------------------------- babalon
# Golden, arched back astride the Beast, spine on col 23, head thrown
# back, right arm raised gripping the Grail's stem, left hand on the reins.
# raised right arm: fist on the stem, forearm, shoulder
PB(9, 18, " (=¡=) ", "babalon")
P(9, 21, "¡", "grail")
PB(10, 20, " \\, ", "babalon")
# head thrown back, chin up-right, throat open (ecstasy implied)
PB(9, 24, " ,-, ", "babalon")
PB(10, 24, " (o´ ", "babalon")
# torso: chest lifted, waist, hips easing left onto the Beast's back
PB(11, 19, " ,;%'%;, ", "babalon")
PB(12, 19, " (;%'%;) ", "babalon")
PB(13, 19, " (%;;%) ", "babalon")
PB(14, 20, " );%;( ", "babalon")
PB(15, 18, " (;%%;) ", "babalon")
PB(16, 17, " (;%%%;) ", "babalon")
# left arm falling to the reins
P(12, 27, ",", "babalon")
P(13, 27, "\\", "babalon")
P(14, 28, "\\", "babalon")
P(15, 28, "o", "babalon")
# folded leg down the Beast's flank: thigh to knee, calf tucked back
PB(17, 13, " ,;%%;;´ ", "babalon")
PB(18, 11, " ,;%%;´ ", "babalon")
PB(19, 11, " (;%, ", "babalon")
PB(20, 12, " `;%;, ", "babalon")
PB(21, 14, " `;;) ", "babalon")

# ---------------------------------------------------------------- reins
# Red reins in her left (carnal) hand, a loop hanging by the flank.
P(15, 29, "__", "reins")
P(16, 28, "(", "reins")
P(16, 31, ")", "reins")
P(17, 28, "(", "reins")
P(17, 31, ")", "reins")
P(18, 29, "`U´", "reins")

# ---------------------------------------------------------------- grail
# THE HERO: the flaming Holy Grail raised aloft (center c21, slightly off
# the spine-axis toward her right — authentic), the Two-in-One elixir
# blazing up through the horizon into the new-Aeon burst.
# flame column
P(2, 20, "¡#¡", "flame")
PB(3, 18, " ,@#@, ", "flame")
PB(4, 17, " (@#@#@) ", "flame")
# stray sparks
P(3, 27, "'", "flame")
P(5, 14, "·", "flame")
P(5, 28, "·", "flame")
# cup: wide blazing mouth, tapering bowl, knobbed foot, stem to her fist
PB(5, 16, " ,%@@#@@%, ", "grail")
P(5, 19, "@@#@@", "flame")
PB(6, 16, " \\%%%%%%%/ ", "grail")
PB(7, 17, " `\\%%%/´ ", "grail")
PB(8, 19, " ‾¡‾ ", "grail")
P(8, 21, "¡", "grail")

# ---------------------------------------------------------------- sig
PB(31, 0, " aw ", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "11-lust-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "11-lust-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
