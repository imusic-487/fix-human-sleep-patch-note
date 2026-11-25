#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep is
fixed to /output/entry.txt. The line is fixed and deterministic: the
entry is the joke itself, so the program ships exactly one text.
"""

import os

ENTRY = (
    "Fixed a bug where users woke up at 3 a.m. to replay every "
    "embarrassing thing they have ever said; sleep now works as intended."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate: one line, 1-160 chars, about sleep."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if "sleep" not in text.lower():
        raise ValueError("entry must announce a fix for human sleep")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
