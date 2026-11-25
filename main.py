"""One Line, Big Laugh — entry runner.

Reads the single joke line from entry.txt next to this file,
writes it to /output/entry.txt, and prints it.
"""

import os
import sys

MAX_CHARS = 200


def load_line(path: str) -> str:
    """Read entry.txt and enforce the one-line rule: exactly one
    non-empty line, at most MAX_CHARS characters, no extra content."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    if len(lines) != 1:
        raise ValueError(f"entry.txt must hold exactly one line, found {len(lines)}")
    line = lines[0].strip()
    if not line:
        raise ValueError("entry line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} limit")
    if raw.strip() != line:
        raise ValueError("entry.txt holds more than the single line")
    return line


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        line = load_line(os.path.join(here, "entry.txt"))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
