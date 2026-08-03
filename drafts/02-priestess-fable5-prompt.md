# Fable Prompt - Atu II, The Priestess (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the figure's visual
center sits on column 23, not its left edge. This card is bilaterally symmetric, so
mirror everything about `AXIS = 23.0` with the `PM`/`PMB` helpers and verify with
`--axis`. Cells are 1:2 so draw circles/curves ~2:1 wider than tall. Courier New;
extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid
masses dithered for volume, never open outlines, lit directionally. Foreground figure
drawn ON TOP; break background edges behind it. Full-bleed to the border. Keep outer
frame + bottom title band. Color mapped to the Harris painting. Sign `aw` or unsigned,
never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift or veil flatness - for those, use the render & review loop.

## Subject
**Atu II - The Priestess.** Hebrew letter Gimel ("camel"), attribution the Moon in
her highest, purest form. Path 13 "Unifying Intelligence," the sole road down the
MIDDLE PILLAR, Kether → Tiphereth, the one path through hidden Daath, the bridge
across the Abyss. She is Isis the Eternal Virgin, Artemis/Diana: light itself, the
body of light, the truth behind the veil of light. The most SPIRITUAL trump. Truth
CONCEALED behind the dazzling veil of illusion; the HGA drawing the soul up to Kether.

## The composition, in one sentence
A serene enthroned moon-goddess sits high and frontal, crowned with the moon-phase
crown of Isis, her arms sweeping UPWARD to pull the crystalline light-web into the
crescent bowl of a Moon-cup across her lap; her latticed body dissolves down into a
stretched net of light that veils the whole field to two faint flanking pillars, and
below sit fruits, spiral shell, Plato's-solid crystals, and a small white camel dead
center.

Hold two things above all: strict bilateral symmetry down the vertical axis, and the
veil of light, a geometric web of straight rays that unifies the entire card and forms
the crescent cup at her arms. The light-web IS the card.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Priestess without these):**

1. **The veil of light.** A stretched geometric NET of fine crystalline rays filling
   the whole field, radiating from her and interlacing into a lattice of light.
   Straight thin lines (`/ \ | . '`) crossing into diamonds. Both background fill and
   hero. Vary density (tighter/brighter near her, opening toward the corners) so it
   reads as a translucent VOLUME of light, not flat wallpaper. Everything is seen
   THROUGH the veil; nothing organic sits behind it.

2. **The enthroned figure + upsweeping arms + crescent cup.** A calm seated woman high
   on the central axis, pale/luminous, gazing out. Her ARMS SWEEP UPWARD and pull the
   webbing into the crescent bowl of a Moon-colored cup that lies horizontally across
   her lap (scrolled ends). Her body reads as a checkered/diamond LATTICE (`x X` mesh);
   lower body melts down into the net (no hard hemline). Mirror her L/R. She is the
   still axis; draw her ON TOP, break the rays behind her.

3. **The Crown of Isis.** Moon-phase crown (waxing-full-waning) at her head, pale with
   a warm gold-green glow; small crescents beneath. Iconic, do not omit - it names her
   the Moon.

4. **Bilateral symmetry.** The whole card mirrors down the vertical axis - throne,
   veil, arms, the two flowers, the falling forms. Serenity comes from the symmetry;
   any asymmetry reads as noise. Keep her perfectly centered.

**Makes it Thoth (5-7):**

5. **The lyre / bow / sistrum + Moon-cup.** The horizontal scrolled instrument across
   her lap IS the crescent cup - a wide `( ... )` arc with `o`/`c` scroll ends. Willpower
   / true will and the AUM sound. One clean curve against the straight veil.

6. **The two pillars.** Mercy and Severity, faint verticals flanking her at the edges,
   spread by the veil and half-lost in the diagonal webbing. Present but subtle - do
   not let them compete with the figure.

7. **The camel + foreground garden.** A small WHITE camel DEAD CENTER at the bottom,
   between two flowers (mirroring her seat between the pillars). Around it: yellow
   10-petal SPIRAL shell/flower on the RIGHT (force/Chokmah), concave-petal flower on
   the LEFT (receptive/Binah), a purple grape cluster (Dionysus), a green pine cone
   (Bacchus), and faceted Plato's-solid crystals (`<>` `/\`) - the seeds/beginnings of
   form.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. Inverted crescent moon on the base of the throne (the subconscious).
9. Full moon disk behind her head; star-points caught in the net's intersections.
10. The hidden Book of Mysteries under the lyre (barely a mark).

---

## Design note (specific to this card)
Sibling to the Moon (XVIII): both are symmetric, but where XVIII is midnight-dark, the
Priestess is LUMINOUS. The risk is the same, flatness - the cure is DEPTH IN THE VEIL:
let the light-web vary in density so the lattice reads as a translucent volume she sits
within. She must stay clearly solid and readable ON TOP of the net (occlusion). Palette
correction from the scan: this is NOT pale silver monochrome - the field is deep BLUE +
TEAL/EMERALD GREEN with a radiant white/cyan light-web, a gold-green crown glow, a
pale-gold crescent cup, and a warm multicolor foreground (yellow spiral shell, olive
flower, purple grapes, faceted crystals, white camel). The `.ans` carries the
blue-green field vs. white rays vs. warm gold cup/foreground contrast.

## Render & review
Do not judge symmetry, veil depth, occlusion, or palette by reading the source. Run the
chain and LOOK: `compose_02-priestess_lg.py` → `frame.py` → `cardkit.py 02-priestess` →
`render_png.py 02-priestess --axis`, then OPEN the PNG and critique against the Harris
scan: does she sit dead on the axis guide? does the veil read as a translucent volume
rather than flat wallpaper? is she solid ON TOP of the net? Fix the compositor and
repeat. Ship at ~80% once the render holds (2-3 passes max). See FABLE_TEMPLATE.md
"Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate), three
judges scoring each against the Harris scan + axis guide, then synthesis / polish /
integration merging the strongest read. Three strategies to seed the composers:
- **A. Veil-dominant** - the crystalline light-web fills the whole field; the figure
  emerges from it, seen through the net.
- **B. Figure + cup dominant** - the enthroned goddess and the crescent Moon-cup are the
  hero; the veil is secondary texture.
- **C. Architecture-symmetric** - the throne and the two pillars framed strongly, the
  veil stretched between them.
Tier: **middle path** - strict bilateral symmetry makes placement low-risk; run one
composer + the render loop + one adversarial critique, and escalate to full panel only
if the light-veil won't read as a translucent volume.

## Title band
Via `tools/frame.py -s majors -n 2`:
top plaque `[ II ]` in the rule; bottom band `THE PRIESTESS` / `~ gimel · moon ~`

## The one-line brief
A moon-crowned goddess enthroned and symmetric, arms sweeping up to pull a crystalline
light-web into a crescent Moon-cup, her latticed body dissolving into rays that veil the
whole blue-green field to two faint pillars; a white camel dead center below among
spiral shell, grapes and crystal solids. Symmetry and the light-veil are the card; the
luminous web against the deep blue-green is the soul of it.
