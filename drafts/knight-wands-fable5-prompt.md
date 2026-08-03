# Fable5 Prompt - Knight of Wands (Thoth)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed. NOTE: this is a court card. There is no Harris scan of it in the repo (only the 22 trumps are scanned), so fidelity is judged against Crowley's verbal description, not a scan.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact leading
whitespace preserved. **Center on the axis (col 23):** the leaping horse-and-rider mass is
centered on column 23; the diagonal thrust reads across it but the visual center of the
mount sits on the axis. Place asymmetric sprites at `23 - len(s)//2` and verify with
`--axis`. Cells are 1:2 so draw the horse's body, the flame masses, and any curves ~2:1
WIDER than tall or they squash. Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume (`. : · ' ° :`),
never open outlines, lit directionally. Foreground figure (the armoured Knight) drawn ON
TOP; break the flame and background edges behind him. Full-bleed to the border. Keep outer
frame + bottom title band. Court cards have NO numeral plaque up top; use the elemental
title in the band. Romanized Hebrew letter only in the art, never a Hebrew glyph. Sign
`aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift, an under-scaled horse, or a flame ground that reads as backdrop instead
of as the surface he rides on - for those, use the render & review loop.

## Subject
**Knight of Wands.** Tetragrammaton letter Yod (Yod of Yod, Fire of Fire). Attribution
Fire of Fire; rules 21 degrees Scorpio to 20 degrees Sagittarius. Original title: The Lord
of the Flame and the Lightning, King of the Salamanders. A warrior in complete golden
armour on a leaping black horse, riding upon flames, waving a flaming torch. In natural
force he is the Lightning flash: swift, violent, transient.

## The composition, in one sentence
An armoured warrior on a rearing black horse rides UPON a body of flame, mane and cloak and
hair all blown backward by the forward thrust, as if riding a rocket.

Hold those two facts above all else. If you get only two things right, get the leaping
black horse as a dark dithered mass and the flame as the GROUND he rides on (not a
backdrop), with everything trailing raked backward by the blast.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The leaping black horse is the body of the card.** "His steed is a black horse
leaping." Draw it rearing / mid-leap on a forward diagonal, a large DARK dithered mass
(density ramp toward black, not an open outline horse). It is centered on the axis (col 23)
even though its motion is diagonal. Because cells are 1:2, draw the barrel of the horse
wider than tall. This is the #1 compositional read.

**2. He rides UPON the flames.** "upon the flames does he ride." The fire is not a
background wash behind him; it is the ground / surface the mount is carried on and out of.
Fire of Fire made literal. Build a body of flame under and around the horse's legs so the
whole figure erupts from it. Rake the flame the same forward diagonal as the leap.

**3. The forward blast rakes everything backward.** DuQuette's key read: the mane, tail,
hair, beard, cloak, and flames are not merely in motion, they are "blown from behind by
some unimaginably strong explosive force." He is riding a rocket. Every trailing element
gets the SAME backward diagonal (`\ \` or `/ /` depending on facing). This single
consistent rake is what turns a horse-diagram into the Knight of Wands.

**4. The armoured warrior, in complete armour.** "a warrior in complete armour." Golden /
scarlet-gold plate, seen in violent forward motion, drawn ON TOP of the horse and flame
(occlude cleanly behind him). Knights wear complete armour BECAUSE they are the Yod, the
most active original part of the Element. Dither the plate so it reads metal, not a flat
body.

**5. The flaming torch and the crest.**
   - **Flaming torch / club, raised in his hand:** "In his hand he bears a flaming torch."
     A waving flame lifted, the weapon of the suit of Fire.
   - **The black-horse crest on the helm:** "On his helmet for a crest he wears a black
     horse" (a WINGED black horse's head). The horse doubled - the mount below, the winged
     horse-head crest above the helm. Read the crest even at small scale.

**6. The flaming mantle.** "a flame also in his mantle." A scarlet-gold cloak that is
itself on fire, streaming backward in the blast (directive 3). Not a static cape - a
trailing tongue of flame-cloth.

**7. Salamander texture.** He is King of the Salamanders. Let flame-tongues lick through
the mass as texture where space allows, so the fire reads alive, not a flat orange fill.

**8. Palette (ANSI/256 + 16-color fallback), text-derived (no scan).** Map from Crowley's
color words only:
   - Horse (mount + crest head): black / darkest.
   - Armour: gold / warm metal, dithered plate.
   - Flames, torch, mantle-fire: scarlet and gold ("waving flames," "scarlet gold cloak").
   - Cloak / mantle: scarlet-gold.
   - Hair and beard: red-gold.
   - Eyes: a small grey / hazel cool highlight on the visor.
   Fiery reds, yellows, and gold dominate, as in all the Wand court cards. Introduce no
   color with no referent in the text (no blues/greens).

**9. Fire of Fire as the meaning.** Divinatory tone to honor: activity, generosity,
fierceness, impetuosity, pride, impulsiveness, swiftness in unpredictable actions. The
lightning flash - swift, violent, transient. Potentially the strongest of the court, but
brittle: no resource if the first effort fails. The image should feel like a launch, all
forward, no reserve. Read hot and explosive, never static.

**10. The lightning-flash note.** In natural force the Knight of Wands is the Lightning
flash. Optional garnish: a single jagged flash-glyph read in the flame or sky if it does
not clutter the blast. Small; the horse and the fire-ground carry the card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the horse's
  barrel, the flame masses, and any curve WIDER than tall or they squash. Bake the
  correction into the geometry.
- **Center on the axis (col 23).** The horse-and-rider mass centers its VISUAL center on
  column 23, not its left edge. Place asymmetric sprites at `23 - len(s)//2` and confirm
  with `--axis`. A card whose helm is centered but whose horse leans is the classic tell.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the overline
  glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus
  extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Masses dithered, never outlined.** The black horse and the flame get density ramps for
  volume, lit directionally. Occlude: the armoured Knight is drawn ON TOP, break flame and
  horse edges behind him.
