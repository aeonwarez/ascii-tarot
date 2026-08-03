# Fable5 Prompt - Prince of Swords (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed. This is a COURT card: no numeral plaque, an elemental title band. A Harris scan DOES exist (`reference/prince-swords-card.jpg`, esotericmeanings.com court-cards page), so judge fidelity against it in the Render & review loop.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact leading
whitespace preserved. **Center on the axis (col 23):** the armoured Prince stands square on
column 23; the raised sword rises on the axis and the winged fairies scatter symmetrically
about it at the base. Place asymmetric sprites at `23 - len(s)//2` and verify with `--axis`.
Cells are 1:2 so draw the yellow bubble-suns and any curve ~2:1 WIDER than tall or they render
as squashed eggs. Courier New; extended alphabet `` ´ ‾ ¡ · `` + line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses (the green Prince, the bubble-suns) dithered
for volume, never open outlines, lit directionally. Foreground Prince drawn ON TOP; break the
crystalline facet lines and bubble edges behind him. Full-bleed to the border. Keep outer frame
+ bottom title band. Court title band, no numeral. Color mapped to the Harris scan. Sign `aw`
or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal quality
shows in the esoteric synthesis and clean compositor structure. It does NOT fix placement
drift, an under-read sword/sickle handedness, or a field that reads as flat wallpaper instead
of a shattered geometric lattice. For those, use the render & review loop.

## Subject
**Prince of Swords. Air of Air.** Tetragrammaton letter Vau, the Son in the chariot. Rules 21
degrees Capricorn to 20 degrees Aquarius; dominates fixed Aquarius. An armoured prince in a
geometric chariot drawn by winged, capricious fairy-children, sword raised in the right hand to
create and sickle lowered in the left to destroy. A picture of the Mind as such: motion without
destination.

## The composition, in one sentence
An armoured green Prince stands over three winged fairies hauling his chariot in three
different directions, sword up to create and sickle down to destroy, the whole field ruled into
crystalline geometry that goes nowhere.

Hold those two facts above all else. If you get only two things right, get the create-and-
destroy (sword up right hand / sickle down left hand) and the chariot pulled by scattering,
un-reined fairies as the read of a Mind in aimless motion.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The chariot drawn by winged, capricious fairies IS the thesis.** He is Vau, "the Son, represented as in a chariot, going forth to carry out the combined Energy of his parents." But this chariot goes nowhere on purpose: "drawn by winged children, looking and leaping irresponsibly in any direction that takes their fancy; they are not reined, but perfectly Capricious. The chariot consequently is easy enough to move, but quite unable to progress in any definite direction except by accident. This is a perfect picture of the Mind." Draw three winged fairy-children low in the frame, each pulling a slack, crossed line off in a DIFFERENT direction. The composition must read as diverging, not converging. No taut reins.

**2. Sword up in the RIGHT hand, sickle down in the LEFT.** "In his right hand is a lifted sword wherewith to create, but in his left hand a sickle, so that what he creates he instantly destroys." Create-and-destroy in one figure, one gesture per hand: the sword raised tall (let it break the inner air), the sickle held low and curved. Get the handedness right. This is his single most identifying pair of objects and the card's core paradox.

