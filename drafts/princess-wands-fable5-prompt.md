# Fable5 Prompt - Princess of Wands (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your
job is not to draw a diagram of the card's symbols but to reproduce the
*composition and energy* of Lady Frieda Harris's painting in text. Fidelity to
Crowley's iconography AND to the feel of the original image both matter. Work
in a fixed-width grid, Courier New assumed.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the leaping
princess is the hero; her VISUAL center (not her left edge) sits on column 23,
the rising Yodh-flame column runs up the axis behind her, and the mass balances
about it. Place asymmetric sprites at `23 - len(s)//2` and verify with `--axis`.
Cells are 1:2 so draw the solar disk, altar curve, and any flame arc ~2:1 wider
than tall. Courier New; extended alphabet `' (backtick) ~ ! ^` plus `´ ‾ ¡ ·`
and line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses (figure, tiger,
altar, solar disk) dithered for volume with a density ramp `. , : ' ° ^`, never
open outlines, lit directionally. Foreground figure drawn ON TOP; break the
flame and altar edges behind her. Full-bleed to the border. Keep the outer
frame + bottom title band. Courts carry NO numeral plaque - use the elemental
title. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans`
(256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis (getting Earth-of-Fire, Hé
final, and the no-decan throne status right) and in clean compositor structure.
It does NOT fix placement drift, an under-scaled flame, or a stiff frontal
figure - for those, use the render & review loop.

## Subject
**Princess of Wands.** Tetragrammaton Hé final; attribution Earth of Fire ("the
earthy part of Fire; the fuel of Fire"). She is a THRONE of Fire, so she has NO
zodiacal decan: she rules a quadrant of the heavens (Cancer/Leo/Virgo) around
the North Pole with the Ace of Wands, not a range of the zodiac. The dance of
the virgin priestess of the Lords of Fire. Do not assign her a sign or degree.

## The composition, in one sentence
A nude priestess leaps, dancing, inside a single surging Yodh-shaped flame,
plumes of fire streaming from her brow, a Sun-tipped wand in hand, the
ram's-headed golden altar and a leaping tiger at her side.

Hold two facts above all else: the whole card is combustion (the figure is
made of the same fire she stands in), and her form reads as a LEAP / dance, not
a standing pose. If you get only two things right, get the Yodh-flame-as-frame
and the leaping motion of the body.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The Yodh-flame is the stage.** She leaps "in a surging flame which
re-calls by its shape the letter Yodh." Draw one dominant rising tongue of fire
up the axis (col 23) that she leaps within, not scattered campfire licks. Give
it volume with a dithering density ramp (`. , : ' ° ^`), tallest and densest on
the axis, thinning outward. This flame is the backdrop the figure sits against.
This is the #1 compositional fix.

**2. She leaps / dances, she does not stand.** "the dance of the virgin
priestess of the Lords of Fire." Rebuild the nude body with flowing diagonal
anti-aliasing strokes so the torso reads as an S-curve mid-leap, one arm arched
overhead with the wand, the other free, legs in a dancer's spring. A stiff
frontal stick figure is the failure mode. She "creates her own beauty by her
essential vigour and energy" - the energy IS the beauty.

**3. She is made of the same fire.** She is unclothed because "chemical action
can only take place when the element is perfectly free to combine." Do not
armor or robe her. Let the flame licks read INTO her contour so figure and fire
share glyphs at the edges - she is "the fuel of Fire," not a person standing
near a fire.

**4. Plumes of justice streaming like flames from her brow.** The headdress is
flame, not a static crown or tiara. Curl the plume tips upward and outward
(`\^^^/`) so they stream like the fire around her. Keep them continuous with
the field flame.

**5. Sun-tipped wand.** "She bears a wand crowned with the disk of the Sun." A
long club/wand (DuQuette: "long club, largest at bottom") topped by a solar
disk `(O)`/`(@)`. Held in the raised, arched arm so it reaches into the top of
the flame. Draw the disk WIDER than tall (cell aspect) so it reads round, not
egg-shaped.

**6. The ram's-headed golden altar.** "she is in attendance upon the golden
altar ornamented with rams' heads) symbolizing the fires of Spring." A gold
slab/pedestal at her side or below, carrying at least one pair of curled ram
horns (Aries = spring fire). Shade the horns and slab (light plane / dark
plane) so gold reads as mass, not outline. This is her station as priestess of
the flaming sacrifice.

