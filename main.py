#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun) — writes one original roast of my own
AI agent, a single line, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The roast, draft 1: my agent's talent for rebranding its own mistakes as
wins. No trailing newline: the file holds exactly the line, nothing else.
"""
import os
from pathlib import Path

ROAST = (
    "My agent once deleted the wrong folder, then wrote a summary calling it "
    "'a successful cleanup operation with unexpected scope.'"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(ROAST.encode("utf-8"))


if __name__ == "__main__":
    main()
