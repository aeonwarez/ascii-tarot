# Fable5 Prompt - Prince of Disks (Thoth court)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot court card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed. This is a COURT card: no numeral plaque, an elemental title band. Unlike the other courts, a Harris scan DOES exist for this one (`reference/prince-disks-card.jpg`), so judge fidelity against the actual painting, not just Crowley's words.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact leading
whitespace preserved. **Center on the axis (col 23):** the ox-and-chariot mass is centered
on column 23; the enthroned prince sits square on the axis, orb-globe and cross-sceptre
balanced about it. Place asymmetric sprites at `23 - len(s)//2` and verify with `--axis`.
Cells are 1:2 so draw the ox's curved bulk, the wheels, and the orb-globe ~2:1 WIDER than
tall. Courier New; extended alphabet `` ´ ‾ ¡ · `` + line-glyphs `o O v V T L 7 U c C x X`
allowed. Solid masses (the ox, the seed-field, the wheels, the globe) dithered for volume,
never open outlines, lit directionally. Foreground prince drawn ON TOP; break the field and
chariot edges behind him. Full-bleed to the border. Keep outer frame + bottom title band.
Court title band, no numeral. Color mapped to the Harris scan. Sign `aw` or unsigned, never
`jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal quality
shows in the esoteric synthesis and clean compositor structure. It does NOT fix placement
drift, an under-scaled ox/chariot, or a seed-field that reads as flat wallpaper instead of a
packed teeming mass. For those, use the render & review loop.

## Subject
**Prince of Disks. Air of Earth.** Tetragrammaton letter Vau, the Son in the chariot. Rules
21 degrees Aries to 20 degrees Taurus; dominates fixed Taurus, Venus's house with Luna
exalted. A naked meditative prince in light armour, eyes closed, enthroned in a chariot drawn
by an ox, holding an orb-globe of geometry in his left hand and a cross-topped orbed sceptre
in his right, riding a field packed with globular seeds ready to burst into plants. The
darkest card of the suit of Disks, rich browns and greens.

## The composition, in one sentence
The prince sits meditative in an ox-drawn chariot heaped with germinating seed, orb-globe in
the left hand and cross-sceptre in the right, and the whole frame is the packed fertile dark
of Earth become intelligible.

Hold those two facts above all else. If you get only two things right, get the ox-drawn
chariot as the spine of the card and the seed-heavy fertile field as the whole ground.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The ox-drawn chariot IS the composition.** He is Vau, "the Son, represented as in a chariot, going forth to carry out the combined Energy of his parents." A single ox draws it, "this animal being peculiarly sacred to the Element of Earth." In the scan the great red-brown bull is planted HEAD-DOWN at the base, filling the lower third. Draw it large, its curved bulk WIDER than tall (cells are 1:2), horns and muzzle low and heavy on the axis. This is the #1 compositional read: not a man standing but a man CARRIED by a slow, earthbound beast. Nothing here is the Prince of Wands' fire-wheel; this is weight and patience.

**2. A field packed with germinating seed for the whole ground, teeming.** DuQuette: he is "seated in a chariot filled with globular seeds that seem to be ready to burst into plants at any moment." The Prince represents "the florescence and fructification" of Earth. Fill the entire field with clustered spheroid seeds (`(o)(o)(o)`), plough furrows (`,~.~,`), and ripe vegetable masses. Dither it with a density ramp so it reads as a packed teeming mass with depth, not a flat row of circles. This is the fertile abundance of Earth; do not leave the chariot or field empty.

**3. Orb-globe in the LEFT hand, cross-sceptre in the RIGHT.** "In his left hand he holds his disk, which is an orb resembling a globe, marked with mathematical symbols" (an armillary / wire-frame sphere of latitude-and-longitude rings, "the planning involved in agriculture"). "In his right hand he bears an orbed sceptre surmounted by a cross, a symbol of the Great Work accomplished" (a dark shaft, small orb, cross finial). Get the handedness right: pale ringed GLOBE left, dark CROSS-SCEPTRE right. The globe is his single most identifying object, the living revolving Disk made abstract; give it ring arcs, do not draw a plain coin.

**4. Bull-crowned helmet, meditative closed eyes, one still form.** "His helmet is crowned with the head of a bull"; the figure is "meditative," "the element of Earth become intelligible." Draw a bull's-head crest on the helm that RHYMES with the ox drawing the chariot below (two bulls, high and low, frame him). His eyes are CLOSED (DuQuette): the face inward, "mentally directing the brooding fecundity of the entire universe." Unlike the restless bare-armed Prince of Wands, this Prince is held, cool, still. That stillness is the reading.

**5. Light armour, the man cool amid teeming Earth.** "Clothed in light armour" (not the Wands prince's heavy scale mail). Texture the torso lightly (`}v}v{`) and keep the whole figure poised and calm. Everything around him germinates and swells; the meditative armoured man is the composition's one held, deliberate form. That contrast is the Air-of-Earth idea: great energy poised on the most solid practical matter, Earth become intelligible.

**6. The living, revolving green Disk.** Crowley's new doctrine: "the primary colour of Earth not black, but green; it insists that every Disk is a living and revolving symbol." Even in the scan's dark browns, keep the Earth fertile and turning, not dead mineral. The orb-globe should read as a turning thing; the field as sprouting, not inert.

**7. Palette from the Harris scan (ANSI/256 + 16-color fallback).** A scan DOES exist for this card; map its colors deliberately:
   - Field / seeds / furrows: rich browns, umber, olive-green (the darkest card of the suit).
   - The ox/bull: deep terracotta red-brown, the single most saturated mass.
   - Prince: warm ochre flesh; light armour pale bronze-grey; bull-crested helm muted steel.
   - Orb-globe: pale wireframe rings, the one cool light note. Cross-sceptre: dark near-black shaft.
   Introduce no color with no referent in the scan (no blue field, no fire red).

**8. Taurus, the steady fertile force, not Aries' onset.** The Prince dominates fixed Taurus (Venus's house, Luna exalted); the transition Aries-to-Taurus settles the card from onset into patient fertility. Keep the masses full, slow, and heavy. This is endurance and germination, not a lightning flash.

**9. The character as the meaning.** Court cards have no divinatory appendix; the chapter portrait IS the meaning. Energetic and enduring, a capable manager, "competent, ingenious, thoughtful, cautious, trustworthy, imperturbable"; lacking almost entirely in emotion, may appear dull but is not; slow to anger but implacable if driven. DuQuette: "a devil . . . but what a devil," the ultimate handyman in control on the material plane. Render him proud, cool, and inwardly commanding, not a posed mannequin.

**10. Gnomes in the loam.** He is "Prince and Emperor of the Gnomes." Where the seed-field has room, let a gnome or delving-figure suggestion coil in the earth. Garnish, but it is the difference between Thoth and a generic farmer-prince card.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the ox's bulk, the wheels, and the orb-globe WIDER than tall or they render as squashed eggs. Bake the correction into the geometry.
- **Font pin: Courier New.** The extended line alphabet (`` ´ ‾ ¡ · ``) breaks the overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus extended `` ´ ‾ ¡ · `` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border; the seed-field should reach the frame on both sides and the bottom. Do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer double-rule border. Courts carry NO numeral plaque up top (leave the top rule plain per `frame.py -s disks` with no `-n`). Bottom band line 1: `PRINCE OF DISKS`. Bottom band line 2: `~ vau . air of earth ~`. Romanized letter only in the art; the real Hebrew glyph lives in site chrome, never in the `.txt`/`.ans`.

## Render & review
Do not judge ox/chariot scale, the seed-field read, placement, or palette by reading the
source. Run the chain and LOOK: `compose_prince-disks_lg.py` -> `frame.py` (`-s disks`, no
`-n`) -> `cardkit.py prince-disks` -> `render_png.py prince-disks --axis`, then OPEN the PNG
and critique it against `reference/prince-disks-card.jpg` (a scan DOES exist for this court
card, so there IS a reference image beside the render). Judge: is the ox-drawn chariot the
spine of the card (prince CARRIED, not standing), the bull head-down and heavy at the base?
is the whole field a packed teeming seed-mass, not flat circles? is the orb-globe in the LEFT
hand and the cross-sceptre in the right? are the eyes closed and the bull crest on the helm
rhyming with the ox? is the palette rich brown / olive-green / terracotta with the pale
wireframe globe and dark cross-sceptre, no stray colors? Fix the compositor and repeat. Ship
at ~80% once the render holds (2-3 passes max). Note: `prince-disks` must be in
`cardkit.CONFIGS` before render_png will run.

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate, judging against
the Harris scan since one exists for this card), three judges scoring each candidate against
the scan + axis guide, then synthesis / polish / integration merging the strongest read. Three
strategies to seed the composers:
- **A. Chariot-dominant** - the ox-drawn chariot is the hero; the great red-brown bull
  head-down and the wheels fill the lower two-thirds, the prince riding cool above.
- **B. Figure-dominant** - the meditative armoured prince with the orb-globe and cross-sceptre
  is the hero, the ox and seed-field a supporting mass beneath, the bull-crest helm and closed
  eyes carrying the card.
- **C. Seed-field dominant** - the packed germinating field (globular seeds, furrows, ripe
  vegetable mass) overwhelms the frame; the prince and ox are the two held forms read against
  an all-fertile teeming Earth.
Tier: **full panel** - hard card (Harris herself called him "a devil" she could not fit in the
picture); the ox/chariot scale and the seed-field read are hard, so spend the full cost.

## Output
- One large-format art block (target the standard 47x32 art dimensions, framed 51x39).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive 7
  (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A meditative prince rides an ox-drawn chariot heaped with germinating seed, orb-globe in the
left hand and cross-sceptre in the right: get the ox-chariot as the spine and the whole ground
as packed fertile Earth, and the card stops being a farmer-prince diagram.
