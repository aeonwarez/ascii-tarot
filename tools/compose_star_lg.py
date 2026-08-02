#!/usr/bin/env python3
"""Compositor for the large Star card per drafts/17-star-fable5-prompt.md.

v2 feedback applied: 47x32 locked canvas; globe is a FILLED dithered
sphere (light upper-left, dark lower-right limb), not an outline; rim
breaks behind every foreground element (halo clears); heptagrams have
true 7-point geometry (one ray straight up, none straight down); the
silver cup pours a dead-straight, unbroken 8-row rectilinear stream
while everything else in the frame curves.

Emits:
  drafts/17-star-art-lg.txt        47x32 art, full-bleed
  drafts/17-star-lg-classes.json   per-cell color classes (art coords)
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]


def P(r, c, s, cls):
    """Paint string s at (r, c); spaces are transparent."""
    for i, ch in enumerate(s):
        if ch != " " and 0 <= r < H and 0 <= c + i < W:
            canvas[r][c + i] = ch
            classes[r][c + i] = cls


def PB(r, c, s, cls):
    """Paint with background: spaces in s ERASE (halo built into sprite)."""
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


# ---- 1. background swirls + star field (corners, cosmic motion) ----
P(0, 30, "_,.--·--.,_", "sky")
P(1, 27, ",-´", "sky")
P(1, 41, "`-.,_", "sky")
P(2, 44, "`,", "sky")
P(13, 1, ")", "sky"); P(15, 0, "(", "sky")
P(20, 1, "`.", "sky"); P(22, 1, ",´", "sky")
P(0, 21, "+", "star"); P(2, 20, ".", "star"); P(3, 44, "·", "star")
P(8, 0, "·", "star"); P(14, 45, ".", "star"); P(24, 44, "·", "star")

# ---- 2. the celestial globe: FILLED dithered sphere, rows 6-24 ----
CX, CY, A, B = 27.0, 15.0, 19.0, 9.5
LR, LC = 9.0, 16.0          # light falls from the upper-left (star side)
for r in range(H):
    for c in range(W):
        dx, dy = (c - CX) / A, (r - CY) / B
        rr = dx * dx + dy * dy
        if rr > 1.0:
            continue
        d = math.hypot((c - LC) / (2 * A), (r - LR) / (2 * B)) * 2.0
        t = (r * 5 + c * 3) % 11 / 11.0        # ordered dither threshold
        # right-side directional shading only (the #5 dither, kept);
        # left/center stay open like the #4 hoop
        if d < 0.95:
            ch = " "
        elif d < 1.20:
            ch = "." if t < 0.40 else " "
        elif d < 1.50:
            ch = ":" if t < 0.45 else ("." if t < 0.80 else " ")
        else:
            ch = ";" if t < 0.50 else ":"
        if ch != " ":
            P(r, c, ch, "globe")
# rim: clean #4-style line hoop — top arc, ( column left, ) right
P(6, 19, "_,.--", "globe"); P(6, 30, "--.,_", "globe")
for r in range(7, 25):
    dy = (r - CY) / B
    s = 1 - dy * dy
    if s <= 0:
        continue
    x = A * math.sqrt(s)
    cl, cr = int(round(CX - x)), int(round(CX + x))
    if r <= 9:
        P(r, cr, "\\", "globe")
    elif r <= 20:
        P(r, cr, ")", "globe")
        if r >= 14:
            P(r, cr - 1, ";", "globe")
    else:
        P(r, cr, "/", "globe")
    if r >= 21:
        P(r, cl, "`", "globe")
    elif r >= 9:
        P(r, cl, "(", "globe")
# sparse lit-side dots inside the hoop, as in #4
for r, c in [(10, 11), (11, 10), (12, 12), (13, 10), (14, 11), (15, 10),
             (16, 11), (17, 12)]:
    P(r, c, "·", "globe")

# ---- 3. the great star, upper left (#4 design, kept per user) ----
P(0, 3, ",", "babalon"); P(0, 6, "\\ ' /", "babalon")
P(1, 2, "`.", "babalon"); P(1, 6, "\\|/", "babalon"); P(1, 11, ",´", "babalon")
P(2, 0, "·--=((o))=--·", "babalon")
P(3, 2, ",´", "babalon"); P(3, 6, "/ \\", "babalon"); P(3, 10, "`.", "babalon")
P(4, 1, "´", "babalon"); P(4, 5, "/", "babalon"); P(4, 9, "\\", "babalon")
P(5, 4, ",", "babalon"); P(5, 10, "`,", "babalon")

# ---- 4. second star whirling ON the globe (#4 design, ¡ accents),
#         rays centered true on the o ----
PB(10, 33, "   \\¡/   ", "babalon")
PB(11, 33, " ·-((o))-· ", "babalon")
PB(12, 33, "   /¡\\   ,", "babalon")
P(10, 40, "´", "babalon")            # CCW curl

# ---- 5. golden cup raised: a real chalice (rim/bowl/stem/foot) ----
CLEAR(3, 7, 24, 33)
P(3, 28, "___", "gold")
P(4, 27, "(o__)", "gold")
P(5, 28, "\\ /", "gold")
P(6, 28, "`-´", "gold")
P(4, 33, "x", "babalon"); P(5, 34, "´", "babalon")   # star-seed, CW tumble

# ---- 6. Nuith: back view, whirling S-curve, dropped one row so her
#         kneeling base sits IN the crystalline shore ----
CLEAR(9, 27, 14, 29)
FIGURE = """\
    ,~´`~,
   ´,cCCc.`,
    (((o)))
    ,`--´,)
   ´ ,´ ,´
   (  (  ´
   `.  `.
    )    `,
   (      )
    `,     )
   ,´)     `,
  (  (      )
  `,  `,    (
   )   )     )
  (   (     (
  `,´  `,    )
  ,´    ,)   (
 (    ,(´ ,   )
 (___,(´__,__,´_"""
PL(FIGURE, 9, 14, "nuith")
# raised arm to the gold chalice — light dotted #4 style
P(12, 26, "´", "nuith"); P(11, 27, "-", "nuith"); P(10, 28, "´", "nuith")
P(9, 29, "-", "nuith"); P(8, 30, "´", "nuith")
# spiral cascade spilling from the rim, ending just above her crown
P(5, 26, "(", "gold"); P(6, 25, ")", "gold"); P(7, 24, "(", "gold")
P(8, 23, ")", "gold")

# ---- 7. the shore: sea of Binah, pyramid city, crystalline earth ----
P(26, 1, ",^, /\\", "pyramid")
P(27, 0, "´  `´ `", "pyramid")
P(28, 13, "_,/\\._____,/\\,_____./\\,_,/\\._/\\,_", "crystal")
P(29, 13, "/:·\\/\\:/<:>\\:/·\\/\\::/<>\\/::\\/\\:/\\", "crystal")
P(30, 18, "\\/´`\\/;;\\/´‾\\/::\\/´`\\/;\\/`´\\", "crystal")
P(27, 31, "<>", "crystal")
P(28, 0, "~.~^~.~^~.~^~", "water")
P(29, 0, ".~^~.~^~.~^~.", "water")
P(30, 0, "~,^.~^~.~^~,.~^~.~", "water")
P(31, 0, "~.~^~ aw ~.~^~.~^~.~^~,.~^~.~^~.~^~,.~^~.~^~.", "water")
P(31, 6, "aw", "sig")

# ---- 8. silver cup + THE dead-straight rectilinear stream, painted
#         LAST so nothing interrupts it; it pours into the junction ----
PB(19, 6, " .--. ", "silver")
PB(20, 5, " ( ~~ ) ", "silver")
PB(21, 6, " `)(´ ", "silver")
PB(22, 7, " |¡| ", "silver")          # first drop sparkles, #4 flavor
for r in range(23, 30):
    PB(r, 7, " | | ", "silver")
# her other arm reaching down to the silver goblet (#4 style)
P(18, 15, "(", "nuith"); P(19, 13, ",´", "nuith"); P(20, 12, "´", "nuith")

# ---- 9. witnesses: three butterflies, clustered lower-right like the
#         painting (was a 5-high ladder — read as rain), + three roses ----
for r, c in [(16, 43), (22, 39), (24, 43)]:
    PB(r, c, " }v{ ", "fly")
P(26, 40, ",o,", "rose"); P(27, 43, ",o,", "rose"); P(27, 36, ",o,", "rose")

# ---- emit ----
art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "17-star-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "17-star-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
