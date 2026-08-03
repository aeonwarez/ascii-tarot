#!/usr/bin/env python3
"""Priestess v3b — panel composer B: FIGURE + CUP DOMINANT.

The enthroned goddess and the crescent Moon-cup are the hero: calm, frontal,
high on the axis, thick arms sweeping UP into spiral curls, tall moon-phase
crown of Isis, luminous latticed body/pedestal melting into the net below.
The veil is secondary texture: a filled blue field (never black emptiness)
with a white/cyan ray-web, teal swirl lobes above, teal floor wedges below.
Proportions follow the scan: face ~rows 2-5, cup at ~43%% height (r12-13),
pedestal to r21, garden r22-31 with the white camel dead center.

Emits:
  drafts/02-priestess-v3b-art-lg.txt       47x32 art
  drafts/02-priestess-v3b-lg-classes.json  per-cell classes
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
    """Place including spaces: spaces punch a breathing halo (occlusion)."""
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


# ================================================== 1. the filled field
# Deep blue ground, dense heavy dither (the veil IS the fill — no black
# holes). Teal wings-class zones: upper swirl lobes + lower floor wedges.
def in_lobe(r, c):
    for cx in (7.5, 38.5):
        dy = (r - 3.0) * 2.0
        dx = c - cx
        if (dx * dx) / 72.0 + (dy * dy) / 44.0 <= 1.0:
            return True
    return False


def in_floor(r, c):
    d = min(c, 46 - c)
    return r >= 21 and d < 14 and (21 + d * 0.55) < r + 3.5


for r in range(H):
    for c in range(W):
        h = (r * 37 + c * 61 + (r * c) % 17) % 100
        if in_lobe(r, c):
            if h < 76:
                P(r, c, ";;:·"[h % 4], "wings")
        elif in_floor(r, c):
            if h < 80:
                P(r, c, ";;:,"[h % 4], "wings")
        else:
            if h < 92:
                P(r, c, ";;::·"[h % 5], "field")

# ================================================== 2. faint pillars
for r in range(6, 22):
    PM(r, 1, "|", "pillar")
    if r % 2 == 0:
        PM(r, 2, "|", "pillar")

# ================================================== 3. the ray-web veil
def ray(r0, c0, r1, c1, cls):
    steps = max(abs(r1 - r0), abs(c1 - c0), 1)
    for i in range(steps + 1):
        rr = int(round(r0 + (r1 - r0) * i / steps))
        cc = int(round(c0 + (c1 - c0) * i / steps))
        if not (0 <= rr < H and 0 <= cc < W):
            continue
        dc = (c1 - c0) / (r1 - r0) if r1 != r0 else 99
        g = "|" if abs(dc) < 0.4 else ("\\" if dc > 0 else "/")
        cur, cl = canvas[rr][cc], classes[rr][cc]
        if cur == " " or cl in ("field", "wings"):
            P(rr, cc, g, cls)
        elif cur in "\\/|" and cur != g and cl in ("veil", "lattice"):
            P(rr, cc, "x", "lattice")


# lower fan: rays stream from behind the cup scrolls down to the borders
for endc in (0, 6, 12):
    ray(12, 20, 31, endc, "veil")
    ray(12, 26, 31, 46 - endc, "veil")
for endr in (16, 22, 28):
    ray(12, 18, endr, 0, "veil")
    ray(12, 28, endr, 46, "veil")
# crossing family from the scroll tips, down-inward: diamonds where they cut
ray(13, 8, 31, 18, "lattice")
ray(13, 38, 31, 28, "lattice")
ray(13, 8, 27, 13, "lattice")
ray(13, 38, 27, 33, "lattice")
ray(10, 4, 20, 12, "lattice")
ray(10, 42, 20, 34, "lattice")
ray(16, 2, 28, 14, "lattice")
ray(16, 44, 28, 32, "lattice")
# upper fan: rays from the crown up and out
for endc in (3, 9, 37, 43):
    ray(2, 23, 0, endc, "veil")
ray(3, 21, 6, 0, "veil")
ray(3, 25, 6, 46, "veil")
# net streaming from her hands down into the cup bowl (punched by figure)
ray(5, 10, 11, 15, "lattice")
ray(6, 13, 11, 18, "lattice")
ray(5, 36, 11, 31, "lattice")
ray(6, 33, 11, 28, "lattice")
# tight sparkle mesh close around her (density high near, open far)
for r in range(6, 14):
    for c in range(12, 35):
        if canvas[r][c] == " " or classes[r][c] == "field":
            if (r * 13 + c * 11) % 7 == 0:
                P(r, c, "x" if (r + c) % 2 else "·", "lattice")
# star-points caught at web intersections
for r, c in [(15, 7), (15, 39), (19, 4), (19, 42), (17, 12), (17, 34),
             (23, 15), (23, 31), (1, 7), (1, 39)]:
    if classes[r][c] in ("veil", "lattice", "field", "wings", None):
        P(r, c, "*", "veil")

# ================================================== 4. teal sweep arcs
# bold swirl edges over the lobes (after the rays so they stay unbroken)
PM(0, 3, "_,~~~-,_", "wings")
PM(1, 2, ",´", "wings")
PM(1, 10, "`-,_", "wings")
PM(2, 1, "/", "wings")
PM(2, 13, "`,", "wings")
PM(3, 0, "(", "wings")
PM(4, 0, "(", "wings")
PM(5, 1, "\\", "wings")
PM(6, 2, "`-,_", "wings")
PM(7, 4, "`~-,_", "wings")

# ================================================== 5. the goddess
# full-moon glow behind her head (the face punches a tight halo into it)
for r in range(1, 6):
    for c in range(14, 33):
        dy, dx = (r - 3.0) * 2.2, c - 23.0
        if dx * dx / 68.0 + dy * dy / 30.0 <= 1.0:
            if (r * 5 + c * 3) % 4 != 0:
                P(r, c, "'", "veil")
# tall crown of Isis: waxing ) full O waning ( over plume rays, gold-green
PB(0, 17, "  \\ )(O)( /  ", "crown")
PB(1, 18, "  \\¡ | ¡/  ", "crown")
# face: calm, frontal, luminous
PB(2, 19, "  ,´‾`,  ", "figure")
PB(3, 19, "  (· ·)  ", "figure")
PB(4, 19, "  `,_,´  ", "figure")
# torso: pale luminous lattice, calm even column, shoulders to hips
PB(5, 18, "  _(`:´)_  ", "figure")
PB(6, 18, "  (x`:´x)  ", "figure")
PB(7, 18, "  (x:::x)  ", "figure")
PB(8, 18, "  )x`:´x(  ", "figure")
PB(9, 18, "  (x-:-x)  ", "figure")
PB(10, 18, "  )x`:´x(  ", "figure")
PB(11, 18, " ,(x-:-x), ", "figure")
# thick arms sweeping UP and OUT of the shoulders (chained diagonal
# segments, drawn after the torso), hands ending in spiral curls
PM(6, 15, "`==-,", "figure")
PM(5, 12, "`===,_", "figure")
PM(4, 10, "`-,_", "figure")
PMB(4, 5, " ((c´", "crown")
# ================================================== 6. the Moon-cup
# one wide crescent across her lap: scrolled ends high, belly low
PB(12, 6, "  ,cC=~-,_               _,-~=Cc,  ", "cup")
PB(13, 12, "  `--,_____________,--´  ", "cup")
# the hidden Book of Mysteries, barely a mark under the lyre
P(14, 22, "[=]", "cup")

# ================================================== 7. latticed pedestal
# luminous draped mass melting down into the net: dense xX mesh + fold
# lines, holes opening at the hem (no hard hemline)
for r in range(14, 22):
    half = 4.5 + (r - 14) * 0.55
    lo, hi = int(round(AXIS - half)), int(round(AXIS + half))
    for c in range(lo, hi + 1):
        hh = (r * 31 + c * 7) % 10
        if r >= 20 and abs(c - 23) > 3 and hh < 4:
            continue                       # the melt: net shows through
        if c == lo:
            g = "/"
        elif c == hi:
            g = "\\"
        elif c in (19, 23, 27):
            g = "|"
        else:
            g = "x" if (r + c) % 2 == 0 else "X"
        P(r, c, g, "figure" if r < 20 else "lattice")
P(14, 22, "[=]", "cup")                    # book sits on the drape
# inverted crescent on the throne base + pale feet below
P(21, 21, "\\,_,/", "cup")
PMB(22, 18, "  (´) ", "figure")

# ================================================== 8. foreground garden
# far left: great faceted crystals
P(23, 0, " ,<>,", "crystal")
P(24, 0, "/:<>:\\", "crystal")
P(25, 0, "\\::::/", "crystal")
P(26, 0, " `<>´", "crystal")
P(28, 0, ",<::>,", "crystal")
P(29, 0, "`<::>´", "crystal")
# concave-petal flower (receptive), left — large
PB(24, 5, " _,-(o)-,_ ", "flower")
PB(25, 4, " ( ( ´` ) ) ", "flower")
PB(26, 4, " (`-,__,-´) ", "flower")
PB(27, 5, " `-,____,-´ ", "flower")
# green pine cone below it
PB(28, 6, " ,(:::), ", "cone")
PB(29, 6, " (:::::) ", "cone")
PB(30, 7, " `(:)´ ", "cone")
# the white camel, DEAD CENTER (leg midpoint = col 23)
PB(24, 15, "  (´),         ", "camel")
PB(25, 16, "  `-,__,^,_   ", "camel")
PB(26, 16, "  (;;;;;;;;;)  ", "camel")
PB(27, 17, "  |(     )|  ", "camel")
PB(28, 17, "  UU     UU  ", "camel")
# purple grapes, right of the camel
PB(28, 30, " ,o(o)o, ", "grapes")
PB(29, 30, " (o)o(o) ", "grapes")
PB(30, 31, " `o´o´ ", "grapes")
# the yellow ten-petal spiral shell (force), right — large fan
PB(22, 36, " __,,-´ ", "shell")
PB(23, 33, " _,,-´,-´ ", "shell")
PB(24, 31, " _,-´((@) ", "shell")
PB(25, 31, " `~,_`~,_ ", "shell")
PB(26, 33, " `~,_`~, ", "shell")
PB(27, 36, " `~,_ ", "shell")
# rose pyramid, upper right of the garden
PB(22, 42, " /\\ ", "pyramid")
PB(23, 41, " /::\\ ", "pyramid")
# faceted crystal, far right
P(28, 41, ",<::>,", "crystal")
P(29, 41, "(::::)", "crystal")
P(30, 41, "`<::>´", "crystal")

# ================================================== 9. signature
P(31, 2, "aw", "sig")

# ================================================== sanity + emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "02-priestess-v3b-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "02-priestess-v3b-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
