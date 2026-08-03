# Fable5 Prompt - Queen of Disks (Thoth court card)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is
not to draw a diagram of the card's symbols but to reproduce the *composition
and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's
iconography AND to the feel of the original image both matter. Work in a
fixed-width grid, Courier New assumed. Note: a Harris scan of THIS court card
DOES exist in the repo (`reference/queen-disks-card.jpg`, scan source
esotericmeanings.com court-cards page), so judge against the pixel reference,
not against the text alone.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved on every line. **Center on the axis (col 23):**
the enthroned Queen, helmed with the great markhor horns, is the stage,
centered on column 23; her seated mass is balanced about the axis, the goat on
its sphere set low and forward to one side, the sceptre in her right hand and
her proper disk cradled in her left arm counter-weighting each other. Place
asymmetric sprites at `23 - len(s)//2` and verify with `--axis`. Cells are 1:2
so draw circles and curves (the horn spirals, the proper disk, the goat's
sphere) about 2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` +
line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for
volume, never open outlines, lit directionally. Foreground figure drawn ON TOP;
break background edges (vegetation, river, desert) behind her. Full-bleed to
the border. Keep outer frame + bottom title band. Courts have NO numeral
plaque; use the elemental title band. Sign `aw` or unsigned, never `jgs`.
Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis and clean compositor
structure. It does NOT fix placement drift, under-scaled horns, or the
barren-to-fertile gradient read - for those, use the render & review loop.

## Subject
**Queen of Disks.** Water of Earth (the watery part of Earth, its function as
Mother). Tetragrammaton: He primal (first He) of the earth-suit; she receives,
ferments, and transmits the Knight's energy, seated upon her throne. Rules 21
degrees Sagittarius to 20 degrees Capricorn; dominates cardinal Capricorn. GD
title: Queen of the Thrones of Earth, Queen of the Gnomes. Her Water is the
fertilizing, mothering influence that brings a calm river through the desert
and coaxes oases from the waste. "She thus represents the ambition of matter
to take part in the great work of Creation."

## The composition, in one sentence
A dark-haired queen sits enthroned upon the life of vegetation, helmed with the
enormous spiral horns of the markhor, armoured in coin-scales, a sceptre topped
by a cubed hexagram in her right hand and her interlaced proper disk in her left
arm, while a goat stands on a sphere before her and a calm river winds through a
sandy desert behind, oases just beginning to green.

Hold two facts above all else: the great markhor horns dominate the top of the
card, and the background is Earth turning fertile (barren desert with a winding
river and beginning oases). If you get only two things right, get the sweeping
spiral horns and the barren-to-fertile gradient.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The great markhor horns are the crown of the composition.** "Her helmet is
adorned with the great spiral horns of the markhor." In the painting these
enormous ram-like spiral horns sweep up and out over her head and own the top
third of the frame. Draw them large, curling outward from the axis (`,~-.(( ))`
mirrored), banded like real horn with a dither ramp for volume. This is the
single most distinctive read; the card is instantly recognizable by the horns.
Do not shrink them to a tidy crown.

**2. The Queen enthroned, throned upon the life of vegetation, in-drawn.** "The
Queen of Disks is throned upon the life of vegetation. She contemplates the
background." She sits (Queens are always throned - they exercise a definite
function), still and passive "in its highest aspect," balanced about the axis.
Her face is lit on one side only (DuQuette: "Light falls on only one side of her
face"), dark hair and dark eyes, half in green-brown shadow, turned inward. Not
frontal-staring. Rebuild the body as a calm seated form, not a stiff stick
figure. She is Water: fluid line inside the earth-mass.

**3. The barren land turning fertile: winding river, desert, beginning oases.**
"She contemplates the background, where a calm river winds through a sandy
desert to bring to it fertility. Oases are beginning to shew themselves amid
the wastes." This IS the meaning of Water of Earth: dead matter receiving life.
Draw the background field as a barren-to-fertile gradient: dry `:::` sand and a
snaking calm river (`~.__~._.~`), greening into small oases (`wYw`) where the
water touches. Read the gradient across the whole back plane behind her.

**4. The goat upon a sphere, before her.** "Before her stands a goat upon a
sphere. There is here a reference to the dogma that the Great Work is
fertility." A live goat balanced on an orb, set low and forward of the throne,
pale cream against the dark ground. The Capricorn beast, the generative sign
made animal. Draw it standing on a dithered sphere (`(:o:)`), offset to one
side of the axis to balance the sceptre. Occlude cleanly where it crosses the
foreground.

**5. The two hand tokens: cubed-hexagram sceptre (right) and interlaced proper
disk (left arm).** "In her right hand she bears a sceptre surmounted by a cube,
within which is a three-dimensional Hexagram, and in her left arm is curved her
proper disk, a sphere of loops and circles interlaced." Sceptre in the RIGHT
hand, topped by a cube holding a 3D hexagram (`[<#>]`, dithered inside). Her
proper disk cradled in the LEFT arm, a woven tangle of loops and circles
(`(@%@)`), not a plain coin. Keep them on the correct sides; they counter-weight
across the axis.

**6. Water of Earth - the mothering, fertilizing quality.** Unlike the Knight
of Disks' laboring, mountainous Earth, her Earth is receptive and life-giving:
water brought to the waste, matter made willing. The whole card is barren
ground about to conceive. Let the composition read as stillness pregnant with
coming growth, not dead rock and not a lush garden yet.

**7. Palette (ANSI/256 + 16-color fallback), from the scan.** Map from the
observed Harris painting (`reference/queen-disks-card.jpg`), confirmed by
DuQuette "Dark greens and rich browns dominate the foreground":
   - Foreground vegetation / frame blades: dark green, near black-green.
   - Markhor horns: warm tan / ochre, banded.
   - Coin-scale armour: golden-yellow, tessellated (the magnifying-glass
     detail).
   - Skin / face: warm ochre, lit one side only, hard chiaroscuro; dark hair,
     dark eyes.
   - Goat: pale cream / bone white; its sphere muted.
   - Background desert / river: paler, cooler grey-tan, greening at the oases.
   Introduce no color with no referent in the painting.

**8. Barren-to-fertile as the visual thesis.** The card is Earth receiving
Water and beginning to live. Everywhere the untempered suit would sit as inert
rock, here it is a river winding, a first oasis greening, matter roused to take
part in Creation. Let the negative space read as sandy waste warming toward
growth, not dead black and not a full garden.

**9. Meaning as tone: quiet strength, the ambition of matter.** Divinatory
sense to honor: the finest of the quieter qualities; ambitious only in useful
directions; immense affection, kindness, greatness of heart; instinct and
intuition over intellect; quiet, hard-working, practical, domesticated. But
underneath, "the ambition of matter to take part in the great work of
Creation," which DuQuette calls "a force to be reckoned with." Render her
still and self-contained, a mother-force at rest, not a display of power. The
shadow (ill-dignified) is the dull servile drudge who cannot rise above her lot.

**10. Witnesses / garnish.** The coin-scale dress worth a magnifying glass; the
3D hexagram legible inside its cube; the calm-river-through-desert dogma that
the Great Work is fertility; the Yi King hexagram Hsien (Influence), advising
one to go forward quietly. Small, supporting. Garnish, but it is the difference
between Thoth and a generic queen on a chair.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  markhor horn spirals, the proper disk, and the goat's sphere WIDER than tall
  or they render as squashed eggs. Bake the correction into every circle and
  curve.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs
  `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border. The
  painting is edge-to-edge; do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer border box. Courts carry
  NO numeral plaque up top. Bottom band line 1: `QUEEN OF DISKS`; line 2:
  `~ he . water of earth ~`. Romanized letter only in the art; the real Hebrew
  glyph lives in site chrome (HTML), never in the `.txt` / `.ans`.

## Render & review
Do not judge horn scale, the barren-to-fertile gradient, placement, or palette
by reading the source. Run the chain and LOOK:
`compose_queen-disks_lg.py` -> `frame.py` -> `cardkit.py queen-disks` ->
`render_png.py queen-disks --axis`, then OPEN the PNG and critique it against
`reference/queen-disks-card.jpg`. Do the great markhor horns dominate the top
and read as banded spirals, not a small crown? Is the Queen enthroned and
centered on the axis, face lit one side only, in-drawn? Does the background read
barren-to-fertile (winding river, sandy desert, beginning oases), not a flat
field? Is the goat standing on its sphere before her, pale against dark ground?
Is the sceptre with cubed hexagram in her RIGHT hand and the interlaced proper
disk in her LEFT arm? Is the palette dark green / rich brown foreground with
tan horns, gold coin-scale armour, cream goat, cooler grey-tan desert, and no
stray colors? Fix the compositor and repeat. Ship at ~80% once the render holds
(2-3 passes max). Note: `queen-disks` must be in `cardkit.CONFIGS` before
render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer
agents in parallel (each running the Render & review loop above to a finished
candidate, viewing its own PNG each pass and judging against the Harris scan),
three judges scoring each candidate on iconographic fidelity to the scan and
text, composition/energy, legibility at 47x32, occlusion, and palette, then
synthesis / polish / integration merging the strongest read. Three strategies
to seed the composers:
- **A. Figure-and-horns dominant** - the enthroned Queen crowned with the great
  markhor spiral horns is the hero, filling the frame top to bottom, the
  background a thin barren-to-fertile band behind her.
- **B. Landscape-gradient dominant** - the barren-to-fertile background (winding
  river, sandy desert, beginning oases) is the field and the thesis, the Queen
  seated within it contemplating the greening waste, horns and goat reading as
  strong local masses.
- **C. Token-and-goat balanced** - the axis is held by the counter-weight of
  the cubed-hexagram sceptre (right) and the interlaced proper disk (left arm),
  with the goat on its sphere forward and low, the coin-scale armour carrying
  texture across the whole torso.
Tier: **full panel** - contested read (horn scale vs. figure, and the
barren-to-fertile gradient vs. a flat ground) justifies the full cost.

## Output
- One large-format art block (target the existing large-format card dimensions,
  47x32 art / 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette
  from directive 7 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A dark-haired queen sits enthroned under the great spiral horns of the markhor,
armoured in coins, a goat on its sphere before her and a river greening the
desert behind: get the sweeping horns and the barren-to-fertile ground and the
card stops being a queen on a chair.
