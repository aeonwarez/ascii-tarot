# Fable5 Prompt - Knight of Cups (Thoth)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed. NOTE: this is a court card, but a Harris scan of it DOES exist in the repo (`reference/knight-cups-card.jpg`, from the esotericmeanings.com court-cards page), so fidelity is judged against that scan as well as Crowley's verbal description.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact leading
whitespace preserved. **Center on the axis (col 23):** the leaping horse-and-rider mass is
centered on column 23; the diagonal thrust reads across it (leaping LEFT) but the visual
center of the mount sits on the axis. Place asymmetric sprites at `23 - len(s)//2` and
verify with `--axis`. Cells are 1:2 so draw the horse's barrel, the wing fan, the wave
masses, and any curve ~2:1 WIDER than tall or they squash. Courier New; extended alphabet
`´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for
volume (`. : · ' ° :`), never open outlines, lit directionally. Foreground figure (the
winged Knight) drawn ON TOP; break the water and background edges behind him. Full-bleed
to the border. Keep outer frame + bottom title band. Court cards have NO numeral plaque up
top; use the elemental title in the band. Romanized Hebrew letter only in the art, never a
Hebrew glyph. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16
fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift, an under-scaled horse, or a water field that reads as flat backdrop
instead of as the churning surface he leaps out of - for those, use the render & review
loop against the scan.

## Subject
**Knight of Cups.** Tetragrammaton letter Yod (Yod of the Water suit, Fire of Water).
Attribution Fire of Water; rules the Heavens from the 21st degree of Aquarius to the 20th
degree of Pisces (DuQuette rounds it 20 Aquarius to 20 Pisces, Feb 9 to Mar 10). Original
title: Lord of the Waves and the Waters, King of the Hosts of the Sea, King of Nymphs or
Undines. A knight in black winged armour on a leaping white charger, bearing a cup from
which a crab issues, his totem a peacock fashioned of pure water. In natural force he is
Rain and Springs: the swift passionate attack of water, and water's power of solution.

## The composition, in one sentence
A winged knight in dark armour on a leaping WHITE charger erupts LEFTWARD out of a whole
field of churning blue-green water, a peacock plume of water fanning from his wake, a
warm red cup with a crab lifted in his right hand.

Hold those two facts above all else. If you get only two things right, get the pale white
horse leaping out of the water as the bright hero mass, and the water as the whole
FIELD/surface (not a backdrop) with the peacock-plume wake fanning behind the leap.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The leaping white charger is the bright body of the card.** "the leaping attitude of
his white charger" marks the most active aspect of Water. Draw it mid-leap on a forward
diagonal thrusting LEFT (the deliberate counter-motion to the Knight of Wands, who leaps
right on a black horse). It is a large LIGHT dithered mass (density ramp toward WHITE, the
inverse of the Wands horse), the single brightest thing on an otherwise cool card,
centered on the axis (col 23) even though its motion is diagonal. Because cells are 1:2,
draw the barrel wider than tall. This is the #1 compositional read.

**2. He leaps UPON / OUT OF the water.** The whole ground and background of the scan is
churning blue-green water, curling in waves and eddies edge to edge. The water is not a
wash behind him; it is the surface the mount erupts from and is carried on. Fire of Water
made literal, the exact mirror of the Wands Knight riding upon flame. Build a body of
water under and around the horse's legs so the whole figure surges out of it. Rake the
water the same forward diagonal as the leap.

**3. The peacock plume is the water of his wake.** "His totem is the peacock, for one of
the stigmata of water in its most active form is brilliance." Per DuQuette, Harris's
peacock is "fashioned from a plume of pure water created by the wake of the Knight's
movement." So do NOT draw a bird perched on the card. Draw the great curling, eyed fan of
water trailing the leap as ONE thing that is both wave and peacock plume, brilliant with
highlight glints. This is the most beautiful and most ASCII-testing idea in the card.

**4. The winged black armour.** "clothed in black armour furnished with bright wings."
Draw the rider's armour DARK (green-black in the scan), a silhouette against the pale
horse, with a large BRIGHT feathered wing-fan sweeping up and back behind him. The wings
plus the leaping horse together are what signal "the most active aspect of Water." Drawn
ON TOP of horse and water, occlude cleanly behind him. Dither the plate so it reads metal,
the wings so they read feathered.

**5. The cup and the crab, raised.** "In his right hand he bears a cup from which issues a
crab, the cardinal sign of Water, for aggressiveness." Lift the cup high to the upper
right, a WARM red / gold vessel - the single warm accent on an all-cool card - with the
crab shape breaking from its lip. Read the crab even at small scale: it is the fiery
aggression (the Fire of Water) carried inside the vessel of feeling.

**6. Fluorescence / brilliance.** "There is here also some reference to the phenomena of
fluorescence." The active water glints and shimmers with peacock-eye brilliance. Give the
water mass bright highlight glints, not a flat teal fill, so it reads alive and luminous.

