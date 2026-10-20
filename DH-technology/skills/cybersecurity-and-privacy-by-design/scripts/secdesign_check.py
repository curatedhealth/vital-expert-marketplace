#!/usr/bin/env python3
"""Checks for cybersecurity and privacy by design, on the person's own files.

Subcommands
  datamap  --file CLASSES.csv
      Data classes with region, legal basis and controls. Flags D1 to D6.
  threats  --file THREATS.csv
      Threat register keyed to hops. Flags T1 to T6 and counts by hop.
  sbom     --file SBOM.csv|SBOM.json --as-of YYYY-MM-DD [--kev KEV.csv]
           [--support-horizon YYYY-MM-DD]
      Software bill of materials: identification fields (EN-026), level of
      support and end-of-support date (EN-054), components past their
      end-of-support date, and known vulnerabilities that appear in the
      KEV list the person supplies (EN-052, EN-080 [WF]). Flags S1 to S7.
  words    ANSWER.md
      Counts a short answer against the 450-word cap, leaving out the calls
      list and the Source and Rows columns of tables.

The script never sets a threshold, a severity, a support horizon or an
acceptance. It prints facts against the person's own inputs. Lines that
start with '#' in a CSV are comments (used to label illustrative files).
"""
import argparse
import csv
import datetime as dt
import io
import json
import re
import sys

CAP = 450


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.lstrip().startswith("#")]
    rows = list(csv.DictReader(io.StringIO("".join(lines))))
    return [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in rows]


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return dt.date.fromisoformat(s)
    except ValueError:
        return "bad"


def fmt(d):
    return f"{d.day} {d.strftime('%B')} {d.year}"


# ---------------------------------------------------------------- datamap
LAW_WORDS = {"hipaa", "gdpr", "mdr", "part 2", "42 cfr part 2", "mhmda", "ccpa", "nis2", "cra"}


def cmd_datamap(a):
    rows = read_csv(a.file)
    print(f"Data classes read: {len(rows)} (file {a.file})")
    bases = set()
    flags = 0
    for r in rows:
        cid = r.get("data_class", "?")
        out = []
        basis = r.get("legal_basis", "")
        if not basis or basis.lower() in {"gap", "[gap]", "not given"}:
            out.append("D1 legal basis not given [GAP]")
        else:
            bases.add(basis.lower())
        if not r.get("region"):
            out.append("D2 region not given")
        for col in ("control_access", "retention", "leaves_region"):
            if not r.get(col):
                out.append(f"D3 {col} not given")
        ctl = r.get("control_access", "").lower()
        if ctl and ctl in LAW_WORDS:
            out.append("D4 control names a law, not a mechanism")
        if not r.get("artifact"):
            out.append("D5 no artifact shows the control in force")
        if r.get("in_force", "").lower() not in {"yes", "y", "true"}:
            out.append("D6 control not shown in force (intended only or not given)")
        flags += len(out)
        print(f"- {cid} | region {r.get('region') or 'not given'} | basis {basis or 'not given'} | "
              + ("; ".join(out) if out else "no flag"))
    if len(rows) > 1 and len(bases) == 1:
        print(f"Note: every class carries the same basis ({bases.pop()}); the old rule says one basis is not applied to every class. Fact for the owner, not a finding.")
    print(f"Flags: {flags}. The legal basis for each class is the person's or their legal owner's call; the script only reports what is filled.")


# ---------------------------------------------------------------- threats
def cmd_threats(a):
    rows = read_csv(a.file)
    print(f"Threats read: {len(rows)} (file {a.file})")
    by_hop = {}
    open_n = covered = accepted = 0
    versions = set()
    for r in rows:
        tid = r.get("id", "?")
        hop = r.get("hop") or "hop not given"
        out = []
        if not r.get("asset"):
            out.append("T1 no asset named (the old rule drops a threat with no asset; owner to decide)")
        ctl = r.get("control", "")
        acc = r.get("accepted_by", "")
        if not ctl and not acc:
            out.append("T2 open: neither a control nor an acceptance")
            state = "open"
        elif ctl:
            state = "covered by a control (as stated)"
        else:
            state = "accepted (as stated)"
        if acc and acc.lower() in {"team", "security", "it", "us", "we"}:
            out.append("T3 acceptance has no named person")
        if acc and not r.get("reopen_condition"):
            out.append("T4 acceptance has no reopen condition")
        if not r.get("design_version"):
            out.append("T5 design version not given")
        else:
            versions.add(r["design_version"])
        if not r.get("actor"):
            out.append("T6 actor not given")
        if state == "open":
            open_n += 1
        elif state.startswith("covered"):
            covered += 1
        else:
            accepted += 1
        by_hop.setdefault(hop, {"total": 0, "open": 0})
        by_hop[hop]["total"] += 1
        if state == "open":
            by_hop[hop]["open"] += 1
        print(f"- {tid} | {hop} | {state} | " + ("; ".join(out) if out else "no flag"))
    print(f"Covered {covered}, accepted {accepted}, open {open_n}.")
    for h, c in by_hop.items():
        print(f"  hop '{h}': {c['total']} threats, {c['open']} open")
    if len(versions) > 1:
        print(f"Note: rows cite {len(versions)} design versions ({', '.join(sorted(versions))}); the model is not dated to one version.")
    print("A control listed is the person's statement; whether it addresses the threat, and whether a risk is acceptable, is the person's call.")


