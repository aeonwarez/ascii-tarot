# Fable Prompt - Atu I, The Magus (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** every element of the
central figure sits so its VISUAL center is column 23, not its left edge. Prefer the
mirror helpers (`PM`/`PMB` about `AXIS = 23.0`) for anything bilaterally symmetric;
for asymmetric sprites place at `23 - len(s)//2` and confirm with `--axis`. Cells are
1:2 so draw circles/curves ~2:1 wider than tall. Courier New; extended alphabet
`´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for
volume, never open outlines, lit directionally. Foreground figure drawn ON TOP; break
background edges behind it. Full-bleed to the border. Keep outer frame + bottom title
band. Color mapped to the Harris painting. Sign `aw` or unsigned, never `jgs`. Output
one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows most in the esoteric SYNTHESIS (Mercury glyph, the eight objects, the
Kether/Binah light) and clean compositor structure. It does NOT fix placement drift -
for that, use the render & review loop.

## Subject
**Atu I - The Magus.** Hebrew letter Beth ("house"), the planet Mercury. Path 12,
"The Intelligence of Transparency," Kether → Binah - the CLEAR CHANNEL. Hermes
Trismegistus (Mercury the messenger, Thoth the scribe, Hermes the alchemist); the
Word / Will / Logos by whom the worlds were created; the male correlative of the High
Priestess; the adult form of the Fool. The alchemical principle MERCURY (the first of
the three alchemical trumps). Creative, dual, tricky: "he represents both truth and
falsehood, wisdom and folly." "Manifestation implies illusion."

## The composition, in one sentence
A naked androgynous youth with winged head and heels hangs in dynamic mid-motion, his
body forming the alchemical glyph of Mercury (two serpents as horns above, wide wings
as the arrowhead below), projected on a great golden caduceus that runs the full height
of the card with a dove descending in its circle, while he JUGGLES eight small objects
in a ring around him, a bright white V of Kether light behind his head and the dark
womb of Binah below, the Ape of Thoth groping up from the lower-right corner.

Hold two things above all: the MERCURY-GLYPH figure in perpetual motion (serpent-horns
+ foot-wings + the swastika/thunderbolt attitude) and the EIGHT JUGGLED OBJECTS
orbiting him. This is the motion-card opposite of the Priestess's stillness.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Magus without these):**

1. **The airborne Mercury-glyph youth, centered on col 23.** A naked, fair,
   ANDROGYNOUS youth (masculine + feminine, like the Fool), suspended in dynamic
   motion, attitude like a swastika / thunderbolt. His body reads as the alchemical
   MERCURY glyph: two serpents at his head make the horns, the wide stylized wings at
   his feet make the arrowhead-cross. Winged helmet, winged heels. Draw him ON TOP.
   His VISUAL center (and the caduceus rod) sits on column 23 - mirror the symmetric
   parts about `AXIS = 23.0`; the classic tell of the bug is a centered head over a
   body that leans a few columns left.

2. **The eight juggled objects, ringing him in midair.** He joyfully juggles
   EIGHT small distinct glyphs around his body: Wand (a phoenix wand), Cup
   (two-handled Grecian), Dagger/stiletto, Disk (the 8-fold star of Mercury),
   the Winged/Orphic Egg, the Stylus, the Scroll/Papyrus, and the Wand of Double
   Power. Keep them small, legible, and clearly airborne. Balance them left/right of
   the axis so the orbit reads centered, not lopsided.

3. **The great caduceus.** A tall golden CADUCEUS as his central axis: its rod
   runs from below his feet to the very bottom of the card ON COL 23; its winged head
   spans the full width of the top and curves down behind his neck. A DOVE descends
   inside its circle (the eye of Horus / spirit entering creation).

4. **Kether light above, Binah dark below.** A bright WHITE V-wedge of Kether
   light behind and above his head (narrowing upward, an inverted formless
   triangle the form-lines never enter); the dark indigo womb of Binah below,
   with a faint arc/semicircle at the very bottom birthing form. Faint crossing
   form-lines fill the mid field.

**Makes it Thoth (5-7):**

5. **The lemniscate of serpents.** Two serpents twined as an INFINITY sign above
   his head, stretching down through his feet - his infinite Kether source
   channelled into Binah. Left serpent wears the throne-headdress of Isis
   (Binah); right serpent a plain crown (Kether).

6. **Winged sandals + serpent strap.** Winged heels of Hermes the messenger; the
   sandal-strap a small serpent shedding its skin (life anew).

7. **The Ape of Thoth (Cynocephalus).** A monkey groping upward from the LOWER
   RIGHT corner by his right foot - the distortion of truth inherent in speech
   and form. "Manifestation implies illusion."

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. A faint golden SUNBURST behind the left foot-wing (Mercury, herald of the Sun).
9. The caduceus outlined in yellow (Vau of Tetragrammaton).
10. The ambiguous two-way face (reads up-left or down-right by focus) - his dual
    trickster nature; only if it doesn't muddy the figure.

---

## Design note (specific to this card)
Sibling to the Fool (0) and correlative of the Priestess (II): where the Priestess is
serene bilateral STILLNESS behind a veil of light, the Magus is pure MOTION - objects
flung into orbit, a spinning swastika/thunderbolt body, the caduceus thrusting through
the whole card. Build that energy: diagonal thrust, airborne clutter held in balance,
nothing at rest. The single most important read is the Mercury glyph (serpent-horns +
foot-wings) plus the ring of eight juggled tools; if those land, the card works. Keep
the Ape small in the lower-right so it reads as a footnote, not a second figure. The
palette from the scan is warm and luminous: a YELLOW-GOLD figure and caduceus against a
white V of Kether light, indigo/violet Binah dark below, with small color accents on
the juggled weapons. The `.ans` carries gold figure vs. white light V vs. indigo depth.

Watch the axis trap here more than most: the body is asymmetric (swastika thrust), so
it is tempting to place it by its left edge and let it drift. Anchor the caduceus rod
and the head on col 23, then hang the diagonal motion off that spine.

## Render & review
Do not judge placement, mass volume, occlusion, or palette by reading the source. Run
the full chain and LOOK: `compose_01-magus_lg.py` → `frame.py <art> "THE MAGUS"
"~ beth · mercury ~" -w 47 -s majors -n I -o 01-magus-lg-v1.txt` → `cardkit.py
01-magus` → `render_png.py 01-magus --axis`, then OPEN the PNG and critique it against
the Harris scan: is the figure centered on the axis line? does the Mercury glyph read?
are the eight objects balanced around him? do the light V and Binah dark read as mass,
not outline? Fix the compositor and repeat. Ship at ~80% once the render holds up (2-3
passes max). Note: `01-magus` must be added to `cardkit.CONFIGS` before render_png
will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate), three
judges scoring each against the Harris scan + axis guide, then synthesis / polish /
integration merging the strongest read. Three strategies to seed the composers:
- **A. Mercury-glyph figure dominant** - the swastika-motion body (serpent-horns +
  foot-wings) is the hero, the eight objects tight around him.
- **B. Caduceus-spine dominant** - the full-height caduceus is the hero, figure overlaid
  on it, dove descending in the circle emphasized.
- **C. Juggling-orbit dominant** - the eight objects flung wide in a balanced ring, the
  figure smaller at the centered hub.
Tier: **full panel** - asymmetric swastika motion plus eight objects makes this the
highest axis / composition risk of the set; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 1`:
top plaque `[ I ]` in the rule; bottom band `THE MAGUS` / `~ beth · mercury ~`

## The one-line brief
A naked winged androgynous Magus suspended in swastika-motion, his body the alchemical
Mercury glyph (serpent horns above, wide foot-wings below), on a full-height golden
caduceus with a dove descending in its circle, juggling eight small objects (wand, cup,
dagger, star-disk, orphic egg, stylus, scroll, double-wand) in a ring around him, a
white V of Kether light behind his head and the dark womb of Binah below, the Ape of
Thoth groping up from the lower-right. The Word in perpetual creative motion.
