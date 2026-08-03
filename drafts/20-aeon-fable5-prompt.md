# Fable Prompt - Atu XX, The Aeon (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved. **Anchor to the axis (col 23):** this card is strongly
axial and near-symmetric. The great transparent child stands centred with his spine on
column 23, the enthroned Ra-Hoor-Khuit ON the axis inside his chest, the flaming Shin
centred at the base, Nuit's arch symmetric about the axis over the top of the card.
Balance Nuit's coils, Hadit's wings and the three Yod-figures about `AXIS = 23.0` with
`PM`/`PMB`; verify with `--axis`. Nuit's arch is the one licensed asymmetry (the painting
is heavier on the right), so place her by mirror-offset from col 23, NOT by left edge.
The classic bug tell is a centred head over a throne that leans a few columns left.
Cells are 1:2 so draw the golden egg/mandorla, Hadit's globe and Nuit's omega ~2:1 wider
than tall. Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X`
allowed. Solid masses dithered for volume, never open outlines, lit directionally - the
golden egg glows from its centre. **Occlusion is INVERTED on this card:** the foreground
figure is TRANSPARENT, so background edges must survive through him (see Design note).
Full-bleed to the border. Keep outer frame + bottom title band. Color mapped to the
Harris painting. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one `.ans`
(256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the twofold Horus read as one column, Nuit as the
enclosing circumference and Hadit as the hidden centre, the Shin with its three Yod-figures
replacing the risen dead, the Libra scales foreshadowing the next Aeon) and clean
compositor structure. It does NOT fix placement drift or the transparency problem - for
those, use the render & review loop.

## Subject
**Atu XX - The Aeon** (old decks: The Angel / The Last Judgment; DuQuette: "The Spirit of
the Primal Fire," "Elemental Trump of Fire and of Spirit"). Hebrew letter Shin ("tooth"),
the mother letter of FIRE. No zodiac sign: element FIRE and SPIRIT. Path 31, Hod ->
Malkuth. Crowley departs completely from the traditional card in order to carry the
tradition on: the destruction of the world by Fire already happened, in 1904, when the
fiery god Horus took the airy god Osiris's place in the East. So the card is an adaptation
of the Stele of Revealing and announces the Aeon of Horus, the Crowned and Conquering
Child. "Every man and every woman is a star."

## The composition, in one sentence
Nuit the star-goddess arches in a deep-blue ecstatic omega over the whole card and down
both sides, Hadit's winged globe of fire spread low beneath her, and between them stands
their child Heru-ra-ha in two forms at once: the huge translucent Hoor-pa-kraat with his
finger to his lips, and, glowing THROUGH his chest inside a golden egg of light, the small
enthroned hawk-headed Ra-Hoor-Khuit with the phoenix wand, while a flaming Shin with three
small figures in its prongs burns across the foot of the card on a scarlet ground.

Hold two things above all: THE TRANSPARENT CHILD WITH THE ENTHRONED GOD SHOWING THROUGH HIM
(the twofold Horus, the hero read) and NUIT'S ARCH ENCLOSING EVERYTHING (the circumference
inside which the whole Aeon happens).

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Aeon without these):**

1. **Hoor-pa-kraat, the great transparent child.** A large milky TRANSLUCENT child standing
   full height, spine on column 23, feet at the very bottom edge, finger to his lips in the
   sign of SILENCE, head shaven but for the Horus lock, crowned with two Uraeus serpents.
   Drawn LAST but THINNEST: a light outline plus a sparse veil, never a solid mass.

2. **Ra-Hoor-Khuit enthroned, showing through the child's chest.** The small hawk-headed
   active god seated on his throne ON the axis at chest height, phoenix wand in his right
   hand, LEFT HAND EMPTY ("for I have crushed an Universe; & nought remains"), coming forth
   in golden light. He is INSIDE the child, not beside him. If a viewer cannot see the
   enthroned god through the standing child, the card has failed.

3. **Nuit arching over the whole card.** The star-goddess, deep blue, her body filled with
   STARS, bending in a great ecstatic OMEGA across the top and curving down both sides to
   mid-card. Wide and flattened (cells are 1:2), placed by mirror-offset from the axis. She
   is the frame of the card, not an ornament in it.

4. **The letter Shin at the foot, with the three figures.** A large flame-shaped SHIN drawn
   like a flower across the bottom of the card, its three Yod-prongs each occupied by a
   small human/embryonic figure rising to partake in the Essence of the new Aeon - the three
   risen dead of the old Last Judgment, reinterpreted. Keep all three legible.

**Makes it Thoth (5-7):**

5. **Hadit, the winged solar globe.** A globe of fire, eternal energy, WINGED to show his
   power of Going, beneath Nuit's heart and nearly camouflaged by the scene - in the
   painting a pair of gold-and-orange wings spread wide and low across the card. Hidden in
   plain sight is correct: "I am everywhere the centre, as she, the circumference, is
   nowhere found."

6. **The golden egg / mandorla of light.** Concentric bands of gold, emerald and orange
   forming an immense egg around the enthroned god, ~2:1 wider than tall, dithered as a
   glow with the brightest value at the centre, NOT an outline. The womb of the Aeon,
   burning inside the child's body.

7. **The scarlet ground.** The field behind everything is glowing orange-scarlet, the
   King-scale of Fire, right out to the border. This is a fire card, not a night card;
   do not let it drift toward the Moon's or the Star's dark sky.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The stylized SCALES / sign of Libra faint behind the Shin, foreshadowing the Aeon to
   follow ("when Hrumachis shall arise and the double-wanded one assume my throne and
   place") - Maat's balance, held very light.
9. Stars scattered through Nuit's arching body; every man and every woman is a star.
10. The two Uraeus serpents reading left and right off the child's crown, and the Horus
    sidelock falling past the ear.

---

## Design note (specific to this card)
The Aeon inverts the run's standard occlusion rule and that is the whole craft problem.
Everywhere else the foreground figure is drawn ON TOP and erases what is behind it; here
the foreground figure is a TRANSPARENT ESSENCE and must not erase anything. Build the card
back to front: scarlet ground, then Nuit's arch, then Hadit's wings, then the golden egg
and the enthroned Ra-Hoor-Khuit at full density, then the Shin and its three figures, and
only then lay Hoor-pa-kraat over the lot as a light contour plus a sparse veil (`.` `:` `'`)
that dims but never deletes. If the child reads as a solid white body, restart the pass.
The second problem is SCALE: three tiers must all survive at 47 wide - Nuit is card-sized,
the child is figure-sized, and Ra-Hoor-Khuit and the three Yod-figures are sprite-sized. If
the small figures blur, cut detail elsewhere, not from them. The third trap is palette
cooling; this is the hottest card of the run. Palette from BoT/DuQuette/the scan: a hot
ORANGE-SCARLET ground; a deep TEAL-BLUE star-filled Nuit arching over and down both sides
to bracelet-marked hands; a GOLD-YELLOW / EMERALD / ORANGE mandorla; a small GREEN-and-GOLD
enthroned Ra-Hoor-Khuit with a red-gold phoenix wand; a milky WHITE translucent child with
teal-tinted legs and a small red-pink hand at the mouth; GOLD-ORANGE Hadit wings spread low;
a golden Shin with three TAWNY-ORANGE figures at the base. The `.ans` should read hotter and
more saturated than any neighbour, the opposite pole from the Moon's indigo murk.

