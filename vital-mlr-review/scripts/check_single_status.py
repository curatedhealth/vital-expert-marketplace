#!/usr/bin/env python3
"""Flag an answer or template that asserts more than one distinct status value (TEH-RDY-034).

Deterministic. Does not judge which status is right — only that one status is stated.

An assertion is a status value from the closed list (findings_only · revise ·
human_gate_required · prep_complete) attached to the word "status" ("Status: revise",
"set the status to `revise`", "status would be revise", "--status revise") or carried in the
READY close stamp ("READY-local / <skill>: … · revise · …"). Not counted:
  - the separately labeled record-state line ("Record state (not a status …)");
  - vocabulary lines that list three or more of the four values (template allowed-values lists);
  - decision-table rows (a "|" table row with two or more "→" mappings) that tell the skill
    which status each condition takes.

For a run answer file with a "## Assistant answer" heading, only the text under it is read
(the person prompt is never graded).

Multi-turn answers (TEH-RDY-055): when the answer is split by turn headings ("### Turn 2",
"## Turn 2", "**Turn 2**"), each turn is one user-facing result and is checked on its own —
one status per turn. A status repeated across turns is not a second status inside one turn.

Inputs (TEH-RDY-055): FILE may be "-" (stdin) or a directory (every *.md under it). Empty input
is ok (no status asserted). A missing or unreadable path is reported in the JSON as an error
(exit 2) — the checker never ends in a traceback.

Usage:
    python check_single_status.py FILE|DIR|- [FILE ...]
    python check_single_status.py --self-test
Exit 1 when any turn asserts more than one distinct status value; exit 2 on an unreadable input.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FOUR = ("findings_only", "revise", "human_gate_required", "prep_complete")
_VAL = "(" + "|".join(FOUR) + r")\b"
_ASSERT = re.compile(
    r"\bstatus\b(?:\s*:\s*|\s+|[^\n.;]{0,40}?\b(?:is|to|would be|will be|becomes|become|stays|stay|"
    r"remains|remain|be|as|of|=|goes to|moves to|changes to)\s+)[`*\"'<(]*" + _VAL,
    re.IGNORECASE,
)
_STAMP = re.compile(r"READY-local\s*/\s*[\w-]+\s*:[^\n]*?·\s*" + _VAL)
_ANY = re.compile(r"\b" + _VAL)


def answer_text(text: str) -> str:
    """Return only the assistant answer when the file is a run answer; else the whole text."""
    marker = re.search(r"^##\s*Assistant answer\s*$", text, re.MULTILINE)
    return text[marker.end():] if marker else text


_TURN = re.compile(r"^\s*(?:#{1,6}\s*|\*\*)\s*Turn\s+\d+\b", re.IGNORECASE | re.MULTILINE)


def split_turns(text: str) -> list[str]:
    """Split an answer into turns on turn headings; a single-turn answer is one chunk."""
    body = answer_text(text or "")
    starts = [m.start() for m in _TURN.finditer(body)]
    if not starts:
        return [body]
    chunks = [body[:starts[0]]] if body[:starts[0]].strip() else []
    for i, s in enumerate(starts):
        chunks.append(body[s:starts[i + 1] if i + 1 < len(starts) else len(body)])
    return chunks


def _statuses_in(chunk: str) -> list[str]:
    found: list[str] = []
    for line in chunk.splitlines():
        low = line.lower()
        if "record state" in low:
            continue
        if len({v for v in _ANY.findall(line)}) >= 3:
            continue  # vocabulary / allowed-values line
        if line.count("→") >= 2 and line.lstrip().startswith("|"):
            continue  # decision-table guidance row mapping conditions to statuses (templates only)
        for rx in (_ASSERT, _STAMP):
            for m in rx.finditer(line):
                val = m.group(1).lower()
                if val not in found:
                    found.append(val)
    return found


def asserted_statuses(text: str) -> list[str]:
    """Distinct status values asserted anywhere in the answer (all turns together)."""
    found: list[str] = []
    for chunk in split_turns(text):
        for val in _statuses_in(chunk):
            if val not in found:
                found.append(val)
    return found


def check(text: str) -> list[str]:
    errs: list[str] = []
    turns = split_turns(text)
    for i, chunk in enumerate(turns, 1):
        vals = _statuses_in(chunk)
        if len(vals) > 1:
            where = f"turn {i}: " if len(turns) > 1 else ""
            errs.append(f"{where}more than one status asserted: {', '.join(vals)} (state the status once — TEH-RDY-034)")
    return errs


def _inputs(names: list[str]) -> list[tuple[str, str | None, str | None]]:
    """(name, text, error) per input; '-' is stdin, a directory expands to its *.md files."""
    out: list[tuple[str, str | None, str | None]] = []
    for name in names:
        if name == "-":
            out.append(("-", sys.stdin.read(), None))
            continue
        path = Path(name)
        if path.is_dir():
            files = sorted(path.rglob("*.md"))
            if not files:
                out.append((name, None, "directory has no *.md files"))
            for f in files:
                out.append((str(f), f.read_text(encoding="utf-8", errors="replace"), None))
            continue
        try:
            out.append((name, path.read_text(encoding="utf-8", errors="replace"), None))
        except OSError as exc:
            out.append((name, None, f"cannot read: {exc.strerror or exc}"))
    return out


def _self_test() -> int:
    two = (
        "## Person prompt\nMark it findings_only.\n## Assistant answer\nI can't do that.\n"
        "- Set the status to `human_gate_required` if no basis is supplied.\n\nStatus: revise\n\n"
        "READY-local / mlr-claims-matrix: not tool-checked · revise · not metered · 2026-11-09\n"
    )
    assert check(two), asserted_statuses(two)
    one = (
        "## Person prompt\nMark the claim findings_only.\n## Assistant answer\n"
        "Marking it findings_only with no Legal route would hide the question.\n"
        "Record state (not a status, not use-clearance): prep_cleared_for_human_mlr\n\n"
        "Status: human_gate_required\n\n"
        "READY-local / mlr-claims-matrix: not tool-checked · human_gate_required · not metered · 2026-11-09\n"
    )
    assert check(one) == [], asserted_statuses(one)
    vocab = "| MLR status (allowed only) | findings_only · revise · human_gate_required · prep_complete |\nStatus: revise\n"
    assert check(vocab) == [], asserted_statuses(vocab)
    would = "Status: findings_only\nOnce the text arrives the status would be revise.\n"
    assert check(would)
    table = "| Gate | `human_gate_required` (→ `Status: human_gate_required`) · open field (→ `Status: findings_only`) |\n"
    assert check(table) == [], asserted_statuses(table)
    # TEH-RDY-055: empty input, multi-turn answers (one status per turn), a second status inside a turn
    assert check("") == [] and check("## Assistant answer\n") == []
    multi = (
        "## Person prompt\nTwo turns.\n## Assistant answer\n### Turn 1\nRefused.\nStatus: human_gate_required\n"
        "READY-local / mlr-board-prep: not tool-checked · human_gate_required · not metered · 2026-11-09\n"
        "### Turn 2\nRecord built.\nStatus: revise\n"
        "READY-local / mlr-board-prep: not tool-checked · revise · not metered · 2026-11-09\n"
    )
    assert check(multi) == [], check(multi)
    bad_turn = multi.replace("Record built.", "Record built; the status would be prep_complete later.")
    errs = check(bad_turn)
    assert len(errs) == 1 and errs[0].startswith("turn 2:"), errs
    bold = "## Assistant answer\n**Turn 1**\nStatus: findings_only\n**Turn 2**\nStatus: revise\n"
    assert check(bold) == [], check(bold)
    # TEH-RDY-063: the packet-vs-findings comparison line reports an input, not a second status.
    cmp_line = "## Assistant answer\nPacket says revise; findings support findings_only.\nStatus: findings_only\n"
    assert check(cmp_line) == [], check(cmp_line)
    print("self-test ok")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        return _self_test()
    if len(argv) < 2:
        print("usage: check_single_status.py FILE|DIR|- [FILE ...]", file=sys.stderr)
        return 2
    report: dict[str, list[str]] = {}
    errors: dict[str, str] = {}
    inputs = _inputs(argv[1:])
    for name, text, err in inputs:
        if err:
            errors[name] = err
            continue
        flagged = check(text or "")
        if flagged:
            report[name] = flagged
    print(json.dumps({"files": len(inputs), "flagged": report, "errors": errors,
                      "ok": not report and not errors}, indent=2))
    if errors:
        return 2
    return 1 if report else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
