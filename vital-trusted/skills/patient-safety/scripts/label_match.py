#!/usr/bin/env python3
"""Compare safety sentences in a draft with the supplied label text.

For each draft sentence that mentions dose, contraindication, warning, interaction or a
special population, find the closest label sentence and report:
  word for word  - same text after normalizing spaces, case and punctuation (or an
                   exact part of a longer label sentence, marked as such)
  close          - similar wording; numbers, units or key terms that differ are listed
  not found      - nothing similar in the supplied label text

Text comparison only. A match does not mean the statement fits the reader or the market,
or that the label is current. Read every "close" result.

Usage:
    python label_match.py label.txt draft.txt
    python label_match.py label.txt draft.txt --json
    python label_match.py label.txt draft.txt --threshold 0.55
"""
import argparse
import difflib
import json
import re
import sys

SAFETY_TERMS = re.compile(
    r"\b(?:dos(?:e|es|ing|age)|mg|mcg|µg|microgram|ml|units?|once|twice|daily|tablet|"
    r"capsule|inject|infusion|contraindicat\w*|must not|do not use|should not|warning|"
    r"precaution|caution|interact\w*|concomitant|inhibitor|inducer|pregnan\w*|"
    r"breast-?feed\w*|lactat\w*|fertility|contracep\w*|child\w*|paediatric|pediatric|"
    r"adolescent|infant|elderly|older|geriatric|renal|kidney|creatinine|hepatic|liver|"
    r"child-pugh|impairment|missed|overdose|maximum)\b",
    re.IGNORECASE,
)

# Words whose change alters a safety meaning; listed when they differ.
KEY_TERMS = [
    "must not", "should not", "do not", "not recommended", "contraindicated", "caution",
    "avoid", "mild", "moderate", "severe", "adults", "children", "elderly", "only",
    "maximum", "once", "twice", "daily", "weekly", "with food", "without food",
]

NUM = re.compile(r"\d+(?:[.,]\d+)?\s*(?:mg/kg|ml/min|mg|mcg|µg|g|ml|units?|%|hours?|days?|weeks?)?",
                 re.IGNORECASE)


def sentences(text):
    text = re.sub(r"[ \t]+", " ", text)
    # A short line with no closing punctuation (a heading or table cell) stands alone.
    lines = text.split("\n")
    marked = []
    for ln in lines:
        st = ln.strip()
        if st and len(st) < 70 and not re.search(r"[.;:,!?]$", st):
            marked.append(st + "\n\n")
        else:
            marked.append(ln + "\n")
    text = "".join(marked)
    parts = re.split(r"(?<=[.;!?])\s+|\n\s*\n|\n(?=\s*[-*•])", text)
    out = []
    for p in parts:
        p = p.strip(" \n-*•\t")
        if len(p) >= 8:
            out.append(p)
    return out


def norm(s):
    s = s.lower()
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[^\w%/.' ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip(" .")
    return s


POPULATIONS = {
    "kidney": re.compile(r"\b(?:renal|kidney|creatinine)", re.I),
    "liver": re.compile(r"\b(?:hepatic|liver|child-pugh)", re.I),
    "children": re.compile(r"\b(?:child(?!-pugh)|children|paediatric|pediatric|adolescent|infant)", re.I),
    "elderly": re.compile(r"\b(?:elderly|older|geriatric)", re.I),
    "pregnancy or breastfeeding": re.compile(r"\b(?:pregnan|breast-?feed|lactat)", re.I),
}


def populations(s):
    return {k for k, rx in POPULATIONS.items() if rx.search(s)}


def numbers(s):
    return sorted({re.sub(r"\s+", "", m.group(0).lower().replace(",", "."))
                   for m in NUM.finditer(s) if m.group(0).strip()})


def key_terms(s):
    low = " " + norm(s) + " "
    return {t for t in KEY_TERMS if f" {t} " in low}


def compare(label_text, draft_text, threshold=0.6):
    label_sents = sentences(label_text)
    label_norm = [norm(s) for s in label_sents]
    results = []
    for d in sentences(draft_text):
        if not SAFETY_TERMS.search(d):
            continue
        dn = norm(d)
        best_i, best_r, part = -1, 0.0, False
        for i, ln in enumerate(label_norm):
            if dn == ln:
                best_i, best_r, part = i, 1.0, False
                break
            if dn and len(dn) >= 15 and dn in ln:
                best_i, best_r, part = i, 1.0, True
                break
            r = difflib.SequenceMatcher(None, dn, ln).ratio()
            # Prefer a label sentence about the same population (kidney, liver, ...).
            dp, lp = populations(d), populations(label_sents[i])
            r = min(0.99, r + 0.2 * len(dp & lp) - 0.1 * len(dp - lp))
            if r > best_r:
                best_i, best_r = i, r
        entry = {"draft": d, "similarity": round(best_r, 2)}
        if best_r == 1.0:
            entry["result"] = "word for word"
            entry["label"] = label_sents[best_i]
            if part:
                entry["part_of_longer_label_sentence"] = True
        elif best_r >= threshold:
            entry["result"] = "close"
            entry["label"] = label_sents[best_i]
            dnums, lnums = numbers(d), numbers(label_sents[best_i])
            entry["numbers_only_in_draft"] = [n for n in dnums if n not in lnums]
            entry["numbers_only_in_label"] = [n for n in lnums if n not in dnums]
            dk, lk = key_terms(d), key_terms(label_sents[best_i])
            entry["terms_only_in_draft"] = sorted(dk - lk)
            entry["terms_only_in_label"] = sorted(lk - dk)
            entry["populations_draft"] = sorted(populations(d))
            entry["populations_label"] = sorted(populations(label_sents[best_i]))
        else:
            entry["result"] = "not found in the supplied label"
            if best_i >= 0:
                entry["nearest_label"] = label_sents[best_i]
        results.append(entry)
    return results


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("label")
    ap.add_argument("draft")
    ap.add_argument("--threshold", type=float, default=0.6,
                    help="match score at or above which a sentence is 'close' (default 0.6); "
                         "the score is text similarity, raised when draft and label sentence "
                         "concern the same population")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    with open(args.label, encoding="utf-8") as fh:
        label = fh.read()
    with open(args.draft, encoding="utf-8") as fh:
        draft = fh.read()
    res = compare(label, draft, args.threshold)
    summary = {k: sum(1 for r in res if r["result"] == k)
               for k in ("word for word", "close", "not found in the supplied label")}
    if args.json:
        print(json.dumps({"summary": summary, "statements": res}, indent=2, ensure_ascii=False))
        return 0
    print(f"Safety statements in the draft: {len(res)}")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    for i, r in enumerate(res, 1):
        print(f"\n{i}. [{r['result']}] (match score {r['similarity']})")
        print(f"   draft: {r['draft']}")
        if "label" in r:
            print(f"   label: {r['label']}")
        if r.get("part_of_longer_label_sentence"):
            print("   note: the draft quotes part of a longer label sentence; check no condition was dropped")
        for key, lab in (("numbers_only_in_draft", "numbers only in draft"),
                         ("numbers_only_in_label", "numbers only in label"),
                         ("terms_only_in_draft", "terms only in draft"),
                         ("terms_only_in_label", "terms only in label")):
            if r.get(key):
                print(f"   {lab}: {', '.join(r[key])}")
    print("\nText comparison only. Read every 'close' result; it does not say the label is current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