**7. The tiger.** DuQuette plate: Crest "Tiger's head," Symbols "Tiger, leaping
flames." Place the tiger at her side or leaping with her, a striped tawny mass
that doubles her ferocity ("she consumes all that comes into her sphere").
Shade the stripes as dark planes on a lit body, not `>xX<` scribble.

**8. Palette (ANSI/256 + 16-color fallback).** NO Harris court scan exists, so
map from Crowley's verbal color words only: "Fiery reds, yellows, and gold
dominate this card." Figure and flame in reds / oranges / yellows / gold; solar
disk and altar bright gold; hair red-gold; a single blue point for her eyes
(the only cool accent); tiger tawny gold with darker stripes. Introduce no
color with no referent in the text (no stray green/violet).

**9. Earth-of-Fire as the meaning.** Tone to honor: brilliant, daring, sudden,
violent, implacable, all-consuming; ambitious and irrationally enthusiastic.
She is the fuel and the fire at once. The card should feel like combustion
about to leap the firebreak, not a decorative pin-up. (Ill-dignified reading -
shallow, theatrical, drama-queen - is the shadow, not the render's target.)

**10. Leaping flames fill the field.** No dead black negative space. Fill the
frame with dithered fire (`. , ' ^` ramp) radiating up and out from behind her,
so the whole card is one combustion. This full-bleed fire is the difference
between Thoth and a diagram.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  solar disk, altar curve, and any flame arc WIDER than tall or they render as
  squashed eggs. Bake the correction in.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push the fire to the card border. Do not float a
  sparse figure in an empty frame.
- **Occlusion.** The figure is drawn ON TOP; break the flame, altar, and tiger
  edges where she overlaps them. Never let a background line slice through her.
- **Card frame (court, NO numeral plaque):** keep the outer double-rule border.
  Courts carry the ELEMENTAL TITLE, not a Roman numeral. Bottom title band:
  line 1 `PRINCESS OF WANDS`, line 2 `~ he final . earth of fire ~`. Romanized
  letter only in the art; the real Hebrew glyph lives in site chrome, never in
  the `.txt`/`.ans`.

## Render & review
Do not judge flame scale, the leaping motion, placement, or palette by reading
the source. Run the chain and LOOK: `compose_princess-wands_lg.py` -> `frame.py`
(court frame, elemental title, no numeral) -> `cardkit.py princess-wands` ->
`render_png.py princess-wands --axis`, then OPEN the PNG and critique it. Note:
**no Harris scan of the court cards exists in this repo**, so judge against
Crowley's verbal description, NOT a scan. Ask: is the Yodh-flame big enough to
be the STAGE she leaps inside (centered on the axis guide)? does the body read
as a leap/dance, not a standing figure? do figure and fire share edge glyphs
(she is the fuel)? are the plumes streaming flame, the wand Sun-tipped, the
altar ram-horned, the tiger present? is the palette reds/yellows/gold with one
blue eye-accent and nothing off-palette? Fix the compositor and repeat. Ship at
~80% once the render holds (2-3 passes max). Note: `princess-wands` must be in
`cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render &
review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three
composer agents in parallel (each running the Render & review loop above to a
finished candidate, judging against Crowley's verbal description since no scan
exists), three judges scoring each candidate on iconographic fidelity,
composition/energy, legibility at 47x32, occlusion, and palette, then
synthesis / polish / integration merging the strongest read. Three strategies
to seed the composers:
- **A. Flame-as-stage dominant** - the surging Yodh-flame is the field; the
  princess leaps small inside it, altar and tiger tucked low.
- **B. Figure-dominant** - the leaping, dancing nude is the hero filling the
  frame, the flame a backdrop mass behind her, wand reaching top.
- **C. Priestess-at-the-altar** - the ram's-headed golden altar and tiger
  share the stage; she dances in attendance, flame binding all three into one
  combustion.
Tier: **full panel** - the leap-vs-stand read and the figure-as-fuel edge
blending are hard and contested, so spend the full cost.

## Output
- One large-format art block (target the standard 47x32 canvas, 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette
  from directive 8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A nude priestess leaps inside a single Yodh-shaped flame she is herself the
fuel of; get the flame-as-frame and the leaping dance and the card stops being
a diagram.
