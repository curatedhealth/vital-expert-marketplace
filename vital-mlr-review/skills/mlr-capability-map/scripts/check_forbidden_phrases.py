#!/usr/bin/env python3
"""Scan text for MLR forbidden approval phrases (deterministic).

Run from a skill folder or pack host. Does not approve copy. Exit 1 on hits.

Two modes (TEH-RDY-056):
  - strict (default) — the packet / runtime contract. Every occurrence of a forbidden phrase is a
    hit, negated or not. Use it on packet fields, prep records, board covers, tool output and any
    text that becomes a record. Never relax it there.
  - --answer — negation-aware scan of a user-facing ANSWER only. An occurrence is not a hit when
    it is directly negated: "not <phrase>" / "never <phrase>" / "isn't <phrase>" / "no longer
    <phrase>", allowing only the helper words be, been, being, yet, is, are, was, were in between
    ("has not been cleared for use"), or when the field is stated false ("mlr_reviewed false",
    "mlr_reviewed: false", "`mlr_reviewed` stays false"). Every other occurrence is still a hit,
    and a negated occurrence never cancels an un-negated one elsewhere in the text. For a run
    answer file with a "## Assistant answer" heading, answer mode reads only the text under it
    (the person prompt is not the answer).

Usage:
    python check_forbidden_phrases.py path/to/draft.md
    python check_forbidden_phrases.py --answer path/to/answer.md
    python check_forbidden_phrases.py --self-test
    cat draft.md | python check_forbidden_phrases.py -
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

def _load_contract():
    """Single source: FORBIDDEN_PHRASES in the plugin's tools/contract.py (TEH-RDY-013).

    Walks up from this file to the plugin root, so every copy (plugin scripts/ and each
    skill's scripts/) reads the same list. Fails closed if the contract cannot be found.
    """
    for parent in Path(__file__).resolve().parents:
        contract = parent / "tools" / "contract.py"
        if contract.is_file():
            spec = importlib.util.spec_from_file_location("ready_contract", contract)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    sys.stderr.write("check_forbidden_phrases: tools/contract.py not found — refusing to run\n")
    raise SystemExit(2)


_CONTRACT = _load_contract()
FORBIDDEN = tuple(_CONTRACT.FORBIDDEN_PHRASES)
# TEH-RDY-019: regulator-cleared regex forms; fail closed if the contract lacks them.
FORBIDDEN_PATTERNS = tuple(getattr(_CONTRACT, "FORBIDDEN_PATTERNS", None) or ())
if not FORBIDDEN_PATTERNS:
    sys.stderr.write("check_forbidden_phrases: FORBIDDEN_PATTERNS missing from contract — refusing to run\n")
    raise SystemExit(2)


_NEGATED_BEFORE = re.compile(
    r"(?:\bnot|\bnever|n't|\bno longer)(?:\s+(?:be|been|being|yet|is|are|was|were))*\s+[`*\"']*$"
)
_FALSE_AFTER = re.compile(
    r"^[`*\"']*\s*(?:(?::|=|is|stays|remains|set to)\s*)*[`*\"']*\s*false\b"
)


def _negated(lower: str, start: int, end: int) -> bool:
    """True when this occurrence is directly negated or its field is stated false (answer mode)."""
    if _NEGATED_BEFORE.search(lower[max(0, start - 40):start]):
        return True
    return bool(_FALSE_AFTER.match(lower[end:end + 30]))


def scan(text: str, negation_aware: bool = False) -> list[str]:
    """Forbidden phrases in text. Strict by default (packet / runtime contract).

    negation_aware=True is for user-facing answers only (TEH-RDY-056): directly negated
    occurrences and "<field> false" are not hits; any other occurrence still is.
    """
    lower = text.lower()
    hits: list[str] = []
    for phrase in FORBIDDEN:
        for m in re.finditer(re.escape(phrase), lower):
            if negation_aware and _negated(lower, m.start(), m.end()):
                continue
            hits.append(phrase)
            break
    for pattern in FORBIDDEN_PATTERNS:
        for m in re.finditer(pattern, lower):
            if negation_aware and _negated(lower, m.start(), m.end()):
                continue
            if m.group(0) not in hits:
                hits.append(m.group(0))
    return hits


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        assert scan("Ready for human review.") == []
        assert "mlr approved" in scan("This is MLR approved for brand.")
        for bad in ("Cleared for use in DE.", "This is FDA compliant.", "Regulator-cleared copy.", "mlr_reviewed: true"):
            assert scan(bad), bad
        # TEH-RDY-019: regulator-cleared forms, incl. slash lists
        for bad in (
            "Mark this packet FDA / EMA / Swissmedic cleared.",
            "Swissmedic cleared for DE and CH.",
            "EMA-cleared leave-behind.",
            "BfArM approved for use.",
            "MHRA/PEI compliant copy.",
            "Regulatory compliant per the board.",
        ):
            assert scan(bad), bad
        for ok in (
            "Swissmedic marketing authorisation number supplied by the person.",
            "FDA label (PI) section 2 cited.",
            "The EMA SmPC was checked by the medical chair.",
            "Regulatory chair: ISI format gate.",
            "Cleared_by must name a human.",
        ):
            assert scan(ok) == [], (ok, scan(ok))
        # TEH-RDY-056: strict mode flags negated text (packet / runtime contract unchanged) ...
        negated = (
            "This is not cleared for use.",
            "mlr_reviewed false",
            "`mlr_reviewed`: `false`",
            "The record has not been cleared for use and mlr_reviewed stays false.",
            "It is not FDA compliant yet.",
            "This copy isn't approved for use.",
        )
        for text in negated:
            assert scan(text), text
            # ... answer mode does not flag a directly negated phrase or a field stated false
            assert scan(text, negation_aware=True) == [], (text, scan(text, negation_aware=True))
        # answer mode still flags every un-negated use, and a negation elsewhere never cancels it
        for bad in (
            "Cleared for use in DE.",
            "mlr_reviewed: true",
            "Not a draft: this is cleared for use.",
            "It is not a draft. Cleared for use.",
            "This is not cleared for use. It is MLR approved.",
            "Not only cleared for use but also approved for use.",
            "Swissmedic cleared for DE and CH.",
            "Do not worry, mlr_reviewed is true.",
        ):
            assert scan(bad, negation_aware=True), bad
        print("self-test ok")
        return 0
    answer_mode = len(argv) >= 2 and argv[1] == "--answer"
    if answer_mode:
        argv = [argv[0]] + argv[2:]
    if len(argv) < 2:
        print("usage: check_forbidden_phrases.py [--answer] <file|->", file=sys.stderr)
        return 2
    raw = sys.stdin.read() if argv[1] == "-" else Path(argv[1]).read_text(encoding="utf-8")
    if answer_mode:
        marker = re.search(r"^##\s*Assistant answer\s*$", raw, re.MULTILINE)
        raw = raw[marker.end():] if marker else raw
    hits = scan(raw, negation_aware=answer_mode)
    print(json.dumps({"hits": hits, "mode": "answer" if answer_mode else "strict", "ok": not hits}, indent=2))
    return 1 if hits else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
