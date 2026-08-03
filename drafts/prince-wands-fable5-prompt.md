# Fable5 Prompt - Prince of Wands (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed. This is a COURT card: no numeral plaque, an elemental title band, and (see Render & review) no Harris scan exists to check against, so you judge fidelity against Crowley's verbal description.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact leading
whitespace preserved. **Center on the axis (col 23):** the chariot-and-lion mass is centered
on column 23; the enthroned prince sits square on the axis, wand and reining arm balanced
about it. Place asymmetric sprites at `23 - len(s)//2` and verify with `--axis`. Cells are
1:2 so draw the flame wheel and the lion's curved bulk ~2:1 WIDER than tall. Courier New;
extended alphabet `` ´ ‾ ¡ · `` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses
(the lion, the flame field, the wheel) dithered for volume, never open outlines, lit
directionally. Foreground prince drawn ON TOP; break the flame and chariot edges behind him.
Full-bleed to the border. Keep outer frame + bottom title band. Court title band, no numeral.
Color mapped to Crowley's text (no scan). Sign `aw` or unsigned, never `jgs`. Output one
`.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal quality
shows in the esoteric synthesis and clean compositor structure. It does NOT fix placement
drift, an under-scaled lion/chariot, or a flame field that reads as flat wallpaper instead of
a moving sea. For those, use the render & review loop.

## Subject
**Prince of Wands. Air of Fire.** Tetragrammaton letter Vau, the Son in the chariot. Rules 21
degrees Cancer to 20 degrees Leo; dominates fixed Leo, the Sun's steady force. A naked
warrior-prince in scale mail with bare arms, enthroned in a chariot drawn by a lion, holding
the Phoenix wand of the Second Adept, riding on a sea of flames. Crowley's idealized
self-portrait (his Ascendant was 3 degrees Leo).

## The composition, in one sentence
The prince rides a lion-drawn chariot across a sea of flames, phoenix wand raised, and every
mass in the frame is fire in motion except the man and the mail he wears.

Hold those two facts above all else. If you get only two things right, get the lion-drawn
chariot as the spine of the card and the whole floor as a moving sea of flames.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The lion-drawn chariot IS the composition.** He is Vau, "the Son, represented as in a chariot, going forth to carry out the combined Energy of his parents." A single lion draws it; he reins the beast with his bare right arm. The chariot's wheel "is fortified by a wheel radiating flame." Draw the lion large, in profile or three-quarter, its curved bulk WIDER than tall (cells are 1:2), the flame-throwing wheel low and centered on the axis. This is the #1 compositional read: not a man standing in flames but a man CARRIED by a fire-chariot.

**2. A sea of flames for the whole floor, waved and salient.** "He rides upon a sea of flames, both waved and salient." The entire lower field is fire: WAVED (curling, `,^~^v^~,`) at the base and SALIENT (leaping vertical tongues, `^ ^ ^`) rising off it. Dither it with a density ramp so it reads as a moving mass with depth, not a flat row of carets. No water, no earth horizon: fire is the ground he travels on.

**3. The Phoenix wand, raised in the LEFT hand.** "In his left hand he bears the Phoenix wand of the Second Adept, the wand of Power and Energy." The head is a phoenix (rising bird / flame crest), not a plain rod. This is his single most identifying object; give it height and let its flame-crest break the frame's inner air. Right arm is the rein to the lion; left arm is the wand. Get the handedness right.

**4. Crown, winged lion-head, curtain of flame, all one fire-fall.** "He wears a rayed crown surmounted by a lion's head winged, and from this crown depends a curtain of flame." Draw crown-to-shoulders as ONE continuous downpour of fire: rayed crown (`\ | /`), a small winged lion head crest above it, then a curtain of flame falling from the crown past his face. The lion-head crest rhymes with the lion drawing the chariot.

**5. Scale mail with bare arms; the man is the one still thing.** "A warrior in complete armour of scale mail, but his arms are bare on account of his vigour and activity." Texture the torso as scale courses (`}v}v}v{`) and leave the arms as clean bare skin. Everything around him spirals and leaps; the mailed man and his bare, active arms are the composition's one held, deliberate form. That contrast is the Air-of-Fire idea: restless energy given a steady human shape.

**6. The sigil of To Mega Therion on his breast.** The Mark of the Beast (sun-and-crescent) blazoned on the breastplate. This is Crowley's personal seal and appears in only two other cards; it makes this the self-portrait. Small, high-contrast, dead-center on the chest, on the axis. Do not omit it: it is the card's signature.

**7. Palette from Crowley's text (ANSI/256 + 16-color fallback), NO scan.** No Harris painting scan exists in this repo, so build the palette from the words only:
   - Fire field, crown-flames, phoenix wand, chariot wheel: reds / oranges / gold (DuQuette: "fiery reds, yellows, and gold dominate this card").
   - Hair: yellow. Eyes: blue-grey (the single cool accent, the one non-fire color in the card).
   - Scale mail: metallic steel / bronze sheen against the flame ground.
   Introduce no color with no referent in the text above (no green, no blue field).

**8. Leo's steady sun, not the Knight's lightning.** BoT: "the airy part of Fire is sympathetic with Leo, the steady force of energy, the Sun." The fire here is SUSTAINED and radiant, not a jagged flash. Keep the flame masses full and rolling. The flame-wheel low in the frame can read as a small second sun.

**9. The character as the meaning.** Court cards have no divinatory appendix; the chapter portrait IS the meaning. Swift, strong, noble, generous, a boaster who laughs at his own boast, "always fighting against odds and always wins in the long, the very long, run," working "without lust of result." Render him proud and forward-driving, not static. Nobility and momentum, not a posed mannequin.

**10. Salamanders in the fire.** He is "Prince and Emperor of the Salamanders." Where the flame field has room, let a salamander suggestion (elemental fire-lizard) coil in the sea of flames. Garnish, but it is the difference between Thoth and a generic burning-man card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the lion's bulk, the flame wheel, and any curve WIDER than tall or they render as squashed eggs. Bake the correction into the geometry.
- **Font pin: Courier New.** The extended line alphabet (`` ´ ‾ ¡ · ``) breaks the overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus extended `` ´ ‾ ¡ · `` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border; the fire field should reach the frame on both sides and the bottom. Do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer double-rule border. Courts carry NO numeral plaque up top (leave the top rule plain per `frame.py -s wands` with no `-n`). Bottom band line 1: `PRINCE OF WANDS`. Bottom band line 2: `~ vau . air of fire ~`. Romanized letter only in the art; the real Hebrew glyph lives in site chrome, never in the `.txt`/`.ans`.

## Render & review
Do not judge lion/chariot scale, the sea-of-flames read, placement, or palette by reading the
source. Run the chain and LOOK: `compose_prince-wands_lg.py` -> `frame.py` (`-s wands`, no
`-n`) -> `cardkit.py prince-wands` -> `render_png.py prince-wands --axis`, then OPEN the PNG
and critique. IMPORTANT: no Harris scan exists for the court cards, so there is no reference
image beside the render. Judge instead against Crowley's verbal description: is the lion-drawn
chariot the spine of the card (prince CARRIED, not standing)? is the whole floor a moving sea
of flames, waved and salient, not flat carets? is the phoenix wand in the LEFT hand and the
rein in the right? is the Beast sigil dead-center on the breast, on the axis? is the palette
red/orange/gold with the single blue-grey eye accent and metallic mail, no stray colors? Fix
the compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note:
`prince-wands` must be in `cardkit.CONFIGS` before render_png will run.

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate, judging against
Crowley's verbal description since no scan exists), three judges scoring each candidate, then
synthesis / polish / integration merging the strongest read. Three strategies to seed the
composers:
- **A. Chariot-dominant** - the lion-drawn flame chariot is the hero; the prince rides small
  and forward atop a large lion and flame-wheel that fill the lower two-thirds.
- **B. Figure-dominant** - the mailed prince with the raised phoenix wand is the hero, the lion
  and chariot a supporting mass beneath, the Beast sigil and crown-flames carrying the card.
- **C. Fire-field dominant** - the sea of flames (waved + salient) plus crown-curtain overwhelm
  the frame; the prince and lion are the two held forms read against an all-consuming fire.
Tier: **full panel** - hero card (Crowley's self-portrait); the lion/chariot scale and the
sea-of-flames read are hard, so spend the full cost.

## Output
- One large-format art block (target the standard 47x32 art dimensions, framed 51x39).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive 7
  (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A mailed prince rides a lion-drawn chariot across a sea of flames, phoenix wand raised: get the
lion-chariot as the spine and the whole floor as moving fire, and the card stops being a
burning-man diagram.
