# Fable Prompt — Atu XIII, Death (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Anchor to the axis (col 23):** this card is DYNAMIC and
diagonal (a cousin of Lust), NOT a mirrored shrine — Osiris the dancing skeleton reads his
spine on column 23 while the SCYTHE sweeps diagonally across, and the three Scorpio symbols
anchor the corners. Keep the SKELETON'S SPINE on the axis and balance the scythe, the
bubbles, and the corner beasts about `AXIS = 23.0`; verify with `--axis`. The classic bug
tell is a centred skull over a body/scythe that leans a few columns left. Cells are 1:2 so
draw the bubbles and the eagle/scorpion bodies ~2:1 wider than tall. Courier New; extended
alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered
for volume, never open outlines, lit directionally — luminous bubbles glow. Foreground
figure drawn ON TOP; break background edges behind him. Full-bleed to the border. Keep
outer frame + bottom title band. Color mapped to the Harris painting. Sign `aw` or unsigned,
never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (Osiris dancing not reaping, the Saturnian scythe
that CREATES bubbles, the crown of Osiris + feathers of Maat, the three forms of Scorpio as
Scorpion/Serpent/Eagle, the Saturn-glyph legs, putrefaction incubating the Orphic egg) and
clean compositor structure. It does NOT fix placement drift — for that, use the render &
review loop.

## Subject
**Atu XIII — Death** (DuQuette: "The Child of the Great Transformers," "The Lord of the Gate
of Death"). Hebrew letter Nun ("fish" — life beneath the waters). The sign SCORPIO (Mars
rules, Pluto exalted), the 8th house, sexuality and death. Path 24, "Imaginative
Intelligence," Tiphareth → Netzach; also tied to Binah, the "50 gates of death." Alchemically
PUTREFACTION — developing the final form of life from the latent seed in the Orphic egg. "Die
daily. Death is the apex of one curve of the snake Life."

## The composition, in one sentence
Osiris as a black skeleton, crowned with the crown of Upper Egypt and the feathers of Maat,
dances on the bed of the sea sweeping a great Saturnian scythe whose sweep raises luminous
bubbles of new lives, his legs tracing the glyph of Saturn, the three forms of Scorpio — a
scorpion, a serpent, and an eagle — set about him, all in dark subaqueous blue-green and
brown depths.

Hold two things above all: THE DANCING BLACK SKELETON (Osiris with the scythe, the hero read)
and the SCYTHE RAISING BUBBLES OF NEW LIFE (generative, not mowing — the card's turn from
death to renewal).

---

## Ranked directives

