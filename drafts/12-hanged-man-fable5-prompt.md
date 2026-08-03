# Fable Prompt - Atu XII, The Hanged Man (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Anchor to the axis (col 23):** this card is bilaterally
symmetric and INVERTED - the hanged figure hangs head-DOWN, his spine on column 23, the
ankh and free foot high, the head low inside its triangle. This is the strongest
axis-symmetry card of the set so far; balance the body, the green disks, and the
background grid about `AXIS = 23.0` with `PM`/`PMB` and verify with `--axis`. The classic
bug tell here is not lateral drift but the figure reading right-way-up - keep the bright
ankh/foot HIGH and the head LOW so the inversion is unmistakable. Cells are 1:2 so draw
the ankh loop and the green disks ~2:1 wider than tall. Courier New; extended alphabet
`´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for
volume, never open outlines, lit directionally - white Kether light from the top.
Foreground figure drawn ON TOP; break the background grid behind him. Full-bleed to the
border. Keep outer frame + bottom title band. Color mapped to the Harris painting. Sign
`aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the cross-over-triangle geometry, Mem the mother
letter of Water, the ankh replacing the gallows, the serpent of new life in the black
womb-waters, the New-Aeon re-reading of "redemption") and clean compositor structure. It
does NOT fix placement drift - for that, use the render & review loop.

## Subject
**Atu XII - The Hanged Man** (DuQuette: "The Spirit of the Mighty Waters"). Hebrew letter
Mem ("water" / the ocean), one of the three MOTHER LETTERS (Aleph/air, Mem/water,
Shin/fire); value 40. Elemental Trump of WATER - no zodiac sign. Path 23 (GD/DuQuette),
Geburah → Hod, on the Pillar of Severity, opposite the Wheel of Fortune. "A baptism which
is also a death"; "the descent of the light into the darkness in order to redeem it."
Crowley's New-Aeon re-reading: NOT sacrifice, sin, or debt - the willing surrender of the
lower for the spiritual, the annihilation of the self in the Beloved.

## The composition, in one sentence
A young fair man hangs head-down by his left foot from an inverted ankh, right leg crossed
behind into a figure 4 and arms clasped behind his head into an upright triangle that
radiates light, green disks at the ends of his limbs and head, a serpent coiled round the
foot, white Kether light descending through a green air into the black womb-waters below
where a serpent of new life stirs, all against an unbounded grid of small squares.

Hold two things above all: THE INVERTED HANGED FIGURE (head-down on the axis, the hero
read) and the CROSS-OVER-TRIANGLE GEOMETRY (legs a 4/cross, arms + torso a triangle around
the head - light entering darkness).

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Hanged Man without these):**

1. **The inverted hanged figure, head-DOWN, hanging by the left foot.** A young fair man
   suspended upside down; his body/spine reads on column 23 as the vertical of the card.
   Draw him ON TOP of the grid; keep the head low, the foot/ankh high - the inversion must
   be unmistakable.

2. **The cross-over-triangle geometry.** Right leg crossed behind the left into a figure 4
   / cross (at the bottom, near the head); arms clasped behind the head into an upright
   TRIANGLE that radiates light, the head centred inside it. Triangle (spirit) over cross
   (matter): light into darkness. Do not let it blur into a plain standing figure.

3. **The inverted Ankh he hangs from.** At the TOP, an ankh (Rose & Cross) as the
   suspension point, replacing the old wooden gallows; keep it pale/gold and lit by the
   white Kether light.

4. **The serpent coiled around the foot.** A serpent wound about the suspending (left) foot
   at the top, binding it to the ankh - creator and destroyer, the will of God (Chokmah)
   that operates all change.

**Makes it Thoth (5-7):**

5. **The green disks + green air of Grace.** GREEN disks (Venus, Grace, Love) at the
   terminations of the limbs and the head; the air above the water green, infiltrated by
   the white rays of Kether from the top.

6. **The black womb-waters + serpent of new life below.** Beneath the figure a BLACK
   enclosed shape (the black waters of Binah / the womb), a solid dithered mass low centre,
   in which a serpent (black flecked gold) stirs, coiled - the serpent of new life.

7. **The unbounded grid of small squares.** The background a boundless grill of small
   squares (the Enochian Elemental Tablets) tiling the whole field behind the figure,
   occluded where he overlaps.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The 18 rays from the man's head down into the womb below (18 = Chai, "Life").
9. The Vau-shaped nails at hands/feet (links him to the Hierophant); tiny marks only.
10. The white Kether light entering from the top; the figure's mouth resolutely closed.

---

## Design note (specific to this card)
This is the axis-symmetry test of the run: a single inverted figure, no rider-on-beast
diagonal (contrast Lust/Death) - so lean hard on the mirror helpers and let the composition
be still and vertical. The danger is threefold: (1) the figure reading upright - fix by
pinning the bright ankh + foot to the TOP and the head + triangle LOW; (2) the body not
reading as cross-over-triangle - make the leg-4 and the arm-triangle explicit; (3) the palette
going generic - this card is GREEN (Venusian air) and WHITE (Kether light) above a BLACK
water base, distinct from Lust's heat and the neighbouring Death's murk. Keep the background
grid full-bleed behind everything and the black womb a solid dithered mass at the bottom with
the coiled serpent inside. Palette from BoT/DuQuette: white Kether light at top, a GREEN air
of Grace, a pale/fair inverted figure with GREEN disks, an inverted gold/pale ANKH, a dark
grid of small squares, a BLACK womb of water with a black-flecked-gold SERPENT. The `.ans`
reads green and pale over a dark base.

## Render & review
Do not judge the inversion, the cross-over-triangle, placement, or palette by reading the
source. Run the chain and LOOK: `compose_12-hanged-man_lg.py` → `frame.py <art> "THE HANGED
MAN" "~ mem · water ~" -w 47 -s majors -n XII` → `cardkit.py 12-hanged-man` → `render_png.py
12-hanged-man --axis`, then OPEN the PNG and critique against the (TBD) Harris scan: does the
figure read INVERTED (head low, ankh/foot high) and centred on the axis guide? do the legs
make a 4/cross and the arms a triangle around the head? does the ankh sit at the top with the
serpent round the foot? do the green disks + green air read against the white top light and the
black womb below? does the background grid tile full-bleed behind the figure? Fix the compositor
and repeat. Ship at ~80% once the render holds (2-3 passes max). Note: `12-hanged-man` must be
added to `cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render & review
loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Figure dominant** - the inverted man as the hero read, the cross-over-triangle body
  filling the frame, ankh and womb as attributes above and below.
- **B. Vertical-axis dominant** - the full top-to-bottom descent read as one column of light:
  Kether light → ankh → inverted figure → 18 rays → black womb + serpent, the whole card a
  single glyph of light entering darkness.
- **C. Field dominant** - the Enochian grid + green air + black womb as an environment the
  figure hangs INSIDE, emphasising the elemental-Water immersion (baptism/drowning) around him.
Tier: **full panel** - an axis-critical, easily-misread (upright vs inverted) card whose whole
meaning rides on geometry; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 12`:
top plaque `[ XII ]` in the rule; bottom band `THE HANGED MAN` / `~ mem · water ~`

## The one-line brief
A young fair man hangs head-down by his left foot from an inverted ankh, legs a figure-4
cross and arms a light-radiating triangle around his head, green disks at his limbs, a serpent
coiled at the foot, white Kether light falling through green air into black womb-waters where a
serpent of new life stirs, over a grid of small Enochian squares. The New-Aeon baptism-death:
not sacrifice or debt, but the willing surrender of the lower for the spiritual, light entering
the darkness to redeem it.
