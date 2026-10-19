#!/usr/bin/env python3
"""Screen launch claims and leave-behind text against the risk words in
references/claim-rules.md (section 4) and, for a leave-behind, against the
approved claim ids.

A hit is a prompt for a person to read the claim, not a finding. A claim with
no hit can still exceed the authorization. Nothing here clears a claim.

Usage:
  python3 claim_screen.py --claims CLAIMS.csv            # columns: id,claim[,status]
  python3 claim_screen.py --claims CLAIMS.txt            # one claim per line
  python3 claim_screen.py --claims APPROVED.csv --text LEAVE_BEHIND.txt
  add --json for machine-readable output

In CLAIMS.csv an optional 'status' column marks approval; with --text, only
rows whose status is 'approved' count as approved (all rows if no column).
"""
import argparse
import csv
import json
import re
import sys

# (label, regex, rows) from references/claim-rules.md section 4
RISK_WORDS = [
    ("cure", r"\bcur(e|es|ed)\b", "PC-EU-10, PC-UK-07, PC-UK-13 [INDUSTRY]"),
    ("guaranteed success", r"\bguarantee(d)?\b|\balways works\b|\b100\s?%", "PC-DE-04, PC-UK-13 [INDUSTRY]"),
    ("no side effects", r"\bno side[- ]effects?\b|\brisk[- ]free\b|\b(completely|absolutely) safe\b", "PC-DE-04, PC-UK-13 [INDUSTRY]"),
    ("FDA approved or registered", r"\bFDA[- ](approved|registered)\b", "CP-US-74, PC-EU-11"),
    ("approval or endorsement", r"\bcertified\b|\bendorsed\b|\brecommended by\b", "PC-EU-11, PC-UK-08"),
    ("clinically proven", r"\bclinically proven\b", "PC-UK-04, PC-UK-10 [INDUSTRY]"),
    ("clinical grade or accuracy", r"\b(clinical|medical)[- ]grade\b|\bclinically accurate\b", "PC-US-63"),
    ("device-indicating verb", r"\bdiagnos(e|es|ed|is)\b|\bdetects?\b|\btreats?\b|\bprevents?\b", "PC-UK-04, PC-US-63"),
    ("discourages treatment", r"\breplaces?\b|\binstead of (your )?(doctor|therapist|therapy|medication)\b|\bno need to see\b", "PC-UK-11 [INDUSTRY]"),
    ("coverage or price statement", r"\breimburs(ed|able)\b|\bcovered by\b|\bfree of charge\b|\bkostenlos\b", "PC-EU-07"),
    ("HIPAA seal", r"\bHIPAA[- ](compliant|certified)\b", "PC-US-78 [WF]"),
    ("testimonial", r"\btestimonial\b|\bfive stars\b|\b5 stars\b", "PC-UK-03, PC-DE-11"),
    ("opaque offer (DiGA)", r"\bfree trial\b|\bsubscription\b|\bauto[- ]renew", "PC-DE-17"),
]


def load_claims(path):
    rows = []
    if path.lower().endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows.append({"id": (r.get("id") or "").strip(),
                             "claim": (r.get("claim") or "").strip(),
                             "status": (r.get("status") or "").strip().lower()})
    else:
        with open(path, encoding="utf-8") as f:
            for i, line in enumerate(l.strip() for l in f):
                if line:
                    rows.append({"id": f"C{i+1}", "claim": line, "status": ""})
    return [r for r in rows if r["claim"]]


def screen(text):
    hits = []
    for label, rx, rows in RISK_WORDS:
        for m in re.finditer(rx, text, flags=re.IGNORECASE):
            hits.append({"word": m.group(0), "flag": label, "rows": rows})
    return hits


def norm(s):
    return re.sub(r"[^a-z0-9%]+", " ", s.lower()).strip()


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip(" -*\t") for p in parts if len(norm(p)) > 0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claims", required=True)
    ap.add_argument("--text")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    claims = load_claims(a.claims)
    out = {"claims": [], "text": None,
           "note": "Hits are prompts for review against references/claim-rules.md, not findings. Nothing here clears a claim."}
    for c in claims:
        out["claims"].append({"id": c["id"], "claim": c["claim"], "status": c["status"] or None,
                              "hits": screen(c["claim"])})

    if a.text:
        has_status = any(c["status"] for c in claims)
        approved = [c for c in claims if (c["status"] == "approved" or not has_status)]
        appr_norm = {c["id"]: norm(c["claim"]) for c in approved}
        with open(a.text, encoding="utf-8") as f:
            body = f.read()
        lines = []
        for s in sentences(body):
            ns = norm(s)
            match = [cid for cid, cn in appr_norm.items() if cn and (cn in ns or ns in cn)]
            lines.append({"sentence": s, "approved_claim_ids": match,
                          "status": "maps to approved claim" if match else "not an approved claim: review or remove",
                          "hits": screen(s)})
        out["text"] = {"sentences": len(lines),
                       "mapped": sum(1 for l in lines if l["approved_claim_ids"]),
                       "unmapped": sum(1 for l in lines if not l["approved_claim_ids"]),
                       "lines": lines}

    if a.json:
        json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
        print()
        return
    print("Claim screen (prompts for review, not findings)")
    for c in out["claims"]:
        flags = "; ".join(f"{h['flag']} ('{h['word']}', {h['rows']})" for h in c["hits"]) or "no risk word"
        st = f" [{c['status']}]" if c["status"] else ""
        print(f"- {c['id']}{st}: {c['claim']}\n    {flags}")
    if out["text"]:
        t = out["text"]
        print(f"\nLeave-behind: {t['sentences']} sentences, {t['mapped']} map to approved claims, {t['unmapped']} do not")
        for l in t["lines"]:
            ids = ",".join(l["approved_claim_ids"]) or "-"
            flags = "; ".join(f"{h['flag']} ({h['rows']})" for h in l["hits"])
            print(f"- [{ids}] {l['sentence']}\n    {l['status']}{'; ' + flags if flags else ''}")


if __name__ == "__main__":
    main()
