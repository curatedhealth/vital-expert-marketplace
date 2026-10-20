#!/usr/bin/env python3
"""List balance cues in a draft, and what the source material holds that the draft does not.

It finds wording, not meaning. It makes no judgment about balance.

Usage:
  python balance_cues.py draft.txt
  python balance_cues.py draft.txt --source material.txt
  python balance_cues.py draft.txt --window 2 --json
  cat draft.txt | python balance_cues.py -

Outputs:
  - each line with benefit, risk or limitation, reassurance, or selection wording
  - counts of benefit lines and risk or limitation lines
  - benefit lines with no risk or limitation wording within --window lines (default 3)
  - with --source: study names and time points in the material that do not appear in the draft
"""
import argparse
import json
import re
import sys

BENEFIT = [
    r"\bimprov\w*", r"\breduc\w*", r"\befficac\w*", r"\beffective\w*", r"\bbenefit\w*",
    r"\brespon(?:se|ded|ders?)\b", r"\bremission\b", r"\bclear(?:ed|ance)?\b",
    r"\bsuperior\w*", r"\bbetter\b", r"\bfaster\b", r"\bprevent\w*", r"\bprotect\w*",
    r"\bcut\b", r"\bhalv\w*", r"\bachiev\w*", r"\bmet (?:its|the) primary\b",
    r"\bfewer\b", r"\bsaving\w*", r"\bvalue\b", r"\bconvenien\w*",
]
RISK = [
    r"\badverse\b", r"\bside[- ]effects?\b", r"\bSAEs?\b", r"\bAEs?\b", r"\bserious\b",
    r"\bdiscontinu\w*", r"\bwithdr[ae]w\w*", r"\bstopped\b", r"\bdrop(?:ped)? ?out\w*",
    r"\bwarning\w*", r"\bcontraindicat\w*", r"\binfection\w*", r"\bdeaths?\b",
    r"\blimitation\w*", r"\bnot (?:statistically )?significant\b", r"\bdid not\b",
    r"\bnot met\b", r"\bfailed\b", r"\bmissed\b", r"\bopen[- ]label\b",
    r"\bshort follow[- ]up\b", r"\bpost hoc\b", r"\binterim\b", r"\buncertain\w*",
    r"\brisks?\b", r"\btoxic\w*", r"\breactions?\b", r"\bnausea\b",
]
REASSURANCE = [
    r"\bsafe\b", r"\bwell[- ]tolerated\b", r"\bno side[- ]effects?\b",
    r"\bfree (?:of|from) side[- ]effects?\b",
    r"\b(?:favou?rable|proven|established|demonstrated|excellent|reassuring|clean|benign)\s+safety\b",
    r"\bsafety profile\b", r"\bno (?:new )?safety (?:signals?|concerns?)\b",
    r"\bminimal side[- ]effects?\b", r"\bsimilar to placebo\b", r"\bgentle\b",
]
SELECTION = [
    r"\bup to\b", r"\bas early as\b", r"\bpeak\w*\b", r"\bin responders\b",
    r"\bcompleters?\b", r"\bpatients who completed\b", r"\bsubgroup\w*\b", r"\bsubset\b",
    r"\bpost hoc\b", r"\bexploratory\b", r"\bbest\b",
]

TIMEPOINT = re.compile(
    r"\b(?:week|wk|month|year|day)s?\s*\d+\b|\b\d+\s*(?:weeks?|months?|years?|days?)\b",
    re.IGNORECASE,
)
STUDY = re.compile(r"\b[A-Z][A-Z]{2,}(?:-[A-Z0-9]+)*-\d+[A-Z]?\b")

GROUPS = [
    ("benefit", BENEFIT),
    ("risk or limitation", RISK),
    ("reassurance", REASSURANCE),
    ("selection", SELECTION),
]
COMPILED = [(g, [re.compile(p, re.IGNORECASE) for p in pats]) for g, pats in GROUPS]
# AE/SAE are case-sensitive abbreviations; avoid matching the word "ae" in other text.
COMPILED = [
    (g, [re.compile(p.pattern) if p.pattern in (r"\bSAEs?\b", r"\bAEs?\b") else p for p in pats])
    for g, pats in COMPILED
]


def scan(text):
    """Return one row per line that has any cue: line, groups, matches, text."""
    rows = []
    for i, line in enumerate(text.splitlines(), start=1):
        groups = {}
        for g, pats in COMPILED:
            found = []
            for p in pats:
                found += [m.group(0) for m in p.finditer(line)]
            if found:
                groups[g] = found
        if groups:
            rows.append({"line": i, "groups": groups, "text": line.strip()})
    return rows


def unpaired_benefits(rows, window):
    """Benefit lines with no risk or limitation cue within +/- window lines."""
    risk_lines = [r["line"] for r in rows if "risk or limitation" in r["groups"]]
    out = []
    for r in rows:
        if "benefit" in r["groups"] and "risk or limitation" not in r["groups"]:
            if not any(abs(r["line"] - k) <= window for k in risk_lines):
                out.append(r["line"])
    return out


def _norm_tp(s):
    s = s.lower().replace("wk", "week")
    num = re.search(r"\d+", s).group(0)
    unit = re.search(r"week|month|year|day", s).group(0)
    return f"{unit} {num}"


def missing_from_draft(draft, source):
    """Study names and time points present in the source but not in the draft."""
    d_studies = set(STUDY.findall(draft))
    s_studies = set(STUDY.findall(source))
    d_tps = {_norm_tp(m.group(0)) for m in TIMEPOINT.finditer(draft)}
    s_tps = {_norm_tp(m.group(0)) for m in TIMEPOINT.finditer(source)}
    return {
        "studies": sorted(s_studies - d_studies),
        "time points": sorted(s_tps - d_tps, key=lambda x: (x.split()[0], int(x.split()[1]))),
    }


def report(draft, source=None, window=3):
    rows = scan(draft)
    result = {
        "lines": rows,
        "counts": {
            "benefit lines": sum(1 for r in rows if "benefit" in r["groups"]),
            "risk or limitation lines": sum(1 for r in rows if "risk or limitation" in r["groups"]),
            "reassurance lines": sum(1 for r in rows if "reassurance" in r["groups"]),
            "selection lines": sum(1 for r in rows if "selection" in r["groups"]),
        },
        "benefit lines with no risk or limitation nearby": unpaired_benefits(rows, window),
        "window": window,
        "note": "Wording cues only. Read the whole draft; this makes no judgment.",
    }
    if source is not None:
        result["in the material, not in the draft"] = missing_from_draft(draft, source)
    return result


def _read(path):
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("draft", help="draft text file, or - for stdin")
    ap.add_argument("--source", help="supplied material text file")
    ap.add_argument("--window", type=int, default=3, help="lines either side counted as nearby")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    draft = _read(a.draft)
    source = _read(a.source) if a.source else None
    res = report(draft, source, a.window)
    if a.json:
        print(json.dumps(res, indent=2))
        return 0
    for r in res["lines"]:
        tags = "; ".join(f"{g}: {', '.join(m)}" for g, m in r["groups"].items())
        print(f"line {r['line']:>3}  [{tags}]  {r['text']}")
    print()
    for k, v in res["counts"].items():
        print(f"{k}: {v}")
    print(f"benefit lines with no risk or limitation within {a.window} lines: "
          f"{res['benefit lines with no risk or limitation nearby'] or 'none'}")
    if source is not None:
        miss = res["in the material, not in the draft"]
        print(f"studies in the material, not in the draft: {miss['studies'] or 'none'}")
        print(f"time points in the material, not in the draft: {miss['time points'] or 'none'}")
    print(res["note"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
