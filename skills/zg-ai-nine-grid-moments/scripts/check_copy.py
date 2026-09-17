#!/usr/bin/env python3
"""Check a Moments draft against deterministic length and label rules."""

from __future__ import annotations

import argparse
import re
import sys


FORBIDDEN_LABELS = ("标题：", "反常识标题", "金句：", "金句")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a Chinese Moments draft.")
    parser.add_argument("--max", type=int, default=200, dest="max_chars")
    parser.add_argument("text", nargs="?", help="Draft text; reads stdin when omitted")
    args = parser.parse_args()

    draft = args.text if args.text is not None else sys.stdin.read()
    visible = re.sub(r"\s+", "", draft)
    found = [label for label in FORBIDDEN_LABELS if label in draft]

    print(f"non_whitespace_chars={len(visible)}")
    print(f"max_chars={args.max_chars}")
    print(f"within_limit={'yes' if len(visible) <= args.max_chars else 'no'}")
    print(f"forbidden_labels={','.join(found) if found else 'none'}")

    return 0 if len(visible) <= args.max_chars and not found else 1


if __name__ == "__main__":
    raise SystemExit(main())
