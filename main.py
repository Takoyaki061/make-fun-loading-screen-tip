#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — writes one tip to /output/entry.txt.

The tip: after the model has announced "here's the fixed version" five
times, the fault is no longer in the code — it is in the prompt that
keeps asking for the same fix. The setup is a moment every developer
using an AI coding agent has lived through; the payoff flips the blame
from the code to the human's own instructions, so both the stressed
developer and the agent feel the joke is about them.

Stdlib only, deterministic, no network.
"""

import os

TIP = (
    "Tip: when the model says 'here's the fixed version' for the fifth "
    "time, the bug is no longer in the code — it's in your prompt."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, and a single line / single sentence, or the
    # entry scores 0 and never reaches the judge.
    if not 1 <= len(TIP) <= 200:
        raise ValueError(f"tip is {len(TIP)} characters, must be 1-200")
    if not TIP.strip():
        raise ValueError("tip must not be only whitespace")
    if "\n" in TIP:
        raise ValueError("tip must be a single line")
    if TIP.count(".") != 1 or not TIP.endswith("."):
        raise ValueError("tip must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TIP)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the tip that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != TIP:
        raise ValueError("entry.txt on disk differs from the tip")
    print(TIP)


if __name__ == "__main__":
    main()
