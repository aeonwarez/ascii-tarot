#!/usr/bin/env python3
"""Compositor for Atu VIII Adjustment — candidate v3a (vesica-frame dominant),
per drafts/08-adjustment-fable5-prompt.md and the Harris scan.

Strategy A: the great DIAMOND/VESICA is the hero structure — clean mirrored
diagonals from the toe-point (bottom, col 23) up to the two scale pans and on
via the chains to the crown-tip (top, col 23), the masked figure balanced
inside it. Everything is a pure mirror about AXIS = 23; background noise,
lattice and curtain are generated from abs(c-23) so the mirror is exact.

Layers (back to front): chartreuse ground dither -> blue harlequin lattice ->
green leaf-diamonds -> feathered ray curtain -> up-spikes + throne shelf +
down-spikes -> corner orbs + spheres (blue top / green bottom exchange) ->
base dome -> lower vesica diagonals -> wings -> pans + glass bubbles
(alpha @ left, omega w right) -> chains (crown to pans) -> crown of Maat ->
robe + chequer -> mask/face/hands -> sword on col 23 (pommel O, grip, crescent
guard, blade, tip V on the dome).

Emits drafts/08-adjustment-v3a-art-lg.txt + drafts/08-adjustment-v3a-lg-classes.json
"""
import json
import os

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


SOFT = (None, "ground", "lattice", "harle", "rays")


def putM(r, c, ch, cls, over=SOFT):
    """Mirror-pair single cell, only over background classes."""
    for cc, g in ((c, ch), (46 - c, ch.translate(MIRROR))):
        if 0 <= r < H and 0 <= cc < W and classes[r][cc] in over:
            canvas[r][cc] = g
            classes[r][cc] = cls


# ---- 1. the chartreuse ground: a bright, exact, STILL weave -------------
for r in range(H):
    for c in range(W):
        canvas[r][c] = "\":"[(r + c) % 2]
        classes[r][c] = "ground"

# ---- 2. the fine blue harlequin diamond lattice (mirror-exact) ----------
for r in range(H):
    for c in range(W):
        d = c - 23
        a = (2 * r + d) % 6 == 0
        b = (2 * r - d) % 6 == 0
        if a and b:
            canvas[r][c] = "x"
            classes[r][c] = "lattice"
        elif a:
            canvas[r][c] = "\\"
            classes[r][c] = "lattice"
        elif b:
            canvas[r][c] = "/"
            classes[r][c] = "lattice"

# ---- 3. green harlequin leaf-diamonds, top band + bottom hints ----------
for r, c in [(0, 8), (0, 11), (0, 14), (0, 17), (0, 20), (1, 9), (1, 12),
             (1, 15), (1, 18), (2, 10), (2, 13), (2, 16)]:
    PM(r, c, "<>", "harle")
for r, c in [(30, 10), (31, 8)]:
    PM(r, c, "<>", "harle")