**3. The whole field is Air reduced to crystalline geometry.** "The operation of his logical mental processes have reduced the Air, which is his element, to many diverse geometrical patterns, but in these there is no real plan; they are demonstrations of the powers of the Mind without definite purpose." Rule the entire ground into thin faceted triangles and lattices (`/\_/\`, `<>`, ruled diagonals). It must read as shattered glass / diagram, not open sky. This is the most ASCII-native idea in the card: pure line-work with no destination.

**4. The armoured Prince as the one held form on the axis.** "The figure of this Prince is clothed with closely woven armour adorned with definite device." He is the single fixed human mass on column 23; everything else scatters and diverges around him. Texture the torso as closely-woven mail with a small central device (`[=x=]`), and let his body be the hub the fairies' pull-lines radiate from. In the scan he is the one saturated mass; keep him solid against the pale splinter field.

**5. The radiant child's head / secret crown.** "On the head of this Prince is, nevertheless, a child's head radiant, for there is a secret crown in the nature of this card; if concentrated, it is exactly Tiphareth." Crown him with a small radiant head throwing rays (`\|/` over `(o)`): the hidden solar centre, the one point of order inside all the aimless motion. Do not omit it; it is the card's secret.

**6. Yellow bubble-suns enclosing the wings.** DuQuette: "The geometrical wings of the Prince and the children are enclosed in bright yellow bubbles - air of air." Draw large round luminous cells (`.-~-.` / `( o )`, wider than tall) around the wing-clusters, several reading as full yellow suns scattered behind the figure. This is the air-of-air medium made visible; it is also the card's warm color against the cold green and pale ice.

**7. Palette from the Harris scan (ANSI/256 + 16-color fallback).** A scan exists; map it, do not invent:
   - The Prince and the fairy-children: metallic GREEN (the dominant, saturated figure-color).
   - Bubbles / sun-disks: bright warm YELLOW-GOLD.
   - Field / facet line-work: pale SILVER-WHITE ice crystals and fine grey-green ruled lines.
   DuQuette confirms: "Clouds of sharp white ice crystals, yellows, and metallic greens dominate this card." Introduce no color with no referent in the scan (no red, no blue field).

**8. Drawn swords, dark clouds, nimbi in the field.** DuQuette symbol list: "Arch Fairies winged. Dark clouds, nimbi, drawn swords." Scatter extra sword blades and cloud/nimbus bands through the geometric field as the suit's weather; the winged angel's-head crest can rhyme with the radiant child's head up top.

**9. The character as the meaning.** Court cards have no divinatory appendix; the chapter portrait IS the meaning. "Full of ideas and designs which tumble over each other . a mass of fine ideals unrelated to practical effort . intensely clever, admirably rational, but unstable of purpose." Immensely powerful "because of its complete freedom from settled principles." Render him brilliant and forward-driving yet aimless: energy scattered, not focused. The figure creates and destroys in the same breath.

**10. The 57th Hexagram, Sun, flexibility and penetration.** BoT: the airy part of Air is Hexagram 57, "one of the most difficult figures in the book, on account of its ambivalence: it means both flexibility and penetration." Where the field has room, let the geometry both bend (flexibility) and stab (penetration): curved lattice giving way to sharp sword-points. Garnish, but it is the difference between Thoth and a generic swordsman card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the yellow bubble-suns and any wing-curve WIDER than tall or they render as squashed eggs. Bake the correction into the geometry.
- **Font pin: Courier New.** The extended line alphabet (`` ´ ‾ ¡ · ``) breaks the overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus extended `` ´ ‾ ¡ · `` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border; the facet field and bubble-suns should reach the frame on both sides and the bottom. Do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer double-rule border. Courts carry NO numeral plaque up top (leave the top rule plain per `frame.py -s swords` with no `-n`). Bottom band line 1: `PRINCE OF SWORDS`. Bottom band line 2: `~ vau . air of air ~`. Romanized letter only in the art; the real Hebrew glyph lives in site chrome, never in the `.txt`/`.ans`.

## Render & review
Do not judge sword/sickle handedness, the diverging-fairies read, placement, or palette by
reading the source. Run the chain and LOOK: `compose_prince-swords_lg.py` -> `frame.py`
(`-s swords`, no `-n`) -> `cardkit.py prince-swords` -> `render_png.py prince-swords --axis`,
then OPEN the PNG and critique against `reference/prince-swords-card.jpg`: is the sword raised
in the RIGHT hand and the sickle lowered in the LEFT? do the three winged fairies pull the
chariot in three DIFFERENT directions (diverging, not converging, un-reined)? is the whole
field ruled into crystalline geometry, not open sky? is the radiant child's head crowning him?
is the palette metallic green / yellow-gold bubbles / pale ice-white, no stray colors? Fix the
compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note:
`prince-swords` must be in `cardkit.CONFIGS` before render_png will run.

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate, judging against
`reference/prince-swords-card.jpg` + the axis guide), three judges scoring each candidate, then
synthesis / polish / integration merging the strongest read. Three strategies to seed the
composers:
- **A. Chariot / fairy-dominant** - the three winged fairy-children hauling the chariot in
  three directions fill the lower two-thirds; the Prince rides small above them, the diverging
  pull-lines the hero of the read.
- **B. Figure-dominant** - the armoured green Prince with sword up and sickle down is the hero,
  the radiant child's head and central device carrying the card, fairies a supporting mass
  below.
- **C. Geometry-field dominant** - the crystalline facet lattice and yellow bubble-suns
  overwhelm the frame; the Prince and fairies are the held green forms read against an
  all-consuming field of aimless Air-of-Air geometry.
Tier: **full panel** - the sword/sickle handedness, the diverging-fairies read, and the
shattered-geometry field are all hard to land, so spend the full cost.

## Output
- One large-format art block (target the standard 47x32 art dimensions, framed 51x39).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive 7
  (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
An armoured green Prince stands over winged fairies hauling his chariot three ways at once,
sword up to create and sickle down to destroy across a field of aimless crystalline geometry:
get the create-and-destroy handedness and the diverging un-reined fairies, and the card stops
being a swordsman diagram.
