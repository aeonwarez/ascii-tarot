# Fable5 Prompt - Knight of Disks (Thoth)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed. NOTE: this is a court card, but unlike his three brother Knights a Harris scan of it IS available in the repo (`reference/knight-disks-card.jpg`, from the esotericmeanings.com court-cards page), so judge fidelity against the scan the same way you would a trump.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact leading
whitespace preserved. **Center on the axis (col 23):** the standing horse-and-rider mass is
centered on column 23; unlike the other Knights there is no leap or diagonal thrust, so the
mass sits square and rooted on the axis, weight low. Place asymmetric sprites at
`23 - len(s)//2` and verify with `--axis`. Cells are 1:2 so draw the horse's barrel, the
disk-shield, and any curves ~2:1 WIDER than tall or they squash. Courier New; extended
alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered
for volume (`. : · ' ° :`), never open outlines, lit directionally. Foreground figure (the
armoured Knight) drawn ON TOP; break the field and background edges behind him. Full-bleed
to the border. Keep outer frame + bottom title band. Court cards have NO numeral plaque up
top; use the elemental title in the band. Romanized Hebrew letter only in the art, never a
Hebrew glyph. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16
fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift, an under-scaled horse, or a field that reads as flat backdrop instead of
as the fertile ground he works - for those, use the render & review loop.

## Subject
**Knight of Disks.** Tetragrammaton letter Yod (Yod of the Earth suit, Fire of Earth).
Attribution Fire of Earth; rules 21 degrees Leo to 20 degrees Virgo. Original title: The
Lord of the Wide and Fertile Land, King of the Gnomes. A short, sturdy warrior in heavy
dark plate on a solidly planted shire horse, helmet thrown back, riding through ripe
cornland, a flail in hand and a heavy disk-shield at his shoulder. In natural force he is
Mountains: solid, rooted, gravity itself; his fire is the smouldering fire of growth, NOT
flame.

## The composition, in one sentence
A short heavy knight in dark plate sits a four-square standing shire horse in a field of
ripe corn, helmet thrown back, gazing over cultivated hills at the harvest, not battle.

Hold those two facts above all else. If you get only two things right, get the STANDING
(not leaping) heavy horse as a rooted dark mass and the ripe fertile field as the ground he
works, with the fire carried as warm sunlight and gold grain rather than any flame.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The horse STANDS, four-square and rooted.** "A shire horse, solidly planted on all
four feet, as was not the case with the other Knights." This is the #1 read and the whole
point of the card: where his brother Knights leap, rear, and explode, this horse stands
still. Draw a broad, heavy draught animal, barrel wider than tall (cells are 1:2), all four
legs planted straight down, centered on the axis (col 23). A chestnut/reddish-brown dithered
mass with a pale flaxen mane and tail. No diagonal thrust, no rake. Weight, not motion.

**2. He rides through the fertile land, and the land is the subject.** "He rides through
the fertile land; even the distant hills are cultivated fields." The field is not a
backdrop wash; it is the ground he works and the reason he exists. Fill the foreground and
lower sides with ripe golden corn and green blades, wheat-heads catching light, and stripe
the distant hills as ploughed cultivated rows on the horizon. Fire of Earth made literal as
agriculture. This is the equivalent of the Knight of Wands' flame-ground, but here it is
grain, not fire.

**3. Short, sturdy warrior in heavy dark plate, drawn ON TOP.** "This warrior is short and
sturdy in type. He is clothed in great solidity of plate armour." Not the tall violent
figure of the Wand court; a stocky farmer-king. Draw him squat and grounded, heavy dark
burnished plate (NOT gold, per the scan), dithered so it reads solid metal weight, occluded
cleanly over the horse and field behind him. He reads as a dark mass from behind against the
warm sky.

**4. The helmet is thrown back: harvest, not battle.** "his helmet, which is crested with
the head of a stag, is thrown back, for at the moment his function is entirely confined to
the production of food." The raised / open visor is the psychology of the whole card. He
gazes at the fields "as if in contemplation of harvest, not battle" (DuQuette). Draw the
helm tilted back off the face, the head gazing out over the land, not forward into combat.

**5. The flail and the disk-shield.**
   - **Flail, hanging low toward the grain:** "For this reason he is armed with a flail."
     A two-part hinged threshing tool, "dangling near the grasses, suggesting the thrashing
     of wheat rather than the thrashing of heads" (DuQuette). Draw the hinged shaft-and-swing
     hanging DOWN toward the corn, not raised to strike. Harris painted from a real flail.
   - **The solid disk / shield:** "The disk which he bears, moreover, is very solid; it
     represents nutrition." A heavy round disk at his back shoulder "that could double as a
     dish that could hold enough food to feed a village" (DuQuette). Draw it as a thick
     round coin-dish, dithered face, WIDER than tall for the 1:2 cell.

**6. The winged stag's-head crest.** "crested with the head of a stag" (DuQuette: "Winged
stag's head"). Above the thrown-back helm, an antlered (and winged) stag head, doubling the
theme of the fertile wild land. Read the antlers even at small scale.

