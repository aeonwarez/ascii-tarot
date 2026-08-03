# Fable5 Prompt - Queen of Wands (Thoth court card)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is
not to draw a diagram of the card's symbols but to reproduce the *composition
and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's
iconography AND to the feel of the original image both matter. Work in a
fixed-width grid, Courier New assumed. Note: no Harris scan of the court cards
exists in this repo, so you judge against Crowley's verbal description in the
Book of Thoth, not against a pixel reference.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved on every line. **Center on the axis (col 23):**
the enthroned Queen and her throne of flame are the stage, centered on column
23; her seated mass is balanced about the axis, the leopard couchant to one
side offsetting the wand held in her left hand. Place asymmetric sprites at
`23 - len(s)//2` and verify with `--axis`. Cells are 1:2 so draw circles and
curves (the winged globe, the leopard's flank, the crown rays) about 2:1 wider
than tall. Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never open
outlines, lit directionally. Foreground figure drawn ON TOP; break background
edges (throne flame, background fire) behind her. Full-bleed to the border.
Keep outer frame + bottom title band. Courts have NO numeral plaque; use the
elemental title band. Sign `aw` or unsigned, never `jgs`. Output one `.txt` +
one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis and clean compositor
structure. It does NOT fix placement drift, an under-scaled throne, or the
calm-fire-vs-blaze read - for those, use the render & review loop.

## Subject
**Queen of Wands.** Water of Fire (the watery part of Fire, its fluidity and
colour). Tetragrammaton: He primal (first He) of the fire-suit; she receives,
ferments, and transmits the Knight's energy, seated upon her throne. Rules 21
degrees Pisces to 20 degrees Aries; dominates cardinal Aries. GD title: Queen
of the Thrones of Flame, Queen of the Salamanders. Her Water is the calming,
modulating influence that orders Fire into geometrical light.

## The composition, in one sentence
An enthroned queen sits still and in-drawn upon a throne of steady, geometrical
flame, one hand resting on a couchant leopard, the other holding a cone-topped
wand, her red-gold hair spilling over scaled mail.

Hold two facts above all else: the fire is CALM and ORDERED here (not the
Knight's blaze), and she is IN-DRAWN, not outward-facing. If you get only two
things right, get the geometrical-steady flame and the meditative, receptive
stillness.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The throne of flame is the stage, and the flame is STEADY.** "She is
seated upon a throne of flame, ordered into geometrical light by her material
power. Beneath the throne the surging flames are steady." This is the single
most important read: her Water calms Fire into rectilinear, faceted geometry.
Draw the throne as a large dithered flame-mass with ordered, faceted edges
(`/\_/\_` steps, not chaotic tongues) centered on the axis. Contrast this
deliberately with the Knight of Wands' waving, exploding flames. Dither for
volume (`. : · ' °`), never open outline.

**2. The Queen enthroned, in-drawn and receptive.** She sits (Queens are
always throned - they exercise a definite function). Her pose is still and
balanced about the axis, "the ecstasy of one whose mind is well in-drawn to
the mystery borne beneath her bosom." Half-lidded eyes, meditative, not
frontal-staring. Rebuild the body as a calm seated S-curve, hair flowing down,
not a stiff stick figure. She is Water: fluid line, not rigid.

**3. The couchant leopard, her hand on its head.** "She is attended by a
couchant leopard upon whose head she lays her hand." The winged/crested
leopard lies low beside the throne; her hand rests on its skull. This contact
reads calm authority over animal fire. Draw it couchant (lying, head up),
spotted with a `:` dither, offset to one side of the axis to balance the wand.
Occlude cleanly where her arm crosses it.

**4. The cone-topped wand in her LEFT hand.** "She bears a wand in her left
hand; but it is topped with a cone suggestive of the mysteries of Bacchus."
Held in the left hand specifically. The tip is a fir-cone / thyrsus, not a
plain rod or a lotus. Make the cone legible (`.(A).` or a small dithered pine
shape), and keep it on the correct (her left) side.

**5. Crown of the winged globe, rayed with flame; red-gold hair on scaled
mail.** "Her crown is topped with the winged globe and rayed with flame. Her
long red golden hair flows down upon her armour of scaled mail." Three linked
reads: a winged-globe crest atop the crown, flame-rays around it, and long
red-gold hair spilling over a scaled-mail shoulder (`<><>` scale texture under
the flowing hair). She is armoured, not merely robed.

**6. Water of Fire - cool the palette, do not scorch it.** Unlike the Knight's
scarlet blaze, her fire is watery: translucent, reflective, modulated. The
suit theory links the watery part of Fire to the Rainbow (Sagittarius
harmony). Keep reds/golds but let them read cooled and luminous, fire seen
through water, not a bonfire.

**7. Palette (ANSI/256 + 16-color fallback), text-derived (no scan).** Map
strictly from Crowley's color words:
   - Hair: red-gold (BoT; DuQuette confirms).
   - Fire / throne / crown rays: reds, oranges, golds - but cooled and
     translucent per directive 6.
   - Armour: brass / gold-toned scaled metal.
   - Leopard: tawny with dark spots (inferred from the animal named; not
     color-specified in text).
   - Winged globe crest: gold.
   "Fiery reds, yellows, and gold dominate this card, as they do all the Wand
   court cards" (DuQuette). Introduce no color with no referent in the text.

**8. Order-out-of-fire as the visual thesis.** The whole card is Fire brought
to geometrical order by Water. Everywhere the untempered suit would flicker
wildly, here it is squared, stepped, steadied. Let the negative space around
her read as calmed heat-haze (soft dithered sweep), not dead black and not a
raging field.

**9. Meaning as tone: calm authority with a proud edge.** Divinatory sense to
honor: adaptability, persistent energy, calm authority used to enhance
attractiveness; kindly and generous but impatient of opposition; immense
capacity for love, always on her own initiative. The shadow is vanity and
snobbery ("when she misses her bite, she breaks her jaw"). Render her noble
and self-possessed, monument-still, with just a hint of the facade DuQuette
names.

**10. Witnesses / garnish.** The mystery borne beneath her bosom (an in-drawn
gestation, suggested by pose, not a literal object); the salient steady flames
at the throne's foot; the fir-cone's Bacchic hint. Small, supporting. Garnish,
but it is the difference between Thoth and a generic queen on a chair.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  winged globe, crown, and leopard flank WIDER than tall or they render as
  squashed eggs. Bake the correction into every circle and curve.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs
  `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border. The
  painting is edge-to-edge; do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer border box. Courts carry
  NO numeral plaque up top. Bottom band line 1: `QUEEN OF WANDS`; line 2:
  `~ he . water of fire ~`. Romanized letter only in the art; the real Hebrew
  glyph lives in site chrome (HTML), never in the `.txt` / `.ans`.

## Render & review
Do not judge throne scale, the steady-vs-blazing flame contrast, placement, or
palette by reading the source. Run the chain and LOOK:
`compose_queen-wands_lg.py` -> `frame.py` -> `cardkit.py queen-wands` ->
`render_png.py queen-wands --axis`, then OPEN the PNG and critique it. NOTE: no
Harris scan exists for the court cards, so judge against Crowley's verbal
description in the Book of Thoth (throne of flame ordered into geometrical
light; steady flames beneath; couchant leopard with her hand on its head;
cone-topped wand in the left hand; winged-globe crown rayed with flame;
red-gold hair on scaled mail; in-drawn ecstatic face). Is the throne big enough
to be the STAGE with the Queen centered on the axis guide? Does the flame read
STEADY and geometrical, not a wild blaze? Is the leopard couchant and clearly
attended? Is the wand in her left hand with a cone tip? Is the palette cooled
red / gold / brass / tawny with no stray colors? Fix the compositor and repeat.
Ship at ~80% once the render holds (2-3 passes max). Note: `queen-wands` must
be in `cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md
"Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three
composer agents in parallel (each running the Render & review loop above to a
finished candidate, viewing its own PNG each pass and judging against Crowley's
verbal description since no scan exists), three judges scoring each candidate
on iconographic fidelity to the text, composition/energy, legibility at 47x32,
occlusion, and palette, then synthesis / polish / integration merging the
strongest read. Three strategies to seed the composers:
- **A. Throne-as-stage dominant** - the great geometrical throne of flame is
  the field; the Queen sits enthroned and centered within it, the leopard low
  at its foot.
- **B. Figure-dominant** - the noble, in-drawn Queen is the hero (DuQuette's
  monument facade), the throne a backdrop flame-mass behind her, crown and
  red-gold hair carrying the read.
- **C. Calm-fire-field dominant** - the whole card is Fire ordered by Water:
  steady geometrical flame everywhere, the single contrast being the living
  leopard and the fluid figure against the squared-off blaze.
Tier: **full panel** - contested read (the steady/geometrical flame vs. the
suit's default blaze, and the seated fluid figure) justifies the full cost.

## Output
- One large-format art block (target the existing large-format card dimensions,
  47x32 art / 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette
  from directive 7 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
An enthroned queen sits still and in-drawn on a throne of steady geometrical
flame, hand on a couchant leopard, cone-wand in her left hand: get the calm
ordered fire and the receptive stillness and the card stops being a queen on a
chair.
