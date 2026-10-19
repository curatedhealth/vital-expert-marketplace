#!/usr/bin/env python3
"""Outcome statement and measure checks. Flags; never rewrites, fills or scores.

Two commands.

  statements  Checks each outcome against the standard form (GOV-06 6.1.1 to 6.1.3, Annex B.1):
              direction of change from the six, an object, a context, a party; no solution words;
              no empty verbs; a value driver it contributes to. Also flags likely duplicates
              (same object and party) and doubles (an object joined by "and").

              {"solution_words": ["copilot", "Vendor X"],          optional, the person's own terms
               "outcomes": [{"id": "1", "direction": "reduce", "object": "...",
                             "context": "...", "party": "...", "driver": "..."}, ...]}

  measures    Checks each objective: measure, unit, baseline with source, target, date, owner;
              target direction agrees with the outcome's direction.

              {"objectives": [{"outcome_id": "1", "direction": "reduce", "measure": "...",
                               "unit": "days", "baseline": 12, "baseline_source": "...",
                               "target": 5, "date": "2027-06", "owner": "..."}, ...]}

Usage:
  python3 outcome_statement_check.py statements outcomes.json
  python3 outcome_statement_check.py measures objectives.json
Output is JSON. Exit 0 when the input parsed, whatever the flags; 2 on bad input.
"""

from __future__ import annotations

import json
import re
import sys

DIRECTIONS = {"minimize", "maximize", "increase", "reduce", "eliminate", "maintain"}
DIRECTION_ALIASES = {"minimise": "minimize", "maximise": "maximize"}
LOWER_IS_BETTER = {"minimize", "reduce", "eliminate"}
HIGHER_IS_BETTER = {"maximize", "increase"}
EMPTY_VERBS = {"drive", "transform", "ignite", "optimise", "optimize", "enable", "establish",
               "accelerate", "foster", "leverage", "enhance"}
SOLUTION_WORDS = {"ai", "genai", "llm", "chatbot", "copilot", "tool", "platform", "software",
                  "agent", "agents", "automate", "automation", "automated",
                  "deploy", "deployment", "implement", "implementation", "dashboard", "app",
                  "vendor", "solution", "workflow", "process", "rpa", "machine learning"}
VAGUE_OBJECTS = {"capability", "performance", "value", "excellence", "efficiency", "quality",
                 "effectiveness", "productivity", "impact"}
WORKER_HINTS = {"team", "department", "function", "staff", "writers", "operations"}


class CheckError(ValueError):
    pass


def _words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _has_term(text: str, term: str) -> bool:
    return re.search(r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])", text.lower()) is not None


def statements(payload: dict) -> dict:
    rows = payload.get("outcomes")
    if not isinstance(rows, list) or not rows:
        raise CheckError("outcomes must be a non-empty list")
    extra = [w for w in payload.get("solution_words") or [] if isinstance(w, str) and w.strip()]
    results, seen = [], {}
    for i, o in enumerate(rows):
        oid = str(o.get("id", i + 1))
        flags = []
        direction = (o.get("direction") or "").strip().lower()
        direction = DIRECTION_ALIASES.get(direction, direction)
        obj = (o.get("object") or "").strip()
        ctx = (o.get("context") or "").strip()
        party = (o.get("party") or "").strip()
        full = " ".join([direction, obj, ctx])
        if not direction:
            flags.append("No direction of change.")
        elif direction in EMPTY_VERBS:
            flags.append(f"'{direction}' is an empty verb; use minimize, maximize, increase, reduce, eliminate or maintain.")
        elif direction not in DIRECTIONS:
            flags.append(f"'{direction}' is not one of the six directions.")
        if not obj:
            flags.append("No object of measurement: what would be counted or timed?")
        else:
            ow = set(_words(obj))
            if ow and ow <= (VAGUE_OBJECTS | {"the", "of", "our", "a", "an", "overall"}):
                flags.append(f"Object '{obj}' is too vague to count; qualify it.")
            if re.search(r"\band\b", obj.lower()):
                flags.append("Object joins two things with 'and': probably two outcomes.")
        if not ctx:
            flags.append("No context: under what conditions?")
        if not party:
            flags.append("No party: for whom must this become true?")
        elif set(_words(party)) & WORKER_HINTS:
            flags.append(f"Party '{party}' may be who does the work rather than whom the outcome is for. Check; keep it if the outcome is about their work.")
        hits = sorted({t for t in SOLUTION_WORDS | set(extra) if _has_term(full, t)})
        if hits:
            flags.append("Names a solution (" + ", ".join(hits) + "): restate, and keep the solution as an option.")
        if not (o.get("driver") or "").strip():
            flags.append("Contributes to no value driver yet.")
        key = (" ".join(_words(obj)), " ".join(_words(party)))
        if obj and key in seen:
            flags.append(f"Same object and party as outcome {seen[key]}: likely a duplicate.")
        elif obj:
            seen[key] = oid
        results.append({"id": oid,
                        "statement": " ".join(p for p in [direction.capitalize(), obj, ctx] if p),
                        "party": party or None,
                        "ok": not flags, "flags": flags})
    return {"checked": len(results), "passing": sum(r["ok"] for r in results), "outcomes": results,
            "rule": "Flags only. The person decides every change. A statement that cannot be put "
                    "in the standard form is not yet an outcome."}


def measures(payload: dict) -> dict:
    rows = payload.get("objectives")
    if not isinstance(rows, list) or not rows:
        raise CheckError("objectives must be a non-empty list")
    results = []
    for i, m in enumerate(rows):
        flags = []
        for field, msg in [("measure", "No measure."), ("unit", "No unit."),
                           ("target", "No target."), ("date", "No date for the target."),
                           ("owner", "No owner.")]:
            if m.get(field) in (None, ""):
                flags.append(msg)
        base = m.get("baseline")
        if base in (None, ""):
            flags.append("No baseline: today's level is not measured.")
        elif not m.get("baseline_source"):
            flags.append("Baseline has no source and date.")
        d = DIRECTION_ALIASES.get((m.get("direction") or "").lower(), (m.get("direction") or "").lower())
        tgt = m.get("target")
        if isinstance(base, (int, float)) and isinstance(tgt, (int, float)):
            if d in LOWER_IS_BETTER and tgt >= base:
                flags.append(f"Outcome says '{d}' but the target ({tgt}) is not below the baseline ({base}).")
            if d in HIGHER_IS_BETTER and tgt <= base:
                flags.append(f"Outcome says '{d}' but the target ({tgt}) is not above the baseline ({base}).")
            if d == "eliminate" and tgt != 0:
                flags.append("Outcome says 'eliminate' but the target is not zero; consider 'reduce'.")
        results.append({"outcome_id": str(m.get("outcome_id", i + 1)), "measure": m.get("measure"),
                        "ok": not flags, "flags": flags})
    return {"checked": len(results), "complete": sum(r["ok"] for r in results), "objectives": results,
            "rule": "Flags only. Baselines, targets, dates and owners come from people or named sources."}


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in ("statements", "measures"):
        print(__doc__)
        return 2
    files = [a for a in argv[2:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        payload = json.loads(raw)
        result = statements(payload) if argv[1] == "statements" else measures(payload)
    except (CheckError, json.JSONDecodeError, OSError) as exc:
        print(f"Not checked: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
