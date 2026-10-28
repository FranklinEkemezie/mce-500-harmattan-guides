#!/usr/bin/env python3
"""Validate the study guides in guides/.

Checks structure, not factual accuracy:
  - required headings
  - Study and Exam lines before the first checkbox in every topic
  - three-column summary table
  - character budget and checkbox count
  - tabs, trailing whitespace, Unicode maths inside formulas

Usage:  python scripts/check_guides.py
Exit code 0 = all guides pass, 1 = at least one error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = sorted((ROOT / "guides").glob("mce-*.md"))

REQUIRED = [
    "## Overview",
    "## Synopsis",
    "## Sources",
    "## Course Content Summary",
    "## Course Content Details",
    "## How to use",
]

MIN_CHARS, MAX_CHARS = 8_000, 20_000
COMFORT_MIN, COMFORT_MAX = 10_000, 17_000
UNICODE_MATH = "√ωπζθφ²³¹⁄Σ∫ΔΩλσ¨˙"


def columns(row: str) -> int:
    return len([cell for cell in row.strip().strip("|").split("|")])


def check(path: Path) -> tuple[list[str], list[str], int, int]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []
    warnings: list[str] = []

    if not text.startswith("# "):
        errors.append("does not start with a level-1 heading")

    for heading in REQUIRED:
        if heading not in text:
            errors.append(f"missing heading: {heading}")

    for tail in ("**Refresh before starting", "**Priority:**"):
        if tail not in text:
            errors.append(f"missing closing line: {tail}")

    # Topics: Study and Exam must appear before the first checkbox.
    topic = None
    seen_study = seen_exam = False
    topics = 0
    boxes = 0
    for number, line in enumerate(lines, 1):
        if line.startswith("### "):
            if topic is not None and not (seen_study and seen_exam):
                errors.append(f"topic '{topic}' is missing a Study or Exam line")
            topic = line[4:].strip()
            topics += 1
            seen_study = seen_exam = False
            continue
        if topic is None:
            continue
        if line.startswith("**Study:**"):
            seen_study = True
        elif line.startswith("**Exam:**"):
            seen_exam = True
        elif line.startswith("- [ ]"):
            boxes += 1
            if not seen_study:
                errors.append(f"line {number}: checkbox before Study in '{topic}'")
            if not seen_exam:
                errors.append(f"line {number}: checkbox before Exam in '{topic}'")

    if topic is not None and not (seen_study and seen_exam):
        errors.append(f"topic '{topic}' is missing a Study or Exam line")

    # Summary table: three columns.
    start = text.find("## Course Content Summary")
    end = text.find("## Course Content Details")
    if start != -1 and end != -1:
        rows = [line for line in text[start:end].splitlines() if line.strip().startswith("|")]
        if len(rows) < 3:
            errors.append("summary table is missing or empty")
        for row in rows:
            if columns(row) != 3:
                errors.append(f"summary table row has {columns(row)} columns: {row[:60]}")
                break

    size = len(text)
    if not MIN_CHARS <= size <= MAX_CHARS:
        errors.append(f"length {size:,} outside {MIN_CHARS:,}-{MAX_CHARS:,}")
    elif not COMFORT_MIN <= size <= COMFORT_MAX:
        warnings.append(f"length {size:,} outside the comfortable {COMFORT_MIN:,}-{COMFORT_MAX:,}")

    if boxes == 0:
        errors.append("no checkboxes")

    for number, line in enumerate(lines, 1):
        if "\t" in line:
            errors.append(f"line {number}: tab character")
        if line != line.rstrip():
            warnings.append(f"line {number}: trailing whitespace")
        if "$" in line:
            bad = sorted({ch for ch in line if ch in UNICODE_MATH})
            if bad:
                errors.append(f"line {number}: Unicode maths inside a formula: {' '.join(bad)}")

    for number, line in enumerate(lines, 1):
        for url in re.findall(r"\]\((http://[^)]+)\)", line):
            warnings.append(f"line {number}: non-https link {url}")

    return errors, warnings, size, boxes


def main() -> int:
    if not GUIDES:
        print("No guides found in guides/. Run from the repository root.")
        return 1

    failed = False
    print(f"{'Guide':44} {'Chars':>7} {'Boxes':>6} {'Status':>8}")
    print("-" * 70)
    for path in GUIDES:
        errors, warnings, size, boxes = check(path)
        status = "FAIL" if errors else ("warn" if warnings else "ok")
        print(f"{path.name:44} {size:7,} {boxes:6} {status:>8}")
        for message in errors:
            failed = True
            print(f"  error: {message}")
        for message in warnings:
            print(f"  warning: {message}")

    print("-" * 70)
    print(f"{len(GUIDES)} guides checked. {'FAILED' if failed else 'All structural checks passed.'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
