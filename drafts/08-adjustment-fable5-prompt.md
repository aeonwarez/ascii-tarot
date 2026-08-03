# Fable Prompt - Atu VIII, Adjustment (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** this is THE most literally
symmetric card in the set - perfect balance left/right AND top/bottom. The masked figure,
her vertical sword, and her crown-tip all sit on column 23; mirror the two scale pans (alpha
left, omega right), the throne, the corner spheres and the feathered curtain about
`AXIS = 23.0` with `PM`/`PMB`, and verify with `--axis`. The classic bug tell is a centered
head/crown over a body or sword that leans a few columns left. Cells are 1:2 so draw
circles/curves ~2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never open outlines, lit
directionally. Foreground figure drawn ON TOP; break background edges behind it. Full-bleed
to the border. Keep outer frame + bottom title band. Color mapped to the Harris painting.
Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the concealed vesica/diamond formed toe-to-pans-to-
crown, the alpha/omega balance, the plumes of Maat, the Harlequin-as-feminine-Fool reading)
and clean compositor structure. It does NOT fix placement drift - for that, use the render &
review loop.

## Subject
**Atu VIII - Adjustment** (old decks: Justice). Hebrew letter Lamed ("ox-goad" - self-
control; with Aleph the Fool, AL = 31, the key of Liber AL), the sign Libra (Venus rules,
Saturn exalted). Path 22, "The Faithful Intelligence," Geburah → Tiphareth - the Sword
peeling away all that does not serve, revealing the heart. The goddess Maat / Harlequin,
masked, poised on the point of her sword in perfect balance; Karma, *justesse*, the exact
compensation of Nature; the feminine complement of the Fool. "Balance against each thought
its exact opposite; for the Marriage of these is the Annihilation of Illusion."

## The composition, in one sentence
A slender masked woman poised on tiptoe upon the very point of her upright sword, perfectly
balanced top-to-bottom and left-to-right, gripping the phallic sword in both hands between
her thighs, crowned with the plumes of Maat from which a great balance hangs by chains -
alpha in the left pan, omega in the right - the whole figure framed inside a great diamond
/ vesica against a cool emerald ground, with balanced spheres of light and dark and a
feathered curtain of rays at the corners.

Hold two things above all: the PERFECT SYMMETRY (this card is balance made visible - mirror
everything about the axis, top and bottom too) and the GREAT DIAMOND (the vesica from toe-
point to scale-pans to crown-tip framing her).

---

## Ranked directives

**Non-negotiable (1-4, it isn't Adjustment without these):**

1. **The masked goddess poised on the sword's point, dead-center.** A young, slender woman
   on TIPTOE upon the very POINT of her upright sword, perfectly balanced. Masked
   (Harlequin), diaphanous dancing wings. Draw her ON TOP; her spine, head and crown sit on
   column 23 - she IS the axis, mirror left/right AND top/bottom.

2. **The vertical phallic sword, between her thighs.** She grips the hilt in BOTH hands, the
   blade held VERTICAL down the center between her thighs, its point what she balances on.
   The sword is the axis line itself - a clean vertical on col 23.

3. **The great balances hung from her crown.** From the point of her CROWN OF MAAT (ostrich
   plumes) the SCALES hang by chains - ALPHA disc in the LEFT pan, OMEGA disc in the RIGHT,
   in perfect equilibrium. Mirror the two pans and chains about the axis.

4. **The concealed vesica / diamond.** The lines from her TOE-POINT (bottom) to the two
   scale pans to the CROWN-TIP (top) form a great LOZENGE / VESICA around her - a clean
   mirrored diamond of diagonals, the figure centered inside it.

**Makes it Thoth (5-7):**

5. **The throne of spheres and pyramids.** Behind/below, a throne of SPHERES and PYRAMIDS
   (four = Law and Limitation), symmetric, on which the whole equity rests.

6. **The corner spheres of light and darkness.** At the corners, balanced SPHERES of light
   and dark (blue and green), mirrored - the poles she adjudicates.

7. **The feathered curtain of rays.** From those spheres, equilibrated RAYS forming a
   diaphanous FEATHERED CURTAIN behind her; the slightest act disturbs it. Keep it faint and
   symmetric.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The Harlequin chequer - mask and leggings of crossed green-and-dark diamonds.
9. The plumes of Maat crowning her (and a faint Uraeus at the brow, or drop it).
10. The cool emerald / deep blue-green Libra ground, exact and still.

---

## Design note (specific to this card)
Sibling/complement to the Fool (0): she is the feminine Fool, Aleph's ox guided by Lamed's
goad - where the Fool is boundless motion, she is boundless BALANCE. This is the single
best axis-and-mirror card in the set: the whole point is symmetry, so build it as a pure
mirror about col 23 and about the vertical middle, and let the DIAMOND/VESICA be the frame
that proves it. The read is a masked figure balanced on a sword point inside a great
diamond with a hanging scale overhead; the throne, corner spheres and curtain are the
symmetric surround. Crowley insisted the balance be DYNAMIC, not a grocer weighing sugar -
so give the figure a dancer's poise (on the point of the sword, wings alive), not a stiff
statue. Palette from BoT/DuQuette is cool and exact: an EMERALD / deep BLUE-GREEN ground, a
paler masked figure, a steel SWORD, glowing ALPHA/OMEGA discs, blue-and-green corner
spheres. The `.ans` carries a cool green field, a pale figure, a steel blade, and two
glowing scale-discs.

## Render & review
Do not judge symmetry, the vesica, placement, or palette by reading the source. Run the
chain and LOOK: `compose_08-adjustment_lg.py` → `frame.py <art> "ADJUSTMENT" "~ lamed ·
libra ~" -w 47 -s majors -n VIII` → `cardkit.py 08-adjustment` → `render_png.py 08-adjustment
--axis`, then OPEN the PNG and critique against the (TBD) Harris scan: does the figure sit
dead on the axis guide, balanced top AND bottom? is the sword a clean vertical on col 23 with
her poised on its point? do alpha (left) and omega (right) hang mirrored from the crown? does
the great diamond/vesica frame her from toe to pans to crown? Fix the compositor and repeat.
Ship at ~80% once the render holds (2-3 passes max). Note: `08-adjustment` must be added to
`cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Vesica-frame dominant** - the great diamond (toe → pans → crown) as the hero
  structure, the figure balanced inside it.
- **B. Figure dominant** - the masked dancing Harlequin poised on the sword point as the
  hero read, scales and diamond as her attributes.
- **C. Balance dominant** - the hanging scales with glowing alpha/omega and the corner
  spheres/curtain as the hero read (equilibrium made visible), the figure the fulcrum.
Tier: **full panel** - a card whose entire meaning is perfect symmetry; spend the full cost
to get the mirror and the vesica exact.

## Title band
Via `tools/frame.py -s majors -n 8`:
top plaque `[ VIII ]` in the rule; bottom band `ADJUSTMENT` / `~ lamed · libra ~`

## The one-line brief
A slender masked Harlequin poised on tiptoe on the point of her upright sword, gripping the
blade vertical between her thighs, crowned with the plumes of Maat from which a great balance
hangs - alpha left, omega right - the whole figure framed inside a great diamond/vesica
against a cool emerald ground, balanced spheres of light and dark and a feathered curtain of
rays at the corners. Balance made visible: Karma, the Woman Satisfied, the feminine Fool.
