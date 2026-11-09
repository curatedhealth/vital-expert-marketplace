#!/usr/bin/env python3
"""Counts-only summary of a by-hand fact-check, in the manual result words.

Part of the VITAL TRUSTED Prove skills. Nothing is looked up and nothing is decided.
You pass in how many claims (one checkable fact each) fell under each manual result word (or a list of the
words themselves); the script prints those counts back in plain words, the number of
open items, one recommendation, and the line "No confidence figure".

There is no percentage, ratio, grade or threshold. Every result is read by hand, so
every output says "not tool-checked".

Manual result words (the same words as claim-assessment):

  found          Found in your passage
  partly         Partly found: <missing part> not in your passage
  not-found      Not found in your passage
  different      Your passage says something different
  no-passage     No passage to compare with
  not-factual    Opinion, recommendation or definition (left to the person)

Examples:
  python faithfulness.py --found 4 --partly 1 --not-found 1 --not-factual 2
  python faithfulness.py --words-file results.json
  echo '["Found in your passage", "Partly found: dose not in your passage"]' | python faithfulness.py --words-file -

A words file is a JSON list of manual result words. Text after "Partly found:" is
ignored for counting. An unknown word stops the script rather than being guessed.
"""
import argparse
import json
import sys

ORDER = ["found", "partly", "not_found", "different", "no_passage", "not_factual"]
FACTUAL = ["found", "partly", "not_found", "different", "no_passage"]
OPEN = ["partly", "not_found", "different", "no_passage"]

WORDS = {
    "found": "Found in your passage",
    "partly": "Partly found",
    "not_found": "Not found in your passage",
    "different": "Your passage says something different",
    "no_passage": "No passage to compare with",
    "not_factual": "Opinion, recommendation or definition (left to the person)",
}

# Longest match first so "partly found: x" is read before shorter phrases.
LOOKUP = [
    ("partly found", "partly"),
    ("found in your passage", "found"),
    ("not found in your passage", "not_found"),
    ("your passage says something different", "different"),
    ("no passage to compare with", "no_passage"),
    ("opinion, recommendation or definition", "not_factual"),
]

# One recommendation, chosen by the first open item present in risk order.
RECOMMEND = [
    ("different", "Ask the person which is right before anything else: a passage says something different."),
    ("not_found", "Remove the claims the passages do not state, or ask for a source that does."),
    ("no_passage", "Ask for a passage for the claims that had none, or take them out."),
    ("partly", "Rewrite each partly found claim to the part the passage states."),
]
NO_OPEN = "No open items. A named person still reviews the work through your usual process."


def word_to_key(raw):
    s = " ".join(str(raw).strip().lower().split())
    # "not found" must be tested before "found in your passage" is a substring match.
    if s.startswith("not found in your passage"):
        return "not_found"
    for prefix, key in LOOKUP:
        if s.startswith(prefix):
            return key
    sys.exit(f"Unknown manual result word: {raw!r}")


def counts_from_words(path):
    try:
        data = json.load(sys.stdin if path == "-" else open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Could not read JSON: {e}")
    if not isinstance(data, list):
        sys.exit("JSON must be a list of manual result words")
    counts = {k: 0 for k in ORDER}
    for item in data:
        counts[word_to_key(item)] += 1
    return counts


def summarize(counts):
    for k, v in counts.items():
        if v < 0:
            sys.exit(f"{k}: count cannot be negative")
    open_items = {k: counts[k] for k in OPEN if counts[k]}
    rec = NO_OPEN
    for key, line in RECOMMEND:
        if counts[key]:
            rec = line
            break
    return {
        "label": "Read by hand, not tool-checked",
        "factual_claims": sum(counts[k] for k in FACTUAL),
        "not_factual_listed_separately": counts["not_factual"],
        "counts": counts,
        "open_items": sum(open_items.values()),
        "recommendation": rec,
        "confidence_figure": None,
        "note": "No confidence figure: these results were not tool-checked.",
    }


def render(r):
    c = r["counts"]
    lines = [f"{r['label']}: {r['factual_claims']} factual claims"]
    for k in FACTUAL:
        lines.append(f"  {c[k]:>3}  {WORDS[k]}")
    lines.append(f"Listed separately, not in the total: {c['not_factual']} "
                 f"{WORDS['not_factual']}")
    lines.append(f"Open items: {r['open_items']}")
    lines.append(f"Recommendation: {r['recommendation']}")
    lines.append(r["note"])
    lines.append("This counts how many claims your passages state. It does not say "
                 "whether they are true, the sources good or the work ready.")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--words-file", help="JSON list of manual result words, or - for stdin")
    for k in ORDER:
        p.add_argument("--" + k.replace("_", "-"), type=int, default=None, dest=k)
    p.add_argument("--json", action="store_true", help="print JSON instead of text")
    a = p.parse_args()

    given = {k: getattr(a, k) for k in ORDER}
    if a.words_file and any(v is not None for v in given.values()):
        sys.exit("Give either --words-file or counts, not both")
    if a.words_file:
        counts = counts_from_words(a.words_file)
    else:
        if all(v is None for v in given.values()):
            sys.exit("Give counts (for example --found 3) or --words-file")
        counts = {k: (v or 0) for k, v in given.items()}
    r = summarize(counts)
    print(json.dumps(r, indent=2) if a.json else render(r))


if __name__ == "__main__":
    main()
