# XIX - The Sun

Definitive working reference. Synthesizes the project sources: Crowley's *Book of
Thoth*, DuQuette's *Understanding...Thoth Tarot*, and the color scan. No
esotericmeanings.com tutorial exists on file for this card, so the Upright /
Reversed readings below are synthesized from Crowley's divinatory list and the
BoT chapter rather than quoted.

## Identity

| Field | Value |
|---|---|
| Number / name | Atu XIX - The Sun. DuQuette title: "The Lord of the Fire of the World"; the Planetary Trump of the Sun. Original (Golden Dawn) design: "A Sun. Below is a wall, in front of which, in a fairy ring, two children wantonly and shamelessly embrace." |
| Esoteric figure | HERU-RA-HA, the Lord of the New Aeon, "in his manifestation to the race of men as the Sun spiritual, moral, and physical"; the Lord of Light, Life, Liberty and Love. The doubled god: Ra-Hoor-Khuit (active, hawk-headed) plus Hoor-pa-kraat (passive, silent), the twin suns danced out by the two children. Heraldically: "the Sun, charged with a rose, on a mount vert." |
| Hebrew letter | Resh ("head" / face; Hebrew R, value 200) - the countenance, the face turned to the light. |
| Astrology | SOL, the Sun itself. Not a zodiacal card: the twelve signs ring it instead, "in their normal position, Aries rising in the East." Rays are twelve, the number of HUA ("he"), the most sacred title of the Ancient Ones. |
| Tree of Life | Path 30, Hod (Splendour) to Yesod (Foundation) - the pillar of Mercury into the Moon-sphere, the daylight that follows the Moon's (Path 29) night. |
| Aeonic formula (the alchemy-slot equivalent) | The expansion of the ROSE AND CROSS into the Sun: "the Cross is now expanded into the Sun, from which, of course, it is originally derived." The four arms of a Cross limited by mundane law are gone; twelve rays pierce Nuit's body in every direction. The restriction of sin and death in their old sense is abolished; freedom brings sanity. |
| Color scale (GD/DuQuette) | Orange; Gold Yellow; Rich Amber; Amber, rayed red. |
| Painting palette | A white-and-rose ROSETTE at the disk's heart; broad GOLD-YELLOW ray-wedges alternating with narrow RED-ORANGE ones, running to every edge; a GREEN mound; a RED-ORANGE wall with yellow scallops; two ROSY naked children with AMBER butterfly wings; two small ROSE-CROSS disks at their feet; a pale LAVENDER / grey-green ground behind the rays; the zodiac ring drawn in pale grey-violet. |
| Keynote | Light, liberation, glad restored innocence; the collapse of the old order into joy. "Give forth thy light to all without doubt." Freedom that is both the cause and the result of the new access of solar energy upon the earth. |

## Element ranking (BoT p.113-114 + DuQuette Atu XIX + the painting)

Tier 1 - the card IS these:
1. **The central rayed Sun charged with a rose** - a great golden solar disk high
   on the axis, a ROSE (a tight white-and-crimson rosette) at its heart: "the
   flowering of the solar influence." The hero read; the human/rosy countenance
   of Resh. Draw the disk ~2:1 wider than tall, dithered as a lit mass, never an
   open circle.
2. **The twelve rays** - exactly TWELVE, broad straight golden wedges alternating
   with narrower waved / red-edged rays, radiating from the disk to EVERY edge of
   the card. Twelve is the number of the Zodiac and of HUA ("he" = 12); the
   fourfold limitation of mundane law has disappeared. These rays are the card's
   full-bleed structure: they must reach the border on all sides.
3. **The two winged dancing children** - naked, rosy, ruddy, eternally young,
   shameless and innocent, with AMBER butterfly wings, dancing hand in hand on
   the mound outside the wall: "the male and female ... dancing in the light, and
   yet they dwell upon the earth." The next stage to be attained by mankind. Draw
   ON TOP of the mound and the rays; mirror-offset the pair about the axis.
4. **The green mound** - the fertile earth, "its shape, so to speak, aspiring to
   the heavens"; a broad green hillock filling the lower third, its crown on the
   axis directly under the solar disk.

Tier 2 - named and emphasized:
5. **The red wall girding the top of the mound** - a low enclosure that COMPLETELY
   encircles the mound's crown (Harris paints it as a red-orange coronet with
   yellow scallops, seen in ellipse). "The aspiration of the new Aeon does not
   mean the absence of control"; the Rose-and-Cross formula still valid in
   terrestrial matters, now in close alliance with the celestial. The children
   stand OUTSIDE it.
