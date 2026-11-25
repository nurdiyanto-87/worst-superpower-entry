#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line to /output/entry.txt: the most useless superpower,
invented in a single line of at most 140 characters.

Pure Python standard library, deterministic, no network, no input
files. The text is fixed so both grader runs produce byte-identical
output.

Candidate lines drafted and scored against the judge brief
(deadpan comedy editor; criteria in order: genuinely useless,
uselessness lands as a visual joke, unexpected, tight/specific,
clear on one reading):

  A. "I can summon rain, but only inside my own umbrella, which is
     already open." (74)
     Useless: the rain falls on you anyway; the umbrella is defeated
     by its own owner. Visual: a hero opens an umbrella, summons a
     storm onto themself. Unexpected: fresh image, not a known gag
     (no slow flight, no unseen invisibility). Specific: umbrella,
     already open. Clear on one reading. STRONGEST — picked.
  B. "I can breathe underwater for exactly as long as I can hold my
     breath." (69)
     Genuinely useless and visual, but "a power that equals a normal
     ability" is a familiar joke structure — weaker on unexpected.
  C. "I can read minds, but only my own, and only thoughts I have
     already had." (72)
     Useless and surprising, but hard to picture in use — weaker on
     the visual-joke criterion than A.
  D. "I can instantly know the exact time on any clock I am already
     looking at." (73)
     Useless, but the joke is thin: the picture is just looking at a
     clock — weaker on the laugh criterion.
  E. "I can ring my own doorbell telekinetically, but only from
     inside my own house." (78)
     Useless and specific, but wordier and less funny than A.
  F. "I can teleport anywhere in the world, as long as it is the
     spot I am standing on." (81)
     Teleport-to-the-same-spot is a familiar gag family — weakest on
     unexpected.

Revision (v1 -> v2): A said "inside my own umbrella, which is already
open" — "underneath my own open umbrella" says the same thing in
fewer words and keeps the punch (the rain still lands on you, the
umbrella still useless). Shorter text also wins the size tie-break.
"""

import os
import sys

# Final entry line (v2, revised from v1 candidate A — see module docstring).
ENTRY = "I can summon rain, but only underneath my own open umbrella."

MAX_CHARS = 140


def validate(text: str) -> None:
    """Enforce the gate: 1-140 chars, UTF-8, not whitespace-only,
    exactly one line."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    text.encode("utf-8")  # raises if not encodable as UTF-8


def self_test() -> None:
    """A couple of self-tests: the entry validates, and the obvious
    bad inputs are rejected."""
    validate(ENTRY)
    assert 1 <= len(ENTRY) <= MAX_CHARS
    assert ENTRY == ENTRY.strip()
    for bad in ("", "   ", "x" * 141, "two\nlines"):
        try:
            validate(bad)
        except SystemExit:
            pass
        else:
            raise AssertionError("validate() accepted: %r" % bad)


def main() -> None:
    if "--self-test" in sys.argv:
        self_test()
        print("self-test ok: %d chars" % len(ENTRY))
        return
    self_test()
    validate(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
