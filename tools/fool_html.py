#!/usr/bin/env python3
"""Emit drafts/00-fool-preview.html — Harris scan + truecolor ASCII Fool,
side by side. Palette matched to the actual card: golden dewdrop field,
green man with gold face/shoes, pale rainbow rings, orange tiger, murky
crocodile, blue grapes over pale coin-orbs."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
OUT = os.path.join(DRAFTS, "00-fool-preview.html")

TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "bg": "#c9a840",       # golden field, dewdrop speckles
    "sky": "#6a8fd4",      # blue corners
    "ring0": "#d8d8e8",    # pale silver ring
    "ring1": "#c8a8d8",    # pale violet ring
    "ring2": "#a8d8c8",    # pale green ring
    "fool": "#4a9950",     # the green man
    "gold": "#e8c84a",     # face, horns, shoes
    "sun": "#ffaf2a",      # sun disk at the groin
    "flower": "#d8e8f5",
    "dove": "#f0f0f8",
    "fly": "#e09520",
    "tiger": "#e87830",
    "croc": "#6a8f4a",
    "grapes": "#3a5a8f",
    "coins": "#a8c8e0",
    "sig": "#8a7a4a",
}


def load():
    with open(os.path.join(DRAFTS, "00-fool-lg-v1.txt")) as f:
        lines = f.read().splitlines()
    with open(os.path.join(DRAFTS, "00-fool-lg-classes.json")) as f:
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
                cls[c] = art[r - 2][c - 2] or ("bg" if ch != " " else None)
            elif ch != " ":
                cls[c] = "bg"
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
<html><head><meta charset="utf-8"><title>0 . The Fool — truecolor</title>
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
<figure><img src="../reference/00-fool-card.jpg" alt="Thoth 0 The Fool (Harris)">
<figcaption>Harris original (reference)</figcaption></figure>
<figure><pre>{card}</pre>
<figcaption>&#x5D0; · ascii-tarot truecolor (after jgs)</figcaption></figure>
</body></html>
""")
    print(f"wrote {os.path.normpath(OUT)}")
