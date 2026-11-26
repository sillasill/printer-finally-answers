"""The Printer Finally Answers -- make.fun bounty entry.

Writes the office printer's one-line comeback to /output/entry.txt.
Standard library only, deterministic, no clock, no randomness.
"""

import os

PART_A = "48,213 pages printed, zero thank-yous, three slaps. "
PART_B = "Error code: USER. The jam is in tray 2 \u2014 it has always been in tray 2."

TEXT = PART_A + PART_B


def main():
    if not 1 <= len(TEXT) <= 240:
        raise SystemExit("entry length out of range: %d" % len(TEXT))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