**7. The smouldering fire of growth, carried as light, NOT flame.** "their fire is the
smouldering fire of the process of growth." Do NOT draw open fire, torches, or flame-tongues;
that is the Knight of Wands, a different card. Here the fire is the low warm sun / molten
orange-yellow sky glow behind the figure and the ripe gold of the grain. Carry the elemental
Fire entirely in the palette warmth and the sunlight, never in literal flame glyphs.

**8. Palette (ANSI/256 + 16-color fallback), observed from the scan.** A scan exists for
this court card, so map from the painting, cross-checked with the text:
   - Armour: dark near-black burnished plate with cool steel highlights (NOT gold).
   - Horse: rich reddish / chestnut brown, broad heavy draught body, pale flaxen mane and
     tail; solidly standing.
   - Sky: molten orange into yellow, a low warm sun/disk behind the figure.
   - Fields / grasses: golden ripe corn and green blades, wheat-heads catching light.
   - Distant hills: brown-grey cultivated slopes.
   - Cloak / mantle: deep red-brown, hanging heavy at the horse's flank.
   - Disk-shield: dark disk with a lighter rim / boss.
   DuQuette's tenor: "Rich browns, greens, and golden yellow dominate this card." Introduce
   no color with no referent in the scan (no scarlet flame, no blues).

**9. Fire of Earth as the meaning.** Divinatory tone to honor: laborious, patient,
material, instinctive, imitating Nature; dull and heavy but well-knit; the smouldering fire
of growth; the producer of food. Not the rocket-launch of the Knight of Wands but the
opposite pole of the court: rooted, weighty, agricultural, off-duty from war and at work on
the harvest. The image should feel STILL, heavy, and fertile, never explosive.

**10. Mountains and the stag as garnish.** In natural force the Knight of Disks is Mountains
(gravitation, earthquakes, the rooted solidity of Earth). Optional garnish: let the distant
cultivated hills read as low mountain shoulders, and let the stag crest tie the wild fertile
land to the worked field. Small; the standing heavy horse and the corn field carry the card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the horse's
  barrel, the round disk-shield, and any curve WIDER than tall or they squash. Bake the
  correction into the geometry.
- **Center on the axis (col 23).** The horse-and-rider mass centers its VISUAL center on
  column 23. Because this horse STANDS square (no leap), the mass should sit balanced and
  symmetric about the axis, not leaning. Place asymmetric sprites at `23 - len(s)//2` and
  confirm with `--axis`.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the overline
  glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus
  extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Masses dithered, never outlined.** The dark plate, the brown horse, and the disk get
  density ramps for volume, lit directionally. Occlude: the armoured Knight is drawn ON TOP,
  break field and horse edges behind him.
- **Full-bleed density.** Push the composition out to the border. The field and warm sky
  fill the frame; do not float a small standing horse in empty space.
- **Card frame:** keep the outer border box. Court cards have NO top numeral plaque.
  Bottom title band, two lines: `KNIGHT OF DISKS` then `~ yod . fire of earth ~`.
  Romanized letter only, never a Hebrew glyph in the art.

## Render & review
Do not judge horse scale, the standing-vs-leaping read, the field-as-ground read, placement,
or palette by reading the source. Run the chain and LOOK: `compose_knight-disks_lg.py` ->
`frame.py` (`-s disks`, no `-n` numeral for a court card) -> `cardkit.py knight-disks` ->
`render_png.py knight-disks --axis`, then OPEN the PNG and critique it against the scan
`reference/knight-disks-card.jpg`: is the shire horse a large heavy mass standing four-square
(NOT leaping), centered on the axis guide? does the ripe cornland read as the fertile GROUND
he works, not a flat backdrop? is the helmet thrown back, gazing at harvest not battle? is
the flail hanging low toward the grain and the disk read as a solid coin-dish? is the armour
DARK burnished plate (not gold) and the palette rich browns / greens / golden yellow with the
fire carried as warm sun, no flame? Fix the compositor and repeat. Ship at ~80% once the
render holds (2-3 passes max). Note: `knight-disks` must be in `cardkit.CONFIGS` before
render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate, judging
against the Harris scan `reference/knight-disks-card.jpg`), three judges scoring each, then
synthesis / polish / integration merging the strongest read. Three strategies to seed the
composers:
- **A. Horse-dominant** - the heavy standing shire horse is the hero mass filling the frame,
  four-square and rooted, the stocky rider on its back, corn at the hooves.
- **B. Field-dominant** - the ripe fertile cornland and cultivated hills are the subject, the
  Fire-of-Earth-as-agriculture thesis made the whole visual field, horse and rider set into
  it as the worker of the land.
- **C. Contemplation-dominant** - the psychology of the thrown-back helm: the knight gazing
  over the harvest at rest, weight and stillness the read, warm low sun behind him, off duty
  from war.
Tier: **full panel** - the standing-vs-leaping horse, the field-as-ground read, and the
dark-plate palette (against the reflex to make Knights golden and leaping) are contested and
easy to get wrong, so spend the full cost.

## Output
- One large-format art block (target the standard `-art-lg.txt` 47x32 dimensions).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive
  8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A short heavy Knight in dark plate sits a four-square STANDING shire horse in a field of ripe
corn, helm thrown back toward the harvest. Get the standing heavy horse and the fertile
field-as-ground and the card stops being a diagram.
