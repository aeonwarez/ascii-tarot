# Fable Prompt — Atu 0, The Fool (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. Cells are 1:2 so draw circles/curves ~2:1 wider than
tall. Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X`
allowed. Solid masses dithered for volume, never open outlines, lit directionally.
Foreground figure drawn ON TOP; break background edges behind it. Full-bleed to the
border. Keep outer frame + bottom title band. Color mapped to the Harris painting.
Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Subject
**Atu 0 — The Fool.** Hebrew letter Aleph, element Air. The Bornless Spirit, the Zero
that contains all: Bacchus/Dionysus, the Green Man of spring, the Holy Ghost, divine
madness. Not mundane foolishness. The origin from which every other trump issues. The
most prismatic, most crowded card in the deck: a whirlwind of light and creatures.

## The composition, in one sentence
A horned, pale figure leaps at the center with arms flung wide, wrapped in a spiraling
rainbow vortex of prismatic light; a dove rises above, a tiger bites at his leg, a
crocodile waits in the water below.

Hold two things above all: the leaping central figure, and the spiral rainbow vortex.
Unlike other cards, COLOR is the hero here. The `.ans` pass carries this card. If the
color spiral works, the card works.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Fool without these):**

1. **The central figure.** Pale/whitish, young, HORNED (Bacchus/Dionysus horns),
   leaping or mid-stride, head tilted back, both arms flung wide and open. Dynamic and
   ecstatic, never static or frontal. Use diagonal strokes for the leap. He is the
   axis the whole card spins around.

2. **The prismatic rainbow vortex.** The entire field is a spiral of colored light
   coiling outward from the figure, not dead black background. Band the color: warm
   core (yellow) → blue → red → violet moving outward. This is both the composition and
   the negative-space fill. The spiral IS the card.

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
(figure + color vortex + sun + dove), add 5-7 as clear small creatures, render 8-10 as
tiny marks or drop them. Do not clutter the color spiral into mud. Empty, well-lit
spiral beats a crammed one.

## Title band
Via `tools/frame.py -s majors -n 0`:
top plaque `[ 0 ]` in the rule; bottom band `THE FOOL` / `~ aleph · air ~`

## The one-line brief
A horned figure leaps, arms wide, at the heart of a spiraling rainbow vortex; dove
above, tiger at his leg, crocodile below. The color spiral is the whole card, get that
and everything else is detail.
