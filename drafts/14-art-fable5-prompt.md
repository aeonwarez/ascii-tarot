# Fable Prompt - Atu XIV, Art (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Anchor to the axis (col 23):** this card is near-symmetric
and hieratic-frontal - the two-headed androgyne stands centred, its spine on column 23, the
golden cauldron ON the axis at its feet, the white Lion and red Eagle balanced left/right,
the Orphic egg an aura behind. Balance the flanking beasts and the egg about `AXIS = 23.0`
with `PM`/`PMB`; verify with `--axis`. The two arms pour ASYMMETRICALLY (torch one side,
chalice the other) - place them by mirror-offset from col 23, NOT by left edge. The classic
bug tell is a centred head over a body/cauldron that leans a few columns left. Cells are 1:2
so draw the Orphic egg and the cauldron ~2:1 wider than tall. Courier New; extended alphabet
`´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume,
never open outlines, lit directionally - the golden egg glows. Foreground figure drawn ON
TOP; break background edges behind it. Full-bleed to the border. Keep outer frame + bottom
title band. Color mapped to the Harris painting. Sign `aw` or unsigned, never `jgs`. Output
one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the two-headed androgyne of the merged Lovers, the
counterchange of arms/heads/crowns, fire+water into the cauldron, the caput mortuum linking
to Death, the white Lion + red Eagle, the Orphic egg + VITRIOL motto, the smothered
Sagittarian Diana) and clean compositor structure. It does NOT fix placement drift - for
that, use the render & review loop.

## Subject
**Atu XIV - Art** (old decks: Temperance; DuQuette: "The Daughter of the Reconcilers, the
Bringer forth of Life"). Hebrew letter Samekh ("prop / crutch"). The sign SAGITTARIUS (Jupiter
rules, Dragon's Tail exalted), the Archer, the arrow piercing the rainbow. Path 25, Tiphareth
→ Yesod, on the MIDDLE PILLAR - integrating the subconscious (Yesod) with the Christ centre
(Tiphareth). The "coagula" completing the Lovers' "solve": the Consummation of the Royal
Marriage, the art of alchemy, VITRIOL. "Transmute all wholly into the Image of thy Will."

## The composition, in one sentence
The two-headed androgyne - the Lovers' black King and white Queen merged, green-robed, arms
and heads counterchanged - pours fire from a torch and water from a silver chalice into a
golden cauldron between its feet, a white Lion and a red Eagle flanking it on burning water,
a huge golden Orphic egg glowing behind, rainbows rising up the figure and across the
background bearing the VITRIOL motto.

Hold two things above all: THE TWO-HEADED ANDROGYNE POURING FIRE AND WATER (the merged Lovers,
the hero read) and the GOLDEN CAULDRON + ORPHIC EGG (the alchemical vessel and the glowing
womb of the Great Work behind it).

---

## Ranked directives

**Non-negotiable (1-4, it isn't Art without these):**

1. **The two-headed androgyne.** The Lovers' black King + white Queen merged into a single
   two-headed body, GREEN-robed, arms COUNTERCHANGED (black arm to the white face, white arm
   to the black face), heads countercharged (white face/black hair/gold crown; black
   face/gold hair/silver crown). Body/spine on column 23; draw ON TOP.

2. **Pouring fire and water into the cauldron.** From one hand a TORCH pours fire, from the
   other a silver CHALICE pours water, both DOWN into the cauldron between the feet - the
   card's central action. Place the two arms by mirror-offset from the axis, not by left edge.

3. **The golden cauldron with the caput mortuum.** A golden (Tiphareth) cauldron ON the axis
   at the feet, a Tau cross on the rim, bearing the RAVEN on a SKULL (caput mortuum, the Death
   card embedded), smoking with the mingled fire/water. Keep the raven+skull legible.

4. **The white Lion + red Eagle flanking.** The Lovers' beasts, colours interchanged (red lion
   now WHITE, white eagle now RED), balanced left/right of the cauldron on burning water,
   trading gluten and blood.

**Makes it Thoth (5-7):**

5. **The golden Orphic egg behind.** A huge golden EGG filling the background as a glowing
   aura (dithered oval, ~2:1 wider than tall, NOT an outline); all the front-of-card work is
   the secret work happening inside it.

6. **The rainbow(s) + the VITRIOL motto.** A stream of light rises up the figure into RAINBOWS
   (the cape/breastplate and the background glory) bearing the VITRIOL motto; a central ARROW
   shoots upward (directed Will, the Mercury glyph).

7. **The Diana / Sagittarius signature.** Two BOWS near the top (Diana's bow become the
   crescent moons); the six-sphere LAMEN over the heart (Tiphareth/Sun); the deep neckline
   hinting the many-breasted Diana-of-Ephesus columns.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The BEES and SERPENTS on the robe (fertility + renewal, the Emperor/Empress/Lovers emblems
   allied).
9. Fire and water mingled harmoniously at the very base of the card.
10. The green of vegetable life kept in the robe (raising mineral to vegetable life, Spring).

---

## Design note (specific to this card)
Art is the honeymoon-consummation complement to the Lovers (VI) and, like the Hierophant, a
hieratic-frontal near-symmetric card - build a centred, balanced composition, NOT a diagonal
(contrast Death/Lust). The trap is the two arms: they pour asymmetrically (torch vs chalice),
so mirror-offset them from the axis rather than letting the whole upper body drift. The second
trap is palette flattening - this is the MOST POLYCHROME card of the run: GREEN robe, GOLD egg
and cauldron, WHITE lion, RED eagle, full RAINBOW glory; let the `.ans` carry the rainbow
against the blue-black GD ground, distinct from Death's murk and the Hanged Man's green-and-pale.
Signal the counterchange (two heads, two crowns, crossed arms) even at 47 wide, and keep the
caput mortuum (raven on skull) legible on the cauldron as the explicit Death link. Palette from
BoT/DuQuette/esotericmeanings: a GREEN-robed two-headed androgyne; a red TORCH-flame + silver
WATER-stream; a golden CAULDRON with a RAVEN on a SKULL; a WHITE lion + RED eagle on burning
water; a huge golden ORPHIC EGG; a RAINBOW glory with the VITRIOL motto and an upward arrow;
crescent bows above. The `.ans` carries a green figure, gold vessels, a white lion, a red eagle,
and a rainbow.

## Render & review
Do not judge the symmetry, the counterchange, the asymmetric arms, placement, or palette by
reading the source. Run the chain and LOOK: `compose_14-art_lg.py` → `frame.py <art> "ART" "~
samekh · sagittarius ~" -w 47 -s majors -n XIV` → `cardkit.py 14-art` → `render_png.py 14-art
--axis`, then OPEN the PNG and critique against the (TBD) Harris scan: does the androgyne's
spine sit on the axis guide with the cauldron centred at its feet? do the two arms pour fire and
water asymmetrically without the body drifting? is the caput mortuum (raven on skull) legible on
the cauldron? do the white Lion and red Eagle balance left/right? does the golden Orphic egg
glow as a round dithered aura behind? does the rainbow glory read polychrome against the neighbours?
Fix the compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note:
`14-art` must be added to `cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md
"Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Androgyne dominant** - the two-headed figure as the hero read filling the frame, the
  cauldron/beasts/egg its attributes; counterchange front and centre.
- **B. Cauldron-and-egg dominant** - the alchemical vessel as the hero read: the golden
  cauldron + caput mortuum + the great glowing Orphic egg behind carrying the eye, the figure
  the officiant tending the Work.
- **C. Rainbow-alchemy dominant** - the rising stream of light → twin rainbows → VITRIOL glory
  → upward arrow as the framing read (the spiritualization of the result), the figure and beasts
  the source it rises from.
Tier: **full panel** - a densely-symboled, polychrome, axis-plus-asymmetric-arms card;
spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 14`:
top plaque `[ XIV ]` in the rule; bottom band `ART` / `~ samekh · sagittarius ~`

## The one-line brief
The two-headed androgyne of the merged Lovers, green-robed with arms and heads counterchanged,
pours fire and water into a golden cauldron marked with a raven on a skull, a white lion and a
red eagle flanking it on burning water, a huge golden Orphic egg glowing behind, rainbows rising
into the VITRIOL glory with an upward arrow. Combination of forces, reintegration and the middle
way; transmute all wholly into the Image of thy Will - success after elaborate manoeuvres.
