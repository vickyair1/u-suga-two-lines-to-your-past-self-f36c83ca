#!/usr/bin/env python3
"""Two Lines to Your Past Self: a warning to your past self about one
specific moment, and one sentence on why that moment mattered.

Writes exactly two lines to /output/entry.txt.
"""

import os

# FINAL v3: tighten line 2's landing -- the sentence doesn't just
# hand the years back, it buys them back: the marriage was the price,
# the decade was what it purchased. "Bought" makes the cause and
# effect a transaction the judge can feel.

LINE_1 = "On the drive home from your sister's wedding, when she asks if you're happy, don't say 'of course' \u2014 say 'I don't know'."
LINE_2 = "That one honest sentence ended the marriage within a month, and it bought you back the next ten years of your life."

ENTRY = LINE_1 + "\n" + LINE_2


def main() -> None:
    # Gate guard: the sealed scorer needs 1-280 chars, UTF-8, not only
    # whitespace, exactly two lines. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
    assert ENTRY.strip() == ENTRY and ENTRY.strip() != "", "entry must be clean text"
    assert ENTRY.count("\n") == 1, "entry must be exactly two lines"
    assert all(line.strip() for line in ENTRY.split("\n")), "neither line may be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
