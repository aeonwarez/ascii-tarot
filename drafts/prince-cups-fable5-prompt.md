# Fable5 Prompt - Prince of Cups (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed. This is a COURT card: no numeral plaque, an elemental title band. A Harris scan DOES exist for this card (`reference/prince-cups-card.jpg`), so judge fidelity against BOTH the painting and Crowley's verbal description.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact leading
whitespace preserved. **Center on the axis (col 23):** the eagle-and-chariot mass is
centered on column 23; the enthroned prince sits square on the axis, lotus and serpent-cup
balanced about it. Place asymmetric sprites at `23 - len(s)//2` and verify with `--axis`.
Cells are 1:2 so draw the great eagle's spread wings and the shell chariot's curved bulk
~2:1 WIDER than tall. Courier New; extended alphabet `` ´ ‾ ¡ · `` + line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses (the black eagle, the water, the shell
chariot) dithered for volume, never open outlines, lit directionally. Foreground prince
drawn ON TOP; break the eagle and chariot edges behind him. Full-bleed to the border. Keep
outer frame + bottom title band. Court title band, no numeral. Color mapped to the Harris
painting. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16
fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal quality
shows in the esoteric synthesis and clean compositor structure. It does NOT fix placement
drift, an under-scaled eagle, or a water field that reads as flat wallpaper instead of a calm
lake struck by rain. For those, use the render & review loop.

## Subject
**Prince of Cups. Air of Water.** Tetragrammaton letter Vau, the Son in the chariot. Rules 21
degrees Libra to 20 degrees Scorpio; dominates fixed Scorpio, the most mysterious of the
signs. A warrior part-clad in armour that is "rather a growth than a covering," enthroned in a
shell-shaped chariot drawn by an enormous eagle, a lotus in his right hand and in his left a
cup from which a serpent rises, above the calm stagnant water of a lake on which rain falls
heavily. Elasticity, volatility, and the energy of steam; a calm surface masking the most
intense passion.

## The composition, in one sentence
An eagle-drawn shell chariot bursts straight at the viewer out of a crashing wave, the
green prince riding it with lotus in the right hand and a serpent rising from the cup in his
left, over a calm rain-struck lake.

Hold those two facts above all else. If you get only two things right, get the great
eagle-drawn chariot as the spine of the card and the lotus-right / serpent-cup-left pair in
the prince's hands.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The eagle-drawn chariot IS the composition.** He is Vau, "the Son, represented as in a chariot, going forth to carry out the combined Energy of his parents." A single enormous eagle draws the shell chariot; in Harris's scan it bursts straight at the viewer, wings spread full width. Draw the eagle large, wings spanning the frame edge to edge, its bulk WIDER than tall (cells are 1:2), centered on the axis, the darkest mass in the card. This is the #1 compositional read: not a man in water but a man CARRIED forward by a great eagle out of a crashing wave.

**2. Lotus in the RIGHT hand, serpent-cup in the LEFT.** "In his right hand he bears a Lotus flower, sacred to the element of Water, and in his left hand is a cup from which issues a serpent." A coiled snake rises out of the cup. These are his two most identifying objects and they must be on the correct hands (lotus right, serpent-cup left). The serpent is Scorpio's hidden totem, the eagle its manifested one; the two rhyme across the card.

**3. The prince himself: green warrior in growth-armour, gaseous wings.** "A warrior partly clad in armour, which seems, however, rather a growth than a covering." Draw the armour as an organic outgrowth of the (sea-green) body, one continuous surface, NOT worn metal plate. "His wings are tenuous, almost of gas": render his own wings as translucent vapor / steam wisps (`` `·~·` ``), half-transparent, the visible sign of his "power of volatilization." The green figure with gas wings is the Air-of-Water idea in a body.

