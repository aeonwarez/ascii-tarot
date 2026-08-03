# Fable Prompt — Atu IV, The Emperor (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the enthroned figure's
visual center (spine, crown, throne midline) sits on column 23, not its left edge.
Mirror the symmetric throne/regalia about `AXIS = 23.0` with `PM`/`PMB`; for asymmetric
sprites place at `23 - len(s)//2` and verify with `--axis`. The classic bug tell is a
centered head over a body that leans a few columns left. Cells are 1:2 so draw
circles/curves ~2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` +
line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never
open outlines, lit directionally. Foreground figure drawn ON TOP; break background edges
behind it. Full-bleed to the border. Keep outer frame + bottom title band. Color mapped
to the Harris painting. Sign `aw` or unsigned, never `jgs`. Output one `.txt` + one
`.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift — for that, use the render & review loop.

## Subject
**Atu IV — The Emperor.** Hebrew letter Tzaddi ("fish hook"; Crowley's swap,
"Tzaddi is not the Star"), sign Aries (Mars rules, Sol exalted). Path 28,
Netzach → Yesod. "Sun of the Morning, chief among the Mighty" — "he who sets in
order." The alchemical principle SULPHUR: the male fiery creative energy (Rajas),
sudden and violent, the initiative of all Being. Consort of the Empress — his RED
tincture (Sun/gold) to her white (Moon/silver). Fiery sovereign authority tempered
by the lesson that to conquer you must also serve and sacrifice.

## The composition, in one sentence
A crowned Emperor in scarlet imperial regalia sits frontal and upright on a throne
whose arms end in Himalayan ram heads, his whole body forming the alchemical Sulphur
glyph — head-and-arms an upright triangle over crossed legs — a ram-headed sceptre in
his right hand catching a diagonal shaft of white light, an orb-and-Maltese-cross in
his left at the navel, the tamed white Lamb and Flag couchant at his feet and a
red-eagle shield with a crimson disk beside him, the whole card ablaze in flame red.

Hold two things above all: the SULPHUR posture (triangle of head+arms over the cross
of the legs) and the total FIERY RED authority — Mars in Aries, hard, angular, kingly.
This is the masculine fire-mirror to the Empress's cool green.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Emperor without these):**

1. **The enthroned Emperor in the Sulphur posture, centered on col 23.** A crowned
   bearded king, frontal, imperial vestments, calm authority, gazing to his left
   (toward the Empress). His BODY IS THE ALCHEMICAL SULPHUR GLYPH: head + arms make
   an upright TRIANGLE, crossed legs make the CROSS below. Keep the silhouette
   geometric and unmistakable. Draw him ON TOP; break the flames behind him. His spine
   and the throne midline sit on column 23 — the head-gaze tilts left but the MASS
   stays centered; do not let the whole figure drift left of the axis.

2. **The ram throne.** The throne's arm-capitals are the heads of the Himalayan
   wild RAM (Aries), curled horns clear. A 16-point star disk set on each throne
   arm.

3. **Dominant flame-red field + diagonal light.** Scarlet / brilliant flame red
   fills the card (Mars in Aries, Sulphur the fiery element) — angular tongues of
   fire, dithered for volume, NOT soft vegetation. A single shaft of WHITE LIGHT
   descends diagonally from the UPPER RIGHT across to the center.

4. **Sceptre + orb.** RIGHT hand: a SCEPTRE surmounted by a RAM'S head, held up
   into the light shaft. LEFT hand: an ORB topped by a MALTESE CROSS, at the navel
   (government established; creative rulership).

**Makes it Thoth (5-7):**

5. **The shield — red double-headed eagle + crimson disk.** Beside/below him, a
   heater shield bearing a two-headed golden-red EAGLE crowned with a CRIMSON
   DISK = the alchemical red tincture (Sun, gold). Its left corner brighter than
   its darker right corner.

6. **The Lamb and Flag, couchant at his feet.** A small white LAMB lying down
   holding a pennant/flag (Agnus Dei) — the tamed ram, subservient, the Aeon of
   Osiris beneath the sovereign.

7. **Four-point crown + Chesed.** A gold crown of four points (jewels of four
   facets), a Sun disk / glow behind his head (Sol exalted in Aries). The legs'
   Four echoes Chesed, the paternal Jupiter sephira.

**Soul + garnish (8-10, tiny marks or drop if crowded):**

8. Bees + fleur-de-lys worked into his robe (paternal rulership).
9. Looping lines terminating in arrowheads across the robe (directed energy).
10. A faint Aries glyph / extra ram motif; the Tzaddi "fish hook" curl echoed
    somewhere subtle.

---

## Design note (specific to this card)
Consort/sibling to the Empress (III): she was cool green vegetation, rounded and
receptive; HE is her opposite — hard scarlet flame, angular, upright, martial,
sovereign. Build the contrast deliberately: sharp diagonal fire tongues vs. her soft
leafy masses; cut-stone throne vs. her twisted grass. The Sulphur-glyph body is the
single most important read — if a viewer can trace a triangle (head+arms) sitting on a
cross (crossed legs), the card works. Keep the heraldry (red eagle shield, Lamb & Flag)
small and low so they don't fight the figure. Note the qabalistic quirk for accuracy,
not for drawing: light comes diagonally from the UPPER RIGHT (Harris's traditional
placement) even though Crowley's swap puts him on Netzach→Yesod. Palette from the scan:
dominant SCARLET / FLAME RED field, GOLD crown + sceptre + regalia, CRIMSON shield
disk, WHITE Lamb and white diagonal light shaft. The `.ans` carries red field vs. gold
regalia vs. crimson disk vs. white lamb/light.

## Render & review
Do not judge placement, mass volume, occlusion, or palette by reading the source. Run
the chain and LOOK: `compose_04-emperor_lg.py` → `frame.py` → `cardkit.py 04-emperor` →
`render_png.py 04-emperor --axis`, then OPEN the PNG and critique against the Harris
scan: does the figure sit on the axis guide (not leaning left)? can you trace the
Sulphur glyph (triangle over cross)? do the flames read as angular mass, not soft fill?
are the heraldry props small and low so they don't fight the figure? Fix the compositor
and repeat. Ship at ~80% once the render holds (2-3 passes max). See FABLE_TEMPLATE.md
"Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate), three
judges scoring each against the Harris scan + axis guide, then synthesis / polish /
integration merging the strongest read. Three strategies to seed the composers:
- **A. Sulphur-glyph silhouette dominant** — the geometric triangle-over-cross body is
  the hero, unmistakable at a glance.
- **B. Throne-architecture dominant** — the ram-headed throne and regalia framed foremost,
  the figure seated within.
- **C. Flame-field dominant** — scarlet fire fills the card and the figure reads as the
  ordered negative space within the blaze.
Tier: **middle path** — frontal and near-symmetric once centered on the axis; run one
composer + the render loop + one adversarial critique, escalate only if the Sulphur glyph
will not read.

## Title band
Via `tools/frame.py -s majors -n 4`:
top plaque `[ IV ]` in the rule; bottom band `THE EMPEROR` / `~ tzaddi · aries ~`

## The one-line brief
A scarlet-robed crowned Emperor enthroned frontal on a ram-headed throne, his body
forming the alchemical Sulphur glyph (triangle of head and arms over the cross of his
legs), ram-headed sceptre raised into a diagonal shaft of white light, orb-and-Maltese-
cross at his navel, a red double-eagle shield with a crimson disk beside him and the
tamed white Lamb and Flag at his feet, the whole card burning flame red. Sovereign fire
that must also serve.
