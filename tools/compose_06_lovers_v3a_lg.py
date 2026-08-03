#!/usr/bin/env python3
"""Atu VI The Lovers — panel candidate v3a (strategy A: sacred-spine dominant).

The vertical sacred spine is the hero: white Kether-light wedge at top ->
blindfold Cupid, arrow straight down -> the great mauve hood-arch of the
officiant with hands emerging at its ends -> the white veil with silver
rays -> the joined royal hands on col 23 -> the grail + lance-of-arrows
exchange between the counterchanged twins -> the serpent-coiled winged
Orphic egg on the red dais. Dark King + red lion left, pale Queen + white
eagle right, as mirrored value-blocks. Warm gold-orange full-bleed field,
red-orange arch bands + dark trunks above, Lilith/Eve statues cornered.

Emits:
  drafts/06-lovers-v3a-art-lg.txt       47x32 art, full-bleed
  drafts/06-lovers-v3a-lg-classes.json  per-cell color classes
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


def hsh(r, c):
    return (r * 53 + c * 31 + (r * c) % 17) % 100


# ------------------------------------------------------- 1. background
# upper third: radiating red-orange arch bands + gold field + dark trunks
# about the apex above the canvas; a pale Kether wedge widens down col 23.
for r in range(H):
    for c in range(W):
        if r >= 28:                                   # red dais / carpet
            if hsh(r, c) < 96:
                P(r, c, "==~=-·=="[(c * 2 + r * 3) % 8], "carpet")
            continue
        if (c <= 1 or c >= 45) and r <= 19:           # edge trunks
            if hsh(r, c) < 92:
                P(r, c, "|%;%"[hsh(r, c) % 4], "trunks")
            continue
        if r <= 8:                                    # arch-band zone
            a = abs((c - 23) / (r + 5.0))
            if a < 0.55:
                cls, ramp, cov = "tent", "'·:'", 72   # Kether wedge
            elif a < 1.15:
                cls, ramp, cov = "bands", ";%;%", 92
            elif a < 1.9:
                cls, ramp, cov = "field", "';:;", 84
            elif a < 2.7:
                cls, ramp, cov = "bands", ";%;%", 92
            else:
                cls, ramp, cov = "trunks", "|%;%", 90
            if hsh(r, c) < cov:
                ch = ramp[hsh(r, c) % 4]
                if cls == "bands" and hsh(r, c) % 3:
                    ch = "/" if c < 23 else "\\"
                P(r, c, ch, cls)
            continue
        if hsh(r, c) < 93:                            # warm lower field
            P(r, c, ";%:;';%;"[hsh(r, c) % 8], "field")

# ------------------------------------------------- 2. veil + silver rays
# the white tent/veil falls from behind the hood down to the exchange
for r in range(9, 16):
    c0, c1 = (17, 29) if r <= 10 else ((18, 28) if r <= 12 else (20, 26))
    for c in range(c0, c1 + 1):
        if hsh(r, c) < 68:
            canvas[r][c] = "'·:'"[hsh(r, c) % 4]
            classes[r][c] = "tent"
        else:
            canvas[r][c] = " "
            classes[r][c] = None
for r in range(9, 13):
    for c in (19, 23, 27):
        P(r, c, "|", "rays")
P(13, 21, "|", "rays"); P(13, 25, "|", "rays")
P(14, 23, "|", "rays"); P(15, 23, "|", "rays")

# ------------------------------------------- 3. mauve drapes down sides
for r in range(9, 19):
    for c in range(2, 7):
        if hsh(r, c) < 88:
            P(r, c, "(;)%;;"[hsh(r, c) % 6], "hood")
    for c in range(40, 45):
        if hsh(r, c) < 88:
            P(r, c, ")(;%;;"[hsh(r, c) % 6], "hood")

# ------------------------------------------- 4. Lilith (UL) + Eve (UR)
PB(0, 2, " o ", "statue")                 # Lilith: pale statue, hip sway
PB(1, 1, " (:) ", "statue")
PB(2, 1, " ):( ", "statue")
PB(3, 1, " (:) ", "statue")
PB(4, 1, " [=] ", "statue")
PB(0, 42, " o ", "statue")                # Eve: praying, serpent behind
P(0, 45, "s", "serpent")
PB(1, 41, " (¡) ", "statue")
PB(2, 41, " (:) ", "statue")
PB(3, 41, " ):( ", "statue")
PB(4, 41, " [=] ", "statue")

# ------------------------------------------------- 5. arch of swords
for c in (10, 13, 16, 30, 33, 36):
    P(0, c, "!", "silver")
P(1, 7, "!", "silver"); P(1, 39, "!", "silver")

# ------------------------------------------------- 6. Cupid on the axis
PB(1, 16, " ,=´ ", "cupid")               # wing arcs
PB(1, 27, " `=, ", "cupid")
P(1, 25, "*%", "bow")                     # quiver + THELEMA mark
PB(2, 17, " <===(", "cupid")              # golden wings + head
P(2, 23, "=", "silver")                   # blindfold
PB(2, 24, ")===> ", "cupid")
PB(3, 18, " `~._", "bow")                 # drawn bow
P(3, 23, "|", "silver")                   # arrow down the axis
PB(3, 24, "_.~´ ", "bow")
P(4, 23, "v", "silver")                   # arrowhead

# ------------------------------------- 7. the great hood-arch + hands
# solid dithered lens r5-7, every cell filled (a mass, not an outline);
# r8 is the ring's near-side bottom edge, passing IN FRONT of the veil
RAMPS = {5: ":;':", 6: ";%;;", 7: "%%;%"}
for r in (5, 6, 7):
    dyn = (r - 6) / 1.9
    x = 17.5 * math.sqrt(max(0.0, 1 - dyn * dyn))
    for c in range(int(round(23 - x)), int(round(23 + x)) + 1):
        canvas[r][c] = RAMPS[r][hsh(r, c) % 4]
        classes[r][c] = "hood"
for c in range(12, 35):                   # near-side rim of the ring
    canvas[8][c] = "%;%,"[hsh(8, c) % 4] if abs(c - 23) < 9 else "%"
    classes[8][c] = "hood"
PB(5, 4, " _,_ ", "statue")               # hands of the Enterer, emerging
PB(6, 0, " <ww= ", "statue")
PB(5, 38, " _,_ ", "statue")
PB(6, 41, " =ww> ", "statue")

# ------------------------------------------------- 8. King (dark, gold)
P(9, 11, "!¡!¡!", "crown")                # 5-point gold crown
PB(10, 10, " [===] ", "crown")
PB(11, 10, " (@@@) ", "king")             # dark face
PB(12, 11, " )@( ", "king")

# ------------------------------------------------ 9. Queen (pale, silver)
P(9, 33, "+", "silver")                   # cross on the silver crown
PB(10, 30, " [(:)] ", "silver")
PB(11, 29, " s(···)s ", "queen")          # golden hair + pale face
PB(12, 31, " s)·(s ", "queen")

# ---------------------------------------------- 10. ermine capes (PMB)
PMB(13, 8, " ,%'%'%'%,_ ", "ermine")
PMB(14, 7, " (%'%'%'%'%) ", "ermine")
PMB(15, 6, " ('%'%'%'%'%) ", "ermine")
PMB(16, 6, " (%'%'%'%'%'%) ", "ermine")
for r, c in [(13, 10), (13, 14), (14, 9), (14, 13), (14, 16),
             (15, 8), (15, 12), (15, 16), (16, 9), (16, 13)]:
    PM(r, c, "v", "trunks")               # dark ermine tails

# ------------------------------------- 11. joined hands across the axis
P(13, 19, "===", "lance")                 # King's red-gloved arm
P(13, 22, "\\", "lance")
P(13, 23, "w", "queen")                   # interlaced fingers
P(13, 24, "/", "queen")
P(13, 25, "===", "queen")                 # Queen's bare arm

# ------------------------------------------------- 12. robes below capes
for r, c0, c1 in [(17, 8, 17), (18, 9, 17), (19, 9, 16), (20, 10, 16)]:
    for c in range(c0, c1 + 1):
        P(r, c, ";s;e;;"[hsh(r, c) % 6] if hsh(r, c) < 88 else ";",
          "robek")
for r, c0, c1 in [(17, 29, 38), (18, 29, 37), (19, 30, 37), (20, 30, 36)]:
    for c in range(c0, c1 + 1):
        P(r, c, ";s;e;;"[hsh(r, c) % 6] if hsh(r, c) < 88 else ";",
          "robeq")

# ------------------------------------------- 13. the counterchanged twins
PB(16, 15, " (´) ", "childw")             # white child, by the King
PB(17, 15, " (%)__,", "childw")
PB(18, 15, " (%) ", "childw")
PB(19, 15, " )%( ", "childw")
PB(20, 15, " (%) ", "childw")
PB(21, 15, " / \\ ", "childw")
PB(22, 15, " | | ", "childw")
PB(23, 15, " L L ", "childw")
PB(19, 12, " ,*, ", "childw")             # white roses, held low
PB(20, 12, " *'* ", "childw")
PB(16, 27, " (%) ", "childb")             # black child, by the Queen
PB(17, 25, ",__(%) ", "childb")
PB(18, 27, " (%) ", "childb")
PB(19, 27, " )%( ", "childb")
PB(20, 27, " (%) ", "childb")
PB(21, 27, " / \\ ", "childb")
PB(22, 27, " | | ", "childb")
PB(23, 27, " L L ", "childb")
P(17, 32, "o", "trunks")                  # the club, head up
P(18, 32, "|", "trunks")
P(19, 32, "|", "trunks")

# --------------------------------- 14. lance + arrow-fan + grail (front)
P(14, 21, "¡", "lance")                   # lance head
for r in (15, 16, 17, 18, 19):
    P(r, 21, "|", "lance")
P(16, 22, "\\", "silver")                 # sheaf of arrows from the cup
P(16, 23, "¡", "silver")
P(16, 24, "/", "silver")
PB(17, 21, " (=) ", "grail")              # the golden grail
P(18, 23, "¡", "grail")

# ------------------------------------------------- 15. red lion (left)
PB(20, 2, " ,%%,_ ", "lion")
PB(21, 0, " (%%%%%,o) ", "lion")
PB(22, 0, " (%%%%%(‾<~ ", "lion")
PB(23, 0, " (%%%%%%)=´ ", "lion")
PB(24, 1, " );;;;;;( ", "lion")
PB(25, 0, " (;;;;;;;) ", "lion")
PB(26, 1, " );;/);;( ", "lion")
PB(27, 1, " ´U´ ´U´ ", "lion")

# ------------------------------------------------ 16. white eagle (right)
PB(19, 36, " <´o) ", "eagle")
PB(20, 37, " )::\\_ ", "eagle")
PB(21, 36, " (:::::, ", "eagle")
PB(22, 36, " (::;::\\ ", "eagle")
PB(23, 36, " ):::;::) ", "eagle")
PB(24, 36, " (::;:::) ", "eagle")
PB(25, 37, " )::;::( ", "eagle")
PB(26, 37, " (:::::) ", "eagle")
PB(27, 38, " L´ `7 ", "eagle")

# --------------------------------- 17. the winged Orphic egg + serpent
PB(24, 14, " ,==´ ", "egg")               # wings (the twins stand on them)
PB(24, 28, " `==, ", "egg")
PB(24, 21, " ,·:, ", "egg")
P(24, 25, "~o", "serpent")                # serpent head rising
PB(25, 19, " (:   :) ", "egg")
P(25, 22, "s~s", "serpent")
PB(26, 19, " (·   ·) ", "egg")
P(26, 21, "s~s", "serpent")
PB(27, 19, " `~,_,~´ ", "egg")

# ------------------------------------------- 18. concealed bow + sig
PB(30, 19, " c~=¡=~C ", "bow")
PB(31, 1, " aw ", "sig")

# ------------------------- 19. re-warm the glow around the figures
# (sprite halos punched the tent-interior glow; refill empty cells)
for r in range(17, 24):
    for c in range(19, 28):
        if canvas[r][c] == " " and hsh(r, c) < 72:
            P(r, c, "'·;'"[hsh(r, c) % 4], "field")
for r0, r1, c0, c1, cov in [(19, 23, 10, 15, 62), (19, 23, 31, 36, 62),
                            (24, 27, 10, 18, 58), (24, 27, 28, 36, 58)]:
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            if canvas[r][c] == " " and hsh(r, c) < cov:
                P(r, c, "·''·"[hsh(r, c) % 4], "field")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "06-lovers-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "06-lovers-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
