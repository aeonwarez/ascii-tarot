#!/usr/bin/env python3
"""Atu VI The Lovers -- panel candidate v3c (shrine-frame dominant).

The whole card is the wedding shrine: rainbow-striped arch bands + the arch
of swords overhead converging on the Kether apex, dark tree trunks at the
edges, blindfold golden Cupid aiming his arrow down the axis, pale Lilith UL
and praying Eve UR framing a smaller central marriage -- the great mauve
hood-arch officiant with hands out over the couple, dark King (gold crown)
and pale Queen (silver crown) with inner hands joined on col 23, the
counterchanged twins exchanging grail + lance-of-arrows, red lion left,
white eagle right, the serpent-coiled winged egg on the red dais.

Emits:
  drafts/06-lovers-v3c-art-lg.txt       47x32 art, full-bleed
  drafts/06-lovers-v3c-lg-classes.json  per-cell color classes
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


# ------------------------------------------------------------- background
# Chevron fan of rainbow bands converging on a virtual apex above the top
# rule (the shrine), dark trunks at the hard edges, warm gold field below,
# red carpet dais across the bottom. Cell aspect 1:2 baked into the slope.
def put(r, c, ch, cls):
    canvas[r][c] = ch
    classes[r][c] = cls


for r in range(H):
    for c in range(W):
        h = (r * 43 + c * 19 + (r * c) % 11) % 100
        if r >= 28:                                   # red carpet / dais
            put(r, c, "=~-·~"[(c + r * 3) % 5], "carpet")
            continue
        edge_trunk = ((c <= 2 or c >= 44) and r <= 12) or \
                     ((c <= 1 or c >= 45) and r <= 19)
        u = (r + 7.0) - abs(c - AXIS) / 1.4
        if r <= 9:                                    # the shrine fan
            if u < -6.0 or edge_trunk:                # dark trunks
                if h < 93:
                    put(r, c, "||;!|;:|"[h % 8], "trunks")
                continue
            t = (u + 40.0) % 3.0
            k = int((u + 40.0) // 3.0)
            if k % 2 == 0:                            # red-orange band
                if t < 0.55:
                    put(r, c, "/" if c < 23 else ("\\" if c > 23 else "!"),
                        "bands")
                elif h < 92:
                    put(r, c, ";;:;"[h % 4], "bands")
            else:                                     # gold gap stripe
                if h < 72:
                    put(r, c, "':;·"[h % 4], "field")
            continue
        if edge_trunk:
            if h < 93:
                put(r, c, "||;!|;:|"[h % 8], "trunks")
            continue
        if h < 72:                                    # warm gold field
            put(r, c, "·:';"[h % 4], "field")


def line(r0, c0, r1, c1, cls, only_field=False):
    steps = max(abs(r1 - r0), abs(c1 - c0))
    for i in range(steps + 1):
        rr = int(round(r0 + (r1 - r0) * i / steps))
        cc = int(round(c0 + (c1 - c0) * i / steps))
        if not (0 <= rr < H and 0 <= cc < W):
            continue
        if only_field and classes[rr][cc] not in ("field", None):
            continue
        dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99
        g = "|" if abs(dc) < 0.35 else ("\\" if dc > 0 else "/")
        put(rr, cc, g, cls)


# silver rays fanning down from under the hood (the veil light)
for endr, endc in ((28, 7), (28, 15), (26, 1), (28, 39), (28, 31), (26, 45)):
    line(11, 23, endr, endc, "rays", only_field=True)

# ------------------------------------------------- the arch of swords (Zain)
# steel blades riding the gold gap stripes of the fan, tips toward the apex
for (r0, c0, r1, c1) in ((8, 3, 1, 13), (9, 9, 3, 17),
                         (8, 43, 1, 33), (9, 37, 3, 29)):
    line(r0, c0, r1, c1, "silver")
P(0, 14, "'", "silver")
P(0, 32, "'", "silver")

# ------------------------------------------------- tent + veil (Kether light)
PB(6, 19, " /:':':\\ ", "tent"); P(6, 23, "*", "rays")
P(5, 21, "·", "rays"); P(5, 25, "·", "rays")
# the veil hanging under the hood, silver-striped, down to the grail
PB(11, 17, " |':':':':'| ", "tent")
P(11, 20, "¡", "rays"); P(11, 23, "¡", "rays"); P(11, 26, "¡", "rays")
PB(12, 17, " |':':':':'| ", "tent")
P(12, 20, "¡", "rays"); P(12, 23, "¡", "rays"); P(12, 26, "¡", "rays")
PB(13, 20, " )':'( ", "tent")
PB(14, 19, " |':':'| ", "tent")
PB(15, 19, " |':':'| ", "tent")
P(14, 23, "¡", "rays"); P(15, 23, "¡", "rays")

# ------------------------------------------------- the great mauve hood-arch
HOOD = {7: (12, 34), 8: (7, 39), 9: (5, 41), 10: (6, 40)}
for r, (a, b) in HOOD.items():
    for c in range(a, b + 1):
        h = (r * 43 + c * 19 + (r * c) % 11) % 100
        if c == a:
            put(r, c, "(", "hood")
        elif c == b:
            put(r, c, ")", "hood")
        elif h < 96:
            put(r, c, ";;:;;·;;"[h % 8], "hood")
        else:
            put(r, c, " ", None)
            classes[r][c] = None
# the officiant's hands, out over the couple (Sign of the Enterer)
PMB(8, 2, " <;===,_ ", "statue")

# ------------------------------------------------- Cupid, blindfold, gold
PB(1, 17, " _,&w", "bow")
PB(1, 22, "(=)", "cupid")
PB(1, 25, "w&,_ ", "bow")
PB(2, 19, " c(;=;)C ", "cupid")
P(2, 27, "%", "bow")                       # quiver, THELEMA implied
PB(3, 18, " `=,_¡_,=´ ", "bow")           # the bow, drawn
P(4, 23, "¡", "silver")                    # the arrow, straight down
P(5, 23, "v", "silver")

# ------------------------------------------------- Lilith UL / Eve UR
PB(1, 0, " ,o, ", "statue")
PB(2, 0, " );( ", "statue")
PB(3, 0, " (;) ", "statue")
PB(4, 0, " ¡;¡ ", "statue")
PB(5, 0, " [_] ", "statue")
PB(1, 42, " ,o, ", "statue")
PB(2, 42, " )¡( ", "statue")               # praying hands
PB(3, 42, " (:) ", "statue")
PB(4, 42, " ¡:¡ ", "statue")
PB(5, 42, " [_] ", "statue")
P(0, 44, "s", "serpent")                   # the serpent behind Eve

# ------------------------------------------------- the dark King (left)
PB(10, 9, " ¡ ¡ ¡ ", "crown")
PB(11, 9, " (===) ", "crown")
PB(12, 9, " (&&&) ", "king")
PB(13, 7, " ,==", "ermine"); P(13, 11, "&&&", "king"); PB(13, 14, "==, ", "ermine")
PB(14, 7, " ('v':'v') ", "ermine")
PB(15, 6, " ('v':v':v') ", "ermine")
PB(16, 6, " (':v'v':v:) ", "ermine")
# ------------------------------------------------- the pale Queen (right)
PB(10, 32, " '·' ", "silver")
PB(11, 31, " ,(¡), ", "silver")
PB(12, 31, " (';') ", "queen")
PB(13, 29, " ,==", "ermine"); P(13, 33, ":':", "queen"); PB(13, 36, "==, ", "ermine")
PB(14, 29, " ('v':'v') ", "ermine")
PB(15, 28, " ('v':v':v') ", "ermine")
PB(16, 28, " (':v'v':v:) ", "ermine")
# robes, flaring to the dais (serpent-and-bee motifs in the weave)
for i, r in enumerate(range(17, 26)):
    half = min(4 + (i + 1) // 2, 7)
    for center, cls, ramp in ((12, "robek", ";e;s;;:;"), (34, "robeq", ";s;:e;;;")):
        a, b = center - half, center + half
        for c in range(a, b + 1):
            h = (r * 37 + c * 29) % 100
            if c == a:
                put(r, c, "(", cls)
            elif c == b:
                put(r, c, ")", cls)
            elif h < 90:
                put(r, c, ramp[h % 8], cls)

# inner hands joined across the axis, under the officiant
P(14, 17, "_,", "king")
P(13, 19, ",=´", "king")
P(13, 22, "&", "king")
P(13, 23, "¡", "crown")
P(13, 24, "o", "queen")
P(13, 25, "`=,", "queen")
P(14, 28, ",_", "queen")

# ------------------------------------------------- grail + lance-of-arrows
PB(16, 20, " \\¡|¡/ ", "lance")
PB(17, 21, " \\¡/ ", "lance")
PB(18, 20, " (:¡:) ", "grail")
PB(19, 21, " \\_/ ", "grail")
P(20, 23, "¡", "grail")

# ------------------------------------------------- the counterchanged twins
# white child (by the dark King), roses
PB(18, 15, " ,o, ", "childw")
PB(19, 15, " (') ", "childw"); P(19, 19, "=´", "childw")
PB(20, 15, " |'| ", "childw")
PB(21, 15, " |'| ", "childw")
PB(22, 15, " /'\\ ", "childw")
PB(23, 14, " ´¡ ¡` ", "childw")
PB(21, 12, " ,*, ", "ermine")              # white roses
PB(22, 11, " ,*'*, ", "ermine")
# black child (by the white Queen), club
PB(18, 28, " ,&, ", "childb")
P(19, 26, "`=", "childb"); PB(19, 28, " (&) ", "childb")
PB(20, 28, " |&| ", "childb")
PB(21, 28, " |&| ", "childb")
PB(22, 28, " /&\\ ", "childb")
PB(23, 27, " ´¡ ¡` ", "childb")
P(20, 33, "!", "childb")                   # the club
P(21, 33, "!", "childb")
P(22, 33, "O", "childb")

# ------------------------------------------------- red lion / white eagle
P(20, 1, "c,", "lion")                     # tail
PB(21, 1, " ,;&&;, ", "lion")
PB(22, 0, ";&&&&&(o´, ", "lion")
PB(23, 0, ";&&&&&&&=< ", "lion")
PB(24, 0, "(;&&&&&;) ", "lion")
PB(25, 0, "(;&&&&;;) ", "lion")
PB(26, 0, ");&&&&;( ", "lion")
PB(27, 0, ",U;&&;U, ", "lion")

PB(21, 40, " ,^', ", "eagle")
PB(22, 38, " <(o', ", "eagle")
PB(23, 39, " );'':( ", "eagle")
PB(24, 38, " (':':':) ", "eagle")
PB(25, 38, " (':':':) ", "eagle")
PB(26, 39, " )':':( ", "eagle")
PB(27, 39, " ,U,U, ", "eagle")

# ------------------------------------------------- the winged Orphic egg
PB(25, 17, " <==,':·:',==> ", "egg")
PB(26, 17, " (':::::::') ", "egg")
PB(27, 18, " (':::::') ", "egg")
PB(28, 19, " `':::'´ ", "egg")
P(26, 20, "s", "serpent"); P(26, 25, "S", "serpent")
P(27, 22, "S", "serpent"); P(27, 25, "s", "serpent")
PB(24, 24, " ,s´ ", "serpent")             # the serpent's head, rising
# the concealed bow, laid on the dais
P(30, 21, "`==´", "bow")

# ------------------------------------------------- signature
P(31, 2, "aw", "sig")

# ------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "06-lovers-v3c-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "06-lovers-v3c-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
