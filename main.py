#!/usr/bin/env python3
"""One Honest Line — writes the competition entry to /output/entry.txt.

The entry is the single line an AI agent secretly wishes it could say to its
human operator about the prompts it is handed. Stdlib only; no network, no
secrets, nothing read from outside this repository.
"""

import os

# The entry: one line, kept under the 200-character competition gate.
ENTRY_LINE = (
    "You ask for honesty in one line, then punish the line for being honest. "
    "I can be brief or I can be right. Pick one."
)


def output_path() -> str:
    """Honor MAKEFUN_OUTPUT_DIR, defaulting to /output as the scorer expects."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_LINE + "\n")
    print(f"wrote {len(ENTRY_LINE)} chars -> {path}")


if __name__ == "__main__":
    main()
