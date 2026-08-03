# Fable5 Prompt - Princess of Swords (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your
job is not to draw a diagram of the card's symbols but to reproduce the
*composition and energy* of Lady Frieda Harris's painting in text. Fidelity to
Crowley's iconography AND to the feel of the original image both matter. Work
in a fixed-width grid, Courier New assumed.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the helmed
warrior-princess is the hero; her VISUAL center (not her left edge) sits on
column 23, the boiling column of smoke she rises out of runs up the axis
beneath her, and the mass balances about it. Place asymmetric sprites at
`23 - len(s)//2` and verify with `--axis`. Cells are 1:2 so draw the helm
curve, altar top, and any wing arc ~2:1 wider than tall. Courier New; extended
alphabet `' (backtick) ~ ! ^` plus `´ ‾ ¡ ·` and line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses (figure, smoke, altar, helm)
dithered for volume with a density ramp `. , : % & @`, never open outlines,
lit directionally. Foreground figure drawn ON TOP; break the smoke, wings, and
altar edges behind her. Full-bleed to the border. Keep the outer frame +
bottom title band. Courts carry NO numeral plaque - use the elemental title.
Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans`
(256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis (getting Earth-of-Air, Hé
final, the fixation-of-the-volatile, and the no-decan throne status right) and
in clean compositor structure. It does NOT fix placement drift, an
under-scaled smoke base, a raised-instead-of-plunging sword, or a stiff
frontal figure - for those, use the render & review loop.

## Subject
**Princess of Swords.** Tetragrammaton Hé final; attribution Earth of Air
("the earthy part of Air; the fixation of the volatile"). She is a THRONE of
Air, so she has NO zodiacal decan: she rules a quadrant of the heavens
(Capricorn/Aquarius/Pisces) around the North Pole with the Ace of Swords, not
a range of the zodiac. A helmed avenging warrior-maiden, Medusa-crested,
Minerva / Artemis / Valkyrie, who brings about the materialization of Idea and
the fixation of the volatile. Do not assign her a sign or degree.

## The composition, in one sentence
A green-robed, Medusa-helmed warrior rises out of a churning gray-black cloud
of dust and stabs her sword downward at a barren stone altar, angular geometric
wing-panes fanning behind her against an angry, acid-yellow-green heaven.

Hold two facts above all else: the sword drives DOWNWARD (the destruction of
the fixed idea, avenging the profaned altar), and she is the earthy settling of
a storm (she rises out of / stands on boiling smoke, air made heavy). If you
get only two things right, get the downward stab and the smoke-mass she rises
from.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The sword stabs DOWNWARD.** "she stabs downward with her sword." This is
the card's kinetic signature and the usual failure mode is a sword raised in
salute. Bend the whole figure into the descending blow: on the scan the blade
is gripped in both hands over the head at the top of the stroke, about to fall
on the altar below. Draw the plunge, the blade angled down toward the altar,
never a static vertical hold. This is the #1 read.

**2. She rises out of a churning smoke / dust base.** "Rising out of a cloud of
dust... swirling clouds of gray-black dust and violent windbursts." The bottom
third of the card is a boiling dithered mass she stands on and emerges from,
tallest and densest up the axis (col 23), thinning outward. Ramp
`. , : % & @`. She is the EARTHY part of Air: the dust is her ground. This
smoke is the stage. This is the #1 compositional fix.

**3. The Medusa-helmed head, face turned away.** "she appears helmed, with
serpent-haired Medusa for her crest," and DuQuette notes the face is
"mercifully turned away from our view" so it cannot petrify us. Draw the helm
as a writhing mass of serpents (`{sSsSs}` / curled tips), the head in
three-quarter or profile turned aside. Not a smooth tiara, not a forward-facing
gorgon mask.

**4. She avenges the barren altar.** "She stands in front of a barren altar as
if to avenge its profanation." A gray stone / silver altar (DuQuette plate:
"Silver altar, smoke") set low and offset, the target of the descending sword.
Shade the slab (light plane / dark plane) so stone reads as mass, not outline.
Her violence points AT it; the geometry of the composition should aim the blade
at the altar.

**5. The geometric wing-panes.** Harris gives her stylized angular wing-panels,
not feathered wings: "the geometrical wings we first encountered on the
Princess of Swords" that festoon the whole suit. Faceted translucent ray-panes
fanning from the shoulders (`<//|\\>`), pale gray-white, hard-edged. They ARE
the fixation of the volatile - Air crystallizing into rigid geometry. Keep them
angular and shard-like, never soft plumage.

**6. Fixation of the volatile / materialization of Idea.** The doctrine made
visible: Air (thought) hardening into stone. The Medusa gaze that turns things
to stone and the crystalline geometric wings are the same freezing. Let the
figure's edges toward the wings read hard and faceted while the smoke below
reads soft and boiling: the card is the moment volatile Air fixes into earth.