**Non-negotiable (1-4, it isn't Death without these):**

1. **Osiris the dancing black skeleton with the scythe.** A BLACK skeleton DANCING (knees
   bent, active, not a stiff reaper) on the seabed, sweeping a great scythe. His body/spine
   reads on column 23; draw him ON TOP. The pose must read as dance, mid-sweep.

2. **The Saturnian scythe raising bubbles of new life.** The scythe (handle a Tau) sweeps
   diagonally; where it passes it RAISES luminous BUBBLES in which new forms take shape — NOT
   mowing the living down. Keep the scythe reading as generative.

3. **The crown of Osiris + feathers of Maat.** On the skull, the crown of Upper Egypt topped
   with the feathers of Maat (as in Adjustment); marks him as Osiris in the waters, not a
   generic Grim Reaper.

4. **The three forms of Scorpio around him.** SCORPION (lowest, lower right, between a
   lily/alpha and a lotus/omega), SERPENT (middle, lower left), EAGLE (highest, upper left,
   exalted). Give each a distinct silhouette in its corner.

**Makes it Thoth (5-7):**

5. **The bubbles of soul-incarnations.** Luminous bubbles rising from the scythe's sweep,
   holding figures of various ages (a man, a woman, a child, a single sperm), threaded
   together — the phallus of Osiris (he creates with the phallus as he destroys with the
   scythe).

6. **The Saturn-glyph legs.** The skeleton's legs arranged to trace the glyph of Saturn;
   between them, the death-process figures below.

7. **The beheading / rising-figure process.** Two small figures at the legs: a LOWER one
   being beheaded as the scythe crosses its neck, an UPPER one rising from the head after
   death wrapped in bright light — the higher mind freed from the lower vehicles.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The lily (left) and lotus (right), Saturnian, shaped as alpha/omega, framing the scorpion.
9. The three states of water read into the corner beasts (Scorpion=ice, Serpent=water,
   Eagle=gas) if the silhouettes allow.
10. The murky underwater field — keep the whole scene subaqueous, the black skeleton against
    blue-green over brown/indigo depths.

---

## Design note (specific to this card)
Death is a dynamic diagonal card like Lust — do NOT force a mirror; build a dancing skeleton
with the spine pinned to the axis and the scythe sweeping across, the three Scorpio symbols
anchoring the corners. Where Lust blazes hot and the Hanged Man glows green-and-pale, Death is
the DARK card of the run: a murky subaqueous field, blue-green over brown/indigo, a black
skeleton, with only the luminous bubbles and the rising-figure's light as highlights — let the
`.ans` read dark and cold against the neighbours. The danger is a stiff land-reaper (kill it:
knees bent, underwater, mid-dance) and the three Scorpio beasts blurring into the murk (give
each a clear corner silhouette). Keep the crown + Maat feathers legible on the skull and the
scythe reading as generative, raising bubbles, not cutting people down. Palette from
BoT/DuQuette: dark blue-green over dull/very-dark brown and livid indigo; a BLACK skeleton
(Saturn/Osiris) crowned with Osiris's crown + Maat feathers; a Saturnian SCYTHE; luminous
BUBBLES of soul-figures; a SCORPION, SERPENT, EAGLE in the corners. The `.ans` carries a dark
subaqueous field, a black skeleton, glowing bubbles.

## Render & review
Do not judge the diagonal, the dance, the three beasts, placement, or palette by reading the
source. Run the chain and LOOK: `compose_13-death_lg.py` → `frame.py <art> "DEATH" "~ nun ·
scorpio ~" -w 47 -s majors -n XIII` → `cardkit.py 13-death` → `render_png.py 13-death --axis`,
then OPEN the PNG and critique against the (TBD) Harris scan: does the skeleton's spine sit on
the axis guide with the scythe sweeping across? does the pose read as DANCE, underwater? does
the scythe raise luminous bubbles (generative, not reaping)? is the crown + Maat feathers
legible? do the scorpion / serpent / eagle separate into distinct corner silhouettes? is the
field dark and cold against the hot Lust / green Hanged Man neighbours? Fix the compositor and
repeat. Ship at ~80% once the render holds (2-3 passes max). Note: `13-death` must be added to
`cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Skeleton dominant** — Osiris dancing with the scythe as the hero figure filling the
  frame, the bubbles and Scorpio beasts his attributes.
- **B. Scythe-and-bubbles dominant** — the generative sweep as the hero read: the arc of the
  scythe and the rising stream of soul-bubbles carrying the eye, the skeleton the engine of it
  (emphasise renewal over death).
- **C. Three-forms-of-Scorpio dominant** — the Scorpion/Serpent/Eagle triad as the framing
  read (the cycle of putrefaction: ice/water/gas), the dancing skeleton the axis they revolve
  around.
Tier: **full panel** — a dynamic, many-element, easily-misread (reaper vs renewer) card;
spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 13`:
top plaque `[ XIII ]` in the rule; bottom band `DEATH` / `~ nun · scorpio ~`

## The one-line brief
Osiris as a black skeleton, crowned with Upper Egypt's crown and the feathers of Maat, dances
on the seabed sweeping a Saturnian scythe that raises luminous bubbles of new lives, his legs
the glyph of Saturn, a scorpion, serpent, and eagle set about him, in dark subaqueous depths.
Transformation and change; die daily; apparent death or destruction, but such interpretation is
illusion — every change the effect of an act of love.
