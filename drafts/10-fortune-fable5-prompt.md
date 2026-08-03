# Fable Prompt — Atu X, Fortune (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** this card is RADIAL, not
bilateral — the WHEEL HUB, the crowning Sphinx and its upright sword all sit on column 23;
mirror the ascending Hermanubis (left) against the descending Typhon (right), and balance the
starry firmament and plumes about `AXIS = 23.0` with `PM`/`PMB`, verifying with `--axis`.
The classic bug tell is a centered Sphinx over a hub/wheel that leans a few columns left.
Cells are 1:2 so draw the wheel-rim as a ~2:1 wide ELLIPSE (a tall circle reads as an egg);
draw all circles/curves ~2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` +
line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never open
outlines, lit directionally. Foreground figures drawn ON TOP; break the wheel/plume edges
behind them. Full-bleed to the border. Keep outer frame + bottom title band. Color mapped to
the Harris painting. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans`
(256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the ten-spoked wheel = the ten Sephiroth, the three
gunas as Sulphur/Mercury/Salt riders, the motionless axle in the triangle, the distorted
stars of Nuit issuing lightnings) and clean compositor structure. It does NOT fix placement
drift — for that, use the render & review loop.

## Subject
**Atu X — Fortune** (old decks: The Wheel of Fortune). Hebrew letter Kaph ("palm / closed
hand" — the hand that turns the wheel; the palm that carries the soul's path). The planet
Jupiter ("the Greater Fortune"). Path 21, "The Intelligence of Conciliation," Chesed →
Netzach — the mechanism of the universe, the endless turning of Karma. "Follow thy Fortune,
careless where it lead thee! The axle moveth not: attain thou that."

## The composition, in one sentence
A great ten-spoked wheel spins counter-clockwise in a whirlpool of blue-violet plumes, a
golden Sphinx with an upright sword crowning its summit, a blue Mercury-ape (Hermanubis)
climbing its left side and a red crocodile-headed Typhon descending its right, all beneath a
firmament of distorted five-pointed stars issuing lightnings, a great apex-up triangle behind
the wheel with the motionless axle at its center.

Hold two things above all: the SPINNING TEN-SPOKED WHEEL centered on its motionless hub (the
card's whole structure) and the THREE RIDERS read as three distinct tinctures — bright
Sphinx atop, blue Hermanubis rising, red Typhon falling.

---

## Ranked directives

**Non-negotiable (1-4, it isn't Fortune without these):**

1. **The great ten-spoked Wheel, hub on the axis.** A WHEEL of ten spokes (the ten
   Sephiroth / Malkuth) spinning counter-clockwise, its HUB dead-center; the whole card
   revolves about col 23. Draw the rim as a 2:1 wide ellipse. The hub = Kether / Hadit / the
   point (a Sun-symbol), "the axle moveth not."

2. **The Sphinx crowning the summit.** A golden SPHINX (SULPHUR, the four Kerubs composited)
   atop the wheel, a SWORD held UPRIGHT between its lion-paws (mind / willpower). Dead-center
   on the axis, the top of the wheel.

3. **Hermanubis ascending (left) + Typhon descending (right).** On the LEFT a blue
   MERCURY-ape / Hermanubis CLIMBING; on the RIGHT the red-SALT crocodile-headed TYPHON
   (inverted Ankh) DESCENDING. Mirror the pair about the axis — one rising, one falling.

4. **The firmament of distorted stars + churning plumes.** Above, a FIRMAMENT of distorted
   five-pointed STARS (Nuit, the cosmic clock) issuing LIGHTNINGS; the whole set in a
   whirlpool of blue-violet PLUMES drawn out by the spin.

**Makes it Thoth (5-7):**

5. **The three gunas as three tinctures.** Value/color-separate the riders so Sulphur
   (Sphinx, bright/gold), Mercury (Hermanubis, blue) and Salt (Typhon, red/dark) read as the
   three principles, not a blur.

6. **The triangle behind the wheel + the motionless axle.** A great apex-up TRIANGLE
   behind/within the wheel, the three gunas stabilised, the HUB sitting in its center
   (*Centrum in Centri Trigono*, the all-seeing eye) = enlightenment, clarity.

7. **Lightnings striking Typhon.** Jupiter's LIGHTNING bolts lance down and strike the
   descending Typhon on the right.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. Exactly ten spokes if legible; a 10-pointed star echoed in upper and lower wheel ("as
   above, so below").
9. Kaph = the closed hand: a fist with six rays turning the wheel from below (the hand of
   God), if space allows.
10. The electric Jupiterian ground: violet, rich purple, bright blue rayed with yellow.

---

## Design note (specific to this card)
Foil to the Wheel's stillness is its motion: the whole point is a spinning mechanism with a
motionless center, so build it RADIALLY about the hub on col 23 rather than as a bilateral
shrine — but still verify the hub and the crowning Sphinx sit dead on the axis, and mirror
the two side-riders (one up, one down) so the wheel doesn't tilt. The trap is a lopsided
wheel or an egg-shaped rim; force the rim to a 2:1 ellipse and keep the spokes even. Make the
three riders read as three tinctures by value (bright Sphinx, blue ape, red crocodile) so the
gunas are legible, not a tangle of limbs. Palette from BoT/DuQuette is cool and electric: a
whirling BLUE-VIOLET / purple field, a golden SPHINX, a blue MERCURY-ape, a red-SALT TYPHON,
distorted STARS and yellow LIGHTNING, a purple TRIANGLE. The `.ans` carries a blue-violet
storm, a gold sphinx, a blue riser, a red faller, yellow lightning.

## Render & review
Do not judge the wheel's roundness, the riders, placement, or palette by reading the source.
Run the chain and LOOK: `compose_10-fortune_lg.py` → `frame.py <art> "FORTUNE" "~ kaph ·
jupiter ~" -w 47 -s majors -n X` → `cardkit.py 10-fortune` → `render_png.py 10-fortune
--axis`, then OPEN the PNG and critique against the (TBD) Harris scan: does the hub sit on
the axis guide with the Sphinx crowning it dead-center? is the rim a clean 2:1 ellipse with
ten even spokes? do Hermanubis (left, rising) and Typhon (right, falling) mirror and read as
distinct tinctures? is the firmament starry with lightnings, the triangle behind the wheel?
Fix the compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note:
`10-fortune` must be added to `cardkit.CONFIGS` before render_png will run. See
FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Wheel dominant** — the great ten-spoked wheel and its motionless hub/triangle as the
  hero structure, the three riders reading as attributes on the rim.
- **B. Riders dominant** — the three gunas (Sphinx / Hermanubis / Typhon) as the hero read,
  the wheel a frame that carries them up and down.
- **C. Cosmos dominant** — the starry firmament of Nuit, the lightnings and blue-violet
  plumes as the hero read (the cosmic clock), the wheel and riders the mechanism within it.
Tier: **full panel** — a radial, many-element card whose wheel must read round and whose
three riders must separate cleanly; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 10`:
top plaque `[ X ]` in the rule; bottom band `FORTUNE` / `~ kaph · jupiter ~`

## The one-line brief
A great ten-spoked wheel spinning counter-clockwise in a whirlpool of blue-violet plumes, a
golden Sphinx with an upright sword crowning its summit, a blue Mercury-ape climbing the
left and a red crocodile-headed Typhon falling on the right, beneath a firmament of distorted
stars and lightnings, an apex-up triangle behind the wheel holding the motionless axle. The
mechanism of the universe: generally good fortune, Karma turning, the wise at the still hub.
