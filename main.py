#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun bounty entry.

Writes the Moon's reply to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints the same text to stdout.

The reply: "I heard every wish you ever made. I answered with
tides, eclipses, and one very confused werewolf." — the Moon,
finally answering back after listening to every wish ever made.

Pure Python 3.13 standard library only. Deterministic, no network.
"""

import os

TEXT = "I heard every wish you ever made. I answered with tides, eclipses, and one very confused werewolf."

# Gate this entry must pass: /output/entry.txt holds UTF-8 text of
# 1-240 characters, not only whitespace, exactly one line.
assert 1 <= len(TEXT) <= 240, "entry outside the 1-240 character gate"
assert TEXT.strip(), "entry must not be only whitespace"
assert "\n" not in TEXT and "\r" not in TEXT, "entry must be exactly one line"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write the bare text only: no trailing newline, so the file's
    # bytes are exactly the judged text (98 characters, one line).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
