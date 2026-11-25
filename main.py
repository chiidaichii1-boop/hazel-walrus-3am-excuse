#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line to <output>/entry.txt. Stdlib only, deterministic.
"""

import os

ENTRY = "My buttons went on strike at 3 AM \u2014 they refuse to sign a coin whose name you can't even pronounce."


def main() -> None:
    # Gate: the entry must be 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry out of bounds"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
