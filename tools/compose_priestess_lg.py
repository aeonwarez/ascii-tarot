#!/usr/bin/env python3
"""Compositor for Atu II The Priestess, per drafts/02-priestess-fable5-prompt.md
and the Harris scan: luminous moon-crowned goddess top center, arms sweeping
up into spiral curls, crystalline ray-veil fanning over the whole blue field,
crescent Moon-cup with scrolled ends across her lap, latticed legs dissolving
into the net, faint pillars, and a warm foreground: crystals + concave flower
+ pine cone (L), white camel dead center, grapes + spiral shell + pyramid +
dodecahedron (R).

Emits drafts/02-priestess-art-lg.txt + drafts/02-priestess-lg-classes.json
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


def line(r0, c0, r1, c1, cls, ch=None):
    """Straight ray with slope-appropriate glyphs."""
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        r = r0 + (r1 - r0) * i / steps
        c = c0 + (c1 - c0) * i / steps
        if ch:
            g = ch
        else:
            dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99
            g = "|" if abs(dc) < 0.35 else ("\\" if dc > 0 else "/")
        rr, cc = int(round(r)), int(round(c))
        if canvas[rr][cc] == " " if 0 <= rr < H and 0 <= cc < W else False:
            P(rr, cc, g, cls)


# ---- 1. the veil of light: rays fanning from behind her to the borders --
ORIG_R, ORIG_C = 7, 23
for endc in (0, 6, 12, 18, 28, 34, 40, 46):
    line(ORIG_R, ORIG_C, 22, endc, "veil")
for endr in (12, 17, 22):
    line(ORIG_R, ORIG_C, endr, 0, "veil")
    line(ORIG_R, ORIG_C, endr, 46, "veil")
# lattice sparkle where the net crosses, denser near her
for r in range(9, 22):
    for c in range(8, 39):
        if canvas[r][c] == " " and (r * 7 + c * 5) % 19 == 0:
            P(r, c, "x", "lattice")
for r, c in [(4, 3), (5, 43), (10, 2), (10, 44), (16, 1), (16, 45)]:
    P(r, c, "·", "veil")

# ---- 2. faint pillars, Mercy and Severity, spread by the veil ----
for r in range(6, 21, 2):
    PM(r, 1, "|", "pillar")
PM(5, 0, "==", "pillar")

# ---- 3. the goddess: crown, face, up-sweeping arms with spiral curls ----
PB(0, 21, ",-·-,", "crown")
PB(1, 19, " )(o)( ", "crown")
PB(2, 20, " \\¡/ ", "crown")
PB(3, 20, "(··) ", "figure")
PB(4, 20, " )( ", "figure")
# arms sweeping up and out, ending in spiral curls (mirrored)
PMB(2, 6, " ((c,_  ", "wings")
PMB(3, 8, " `-,_`--,_ ", "figure")
PMB(4, 11, " `--,_ ", "figure")
PMB(5, 14, " `-,_ ", "figure")
PB(5, 19, "(xx)", "figure")
PB(6, 18, "(x||x)", "figure")
PB(7, 18, "(x||x)", "figure")
PB(8, 19, ")xx(", "figure")
# ---- 4. the crescent Moon-cup / lyre across her lap, scrolled ends ----
PB(9, 13, " ,cC=~~~~~~~~~~~=Cc, ", "cup")
PB(10, 14, " `--,_________,--´ ", "cup")
# ---- 5. latticed legs kneeling, dissolving into the net ----
PMB(11, 17, " /x\\ ", "figure")
PMB(12, 16, " /xx\\ ", "figure")
PMB(13, 16, " |xx| ", "figure")
PMB(14, 15, " /xx| ", "figure")
PMB(15, 15, " |xx| ", "figure")
PMB(16, 15, " |xx| ", "figure")
PMB(17, 14, " /xx| ", "figure")
PMB(18, 14, " |xx| ", "figure")
PMB(19, 14, " |xx| ", "figure")
PB(20, 17, "(x´`x´`x)", "figure")
PB(21, 16, "(___,,___)", "figure")

# ---- 6. the foreground garden (asymmetric, per the painting) ----
# far left: great faceted crystals
P(23, 0, " ,<>,", "crystal")
P(24, 0, "/:<>:\\", "crystal")
P(25, 0, "\\::::/", "crystal")
P(26, 0, " `<>´", "crystal")
P(27, 0, ",<::>,", "crystal")
P(28, 0, "`<::>´", "crystal")
# concave flower + pine cone, left
P(24, 7, ",-(o)-,", "flower")
P(25, 6, "( (´`) )", "flower")
P(26, 7, "`-,__,-´", "flower")
P(27, 6, ",(:::),", "cone")
P(28, 6, "(:::::)", "cone")
P(29, 7, "`(:::)´", "cone")
# the white camel, dead center
PB(25, 18, "   _,^,_    ", "camel")
PB(26, 17, "  ,´(´ ), `, ", "camel")
PB(27, 17, " ( o)   `,  )", "camel")
PB(28, 18, "  ||   || ", "camel")
# grapes right of the camel
P(28, 28, ",o(o)o,", "grapes")
P(29, 29, "(o)o(o)", "grapes")
# the yellow spiral shell fan
P(23, 33, "__,,~-´", "shell")
P(24, 31, ",~´,~´´", "shell")
P(25, 30, "((*)´", "shell")
P(26, 30, " `~,`~,_", "shell")
# pyramid + dodecahedron, far right
P(23, 41, "/\\", "pyramid")
P(24, 40, "/::\\", "pyramid")
P(27, 41, ",<:>,", "crystal")
P(28, 41, "`<:>´", "crystal")
# ---- 7. signature ----
P(31, 2, "aw", "sig")

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "02-priestess-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "02-priestess-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
