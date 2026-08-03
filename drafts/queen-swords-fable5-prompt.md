# Fable5 Prompt - Queen of Swords (Thoth court card)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is
not to draw a diagram of the card's symbols but to reproduce the *composition
and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's
iconography AND to the feel of the original image both matter. Work in a
fixed-width grid, Courier New assumed. Note: a Harris scan of this court card
DOES exist in this repo (`reference/queen-swords-card.jpg`, esotericmeanings.com
court-cards page), so judge against the pixel reference, not only the text.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved on every line. **Center on the axis (col 23):** the
enthroned Queen and the great cloud bank she rides are the stage, centered on
column 23; her seated mass is balanced about the axis, the upright sword in her
right hand offsetting the severed head hung low from her left hand. Place
asymmetric sprites at `23 - len(s)//2` and verify with `--axis`. Cells are 1:2
so draw circles and curves (the cumulus lobes, the child's-head crest, the ray
burst) about 2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` +
line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume,
never open outlines, lit directionally. Foreground figure drawn ON TOP; break
background edges (cloud lobes, ray streaks) behind her. Full-bleed to the
border. Keep outer frame + bottom title band. Courts have NO numeral plaque; use
the elemental title band. Sign `aw` or unsigned, never `jgs`. Output one `.txt`
+ one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis and clean compositor
structure. It does NOT fix placement drift, an under-scaled cloud bank, or the
upright-sword-vs-hung-head balance - for those, use the render & review loop.

## Subject
**Queen of Swords.** Water of Air (the watery part of Air, its elasticity and
its power of transmission). Tetragrammaton: He primal (first He) of the
air-suit; she receives, ferments, and transmits the Knight's energy, seated upon
her throne. Rules 21 degrees Virgo to 20 degrees Libra; dominates cardinal
Libra. GD title: Queen of the Thrones of Air, Queen of the Sylphs and Sylphides.
She is the clear, conscious perception of Idea, the Liberator of the Mind; she
has cut the higher intellect free of the lower animal soul with the sword of
reason.

## The composition, in one sentence
A helmed queen sits enthroned upon a vast bank of cumulus cloud, an upright drawn
sword in her right hand and the newly severed, peacefully-sleeping bearded head
in her lowered left hand, sharp rays of light streaming from the winged
child's-head crest of her helm.

Hold two facts above all else: she rides the CLOUDS as her stage (not a solid
throne), and the read is the SEVERANCE, the upright sword above and the severed
head hung low. If you get only two things right, get the cumulus-bank-as-stage
and the sword-up / head-down vertical severance.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The cloud bank is the stage.** "She is enthroned upon the clouds." A vast
bank of cumulus fills the lower half and is the field she rides; there is no
solid throne. In the scan it is a huge cream-white cumulus mass, soft-lit,
rounded. Draw it large and dithered for volume (`.oOOo.` lobes, `. : ' °`
density ramp), never an open outline row. This is the #1 compositional fix: the
figure sits IN FRONT OF and UPON the cloud, centered on the axis.

