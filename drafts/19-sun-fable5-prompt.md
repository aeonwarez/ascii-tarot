# Fable Prompt - Atu XIX, The Sun (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Anchor to the axis (col 23):** this card is radial and
bilaterally symmetric - the great rayed Sun sits ON the axis high in the frame, the green
mound crowns on the axis beneath it, the walled ring is a shallow ellipse centred on the
axis, and the two winged children are mirror-offset left and right of it. Balance the disk,
the mound, the wall and the ray fan about `AXIS = 23.0` with `PM`/`PMB`; verify with
`--axis`. The two children are the only asymmetric sprites - place each at
`23 ± offset - len(s)//2`, NOT by left edge. The classic bug tell is a centred sun over a
mound that leans a few columns left. Cells are 1:2 so draw the solar disk and the wall
ellipse ~2:1 wider than tall, and compute the twelve rays as true angles with x scaled by 2.
Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs `o O v V T L 7 U c C x X` allowed.
Solid masses dithered for volume, never open outlines, lit directionally - the solar disk
glows from its rose centre. Foreground figures drawn ON TOP; break ray and mound edges
behind them. Full-bleed to the border: the rays MUST reach all four edges. Keep outer frame
+ bottom title band. Color mapped to the Harris painting. Sign `aw` or unsigned, never
`jgs`. Output one `.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis (Heru-ra-ha as the doubled sun, Resh as the
countenance, the twelve rays as HUA rather than a decorative count, the wall as control
retained inside freedom, the Rose-and-Cross disks as the old Aeon still supporting the new,
the colour counterchange) and in clean compositor structure, especially the ray fan. It does
NOT fix placement drift - for that, use the render & review loop.

## Subject
**Atu XIX - The Sun** (DuQuette: "The Lord of the Fire of the World"; the Planetary Trump of
the Sun). Hebrew letter Resh ("head" / face, the countenance turned to the light). The
planet SOL itself, ringed by the twelve zodiacal signs in their normal position with Aries
rising in the East. Path 30, Hod (Splendour) to Yesod (Foundation) - the daylight that
follows the Moon's night on Path 29. Heru-ra-ha, Lord of the New Aeon, Lord of Light, Life,
Liberty and Love, in manifestation as the Sun spiritual, moral and physical; the Cross
expanded into the Sun and freed from the fourfold limitation of mundane law. "Give forth thy
light to all without doubt."

## The composition, in one sentence
A great golden Sun charged with a rose blazes high on the axis, throwing twelve rays -
broad straight gold wedges alternating with narrow waved red ones - to every edge of the
card, while below, on a green mound girdled at its crown by a red walled ring, two naked
rosy children with amber butterfly wings dance hand in hand outside the wall, two
Rose-and-Cross disks lying on the grass at their feet, the whole picture belted by the
twelve signs of the Zodiac.

Hold two things above all: THE RAYED SUN WITH THE ROSE AT ITS HEART (the hero read, on the
axis, full-bleed radiance) and the TWO WINGED CHILDREN DANCING ON THE GREEN MOUND (the soul
read, liberated new-Aeon innocence, feet on the earth in the middle of all that light).

---

## Ranked directives

**Non-negotiable (1-4, it isn't The Sun without these):**

1. **The central rayed Sun charged with a rose.** A great golden solar disk high on the
   frame, centred on column 23, with a ROSE (a tight white-and-crimson rosette) at its
   heart: "the flowering of the solar influence," and the human countenance of Resh. Draw
   it ~2:1 wider than tall as a DITHERED lit mass with the rosette legible at its core,
   never an open circle.

2. **The twelve rays.** Exactly TWELVE, broad straight gold wedges alternating with narrower
   waved / red-edged rays, radiating from the disk to EVERY border of the card. Twelve is the
   Zodiac and the number of HUA ("he"); the four arms of a Cross limited by mundane law are
   gone. Compute them as true angles then scale x by 2 for the 1:2 cell; alternate glyph
   weight so the straight/waved alternation reads. This fan is the card's full-bleed
   structure, not decoration.

3. **The two winged dancing children.** Naked, rosy, ruddy, eternally young, shameless and
   innocent, with AMBER butterfly wings spread, dancing hand in hand on the mound OUTSIDE the
   wall: "dancing in the light, and yet they dwell upon the earth." Mirror-offset the pair
   about the axis (inner arms raised and joined, outer arms flung wide) and draw them ON TOP,
   breaking the rays and the mound edge behind them.

4. **The green mound.** The fertile earth, "its shape, so to speak, aspiring to the heavens":
   a broad GREEN hillock filling the lower third, its crown on the axis directly beneath the
   solar disk. It anchors the whole radial composition to the ground.

**Makes it Thoth (5-7):**

5. **The red wall girding the mound's crown.** A low enclosure that COMPLETELY encircles the
   top of the mound, drawn as a shallow ellipse (~2:1 wider than tall) in red-orange with
   yellow scallops. "The aspiration of the new Aeon does not mean the absence of control";
   the Rose-and-Cross formula still valid in terrestrial matters, now in close alliance with
   the celestial. The children stand OUTSIDE it, in front and below.

6. **The zodiac belt around the whole picture.** The twelve signs set around the entire card
   border in their normal position, Aries rising in the East: "a chosen belt, one girdle of
   Our Lady of infinite space," a differentiation of the body of Nuit. Tiny marks in the outer
   margin rows/columns where the rays pass; do not let them fight the rays for weight.

7. **The two Rose-and-Cross disks at the children's feet.** Two small round emblems on the
   green, one under each child: "the most sacred signs of the old Aeon, the combination of the
   Rose and Cross from which they are arisen, yet which still forms their support."

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. The colour COUNTERCHANGE: mound GREEN where one would expect red, wall RED where one would
   expect green or blue - the fire-change into "something rich and strange." Do not normalize
   it in the `.ans`.
9. The amber butterfly wings and the dance gesture: veined wings held wide, inner arms raised
   and joined, feet planted on the earth. Liberty in a body, not liberty from one.
10. The bright ground: pale lavender and grey-green wherever the rays do not reach. NO dark
    sky anywhere on this card.

---

## Design note (specific to this card)
The Sun is the exact inverse of the Moon (XVIII) and must not be confusable with it in the
`.ans`: XVIII is midnight and murk, XIX is noon with no dark sky at all. It is also the most
purely RADIAL card of the run - not a hieratic standing figure like Art or the Hierophant,
and not a diagonal like Death or Lust, but a point source with twelve arms. The first trap is
the ray fan: naive angles in a 1:2 cell grid produce a lopsided starburst, so compute true
angles and scale x by 2, and check that all twelve reach the border. The second trap is
reading "bright" as "empty" - the painting is edge to edge; fill negative space with ray
glyphs and zodiac marks rather than leaving white. The third trap is scale: Crowley calls
this "one of the simplest of the cards," which tempts a small sun floating in a frame. Make
the disk BIG and high, the mound BROAD and low, and let the children be small figures inside
a great radiance. Palette from BoT/DuQuette/the scan: a white-and-ROSE rosette at the
centre; GOLD-YELLOW ray wedges alternating with narrow RED-ORANGE rays; a GREEN mound; a
RED-ORANGE wall with yellow scallops; ROSY children with AMBER wings; green-and-gold
Rose-Cross disks; a pale LAVENDER / grey-green ground; pale grey-violet zodiac marks in the
margin. GD scale for the `.ans` ground: Orange, Gold Yellow, Rich Amber, Amber rayed red.

## Render & review
Do not judge the ray geometry, the symmetry, the disk's roundness, placement, or palette by
reading the source. Run the chain and LOOK: `compose_19-sun_lg.py` -> `frame.py <art> "THE
SUN" "~ resh · sol ~" -w 47 -s majors -n XIX` -> `cardkit.py 19-sun` -> `render_png.py
19-sun --axis`, then OPEN the PNG and critique against the Harris scan
(`reference/19-sun-card.jpg`): does the solar disk sit on the axis guide with the mound crown
directly under it? are there exactly twelve rays, evenly fanned, all reaching the border?
does the disk read as a round LIT mass with the rose legible at its core, not a squashed egg
or an outline? do the two children balance left/right without the mound drifting? is the wall
a shallow ellipse rather than an upright hoop? is the whole frame bright, with no dark sky?
Fix the compositor and repeat. Ship at ~80% once the render holds (2-3 passes max). Note:
`19-sun` must be added to `cardkit.CONFIGS` before render_png will run. See FABLE_TEMPLATE.md
"Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents in
parallel (each running the Render & review loop above to a finished candidate), three judges
scoring each against the Harris scan + axis guide, then synthesis / polish / integration
merging the strongest read. Three strategies to seed the composers:
- **A. Sun dominant** - the rayed disk and its twelve-ray fan as the hero read, filling the
  upper two thirds and blowing out to every border; the mound, wall and children a small,
  precise band of life at the bottom, dwarfed by the radiance.
- **B. Children dominant** - the two winged dancers as the hero read, large on the green
  mound and carrying the eye, the Sun a great presence above them and the rays a canopy;
  the emphasis on liberated innocence rather than on the star.
- **C. Mound-and-wall dominant** - the walled green mound as the framing read, the world
  girdled by the zodiac and crowned by the red ring, with the Sun as its answering pole
  above and the children crossing the boundary between them; the Rose-and-Cross disks
  explicit at the base.
Tier: **full panel** - a radial card whose geometry (twelve rays in a 1:2 grid) is genuinely
hard and whose brightness is easy to render as emptiness; spend the full cost.

## Title band
Via `tools/frame.py -s majors -n XIX`:
top plaque `[ XIX ]` in the rule; bottom band `THE SUN` / `~ resh · sol ~`

## The one-line brief
A great golden Sun charged with a rose throws twelve rays, straight gold alternating with
waved red, to every edge of the card; below, on a green mound ringed at its crown by a red
wall, two naked rosy children with amber butterfly wings dance hand in hand outside it, two
Rose-and-Cross disks at their feet, the twelve zodiac signs belting the whole picture. Light,
liberation and glad restored innocence; the old order collapsed into joy - glory, gain,
triumph, frankness and truth, "give forth thy light to all without doubt."
