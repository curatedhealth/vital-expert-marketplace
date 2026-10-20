#!/usr/bin/env python3
"""Helper for data-quality-monitoring (dh-technology).

Five subcommands. None of them sets a limit, a pass rule, an owner or a
decision: every limit comes from the person's rules file, every owner and date
from the person's repair log. Flags are facts about the files, never verdicts.
Standard library only.

  rules    Check the person's rules file before anything is run: each check's
           Kahn category, field, limit and the date the rules were written.
           Flags Q1 to Q6.
             python3 dq_check.py rules --rules RULES.json
  run      Run the person's checks on one dataset version and print counts,
           shares, the person's limit and the result (pass, fail, or "limit not
           given"). Optional --json writes the results for the review step.
             python3 dq_check.py run --data DATA.csv --rules RULES.json \
                 --version v4 [--ref patients=PATIENTS.csv] [--json RESULTS.json]
  compare  Compare two dataset versions field by field: row counts, missing
           shares, numeric mean and median, category shares. No threshold;
           a difference is a fact.
             python3 dq_check.py compare --old OLD.csv --new NEW.csv --fields a,b,c
  review   Join the run results with the person's repair log (CSV: check_id,
           owner, action, new_version, recheck_date, note) and flag every failed
           check that lacks an owner, an action, a new version or a recheck
           date. Flags R1 to R6.
             python3 dq_check.py review --results RESULTS.json --log REPAIRS.csv
  words    Count a short answer against the 450-word cap. Leaves out the
           "Calls made" block (up to the record block, which is counted) and
           the Source and Rows columns.
             python3 dq_check.py words ANSWER.md
"""
import argparse
import ast
import csv
import json
import operator
import re
import statistics
import sys
from datetime import date, datetime

CAP = 450
KAHN = {
    "value_conformance": "Conformance (value)",
    "relational_conformance": "Conformance (relational)",
    "computational_conformance": "Conformance (computational)",
    "completeness": "Completeness",
    "plausibility_uniqueness": "Plausibility (uniqueness)",
    "plausibility_atemporal": "Plausibility (atemporal)",
    "plausibility_temporal": "Plausibility (temporal)",
    "leak": "Leak check (feature dated after the index time; the person's rule, outside Kahn)",
    "row_count": "Row count against the cohort (the person's rule, outside Kahn)",
}


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def blank(v):
    return v is None or str(v).strip() == "" or str(v).strip().lower() in ("na", "n/a", "null", "none")


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def as_date(v):
    if blank(v):
        return None
    s = str(v).strip()
    try:
        return datetime.fromisoformat(s[:19])
    except ValueError:
        try:
            return datetime.fromisoformat(s[:10])
        except ValueError:
            return None


def full_date(s):
    try:
        d = date.fromisoformat(str(s)[:10])
        return f"{d.day} {d.strftime('%B')} {d.year}"
    except (TypeError, ValueError):
        return "not given"


def load_rules(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def field_label(c):
    if c.get("category") == "row_count":
        return "all rows"
    if c.get("field"):
        return c["field"]
    if c.get("fields"):
        return ", ".join(c["fields"])
    if c.get("before") or c.get("after"):
        return f"{c.get('before', 'not given')} on or before {c.get('after', 'not given')}"
    return "not given"


# ---------------------------------------------------------------- rules
def cmd_rules(a):
    r = load_rules(a.rules)
    checks = r.get("checks", [])
    print(f"Dataset: {r.get('dataset', 'not given')}; rules for version {r.get('version', 'not given')}; "
          f"unit of row {r.get('unit_of_row', 'not given')}; written {full_date(r.get('written_on'))} by {r.get('written_by', 'not given')}.")
    print("| Check | Kahn category | Field(s) | Context | Your limit | Flags |")
    print("|---|---|---|---|---|---|")
    cats = set()
    for c in checks:
        fl = []
        cat = c.get("category", "")
        cats.add(cat)
        if cat not in KAHN:
            fl.append("Q2 category not recognized")
        if "limit" not in c or c.get("limit") is None:
            fl.append("Q3 limit not given")
        fields = field_label(c)
        print(f"| {c.get('id')} | {KAHN.get(cat, cat)} | {fields or 'not given'} | {c.get('context', 'not given')} | "
              f"{'not given' if c.get('limit') is None else c.get('limit')} | {', '.join(fl) or 'none'} |")
    print()
    if blank(r.get("version")):
        print("Q1 dataset version not given.")
    if cats and cats <= {"completeness"}:
        print("Q4 completeness is the only check: the old rule says a single completeness percentage is not enough.")
    if "leak" not in cats:
        print("Q5 no leak check: no feature is checked against the index time.")
    if blank(r.get("written_on")):
        print("Q6 date the rules were written not given: a run cannot show the rules came before the results.")
    print("Limits, categories and the version are the person's; this check sets none.")
    return 0


# ---------------------------------------------------------------- run
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
       ast.Pow: operator.pow, ast.USub: operator.neg}