**2. The upright sword in her RIGHT hand.** "In her right hand, she bears a
sword." A drawn, vertical blade, the sword of discretion and reason that did the
severing. Keep it rigid and upright (`|` blade, `-+-` guard, `T` pommel), held
on her right side (viewer's left). This vertical is the spine of the card's
read.

**3. The newly severed bearded head in her LEFT hand, hung LOW.** "In her left
hand, the newly severed head of a bearded man." It hangs down from her lowered
left hand (viewer's right), eyes closed peacefully, the face in the trance of
deep meditation (DuQuette: the Hermit of Virgo perhaps). Draw it small, bearded,
eyes-closed (`,(-.-),` with a beard hint), hung low to balance the raised sword
about the axis. This is NOT a grisly flourish: she is the Liberator of the Mind,
the intellect cut free of the animal soul. Occlude cleanly where her arm crosses
the cloud behind.

**4. The child's-head crest streaming sharp rays.** "Her helmet is crested by
the head of a child, and from it stream sharp rays of light, illuminating her
empire of celestial dew." A winged child's head atop the helm, sharp rays
radiating out. In the scan the ray burst reads green-toned behind and above the
head. Make the rays SHARP and radiating (`\ | / `), not a soft halo, and keep
the tiny child's head legible on the crest.

**5. Helmed, naked above the belt, gleaming belt, sarong below.** "The upper part
of her body is naked, but she wears a gleaming belt and a sarong. Her helmet
is..." Three linked reads: a war helm (crowned by the child crest), bare upper
body, a gleaming belt at the waist, and a sarong draped below (gray-blue in the
scan). She is martial Air made regal, not softly robed.

**6. Water of Air - elasticity and transmission, cool the palette.** She is the
watery part of Air: its elasticity and its power of transmission. DuQuette:
clouds that promise either life-giving rain or the threat of a torrential
cloudburst. Keep the whole field cool and airy, sky-blue with cream cumulus,
loaded and latent, not scorched or heavy.

**7. Palette (ANSI/256 + 16-color fallback), OBSERVED from the scan.** A Harris
scan exists, so map from the painting:
   - Sky / field: streaked mid sky-blue with paler wash, fine pale crackle lines
     (DuQuette: "Sky blues ... dominate this card").
   - Cloud bank: cream-white cumulus, the largest mass, soft-lit.
   - Crest rays: green-toned radiant burst behind and above the head.
   - Figure: pale flesh upper body.
   - Drapery / sarong: gray-blue; belt gleaming lighter.
   - Sword: pale steel / light gray, upright.
   - Severed head: small, greenish-toned, hung low.
   - Touches of pale yellow light (DuQuette lists yellows).
   Introduce no color with no referent in the scan or text.

**8. Severance as the visual thesis.** The whole card is separation by the
intellect: the sword up, the head down, the higher faculties cut free of the
lower. Let the vertical read (upright blade above, severed head below, the
figure poised in Libran balance between) carry the composition. She is clear,
conscious perception, exact and graceful.

**9. Meaning as tone: keen, exact, gracious, and dangerous.** Divinatory sense
to honor: intensely perceptive, a keen observer, a subtle interpreter, swift and
accurate at recording ideas; in action confident, in spirit gracious and just;
graceful movements, exceptional balance. The shadow (ill-dignified): cruel, sly,
deceitful, unreliable, dangerous through her superficial beauty. Render her
poised and perceptive, monument-composed (Crowley's own Sun sign, the most
intimidating lady in the deck: she means business), with just the edge of the
shadow.

**10. Witnesses / garnish.** The empire of celestial dew the rays illuminate
(scattered dew flecks `. ' .` in the air field); the loaded cumulus that could
break into rain; the Libran poise of a figure held in perfect balance above the
clouds. Small, supporting. Garnish, but it is the difference between Thoth and a
generic queen with a sword.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  cumulus lobes, the child's-head crest, and the ray burst WIDER than tall or
  they render as squashed eggs. Bake the correction into every circle and curve.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs
  `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border. The painting
  is edge-to-edge; do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer border box. Courts carry NO
  numeral plaque up top. Bottom band line 1: `QUEEN OF SWORDS`; line 2:
  `~ he . water of air ~`. Romanized letter only in the art; the real Hebrew
  glyph lives in site chrome (HTML), never in the `.txt` / `.ans`.

## Render & review
Do not judge cloud-bank scale, the sword-up / head-down severance, placement, or
palette by reading the source. Run the chain and LOOK:
`compose_queen-swords_lg.py` -> `frame.py` -> `cardkit.py queen-swords` ->
`render_png.py queen-swords --axis`, then OPEN the PNG and critique it against
`reference/queen-swords-card.jpg`. Is the cumulus bank big enough to be the
STAGE with the Queen enthroned upon it, centered on the axis guide? Is the sword
upright in her right hand? Is the severed bearded head hung low in her left,
eyes closed? Do sharp rays stream from the child's-head crest? Is the palette
sky-blue / cream cumulus / gray-blue drape / green crest-rays with no stray
colors? Fix the compositor and repeat. Ship at ~80% once the render holds (2-3
passes max). Note: `queen-swords` must be in `cardkit.CONFIGS` before render_png
will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer
agents in parallel (each running the Render & review loop above to a finished
candidate, viewing its own PNG each pass and judging against the Harris scan +
Crowley's verbal description), three judges scoring each candidate on
iconographic fidelity, composition/energy, legibility at 47x32, occlusion, and
palette, then synthesis / polish / integration merging the strongest read. Three
strategies to seed the composers:
- **A. Cloud-as-stage dominant** - the vast cream cumulus bank is the field; the
  Queen sits enthroned upon it, small and poised, the whole lower half cloud.
- **B. Figure-dominant** - the helmed, perceptive Queen is the hero (Crowley's
  intimidating Sun-sign lady), the cloud a backdrop mass behind her, sword and
  severed head carrying the read.
- **C. Severance-field dominant** - the whole card is separation by intellect:
  the upright sword above and the severed head below as the single dominant
  vertical, the figure balanced Libra-still between them, cloud and rays framing.
Tier: **full panel** - contested read (the cloud-as-throne stage, and the
sword-up / head-down severance balanced about the axis) justifies the full cost.

## Output
- One large-format art block (target the existing large-format card dimensions,
  47x32 art / 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette from
  directive 7 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A helmed queen enthroned upon a vast cumulus bank, upright sword in her right
hand, severed sleeping bearded head hung low in her left, sharp rays streaming
from a child's-head crest: get the cloud-as-stage and the sword-up / head-down
severance and the card stops being a queen with a weapon.
