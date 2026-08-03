# Fable5 Prompt - Knight of Swords (Thoth)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is not
to draw a diagram of the card's symbols but to reproduce the *composition and
energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's
iconography AND to the feel of the original image both matter. Work in a
fixed-width grid, Courier New assumed. NOTE: this is a court card, but UNLIKE the
other court cards in this repo a Harris scan IS available
(`reference/knight-swords-card.jpg`, from the esotericmeanings.com court-cards
page). Judge fidelity against that scan, not against the text alone.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the rushing
warrior-and-steed mass is centered on column 23; the plunge reads on a steep
diagonal across it, but the visual center of the figure sits on the axis. Place
asymmetric sprites at `23 - len(s)//2` and verify with `--axis`. Cells are 1:2 so
draw the wing-fan, the horse barrel, the cloud sweeps, and any curves ~2:1 WIDER
than tall or they squash. Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume (`. : · ' ° :`),
never open outlines, lit directionally. Foreground figure (the armoured Knight)
drawn ON TOP; break the cloud and wind edges behind him. Full-bleed to the border.
Keep outer frame + bottom title band. Court cards have NO numeral plaque up top;
use the elemental title in the band. Romanized Hebrew letter only in the art,
never a Hebrew glyph. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one
`.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis and clean compositor structure.
It does NOT fix placement drift, an under-scaled wing-fan, or a wind field that
reads as flat backdrop instead of as the storm he embodies - for those, use the
render & review loop against the scan.

## Subject
**Knight of Swords.** Tetragrammaton letter Yod (Yod of the suit of Air, Fire of
Air). Attribution Fire of Air; rules 21 degrees Taurus to 20 degrees Gemini.
Original title: The Lord of the Winds and Breezes, King of the Spirits of Air,
King of the Sylphs and Sylphides. A helmed warrior on a maddened steed, driving
down the Heavens as the Spirit of the Tempest, a revolving wing for his crest, a
sword in one hand and a poniard in the other. He is the wind and the storm: the
violent power of motion applied to an apparently manageable element.

## The composition, in one sentence
A helmed warrior on a maddened brown steed dives head-first DOWN the sky, four
veined dragonfly wings spinning behind him and sword and poniard thrust forward,
the whole field raked into driving storm-wind on the plunge diagonal.

Hold those two facts above all else. If you get only two things right, get the
headlong downward plunge (he DRIVES DOWN the Heavens, not upright) and the
revolving four-wing fan behind the helm, with everything raked the same diagonal
by the storm.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. He drives DOWN the Heavens, head-first.** "Mounted upon a maddened steed, he
drives down the Heavens, the Spirit of the Tempest." The single most-missed read:
the figure is not an upright equestrian, he is a body thrown headlong down the
sky on a steep forward/downward diagonal. Build the whole mass plunging, head low,
weapons leading. Centered on the axis (col 23) even though the motion is diagonal.
This is the #1 compositional read.

**2. The revolving wing crest, four veined wings.** "for his crest he bears a
revolving wing." DuQuette: what look at first like four propeller blades spinning
atop his pointed helmet are four transparent, veined dragonfly-style wings (maybe
two moving so fast they read as four). This spinning angular fan is the signature
of the whole suit of Swords and the loudest shape on the card. Draw it as a
whirling angular fan of veined translucent wings, `\ | /` blades with `` `.,-'' ``
vane lines, NOT a solid block and NOT feathered bird-wings.

**3. Sword and poniard, both.** "In one hand is a sword, in the other a poniard."
Two blades, not one. He represents the idea of attack. Give him a long sword and a
shorter dagger, both driven forward ahead of the plunge, leading the dive.

**4. The maddened brown steed, driven down.** "Mounted upon a maddened steed."
DuQuette symbol note: a winged brown horse. Draw the mount as a warm brown
dithered mass carried in the dive beneath and behind the rider, driven downward
through the tempest, not a calm standing horse. Because cells are 1:2, draw the
horse's barrel wider than tall.

**5. He IS the wind and the storm; rake the whole field.** He is "the wind, the
storm... the violent power of motion applied to an apparently manageable element."
The air is not a neutral backdrop; it is the driving medium he embodies. Rake the
entire field into streaming wind-lines on the plunge diagonal, and tear driving
cirrus clouds ("driving clouds," DuQuette symbol) along the same path. One
consistent rake governs the card: wings, clouds, horse, blades, all lean the same
way, thrown by the headlong dive. This consistent rake is what turns a
warrior-diagram into the Spirit of the Tempest.

**6. Birds driven before the storm.** Small dark swallows scatter ahead of and
below him (visible lower right on the scan), blown before the tempest. Witnesses
of the wind, the airy suit's small life driven along. Small, lower right.

**7. The armoured warrior, helmed, in green-gold scale.** "a warrior helmed" in
complete armour as all Knights are (they are the Yod, the most active original
part of the Element). On the scan the plate reads golden-yellow over green scale.
Draw him ON TOP of horse and wind, occlude cleanly, dither the plate so it reads
metal, not a flat body. Pointed helm under the spinning wing-fan.

