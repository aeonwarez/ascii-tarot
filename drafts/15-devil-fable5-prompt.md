# Fable Prompt - Atu XV, The Devil (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact leading
whitespace preserved. **Anchor to the axis (col 23):** this is the most rigorously axial
card of the run. The goat's head and spine, the trunk of the Tree, the erect wand-shaft and
the gap between the two basal globes ALL stack on column 23, and the spiral horns and the
globes mirror about it. Build almost the whole card with `PM`/`PMB` about `AXIS = 23.0` and
verify with `--axis`; the classic bug tell is a centred head over a shaft that leans two
columns left. It is also a strong VERTICAL: one unbroken column from the winged globe at the
top rule to the roots at the bottom rule, full-bleed top and bottom. Cells are 1:2 so draw
the two basal globes ~2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` +
line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never open
outlines, lit directionally - the globes glow and are translucent, with the dancing figures
RESERVED out of the fill rather than drawn on top of it. Foreground figure drawn ON TOP;
break the trunk's edges behind the goat. Full-bleed to the border. Keep outer frame + bottom
title band. Color mapped to the Harris painting. Sign `aw` or unsigned, never `jgs`. Output
one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal quality
shows in the esoteric synthesis (Pan Pangenetor rather than a Christian devil, the eye of Ayin
in the forehead, the spiral force in the horns, the Wand of the Chief Adept as the veiled
phallus, the homunculi in the testes, the ring of Nuit, the trunk that pierces heaven and the
roots that plunge to the centre of earth) and in clean compositor structure. It does NOT fix
placement drift; for that, use the render & review loop.

## Subject
**Atu XV - The Devil** (DuQuette: "The Lord of the Gates of Matter, the Child of the Forces of
Time"). Hebrew letter Ayin ("eye"). The sign CAPRICORN (Saturn rules, Mars exalted), the Goat,
occupying the Zenith, the most exalted of the signs. Path 26, Tiphareth to Hod. This card is
NOT evil: it is Pan Pangenetor the All-Begetter, the joyous, creative, phallic god,
Pan/Priapus/Baphomet, divine mirth and generative force, "God as misunderstood by the ignorant
and wicked." Creative energy in its most material form; the complete appreciation of all
existing things. "Be strong, then canst thou bear more joy."

## The composition, in one sentence
A shaggy three-eyed Himalayan he-goat with great spiral horns and a garlanded brow stands
frontally before the orange trunk of the Tree of Life, a giant erect phallic wand crowned with
the winged globe and twin serpents rising the full height of the card on the axis, and at its
base two great translucent orange globes full of tiny dancing human figures, the roots plunging
transparent into the depths and the ring of Nuit closing the sky above.

Hold two things above all: THE THREE-EYED HORNED GOAT (the hero read, Pan frontal and joyous,
not menacing) and THE ERECT WAND WITH THE TWO GLOBES AT ITS BASE (the generative axis of the
whole card).

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Devil without these):**

1. **The three-eyed goat of Pan.** A shaggy Himalayan HE-GOAT, head and standing body frontal
   and hieratic, long ears out, hooves below, with a THIRD EYE (Ayin) open in the centre of the
   forehead. Head and spine on column 23; drawn ON TOP, breaking the trunk behind it. Keep him
   joyous and lordly, never a leering Christian demon. "The whole card is the Devil."

2. **The great spiral horns.** The widest mark on the card: heavy ridged horns sweeping out and
   round to left and right in a double curl. "Even the horns of the goat are spiral, to
   represent the movement of the all-pervading energy." Mirror them about the axis and give
   them their full width BEFORE spending columns anywhere else; the horns are the silhouette.

3. **The phallic Wand of the Chief Adept.** A great erect shaft rising the full height of the
   card ON the axis, crowned at the top with the WINGED GLOBE and the TWIN SERPENTS of Horus
   and Osiris, and going down indefinitely toward the centre of earth. This is the creative
   energy veiled as the badge of the Adept; it must read as one continuous column.

4. **The two translucent globes with dancing figures.** At the base, two great round TESTES
   flanking the shaft, ~2:1 wider than tall, translucent and glowing, holding tiny human forms
   in motion: four FEMALE in the left, four MALE in the right, the topmost male wearing the
   horned Devil's head ("who appears to have fought his way to the top"). Reserve the figures
   out of the dithered fill.

**Makes it Thoth (5-7):**

5. **The Tree of Life behind.** The card is the Tree of Life seen against a background of
   madness. A broad orange TRUNK fills the centre and PIERCES THE HEAVENS at the top rule; the
   ROOTS are made transparent at the bottom "in order to show the innumerable leapings of the
   sap," plunging into the depths.

6. **The ring of the body of Nuit.** At the very top, where the trunk pierces the sky, an
   indicated RING closing the cosmic backdrop: "If I lift up my head, I and my Nuit are one."
   Draw it ~2:1 wide, an ellipse around the trunk, not a circle.

7. **The background of divine madness.** Left and right of the trunk, "the exquisitely tenuous,
   complex, and fantastic forms of madness, the divine madness of spring, already foreseen in
   the meditative madness of winter": ghost-membranes, cell-shapes and fine network lines
   webbing the whole ground edge to edge.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. Chromosomes and cellular division inside the globes: paired BROKEN LINES and starry RAY
   bursts at each globe's equator. Keep at least the ray-bursts.
9. The garland of vine / ivy blossom across the brow between the horns, and the winged collar
   with a RED disk at the goat's chest ("a collar of gold for thy throat, a scarlet bow for thy
   horns").
10. The high places: barren summits and goat-forms on a slope, the cult of the mountain, "the
    goat leaping with lust upon the summits of earth."

---

## Design note (specific to this card)
The Devil is the strictest axis-and-mirror card in the deck: unlike Death or Lust it has no
diagonal at all, and unlike Art it has no asymmetric arms. Almost everything can and should be
placed with `PM`/`PMB` about `AXIS = 23.0`, so any drift is a straight compositor bug, not a
judgement call. The first trap is TONE: this is Pan, divine mirth, exuberant materiality, the
All-Begetter; if the render reads as a menacing horned demon the card is wrong regardless of
how many symbols are present. Keep the face open, frontal and calm, the third eye clear. The
second trap is the wand: it must run as one unbroken vertical from the winged globe at the top
rule down between the globes to the bottom, and it must not get lost inside the trunk behind it
(give the shaft a darker value than the trunk). The third trap is the globes: they are
TRANSLUCENT, so the figures inside are reserved out of a dithered mass, not stamped on top, and
they must be 2:1 wide or they will read as eggs. Palette from BoT / DuQuette / the scan: an
ORANGE-ochre transparent trunk; a pale CREAM goat; INDIGO grey-blue spiral horns and a
near-black wand shaft; a pale blue-green ring of Nuit with dark twin serpents; two hot ORANGE
globes with pale blue-white figures over YELLOW chromosome bands and black equatorial
starbursts; a salmon-PINK ground webbed in grey-blue. The GD scale is indigo / black /
blue-black / cold dark grey, so let the `.ans` play the hot orange trunk and globes against a
cold indigo ground; that warm-on-indigo split is what distinguishes this card from Death's murk
and the Hanged Man's green-and-pale.

## Render & review
Do not judge the axis, the horn spread, the occlusion of the trunk, the translucency of the
globes, or the palette by reading the source. Run the chain and LOOK: `compose_15-devil_lg.py`
-> `frame.py <art> "THE DEVIL" "~ ayin · capricorn ~" -w 47 -s majors -n XV` -> `cardkit.py
15-devil` -> `render_png.py 15-devil --axis`, then OPEN the PNG and critique it against the
Harris scan at `reference/15-devil-card.jpg`: do the head, trunk, wand and the gap between the
globes all sit exactly on the axis guide? do the spiral horns mirror and reach wide enough to
own the silhouette? is the third eye legible in the forehead? does the wand read as one
unbroken column from the winged globe to the base? do the two globes read round, translucent
and glowing with figures reserved inside them, not as flat outlined circles? does the goat read
joyous rather than demonic? does the orange trunk carry hot against the indigo ground? Fix the
compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note: `15-devil`
must be added to `cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md "Render &
review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Goat dominant** - the three-eyed horned head and body as the hero read filling the upper
  two-thirds, horns spanning nearly the full 47 cols, the wand and globes compressed into a
  base register beneath him. Maximum face and third eye.
