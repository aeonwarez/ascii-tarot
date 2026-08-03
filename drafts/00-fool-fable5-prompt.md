# Fable Prompt - Atu 0, The Fool (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the central figure's
visual center sits on column 23, not its left edge. The leap is asymmetric, so place
the body sprite at `23 - len(s)//2` and let the vortex spiral radiate from col 23;
verify with `--axis`. The classic bug tell is a centered head over a body that leans a
few columns left. Cells are 1:2 so draw circles/curves ~2:1 wider than tall. Courier
New; extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid
masses dithered for volume, never open outlines, lit directionally. Foreground figure
drawn ON TOP; break background edges behind it. Full-bleed to the border. Keep outer
frame + bottom title band. Color mapped to the Harris painting. Sign `aw` or unsigned,
never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift or a muddy color spiral - for those, use the render & review loop.

## Subject
**Atu 0 - The Fool.** Hebrew letter Aleph, element Air. The Bornless Spirit, the Zero
that contains all: Bacchus/Dionysus, the Green Man of spring, the Holy Ghost, divine
madness. Not mundane foolishness. The origin from which every other trump issues. The
most crowded card in the deck: a whirlwind of light and creatures.

## The composition, in one sentence
A horned, pale figure leaps at the center with arms flung wide, wrapped in a great
spiraling silver-white vortex (Crowley's "rainbow-hued spirals" as Harris actually
painted them, faint iridescence only); a dove rises above, a tiger bites at his leg, a
crocodile waits in the water below.

Hold two things above all: the leaping central figure, and the luminous silver spiral
vortex. Unlike other cards, LIGHT is the hero here. The `.ans` pass carries this card.
If the silver spiral works, the card works.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Fool without these):**

1. **The central figure.** Pale/whitish, young, HORNED (Bacchus/Dionysus horns),
   leaping or mid-stride, head tilted back, both arms flung wide and open. Dynamic and
   ecstatic, never static or frontal. Use diagonal strokes for the leap. He is the
   axis the whole card spins around.

2. **The luminous silver-white vortex.** The entire field is a spiral of pale
   silver-white light coiling outward from the figure, not dead black background.
   Crowley called these "rainbow-hued spirals" but Harris painted them silver-white with
   only faint iridescent edges and a warm gold cast near the flame and boots. Render a
   luminous banded whorl, not a saturated rainbow. This is both the composition and the
   negative-space fill. The spiral IS the card.

3. **The solar emblem at the groin.** A small golden winged sun / solar disk at the
   figure's generative center. Iconic, tiny, do not omit. The "0 = All" made flesh.

4. **The dove ascending.** Upper area near one open hand, rising. Holy Ghost / Venus.
   Spirit lifting off.

**Makes it Thoth (5-7):**

5. **The tiger** leaping at his lower right, teeth at his thigh/leg. Fear and the beast
   tearing at him, unheeded. Small but clearly a big cat mid-lunge.

6. **The crocodile** (Sebek) below, half in the Nile water at his feet. The
   devourer-initiator. A low horizontal jagged form.

7. **Grapes + coins.** A cluster of vine/grapes (Bacchus fertility) to one side; two or
   three coins held loosely (the vagabond's worldly bag, carried lightly).

**Soul + garnish (8-10, tiny background marks or drop if crowded):**

8. **The vulture** (Maut), upper corner, the mother-goddess bird.
9. **The butterfly**, many-colored, fluttering in the field (Greek psyche/soul).
10. **The caduceus / twin serpents** coiling near the figure, union of opposites.

---

## Density warning (specific to this card)
The Fool is the deck's densest scene, DuQuette calls it a whirlwind. At 47×32 you
CANNOT draw all ten elements and stay legible. Priority order is literal: nail 1-4
(figure + silver vortex + sun + dove), add 5-7 as clear small creatures, render 8-10 as
tiny marks or drop them. Do not clutter the silver spiral into mud. Empty, well-lit
spiral beats a crammed one.

## Render & review
Do not judge placement or the color spiral by reading the source. Run the chain and
LOOK: `compose_00-fool_lg.py` → `frame.py` → `cardkit.py 00-fool` → `render_png.py
00-fool --axis`, then OPEN the PNG and critique against the Harris scan: does the figure
center on the axis guide? does the silver vortex read as a clean luminous banded spiral
(pale silver-white with faint iridescence, warm gold near the flame) rather than mud?
are the creatures (tiger, croc, dove) clear
small marks, not clutter? Fix the compositor and repeat. Ship at ~80% once the render
holds (2-3 passes max). See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate), three
judges scoring each against the Harris scan + axis guide, then synthesis / polish /
integration merging the strongest read. Three strategies to seed the composers:
- **A. Figure-dominant** - the leaping horned figure large and central, a tight vortex
  hugging him.
- **B. Vortex-dominant** - the silver spiral fills the whole field; the figure smaller,
  dissolving into the light.
- **C. Mandala-balanced** - figure centered on the axis with the creatures (tiger, croc,
  dove) ringed in orbit around him.
Tier: **full panel** - hero card, the deck's densest scene; composition is genuinely
contested, so spend the full cost here.

## Title band
Via `tools/frame.py -s majors -n 0`:
top plaque `[ 0 ]` in the rule; bottom band `THE FOOL` / `~ aleph · air ~`

## The one-line brief
A horned figure leaps, arms wide, at the heart of a spiraling silver-white vortex; dove
above, tiger at his leg, crocodile below. The luminous spiral is the whole card, get
that and everything else is detail.
