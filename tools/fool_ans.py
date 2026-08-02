#!/usr/bin/env python3
"""Emit terminal versions of the Fool: drafts/00-fool-lg-{16,256}.ans."""
import os
from fool_html import load

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")

PALETTES = {
    "16": {
        "frame": "\033[90m", "title": "\033[37m", "bg": "\033[33m",
        "sky": "\033[94m", "ring0": "\033[97m", "ring1": "\033[95m",
        "ring2": "\033[96m", "fool": "\033[32m", "gold": "\033[93m",
        "sun": "\033[93m", "flower": "\033[97m", "dove": "\033[97m",
        "fly": "\033[33m", "tiger": "\033[91m", "croc": "\033[32m",
        "grapes": "\033[34m", "coins": "\033[96m", "sig": "\033[90m",
    },
    "256": {
        "frame": "\033[38;5;61m", "title": "\033[38;5;250m",
        "bg": "\033[38;5;178m", "sky": "\033[38;5;68m",
        "ring0": "\033[38;5;253m", "ring1": "\033[38;5;182m",
        "ring2": "\033[38;5;115m", "fool": "\033[38;5;71m",
        "gold": "\033[38;5;220m", "sun": "\033[38;5;214m",
        "flower": "\033[38;5;195m", "dove": "\033[38;5;255m",
        "fly": "\033[38;5;172m", "tiger": "\033[38;5;208m",
        "croc": "\033[38;5;101m", "grapes": "\033[38;5;25m",
        "coins": "\033[38;5;152m", "sig": "\033[38;5;58m",
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
        path = os.path.join(DRAFTS, f"00-fool-lg-{name}.ans")
        with open(path, "w") as f:
            f.write("\n".join(out) + "\n")
        print(f"wrote 00-fool-lg-{name}.ans")
