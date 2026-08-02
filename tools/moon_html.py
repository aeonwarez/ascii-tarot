#!/usr/bin/env python3
"""Emit drafts/18-moon-preview.html — Harris scan + truecolor ASCII Moon.
Palette per the painting: indigo towers, pale gold moon, crimson yods,
silver-blue light cone, tan Anubis, red/blue bell-waves, and the warm
scarab-sun at the bottom of the night."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
OUT = os.path.join(DRAFTS, "18-moon-preview.html")

TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "moon": "#e8d8a0",     # pale gold orb
    "blood": "#c23a4a",    # red swirl, nine yods, mercury signs
    "tower": "#4a5288",    # indigo towers, cloak-hills, ground
    "cone": "#b8c8d8",     # the V of tainted light
    "anubis": "#d4884a",   # orange-tan guardians
    "jackal": "#7a7a8a",   # the black beasts, greyed to read on black
    "flame": "#e07840",    # the flame-point the cone lands on
    "water": "#8a98b0",    # pool ripple lines
    "wavered": "#c25a5a",  # red bell-waves
    "waveblue": "#5a78c2", # blue bell-waves
    "aura": "#e8ce7a",     # the gold ring around the scarab
    "sun": "#ffaf2a",      # the sun borne through midnight
    "scarab": "#9a9aa8",
    "sig": "#55558a",
}


def load():
    with open(os.path.join(DRAFTS, "18-moon-lg-v1.txt")) as f:
        lines = f.read().splitlines()
    with open(os.path.join(DRAFTS, "18-moon-lg-classes.json")) as f:
        art = json.load(f)
    nrows = len(lines)
    grid = []
    for r, line in enumerate(lines):
        cls = [None] * len(line)
        right = len(line) - 2
        for c, ch in enumerate(line):
            if r in (0, nrows - 1) or c <= 1 or c >= right:
                cls[c] = "frame"
            elif r >= nrows - 4:
                cls[c] = "title"
            elif 2 <= r < 2 + len(art) and 0 <= c - 2 < len(art[r - 2]):
                cls[c] = art[r - 2][c - 2] or ("cone" if ch != " " else None)
            elif ch != " ":
                cls[c] = "cone"
        grid.append(cls)
    return lines, grid


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
    lines, grid = load()
    card = html_card(lines, grid, TRUE)
    with open(OUT, "w") as f:
        f.write(f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>XVIII . The Moon — truecolor</title>
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
<figure><img src="../reference/18-moon-card.jpg" alt="Thoth XVIII The Moon (Harris)">
<figcaption>Harris original (reference)</figcaption></figure>
<figure><pre>{card}</pre>
<figcaption>&#x5E7; · ascii-tarot truecolor (after jgs)</figcaption></figure>
</body></html>
""")
    print(f"wrote {os.path.normpath(OUT)}")
