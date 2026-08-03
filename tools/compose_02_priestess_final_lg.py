#!/usr/bin/env python3
"""Priestess FINAL — ultracode panel synthesis (judge tally v3a 8 · v3b 6 · v3c 4).

BASE (v3a): the full-bleed translucent LIGHT-WEB — procedural polar net
(radial rays + concentric arc rings crossing into diamonds) with density
graded bright-near-figure to open-dot-fade corners, over a deep blue/teal
field with no black voids; net converges into the cup scrolls; [=] Book of
Mysteries. FIX: every dither/zone decision keys on |c-23| (folded angle) so
the background noise mirrors — v3a's rows 11-14 asymmetry is gone.
GRAFT 1 (v3b): the SOLID figure stack — crown + calm face rows, (x`:´x)/
(x:::x)/(x-:-x) torso column, thick upswept arms, dense pleated |xXx|XxX|
throne-skirt melting into the net at the hem, explicit white camel (hump on
col 23, legs, UU feet). All halo-punched; no ray slices her.
GRAFT 2 (v3c): the long GOLD crescent cup ,c@C==~~...~~==C@c, (cup class);
mirrored ((@) corner swirls at the arm-end glows (gold @ eyes); pillar
capitals T== / ==T with faint shaft hints threaded INTO the veil.
KEEP: Crown of Isis + gold-green glow, full-moon disk behind the head,
star-points in the net, inverted crescent on the throne base, full garden
register (flower L, cone, grapes, camel DEAD CENTER, spiral shell R with @
eye, rose pyramid, faceted crystals), 'aw' signature.

Emits:
  drafts/02-priestess-final-art-lg.txt       47x32 art
  drafts/02-priestess-final-lg-classes.json  per-cell classes
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


def put_empty(r, c, ch, cls):
    if 0 <= r < H and 0 <= c < W and canvas[r][c] == " ":
        canvas[r][c] = ch
        classes[r][c] = cls


def CLR(r, c):
    if 0 <= r < H and 0 <= c < W:
        canvas[r][c] = " "
        classes[r][c] = None


# ---- the net's polar frame: origin behind her lap (the cup line) --------
OR_, OC_ = 12.0, 23.0


def polar(r, c):
    """Signed angle (glyph choice only — mirrors to the mirrored glyph)."""
    du = (c - OC_) * 0.5              # visual x in row units (cells are 1:2)
    dv = r - OR_
    return math.hypot(du, dv), math.degrees(math.atan2(dv, du))


def polar_fold(r, c):
    """Folded |c-23| angle in [-90, 90]: ALL zone/dither decisions key on
    this so left and right noise mirror exactly (the v3a fix)."""
    du = abs(c - OC_) * 0.5
    dv = r - OR_
    return math.hypot(du, dv), math.degrees(math.atan2(dv, du))


# ---- 1. pillar shafts first: faint hints, half-lost under the webbing ---
for r in range(2, 22):
    if r % 4:
        PM(r, 0, "|:", "pillar")

# ---- 2. the veil: straight rays fanning from the cup-line origin --------
RAY_ANGLES = list(range(0, 181, 10)) + [-45, -60, -75, -90, -105, -120, -135]
for a in RAY_ANGLES:
    th = math.radians(a)
    sl = 0.5 * math.tan(th) if abs(math.cos(th)) > 1e-6 else 99.0
    if abs(sl) < 0.38:
        g = "-"
    elif abs(sl) > 2.8:
        g = "|"
    else:
        g = "\\" if sl > 0 else "/"
    R = 3.0
    while R < 24.0:
        dash = int(R * 2.5) % 2 if (abs(sl) < 0.38 or R > 19.0) else 0
        if not dash:
            rr = int(round(OR_ + R * math.sin(th)))
            cc = int(round(OC_ + 2.0 * R * math.cos(th)))
            if rr < 22:                    # the garden band stays net-free
                put_empty(rr, cc, g, "veil" if R < 9.0 else "lattice")
        R += 0.4

# ---- 3. concentric arc rings crossing the rays into diamonds ------------
RINGS = [3.5, 5.0, 6.5, 8.0, 9.75, 11.5, 13.5, 15.75, 18.0, 20.5, 23.0]
for r in range(22):
    for c in range(W):
        R, am = polar_fold(r, c)
        if am < -20:                       # zone test on the FOLDED angle
            continue
        for ki, Rk in enumerate(RINGS):
            if abs(R - Rk) >= 0.30:
                continue
            if Rk > 16.0 and (r * 2 + abs(c - 23)) % 2:   # dash outer rings
                continue
            _, a = polar(r, c)             # signed: glyph choice only
            th = math.radians(a)
            sl = -0.5 / math.tan(th) if abs(math.sin(th)) > 1e-6 else 99.0
            if abs(sl) < 0.38:
                g = "_" if a > 0 else "-"
            elif abs(sl) > 2.8:
                g = "(" if math.cos(th) < 0 else ")"
            else:
                g = "\\" if sl > 0 else "/"
            put_empty(r, c, g, "veil" if Rk < 9.0 else "lattice")
            break

# ---- 4. star-points caught in the net's intersections -------------------
for ki, Rk in enumerate(RINGS):
    for a in RAY_ANGLES:
        fam = round(min(abs(a), 180 - abs(a)) / 10)
        if (ki + fam) % 3:
            continue
        th = math.radians(a)
        rr = int(round(OR_ + Rk * math.sin(th)))
        cc = int(round(OC_ + 2.0 * Rk * math.cos(th)))
        if Rk > 4.5 and 0 <= rr < 22 and 0 <= cc < W:
            P(rr, cc, "*", "veil")

# ---- 5. between the net: blue field + alternating teal wedges -----------
# every hash and every zone keys on d = |c-23| / the folded angle: the
# dither mirrors exactly. No region reads as black emptiness.
for r in range(H):
    for c in range(W):
        if canvas[r][c] != " ":
            continue
        d = abs(c - 23)
        R, am = polar_fold(r, c)
        h = (r * 31 + d * 17 + (r * d) % 7) % 100
        if r >= 22:                        # quiet indigo ground of the garden
            if h < 88:
                put_empty(r, c, ":;·:"[h % 4], "field")
            continue
        cov = 96 if R < 6 else (90 if R < 11 else (84 if R < 17 else 76))
        if am < -20 and R > 5.5:
            cov = min(cov + 8, 99)         # the top sweeps are a dense mass
        if h >= cov:
            continue
        if am > 0 and 8 <= am <= 70:
            cls = "wings" if int((am + 4) / 12) % 2 == 0 else "field"
        elif -62 <= am < -20:
            cls = "wings"
        else:
            cls = "field"
        ramp = ";·;," if cls == "wings" else ":;;:"
        put_empty(r, c, ramp[h % len(ramp)], cls)

# ---- 6. full-moon disk behind the head (the face punches into it) -------
for r in range(1, 6):
    for c in range(14, 33):
        dy, dx = (r - 3.0) * 2.2, c - 23.0
        if dx * dx / 68.0 + dy * dy / 30.0 <= 1.0:
            if (r * 5 + abs(c - 23) * 3) % 4 != 0:
                P(r, c, "'", "veil")

# ---- 7. the warm gold-green glow rimming head + crown -------------------
for r in range(0, 7):
    for c in range(12, 35):
        Rh = math.hypot((c - 23) * 0.5, r - 2.5)
        if 2.3 <= Rh <= 4.6 and (r * 11 + abs(c - 23) * 5) % 3:
            P(r, c, "'" if Rh < 3.5 else "·", "crown")

# ---- 8. teal wing sweeps, bold bands over the net -----------------------
PM(0, 2, "_,--~~´", "wings")
PM(1, 0, ",-´_,-~´", "wings")
PM(2, 0, "/,-´", "wings")
PM(3, 0, "(´", "wings")
PM(4, 0, "\\`,", "wings")
PM(5, 1, "`-,_", "wings")
PM(6, 3, "`-,_", "wings")
PM(7, 6, "`--,_", "wings")
PM(8, 10, "`--,_", "wings")

# ---- 9. pillar capitals set into the top corners (over the sweeps) ------
PM(0, 0, "T==", "pillar")

# ---- 10. mirrored corner swirls at the arm-end glows, gold @ eyes -------
PMB(2, 4, " ,--, ", "wings")
PMB(3, 3, " ((@), ", "wings")
PMB(4, 4, " `-´, ", "wings")
PM(3, 6, "@", "crown")

# ---- 11. the goddess: crown, calm face, solid latticed torso ------------
PB(0, 17, "  \\ )(O)( /  ", "crown")
PB(1, 18, "  \\¡ | ¡/  ", "crown")
PB(2, 19, "  ,´‾`,  ", "figure")
PB(3, 19, "  (· ·)  ", "figure")
PB(4, 19, "  `,_,´  ", "figure")
PB(5, 18, "  _(`:´)_  ", "figure")
PB(6, 18, "  (x`:´x)  ", "figure")
PB(7, 18, "  (x:::x)  ", "figure")
PB(8, 18, "  )x`:´x(  ", "figure")
PB(9, 18, "  (x-:-x)  ", "figure")
PB(10, 18, "  )x`:´x(  ", "figure")
PB(11, 18, " ,(x-:-x), ", "figure")

# ---- 12. thick arms sweeping UP and OUT to the swirls, halo-punched -----
for r0, c0, c1 in ((5, 15, 19), (4, 12, 17), (3, 10, 13)):
    for c in range(c0, c1 + 1):            # breathing halo above each stroke
        CLR(r0, c)                         # (punch FIRST — strokes re-cover
        CLR(r0, 46 - c)                    #  their own cells below)
PM(6, 15, "`==-,", "figure")
PM(5, 12, "`===,_", "figure")
PM(4, 10, "`-,_", "figure")

# ---- 13. the long GOLD crescent Moon-cup, scrolled @ ends, the Book -----
cup = ",c@C==" + "~" * 23 + "==C@c,"
PB(12, 23 - len(cup) // 2 - 1, " " + cup + " ", "cup")
und = "`--,________" + "[=]" + "________,--´"
PB(13, 23 - len(und) // 2 - 1, " " + und + " ", "cup")

# ---- 14. dense pleated throne-skirt, melting into the net at the hem ----
for r in range(14, 22):
    half = 4.5 + (r - 14) * 0.55
    lo, hi = int(round(AXIS - half)), int(round(AXIS + half))
    if r < 20:
        CLR(r, lo - 1)                     # halo just outside the drape
        CLR(r, hi + 1)
    for c in range(lo, hi + 1):
        hh = (r * 31 + abs(c - 23) * 7) % 10
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
        canvas[r][c] = g
        classes[r][c] = "figure" if r < 20 else "lattice"
# inverted crescent on the throne base (the subconscious)
PB(20, 20, " ´‾‾‾` ", "cup")

# ---- 15. the foreground garden ------------------------------------------
# far left: great icosahedral crystal
PB(22, 0, ",-<>-, ", "crystal")
PB(23, 0, "/:<>::\\ ", "crystal")
PB(24, 0, "\\::<>:/ ", "crystal")
PB(25, 0, "`,<>,´ ", "crystal")
PB(26, 0, " `<>´ ", "crystal")
P(27, 0, ",<>,", "crystal")
P(28, 0, "<::>", "crystal")
P(29, 0, "`<>´", "crystal")
# concave-petal flower, LEFT (receptive / Binah)
PB(22, 6, " _,---,_ ", "flower")
PB(23, 4, " ,´((´`))`, ", "flower")
PB(24, 3, " ( ((´¡`)) ) ", "flower")
PB(25, 4, " `,((_,_)),´ ", "flower")
PB(26, 6, " `-,_,-´ ", "flower")
# green pine cone below the flower
PB(27, 5, " ,(%), ", "cone")
PB(28, 4, " ((%%%)) ", "cone")
PB(29, 4, " ((%%%)) ", "cone")
PB(30, 5, " `(%)´ ", "cone")
# the WHITE camel, DEAD CENTER: hump apex on col 23, legs, UU feet
PB(23, 15, "  (´),  ", "camel")
PB(24, 15, "  `-,__,^,__  ", "camel")
PB(25, 17, "  (:::::::)  ", "camel")
PB(26, 18, "  ||   ||  ", "camel")
PB(27, 18, "  UU   UU  ", "camel")
# purple grapes right of the camel
PB(27, 27, " ,o,o,o, ", "grapes")
PB(28, 26, " (o,o,o,o) ", "grapes")
PB(29, 27, " (o,o,o) ", "grapes")
PB(30, 28, " `o,o´ ", "grapes")
# the yellow spiral shell fan, RIGHT (force / Chokmah): long doubled arcs
PB(21, 36, " _,,--´´ ", "shell")
PB(22, 32, " _,-´_,-´´ ", "shell")
PB(23, 30, " ,´_,-´_,´ ", "shell")
PB(24, 29, " ,´,-´-´ ", "shell")
PB(25, 28, " ((@),´ ", "shell")
PB(26, 29, " `~,_`~,_, ", "shell")
# gold sheen filling the fan wedge so it reads as a mass, not strings
for _r, _c in [(22, 36), (22, 38), (23, 34), (23, 37), (24, 32), (24, 35),
               (24, 37), (25, 34), (25, 36), (26, 38), (23, 39), (22, 41)]:
    put_empty(_r, _c, "'", "shell")
# rose pyramid above the shell
PB(20, 41, " /\\ ", "pyramid")
PB(21, 40, " /::\\ ", "pyramid")
PB(22, 39, " /_::_\\ ", "pyramid")
# faceted crystal far right
PB(26, 40, " ,<:>, ", "crystal")
PB(27, 39, " <:::::> ", "crystal")
PB(28, 39, " <:::::> ", "crystal")
PB(29, 40, " `<:>´ ", "crystal")

# ---- 16. signature ------------------------------------------------------
P(31, 1, "aw", "sig")

# ---- emit ---------------------------------------------------------------
assert len(canvas) == H
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "02-priestess-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "02-priestess-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