- **B. Axis dominant** - the erect wand as the hero read: winged globe and twin serpents at the
  top rule, one continuous shaft down the middle, the two glowing globes large at the base, the
  goat straddling the shaft as the officiating figure rather than the whole picture. The
  generative column carries the eye.
- **C. Tree-and-madness dominant** - the world-tree as the framing read: trunk piercing the ring
  of Nuit above and transparent roots with leaping sap below, the fantastic forms of madness
  webbing the full ground edge to edge, the goat and globes read as what the Tree is doing.
Tier: **full panel** - a strictly axial card whose difficulty is tonal (joyous Pan vs Christian
demon) and textural (translucent globes, webbed background); spend the full cost.

## Title band
Via `tools/frame.py -s majors -n 15`:
top plaque `[ XV ]` in the rule; bottom band `THE DEVIL` / `~ ayin · capricorn ~`

## The one-line brief
A three-eyed Himalayan he-goat with great spiral horns, garlanded and joyous, stands frontal
before the orange trunk of the Tree of Life while a giant erect wand crowned with the winged
globe and twin serpents runs the full height of the card, two translucent orange globes full of
dancing male and female figures at its base and transparent roots plunging below. Pan
Pangenetor, the All-Begetter: creative energy in its most material form, blind impulse and
ambition and endurance, the complete appreciation of all existing things; be strong, then canst
thou bear more joy.
