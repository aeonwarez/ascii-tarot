# Fable Prompt - Atu IX, The Hermit (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Build on the Yod spine (col 23):** the cowl-peak, the ibis
head, the lantern-hand, the Orphic egg and the toe read down column 23 - less strictly
mirror-symmetric than VII/VIII (it is a single stooped figure, not a mirrored shrine), but
keep the figure's vertical spine and the wheat/ray balance about `AXIS = 23.0` with `PM`/`PMB`
and verify with `--axis`. The classic bug tell is a centered cowl over a body/egg that leans
a few columns left. Cells are 1:2 so draw circles/curves ~2:1 wider than tall. Courier New;
extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses
dithered for volume, never open outlines, lit directionally - the lantern is the light
source. Foreground figure drawn ON TOP; break background wheat/rays behind him. Full-bleed
to the border. Keep outer frame + bottom title band. Color mapped to the Harris painting.
Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the Yod-shaped Logos, the lantern's Sun-core with
its four rays completing the cycle to the egg, the spermatozoon-wand with its homunculus and
Kether-diamond, the tamed three-headed Cerberus) and clean compositor structure. It does NOT
fix placement drift - for that, use the render & review loop.

## Subject
**Atu IX - The Hermit.** Hebrew letter Yod ("the Hand" - the seed-letter, foundation of all
the others; the Father, the highest Mercury, the Logos, whose physical representative is the
spermatozoon - hence "The Hermit"). The sign Virgo (Mercury both RULES and is EXALTED). Path
20, "The Intelligence of Will," Chesed → Tiphareth - the light of the higher self carried in
silence and solitude. Thoth / Mercury as psychopompos, guide of souls out of the ignorance
of Hades. "Wander alone; bearing the Light and thy Staff."

## The composition, in one sentence
An ancient cowled prophet bent into the shape of the letter Yod, ibis-headed, only his hand
visible, holds aloft a diamond lantern whose core is the Sun (casting four yellow rays) and
gazes down into a green Orphic egg wound by a many-coloured serpent, his spermatozoon-wand
lower-left, the tamed three-headed Cerberus at his heel, all in a field of golden wheat
under two crossing white rays.

Hold two things above all: the GLOWING SUN-LANTERN held aloft (the card's light and hero
read) and the STOOPED YOD-FIGURE bent inward over the luminous EGG (wisdom grown in silence).

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Hermit without these):**

1. **The cowled, ibis-headed Hermit, Yod-shaped, on the axis.** An ancient hooded PROPHET
   bent in the shape of the letter YOD, IBIS-headed (Thoth / Mercury), only his HAND visible,
   turned inward and downward. Draw him ON TOP; his cowl-peak, head and spine sit on column
   23 - do not let the mass drift left.

2. **The lantern with the Sun at its heart, held aloft.** In his raised hand a DIAMOND
   lantern whose center is the SUN (the Sigil of the King of Fire), glowing, casting FOUR
   yellow rays. The single most important read - keep it lit and high.

3. **The green Orphic egg + iridescent serpent, contemplated.** Before/below him the green
   (Venus) Orphic EGG wound by a MANY-COLOURED serpent, the subjective universe he gazes
   into. Centered low, the object of his downward gaze.

4. **The spermatozoon-wand (the Logos / seed of life).** Lower-left, his WAND is a
   spermatozoon - a homunculus / foetus coiled within, a KETHER-diamond at its head - lit by
   one of the lantern's rays. The Father's physical representative.

**Makes it Thoth (5-7):**

5. **Cerberus, the three-headed hound, tamed.** At his heel the three-headed dog (speech /
   thought / action of the lower self), tamed and following - the lower nature raised to
   serve the higher. Small and low.

6. **The field of wheat.** A background of golden WHEAT (Virgo, Persephone): inner wisdom
   grown slowly like a crop, surrounding him; the one warm color in a cool field.

7. **The four rays + the pyramid + horizon.** The lantern's four yellow rays reach the egg
   (bottom), the apex of a PYRAMID (top), the sperm-wand (lower-left) and Cerberus - the
   completed cycle. Two separate WHITE rays cross the top (not from the lamp): the upper
   forming the pyramid, the lower the horizon.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The distinct ibis / beaked profile of Thoth on the cowled head.
9. The Kether-diamond motifs in the lantern and the spermatozoon (the Fool→Hermit diamond).
10. The cool slate / green-grey / plum palette, the wheat the single warm gold.

---

## Design note (specific to this card)
Sibling to the Fool (0) - both hide the Sun over the genitals and carry the Kether-diamond;
where the Fool is boundless outward motion, the Hermit is boundless inward silence. This is
the first strongly single-figure card in the middle run, so the danger is NOT clutter but
flatness: build the read around the lantern's light doing real work - a directional
light-source whose four rays actually travel to the egg, the pyramid, the wand and Cerberus,
so the "completed cycle" is legible and the figure has volume. Keep the Yod-stoop genuinely
bent (an old man folded over his lamp), not a standing staff-bearer. Palette from
BoT/DuQuette is cool and earthy: a slate / green-grey cowled figure, golden WHEAT, a bright
Sun-LANTERN with yellow rays, a GREEN egg, a pale sperm-wand; the `.ans` carries a cool
figure against warm wheat with a single blazing lamp.

## Render & review
Do not judge the Yod-spine, the lantern's light, placement, or palette by reading the source.
Run the chain and LOOK: `compose_09-hermit_lg.py` → `frame.py <art> "THE HERMIT" "~ yod ·
virgo ~" -w 47 -s majors -n IX` → `cardkit.py 09-hermit` → `render_png.py 09-hermit --axis`,
then OPEN the PNG and critique against the (TBD) Harris scan: does the cowled figure sit on
the axis guide, genuinely stooped in a Yod? does the Sun-lantern glow as the hero read with
its four rays reaching egg / pyramid / wand / Cerberus? does the green egg read below his
gaze, the wheat behind, the horizon and pyramid across the top? Fix the compositor and
repeat. Ship at ~80% once the render holds (2-3 passes max). Note: `09-hermit` must be added
to `cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Lantern-light dominant** - the glowing Sun-lantern and its four traveling rays as the
  hero structure, the figure a dark Yod-frame around the light.
- **B. Figure dominant** - the stooped ibis-headed prophet folded over his lamp as the hero
  read, egg / wand / Cerberus as his attributes.
- **C. Cycle dominant** - the completed cycle (lamp → sperm-wand → pyramid → egg) and the
  wheat field as the hero read, the figure the fulcrum of the circulation.
Tier: **full panel** - a subtle single-figure card whose depth depends on the lamp's
directional light reading correctly; spend the full cost to get the light and the Yod-stoop
right.

## Title band
Via `tools/frame.py -s majors -n 9`:
top plaque `[ IX ]` in the rule; bottom band `THE HERMIT` / `~ yod · virgo ~`

## The one-line brief
An ancient cowled, ibis-headed prophet bent into the letter Yod, only his hand showing,
holds aloft a diamond lantern with the Sun at its heart (four rays reaching the egg, the
pyramid, the sperm-wand and Cerberus) and gazes down into a green Orphic egg wound by an
iridescent serpent, his spermatozoon-wand lower-left, the tamed three-headed hound at his
heel, in a field of golden wheat. The light of the higher self, carried alone in silence.