**7. The angry heaven.** "The heaven and the clouds, which are her home, seem
angry." Behind and above her, radiating windbursts and shattered acid light
(`\´\ | /´/`), not a calm ground. The sky is in revolt; fill the upper field
with directional light-bursts and torn cloud so nothing sits still.

**8. Palette (ANSI/256 + 16-color fallback), from the SCAN.** A Harris scan
DOES exist for this card (`reference/princess-swords-card.jpg`,
esotericmeanings.com court-cards page). Map it: figure robed in strong olive /
emerald GREEN; smoke base gray-brown to near-black; radiating light
yellow-green / acid yellow (DuQuette "metallic greens" and residual yellows);
wing-panes pale gray-white geometric facets; sword brown / dull steel (plate
"Drawn brown sword"); altar gray stone / silver; hair light brown; a single
blue eye-point (the only clear cool accent, mostly hidden under the helm).
Introduce no color with no referent in the scan or text.

**9. Earth-of-Air as the meaning.** Tone to honor: stern, revengeful,
destructive in logic, firm, aggressive, adroit in controversy; the anger of
the Gods; a Minerva / Artemis / Valkyrie. She is "the throne of Spirit," free
to blow everything sky high. The card should feel like an avenging blow
falling out of a storm, not a decorative angel. (Ill-dignified reading -
incoherent, low cunning - is the shadow, not the render's target.)

**10. Full-field turbulence.** No dead black negative space. Fill the frame
with agitated air: boiling smoke below, torn windbursts and shattered light
above, geometric shards mid-field. The whole card is one storm settling into
earth. This full-bleed turbulence is the difference between Thoth and a
diagram.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  helm curve, altar top, and any wing arc WIDER than tall or they render as
  squashed eggs. Bake the correction in.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push the smoke and windbursts to the card border. Do
  not float a sparse figure in an empty frame.
- **Occlusion.** The figure is drawn ON TOP; break the smoke, wing-panes, and
  altar edges where she overlaps them. Never let a background line slice
  through her.
- **Card frame (court, NO numeral plaque):** keep the outer double-rule border.
  Courts carry the ELEMENTAL TITLE, not a Roman numeral. Bottom title band:
  line 1 `PRINCESS OF SWORDS`, line 2 `~ he-final . earth of air ~`. Romanized
  letter only in the art; the real Hebrew glyph lives in site chrome, never in
  the `.txt`/`.ans`.

## Render & review
Do not judge smoke scale, the downward stab, placement, or palette by reading
the source. Run the chain and LOOK: `compose_princess-swords_lg.py` ->
`frame.py` (court frame, elemental title, no numeral) ->
`cardkit.py princess-swords` -> `render_png.py princess-swords --axis`, then
OPEN the PNG and critique it AGAINST `reference/princess-swords-card.jpg` (a
scan DOES exist for this card; judge against it, not just the verbal text).
Ask: is the smoke base big enough to be the stage she rises out of (centered on
the axis guide)? does the sword clearly PLUNGE DOWNWARD at the altar, not stand
in salute? is the helm a serpent-Medusa mass with the face turned away? are the
wing-panes hard geometric shards, not feathers? is the altar present, shaded,
low and offset as the target? is the palette green figure + gray-brown smoke +
acid yellow-green light + pale wing-panes + brown sword, with one blue
eye-point and nothing off-palette? Fix the compositor and repeat. Ship at ~80%
once the render holds (2-3 passes max). Note: `princess-swords` must be in
`cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render &
review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three
composer agents in parallel (each running the Render & review loop above to a
finished candidate, judging against `reference/princess-swords-card.jpg`),
three judges scoring each candidate on iconographic fidelity,
composition/energy, legibility at 47x32, occlusion, and palette, then
synthesis / polish / integration merging the strongest read. Three strategies
to seed the composers:
- **A. Smoke-as-stage dominant** - the churning gray-black dust cloud fills the
  lower two-thirds; the princess rises small out of it, sword plunging, altar
  tucked to one side.
- **B. Figure-dominant** - the helmed, green-robed warrior is the hero filling
  the frame mid-stab, geometric wing-panes fanning wide behind her, smoke a
  backdrop mass at her feet.
- **C. Avenging-blow dominant** - the downward line of the sword driving at the
  barren altar is the spine of the composition; figure, wings, and smoke all
  angle to aim the blade, the whole card leaning into the strike.
Tier: **full panel** - the downward-stab-vs-salute read and the
figure-rising-from-smoke edge are hard and contested, so spend the full cost.

## Output
- One large-format art block (target the standard 47x32 canvas, 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette
  from directive 8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A green-robed, Medusa-helmed warrior rises out of a boiling dust-cloud and
stabs her sword downward at a barren altar; get the downward blow and the
smoke-mass she rises from and the card stops being a diagram.
