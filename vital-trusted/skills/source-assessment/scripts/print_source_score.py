#!/usr/bin/env python3
"""Print a VERIFY source score as the total plus the axes that have numbers.

Part of the VITAL TRUSTED skill source-assessment (task TR-8.2.1).

  python print_source_score.py qualify_result.json
  cat qualify_result.json | python print_source_score.py -

VERIFY's instruction: "Under each reference, print the source_score total and the axes
whose values are numbers. Omit an axis whose value is null." This script does only that.
It never computes, rescales or rounds a score. If the JSON holds no score, it says so.

The return shape of qualify_source is not yet confirmed ([CHECK] in references/tools.md).
Accepted shapes, searched anywhere in the JSON:
  {"source_score": {"total": 72, "axes": {"authority": 25, "relevance": null, ...}}}
  {"source_score": {"total": 72, "authority": 25, "relevance": null, ...}}
  {"source_score": 72}                       (total only)
"""
import json
import sys

TOTAL_KEYS = ("total", "score", "value")
NON_AXIS_KEYS = set(TOTAL_KEYS) | {"axes", "weights", "reasons", "note", "notes", "version"}
PLAIN = {
    "authority": "who published it",
    "recency": "how recent it is",
    "relevance": "how well it matches your question",
    "provenance": "how completely it identifies itself",
    "currency": "whether a retraction or update check cleared it",
}


def is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def find_score(obj):
    if isinstance(obj, dict):
        if "source_score" in obj:
            return obj["source_score"]
        for v in obj.values():
            r = find_score(v)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = find_score(v)
            if r is not None:
                return r
    return None


def render(data):
    s = find_score(data)
    if s is None:
        return "No source_score in this result. Print nothing for the score; do not estimate one."
    if is_number(s):
        return f"Source score {s}"
    if not isinstance(s, dict):
        return "source_score has an unexpected shape. Print the tool's result as returned; do not reformat."
    total = next((s[k] for k in TOTAL_KEYS if is_number(s.get(k))), None)
    axes = s.get("axes") if isinstance(s.get("axes"), dict) else {k: v for k, v in s.items() if k not in NON_AXIS_KEYS}
    shown = [(k, v) for k, v in axes.items() if is_number(v)]
    head = f"Source score {total}" if total is not None else "Source score total not returned"
    line = head + (": " + " · ".join(f"{k} {v}" for k, v in shown) if shown else "")
    out = [line]
    meanings = [f"{k}: {PLAIN[k]}" for k, _ in shown if k in PLAIN]
    if meanings:
        out.append("Plain meaning: " + "; ".join(meanings) + ".")
    return "\n".join(out)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    raw = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8").read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Not JSON ({e}). Paste the tool result exactly as returned.")
        sys.exit(1)
    print(render(data))


if __name__ == "__main__":
    main()
