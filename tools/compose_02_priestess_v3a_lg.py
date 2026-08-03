#!/usr/bin/env python3
"""Priestess v3a — VEIL-DOMINANT (ultracode panel, composer A).

Strategy: the crystalline light-web fills the WHOLE field. A radial net —
straight rays fanning from an origin behind her lap, crossed by concentric
arc rings — covers every region of the card, crossing into diamonds. Density
varies (tight/bright veil-class near her, opening to dashed lattice-class at
the corners) so the web reads as a translucent VOLUME of light. Between the
net lines, a symmetric dither of deep-blue field + alternating teal wedges
(the Harris blue/green fan stripes) — no black emptiness anywhere. The
figure, cup, skirt, and foreground garden are halo-punched (PB) ON TOP.

Emits drafts/02-priestess-v3a-art-lg.txt + drafts/02-priestess-v3a-lg-classes.json
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


# ---- the net's polar frame: origin behind her lap, cell aspect baked in --
OR_, OC_ = 12.0, 23.0


def polar(r, c):
    du = (c - OC_) * 0.5          # visual x in row units (cells are 1:2)
    dv = r - OR_
    return math.hypot(du, dv), math.degrees(math.atan2(dv, du))


# ---- 1. pillars first (half-lost in the webbing drawn over them) --------
for r in range(5, 22):
    if r % 4:
        PM(r, 0, "|:", "pillar")

# ---- 2. the veil: straight rays fanning from the origin -----------------
# dense down-fan (the stretched net below the cup), sparser up-fan plumes
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

# ---- 3. the veil: concentric arc rings crossing the rays into diamonds --
# rings live below the horizontal (the net); the top is wing-sweep country
RINGS = [3.5, 5.0, 6.5, 8.0, 9.75, 11.5, 13.5, 15.75, 18.0, 20.5, 23.0]
for r in range(22):
    for c in range(W):
        R, a = polar(r, c)
        if a < -20:
            continue
        for ki, Rk in enumerate(RINGS):
            if abs(R - Rk) >= 0.30:
                continue
            if Rk > 16.0 and (r * 2 + abs(c - 23)) % 2:   # dash outer rings
                continue
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
# dense enough that no region reads as black emptiness; density opens with R
for r in range(H):
    for c in range(W):
        if canvas[r][c] != " ":
            continue
        R, a = polar(r, c)
        d = abs(c - 23)
        h = (r * 31 + d * 17 + (r * d) % 7) % 100
        if r >= 22:                        # quiet indigo ground of the garden
            if h < 88:
                put_empty(r, c, ":;·:"[h % 4], "field")
            continue
        cov = 96 if R < 6 else (90 if R < 11 else (84 if R < 17 else 76))
        if a < -20 and R > 5.5:
            cov = min(cov + 8, 99)         # the top sweeps are a dense mass
        if h >= cov:
            continue
        diag = min(abs(a), 180 - abs(a))
        if a > 12 and 8 <= diag <= 70:
            cls = "wings" if int((diag + 4) / 12) % 2 == 0 else "field"
        elif a < -20 and diag <= 62:
            cls = "wings"
        else:
            cls = "field"
        # chunky dark-blue ground vs bright teal marks: the white net keeps
        # the top of the luminance stack
        ramp = ";·;," if cls == "wings" else ":;;:"
        put_empty(r, c, ramp[h % len(ramp)], cls)

# ---- 6. the warm gold-green glow around head + crown --------------------
for r in range(0, 7):
    for c in range(12, 35):
        Rh = math.hypot((c - 23) * 0.5, r - 2.5)
        if 2.3 <= Rh <= 4.6 and (r * 11 + abs(c - 23) * 5) % 3:
            P(r, c, "'" if Rh < 3.5 else "·", "crown")

# ---- 7. teal wing sweeps, bold bands over the net -----------------------
PM(0, 2, "_,--~~´", "wings")
PM(1, 0, ",-´_,-~´", "wings")
PM(2, 0, "/,-´", "wings")
PM(3, 0, "(´", "wings")
PM(4, 0, "\\`,", "wings")
PM(5, 1, "`-,_", "wings")
PM(6, 3, "`-,_", "wings")
PM(7, 6, "`--,_", "wings")
PM(8, 10, "`--,_", "wings")

# ---- 8. arms sweeping up-out into spiral curls (double-stroke ribbon) ---
PM(2, 5, ",--,", "figure")             # curl top
PM(3, 3, "((", "figure")
PM(3, 5, "o", "crown")                 # gold-green eye of the curl
PM(3, 6, "`", "figure")
PM(4, 4, "`--´", "figure")             # curl bottom
PM(3, 8, "--,_", "figure")             # upper arm stroke
PM(4, 12, "`-,_", "figure")
PM(5, 16, "`-,", "figure")
PM(4, 8, "-,_", "figure")              # lower arm stroke
PM(5, 11, "`-,_", "figure")
PM(6, 15, "`-,_", "figure")

# ---- 9. the goddess: crown, face, latticed torso (halo-punched) ---------
PB(0, 20, " )(O)( ", "crown")
PB(1, 20, " /´|`\\ ", "crown")
PB(2, 20, " (-·-) ", "figure")
PB(3, 21, " )-( ", "figure")
PB(4, 21, " )x( ", "figure")
PB(5, 20, " (x'x) ", "figure")
PB(6, 20, " (x|x) ", "figure")
PB(7, 20, " )x|x( ", "figure")
PB(8, 20, " (x|x) ", "figure")
PB(9, 19, " (xx|xx) ", "figure")
PB(10, 19, " (xx|xx) ", "figure")
PB(11, 19, " )xx|xx( ", "figure")

# ---- 10. the crescent Moon-cup / lyre, scrolled ends, hidden book -------
cup1 = ",cC==" + "~" * 9 + "-·-" + "~" * 9 + "==Cc,"
PB(12, 23 - len(cup1) // 2 - 1, " " + cup1 + " ", "cup")
cup2 = "`--,__" + "_[=]_" + "__,--´"
PB(13, 23 - len(cup2) // 2 - 1, " " + cup2 + " ", "cup")

# ---- 11. latticed skirt-tent, melting into the net (no hard hemline) ----
PB(14, 18, " (xx´|`xx) ", "figure")
PB(15, 18, " /xx´|`xx\\ ", "figure")
PB(16, 17, " /xxx´|`xxx\\ ", "figure")
PB(17, 16, " /xxxx´|`xxxx\\ ", "figure")
PB(18, 16, " /xxxx´|`xxxx\\ ", "figure")
PB(19, 15, " /xxxxx´|`xxxxx\\ ", "figure")
PM(20, 15, "x`,", "figure")
PM(20, 18, "x", "figure")
PB(20, 20, " ´‾‾‾` ", "cup")       # inverted crescent on the throne base

# ---- 12. the foreground garden ------------------------------------------
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
# the white camel, DEAD CENTER (hump apex on col 23), clean sky punched
PB(24, 17, "  o,       ", "camel")
PB(25, 19, "  _,^,_  ", "camel")
P(25, 19, "\\", "camel")
PB(26, 18, " (:::::::) ", "camel")
PB(27, 19, " ||   || ", "camel")
# purple grapes right of the camel
PB(27, 27, " ,o,o,o, ", "grapes")
PB(28, 26, " (o,o,o,o) ", "grapes")
PB(29, 27, " (o,o,o) ", "grapes")
PB(30, 28, " `o,o´ ", "grapes")
# the yellow spiral shell fan, RIGHT (force / Chokmah): long doubled arcs
# sweeping up-right out of the spiral eye
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

# ---- 13. signature ------------------------------------------------------
P(31, 1, "aw", "sig")

# ---- emit ---------------------------------------------------------------
assert len(canvas) == H
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "02-priestess-v3a-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "02-priestess-v3a-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