**8. Palette (ANSI/256 + 16-color fallback), scan-observed.** A scan exists;
observe it and map deliberately (cross-checked with DuQuette's "sky blues,
yellows, and white cirrus clouds dominate this card"):
   - Field / sky: pale sky blue, streaked with white and blue driving cirrus.
   - Armour: golden-yellow over green scale, dithered plate.
   - Wing-fan: pale translucent, near-colorless blue-white with darker vanes.
   - Steed: warm brown / tan.
   - Blades (sword + poniard): muted brown-steel (DuQuette: "drawn brown sword"),
     not bright silver.
   - Hair: dark brown; eyes: dark. Birds: small dark swallows.
   Sky blue, yellow, green, brown, white cirrus dominate. Introduce no color with
   no referent in the scan or text.

**9. Fire of Air as the meaning.** Divinatory tone to honor: the one word is
attack. Activity and skill, subtlety and cleverness; fierce, delicate and
courageous, but altogether the prey of his idea, which comes as an inspiration
without reflection. The image should read as a storm-front of pure intellect,
swift and violent and transient, all forward-and-down, no reserve. Hot-minded and
plunging, never static.

**10. The "extended flame of mind."** Crowley's synthesis: "the extended flame of
mind... the True Will exploding the mind spontaneously," a light-shaft of the
Ideal passing from earthy Taurus to exalted Gemini. Optional garnish: a single
thin bright shaft or lance of light read through the plunge if it does not clutter
the storm. Small; the plunge and the wing-fan carry the card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  wing-fan, the horse's barrel, and any curve WIDER than tall or they squash. Bake
  the correction into the geometry.
- **Center on the axis (col 23).** The warrior-and-steed mass centers its VISUAL
  center on column 23, not its left edge. Place asymmetric sprites at
  `23 - len(s)//2` and confirm with `--axis`. A card whose helm is centered but
  whose plunging body leans off-axis is the classic tell.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Masses dithered, never outlined.** The brown steed, the green-gold armour, and
  the cloud sweeps get density ramps for volume, lit directionally. The wing-fan
  is the exception: translucent veined blades, not a solid mass. Occlude: the
  armoured Knight is drawn ON TOP, break wind and cloud edges behind him.
- **Full-bleed density.** Push the composition out to the border. The storm fills
  the frame; do not float a small figure in empty sky.
- **Card frame:** keep the outer border box. Court cards have NO top numeral
  plaque. Bottom title band, two lines: `KNIGHT OF SWORDS` then
  `~ yod . fire of air ~`. Romanized letter only, never a Hebrew glyph in the art.
  Frame with `tools/frame.py -s swords` (no `-n` numeral for a court card).

## Render & review
Do not judge the plunge angle, the wing-fan scale, the storm-as-field read,
placement, or palette by reading the source. Run the chain and LOOK:
`compose_knight-swords_lg.py` -> `frame.py` (`-s swords`, no `-n` numeral for a
court card) -> `cardkit.py knight-swords` -> `render_png.py knight-swords --axis`,
then OPEN the PNG and critique it against `reference/knight-swords-card.jpg`: does
the figure DRIVE DOWN the sky head-first on a steep diagonal, centered on the axis
guide? does the four-wing fan spin behind the helm as veined translucent blades,
not feathered wings or a solid block? are BOTH the sword and the poniard present
and leading the dive? is the brown steed a dithered mass driven downward beneath
him? is the whole field raked into driving storm-wind and cirrus on the plunge
diagonal? is the palette sky-blue / green-gold / brown / white-cirrus with no
stray colors? Fix the compositor and repeat. Ship at ~80% once the render holds
(2-3 passes max). Note: `knight-swords` must be in `cardkit.CONFIGS` before
render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer
agents in parallel (each running the Render & review loop above to a finished
candidate, judging against `reference/knight-swords-card.jpg`), three judges
scoring each against the scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Plunge-dominant** - the headlong head-first dive down the Heavens is the
  subject; warrior, steed, blades, and wings are one raked diagonal streak driving
  down the sky.
- **B. Wing-fan dominant** - the four spinning veined dragonfly wings are the hero
  shape, a whirling angular fan filling the upper card, the diving figure hung
  beneath it.
- **C. Storm-field dominant** - the driving wind and torn cirrus he embodies fill
  the whole field, the rider and steed erupting from the tempest as its living
  center, the Fire-of-Air thesis made the visual field.
Tier: **full panel** - the plunge angle, the veined wing-fan read, and the
consistent storm rake are hard and easy to get wrong, so spend the full cost.

## Output
- One large-format art block (target the standard `-art-lg.txt` 47x32 dimensions).
- Provide both a plain `.txt` version and a `.ans` version with the palette from
  directive 8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A helmed warrior on a maddened brown steed dives head-first DOWN the sky, four
veined wings spinning behind him, sword and poniard leading, the whole field raked
into storm-wind. Get the downward plunge and the spinning wing-fan and the card
stops being a diagram.
