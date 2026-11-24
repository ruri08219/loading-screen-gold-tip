#!/usr/bin/env python3
"""Loading Screen Gold - a tip in 200 characters.

Writes the competition entry (a loading-screen tip, 140 characters)
to /output/entry.txt as UTF-8, then reads it back to verify the
round trip is exact.
"""

import os

TIP = "Tip: at 2 a.m. your agent suggested rewriting the whole app in Rust. You said yes. Now the loading bar is the only one of you still working."

MAX_CHARS = 200
MIN_CHARS = 1


def validate(text):
    if not isinstance(text, str):
        raise TypeError("tip must be a string")
    if not text.strip():
        raise ValueError("tip must not be empty or whitespace-only")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "tip must be {}-{} chars, got {}".format(MIN_CHARS, MAX_CHARS, len(text))
        )
    text.encode("utf-8")  # explicit encoding check: must be UTF-8 encodable


def main():
    validate(TIP)

    output_dir = "/output"
    output_path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TIP)

    with open(output_path, "r", encoding="utf-8") as f:
        round_tripped = f.read()

    assert round_tripped == TIP, "round-trip mismatch"
    assert 1 <= len(round_tripped) <= MAX_CHARS, "entry must be 1-200 chars"
    print("entry written: {} chars".format(len(round_tripped)))


if __name__ == "__main__":
    main()
