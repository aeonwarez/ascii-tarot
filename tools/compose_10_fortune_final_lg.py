#!/usr/bin/env python3
"""Atu X Fortune — SYNTHESIS (judge tally v3b 9 / v3a 6 / v3c 3).

BASE v3b (riders dominant): reclining gold Sphinx with UU paws + upright
sword, tincture-separated riders (grey-gold plated Hermanubis climbing
left, red-gold croc-Typhon falling right with ankh + hook), rim-grip
occlusion (hands/plates breaking the rim), =(m)= Kaph fist with rays.
FIX 1: whole wheel group dead on col 23 (hub star, sword, fist, top star
all asserted at col 23; rim band exactly mirror-symmetric).
FIX 2: rim emphatically GOLD — every band cell stamped class "wheel",
closed 2:1 ellipse, calm interior so the gold pops.
GRAFT v3a: beaded top/bottom arcs (o;o: beads, = crown) + doubled
((( / ))) side-rim stacks; exactly TEN even spokes; two-tier gold+blue
distorted-star firmament with pendant v-fringe; tall flanking orange
lightning columns with strike-tips lancing into the falling Typhon.
GRAFT v3c: s/c curl plume whirlpool full-bleed (plume/field/dusk bands,
no black emptiness) and the crisper <;==( open-jawed croc snout.
KEEP: faint purple triangle fragments outside the rim + dashed base,
electric Jupiterian palette, 'aw' signature.

Emits:
  drafts/10-fortune-final-art-lg.txt       47x32 art
  drafts/10-fortune-final-lg-classes.json  per-cell class grid
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
W, H = 47, 32
AXIS = 23.0

canvas = [[" "] * W for _ in range(H)]
classes = [[None] * W for _ in range(H)]
MIRROR = str.maketrans("()/\\[]{}<>`´,.", ")(\\/][}{><´`,.")

BG = {None, "field", "plume", "dusk", "tri"}   # classes bolts/spokes may cover


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


def PBGC(r, c, ch, cls):
    """Place only over background classes (weaves behind solids)."""
    if 0 <= r < H and 0 <= c < W and classes[r][c] in BG:
        canvas[r][c] = ch
        classes[r][c] = cls


# ------------------------------------------------------------- geometry
# Hub dead on col 23; rim a 2:1-wide ellipse (cells are 1:2).
CY, CX = 15.5, 23.0
RX, RY = 13.0, 6.5           # rim reaches rows 9..22, cols ~9..37


def q(r, c):
    """Normalized ellipse coordinate: 1.0 on the rim centreline."""
    return math.hypot((c - CX) / RX, (r - CY) / RY)


BAND_LO, BAND_HI = 0.82, 1.06   # golden rim band (3-deep on the sides)

# ------------------------------------------------- 1. whirlpool (v3c graft)
# s/c curl plume bands drawn out by the spin, FULL-BLEED — no black
# emptiness anywhere; the wheel face kept calm so the spokes read.
PERIOD = 5.0
SWIRL = 2 * PERIOD
RAMPS = {
    "plume": (97, "~s~c~;"),
    "field": (88, ";:·';~"),
    "dusk":  (72, ":.·,;."),
}
ORDER = ["plume", "field", "dusk"]
for r in range(5, H):
    for c in range(W):
        h = (r * 37 + c * 59 + (r * c) % 13) % 100
        qq = q(r, c)
        if qq < 0.78:                 # calm violet wheel face
            if h < 32:
                P(r, c, "·'.:"[h % 4], "dusk")
            continue
        if qq < 1.18:                 # quiet ring so the gold rim pops
            if h < 30:
                P(r, c, "·,"[h % 2], "dusk")
            continue
        dx = c - CX
        dy = 2.0 * (r - CY)
        d = math.hypot(dx, dy)
        th = math.atan2(dy, dx) % (2 * math.pi)
        v = d + SWIRL * th / (2 * math.pi)
        cls = ORDER[int(v / PERIOD) % 3]
        cov, ramp = RAMPS[cls]
        if h >= cov:
            continue
        t = (v % PERIOD) / PERIOD
        ch = ramp[0] if (cls == "plume" and t < 0.45) else ramp[h % len(ramp)]
        P(r, c, ch, cls)

# --------------------------------------- 2. star firmament (v3a graft)
# Two-tier gold+blue distorted stars over star-dust, pendant v-fringe.
for r in range(0, 4):
    for c in range(W):
        h = (r * 41 + c * 23 + (r * c) % 7) % 100
        if h < 32:
            P(r, c, "·,'."[h % 4], "starsb")


def gstar(r, c):  # 5x3 great gold star, centred (r, c)
    PB(r - 1, c - 2, " \\¡/ ", "starsg")
    PB(r, c - 2, "<=*=>", "starsg")
    PB(r + 1, c - 2, " /¡\\ ", "starsg")


def bstar(r, c):  # 3x3 blue star
    PB(r - 1, c - 1, "\\¡/", "starsb")
    PB(r, c - 1, "=*=", "starsb")
    PB(r + 1, c - 1, "/¡\\", "starsb")


gstar(1, 23)          # the crown star, dead on the axis
gstar(2, 11)
gstar(2, 35)
gstar(1, 3)
gstar(1, 43)
bstar(1, 7)
bstar(1, 39)
bstar(2, 17)
bstar(2, 29)
P(0, 15, "*", "starsg")
P(0, 31, "*", "starsg")
P(3, 20, "*", "starsb")
P(3, 26, "*", "starsb")
# pendant v-fringe under the star band
for c in range(0, W):
    if c % 2 == 0:
        P(4, c, "v", "starsg")
    else:
        P(4, c, "·", "starsb")

# ------------------------------------------- 3. triangle fragments (KEEP)
# Apex-up triangle behind the wheel, hub in its centre; only the faint
# fragments OUTSIDE the rim survive, plus the dashed base.
for r in range(5, 27):
    fc = 23.0 - (r - 4) * 20.0 / 23.0
    for cc, ch in ((fc, "/"), (2 * AXIS - fc, "\\")):
        ci = int(round(cc))
        if q(r, ci) > 1.12:
            PBGC(r, ci, ch, "tri")
for c in range(4, 43, 2):
    PBGC(27, c, "_", "tri")

# ------------------------------------------------- 4. the golden wheel
# Every band cell stamped gold: beaded arcs top/bottom (o;o: beads, "="
# crown at the poles, slashed shoulders) + doubled ((( / ))) side stacks
# forcing a CLOSED clean 2:1 ellipse.  (v3a rim treatment at v3b size.)
rim_min = [W] * H
rim_max = [-1] * H
for r in range(H):
    for c in range(W):
        qq = q(r, c)
        if not (BAND_LO <= qq <= BAND_HI):
            continue
        dxn = (c - CX) / RX
        dyn = (r - CY) / RY
        s = -dyn / qq                      # sin of the visual angle
        if abs(s) < 0.45:
            g = "(" if dxn < 0 else ")"    # doubled paren side stacks
        elif abs(s) < 0.92:                # shoulders: slash edges, bead fill
            if qq >= 0.97 or qq <= 0.88:
                g = ("\\" if dxn > 0 else "/") if s > 0 else \
                    ("/" if dxn > 0 else "\\")
            else:
                g = "o;o:"[(r * 31 + c * 17) % 4]
        elif qq > 0.97:
            g = "="                        # crown / keel outer edge
        else:
            g = "o;o:"[(r * 31 + c * 17) % 4]   # gold beads inside
        P(r, c, g, "wheel")
        rim_min[r] = min(rim_min[r], c)
        rim_max[r] = max(rim_max[r], c)

# rim must be mirror-symmetric about col 23 (the v3b lean, fixed)
for r in range(H):
    if rim_max[r] >= 0:
        assert rim_min[r] + rim_max[r] == 46, f"rim leans at row {r}"

# the motionless hub: rayed sun dead on the axis
PB(14, 20, " ,\\¡/, ", "hub")
PB(15, 19, " =<(*)>= ", "hub")
PB(16, 20, " `/¡\\´ ", "hub")

# exactly TEN even spokes, hub to inner rim (vertical pair at 12 + 6)
SPOKES = 10
for k in range(SPOKES):
    a = math.radians(k * 36.0)
    sa, ca = math.sin(a), math.cos(a)
    ratio = abs(2 * sa) / max(abs(ca), 1e-6)
    if ratio < 0.7:
        g = "|"
    elif ratio > 3.2:
        g = "-"
    else:
        g = "/" if (sa > 0) == (ca > 0) else "\\"
    for t in [i / 24.0 for i in range(8, 25)]:
        rr = int(round(CY - t * (RY * 0.80) * ca))
        cc = int(round(CX + t * (RX * 0.80) * sa))
        PBGC(rr, cc, g, "wheel")

# plume tufts filling the sky right of the Sphinx's haunch (full-bleed)
P(5, 26, "~·~,", "plume")
P(5, 31, ",~", "plume")

# ------------------------------------------- 5. Sphinx + sword (v3b base)
# Reclining gold Sphinx atop the wheel, head left as Harris paints her,
# haunches sweeping right, UU paws ON the rim, sword upright dead on 23.
PB(4, 14, " ,-^-, ", "sphinx")
PB(5, 13, " /(o·o)\\ ", "sphinx")
PB(6, 13, " ,(;;;), ", "sphinx")
PB(6, 25, " __,--,_ ", "sphinx")
PB(7, 13, " (;;;;;;`-,__,--´;;;;;;;`, ", "sphinx")
PB(8, 13, " (;;;;;;;;;;;;;;;;;;;;;;;;) ", "sphinx")
PB(9, 17, " _,UU,¡,UU;;;;;;;)_U´ ", "sphinx")
# the sword: tip in the fringe, haloed blade, guard at the breast
P(4, 23, "|", "sword")
PB(5, 22, " | ", "sword")
PB(6, 22, " | ", "sword")
PB(7, 22, " | ", "sword")
P(8, 22, "<", "sword")
P(8, 23, "+", "sword")
P(8, 24, ">", "sword")

# --------------------------------- 6. Hermanubis (Mercury, grey-gold, L)
# c(( plate carapace at the edge, body climbing OUTSIDE the left rim,
# arm up gripping the wheel, halos breaking the rim where he holds it.
P(11, 2, "((", "plate")
P(12, 1, "c((", "plate")
P(13, 1, "c((", "plate")
P(14, 1, "c((", "plate")
P(15, 1, "c((", "plate")
P(16, 2, "((", "plate")
PB(10, 4, " ,--, ", "herm")
PB(10, 10, " ,-´) ", "herm")
PB(11, 4, " (o;=´ ", "herm")
PB(12, 4, " (;;;), ", "herm")
PB(13, 4, " (;;;;) ", "herm")
PB(14, 4, " (;;;;) ", "herm")
PB(15, 4, " );;;( ", "herm")
PB(16, 4, " (;;;;) ", "herm")
PB(17, 5, " );;,_) ", "herm")
PB(18, 6, " (;;;) ", "herm")
PB(19, 6, " );;=) ", "herm")
PB(20, 5, " `;,´ ", "herm")
PB(21, 3, " (c,_ ", "herm")

# --------------------------------------------- 7. Kaph: the turning fist
# (drawn before Typhon so his ankh-hand is never halo-punched)
PB(24, 21, " \\¡/ ", "hub")
PB(25, 20, " =(m)= ", "hub")
PB(26, 21, " /¡\\ ", "hub")

# ------------------------------------ 8. Typhon (Salt, red-gold, R, falls)
# v3b body: tail coiled on the upper rim, trunk descending outside it;
# v3c's crisper open-jawed croc snout <;==( grafted at the bottom.
PB(9, 30, " _,o-, ", "typhon")
PB(10, 31, " (o,o( ", "typhon")
PB(11, 34, " ),;;, ", "typhon")
PB(12, 36, " );;;) ", "typhon")
PB(13, 37, " (;;;) ", "typhon")
PB(14, 37, " (;;;) ", "typhon")
PB(15, 37, " (;;;) ", "typhon")
PB(16, 37, " (;;;( ", "typhon")
PB(17, 36, " );;;) ", "typhon")
PB(18, 35, " (;;;( ", "typhon")
PB(19, 33, " (;;=( ", "typhon")
PB(20, 31, " ,(;;) ", "typhon")
PB(21, 29, " (;;,´ ", "typhon")
PB(22, 29, " ,(;;), ", "typhon")       # neck turning under
PB(23, 28, " (o;;;( ", "typhon")       # eye row
PB(24, 28, " <;==( ", "typhon")        # open upper jaw (v3c)
PB(25, 29, " <_=<´ ", "typhon")        # lower jaw (v3c)
# arms + implements: inverted ankh (inner hand), long crook (outer);
# placed with P (no halo) so the small marks stay whole
P(23, 26, "),", "typhon")
P(24, 25, "-+-", "typhon")
P(25, 26, "o", "typhon")
PB(21, 36, " \\, ", "typhon")
PB(22, 37, " \\, ", "typhon")
PB(23, 38, " _7 ", "typhon")
PB(24, 39, " | ", "typhon")
PB(25, 39, " | ", "typhon")

# ------------------------------------- 9. lightning columns (v3a graft)
def bolt(r0, c0, n):
    c = float(c0)
    for i in range(n):
        r = r0 + i
        if i % 6 < 3:
            g = "\\"
            c += 0.45
        else:
            g = "/"
            c -= 0.45
        ci = int(round(c))
        if q(r, ci) > 1.02:
            PBGC(r, ci, g, "bolt")
    ci = int(round(c))
    if q(r0 + n, ci) > 1.02:
        PBGC(r0 + n, ci, "v", "bolt")


bolt(5, 2, 24)       # tall left column
bolt(5, 6, 8)
bolt(5, 12, 4)       # tip flares at the wheel's left shoulder
bolt(17, 5, 12)      # lower-left column
bolt(5, 34, 5)       # tip beside Typhon's coil, in the quiet ring
bolt(5, 38, 14)      # lances down along Typhon's back
bolt(5, 41, 10)
bolt(5, 44, 24)      # tall right column
bolt(20, 43, 8)
bolt(26, 13, 5)      # under-wheel bolts running to the bottom edge
bolt(27, 31, 4)
# strike-tips stamped ON the falling Typhon (Jupiter finds his mark)
P(12, 38, "v", "bolt")
P(18, 39, "v", "bolt")
P(21, 33, "v", "bolt")

# ------------------------------------------------------------------ sig
P(31, 2, "aw", "sig")

# ---------------------------------------------------------------- emit
for r in range(H):
    assert any(ch != " " for ch in canvas[r]), f"row {r} empty"
assert any(canvas[r][46] != " " for r in range(H)), "col 46 never reached"
# the axis group is DEAD on col 23 (the v3b lean, fixed)
assert canvas[15][23] == "*" and classes[15][23] == "hub", "hub off axis"
assert canvas[1][23] == "*" and classes[1][23] == "starsg", "crown star off axis"
assert canvas[9][23] == "¡", "sword hilt off axis"
assert canvas[25][23] == "m", "Kaph fist off axis"
assert SPOKES == 10, "spoke count"

art = "\n".join("".join(row).rstrip() for row in canvas) + "\n"
with open(os.path.join(DRAFTS, "10-fortune-final-art-lg.txt"), "w") as f:
    f.write(art)
with open(os.path.join(DRAFTS, "10-fortune-final-lg-classes.json"), "w") as f:
    json.dump(classes, f)
print(art)