# ---------------------------------------------------------------- sbom
def load_sbom(path):
    if path.lower().endswith(".json"):
        d = json.load(open(path, encoding="utf-8"))
        comps = []
        for c in d.get("components", []):
            props = {p.get("name"): p.get("value") for p in c.get("properties", []) or []}
            sup = c.get("supplier") or {}
            comps.append({
                "component": c.get("name", ""),
                "supplier": sup.get("name", "") if isinstance(sup, dict) else str(sup),
                "version": c.get("version", ""),
                "release_date": props.get("release_date", ""),
                "patch": props.get("patch", ""),
                "level_of_support": props.get("level_of_support", ""),
                "end_of_support": props.get("end_of_support", ""),
                "known_vulnerabilities": props.get("known_vulnerabilities", ""),
            })
        return comps
    return read_csv(path)


def cmd_sbom(a):
    as_of = parse_date(a.as_of)
    if not as_of or as_of == "bad":
        sys.exit("--as-of YYYY-MM-DD is required (the person's read date)")
    horizon = parse_date(a.support_horizon) if a.support_horizon else None
    kev = set()
    if a.kev:
        for r in read_csv(a.kev):
            v = r.get("id") or r.get("cveID") or r.get("cve_id") or ""
            if v:
                kev.add(v.strip())
    comps = load_sbom(a.file)
    print(f"Components read: {len(comps)} (file {a.file}); as of {fmt(as_of)}")
    print("Support horizon: " + (fmt(horizon) + " (the person's)" if horizon and horizon != "bad" else "not given"))
    print("KEV list: " + (f"{len(kev)} ids from {a.kev} (the person's export)" if a.kev else "not given; S7 not checked"))
    counts = {}
    for c in comps:
        name = f"{c.get('component') or '?'} {c.get('version') or ''}".strip()
        out = []
        for col, label in (("component", "title"), ("supplier", "manufacturer"), ("version", "version"),
                           ("release_date", "release date")):
            if not c.get(col):
                out.append(f"S1 {label} not given (EN-026)")
        lvl = (c.get("level_of_support") or "").lower()
        if not lvl:
            out.append("S2 level of support not given (EN-054)")
        elif lvl in {"no longer maintained", "abandoned"}:
            out.append(f"S6 level of support stated as '{lvl}' (EN-054 wording)")
        eos = parse_date(c.get("end_of_support"))
        if eos is None:
            out.append("S3 end-of-support date not given (EN-054)")
        elif eos == "bad":
            out.append("S3 end-of-support date unreadable")
        else:
            if eos <= as_of:
                out.append(f"S4 end-of-support {fmt(eos)} on or before the read date")
            elif horizon and horizon != "bad" and eos < horizon:
                out.append(f"S5 end-of-support {fmt(eos)} before your support horizon {fmt(horizon)}")
        vulns = [v.strip() for v in re.split(r"[;,]", c.get("known_vulnerabilities") or "") if v.strip()]
        hits = [v for v in vulns if v in kev]
        if hits:
            out.append("S7 listed in your KEV export: " + ", ".join(hits) + " (EN-052: designed out; EN-080 [WF])")
        for o in out:
            k = o.split()[0]
            counts[k] = counts.get(k, 0) + 1
        vtxt = f" | known vulnerabilities listed: {len(vulns)}" if vulns else " | known vulnerabilities listed: none stated"
        print(f"- {name}{vtxt} | " + ("; ".join(out) if out else "no flag"))
    print("Flag counts: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none"))
    print("Severity, reachability and the response to each component are the person's call. NTIA minimum elements are not checked: that document is not in this skill's sources [GAP].")


# ---------------------------------------------------------------- words
def strip_calls_and_cols(text):
    lines = text.splitlines()
    out = []
    skip = False
    drop_idx = None
    for ln in lines:
        if re.match(r"^\s*#*\s*\**\s*Calls made", ln, re.I):
            skip = True
            continue
        if skip and (re.match(r"^\s*#", ln) or re.match(r"^\s*\**\s*(Record|Clears it|One line|Full version)", ln, re.I)):
            skip = False
        if skip:
            continue
        if ln.strip().startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if drop_idx is None and any(c.lower() in {"source", "rows", "row", "source and rows"} for c in cells):
                drop_idx = {i for i, c in enumerate(cells) if c.lower() in {"source", "rows", "row", "source and rows"}}
            if drop_idx:
                cells = [c for i, c in enumerate(cells) if i not in drop_idx]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            out.append(" ".join(cells))
        else:
            drop_idx = None if not ln.strip() else drop_idx
            out.append(ln)
    return "\n".join(out)


def cmd_words(a):
    text = open(a.answer, encoding="utf-8").read()
    body = strip_calls_and_cols(text)
    n = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.\-/%]*", body))
    print(f"Words counted: {n} (cap {CAP}; calls list and Source and Rows columns left out)")
    if n <= CAP:
        print("within the short-mode cap")
    else:
        print(f"over the cap by {n - CAP}: cut context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the question; never a gap, a stop or the record line")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("datamap"); s.add_argument("--file", required=True); s.set_defaults(f=cmd_datamap)
    s = sub.add_parser("threats"); s.add_argument("--file", required=True); s.set_defaults(f=cmd_threats)
    s = sub.add_parser("sbom"); s.add_argument("--file", required=True); s.add_argument("--as-of", required=True)
    s.add_argument("--kev"); s.add_argument("--support-horizon"); s.set_defaults(f=cmd_sbom)
    s = sub.add_parser("words"); s.add_argument("answer"); s.set_defaults(f=cmd_words)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
