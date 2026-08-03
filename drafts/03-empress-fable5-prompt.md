# Fable Prompt - Atu III, The Empress (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the enthroned figure's
visual center sits on column 23, not its left edge. Mirror the symmetric throne/crown
about `AXIS = 23.0` with `PM`/`PMB`; for asymmetric sprites place at `23 - len(s)//2`
and verify with `--axis`. The classic bug tell is a centered head over a body that leans
a few columns left. Cells are 1:2 so draw circles/curves ~2:1 wider than tall. Courier
New; extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid
masses dithered for volume, never open outlines, lit directionally. Foreground figure
drawn ON TOP; break background edges behind it. Full-bleed to the border. Keep outer
frame + bottom title band. Color mapped to the Harris painting. Sign `aw` or unsigned,
never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift or busyness - for those, use the render & review loop.

## Subject
**Atu III - The Empress.** Hebrew letter Daleth ("door"), attribution the planet
Venus. Path 14 "Illuminating Intelligence," Chokmah → Binah, uniting the Supernal
Father with the Supernal Mother - one of the three paths wholly ABOVE the Abyss and
the FIRST trump to join the two side pillars. "The Daughter of the Mighty Ones."
She is Venus/Aphrodite (consort to the Emperor/Mars), the Great Mother nurturing the
Universe with the milk of Spiritual Light, and the alchemical principle SALT. The
doctrine: the fundamental formula of the Universe is LOVE.

## The composition, in one sentence
A serene enthroned goddess sits high and frontal, crowned with the moon-phase Crown
of Isis between a waxing and a waning moon, her ARMS forming the alchemical Salt glyph
- a blue lotus lifted to her heart in one hand, the other arm curved low to cradle her
pregnant belly (Mater Triumphans); her twisted-flame/grass throne rises through cool
green vegetation with a sparrow and dove perched at its tops, and below sit the white
Pelican feeding its young, the white double-eagle shield holding the Moon, and a carpet
of fleurs-de-lis and fish adoring the Secret Rose.

Hold two things above all: the SALT-glyph gesture of the arms (lotus-to-heart + belly
cradle, she is pregnant), and the overall WARM VEGETAL SERENITY - soft green growth,
not a rigid geometric field. She is love uniting Will and Understanding; disregard the
parts, feel the whole.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Empress without these):**

1. **The enthroned goddess + Salt-glyph arms + Mater Triumphans.** A calm seated
   woman high on the central axis, gazing gently down. Her ARMS trace the alchemical
   glyph of SALT (a circle riding a horizontal bar): a blue lotus lifted to her HEART
   in her right hand, her left arm curved LOW cradling a rounded pregnant belly with a
   faint infant inside (Isis suckling Horus). Green skirt, passionate RED blouse. Draw
   her ON TOP; break the vegetation behind her.

2. **The Crown of Isis + revolving moons.** Moon-phase crown (waxing-full-waning) at
   her head, topped by the Maltese cross (four elements in balance). A revolving moon
   to each side of her - a waxing crescent she faces and a waning crescent - legible,
   iconic. Do not omit; they name her Venus-Luna.

3. **The twisted throne + sparrow & dove.** Throne uprights = twisted ropes of blue
   flame reading as blades of grass (`{ } ( ) S` curls), born of water. Perch her two
   sacred birds of Venus at the tops: a small sparrow and a small dove.

4. **Venus / the vegetal whole.** Cool EMERALD + SPRING GREEN + SKY BLUE field of soft
   leafy growth (dithered masses, NOT straight rays - this is her contrast with the
   Priestess). A golden ZODIAC girdle at her waist. The Venus glyph faintly hidden in
   the shield. The card reads as one soothing whole; symmetry is gentle, not rigid.

**Makes it Thoth (5-7):**

5. **The lotus of Isis to the heart.** The blue lotus in her right hand held over the
   heart chakra - roots in water, petals open to the Sun (belly of the chalice = the
   Holy Grail). Heart-path, not head-path. One clean curved bloom.

