# Fable Prompt - Atu XVIII, The Moon (Thoth)

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47×32, framed 51×39, aspect 0.64, exact
leading whitespace preserved. **Center on the axis (col 23):** the whole scene is
bilaterally symmetric, so mirror everything (towers, mountains, path, Anubis, moon)
about `AXIS = 23.0` with the `PM`/`PMB` helpers and verify with `--axis`. Cells are 1:2
so draw circles/curves ~2:1 wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` +
line-glyphs `o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never
open outlines, lit directionally. Foreground drawn ON TOP; break background edges behind
it. Full-bleed to the border. Frame + two-line band via `tools/frame.py -s majors`.
Color mapped to the Harris painting. Sign `aw` or unsigned, never `jgs`. Output one
`.txt` + one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the marginal
quality shows in the esoteric synthesis and clean compositor structure. It does NOT fix
placement drift or flatness - for those, use the render & review loop.

## Subject
**Atu XVIII - The Moon.** Hebrew letter Qoph ("back of the head"), element/sign Pisces
(water). The card is MIDNIGHT: the Gateway of Resurrection, the Dark Night of the Soul,
illusion, poisoned darkness that is the condition of the rebirth of light. The sun
carried through the underworld. Corruption before dawn.

## The composition, in one sentence
Two black towers crown two barren mountains flanking a central path; a blood-tinged
stream flows down from the gap between them, nine Yod-shaped drops fall from a dark
waning moon above, twin Anubis guard the way, and at the very bottom under the water a
scarab bears the sun disk through the night.

Hold two things: strict bilateral symmetry down the vertical axis, and depth, the path
receding up-center to the gap on the horizon. This is the most architectural, most
symmetrical card in the deck. Mirror it. Use converging perspective lines for the road.

---

## Ranked directives

**Non-negotiable (1-4, it isn't the Moon without these):**

1. **Bilateral symmetry, two towers.** Two barren mountains, each crowned with a black
   tower of nameless dread, flanking a central gap. The whole card mirrors left/right
   down the vertical axis. Symmetry is the structure.

2. **The receding central path.** A blood-tinged stream/road flows down the center from
   the gap between the mountains toward the viewer. Narrow it toward the horizon
   (converging lines) so it reads as depth, not a flat stripe. This recession is what
   keeps the symmetry from becoming wallpaper.

3. **The dark waning moon + nine drops.** A pale, sinister, waning moon at top center.
   Exactly NINE Yod-shaped drops of blood falling from it down toward the path. Nine,
   Crowley is specific.

4. **The scarab bearing the sun.** At the very bottom, under the water, Khephra the
   sacred beetle holds the solar disk in his mandibles. Small, but it is the single
   warm gold point in a black card, the promise of the sun's return. The emotional
   heart. Never omit.

**Makes it Thoth (5-7):**

5. **Twin Anubis** flanking the path, jackal-headed guardians on the threshold, in
   double form between the Ways.

6. **The jackals** waiting at Anubis's feet, on watch.

7. **The water/pool** at the base (blood-tinged serum) that the scarab crosses beneath.

**Garnish (8-10, atmosphere or drop if crowded):**

8. Jagged barren mountain texture.
9. A sinister, starless sky glow (this is the abyss of night, keep it empty above).
10. Keep the drop count to exactly nine (do not let it drift to a generic scatter).

---

## Design note (specific to this card)
Opposite problem from the last two. The Star needed a stage (too empty); the Fool was
too crowded. The Moon is naturally ASCII-friendly, strict mirror symmetry plus
perspective recession, both of which text does well (verticals, converging lines).
The risk is FLATNESS: a symmetric pattern with no depth reads as wallpaper. The
receding central path (directive 2) is the cure. And it is the darkest card in the
deck: the `.ans` should be indigo/black dominant, pale sickly moon, blood-red drops,
and ONE warm gold point (the scarab-sun) at the bottom. That single warm mark alone in
the dark IS the meaning, the sun borne through night. Do not add other warmth.

## Render & review
Do not judge symmetry, depth, or palette by reading the source. Run the chain and LOOK:
`compose_18-moon_lg.py` → `frame.py` → `cardkit.py 18-moon` → `render_png.py 18-moon
--axis`, then OPEN the PNG and critique against the Harris scan: is the scene truly
mirrored on the axis guide? does the central path RECEDE (converging lines) rather than
sit flat? exactly nine drops? is the whole card indigo/black dominant with the single
warm scarab-sun the only warmth at the very bottom? Fix the compositor and repeat. Ship
at ~80% once the render holds (2-3 passes max). See FABLE_TEMPLATE.md "Render & review
loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three composer agents
in parallel (each running the Render & review loop above to a finished candidate), three
judges scoring each against the Harris scan + axis guide, then synthesis / polish /
integration merging the strongest read. Three strategies to seed the composers:
- **A. Architectural-symmetry dominant** - towers, mountains and path framed as a strict
  mirror.
- **B. Path-recession dominant** - depth first; the receding central road is the hero
  read, converging to the gap.
- **C. Atmosphere dominant** - the dark field, the nine drops and the single warm
  scarab-sun as the emotional focus.
Tier: **middle path** - naturally ASCII-friendly (mirror symmetry + perspective); run one
composer + the render loop + one adversarial critique, escalate only if it reads flat.

## Title band
Two centered lines via `tools/frame.py -s majors`:
`XVIII . THE MOON` / `~ qoph · pisces ~`

## The one-line brief
Two towers, a road receding into the dark between them, nine blood-drops from a waning
moon, and one warm scarab-sun at the very bottom carrying the light through midnight.
Symmetry and depth are the card; the single gold point is the soul of it.
