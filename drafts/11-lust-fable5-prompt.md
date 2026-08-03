# Fable Prompt - Atu XI, Lust (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Anchor to the axis (col 23):** this card is DYNAMIC and
diagonal, NOT a mirrored shrine - Babalon's body/spine reads on column 23, the seven-headed
Beast fills the lower center, and the flaming Grail is raised high toward her right (a slight
off-axis lift is authentic). Keep the RIDER'S SPINE on the axis and balance the ten rayed
circles and the trampled saints about `AXIS = 23.0` with `PM`/`PMB`; verify with `--axis`.
The classic bug tell is a centered head over a body/Beast that leans a few columns left.
Cells are 1:2 so draw the Grail-cup and the rayed circles ~2:1 wider than tall. Courier New;
extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses
dithered for volume, never open outlines, lit directionally - the Grail blazes. Foreground
figures drawn ON TOP; break background edges behind them. Full-bleed to the border. Keep
outer frame + bottom title band. Color mapped to the Harris painting. Sign `aw` or unsigned,
never `jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (Babalon on the seven-headed Beast, the Two-in-One
Grail, the seven distinct heads, the ten latent Sephiroth as rayed circles, the trampled
saints shaped like Shin) and clean compositor structure. It does NOT fix placement drift -
for that, use the render & review loop.

## Subject
**Atu XI - Lust** (old decks: Strength; Crowley swapped VIII↔XI so Leo follows Libra).
Hebrew letter Teth ("the serpent" - lowest, the earthly serpent / lower mind; highest, the
KUNDALINI rising through the chakras). The sign Leo (Sol RULES; the Lion, King of the
Beasts). Path 19, "The Intelligence of the Secret of all Spiritual Activities," Chesed →
Geburah - the highest ideals below the Abyss, dissected by the High Priestess. "Mitigate
Energy with Love; but let Love devour all things."

## The composition, in one sentence
Babalon the Scarlet Woman rides astride a great tawny seven-headed lion-serpent Beast, red
reins in her left hand and the flaming Holy Grail raised aloft in her right, drunk on the
ecstasy of the union of opposites, ten luminous rayed circles scattered above and below a
dawn horizon, grey bloodless saints trampled at the base - all in a flaming golden-amber
field.

Hold two things above all: BABALON RIDING THE BEAST (the woman astride the seven-headed
lion-serpent, the hero read) and the FLAMING GRAIL raised aloft (the Two-in-One elixir, the
second focus and the card's light).

---

## Ranked directives

**Non-negotiable (1-4, it isn't Lust without these):**

1. **Babalon, the Scarlet Woman, riding the Beast.** A woman astride, drunk in ecstasy, one
   hand reining the Beast, the other raising the Grail. Draw her ON TOP; her body and spine
   read on column 23 as the vertical of the card - do not let the mass drift left.

2. **The flaming Holy Grail, raised in her right hand.** A blazing CUP held ALOFT (her right
   / spiritual side), brimming with the Two-in-One elixir (Sun + Moon, male + female fluids),
   kundalini rising from it. Keep it lit and high - the card's light source.

3. **The seven-headed lion-serpent Beast.** A great tawny LION-SERPENT beneath her with
   SEVEN heads (Angel / Saint / Poet / Adulterous Woman / Man of Valour / Satyr /
   Lion-Serpent), aflame with lust - the phallic base she rides. Fill the lower/central mass;
   give the seven heads distinct silhouettes.

4. **The red reins.** In her LEFT (carnal) hand, RED reins running to the Beast: passion
   guided, not repressed; her connection to the lower nature.

**Makes it Thoth (5-7):**

5. **The ten luminous rayed circles (latent Sephiroth).** Ten glowing rayed CIRCLES
   scattered above and below the horizon ("as above, so below"), NOT in Tree order - the
   Sephiroth un-organised because a new Aeon is dawning.

6. **The dawn horizon + new-Aeon light.** A HORIZON of dawn (new life); above it the emblem
   of the new light and the ten serpent-HORNS of the Beast destroying the old order.

7. **The bloodless saints trampled below.** At the base, grey / bloodless SAINTS trampled by
   the Beast (the old purities denying the carnal nature), the group shaped like the letter
   SHIN (the Aeon). Small and low.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The 13 rays from the Lion-Serpent head (13 = Love + Unity), or rays from the Grail.
9. Her ecstatic gesture - gazing at the Beast, touching herself - kept implied, not explicit.
10. The hot golden-amber ground: greenish-yellow, reddish amber, deep-purple accents, Leo
    fire.

---

## Design note (specific to this card)
Complement to Adjustment (VIII, its number-swap partner) and to the Lovers (VI): where
Adjustment is perfect static symmetry, Lust is DYNAMIC diagonal motion - do NOT force a
mirror; build a rider-on-beast diagonal with the woman's spine pinned to the axis and the
Beast's mass sweeping the lower center. This is also the one HOT card in a cool run (VII-X
are amber/blue/green/violet), so let it blaze: the `.ans` should read golden-amber and
scarlet against the neighbors' cool. The danger is the seven heads blurring into one lump and
the figure reading as merely erotic rather than ecstatic-sacred; give each head its own
silhouette and let the raised Grail (not the body) be the compositional climax so the read is
sacrament, not pin-up. Palette from BoT/DuQuette: a flaming golden / greenish-yellow /
reddish-amber field, BABALON in scarlet and gold, a tawny seven-headed LION-SERPENT, a
white-gold blazing GRAIL, ten rayed CIRCLES, grey trampled SAINTS. The `.ans` carries a hot
field, a scarlet rider, a tawny Beast, a blazing cup, grey saints.

## Render & review
Do not judge the diagonal, the seven heads, placement, or palette by reading the source. Run
the chain and LOOK: `compose_11-lust_lg.py` → `frame.py <art> "LUST" "~ teth · leo ~" -w 47
-s majors -n XI` → `cardkit.py 11-lust` → `render_png.py 11-lust --axis`, then OPEN the PNG
and critique against the (TBD) Harris scan: does Babalon's spine sit on the axis guide with
the Beast sweeping the lower center? does the flaming Grail read as the raised climax and
light source? do the Beast's seven heads separate into distinct silhouettes? do the ten rayed
circles scatter above and below the horizon, the grey saints trampled low? is the field hot
(amber/scarlet) against the cool neighbors? Fix the compositor and repeat. Ship at ~80% once
the render holds (2-3 passes max). Note: `11-lust` must be added to `cardkit.CONFIGS` before
render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Rider dominant** - Babalon astride, ecstatic, as the hero figure; the Grail and Beast
  her attributes.
- **B. Grail dominant** - the flaming Two-in-One cup raised aloft as the hero read (the
  sacrament of the Aeon), the woman and Beast the offering that bears it.
- **C. Beast dominant** - the great seven-headed lion-serpent as the hero read (the tamed,
  blazing animal nature), the rider its guiding will, the Grail its crown.
Tier: **full panel** - a dynamic, many-headed, contested-hero card that must read
ecstatic-sacred not merely erotic; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 11`:
top plaque `[ XI ]` in the rule; bottom band `LUST` / `~ teth · leo ~`

## The one-line brief
Babalon the Scarlet Woman rides astride a tawny seven-headed lion-serpent Beast, red reins in
her left hand and the flaming Holy Grail raised aloft in her right, drunk on the ecstasy of
union, ten luminous rayed circles above and below a dawn horizon, grey bloodless saints
trampled at the base, in a flaming golden-amber field. Courage, une grande passion, the sacred
integration of the animal and the divine - love devouring all things.