6. **The heraldry - Pelican + White Eagle.** LOWER LEFT: the white Pelican bending to
   feed its brood from its own breast (the Great Mother; Aeon of Osiris). LOWER RIGHT:
   a heater shield, green+white field, a white DOUBLE-HEADED EAGLE holding a small
   waxing Moon in its beaks (the alchemical white tincture; New Aeon of Horus).

7. **The floor tapestry + Secret Rose.** A carpet of fleur-de-lis diamonds and tiny
   FISH at the base, seeming to adore the white SECRET ROSE at the foot of the throne,
   from which green-tinged waters of Universal Life spread.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. Bees + black/white dominos wrapped in spiral rose-petal lines on her robe.
9. The Arch / Door of Daleth behind her (the "Gate of Heaven") - a faint framing arch.
10. Antimony glyph (orb + cross) echoed at the crown; two tiny fish in the waters.

---

## Design note (specific to this card)
Sibling/consort to the Emperor (IV): where he is fiery red, angular, martial, SHE is
the cool cure - soft green vegetation, twisted-grass throne, rounded pregnant curves.
The risk here is the OPPOSITE of the Priestess: not flatness but BUSYNESS. There are
many named symbols (crown, moons, lotus, birds, pelican, eagle-shield, rose, fish,
fleurs, bees, dominos, zodiac). Crowley's own instruction is the cure: "disregard the
parts, concentrate upon the whole." Let the arms + belly + crown carry the read; keep
the heraldry and tapestry as small quiet marks in the lower corners so they don't fight
the figure. Palette from the scan: cool EMERALD/SPRING GREEN + SKY BLUE field, RED
blouse, GOLD zodiac belt, BLUE lotus, WHITE pelican and double-eagle heraldry, and a
warm-white Secret Rose over green waters. The `.ans` carries green field vs. red blouse
vs. gold belt vs. white heraldry.

## Render & review
Do not judge placement, mass volume, occlusion, or palette by reading the source. Run
the chain and LOOK: `compose_03-empress_lg.py` → `frame.py` → `cardkit.py 03-empress` →
`render_png.py 03-empress --axis`, then OPEN the PNG and critique against the Harris
scan: does she sit on the axis guide (not leaning left)? do the Salt-glyph arms read
(lotus-to-heart + belly cradle)? is the field soft vegetal mass, not straight rays? are
the many props (pelican, eagle-shield, rose, fish, fleurs) small and quiet in the
corners so they don't fight the figure? Fix the compositor and repeat. Ship at ~80% once
the render holds (2-3 passes max). See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate), three
judges scoring each against the Harris scan + axis guide, then synthesis / polish /
integration merging the strongest read. Three strategies to seed the composers:
- **A. Figure + Salt-arms dominant** - the pregnant goddess and the lotus-to-heart +
  belly-cradle gesture are the hero.
- **B. Vegetal-throne enveloping** - the twisted-grass throne and soft green growth wrap
  a nested figure; the whole card is her garden.
- **C. Heraldry-framed** - pelican, white eagle-shield and Secret Rose balanced in the
  corners around a calmer central figure.
Tier: **middle path** - the risk is busyness, not composition ("disregard the parts");
run one composer + the render loop + one adversarial critique, escalate only if it will
not cohere as one whole.

## Title band
Via `tools/frame.py -s majors -n 3`:
top plaque `[ III ]` in the rule; bottom band `THE EMPRESS` / `~ daleth · venus ~`

## The one-line brief
A moon-crowned green goddess enthroned and pregnant, arms tracing the alchemical Salt
glyph - blue lotus to her heart, the other arm cradling her belly - on a twisted-grass
throne with sparrow and dove, amid cool vegetation, a waxing and waning moon revolving
beside her; below, the white Pelican feeding its young and the white double-eagle
shield holding the Moon, over a carpet of fleurs-de-lis and fish adoring the Secret
Rose. Universal Love as the whole; disregard the parts.
