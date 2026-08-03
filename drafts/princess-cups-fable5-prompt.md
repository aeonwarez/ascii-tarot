# Fable5 Prompt - Princess of Cups (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your
job is not to draw a diagram of the card's symbols but to reproduce the
*composition and energy* of Lady Frieda Harris's painting in text. Fidelity to
Crowley's iconography AND to the feel of the original image both matter. Work
in a fixed-width grid, Courier New assumed.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the dancing
princess is the hero; her VISUAL center (not her left edge) sits on column 23,
the covered cup she tends and the swan crest above her ride the axis, and the
great fanning robe balances its mass about it. Place asymmetric sprites at
`23 - len(s)//2` and verify with `--axis`. Cells are 1:2 so draw the cup bowl,
swan wings, lotus, and any wave arc ~2:1 wider than tall. Courier New; extended
alphabet `` ` ~ ! ^ `` plus `´ ‾ ¡ ·` and line-glyphs `o O v V T L 7 U c C x X`
allowed. Solid masses (figure, robe, cup, tortoise, swan, dolphin) dithered for
volume with a density ramp `. , : ' ° ^`, never open outlines, lit
directionally. Foreground figure drawn ON TOP; break the robe, sea, and cup
edges behind her. Full-bleed to the border. Keep the outer frame + bottom title
band. Courts carry NO numeral plaque - use the elemental title. Sign `aw` or
unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis (getting Earth-of-Water, He
final, the crystallization faculty, and the no-decan throne status right) and in
clean compositor structure. It does NOT fix placement drift, an under-scaled
robe, or a stiff frontal figure - for those, use the render & review loop.

