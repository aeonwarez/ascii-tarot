# Fable Prompt — Atu VII, The Chariot (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** this is a frontal, throned,
symmetric card. The armoured Charioteer's spine, helmet-crest, the Grail at his hands, and
the canopy peak all sit on column 23; mirror the four pillars, the two scarlet wheels, and
the sphinx-pairs about `AXIS = 23.0` with `PM`/`PMB`, and verify with `--axis`. The classic
bug tell is a centered helmet over a car/body that leans a few columns left. Cells are 1:2
so draw circles/curves ~2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` +
line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never open
outlines, lit directionally. Foreground figure drawn ON TOP; break background edges behind
it. Full-bleed to the border. Keep outer frame + bottom title band. Color mapped to the
Harris painting. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 +
16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the amethyst Grail as full-moon/Great-Sea of
Binah, the four counterchanged Kerubic sphinxes, the ABRAHADABRA canopy, the ten Stars of
Assiah) and clean compositor structure. It does NOT fix placement drift — for that, use the
render & review loop.

## Subject
**Atu VII — The Chariot.** Hebrew letter Cheth ("fence" / enclosure; Cheth = 418 =
ABRAHADABRA), the sign Cancer (Luna rules, Jupiter exalted). Path 18, "The House of
Influence," Binah → Geburah — the Supernals descending through the Veil of Water upon man,
the path crossing the Abyss. A holy armoured King throned in a chariot drawn by four
sphinxes, bearing the Holy Grail beneath a starry canopy; his one function is to bear the
Grail (the Two-in-One elixir). "The Issue of the Vulture, Two-in-One, conveyed; this is the
Chariot of Power. TRINC."

## The composition, in one sentence
An armoured King in amber sits frontal and central under a starry blue canopy, his lowered
visor hiding his face and a crab crest on his helmet, holding a glowing amethyst Holy Grail
at his center, four pillars rising to the canopy, two scarlet wheels to his sides, and four
counterchanged sphinxes drawing the whole beneath him — a stationary, perfectly balanced
throne-on-wheels, not a racing car.

Hold two things above all: the GLOWING CENTRAL GRAIL borne in his hands (the card's heart)
and the FRONTAL, ARMOURED, SYMMETRIC STILLNESS — he is throned, not driving; the chariot is
balanced, self-contained, at rest in motion.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Chariot without these):**

1. **The armoured Charioteer, throned frontal on col 23.** A King in full AMBER armour, no
   flesh exposed, VIZOR lowered ("no man may look upon his face and live"), in a meditative
   posture, throned and holding no reins. Draw him ON TOP; his spine and helmet sit on
   column 23 — mirror the car about the axis, do not let the mass drift left.

2. **The Holy Grail, glowing, at his center.** In his hands, centered, a pure AMETHYST cup
   shaped like the full moon / the Great Sea of Binah, with RADIANT BLOOD at its heart whose
   rays revolve. This is the card's single most important read — keep it central and lit.

3. **The four sphinxes drawing the chariot.** Below and in front, FOUR sphinxes of the four
   Kerubs (Bull, Lion, Eagle, Man), elements counterchanged — TWO dark and TWO light.
   Mirror them in pairs about the axis; keep them small and low.

4. **The starry blue canopy with ABRAHADABRA.** A night-sky-BLUE canopy of Binah, starry,
   spanning the top, the word ABRAHADABRA lettered across it (as ABRACADABRA — the Harris
   typo). The lid of the shrine-on-wheels, centered and symmetric.

**Makes it Thoth (5-7):**

5. **The four pillars.** Four pillars (the regimen of Tetragrammaton) rising from the car to
   hold the canopy — mirror two per side about the axis.

6. **The scarlet wheels.** Two SCARLET wheels (Geburah / Mars, the revolving energy), one to
   each side of the car, mirrored. Draw as 2:1 wide ellipses (1:2 cells).

7. **The crab crest + ten Stars of Assiah.** A CRAB crest atop the helmet (Cancer); ten
   small star-studs (sapphires) scattered on the amber armour.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. A RED cloak over WHITE at his shoulders (passion over purity).
9. The Moon he is seated upon, implied at the base (riding above the tides of emotion).
10. Warm maroon / russet / greenish-brown structure on the car body, against the blue canopy.

---

## Design note (specific to this card)
Sibling/foil to the Priestess (II) and the Hierophant (V): Cancer is the house of the Moon,
so this shares the Priestess's lunar water, but rendered as ARMOUR and WEIGHT — a sealed,
frontal, symmetric shrine. The trap is drawing a dynamic racing chariot; it is the opposite,
a throned figure at perfect rest, "because the whole system of progression is perfectly
balanced." Build the read around the glowing central Grail: if a viewer sees an armoured
seated figure cradling a luminous cup under a starry canopy over four sphinxes, the card
works; the pillars, wheels and crest are supporting symmetry, kept mirrored so they don't
tilt. Value-contrast the four sphinxes (two dark, two light) so the quartet reads as the
counterchanged Kerubs. Palette from BoT/DuQuette: AMBER armour, a deep night-sky BLUE starry
canopy, SCARLET wheels, a violet/AMETHYST Grail with a red-blood center, warm maroon/russet
structure. The `.ans` carries amber figure vs. blue canopy vs. scarlet wheels vs. amethyst
Grail.

## Render & review
Do not judge symmetry, the central Grail, placement, or palette by reading the source. Run
the chain and LOOK: `compose_07-chariot_lg.py` → `frame.py <art> "THE CHARIOT" "~ cheth ·
cancer ~" -w 47 -s majors -n VII` → `cardkit.py 07-chariot` → `render_png.py 07-chariot
--axis`, then OPEN the PNG and critique against the (TBD) Harris scan: does the Charioteer
sit dead on the axis guide? does the amethyst Grail glow at his center as the hero read? are
the four sphinxes counterchanged (two dark, two light) and mirrored low? is the canopy
starry-blue with a legible ABRAHADABRA band, the wheels scarlet and mirrored? Fix the
compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note:
`07-chariot` must be added to `cardkit.CONFIGS` before render_png will run. See
FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Grail dominant** — the glowing amethyst cup at the center as the hero read, the
  Charioteer a dark armoured frame around it.
- **B. Enthroned-figure dominant** — the amber armoured King, visor and crab crest foremost,
  the Grail read at his hands.
- **C. Vehicle-symmetry dominant** — the starry canopy, four pillars, scarlet wheels and
  four sphinxes as a symmetric shrine-on-wheels around a smaller seated figure.
Tier: **full panel** — a symmetric, many-element vehicle with a contested hero (figure vs.
Grail); spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 7`:
top plaque `[ VII ]` in the rule; bottom band `THE CHARIOT` / `~ cheth · cancer ~`

## The one-line brief
An armoured King in amber throned frontal under a starry blue ABRAHADABRA canopy, visor down
and crab-crested, cradling a glowing amethyst Holy Grail at his center, four pillars to the
canopy, two scarlet wheels at his sides, four counterchanged Kerubic sphinxes drawing the
whole beneath him. A perfectly balanced shrine-on-wheels at rest in motion — victory borne,
not driven.