- **Full-bleed density.** Push the composition out to the border. The blast fills the
  frame; do not float a small horse in empty space.
- **Card frame:** keep the outer border box. Court cards have NO top numeral plaque.
  Bottom title band, two lines: `KNIGHT OF WANDS` then `~ yod . fire of fire ~`.
  Romanized letter only, never a Hebrew glyph in the art.

## Render & review
Do not judge horse scale, the flame-as-ground read, the backward rake, placement, or
palette by reading the source. Run the chain and LOOK: `compose_knight-wands_lg.py` ->
`frame.py` (`-s wands`, no `-n` numeral for a court card) -> `cardkit.py knight-wands` ->
`render_png.py knight-wands --axis`, then OPEN the PNG and critique it. There is NO Harris
scan to compare against for court cards, so judge fidelity against Crowley's verbal
description instead: is the black horse a large dark mass leaping on the diagonal, centered
on the axis guide? does the fire read as the GROUND he rides UPON, not a backdrop? is
everything (mane, tail, hair, cloak, flames) raked the same backward diagonal by the blast?
is the armour gold plate drawn ON TOP with clean occlusion? is the palette black / gold /
scarlet with no stray colors? Fix the compositor and repeat. Ship at ~80% once the render
holds (2-3 passes max). Note: `knight-wands` must be in `cardkit.CONFIGS` before
render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate, judging
against Crowley's verbal description since there is no scan), three judges scoring each,
then synthesis / polish / integration merging the strongest read. Three strategies to seed
the composers:
- **A. Horse-dominant** - the leaping black horse is the hero mass filling the frame, the
  rider small on its back, fire at the hooves.
- **B. Blast-dominant** - the forward explosive thrust is the subject; horse, rider, cloak,
  and flame are all one raked diagonal streak, riding a rocket.
- **C. Flame-ground dominant** - the body of fire he rides UPON fills the lower card and
  erupts around the mount, the Fire-of-Fire thesis made the visual field.
Tier: **full panel** - the horse scale, the flame-as-ground read, and the consistent
backward rake are hard and easy to get wrong, so spend the full cost.

## Output
- One large-format art block (target the standard `-art-lg.txt` 47x32 dimensions).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive
  8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
An armoured Knight on a leaping black horse rides UPON a body of flame, everything raked
backward by the blast. Get the dark horse mass and the fire-as-ground and the card stops
being a diagram.
