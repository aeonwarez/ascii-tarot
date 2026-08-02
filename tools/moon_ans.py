#!/usr/bin/env python3
"""Emit terminal versions of the Moon: drafts/18-moon-lg-{16,256}.ans."""
import os
from moon_html import load

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")

PALETTES = {
    "16": {
        "frame": "\033[90m", "title": "\033[37m", "moon": "\033[93m",
        "blood": "\033[91m", "tower": "\033[34m", "cone": "\033[37m",
        "anubis": "\033[33m", "jackal": "\033[90m", "flame": "\033[91m",
        "water": "\033[36m", "wavered": "\033[91m", "waveblue": "\033[94m",
        "aura": "\033[93m", "sun": "\033[93m", "scarab": "\033[37m",
        "sig": "\033[90m",
    },
    "256": {
        "frame": "\033[38;5;61m", "title": "\033[38;5;250m",
        "moon": "\033[38;5;187m", "blood": "\033[38;5;131m",
        "tower": "\033[38;5;60m", "cone": "\033[38;5;146m",
        "anubis": "\033[38;5;173m", "jackal": "\033[38;5;244m",
        "flame": "\033[38;5;166m", "water": "\033[38;5;103m",
        "wavered": "\033[38;5;167m", "waveblue": "\033[38;5;68m",
        "aura": "\033[38;5;186m", "sun": "\033[38;5;214m",
        "scarab": "\033[38;5;247m", "sig": "\033[38;5;60m",
    },
}
RESET = "\033[0m"

if __name__ == "__main__":
    lines, grid = load()
    for name, pal in PALETTES.items():
        out = []
        for line, cls in zip(lines, grid):
            row, cur = [], None
            for c, ch in enumerate(line):
                if ch != " " and cls[c] != cur:
                    row.append(pal[cls[c]])
                    cur = cls[c]
                row.append(ch)
            row.append(RESET)
            out.append("".join(row))
        path = os.path.join(DRAFTS, f"18-moon-lg-{name}.ans")
        with open(path, "w") as f:
            f.write("\n".join(out) + "\n")
        print(f"wrote 18-moon-lg-{name}.ans")
