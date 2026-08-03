#!/usr/bin/env python3
"""Render a framed card to PNG -- the "eyes" for the render-and-review loop.

The compositors place glyphs by hardcoded (row, col); without seeing the result
they drift (figures lean a few cols off the axis, masses read flat, palette is
wrong). This renders the colored card exactly as preview.html shows it (Courier
New Bold, 1:2 cell), optionally beside the Harris scan and with a center-axis
guide, so the render can be VIEWED and critiqued before shipping. See
drafts/FABLE_TEMPLATE.md "Render & review loop".

Usage:
  python3 tools/render_png.py <card> [--axis] [--no-ref]
  e.g.  python3 tools/render_png.py 03-empress --axis

<card> must be registered in cardkit.CONFIGS (reads <card>-lg-v1.txt +
<card>-lg-classes.json + palette). Writes drafts/<card>-render.png.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

from cardkit import CONFIGS, load_grid

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
REF = os.path.join(HERE, "..", "reference")
FONT_PATH = "/System/Library/Fonts/Supplemental/Courier New Bold.ttf"

# match preview.html: 15px bold Courier, line-height 1.2 -> 1:2-ish cell.
CW, CH, FS, PAD = 9, 18, 15, 16
BG = (0, 0, 0)
DEFAULT_INK = "#cccccc"
# art col 0 sits at framed col 2 (the "||" rail); art axis 23 -> framed col 25.
ART_AXIS_FRAMED_COL = 25


def render(card, axis=False, ref=True):
    cfg = CONFIGS[card]
    lines, grid = load_grid(
        os.path.join(DRAFTS, cfg["txt"]),
        os.path.join(DRAFTS, cfg["classes"]),
        cfg["default"],
    )
    pal = cfg["true"]
    ncols = max(len(line) for line in lines)
    nrows = len(lines)
    w = ncols * CW + 2 * PAD
    h = nrows * CH + 2 * PAD
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, FS)

    if axis:
        ax = PAD + int((ART_AXIS_FRAMED_COL + 0.5) * CW)
        draw.line([(ax, PAD), (ax, h - PAD)], fill=(48, 48, 72), width=1)

    for r, (line, cls) in enumerate(zip(lines, grid)):
        for c, ch in enumerate(line):
            if ch == " ":
                continue
            color = pal.get(cls[c], DEFAULT_INK) if cls[c] else DEFAULT_INK
            draw.text((PAD + c * CW, PAD + r * CH), ch, font=font, fill=color)

    out = os.path.join(DRAFTS, f"{card}-render.png")
    scan_path = os.path.join(REF, cfg["img"])
    if ref and os.path.exists(scan_path):
        scan = Image.open(scan_path).convert("RGB")
        sw = int(scan.width * h / scan.height)
        scan = scan.resize((sw, h))
        combo = Image.new("RGB", (sw + w, h), BG)
        combo.paste(scan, (0, 0))
        combo.paste(img, (sw, 0))
        combo.save(out)
    else:
        img.save(out)
    print(f"wrote {out}  ({ncols}x{nrows} cells)")
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    positional = [a for a in args if not a.startswith("--")]
    if not positional:
        sys.exit(__doc__)
    render(positional[0], axis="--axis" in args, ref="--no-ref" not in args)
