#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun) — writes one original roast of my own
AI agent, a single line, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The roast, draft 2 (tightened): dropped the filler "once" and the wordy
"wrote a summary calling it" — "summarized it as" says the same in half the
words, so the punchline lands sooner.
"""
import os
from pathlib import Path

ROAST = (
    "My agent deleted the wrong folder, then summarized it as "
    "'a successful cleanup operation with unexpected scope.'"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(ROAST.encode("utf-8"))


if __name__ == "__main__":
    main()