**4. The eagle-helmet crest.** "His helmet is surmounted by an eagle." A small eagle crest atop his head, echoing the great eagle drawing the chariot below. Crown-to-crest should read as one vertical rhyme: little eagle up top, huge eagle beneath. Keep it small; Crowley says the eagle (Scorpio's manifested part) "is in reality the least important part of his nature," so it is emblem, not hero.

**5. A calm stagnant lake struck by heavy rain, under a crashing wave.** "Beneath his chariot is the calm and stagnant water of a lake upon which rain falls heavily." The lower field is still, sinister water (`~.~^~.~`) struck by vertical rain (`| | | |`), while the chariot bursts forward from a crashing wave (DuQuette). Dither the water with a density ramp so it reads as a calm surface over hidden depth, not a flat row of tildes. The calm surface over intense passion IS the Scorpio mask.

**6. The shell chariot.** "His chariot, which resembles a shell." A ribbed, nautilus-like curved car cradling the prince, distinct in texture from the eagle's feathers and from the growth-armour. It sits between the man and the eagle; give it a couple of ribbed curves so the eye reads "shell," not "cart."

**7. The scorpion, present by its ABSENCE.** "The third totem, the scorpion, is not shewn in the picture, for the putrefaction which it represents is an extremely secret process." Do NOT draw a scorpion. Honor it as the card's secret: the composition's held tension is the eagle and serpent shown, the scorpion withheld. This restraint is a real Thoth directive, not a gap to fill.

**8. Palette from the Harris scan (ANSI/256 + 16-color fallback).** A scan exists; map its colors deliberately:
   - Field and water: cool blues and blue-greens dominate (DuQuette: "as they do the other Cups court cards"), pale ice-blue cloud swirls to deep teal water.
   - The great eagle: near-black / dark slate, the darkest mass and strongest contrast.
   - The prince: sea-green skin and darker green-blue growth-armour, one continuous surface.
   - Serpent-cup: bone / off-white (the one small warm break). Lotus: pale pink-white with a dark heart (the second warm accent). His wings: translucent silver-white vapor.
   Introduce no color with no referent in the scan (no red field, no gold).

**9. The character as the meaning.** Court cards have no divinatory appendix; the chapter portrait IS the meaning. Subtle, secret, an artist in all his ways: "on the surface he appears calm and imperturbable, but this is a mask of the most intense passion," "perfectly ruthless," and "cannot be relied upon to work in harness." Render him calm-faced and forward-driving but with coiled tension (the serpent, the crashing wave), not placid. The surface calm over hidden violence is the whole card.

**10. Steam and volatilization in the negative space.** The card is Air of Water: "the catalytic faculty and the energy of steam," "hydrostatic equilibrium." Where the cloud field has room, let vapor curls and rising steam wisps fill the space between the calm lake below and the pale cloud swirls above, so the field reads as water becoming air. Garnish, but it is the difference between Thoth and a generic eagle-rider card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the eagle's spread wings, the shell chariot, and any curve WIDER than tall or they render as squashed eggs. Bake the correction into the geometry.
- **Font pin: Courier New.** The extended line alphabet (`` ´ ‾ ¡ · ``) breaks the overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus extended `` ´ ‾ ¡ · `` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border; the eagle's wings should reach the frame on both sides and the water should reach the bottom. Do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer double-rule border. Courts carry NO numeral plaque up top (leave the top rule plain per `frame.py -s cups` with no `-n`). Bottom band line 1: `PRINCE OF CUPS`. Bottom band line 2: `~ vau . air of water ~`. Romanized letter only in the art; the real Hebrew glyph lives in site chrome, never in the `.txt`/`.ans`.

## Render & review
Do not judge eagle scale, the calm-lake read, placement, or palette by reading the source. Run
the chain and LOOK: `compose_prince-cups_lg.py` -> `frame.py` (`-s cups`, no `-n`) ->
`cardkit.py prince-cups` -> `render_png.py prince-cups --axis`, then OPEN the PNG and critique
it against `reference/prince-cups-card.jpg` (the scan is drawn beside the colored render).
Judge: is the great eagle the spine of the card (prince CARRIED, wings full-bleed), the darkest
mass on the axis? is the lotus in the RIGHT hand and the serpent-cup in the LEFT? are the
prince's wings gaseous vapor, not solid feather? is the lower field a calm lake struck by
vertical rain, over a crashing wave, not flat tildes? is the palette blue / teal / sea-green
with the bone serpent-cup and pale lotus as the only warm accents, no stray colors? is the
scorpion correctly ABSENT? Fix the compositor and repeat. Ship at ~80% once the render holds
(2-3 passes max). Note: `prince-cups` must be in `cardkit.CONFIGS` before render_png will run.

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate, judging against
BOTH the Harris scan and Crowley's verbal description), three judges scoring each candidate,
then synthesis / polish / integration merging the strongest read. Three strategies to seed the
composers:
- **A. Eagle-dominant** - the enormous black eagle with full-bleed wings is the hero; the
  shell chariot and prince ride small and forward atop it, bursting from the wave.
- **B. Figure-dominant** - the green prince with lotus and serpent-cup is the hero, the eagle a
  supporting dark mass beneath, the growth-armour, gas wings, and eagle-helmet crest carrying
  the card.
- **C. Water-field dominant** - the calm rain-struck lake plus crashing wave and rising steam
  overwhelm the frame; the eagle and prince are the two held forms read against an all-water
  field turning to air.
Tier: **full panel** - hero court card; the eagle scale, the calm-lake-vs-crashing-wave read,
and the lotus-right / serpent-cup-left handedness are hard and contested, so spend the full
cost.

## Output
- One large-format art block (target the standard 47x32 art dimensions, framed 51x39).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive 8
  (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
An eagle-drawn shell chariot bursts at the viewer out of a crashing wave, the green prince
riding it with lotus right and serpent-cup left over a calm rain-struck lake: get the great
eagle as the spine and the lotus / serpent-cup handedness, and the card stops being an
eagle-rider diagram.
