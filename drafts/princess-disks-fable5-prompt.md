# Fable5 Prompt - Princess of Disks (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your
job is not to draw a diagram of the card's symbols but to reproduce the
*composition and energy* of Lady Frieda Harris's painting in text. Fidelity to
Crowley's iconography AND to the feel of the original image both matter. Work
in a fixed-width grid, Courier New assumed. A Harris scan of THIS court card
exists (`reference/princess-disks-card.jpg`), so judge against the painting.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the standing
pregnant priestess is the hero; her VISUAL center (not her left edge) sits on
column 23, the diamond-tipped sceptre plunges down near the axis, and the mass
balances about it. Place asymmetric sprites at `23 - len(s)//2` and verify with
`--axis`. Cells are 1:2 so draw the seed-disk, the ram horns, and any curve
~2:1 wider than tall or they render as squashed eggs. Courier New; extended
alphabet `` ` ~ ! ^`` plus `´ ‾ ¡ ·` and line-glyphs `o O v V T L 7 U c C x X`
allowed. Solid masses (figure, fur cape, disk, rock, altar) dithered for volume
with a density ramp `. , : ' ° ^`, never open outlines, lit directionally.
Foreground figure drawn ON TOP; break the grove, altar, and disk edges behind
her. Full-bleed to the border. Keep the outer frame + bottom title band. Courts
carry NO numeral plaque - use the elemental title. Sign `aw` or unsigned, never
`jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis (getting Earth-of-Earth, Hé
final, and the no-decan throne status right, and NOT confusing her North-Pole
quadrant with the Wands Princess) and in clean compositor structure. It does
NOT fix placement drift, an under-read pregnancy, or a stiff frontal figure -
for those, use the render & review loop.

## Subject
**Princess of Disks.** Tetragrammaton Hé final; attribution Earth of Earth
("the earthy part of Earth"). She is the last of the sixteen court cards, the
Malkuth of Malkuths. She is a THRONE of Earth, so she has NO zodiacal decan:
with the Ace of Disks she rules the Aries/Taurus/Gemini quadrant of the heavens
around the North Pole (the area of Europe and Africa), NOT a range of the
zodiac. A pregnant priestess of Demeter, on the brink of transfiguration. Do
not assign her a sign or degree. Do not reuse the Wands Princess quadrant.

## The composition, in one sentence
A brooding, pregnant priestess stands wrapped in an enormous fur cape within a
grove of bare trees, a ram's-head crest on her brow, a diamond-tipped sceptre
plunging from her hand down into the rock, and a great seed-disk carrying the
rose of Isis at her side.

Hold two facts above all else: she is the Earth about to give birth (the
pregnancy and the brooding stillness are the card, not decoration), and the
sceptre travels DOWNWARD, the diamond born in the deepest darkness. If you get
only two things right, get the pregnant standing stillness and the
sceptre-descending-into-earth.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The pregnant, brooding priestess is the stage.** Unlike the leaping Wands
Princess, she STANDS, still and monumental, "on the brink of transfiguration,"
with "an expression of intense brooding, as if about to become aware of secret
wonder." "She bears within her body the secret of the future." Build the swell
of the pregnant belly under the cape on the axis (col 23); the figure fills the
frame vertically and hardly moves. Stillness, not dance, is the read. This is
the #1 compositional fix and the opposite failure mode from the Wands card.

**2. The sceptre descends into the earth, diamond-tipped.** "her sceptre
descends into the earth. There its head becomes a diamond, the precious stone
of Kether." Draw one long rod running DOWNWARD from her hand into the rock at
the base, its lower tip a faceted diamond `<>`/`<+>` buried in the ground. This
is the highest light (Kether) born in the deepest, darkest Element. Do NOT
raise it like a wand; its whole meaning is the downward plunge into matter.

**3. The great seed-disk with the twin-spiral rose.** She bears a disk that is
a giant seed "composed of thirty-six sections," a notched/segmented rim; at its
centre the Chinese ideogram of "the twin spiral force of Creation in perfect
equilibrium" (the yin-yang), "from this is born the rose of Isis." In the scan
it reads as a round shield-disk at her side carrying a golden-orange rose
rosette. Draw the disk WIDER than tall (cell aspect), dithered as a mass, with
the spiral/rose germ at center. Do not draw it as a flat open ring.

**4. The ram's-head crest.** "Her crest is the head of the ram" (DuQuette:
WINGED ram's head). The headdress is curling ram horns on her brow, greenish-
gold in the scan, with red-pink streamers falling from it down the figure.
Curl the horns outward `(m) (m)`; hint a wing above the brow. Draw the horns
wider than tall so they read round, not spiky.

**5. She is wrapped in an enormous fur cape.** "wrapped in an enormous cape of
what appears to be animal fur." A heavy cream-white pelt is the dominant lower
silhouette, falling full-width to the ground. Dither it as a soft textured mass
(`. , : '` ramp), not an outline; let it carry most of the figure's bulk and
occlude the altar and rock behind her.

