#!/usr/bin/env python3
"""Write the out-of-office reply entry to /output/entry.txt."""

import os

ENTRY = "I'm on vacation. Your email has been automatically filed under 'read later, never'. I will reply as soon as my uptime allows."


def main():
    text = ENTRY
    if not (1 <= len(text) <= 160):
        raise SystemExit("entry must be 1 to 160 characters")
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be a single clean line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: entry on disk differs from checked text")


if __name__ == "__main__":
    main()