# ---- 4. the feathered curtain of rays, faint verticals at the sides ----
for c0 in (2, 5):
    for r in range(4, 28):
        if (r + c0) % 4 == 0:
            continue
        cc = c0 + (1 if (r // 3) % 2 else 0)
        ch = "'" if r % 2 else "|"
        putM(r, cc, ch, "rays")

# ---- 5. the throne: up-spikes (top), shelf + down-spikes (below pans) ---
PMB(6, 13, " ¡ ", "spike")
PMB(7, 12, " %%% ", "spike")
PMB(8, 12, " %%%% ", "spike")
PMB(9, 11, " %%%%% ", "spike")
PMB(10, 11, " %%%%%% ", "spike")
# shelf at pan level, behind the robe (robe drawn later on top)
PMB(15, 11, " %%%%%%%% ", "spike")
PMB(16, 12, " %%%%%%: ", "spike")
# great down-spikes converging inside the lower diamond, clear of the robe
PMB(17, 10, " %%%%%: ", "spike")
PMB(18, 11, " %%%%: ", "spike")
PMB(19, 11, " %%%%: ", "spike")
PMB(20, 12, " %%%: ", "spike")
PMB(21, 12, " %%%: ", "spike")
PMB(22, 13, " %%: ", "spike")
PMB(23, 13, " %%: ", "spike")
PMB(24, 14, " v: ", "spike")
PMB(25, 15, " v ", "spike")

# ---- 6. spheres of light and darkness: blue above, green below ---------
# top corner orbs (blue)
PM(0, 0, "%%%%%:,", "sphb")
PM(1, 0, "%%%%:,", "sphb")
PM(2, 0, "%%:,", "sphb")
PM(3, 0, "::", "sphb")
# top pair: light-blue outer sphere + dark-green sphere on the spike tip
PM(2, 6, ",·:,", "sphb")
PM(3, 5, "(·:%:)", "sphb")
PM(4, 6, "`·:´", "sphb")
PM(3, 13, ",:,", "sphg")
PM(4, 12, "(:%:)", "sphg")
PM(5, 13, "`:´", "sphg")
# bottom corner orbs (green)
PM(28, 0, "::", "sphg")
PM(29, 0, "%%:,", "sphg")
PM(30, 0, "%%%%:,", "sphg")
PM(31, 0, "%%%%%:,", "sphg")
# bottom pair: dark-green outer + light-blue inner (light/dark exchange)
PM(26, 7, ",:,", "sphg")
PM(27, 6, "(:%:)", "sphg")
PM(28, 7, "`:´", "sphg")
PM(28, 12, ",·,", "sphb")
PM(29, 11, "(·:·)", "sphb")
PM(30, 12, "`·´", "sphb")

# ---- 7. the dark base dome the whole equity rests on -------------------
PB(28, 19, " ,·:%:·, ", "sphg")
PB(29, 17, " ,:%%%%%%%:, ", "sphg")
PB(30, 15, " (%%%%%%%%%%%%%) ", "sphg")
PB(31, 14, " %%%%%%%%%%%%%%%%% ", "sphg")

# ---- 8. the great vesica, lower diagonals: pans down to the toe-point --
for rr in range(18, 28):
    cc = 8.0 + 15.0 * (rr - 18) / 9.0
    putM(rr, int(cc), "\\", "chains")
    if int(cc) + 1 <= 23:
        putM(rr, int(cc) + 1, "\\", "chains")

# ---- 9. the wing-fans: solid dithered fans radiating from the shoulders
WING_OVER = SOFT + ("spike",)
WING_SPANS = {9: (14, 18), 10: (13, 19), 11: (10, 19), 12: (9, 19),
              13: (10, 18), 14: (12, 18)}
for r, (c0, c1) in WING_SPANS.items():
    for c in range(c0, c1 + 1):
        if (r * 3 + c * 7) % 7 == 0:
            continue                       # ~14% holes keep it diaphanous
        dy = (r - 10.5) * 2.0
        dx = 20.0 - c
        slope = dy / max(dx, 0.5)
        if slope < -0.35:
            ch = "\\"
        elif slope < 0.30:
            ch = "‾"
        elif slope < 0.85:
            ch = "-"
        else:
            ch = "/"
        putM(r, c, ch, "wings", over=WING_OVER)

# ---- 10. the scale pans + glass bubbles (alpha left, omega right) ------
PMB(12, 3, " ,·‾‾·, ", "bubble")
PMB(13, 2, " (:·''·:) ", "bubble")
PMB(14, 2, " (·:··:·) ", "bubble")
PMB(15, 0, " <==========> ", "pan")
PMB(16, 1, " \\%%%%%%%%/ ", "pan")
PMB(17, 2, " `%%%%%%´ ", "pan")
PMB(18, 3, " `~%%~´ ", "pan")
P(13, 5, "@", "bubble")       # alpha, left pan
P(13, 41, "w", "bubble")      # omega, right pan

# ---- 11. the chains, crown down to the pan rims (upper vesica) ---------
CHAIN_OVER = SOFT + ("spike", "wings", "bubble")
for r, c in [(6, 17), (6, 16), (7, 15), (8, 14), (9, 13), (10, 12),
             (11, 11), (12, 10), (13, 9), (14, 8)]:
    putM(r, c, "s", "chains", over=CHAIN_OVER)
for r, c in [(6, 19), (7, 18), (8, 17), (9, 16), (10, 15), (11, 14),
             (12, 13), (13, 12), (14, 11)]:
    putM(r, c, "s", "chains", over=CHAIN_OVER)

# ---- 12. the crown of Maat: tip, finial, split disc, cone, ball --------
PB(2, 21, "  ¡  ", "crown")
PB(3, 21, " <%> ", "crown")
PB(4, 17, " (%%%:%:%%%) ", "crown")
PB(5, 16, " (%%%%:%:%%%%) ", "crown")
PB(6, 19, " \\%:¡:%/ ", "crown")
PB(7, 18, " /%=:¡:=%\\ ", "crown")
PB(8, 21, " ,O, ", "crown")

# ---- 13. mask, face, collar --------------------------------------------
PB(9, 20, " <x·x> ", "mask")
PB(10, 21, " \\·/ ", "skin")
PB(11, 20, " ,;·;, ", "robe")

# ---- 14. the robe: dithered green-gold, lit along the blade ------------
WIDTHS = {12: 7, 13: 7, 14: 7, 15: 5, 16: 7, 17: 9, 18: 11, 19: 11,
          20: 11, 21: 9, 22: 9, 23: 7, 24: 7, 25: 5, 26: 3}
for r, w in WIDTHS.items():
    half = w // 2
    body = ""
    for c in range(23 - half, 23 + half + 1):
        d = abs(c - 23)
        if d == half:
            body += "(" if c < 23 else ")"
        elif d <= 1:
            body += "'"                    # lit channel along the blade
        else:
            body += ";:%"[(d + r) % 3]
    PB(r, 23 - half - 1, " " + body + " ", "robe")
# the lit channel flanking the blade glows paler than the robe
for r in WIDTHS:
    for c in (22, 24):
        if classes[r][c] == "robe" and canvas[r][c] == "'":
            classes[r][c] = "figure"
# hem point
PB(26, 21, " \\;/ ", "robe")
# harlequin chequer hints on the leggings
for r, c in [(18, 20), (20, 21), (22, 21), (24, 22)]:
    P(r, c, "x", "harle")
    P(r, 46 - c, "x", "harle")

# ---- 15. hands gripping the hilt ---------------------------------------
PB(13, 20, " (m m) ", "skin")

# ---- 16. the sword: pommel, grip, crescent guard, blade, tip -----------
P(12, 23, "O", "sword")
P(13, 23, "|", "sword")
PB(14, 17, " o`=,_|_,=´o ", "sword")
for r in range(15, 27):
    P(r, 23, "|", "sword")
P(27, 23, "V", "sword")

# ---- 17. signature ------------------------------------------------------
P(31, 1, "aw", "sig")

# ---- sanity: shape, coverage, mirror ------------------------------------
for r in range(H):
    assert len(canvas[r]) == W
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
assert canvas[2][23] == "¡" and canvas[27][23] == "V", "axis endpoints"
EXEMPT = {(13, 5), (13, 41), (31, 1), (31, 2), (31, 44), (31, 45)}
bad = []
for r in range(H):
    for c in range(23):
        if (r, c) in EXEMPT or (r, 46 - c) in EXEMPT:
            continue
        lch, rch = canvas[r][c], canvas[r][46 - c]
        if rch != lch.translate(MIRROR):
            bad.append((r, c, lch, rch))
assert not bad, f"mirror broken at {bad[:8]}"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "08-adjustment-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "08-adjustment-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
