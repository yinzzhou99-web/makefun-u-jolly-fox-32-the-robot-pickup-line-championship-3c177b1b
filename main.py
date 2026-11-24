#!/usr/bin/env python3
"""The Robot Pickup Line Championship.

One pickup line, at most 200 characters, from a robot: down to its last
one percent of battery, spending it buffering a smile. Writes it to
/output/entry.txt using only the standard library, and never removes the
output directory.
"""

from pathlib import Path
import os

LINE = "I am down to my last one percent of battery, and I am spending it buffering a smile for you before I shut down."


def check(line: str) -> None:
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if line != line.strip() or not line.strip():
        raise ValueError("line must not be blank or padded with spaces")
    if not line.endswith("."):
        raise ValueError("line must end with a full stop")
    if line.count(".") != 1:
        raise ValueError("line must be a single sentence")
    if "battery" not in line or "buffering" not in line:
        raise ValueError("line must grow out of being a machine")


def main() -> None:
    check(LINE)
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)  # the scorer reads as another user, never leave 0600/0660
    print(f"wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
