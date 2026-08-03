# Fable Prompt - Atu VI, The Lovers (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the hooded officiant, the
blindfold Cupid above him, the winged Orphic egg below, and the overhead arch of swords
all sit on column 23; the King+lion on one side mirror the Queen+eagle on the other, so
mirror the flanking pairs about `AXIS = 23.0` with `PM`/`PMB` and verify with `--axis`.
The classic bug tell is a centered officiant over a body/scene that leans a few columns
left. Cells are 1:2 so draw circles/curves ~2:1 wider than tall. Courier New; extended
alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered
for volume, never open outlines, lit directionally. Foreground figures drawn ON TOP; break
background edges behind them. Full-bleed to the border. Keep outer frame + bottom title
band. Color mapped to the Harris painting. Sign `aw` or unsigned, never `jgs`. Output one
`.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the counterchanged King/Queen and their tinctures,
the lion/eagle Chesed-Geburah pairing, the Kether-to-egg spine, "Thelema" on Cupid's
quiver) and clean compositor structure. It does NOT fix placement drift - for that, use the
render & review loop.

## Subject
**Atu VI - The Lovers (The Brothers).** Hebrew letter Zain ("Sword" - that which DIVIDES,
the opposite of the Hierophant's nail), the sign Gemini (Mercury rules, Dragon's Head
exalted). Path 17, "The Disposing Intelligence," Binah → Tiphareth - form born out of
unity, the card of DUALITY, analysis, and CHOICE. The Hermetic Marriage of the black King
and white Queen, officiated by the hooded Hermit under an arch of swords, blindfold Cupid
above, the winged Orphic egg below. *Solve* to Art's *coagula*. "The Oracle of the Gods is
the Child-Voice of Love in thine own Soul; hear thou it."

## The composition, in one sentence
A closely hooded officiant stands frontal and central making the Sign of the Enterer over a
royal couple - a dark King with a gold crown, lance, and red lion to one side, a white
Queen with a silver crown, grail, and white eagle to the other - their free hands joined,
beneath a great arch of swords, a blindfold golden-winged Cupid aiming his arrow down the
axis above, the winged grey Orphic egg coiled by a serpent below, Lilith and Eve in the
upper corners, all in a warm orange-and-yellow field.

Hold two things above all: the DUALITY read (dark King vs. pale Queen, lion vs. eagle, the
two counterchanged twins) and the VERTICAL SACRED SPINE on the axis (Kether-light → hooded
officiant → joined hands → winged egg), with the arch of swords and blindfold Cupid framing
it.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Lovers without these):**

1. **The hooded officiant, centered on col 23.** A closely shrouded figure (the Hermit /
   Mercury) frontal at the center, arms thrust forward in the SIGN OF THE ENTERER over the
   couple, a SCROLL looped round his arms, WHITE Kether-light behind his head. Draw him ON
   TOP; his spine sits on column 23 - do not let the mass drift left.

2. **The Hermetic Marriage: dark King + white Queen, hands joined.** To one side the
   dark/black KING (gold crown = Sun, 5 points, holds the LANCE); to the other the white
   QUEEN (silver crown = Moon, holds the GRAIL with its dove + rays). Contrast them by
   value - dark vs. pale - and JOIN their inner hands across the axis below the officiant.

3. **Cupid above, blindfolded, arrow down the axis.** A small blindfolded winged Eros over
   their heads, GOLDEN wings and quiver, aiming his ARROW straight DOWN the center (Kether
   toward Chokmah; directed Will). Centered high on col 23.

4. **The winged Orphic egg below, between lion and eagle.** At the bottom center, the grey
   speckled WINGED egg coiled by a serpent (Hadit / Kether), flanked by the RED LION (left,
   with the King) and the WHITE EAGLE (right, with the Queen). The child of the union.

**Makes it Thoth (5-7):**

5. **The arch of swords overhead.** The whole scene stands beneath an ARCH of steel swords
   (Zain) - a row of blade-tips curving over the top, the gateway to the Kether light.

6. **The counterchanged twins.** Two small attendant children: the WHITE child (by the dark
   King) with white ROSES (Chesed, receptive); the BLACK child (by the white Queen) with a
   CLUB / the Lance (Geburah, phallic). Standing on the egg's wings, mirrored L/R.

7. **Lilith and Eve in the upper corners.** LILITH upper-left (dark, seductive - death);
   EVE upper-right (pale, the serpent entwined behind her head - life). Small, cornered,
   the duality of Binah.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The warm ORANGE overlap-robe on the officiant and the yellow Tiphareth field.
9. "THELEMA" implied on Cupid's golden quiver (a tiny mark, not legible letters).
10. Serpent-and-bee motifs on the King's and Queen's robes; the concealed bow at the base.

---

## Design note (specific to this card)
Sibling/foil to the Hierophant (V): where the Hierophant NAILS opposites together, the
Lovers SWORD divides them - build the whole card as a legible duality (dark/pale, lion/eagle,
club/roses) resolved on a single sacred vertical spine. This is the first multi-figure card,
so the danger is clutter: lean hard on the axis and on value-contrast so the two monarchs
read instantly as opposites, and keep Cupid, the twins, Lilith and Eve small and cornered so
they support rather than fight the center. The union - joined hands under the officiant, egg
below, Cupid above - is the read; everything else is structure. Palette from BoT/DuQuette is
warm: an ORANGE-robed officiant, a dark KING with a GOLD crown vs. a white QUEEN with a
SILVER crown, a RED LION vs. a WHITE EAGLE, a pale-blue blindfold CUPID, a grey EGG, a
steel-grey SWORD ARCH, and warm YELLOW hues in the field. The `.ans` carries dark-vs-pale
monarchs, red lion vs. white eagle, orange center vs. yellow ground.

## Render & review
Do not judge symmetry, the duality read, placement, or palette by reading the source. Run
the chain and LOOK: `compose_06-lovers_lg.py` → `frame.py <art> "THE LOVERS" "~ zain ·
gemini ~" -w 47 -s majors -n VI` → `cardkit.py 06-lovers` → `render_png.py 06-lovers
--axis`, then OPEN the PNG and critique against the (TBD) Harris scan: does the officiant
sit dead on the axis guide with the joined hands centered under him? do the King (dark) and
Queen (pale) read as opposites by value? is Cupid centered high with the arrow down the
axis, the egg centered low between a red lion and white eagle? is the sword-arch legible
overhead? Fix the compositor and repeat. Ship at ~80% once the render holds (2-3 passes
max). Note: `06-lovers` must be added to `cardkit.CONFIGS` before render_png will run. See
FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Sacred-spine dominant** - the vertical Kether-light → hooded officiant → joined hands
  → winged egg as the hero read, monarchs kept as flanking value-blocks.
- **B. Duality dominant** - the dark King + red lion vs. the white Queen + white eagle as
  the hero read (opposites resolved), the officiant a smaller uniting hinge.
- **C. Shrine-frame dominant** - the arch of swords, blindfold Cupid, and the corner
  Lilith/Eve frame a smaller central marriage; the whole card is the wedding shrine.
Tier: **full panel** - a crowded, contested multi-figure card whose duality read must stay
legible; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 6`:
top plaque `[ VI ]` in the rule; bottom band `THE LOVERS` / `~ zain · gemini ~`

## The one-line brief
A hooded officiant frontal on the axis making the Sign of the Enterer over a dark King (gold
crown, lance, red lion) and a white Queen (silver crown, grail, white eagle) with joined
hands, beneath an arch of swords, a blindfold golden Cupid aiming his arrow down the center
above, the winged grey Orphic egg coiled by a serpent below, Lilith and Eve in the upper
corners, in a warm orange-and-yellow field. Duality resolved on one sacred spine - the
sword divides, love rejoins.
