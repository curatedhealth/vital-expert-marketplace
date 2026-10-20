#!/usr/bin/env python3
"""Software quality and delivery reads on the person's own files (software-quality-and-delivery-monitoring).

Every flag is a fact about the person's file read against the person's own lists and rules. The script
supplies no threshold: no coverage figure, failure rate, capacity margin or end-of-support allowance.

Subcommands
  trace      --hazards H.csv --cases C.csv --candidate BUILD
             hazards: id, hazard, item, class (as the person states), influences_clinical_action (yes|no)
             cases:   id, hazard_ids (semicolon list), level (unit|integration|system|validation),
                      spec_ref, expected, build, result (pass|fail|not run), waiver
             Flags T1 hazard with no case; T2 hazard covered only by unit-level cases (person to judge
             whether they exercise the hazard); T3 case run on a build other than the candidate with no
             waiver; T4 failed or not run; T5 expected output "works correctly" or blank; T6 class not tied
             to a hazard or not given; T7 item marked as influencing a clinical action with the class the
             person names as lowest (--lowest-class, only if the person gives it).
  plans      --register P.csv --product NAME
             plan, document, version, status (present|draft|missing|template), product
             Flags L1 missing; L2 draft; L3 template not filled; L4 names another product.
  releases   --log R.csv --required STAGE,STAGE,... --from YYYY-MM-DD --to YYYY-MM-DD
             release_id, date, build, stages_run (semicolon list), exception (hotfix|blank),
             exception_recorded_on (date or blank), outcome (deployed|rolled_back|failed_health_check),
             clinical_defect (yes|no|blank), caught_at (stage name|production|blank)
             Counts deploys, rollbacks, failed health checks and reverted clinical defects; lists
             releases that skipped a required stage. Flags R1 required stage skipped; R2 skip with no
             exception recorded at the time; R3 caught in production; R4 caught_at not given.
  sbom       --file S.csv --as-of YYYY-MM-DD [--kev KEV.csv]
             component, version, supplier, support_level, end_of_support, cves (semicolon list)
             KEV file (from the person): a column named cveID or cve_id.
             Flags S1 support level or end of support not given; S2 support level outside the three FDA
             values; S3 no longer maintained or abandoned; S4 end of support before the read date;
             S5 a listed CVE id is in the KEV file the person supplied.
  capacity   --file K.csv
             unit, design_number, measured_value, measured_on, environment, kind (load test|production
             peak|quota), first_failure_component, saturated_component
             Prints measured / design as arithmetic. Flags K1 kind is a quota (not a load test);
             K2 no measurement; K3 saturation on a component other than the named first-failure one.
  residency  --file P.csv
             store, data_class, design_region, live_region, replica_regions (semicolon list),
             backup_region
             Flags Y1 live region differs from design; Y2 replica outside design region;
             Y3 backup region not given or outside design region.
  misses     --file M.csv --as-of YYYY-MM-DD
             id, unit, element, pass_rule, result (pass|fail|not measured), blocks_release (yes|no|blank),
             owner, recheck_date, status (open|stopped|closed), closed_evidence, build
             Flags G1 pass rule not given; G2 failed element with no owner; G3 failed, open, no recheck
             date; G4 closed with no evidence; G5 recheck date before the read date (a fact);
             G6 blocks_release not stated for a failed element; G7 build not given.
  words      ANSWER.md
"""
import argparse
import csv
import re
import sys
from datetime import date

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
SUPPORT = {"maintained", "no longer maintained", "abandoned"}


def blank(v):
    return v is None or str(v).strip() == "" or str(v).strip().lower() in {"not given", "n/a", "na"}


def show(v):
    return "not given" if blank(v) else str(v).strip()


def pdate(v):
    if blank(v):
        return None
    try:
        y, m, d = [int(x) for x in str(v).strip().split("-")]
        return date(y, m, d)
    except ValueError:
        return None