## Subject
**Princess of Cups.** Tetragrammaton He final; attribution Earth of Water ("the
earthy part of Water; in particular, the faculty of crystallization"). She is a
THRONE of Water, so she has NO zodiacal decan: she rules a quadrant of the
heavens (Libra/Scorpio/Sagittarius) around the North Pole with the Ace of Cups,
not a range of the zodiac. A dancing figure in a flowing scalloped robe on
whose edges crystals form, eyes closed, head thrown back in rapture. Do not
assign her a sign or degree.

## The composition, in one sentence
A dancing princess in a great fanning scalloped robe (crystals forming along
its edges) tends a covered cup from which a tortoise issues, a swan with open
wings for her crest, dancing on a foaming sea where a dolphin sports.

Hold two facts above all else: everything is fluid, undulating movement (robe
and sea are one continuous flow), and the doctrinal core is CRYSTALLIZATION -
vaporous Water grounding into faceted solids at the hem. If you get only two
things right, get the fanning dance-robe and the crystals forming at its edge.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The fanning scalloped robe is the stage.** She is "a dancing figure, robed
in a flowing garment on whose edges crystals are seen to form." The pale silk
robe fans across nearly the whole frame in scalloped folds (the same scallop
motif as the Ace of Cups). Draw it as the dominant dithered mass, sweeping
diagonally out from the figure on the axis, thinning at the border. This robe,
not a background, is what the composition sits against. This is the #1
compositional fix.

**2. Crystallization at the hem.** Earth of Water = "the faculty of
crystallization." Clear water-crystals form along the flowing edges of the
garment. Draw faceted solids (`<>_/\_<>`, shaded light-plane / dark-plane, not
open outlines) scattered down the robe and densest at the hem. This is the
visible doctrine: formless Water becoming substance. Do not omit it.

**3. She dances, she does not stand.** "Harris's image is one of graceful fluid
movement": eyes closed, head thrown back, an expression of pure rapture
(DuQuette compares Bernini's Ecstasy of Saint Theresa). Rebuild the body with
flowing diagonal anti-aliasing strokes so it reads as dance mid-turn, head
tilted back, arms tending the cup, robe trailing the motion. A stiff frontal
figure is the failure mode.

**4. The swan crest, open wings.** "For her crest she wears a swan with open
wings," the swan that is the word AUM / AUMGN, "the symbol of the entire
process of creation." Draw an open-winged swan rising above her brow on the
axis (`.-<((v)(A)(v))>-.`), wings spread wide (2:1). It is her crest, drawn ON
TOP of the field, not a bird lost in the background.

**5. The covered cup with the tortoise issuing.** "She bears a covered cup from
which issues a tortoise" (the Hindu world-tortoise). Draw a lidded cup she
tends near the axis, a shaded jade-and-gold mass, with a small tortoise
(`<oQo>`) emerging from under the lid. Draw the cup bowl WIDER than tall (cell
aspect) so it reads round, not egg-shaped. Crown it with the lotus / rose seen
in the scan.

**6. The dolphin in the foaming sea.** "She is dancing upon a foaming sea in
which disports himself a dolphin, the royal fish, which symbolizes the power of
Creation." In the scan it reads as a coiling green sea-serpent / dolphin low
left. Draw it arcing through the foam beneath her (`,~=c<===<~,`), a shaded
jade mass, sporting in the wave.

**7. The lotus and the heavy sea.** The lotus (also in her title, "Lotus of the
Palace of the Floods") sits high in the field (upper right) and crowns the cup.
Beneath her, the base of the card is a foaming sea of "large smooth waves that
suggest the heavy environment of ocean's depth" (DuQuette). Undulating
wave-runs with foam flecks, not flat ground.

**8. Palette (ANSI/256 + 16-color fallback).** A Harris scan of this court card
EXISTS (`reference/princess-cups-card.jpg`, esotericmeanings.com court-cards
page), so map from the painting: "Cool blues and blue-greens dominate this
card." Robe pale silver-lilac / white; swan, cup, tortoise, and dolphin in
jade / sea-green with brass-gold accents; lotus and water-crystals in soft rose
/ pink; sea in teal and blue-green; hair brown. Introduce no color with no
referent in the scan or text (no stray red/orange).

**9. Earth-of-Water as the meaning.** Tone to honor: infinitely gracious, all
sweetness, voluptuousness, gentleness, tenderness; she lives in the world of
Romance, in the perpetual dream of rapture. Not selfish or indolent despite a
superficial look, but silently and effortlessly at her work. She grounds
vaporous, romantic ideas into manifestation. The card should feel like water
settling into crystal, dreamy but quietly doing its work, not a static portrait.

**10. The whole field undulates.** No dead flat negative space. Fill the frame
with the continuous flow of robe and sea, curved sweep strokes so the whole
card is one moving body of water. This full-bleed fluidity is the difference
between Thoth and a diagram.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  cup bowl, swan wings, lotus, and any wave arc WIDER than tall or they render
  as squashed eggs. Bake the correction in.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push the robe and sea to the card border. Do not float
  a sparse figure in an empty frame.
- **Occlusion.** The figure is drawn ON TOP; break the robe, sea, cup, and swan
  edges where she overlaps them. Never let a background line slice through her.
- **Card frame (court, NO numeral plaque):** keep the outer double-rule border.
  Courts carry the ELEMENTAL TITLE, not a Roman numeral. Bottom title band:
  line 1 `PRINCESS OF CUPS`, line 2 `~ he-final . earth of water ~`. Romanized
  letter only in the art; the real Hebrew glyph lives in site chrome, never in
  the `.txt`/`.ans`.

## Render & review
Do not judge robe scale, the dance motion, placement, or palette by reading the
source. Run the chain and LOOK: `compose_princess-cups_lg.py` -> `frame.py`
(court frame, elemental title, no numeral) -> `cardkit.py princess-cups` ->
`render_png.py princess-cups --axis`, then OPEN the PNG and critique it against
`reference/princess-cups-card.jpg`. A Harris scan of THIS court card exists, so
judge against the scan. Ask: is the fanning scalloped robe big enough to be the
STAGE (centered on the axis guide)? do water-crystals form at the hem? does the
body read as a head-thrown-back dance, not a standing figure? is the swan crest
open-winged above the brow, the cup covered with a tortoise issuing, the dolphin
sporting in the sea, the lotus present? is the palette blues / blue-greens /
jade with pale silver-lilac robe, rose crystals, brass-gold cup, and nothing
off-palette? Fix the compositor and repeat. Ship at ~80% once the render holds
(2-3 passes max). Note: `princess-cups` must be in `cardkit.CONFIGS` before
render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer
agents in parallel (each running the Render & review loop above to a finished
candidate, judging against the Harris scan since one exists), three judges
scoring each candidate on iconographic fidelity, composition/energy, legibility
at 47x32, occlusion, and palette, then synthesis / polish / integration merging
the strongest read. Three strategies to seed the composers:
- **A. Robe-as-stage dominant** - the great fanning scalloped robe fills the
  field, crystals forming along its edges; the dancing figure, swan, and cup
  ride small on the axis inside it.
- **B. Figure-dominant** - the dancing nude-formed priestess, head thrown back
  in rapture, is the hero filling the frame; robe and sea are the backdrop
  flow, cup and swan tucked to the axis.
- **C. Cup-and-creatures dominant** - the covered cup with issuing tortoise,
  the swan crest, and the sporting dolphin share the stage as the three sacred
  animals; she dances among them, robe and sea binding all into one water-body.
Tier: **full panel** - the fanning-robe scale, the crystallization read at the
hem, and the fluid dance-vs-stand motion are hard and contested, so spend the
full cost.

## Output
- One large-format art block (target the standard 47x32 canvas, 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette
  from directive 8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A dancing princess in a great fanning scalloped robe, crystals forming at its
edges, tends a covered cup with a tortoise issuing while a swan crests her and a
dolphin sports in the foam; get the robe-as-stage and the crystallization at the
hem and the card stops being a diagram.