def safe_eval(expr, row):
    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            return OPS[type(node.op)](ev(node.left), ev(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
            return OPS[type(node.op)](ev(node.operand))
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.Name):
            v = num(row.get(node.id))
            if v is None:
                raise ValueError("missing")
            return v
        raise ValueError("formula element not allowed")
    return ev(ast.parse(expr, mode="eval"))


def run_check(c, rows, refs):
    cat = c.get("category")
    checked, failing, note = 0, 0, ""
    f = c.get("field")
    if f and rows and f not in rows[0]:
        return None, None, f"field {f} not in the data"
    if cat == "value_conformance":
        allowed = c.get("allowed")
        typ = c.get("type")
        pat = c.get("pattern")
        for r in rows:
            v = r.get(f)
            if blank(v):
                continue
            checked += 1
            ok = True
            if allowed is not None and str(v).strip() not in [str(x) for x in allowed]:
                ok = False
            if typ == "number" and num(v) is None:
                ok = False
            if typ == "date" and as_date(v) is None:
                ok = False
            if pat and not re.fullmatch(pat, str(v).strip()):
                ok = False
            failing += not ok
        note = "blank values are left to completeness"
    elif cat == "relational_conformance":
        ref = refs.get(c.get("ref"))
        if ref is None:
            return None, None, f"reference file {c.get('ref')} not supplied (--ref {c.get('ref')}=PATH)"
        keys = {str(x.get(c.get("ref_field", f))).strip() for x in ref}
        for r in rows:
            v = r.get(f)
            if blank(v):
                continue
            checked += 1
            failing += str(v).strip() not in keys
    elif cat == "computational_conformance":
        tol = c.get("tolerance", 0)
        for r in rows:
            if blank(r.get(f)):
                continue
            try:
                calc = safe_eval(c["formula"], r)
            except (ValueError, ZeroDivisionError, KeyError):
                continue
            checked += 1
            failing += abs(num(r.get(f)) - calc) > tol
        note = f"recomputed as {c.get('formula')}, tolerance {tol} (yours)"
    elif cat == "completeness":
        checked = len(rows)
        failing = sum(1 for r in rows if blank(r.get(f)) or str(r.get(f)).strip() in [str(x) for x in c.get("missing_codes", [])])
        note = "decision-time feature" if c.get("decision_time") else ""
    elif cat == "plausibility_uniqueness":
        fields = c.get("fields", [])
        missing = [x for x in fields if rows and x not in rows[0]]
        if missing:
            return None, None, f"field(s) {', '.join(missing)} not in the data"
        seen = {}
        for r in rows:
            k = tuple(str(r.get(x)).strip() for x in fields)
            seen[k] = seen.get(k, 0) + 1
        checked = len(rows)
        failing = sum(n for n in seen.values() if n > 1)
        note = "rows sharing a key with another row"
    elif cat == "plausibility_atemporal":
        lo, hi = c.get("min"), c.get("max")
        for r in rows:
            v = num(r.get(f))
            if v is None:
                continue
            checked += 1
            failing += (lo is not None and v < lo) or (hi is not None and v > hi)
        note = f"range {lo} to {hi} (yours)"
    elif cat == "plausibility_temporal":
        b, e = c.get("before"), c.get("after")
        for r in rows:
            d1, d2 = as_date(r.get(b)), as_date(r.get(e))
            if d1 is None or d2 is None:
                continue
            checked += 1
            failing += d1 > d2
        note = f"{b} on or before {e}"
    elif cat == "leak":
        idx = c.get("index_field")
        for r in rows:
            d1, d2 = as_date(r.get(f)), as_date(r.get(idx))
            if d1 is None or d2 is None:
                continue
            checked += 1
            failing += d1 > d2
        note = f"{f} dated after {idx}"
    elif cat == "row_count":
        exp = c.get("expected_rows")
        if exp is None:
            return len(rows), None, "expected row count not given"
        return len(rows), abs(len(rows) - exp), f"{len(rows)} rows against {exp} expected from your cohort rule"
    else:
        return None, None, "category not recognized"
    return checked, failing, note


def cmd_run(a):
    r = load_rules(a.rules)
    rows = read_csv(a.data)
    refs = {}
    for spec in a.ref or []:
        k, p = spec.split("=", 1)
        refs[k] = read_csv(p)
    rv = r.get("version")
    print(f"Data file {a.data}: {len(rows)} rows, labeled version {a.version or 'not given'}; "
          f"rules written for version {rv or 'not given'} on {full_date(r.get('written_on'))}.")
    if a.version and rv and str(a.version) != str(rv):
        print(f"V1 the rules were written for version {rv}; this run reads version {a.version}. Results are reported against the rules as written.")
    if not a.version:
        print("V2 dataset version not given: the result cannot be tied to a version.")
    print("| Check | Kahn category | Field | Rows checked | Failing | Share failing | Your limit | Result | Note |")
    print("|---|---|---|---|---|---|---|---|---|")
    results = []
    for c in r.get("checks", []):
        checked, failing, note = run_check(c, rows, refs)
        lim = c.get("limit")
        share = None
        if c.get("category") == "row_count":
            res = "limit not given" if (lim is None or failing is None) else ("pass" if failing <= lim else "fail")
            share_s = ""
        else:
            share = (failing / checked) if (checked and failing is not None) else None
            share_s = "" if share is None else f"{100 * share:.1f}%"
            if checked is None:
                res = "not run"
            elif lim is None:
                res = "limit not given"
            else:
                res = "pass" if (share or 0) <= lim else "fail"
        field = field_label(c)
        print(f"| {c.get('id')} | {KAHN.get(c.get('category'), c.get('category'))} | {field} | "
              f"{'' if checked is None else checked} | {'' if failing is None else failing} | {share_s} | "
              f"{'not given' if lim is None else lim} | {res} | {note} |")
        results.append({"id": c.get("id"), "category": c.get("category"), "field": field, "checked": checked,
                        "failing": failing, "share": share, "limit": lim, "result": res, "note": note,
                        "decision_time": bool(c.get("decision_time"))})
    n_fail = sum(1 for x in results if x["result"] == "fail")
    n_pass = sum(1 for x in results if x["result"] == "pass")
    n_nl = sum(1 for x in results if x["result"] == "limit not given")
    n_nr = sum(1 for x in results if x["result"] == "not run")
    print(f"\nAgainst your limits: {n_pass} pass, {n_fail} fail, {n_nl} with no limit given, {n_nr} not run.")
    leaks = [x["field"] for x in results if x["category"] == "leak" and (x["failing"] or 0) > 0]
    if leaks:
        print(f"Features with rows dated after the index time: {', '.join(leaks)}.")
    print("Whether the dataset is fit for its use is the person's call; a failed check stays open until the person closes it with evidence.")
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump({"data": a.data, "version": a.version, "rules_version": rv, "results": results}, fh, indent=1)
    return 0


# ---------------------------------------------------------------- compare
def cmd_compare(a):
    old, new = read_csv(a.old), read_csv(a.new)
    print(f"Rows: {len(old)} in {a.old}; {len(new)} in {a.new}.")
    print("| Field | Missing share old | Missing share new | Old summary | New summary |")
    print("|---|---|---|---|---|")
    for f in [x.strip() for x in a.fields.split(",") if x.strip()]:
        def summ(rows):
            if not rows or f not in rows[0]:
                return "field not in file", None
            vals = [r.get(f) for r in rows]
            miss = sum(1 for v in vals if blank(v)) / len(vals)
            nums = [num(v) for v in vals if not blank(v)]
            if nums and all(x is not None for x in nums):
                return miss, f"mean {statistics.mean(nums):.2f}, median {statistics.median(nums):.2f}, n {len(nums)}"
            cnt = {}
            for v in vals:
                if not blank(v):
                    cnt[str(v).strip()] = cnt.get(str(v).strip(), 0) + 1
            tot = sum(cnt.values()) or 1
            top = sorted(cnt.items(), key=lambda kv: -kv[1])[:4]
            return miss, "; ".join(f"{k} {100 * v / tot:.0f}%" for k, v in top)
        mo, so = summ(old)
        mn, sn = summ(new)
        fm = lambda m: m if isinstance(m, str) else f"{100 * m:.1f}%"
        print(f"| {f} | {fm(mo)} | {fm(mn)} | {so or ''} | {sn or ''} |")
    print("\nDifferences are facts about the two files, not a verdict and not a drift threshold. "
          "What they mean for a model's performance goes to model-performance-and-drift-monitoring (this pack).")
    return 0


# ---------------------------------------------------------------- review
def cmd_review(a):
    res = json.load(open(a.results, encoding="utf-8"))
    log = {r.get("check_id"): r for r in read_csv(a.log)} if a.log else {}
    failed = [x for x in res["results"] if x["result"] == "fail"]
    print(f"Run on version {res.get('version') or 'not given'}: {len(failed)} failed checks against your limits.")
    print("| Check | Field | Failing | Owner (yours) | Action (yours) | New version | Recheck date | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    for x in failed:
        e = log.get(x["id"], {})
        fl = []
        owner = e.get("owner") if not blank(e.get("owner")) else "owner not named"
        if owner == "owner not named":
            fl.append("R1 owner not named")
        act = (e.get("action") or "").strip().lower()
        if act not in ("removed", "redefined", "stopped", "accepted with reason"):
            fl.append("R2 action not given")
        nv = e.get("new_version") if not blank(e.get("new_version")) else "not given"
        if nv == "not given" and act in ("removed", "redefined"):
            fl.append("R3 new dataset version not given")
        if nv != "not given" and str(nv) == str(res.get("version")):
            fl.append("R4 the repair names the failed version itself")
        rd = full_date(e.get("recheck_date")) if not blank(e.get("recheck_date")) else "not given"
        if rd == "not given" and act != "stopped":
            fl.append("R5 recheck date not given")
        print(f"| {x['id']} | {x['field']} | {x['failing']} of {x['checked']} | {owner} | {e.get('action') or 'not given'} | "
              f"{nv} | {rd} | {', '.join(fl) or 'none'} |")
    extra = [k for k in log if k not in {x['id'] for x in failed}]
    if extra:
        print(f"\nR6 repair log rows for checks that did not fail in this run: {', '.join(extra)}.")
    nl = [x["id"] for x in res["results"] if x["result"] == "limit not given"]
    if nl:
        print(f"Checks with no limit given (reported, never marked pass or fail): {', '.join(nl)}.")
    print("Until a failed check is closed with a new version, the failed version is not used for training (old task: 'Do not train on the failed version'). Owners, actions and dates are the person's.")
    return 0


# ---------------------------------------------------------------- words
def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows", "source and rows (doi for [paper])")
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            low = [c.lower() for c in cells]
            if any(c in names for c in low):
                drop = {i for i, c in enumerate(low) if c in names}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop))
        else:
            if not line.strip():
                drop = set()
            out.append(line)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9.,'%()/-]*", "\n".join(out)))


def cmd_words(a):
    n = count_words(a.answer)
    print(f"{n} words")
    if n <= CAP:
        print("within the short-mode cap")
        return 0
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, "
          "rows not tied to the question; never a gap, a stop or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("rules")
    r.add_argument("--rules", required=True)
    u = sub.add_parser("run")
    u.add_argument("--data", required=True)
    u.add_argument("--rules", required=True)
    u.add_argument("--version")
    u.add_argument("--ref", action="append")
    u.add_argument("--json")
    c = sub.add_parser("compare")
    c.add_argument("--old", required=True)
    c.add_argument("--new", required=True)
    c.add_argument("--fields", required=True)
    v = sub.add_parser("review")
    v.add_argument("--results", required=True)
    v.add_argument("--log")
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"rules": cmd_rules, "run": cmd_run, "compare": cmd_compare, "review": cmd_review, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