6. **The zodiac ring around the whole picture** - the twelve signs set around the
   entire card border in their normal position, Aries rising in the East. "A kind
   of childish representation of the body of Nuith, a differentiation and
   classification, a chosen belt, one girdle of Our Lady of infinite space." In
   the scan they are pale grey-violet panels in the outer margin, Cancer at
   bottom centre.
7. **The two rose-cross disks at the children's feet** - "the most sacred signs of
   the old Aeon, the combination of the Rose and Cross from which they are arisen,
   yet which still forms their support." Two small round emblems on the green,
   one under each child.

Tier 3 - atmosphere / as space allows:
8. **The colour counterchange** - the mound is GREEN where one would expect red,
   the wall RED where one would expect green or blue: the Rose-and-Cross formula
   has completed "the fire-change into something rich and strange." Do not
   normalize this in the `.ans`.
9. **The butterfly wings and the dance gesture** - amber, veined, held wide;
   inner arms raised and joined, outer arms flung out, feet on the earth. Liberty
   in a body, not liberty from one.
10. **The bright full-bleed ground** - pale lavender and grey-green everywhere
    the rays do not reach; NO dark sky anywhere on this card. It is the exact
    inverse of Atu XVIII's midnight, and the two must not look alike.

## ASCII treatment notes (to prove in drafts)

- Strictly axial and radial: the solar disk on col 23, the mound crown on col 23,
  the two children mirror-offset left and right of it. A strong axis card; verify
  with `--axis`. Use `PM`/`PMB` about `AXIS = 23.0` for the disk, the mound, the
  wall ellipse and the ray fan; place the two children by mirror-offset, NOT by
  left edge.
- Cells are 1:2 - draw the solar disk and the wall ellipse ~2:1 WIDER than tall,
  or the sun renders as a squashed egg and the wall as a hoop standing on end.
- The rays are the hardest geometry: twelve of them from a point source in a
  1:2 cell grid. Compute them as true angles then scale x by 2, so the fan looks
  even; alternate glyph weight (dense wedge / light waved) to read the
  straight-and-waved alternation. They must reach all four borders.
- The single most important read: a great rayed sun with a rose at its heart over
  two winged children dancing on a green mound, light filling the whole frame.
- Density trap: this card is bright and open, but "bright" is not "empty." Fill
  the negative space with ray glyphs and zodiac marks rather than leaving white.
  Full-bleed still applies.
- Palette: GOLD and AMBER rays, a WHITE-and-ROSE centre, a GREEN mound, a RED
  wall, ROSY children with AMBER wings, a PALE LAVENDER ground. The `.ans` should
  be the brightest of the run and must not be confusable with the Moon's murk or
  Art's rainbow.

## Meanings

**Crowley divinatory (BoT appendix, Atu XIX):** "Glory, gain, riches, triumph,
pleasure, frankness, truth, shamelessness, arrogance, vanity, manifestation,
recovery from sickness, but sometimes sudden death."

**Title-page verse (BoT / DuQuette):** "Give forth thy light to all without doubt;
the clouds and shadows are no matter for thee. Make Speech and Silence, Energy and
Stillness, twin forms of thy play."

**Upright (synthesis; no esotericmeanings tutorial on file):** Daylight after the
Moon's night. Clarity, vitality, and glad restored innocence; a thing hidden or
distorted now simply seen. Success that is visible rather than negotiated: gain,
triumph, recovery from sickness, the good news arriving. Frankness and truth
without shame, freedom that does not need to hide; play, dance, and the
partnership of speech and silence, energy and stillness. The querent's own solar
nature, the face shown to the world, working as it should.

**Reversed / lower expression:** The same light gone hard and self-regarding:
arrogance, vanity, shamelessness as bluster; performance in place of frankness.
Optimism that skips the work, or the glare that will not admit shadow. Freedom
mistaken for the absence of control (the wall is still there for a reason). Burn-out
from spending everything at noon; the sudden reversal in the middle of triumph
("but sometimes sudden death").

