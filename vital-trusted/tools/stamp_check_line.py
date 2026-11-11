#!/usr/bin/env python3
"""Build trusted-check letter lines from letter words and counts.

Lines go to trusted-check only. They are never pasted into a reply the person reads.
Every line for a check that ran is labeled "not tool-checked" because every result is
read by hand. A not-run line ("not checked, <what is missing>") carries no label.

  python stamp_check_line.py \\
    --letter 'True|sources|3 claims with no source, 1 figure to confirm|second paragraph' \\
    --letter 'Defensible|record|3 materials, 1 assumption, 2 open items (1 without an owner); Uncleared draft'

Letter spec: Letter word|aspect|counts[|note]. Letter words only (Tangible,
Rule-compliant, Unbiased, Safe, True, Ethical, Defensible). A code such as T is refused.
Counts must be counts and plain noun phrases; verdict words are refused (TR-H3).
"""
from __future__ import annotations

import argparse
import json
import re

LETTER_WORDS = ("Tangible", "Rule-compliant", "Unbiased", "Safe", "True", "Ethical", "Defensible")
LABEL = "not tool-checked"
# "pass" as a hand-on verb ("pass to your safety process") and "fine print" are not
# verdicts, so they are let through.
VERDICTS = re.compile(
    r"\b(pass(?:es|ed)?(?!\s+(?:to|on|it|this|them)\b)|fail(?:s|ed)?|compliant|approved"
    r"|validated|ready to (?:send|go)|good to go|all set|fine(?!\s+print))\b",
    re.I,
)
NOT_RUN = "not checked,"


def build_line(item: dict) -> str:
    # A check that did not run reads "not checked, <what is missing>" and carries no
    # label, because nothing was read (templates/check-line-stamp.md).
    if item["counts"].lower().startswith(NOT_RUN):
        line = f"{item['letter']} · {item['aspect']}: {item['counts']}"
    else:
        line = f"{item['letter']} · {item['aspect']}: {item['counts']} ({LABEL})"
    if item.get("note"):
        line = f"{line}\n  {item['note'].strip()}"
    return line


def parse_letter_spec(spec: str) -> dict:
    parts = [p.strip() for p in spec.split("|")]
    if len(parts) < 3 or not all(parts[:3]):
        raise SystemExit(f"Letter spec needs Letter word|aspect|counts[|note]; got {spec!r}")
    letter, aspect, counts = parts[0], parts[1], parts[2]
    note = parts[3] if len(parts) > 3 else ""
    match = next((w for w in LETTER_WORDS if w.lower() == letter.lower()), None)
    if match is None:
        raise SystemExit(
            f"Unknown letter {letter!r}; use a letter word: {', '.join(LETTER_WORDS)}"
        )
    for text in (aspect, counts, note):
        hit = VERDICTS.search(text)
        if hit:
            raise SystemExit(f"Verdict word {hit.group(0)!r} is not allowed; give counts and notes")
    return {"letter": match, "aspect": aspect, "counts": counts, "note": note}


def letter_lines(letters: list[dict]) -> dict:
    lines = [build_line(i) for i in letters]
    return {"label": LABEL, "letters": letters, "lines": lines, "text": "\n".join(lines)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--letter", action="append", default=[], metavar="WORD|aspect|counts|note")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not args.letter:
        raise SystemExit("Give at least one --letter 'Letter word|aspect|counts|note'")
    out = letter_lines([parse_letter_spec(s) for s in args.letter])
    print(json.dumps(out, indent=2, ensure_ascii=False) if args.json else out["text"])


if __name__ == "__main__":
    main()