**6. The grove of bare trees.** "She stands within a grove of sacred trees."
DuQuette: barren and DYING trees "that her fertile presence will now restore to
green health." In the scan they are leafless golden-brown trunks flanking both
sides against an ochre sky. Draw them as vertical dithered trunks `,Y,` `.|.`
at the left and right edges, framing her; keep them behind the figure
(occlusion). They are dead now, on the verge of greening.

**7. The wheatsheaf altar of Demeter.** "before an altar suggesting a
wheatsheaf, for she is a priestess of Demeter." A pale sheaf-bundle form at or
below her feet, on a slab. This is her station as a priestess of the grain
mysteries (Eleusis). Shade the sheaf and slab (light plane / dark plane) so
they read as mass, not outline.

**8. Palette (ANSI/256 + 16-color fallback), from the scan.** A Harris scan of
this court card EXISTS, so map from it, not from bare color words: warm ochre /
dark-yellow field and humid golden atmosphere; cape and wheatsheaf cream /
ivory-white; ram horns green-gold with a red-pink streamer accent; seed-disk
rose golden-orange; grove yellow-brown; rock and altar gray-brown; hair rich
brown, eyes dark. The card is dominated by earth warmth. Introduce no color
with no referent in the scan or text (no stray blue/violet).

**9. Earth-of-Earth as the meaning.** Tone to honor: monumental stillness on
the brink of transfiguration; the Earth pregnant and about to give birth; the
Malkuth of Malkuths carrying "the potential of all possible possibilities." She
is "Womanhood in its ultimate projection," of "bewildering inconsistency." The
Yi King reading is Kan, the MOUNTAIN, whose characteristic is rest. The card
should feel grave, fertile, and still, a seed about to split, not busy.

**10. Full-bleed earth atmosphere.** No dead black negative space. Fill the
frame with the humid ochre light and the flanking grove so the whole card is
one warm, tactile, textured earth-mass (DuQuette: "Textured grays combine to
make this card almost tactile"). This full-bleed warmth is the difference
between Thoth and a diagram.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  seed-disk, ram horns, and any curve WIDER than tall or they render as
  squashed eggs. Bake the correction in.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push the grove and ochre earth to the card border. Do
  not float a sparse figure in an empty frame.
- **Occlusion.** The figure is drawn ON TOP; break the grove, disk, altar, and
  rock edges where she overlaps them. Never let a background line slice through
  her or through the fur cape.
- **Card frame (court, NO numeral plaque):** keep the outer double-rule border.
  Courts carry the ELEMENTAL TITLE, not a Roman numeral. Bottom title band:
  line 1 `PRINCESS OF DISKS`, line 2 `~ he-final . earth of earth ~`. Romanized
  letter only in the art; the real Hebrew glyph lives in site chrome, never in
  the `.txt`/`.ans`.

## Render & review
Do not judge the pregnancy read, the downward sceptre, placement, or palette by
reading the source. Run the chain and LOOK: `compose_princess-disks_lg.py` ->
`frame.py` (court frame, elemental title, no numeral) -> `cardkit.py
princess-disks` -> `render_png.py princess-disks --axis`, then OPEN the PNG and
critique it against `reference/princess-disks-card.jpg`. A Harris scan of this
court card EXISTS in the repo, so judge against the painting. Ask: does the
figure read as pregnant and STILL (monumental, not leaping)? does the sceptre
plunge DOWNWARD into the rock with a diamond tip, not raised like a wand? is the
seed-disk a dithered mass with the rose/spiral germ, not an open ring? are the
ram horns, fur cape, grove of bare trees, and wheatsheaf altar all present and
occluded correctly? is the palette warm ochre / cream / green-gold / brown from
the scan with no off-palette color? Fix the compositor and repeat. Ship at ~80%
once the render holds (2-3 passes max). Note: `princess-disks` must be in
`cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render &
review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three
composer agents in parallel (each running the Render & review loop above to a
finished candidate, judging against the Harris scan since one exists for this
card), three judges scoring each candidate on iconographic fidelity,
composition/energy, legibility at 47x32, occlusion, and palette, then
synthesis / polish / integration merging the strongest read. Three strategies
to seed the composers:
- **A. Figure-dominant (pregnant priestess)** - the still, brooding, pregnant
  priestess fills the frame, cape falling to the base, sceptre plunging from
  her hand, grove and disk tucked to the sides.
- **B. Sceptre-and-disk axis** - the vertical descent of the diamond sceptre
  into the rock and the great seed-disk carry the composition, the figure read
  through her attributes as much as her body.
- **C. Grove-and-altar frame** - the grove of bare trees and the wheatsheaf
  altar of Demeter build the stage, the priestess arising from the Earth in
  their midst, fertility about to green the dead grove.
Tier: **full panel** - the still-vs-leaping read (opposite of the Wands
Princess), the downward sceptre, and the fur-cape mass are contested enough to
spend the full cost. A scan exists, so judges have ground truth.

## Output
- One large-format art block (target the standard 47x32 canvas, 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette
  from directive 8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A pregnant priestess stands still and monumental in a grove of bare trees, her
diamond sceptre plunging down into the rock and her great seed-disk bearing the
rose of Isis; get the pregnant stillness and the downward-into-earth sceptre and
the card stops being a diagram.