**BoT texture:** "One of the simplest of the cards." Heru-ra-ha, Lord of the New
Aeon, in manifestation as the Sun spiritual, moral and physical; the Aeon's purpose
is "the complete emancipation of the human race." The rose is the flowering of the
solar influence. The zodiac rings the picture in normal position, Aries rising in
the East, a chosen belt of Nuit; freedom brings sanity. The green mound is the
fertile earth aspiring to the heavens, its crown walled to show that aspiration is
not the absence of control; outside the wall the twin children, male and female,
eternally young, shameless and innocent, dance in the light yet dwell upon the
earth, and at their feet lie the Rose and Cross of the old Aeon from which they
arose and which still supports them. The Cross expands into the Sun; its rays are
twelve (HUA), and the fourfold limitation of mundane law is gone. Mound green where
it should be red, wall red where it should be green: "the fire-change into something
rich and strange." Crowley closes on the pioneers of the new Aeon, whose task is to
work out the problems of civilization "simply and without prejudice," against
people whose prejudices "date morally from about 25,000 B.C."

**DuQuette:** "The Lord of the Fire of the World," Planetary Trump of the Sun,
Resh ("head"), Path 30 Hod to Yesod, colours Orange / Gold Yellow / Rich Amber /
Amber rayed red. In fortune-telling traditions the Sun is the card of the querent
himself, or the face he shows the world: "deep down inside, all of us are inherently
aware that we are ultimately solar beings." Thelema described in the most primitive
terms is "a modern form of Sun worship" - and "when I use the word 'Sun,' I am also
referring to myself." Just as sunlight is perpetual, consciousness is continuous;
death is an illusion every bit as much as night is an illusion, and immortality is
simply consciousness of the continuity of existence. Heru-ra-ha unites Hoor-pa-kraat
(passive, silent, infinite potential) and Ra-Hoor-Khuit (active, hawk-headed
avenger): the passive/active dynamic of Spirit, echoed in the ancient doctrine of
twin suns and in the actual physics of the star (thermonuclear outburn against
gravitational collapse). The two dancing children are the same pair as the twin
babies of the Fool and the children of the Lovers, arrived at last at their freedom.
"Every man and every woman is a star."

## Expected Harris palette (scan: reference/19-sun-card.jpg)

- Centre: a small white-and-ROSE rosette (concentric petals, crimson tips) inside
  a pale halo, high on the axis
- Rays: broad GOLD-YELLOW wedges alternating with narrow RED-ORANGE / vermilion
  rays, running to all four borders, warm gold near the disk cooling outward
- Mound: mid GREEN with darker green shading, filling the lower third
- Wall: RED-ORANGE band with YELLOW scallops, drawn as a shallow ellipse around
  the mound's crown
- Children: pale ROSY flesh, naked, inner arms raised and joined, AMBER-gold
  butterfly wings spread behind them
- At their feet: two small ROSE-CROSS disks in green and gold on the mound
- Ground: pale LAVENDER / mauve and grey-green between the rays; no dark sky
- Border: the twelve zodiac signs drawn pale grey-violet in the outer margin,
  Cancer bottom centre
- Frame: pale warm gray art deco; `XIX` plaque top, "The Sun" band

## Sources

- Crowley, *The Book of Thoth*, "XIX. The Sun" -
  `reference/Crowley - The Book of Thoth.txt` line 4316 (heraldic blazon 4319;
  Heru-ra-ha / Lord of Light, Life, Liberty and Love 4322-4325; the rose and the
  zodiac ring 4330-4335; green mound and wall 4337-4339; twin children 4340-4350;
  Rose and Cross at their feet 4351-4353; Cross expanded into the Sun, twelve rays,
  HUA 4355-4363; the wall completely encircles 4365-4368; colour counterchange
  4370-4373; the new-Aeon pioneers 4378-4392). Divinatory appendix, Atu XIX -
  line 9542 (verse 9545-9548; meanings 9551-9555)
- DuQuette, *Understanding Aleister Crowley's Thoth Tarot*, Atu XIX -
  `reference/DuQuette - ....txt` line 6137 (title 6140; planetary trump 6142;
  original GD design 6144-6146; Hebrew letter 6148; Tree of Life 6150-6151;
  colours 6153-6154; verse 6157-6161; "every man and every woman is a star" 6164;
  the querent's solar face 6167-6169; Crowley quoted 6173-6176; Thelema as Sun
  worship 6180-6196; Heru-ra-ha / Hoor-pa-kraat / Ra-Hoor-Khuit and the twin suns
  6197-6217; the two dancing children 6218-6227). Path table line 3701; glossary
  "Resh" line 12012; "Sun: Atu XIX ... See Resh" line 12104; the Universe's dancing
  partner as Heru-Ra-Ha of Atu XIX, line 6567
- esotericmeanings.com tutorial: NONE on file for this card
  (`reference/esoteric-meanings/` holds 01-14 and 17 only)
- Color scan: `reference/19-sun-card.jpg`
- Prompt: `drafts/19-sun-fable5-prompt.md`