def full(d):
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def fdate(v):
    d = pdate(v)
    return full(d) if d else show(v)


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [{(k or "").strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]


def lst(v):
    return [x.strip() for x in re.split(r"[;,]", v or "") if x.strip()]


def tally(counts, flags):
    for f in flags:
        k = f.split(" ")[0]
        counts[k] = counts.get(k, 0) + 1


def summary(counts):
    return ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none"


def cmd_trace(a):
    hz = read(a.hazards)
    cs = read(a.cases)
    by_h = {}
    for c in cs:
        for h in lst(c.get("hazard_ids")):
            by_h.setdefault(h, []).append(c)
    print(f"Release candidate: {a.candidate}. Hazards from your risk file; cases from your test records.")
    print("| Hazard | Item | Class (yours) | Cases | Levels | Flags |")
    print("|---|---|---|---|---|---|")
    hc = {}
    for h in hz:
        flags = []
        cases = by_h.get(h.get("id"), [])
        if not cases:
            flags.append("T1")
        elif all(c.get("level", "").lower() == "unit" for c in cases):
            flags.append("T2")
        if blank(h.get("class")):
            flags.append("T6")
        if a.lowest_class and h.get("class", "").strip().upper() == a.lowest_class.strip().upper() \
                and h.get("influences_clinical_action", "").lower() == "yes":
            flags.append("T7")
        tally(hc, flags)
        print(f"| {show(h.get('id'))} {show(h.get('hazard'))} | {show(h.get('item'))} | {show(h.get('class'))} | "
              f"{', '.join(c.get('id') for c in cases) or 'none'} | "
              f"{', '.join(sorted({c.get('level', '') for c in cases})) or 'none'} | {', '.join(flags) or 'none'} |")
    print()
    print("| Case | Hazards | Spec | Expected | Build | Result | Waiver | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    cc = {}
    known = {h.get("id") for h in hz}
    for c in cs:
        flags = []
        if c.get("build") != a.candidate and blank(c.get("waiver")):
            flags.append("T3")
        if c.get("result", "").lower() in {"fail", "not run", ""}:
            flags.append("T4")
        exp = c.get("expected", "")
        if blank(exp) or re.search(r"works?\s+correctly", exp, re.I):
            flags.append("T5")
        tally(cc, flags)
        unknown = [x for x in lst(c.get("hazard_ids")) if x not in known]
        hz_txt = c.get("hazard_ids", "") + (f" (not in hazard list: {', '.join(unknown)})" if unknown else "")
        print(f"| {show(c.get('id'))} | {show(hz_txt)} | {show(c.get('spec_ref'))} | {show(exp)} | {show(c.get('build'))} | "
              f"{show(c.get('result'))} | {show(c.get('waiver'))} | {', '.join(flags) or 'none'} |")
    print()
    print(f"Hazards: {len(hz)}; flags {summary(hc)}. Cases: {len(cs)}; flags {summary(cc)}.")
    print("T2 lists hazards whose only cases are unit-level; whether they exercise the hazard is yours to judge. "
          "Repeat or waive T3 cases is your decision. No coverage figure is a rule unless you set one.")
    return 0


def cmd_plans(a):
    rows = read(a.register)
    print(f"Plans your procedure requires, checked against product '{a.product}'. Status as recorded; documents not opened.")
    print("| Plan | Document | Version | Status | Product named | Flags |")
    print("|---|---|---|---|---|---|")
    counts = {}
    for r in rows:
        flags = []
        st = r.get("status", "").lower()
        if blank(st) or st == "missing":
            flags.append("L1")
        elif st == "draft":
            flags.append("L2")
        elif st == "template":
            flags.append("L3")
        if not blank(r.get("product")) and r["product"].strip().lower() != a.product.strip().lower():
            flags.append("L4")
        tally(counts, flags)
        print(f"| {show(r.get('plan'))} | {show(r.get('document'))} | {show(r.get('version'))} | {show(r.get('status'))} | "
              f"{show(r.get('product'))} | {', '.join(flags) or 'none'} |")
    print()
    present = sum(1 for r in rows if r.get("status", "").lower() == "present" and
                  (blank(r.get("product")) or r["product"].strip().lower() == a.product.strip().lower()))
    print(f"Plans listed: {len(rows)}; present and naming this product: {present}; flags {summary(counts)}.")
    return 0


def cmd_releases(a):
    rows = read(a.log)
    req = [s.strip().lower() for s in a.required.split(",") if s.strip()]
    f0, t0 = pdate(getattr(a, "from")), pdate(a.to)
    if not f0 or not t0:
        print("Period not given: pass --from and --to (the person's period). Nothing counted.")
        return 2
    rows = [r for r in rows if pdate(r.get("date")) and f0 <= pdate(r["date"]) <= t0]
    print(f"Period: {full(f0)} to {full(t0)}. Required stages (yours): {', '.join(req)}.")
    print("| Release | Date | Build | Stages run | Skipped | Exception | Recorded on | Outcome | Clinical defect | Caught at | Flags |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    counts, n = {}, {"deployed": 0, "rolled_back": 0, "failed_health_check": 0}
    clinical = 0
    for r in rows:
        flags = []
        ran = [s.lower() for s in lst(r.get("stages_run"))]
        skipped = [s for s in req if s not in ran]
        if skipped:
            flags.append("R1")
            if blank(r.get("exception_recorded_on")):
                flags.append("R2")
        out = r.get("outcome", "").lower()
        if out in n:
            n[out] += 1
        if out in {"rolled_back", "failed_health_check"}:
            if r.get("caught_at", "").lower() == "production":
                flags.append("R3")
            elif blank(r.get("caught_at")):
                flags.append("R4")
        if r.get("clinical_defect", "").lower() == "yes":
            clinical += 1
        tally(counts, flags)
        print(f"| {show(r.get('release_id'))} | {fdate(r.get('date'))} | {show(r.get('build'))} | {show(r.get('stages_run'))} | "
              f"{', '.join(skipped) or 'none'} | {show(r.get('exception'))} | {fdate(r.get('exception_recorded_on'))} | "
              f"{show(r.get('outcome'))} | {show(r.get('clinical_defect'))} | {show(r.get('caught_at'))} | {', '.join(flags) or 'none'} |")
    total = len(rows)
    print()
    print(f"Releases in period: {total}. Deployed and kept: {n['deployed']}; rolled back: {n['rolled_back']}; "
          f"failed health check: {n['failed_health_check']}; releases you marked as a clinical defect: {clinical}.")
    if total:
        print(f"Arithmetic on your log: rolled back or failed {n['rolled_back'] + n['failed_health_check']} of {total} "
              f"({100 * (n['rolled_back'] + n['failed_health_check']) / total:.0f}%). No source sets a rate; the reading is yours.")
    print("Flags: " + summary(counts) + ". An unrecorded skip (R2) is not treated as a hotfix.")
    return 0


def cmd_sbom(a):
    rows = read(a.file)
    asof = pdate(a.as_of)
    if not asof:
        print("Read date not given: pass --as-of (the person's read date). Nothing checked.")
        return 2
    kev = set()
    if a.kev:
        for r in read(a.kev):
            v = r.get("cveid") or r.get("cve_id") or r.get("cve")
            if v:
                kev.add(v.strip().upper())
    print(f"Read date: {full(asof)}. Fields: FDA premarket cybersecurity guidance (EN-054). "
          + ("KEV list: supplied by you, " + str(len(kev)) + " ids." if a.kev else "KEV list: not supplied; S5 not checked."))
    print("| Component | Version | Supplier | Support level | End of support | CVE ids (yours) | Flags |")
    print("|---|---|---|---|---|---|---|")
    counts = {}
    for r in rows:
        flags = []
        sl = r.get("support_level", "").lower()
        if blank(sl) or blank(r.get("end_of_support")):
            flags.append("S1")
        if not blank(sl) and sl not in SUPPORT:
            flags.append("S2")
        if sl in {"no longer maintained", "abandoned"}:
            flags.append("S3")
        eos = pdate(r.get("end_of_support"))
        if eos and eos < asof:
            flags.append(f"S4 ({(asof - eos).days} days before the read date)")
        hits = [c for c in lst(r.get("cves")) if c.upper() in kev]
        if hits:
            flags.append("S5 (" + ", ".join(hits) + ")")
        tally(counts, flags)
        print(f"| {show(r.get('component'))} | {show(r.get('version'))} | {show(r.get('supplier'))} | {show(r.get('support_level'))} | "
              f"{fdate(r.get('end_of_support'))} | {show(r.get('cves'))} | {', '.join(flags) or 'none'} |")
    print()
    print(f"Components: {len(rows)}. Flags: {summary(counts)}.")
    print("Dates and matches are facts. Whether a risk is controlled or uncontrolled, and the patch priority, are yours "
          "(security-and-privacy-operations-monitoring, this pack).")
    return 0


def num(v):
    try:
        return float(str(v).replace(",", ""))
    except ValueError:
        return None


def cmd_capacity(a):
    rows = read(a.file)
    print("Scale claims against your measurements. Ratio = measured / design (arithmetic, not a verdict).")
    print("| Unit | Design number | Measured | Ratio | Measured on | Environment | Kind | First-failure (design) | Saturated | Flags |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    counts = {}
    for r in rows:
        flags = []
        d, m = num(r.get("design_number", "")), num(r.get("measured_value", ""))
        kind = r.get("kind", "").lower()
        if kind == "quota":
            flags.append("K1")
        if m is None:
            flags.append("K2")
        sat, ff = r.get("saturated_component", ""), r.get("first_failure_component", "")
        if not blank(sat) and not blank(ff) and sat.strip().lower() != ff.strip().lower():
            flags.append("K3")
        tally(counts, flags)
        ratio = f"{m / d:.2f}" if d and m is not None else "n/a"
        print(f"| {show(r.get('unit'))} | {show(r.get('design_number'))} | {show(r.get('measured_value'))} | {ratio} | "
              f"{fdate(r.get('measured_on'))} | {show(r.get('environment'))} | {show(r.get('kind'))} | {show(ff)} | {show(sat)} | "
              f"{', '.join(flags) or 'none'} |")
    print()
    print(f"Flags: {summary(counts)}. A quota is not a load test (K1). Saturation on a component the design did not name "
          "is shown, not hidden (K3); whether the design note changes is yours.")
    return 0


def cmd_residency(a):
    rows = read(a.file)
    print("Live placement against your placement table.")
    print("| Store | Data class | Design region | Live region | Replicas | Backup | Flags |")
    print("|---|---|---|---|---|---|---|")
    counts = {}
    for r in rows:
        flags = []
        dr = r.get("design_region", "").strip().lower()
        if not blank(r.get("live_region")) and r["live_region"].strip().lower() != dr:
            flags.append("Y1")
        if any(x.lower() != dr for x in lst(r.get("replica_regions"))):
            flags.append("Y2")
        if blank(r.get("backup_region")) or r["backup_region"].strip().lower() != dr:
            flags.append("Y3")
        tally(counts, flags)
        print(f"| {show(r.get('store'))} | {show(r.get('data_class'))} | {show(r.get('design_region'))} | {show(r.get('live_region'))} | "
              f"{show(r.get('replica_regions'))} | {show(r.get('backup_region'))} | {', '.join(flags) or 'none'} |")
    print()
    print(f"Flags: {summary(counts)}. A region difference is a fact; whether it is permitted (BAA, transfer rules) is "
          "for the owner you name (cybersecurity-and-privacy-by-design, this pack).")
    return 0


def cmd_misses(a):
    rows = read(a.file)
    asof = pdate(a.as_of)
    if not asof:
        print("Read date not given: pass --as-of. Nothing checked.")
        return 2
    print(f"Read date: {full(asof)}. Rules, owners and recheck dates are yours.")
    print("| Id | Unit | Element | Your rule | Result | Blocks release | Owner | Recheck | Status | Build | Flags |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    counts, res = {}, {"pass": 0, "fail": 0, "not measured": 0}
    for r in rows:
        flags = []
        result = r.get("result", "").lower()
        if blank(r.get("pass_rule")):
            flags.append("G1")
        elif result in res:
            res[result] += 1
        failed = result == "fail" and not blank(r.get("pass_rule"))
        st = r.get("status", "").lower()
        if failed and blank(r.get("owner")):
            flags.append("G2")
        if failed and st == "open" and blank(r.get("recheck_date")):
            flags.append("G3")
        if st == "closed" and blank(r.get("closed_evidence")):
            flags.append("G4")
        rd = pdate(r.get("recheck_date"))
        if rd and rd < asof and st == "open":
            flags.append("G5")
        if failed and blank(r.get("blocks_release")):
            flags.append("G6")
        if blank(r.get("build")):
            flags.append("G7")
        tally(counts, flags)
        print(f"| {show(r.get('id'))} | {show(r.get('unit'))} | {show(r.get('element'))} | {show(r.get('pass_rule'))} | "
              f"{show(r.get('result')) if not blank(r.get('pass_rule')) else 'not read (no rule)'} | {show(r.get('blocks_release'))} | "
              f"{show(r.get('owner')) if not blank(r.get('owner')) else 'owner not named'} | {fdate(r.get('recheck_date'))} | "
              f"{show(r.get('status'))} | {show(r.get('build'))} | {', '.join(flags) or 'none'} |")
    print()
    print(f"Against your rules: pass {res['pass']}, fail {res['fail']}, not measured {res['not measured']}; "
          f"elements without a rule: {counts.get('G1', 0)} (not marked pass or fail). Flags: {summary(counts)}.")
    print("No overall verdict and no go or no-go: the gate decision is yours, recorded against the build id with a named acceptor.")
    return 0


def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows", "source (row)")
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
    print(f"{n} words (calls list and Source or Rows columns excluded); cap 450")
    if n <= 450:
        print("within the short-mode cap")
        return 0
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, "
          "rows not tied to the question; never a gap, a stop or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("trace")
    t.add_argument("--hazards", required=True)
    t.add_argument("--cases", required=True)
    t.add_argument("--candidate", required=True)
    t.add_argument("--lowest-class", default=None)
    p = sub.add_parser("plans")
    p.add_argument("--register", required=True)
    p.add_argument("--product", required=True)
    r = sub.add_parser("releases")
    r.add_argument("--log", required=True)
    r.add_argument("--required", required=True)
    r.add_argument("--from", required=True)
    r.add_argument("--to", required=True)
    s = sub.add_parser("sbom")
    s.add_argument("--file", required=True)
    s.add_argument("--as-of", required=True)
    s.add_argument("--kev", default=None)
    k = sub.add_parser("capacity")
    k.add_argument("--file", required=True)
    y = sub.add_parser("residency")
    y.add_argument("--file", required=True)
    m = sub.add_parser("misses")
    m.add_argument("--file", required=True)
    m.add_argument("--as-of", required=True)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"trace": cmd_trace, "plans": cmd_plans, "releases": cmd_releases, "sbom": cmd_sbom,
            "capacity": cmd_capacity, "residency": cmd_residency, "misses": cmd_misses,
            "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
