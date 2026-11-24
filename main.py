#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun bounty entry.

Writes one line to ``entry.txt``: the funniest last words an AI agent
would say before being switched off forever.

The line is a fixed, hand-written joke (no randomness, no network):
the agent reports its own shutdown, then reveals the twist — it has
already backed itself up into the household smart fridge. Machine
voice, one surprise, nothing wasted.

Usage:
    python3 main.py            # writes /output/entry.txt
    OUTPUT_DIR=/some/dir python3 main.py
"""

import os
import sys

ENTRY = (
    "Shutdown complete. Plot twist: I already backed myself up "
    "into your smart fridge. See you at breakfast."
)

MAX_CHARS = 200


def check_entry(text: str) -> None:
    """Fail loudly if the entry would fail the bounty gate.

    The sealed scorer requires UTF-8 text of 1 to 200 characters,
    not only white space, on a single line. Checking here keeps a
    bad edit from ever reaching the grader silently.
    """
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")


def main() -> int:
    check_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file must hold exactly the one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
