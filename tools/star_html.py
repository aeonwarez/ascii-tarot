#!/usr/bin/env python3
"""Emit drafts/17-star-preview.html — real card image + truecolor large ASCII.

Truecolor palette is matched to the actual Harris card scan
(reference/17-star-card.jpg): deep violet star-speckled field, huge
pink/rose celestial globe, blue-white Nuith, brass gold cup raised /
pewter cup lowered, white-crystal Babalon star, mauve pyramids,
white-violet crystalline shore, amber butterflies, dark red roses.
"""
import os
from colorize_star import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "drafts", "17-star-preview.html")

TRUE = {
    "frame": "#8f8fb8",     # pale deco border, dimmed for black bg
    "title": "#c8c8d8",
    "sky": "#7a6fc0",       # violet field (chars in sky)
    "star": "#f0ecff",      # white star-speckle
    "babalon": "#e8e4f8",   # big star is white-crystal, faintly violet
    "globe": "#d9a0b8",     # the pink/rose celestial globe
    "gold": "#c9a23a",      # brass golden cup + its pour
    "nuith": "#b8c4e8",     # blue-white goddess
    "silver": "#a8d4e0",    # silver-cyan lowered cup + rigid stream —
                            # deliberately split from the gold act
    "fly": "#c09040",       # amber butterflies
    "rose": "#8f2f3f",      # dark red roses
    "crystal": "#c8c0e0",   # white-violet faceted shore
    "earth": "#b8a8c8",     # mauve ground
    "pyramid": "#c090a8",   # pink-mauve pyramids
    "water": "#8fa8c8",     # pale lavender sea
    "sig": "#55558a",
}


def esc(ch):
    return ch.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def html_card(lines, grid, pal):
    out = []
    for line, cls in zip(lines, grid):
        row, cur, buf = [], None, []
        for c, ch in enumerate(line):
            k = cls[c] if ch != " " else cur
            if k != cur and buf:
                row.append(f'<span style="color:{pal[cur]}">{"".join(buf)}</span>'
                           if cur else "".join(buf))
                buf = []
            cur = k if ch != " " else cur
            buf.append(esc(ch))
        if buf:
            row.append(f'<span style="color:{pal[cur]}">{"".join(buf)}</span>'
                       if cur else "".join(buf))
        out.append("".join(row))
    return "\n".join(out)


if __name__ == "__main__":
    lines, grid = load("large")
    card = html_card(lines, grid, TRUE)
    with open(OUT, "w") as f:
        f.write(f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>XVII . The Star — truecolor</title>
<style>
  body {{ background: #000; margin: 2rem; display: flex; flex-direction: row;
         justify-content: center; align-items: flex-start; gap: 3rem;
         flex-wrap: wrap; }}
  figure {{ margin: 0; }}
  img {{ max-height: 44rem; border-radius: 8px; }}
  pre {{ font-family: "Courier New", Courier, monospace; font-weight: bold;
        font-size: 15px; line-height: 1.2; }}
  figcaption {{ color: #666; font-family: monospace; text-align: center;
               margin-top: .8rem; }}
</style></head><body>
<figure><img src="../reference/17-star-card.jpg" alt="Thoth XVII The Star (Harris)">
<figcaption>Harris original (reference)</figcaption></figure>
<figure><pre>{card}</pre>
<figcaption>&#x5D4; · ascii-tarot truecolor (after jgs)</figcaption></figure>
</body></html>
""")
    print(f"wrote {os.path.normpath(OUT)}")