## Render & review
Do not judge the transparency, the symmetry, the three scale tiers, placement, or palette by
reading the source. Run the chain and LOOK: `compose_20-aeon_lg.py` -> `frame.py <art> "THE
AEON" "~ shin · fire ~" -w 47 -s majors -n XX` -> `cardkit.py 20-aeon` -> `render_png.py
20-aeon --axis`, then OPEN the PNG and critique against the Harris scan
(`reference/20-aeon-card.jpg`): does the child's spine sit on the axis guide with the throne
centred inside his chest? can you SEE the enthroned Ra-Hoor-Khuit through the child's body?
does Nuit's omega arch symmetrically over the card and down both sides? are all three
Yod-figures legible in the Shin? does the golden egg glow as a round dithered aura rather
than an outline? is the ground scarlet-hot to the border? Fix the compositor and repeat.
Ship at ~80% once the render holds (2-3 passes max). Note: `20-aeon` must be added to
`cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Transparent child dominant** - Hoor-pa-kraat filling the frame as the hero read, the
  finger-at-the-lips silence carrying the card, Nuit/Hadit/the throne/the Shin all seen
  through and around him; the whole gamble is on getting transparency to read.
- **B. Twofold god dominant** - the enthroned Ra-Hoor-Khuit in his golden egg as the bright
  centre of the composition, the standing child a veil drawn over him; the eye goes to the
  glowing throne first and only then discovers the outline of the child containing it.
- **C. Nuit-and-Hadit dominant** - the cosmic frame as the framing read: the star-filled
  omega of Nuit arching over the whole card, Hadit's winged globe spread low beneath her,
  the twin Horus small and radiant between them and the Shin burning at the foot; the card
  as an act of cosmogony rather than a portrait.
Tier: **full panel** - a three-scale, transparency-dependent, densely-symboled card whose
central craft problem (a foreground figure that must not occlude) has no precedent in the
run; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 20`:
top plaque `[ XX ]` in the rule; bottom band `THE AEON` / `~ shin · fire ~`

## The one-line brief
Nuit the star-goddess arches in a deep-blue omega over a scarlet card, Hadit's winged globe
of fire spread low beneath her, and their child stands between them in both his forms at
once: the huge translucent Hoor-pa-kraat with a finger to his lips, and the small enthroned
hawk-headed Ra-Hoor-Khuit glowing through his chest in a golden egg, phoenix wand in the
right hand and the left hand empty, while a flaming Shin with three small figures in its
prongs burns across the foot of the card. The Equinox of the Gods; final decision about the
past and a new current for the future, always the taking of a definite step.
