#!/usr/bin/env python3
"""Faithfulness percent and Verify card counts from claim-assessment statuses.

Part of the VITAL TRUSTED skill confidence-scoring (tasks TR-8.3.1 and TR-8.3.2).
Nothing is looked up. Every output is computed from the statuses passed in.

Formula (VERIFY connector instruction, as exposed on 20 October 2026):

    faithfulness percent =
        (supported + 0.5 * partial)
        / (supported + partial + unsupported + contradicted + unverifiable)

as a whole percent. out_of_scope is counted on the card but left out of the
denominator. Rounding: half up (12.5 -> 13). [CHECK] VERIFY's own rounding
convention is not stated in the connector schema.

Where the statuses came from matters. --source is required:

  --source verify   statuses returned by VERIFY tools (check_claim or verify_text).
                    The percent is computed.
  --source method   statuses decided by reading, without a tool. Counts are printed;
                    no percent is computed, by design.

Examples:
  python faithfulness.py --source verify --supported 6 --partial 2 --unsupported 1 \
      --unverifiable 1 --out-of-scope 3
  python faithfulness.py --source verify --json-file findings.json
  echo '["supported","partial","out_of_scope"]' | python faithfulness.py --source verify --json-file -
  python faithfulness.py --source method --supported 4 --unsupported 1

JSON input may be a list of status strings, a list of objects with a "status" key
(other keys are ignored, so VERIFY findings can be passed as they are), or an object
with a "findings" list of either kind.

The script never prints a pass, a fail, a grade or a threshold. A percent is a share
of checked statements backed by the supplied passages, nothing more.
"""
import argparse
import json
import sys
from decimal import Decimal, ROUND_HALF_UP

COUNTED = ["supported", "partial", "unsupported", "contradicted", "unverifiable"]
ALL_STATUSES = COUNTED + ["out_of_scope"]
OPEN = ["partial", "unsupported", "contradicted", "unverifiable"]

# Plain words for the person (TR-H13). VERIFY status names stay in the JSON output.
PLAIN = {
    "supported": "backed by the passage",
    "partial": "partly backed",
    "unsupported": "not backed by the passages checked",
    "contradicted": "contradicted by a passage",
    "unverifiable": "could not be checked",
    "out_of_scope": "not a factual statement (not counted in the percent)",
}

# One recommendation, chosen by the most serious open item present.
RECOMMEND = [
    ("contradicted", "Fix or remove the statement a passage contradicts before anything else."),
    ("unsupported", "Remove the statements the passages do not back, or supply a source that does and check again."),
    ("unverifiable", "Supply a usable source for the statements that could not be checked, or take them out."),
    ("partial", "Trim each partly backed statement to the part the passage states, or supply the missing detail."),
]
NO_OPEN = "No open items. A named person still reviews the work through your usual process."


def normalize(raw):
    s = str(raw).strip().lower().replace("-", "_").replace(" ", "_")
    if s in ("outofscope", "out_of_scope"):
        return "out_of_scope"
    if s not in ALL_STATUSES:
        sys.exit(f"Unknown status: {raw!r}. Expected one of: {', '.join(ALL_STATUSES)}")
    return s


def counts_from_json(path):
    try:
        data = json.load(sys.stdin if path == "-" else open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Could not read JSON: {e}")
    if isinstance(data, dict):
        if "findings" not in data:
            sys.exit('JSON object must have a "findings" list')
        data = data["findings"]
    if not isinstance(data, list):
        sys.exit("JSON must be a list of statuses or findings")
    counts = {k: 0 for k in ALL_STATUSES}
    for item in data:
        if isinstance(item, dict):
            if "status" not in item:
                sys.exit(f'Finding without a "status" key: {item!r}')
            item = item["status"]
        counts[normalize(item)] += 1
    return counts


def compute(counts, source):
    for k, v in counts.items():
        if v < 0:
            sys.exit(f"{k}: count cannot be negative")
    denominator = sum(counts[k] for k in COUNTED)
    numerator = Decimal(counts["supported"]) + Decimal("0.5") * Decimal(counts["partial"])
    result = {
        "source": source,
        "counts": counts,
        "statements_total": sum(counts.values()),
        "denominator": denominator,
        "open_items": {k: counts[k] for k in OPEN if counts[k]},
        "faithfulness_percent": None,
        "exact_percent": None,
        "reason_no_figure": None,
    }
    if source == "method":
        result["reason_no_figure"] = (
            "not tool-checked: these statuses were decided by reading, not returned by VERIFY"
        )
    elif denominator == 0:
        result["reason_no_figure"] = (
            "nothing to count: no factual statements were checked"
            if counts["out_of_scope"] == 0
            else "nothing to count: every statement checked was not a factual statement"
        )
    else:
        exact = numerator * 100 / Decimal(denominator)
        result["exact_percent"] = float(round(exact, 4))
        result["faithfulness_percent"] = int(exact.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    rec = NO_OPEN
    for status, line in RECOMMEND:
        if counts[status]:
            rec = line
            break
    result["recommendation"] = rec
    return result


def render(r):
    c = r["counts"]
    lines = []
    if r["faithfulness_percent"] is not None:
        lines.append(
            f"Faithfulness {r['faithfulness_percent']}%: how much of the checked text is backed "
            f"by the passages supplied (partly backed counts half). Not a measure of truth, "
            f"quality or compliance."
        )
        lines.append(
            f"  Arithmetic: ({c['supported']} + 0.5 x {c['partial']}) / {r['denominator']} "
            f"= {r['exact_percent']}%; {c['out_of_scope']} not counted."
        )
    else:
        lines.append(f"No confidence figure: {r['reason_no_figure']}.")
    lines.append("")
    label = "Checked with VERIFY" if r["source"] == "verify" else "Read, not tool-checked"
    lines.append(f"{label}: {r['statements_total']} statements")
    for k in ALL_STATUSES:
        lines.append(f"  {c[k]:>3}  {PLAIN[k]}")
    open_total = sum(r["open_items"].values())
    lines.append(f"Open items: {open_total}")
    lines.append(f"Recommendation: {r['recommendation']}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", choices=["verify", "method"], required=True,
                   help="verify: statuses returned by VERIFY; method: decided by reading (no percent)")
    p.add_argument("--json-file", help="path to JSON statuses or findings, or - for stdin")
    for k in ALL_STATUSES:
        p.add_argument("--" + k.replace("_", "-"), type=int, default=None, dest=k)
    p.add_argument("--json", action="store_true", help="print JSON instead of text")
    a = p.parse_args()

    given = {k: getattr(a, k) for k in ALL_STATUSES}
    if a.json_file and any(v is not None for v in given.values()):
        sys.exit("Give either --json-file or status counts, not both")
    if a.json_file:
        counts = counts_from_json(a.json_file)
    else:
        if all(v is None for v in given.values()):
            sys.exit("Give status counts (for example --supported 3) or --json-file")
        counts = {k: (v or 0) for k, v in given.items()}

    r = compute(counts, a.source)
    print(json.dumps(r, indent=2) if a.json else render(r))


if __name__ == "__main__":
    main()
