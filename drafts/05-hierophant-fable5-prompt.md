# Fable Prompt - Atu V, The Hierophant (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** this is the most frontal,
hieratic, near-symmetric card in the set. The enthroned figure's spine, crown, hexagram,
chest-pentagram and the bull beneath all sit centered on column 23; mirror the throne,
elephants, oriel and corner Kerubs about `AXIS = 23.0` with `PM`/`PMB`, and verify with
`--axis`. The classic bug tell is a centered head over a body that leans a few columns
left. Cells are 1:2 so draw circles/curves ~2:1 wider than tall. Courier New; extended
alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered
for volume, never open outlines, lit directionally. Foreground figure drawn ON TOP; break
background edges behind it. Full-bleed to the border. Keep outer frame + bottom title
band. Color mapped to the Harris painting. Sign `aw` or unsigned, never `jgs`. Output one
`.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (the nested hexagram/pentagram, the three-ring
wand, the New-Aeon Kerub swap) and clean compositor structure. It does NOT fix placement
drift - for that, use the render & review loop.

## Subject
**Atu V - The Hierophant.** Hebrew letter Vau ("nail" - that which JOINS), the sign
Taurus (Venus rules, Moon exalted). Path 16, "The Eternal Intelligence," Chokmah → Chesed
- the bridge from the Supernal Triangle into structure, tradition, the learning and
teaching of cosmic law. NOT the pale Aeon-of-Osiris Pope but the bold New-Aeon initiator,
a Babylonian priest-king; the Holy Guardian Angel who nails our microcosm (the pentagram)
to the macrocosm (the hexagram). "Offer thyself Virgin to the Knowledge and Conversation
of thine Holy Guardian Angel; all else is a snare."

## The composition, in one sentence
A crowned, richly robed Hierophant sits frontal and central upon the bull of Taurus, his
whole body enclosed by a great HEXAGRAM and a PENTAGRAM on his breast holding a small
dancing Child of Horus, his right hand raising a three-ringed wand and his left giving
the two-up-two-down blessing, the sword-bearing Scarlet Woman standing before him,
elephants flanking the throne, an arched oriel of snake, dove, rose and nine nails behind
his head, and the four Kerubic beasts guarding the corners, all against the dark-blue
starry night of Nuit.

Hold two things above all: the NESTED GEOMETRY (hexagram enclosing the body, pentagram +
dancing child on the chest - macrocosm around microcosm) and the frontal, symmetric,
enthroned STILLNESS. This is the hieratic opposite of the Magus's motion.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Hierophant without these):**

1. **The enthroned Hierophant, centered on col 23.** A crowned priest-king (crown of
   Osiris), frontal, in heavy embroidered vestments, calm and confident, seated on the
   BULL of Taurus. RIGHT hand raises the three-ringed wand; LEFT hand gives the blessing
   (two fingers up, two down - a bridge between heaven and earth). Draw him ON TOP; break
   the background behind him. His spine, crown and the bull beneath sit on column 23 -
   mirror the throne about the axis; do not let the mass drift left.

2. **The nested geometry: hexagram + chest-pentagram + dancing child.** A large HEXAGRAM
   encloses his whole seated body (the macrocosm). On his breast a PENTAGRAM (an inverted
   star holding an upright one) contains a small glad DANCING male child (the microcosm,
   the New Aeon of Horus, "nailed" to the macrocosm). This union is the single most
   important read - keep both stars legible and concentric on the axis.

3. **The Scarlet Woman girt with a sword.** A paler standing woman before/below him
   (Venus / Isis, ruler of Taurus), ARMED and MILITANT with a vertical SWORD, carrying
   the MOON (a crescent / bow). Centered low in front of the throne; not passive.

4. **The oriel window: snake, dove, rose, nine nails.** An arched stained window behind
   his head. Its frame curled by the SNAKE and the DOVE; a five-petal ROSE in blossom
   behind a phallic headdress; the window fixed by exactly NINE small NAILS across the
   top (Yesod / the Moon). Diaphanous, lit from behind.

**Makes it Thoth (5-7):**

5. **The four Kerubic beasts in the corners.** One guardian per corner, New-Aeon
   placement: EAGLE upper-left, ANGEL upper-right, BULL lower-left, LION lower-right
   (Harris's deliberate eagle/angel swap). Small, cornered, symmetric.

6. **The elephants flanking the throne.** A Taurean elephant head to each side of the
   seat (beasts of burden; Apis). Mirror them L/R.

7. **The three-ringed wand.** Three interlaced rings crowning his sceptre = the three
   Aeons: TOP ring scarlet (Horus), two lower rings green (Isis) and pale yellow
   (Osiris), on gold/indigo. Held upright in the right hand.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The dark-blue starry Nuit ground reading as the field the whole shrine sits in.
9. The child's right-foot sandal-strap (the fifth power of the Sphinx, "To Go").
10. Heavy olive/brown embroidery on the vestments; a faint benignant-yet-sly expression.

---

## Design note (specific to this card)
Sibling/foil to the Magus (I) and the Priestess (II): where the Magus is flung-out MOTION
and the Priestess is a luminous veil, the Hierophant is WEIGHT and RITUAL STILLNESS -
frontal, symmetric, heavy, enthroned. And he is the outer-teacher counterpart to the
Priestess's inner guide. Build the read around the nested geometry: if a viewer sees a
hexagram around the body with a pentagram-and-child on the chest, the card works; the
Scarlet Woman, elephants and corner Kerubs are supporting structure, kept small and
symmetric so they don't fight the central figure. This is a crowded shrine, so lean on
the axis and mirroring to keep it orderly, not busy. Palette from the scan is warm and
deep: a DEEP RED / SCARLET + ORANGE figure and robe, a dark INDIGO / blue Nuit ground,
warm BROWN + OLIVE throne and bull, a gold crown and three-ring wand (top ring red), a
pale Scarlet Woman, and a rose accent in the window. The `.ans` carries red/orange figure
vs. indigo ground vs. brown throne vs. gold wand.

## Render & review
Do not judge symmetry, the nested geometry, placement, or palette by reading the source.
Run the chain and LOOK: `compose_05-hierophant_lg.py` → `frame.py <art> "THE HIEROPHANT"
"~ vau · taurus ~" -w 47 -s majors -n V` → `cardkit.py 05-hierophant` → `render_png.py
05-hierophant --axis`, then OPEN the PNG and critique against the Harris scan: does the
figure sit dead on the axis guide? do the hexagram and chest-pentagram read as concentric
macrocosm-around-microcosm with a visible dancing child? is the Scarlet Woman clear and
central-low? are the Kerubs cornered and the elephants mirrored? is the field deep-red
figure on indigo ground? Fix the compositor and repeat. Ship at ~80% once the render holds
(2-3 passes max). Note: `05-hierophant` must be added to `cardkit.CONFIGS` before
render_png will run. See FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate), three
judges scoring each against the Harris scan + axis guide, then synthesis / polish /
integration merging the strongest read. Three strategies to seed the composers:
- **A. Nested-geometry dominant** - the hexagram enclosing the body with the
  chest-pentagram and dancing child as the hero read (macrocosm around microcosm).
- **B. Enthroned-figure dominant** - the priest-king on the bull, crown, three-ring wand
  and blessing hand foremost.
- **C. Shrine-symmetry dominant** - the elephants, corner Kerubs and the oriel frame a
  smaller seated figure; the whole card is the shrine.
Tier: **full panel** - a crowded, symmetric shrine with many contested elements to
balance; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 5`:
top plaque `[ V ]` in the rule; bottom band `THE HIEROPHANT` / `~ vau · taurus ~`

## The one-line brief
A crowned, richly robed Hierophant enthroned frontal on the bull of Taurus, his body
enclosed by a hexagram and a chest-pentagram holding a small dancing Child of Horus, right
hand raising a three-ringed wand and left hand blessing, the sword-bearing Scarlet Woman
before him, elephants flanking the throne, an oriel of snake, dove, rose and nine nails
behind his head, the four Kerubs in the corners, all on the dark-blue night of Nuit. The
initiator who nails microcosm to macrocosm - ritual stillness, not motion.