**7. The leftward leap rakes everything backward.** The counter-thrust to the Knight of
Wands. DuQuette: he leaps "in the opposite direction than that of the Knight of Wands."
Every trailing element - mane, tail, wing edges, plume-wake water - gets the SAME backward
diagonal off the leftward leap. This consistent rake is what turns a horse-diagram into
the Knight of Cups.

**8. Palette (ANSI/256 + 16-color fallback), observed from the scan.** Map from
`reference/knight-cups-card.jpg`:
   - Field / water: cool blue-green, teal, edge to edge ("cool blues and blue-greens
     dominate this card").
   - Charger: pale white / grey-blue shadow, the brightest mass.
   - Armour: dark green-black metal, dithered plate.
   - Wings: bright pale feathered fan.
   - Peacock plume-wake: blue-green with brilliant eyed highlights.
   - Cup: warm red / gold, the one warm accent; crab at its lip.
   - Hair fair, eyes blue: small warm/cool head accents.
   Introduce no color with no referent in the scan (no fiery reds/oranges beyond the cup;
   this is a cool card, the opposite of the Wands Knight).

**9. Fire of Water as the meaning.** Divinatory tone to honor: graceful, amiable, quick to
respond and enthuse but not enduring; sensitive, innocent and pure but shallow, "his name
is writ in water." Water in action - a pelting rain, a gushing spring, water's patient
power to dissolve. The image should feel like a cool, brilliant surge, all responsive
motion and shimmer, never the hot launch of the Wands Knight. Read fluid and luminous, not
explosive.

**10. The sea and the undine note.** He is Lord of the Waves and the Waters, King of the
Hosts of the Sea, King of Nymphs or Undines. Optional garnish: let the lower/outer field
open into sea, the water elementals implied in the eddies, if it does not clutter the
leap. Small; the white horse, the water-field, and the peacock plume carry the card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the horse's
  barrel, the wing fan, the peacock plume, and any wave curve WIDER than tall or they
  squash. Bake the correction into the geometry.
- **Center on the axis (col 23).** The horse-and-rider mass centers its VISUAL center on
  column 23, not its left edge, even though the leap thrusts LEFT. Place asymmetric sprites
  at `23 - len(s)//2` and confirm with `--axis`. A card whose helm is centered but whose
  horse drifts is the classic tell.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the overline
  glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus
  extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Masses dithered, never outlined.** The white horse (ramp toward white), the water
  field, the dark armour, and the wing fan all get density ramps for volume, lit
  directionally. Occlude: the winged Knight is drawn ON TOP, break water and horse edges
  behind him.
- **Full-bleed density.** Push the composition out to the border. The water fills the
  frame; do not float a small horse in empty space.
- **Card frame:** keep the outer border box. Court cards have NO top numeral plaque.
  Bottom title band, two lines: `KNIGHT OF CUPS` then `~ yod . fire of water ~`.
  Romanized letter only, never a Hebrew glyph in the art.

## Render & review
Do not judge horse scale, the water-as-field read, the peacock-plume wake, the backward
rake, placement, or palette by reading the source. Run the chain and LOOK:
`compose_knight-cups_lg.py` -> `frame.py` (`-s cups`, no `-n` numeral for a court card) ->
`cardkit.py knight-cups` -> `render_png.py knight-cups --axis`, then OPEN the PNG and
critique it against `reference/knight-cups-card.jpg` (the scan now exists, so judge against
it, not only the text): is the white horse a large bright mass leaping LEFT on the
diagonal, centered on the axis guide? does the water read as the whole FIELD he erupts
from, not a backdrop? does the peacock plume read as the eyed water of his wake, not a
perched bird? is the armour dark with a bright wing fan, drawn ON TOP with clean occlusion?
is the cup a single warm accent with a crab at its lip? is the palette cool teal /
pale-white / dark green-black with only the one warm cup, no stray fiery colors? Fix the
compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note:
`knight-cups` must be in `cardkit.CONFIGS` before render_png will run. See
FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate, judging
against the Harris scan `reference/knight-cups-card.jpg`), three judges scoring each, then
synthesis / polish / integration merging the strongest read. Three strategies to seed the
composers:
- **A. Horse-dominant** - the leaping WHITE charger is the bright hero mass filling the
  frame, the winged rider small on its back, water at the hooves and a plume behind.
- **B. Water-field dominant** - the churning blue-green water he leaps OUT OF is the
  subject, edge to edge, with the horse and rider erupting from it; the Fire-of-Water
  thesis made the visual field.
- **C. Peacock-plume dominant** - the great eyed fan of water-as-peacock trailing the
  leftward wake is the hero curve, the horse and rider read against it.
Tier: **full panel** - the white-horse-as-bright-mass, the water-as-field read, and the
peacock-plume-as-water-wake are hard and easy to get wrong (especially not drawing a
perched bird), so spend the full cost.

## Output
- One large-format art block (target the standard `-art-lg.txt` 47x32 dimensions).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive
  8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A winged Knight on a leaping WHITE charger erupts LEFTWARD out of a whole field of
blue-green water, a peacock plume of water fanning from his wake, one warm crab-cup raised.
Get the bright white horse, the water-as-field, and the plume-as-wake and the card stops
being a diagram.
