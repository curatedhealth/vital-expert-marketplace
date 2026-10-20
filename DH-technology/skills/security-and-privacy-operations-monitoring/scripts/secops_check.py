#!/usr/bin/env python3
"""Checks for security and privacy operations monitoring, on the person's own files.

Subcommands
  controls --file CONTROLS.csv
      Claimed control versus artifact. Proof status per row (proven as stated,
      unproven, contradicted as stated) and flags C1 to C6.
  vulns    --file VULNS.csv --as-of YYYY-MM-DD [--windows "critical=30,high=90"]
           [--since YYYY-MM-DD]
      Open reachable vulnerabilities with age from intake, against the windows
      the person gives; closed items checked for resolution evidence; repeat
      failure classes counted. Flags V1 to V9.
  consent  --purposes PURPOSES.csv --processing PROCESSING.csv
           [--withdrawal WITHDRAWAL.csv]
      Consent text versus what the system does, and the withdrawal test log.
      Flags P1 to P3 and W1 to W3.
  words    ANSWER.md
      Counts a short answer against the 450-word cap, leaving out the calls
      list and the Source and Rows columns.

The script never sets a window, a severity, a pass rule or an owner. Where the
person gives none, it says "not given". Lines starting with '#' in a CSV are
comments (used to label illustrative files).
"""
import argparse
import csv
import datetime as dt
import io
import re
import sys

CAP = 450
YES = {"yes", "y", "true", "1"}


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.lstrip().startswith("#")]
    rows = list(csv.DictReader(io.StringIO("".join(lines))))
    return [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in rows]


def pdate(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return dt.date.fromisoformat(s)
    except ValueError:
        return "bad"


def fmt(d):
    return f"{d.day} {d.strftime('%B')} {d.year}"


# ---------------------------------------------------------------- controls
def cmd_controls(a):
    rows = read_csv(a.file)
    print(f"Controls read: {len(rows)} (file {a.file})")
    tally = {}
    for r in rows:
        cid = r.get("control_id", "?")
        art = r.get("artifact", "")
        atype = (r.get("artifact_type") or "").lower()
        note = (r.get("reviewer_note") or "").lower()
        out = []
        if not art:
            status = "unproven"
            out.append("C1 no artifact named")
        elif atype in {"control matrix", "matrix"}:
            status = "unproven"
            out.append("C2 only evidence is the control matrix itself")
        elif note.startswith("contradict"):
            status = "contradicted (as the reviewer noted)"
        else:
            status = "proven as stated (artifact named; the model has not opened it)"
        if not r.get("citation"):
            out.append("C3 citation not given")
        if atype in {"policy"} and not r.get("artifact_date"):
            out.append("C4 artifact undated")
        if not status.startswith("proven"):
            if not r.get("owner"):
                out.append("C5 owner not named")
            if not r.get("due"):
                out.append("C6 due date not given")
            gc = r.get("gap_class") or "not given"
            out.append(f"gap class (yours): {gc}")
        tally[status.split(" (")[0]] = tally.get(status.split(" (")[0], 0) + 1
        print(f"- {cid} | {r.get('claimed_control', '')} | cites {r.get('citation') or 'not given'} | {status} | "
              + ("; ".join(out) if out else "no flag"))
    print("Totals: " + ", ".join(f"{k} {v}" for k, v in tally.items()))
    print("Blocking versus documentation miss is the person's classification; the script prints it only where given.")


# ---------------------------------------------------------------- vulns
def parse_windows(s):
    w = {}
    if not s:
        return w
    for part in s.split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            w[k.strip().lower()] = int(v)
    return w


def cmd_vulns(a):
    as_of = pdate(a.as_of)
    if not as_of or as_of == "bad":
        sys.exit("--as-of YYYY-MM-DD is required (the person's read date)")
    windows = parse_windows(a.windows)
    since = pdate(a.since) if a.since else None
    rows = read_csv(a.file)
    print(f"Items read: {len(rows)} (file {a.file}); as of {fmt(as_of)}")
    print("Windows: " + (", ".join(f"{k} {v} days" for k, v in windows.items()) + " (the person's)" if windows else "not given; no item is called past its window"))
    open_rows, closed_rows, unreach, unknown = [], [], [], []
    for r in rows:
        st = (r.get("status") or "").lower()
        reach = (r.get("reachable") or "").lower()
        if st in {"open", "under review", "triage", ""}:
            if reach == "no":
                unreach.append(r)
            elif reach in {"yes"}:
                open_rows.append(r)
            else:
                unknown.append(r)
        else:
            closed_rows.append(r)
    print(f"\nOpen and reachable: {len(open_rows)}")
    past = 0
    for r in sorted(open_rows, key=lambda x: str(x.get("intake_date"))):
        d = pdate(r.get("intake_date"))
        out = []
        if d in (None, "bad"):
            age = "age not computable (V1 intake date not given)"
        else:
            days = (as_of - d).days
            age = f"{days} days since intake {fmt(d)}"
            sev = (r.get("severity") or "").lower()
            if sev and sev in windows:
                if days > windows[sev]:
                    out.append(f"V2 past your {sev} window of {windows[sev]} days by {days - windows[sev]}")
                    past += 1
                else:
                    out.append(f"inside your {sev} window ({windows[sev]} days)")
            elif windows:
                out.append("V3 severity not given or no window for it")
        if (r.get("kev") or "").lower() in YES:
            out.append("V4 marked as in the KEV catalog in your file (check the catalog entry itself, EN-081 [WF])")
        if st == "under review":
            out.append("V5 reachable and still 'under review' with no action named")
        print(f"- {r.get('id')} | {r.get('identifier')} | {r.get('component')} {r.get('version')} | severity {r.get('severity') or 'not given'} | {age} | "
              + ("; ".join(out) if out else "no flag"))
    if windows:
        print(f"Past your window: {past}")
    print(f"\nOpen, reachability not stated (V6, not aged until stated): {len(unknown)}"
          + ("".join(f"\n- {r.get('id')} | {r.get('identifier')} | {r.get('component')}" for r in unknown)))
    print(f"Open, stated not reachable (left out of the age count): {len(unreach)}")
    print(f"\nClosed items: {len(closed_rows)}")
    for r in closed_rows:
        st = (r.get("status") or "").lower()
        out = []
        if st == "patched":
            if not r.get("deployed_version"):
                ev = r.get("evidence") or "none"
                out.append(f"V7 no deployed version (evidence given: {ev}); a merged change is not deployment: reopen per the old rule, owner to confirm")
            elif r.get("fixed_version") and r.get("deployed_version") != r.get("fixed_version"):
                out.append(f"V7 deployed {r.get('deployed_version')} differs from fixed version {r.get('fixed_version')}")
            else:
                dd = pdate(r.get('deployed_on'))
                out.append(f"deployed {r.get('deployed_version')} on " + (fmt(dd) if dd not in (None, 'bad') else 'date not given'))
        elif st == "accepted":
            exp = pdate(r.get("acceptance_expires"))
            if not r.get("acceptor"):
                out.append("V8 acceptance has no named acceptor")
            if exp is None:
                out.append("V8 acceptance has no expiry date")
            elif exp != "bad" and exp < as_of:
                out.append(f"V8 acceptance expired {fmt(exp)}")
            elif exp != "bad":
                out.append(f"acceptance by {r.get('acceptor') or 'not named'} runs to {fmt(exp)}")
        elif st == "mitigated":
            out.append("mitigation named: " + (r.get("evidence") or "V7 no evidence given"))
        print(f"- {r.get('id')} | {r.get('identifier')} | {st} | " + "; ".join(out))
    print("\nRepeat failure classes (open plus closed" + (f" with intake on or after {fmt(since)}" if since and since != "bad" else ", all dates") + "):")
    counts = {}
    for r in rows:
        d = pdate(r.get("intake_date"))
        if since and since != "bad" and d not in (None, "bad") and d < since:
            continue
        c = r.get("failure_class") or "class not given"
        reach = (r.get("reachable") or "").lower() == "yes"
        counts.setdefault(c, [0, 0])
        counts[c][0] += 1
        counts[c][1] += 1 if reach else 0
    for c, (n, nr) in sorted(counts.items(), key=lambda x: (-x[1][1], -x[1][0])):
        print(f"  {c}: {n} items, {nr} reachable")
    top = max(counts.items(), key=lambda x: (x[1][1], x[1][0])) if counts else None
    if top:
        ties = [c for c, v in counts.items() if v[1] == top[1][1] and c != top[0]]
        print(f"Class with the most reachable items: {top[0]} ({top[1][1]})" + (f"; tied with {', '.join(ties)}" if ties else ""))
    print("V9: severity, reachability and windows are the person's; the script counts against them and never sets them.")


# ---------------------------------------------------------------- consent
def cmd_consent(a):
    purposes = read_csv(a.purposes)
    proc = read_csv(a.processing)
    text = {}
    for p in purposes:
        key = p.get("purpose", "").lower()
        text.setdefault(key, {"classes": set(), "recipients": set()})
        text[key]["classes"].update(x.strip().lower() for x in re.split(r"[;,]", p.get("data_class", "")) if x.strip())
        text[key]["recipients"].update(x.strip().lower() for x in re.split(r"[;,]", p.get("recipients", "")) if x.strip())
    print(f"Purposes in the consent text: {len(purposes)}; processing steps listed: {len(proc)}")
    tally = {"described": 0, "broader than described": 0, "missing from the text": 0}
    for s in proc:
        pk = s.get("purpose", "").lower()
        dc = s.get("data_class", "").lower()
        rc = s.get("recipient", "").lower()
        if pk not in text:
            res = "missing from the text"
            why = "P3 purpose not in the consent text"
        else:
            why = []
            if dc and dc not in text[pk]["classes"]:
                why.append(f"P2 data class '{s.get('data_class')}' not named for this purpose")
            if rc and rc not in text[pk]["recipients"] and rc not in {"internal", "none", ""}:
                why.append(f"P2 recipient '{s.get('recipient')}' not named for this purpose")
            res = "broader than described" if why else "described"
            why = "; ".join(why) if why else "no flag"
        tally[res] += 1
        print(f"- {s.get('step')} | purpose {s.get('purpose')} | {s.get('data_class')} -> {s.get('recipient') or 'internal'} | {res} | {why}")
    print("Totals: " + ", ".join(f"{k} {v}" for k, v in tally.items()))
    if a.withdrawal:
        rows = read_csv(a.withdrawal)
        print(f"\nWithdrawal test rows: {len(rows)}")
        envs = {r.get("test_env", "").lower() for r in rows}
        if any(e in {"production", "prod"} for e in envs):
            print("W2 test run in production (the old rule runs it in a non-production environment)")
        for r in rows:
            should = (r.get("should_stop") or "").lower() in YES
            ran = (r.get("ran_after_withdrawal") or "").lower()
            if ran == "":
                res = "W3 result not recorded"
            elif should and ran in YES:
                res = "W1 still ran after withdrawal although it should have stopped"
            elif should:
                res = "stopped as promised"
            else:
                res = "not expected to stop (your file)" + (", ran" if ran in YES else "")
            td = pdate(r.get('test_date'))
            print(f"- {r.get('job')} | test {fmt(td) if td not in (None, 'bad') else 'date not given'} in {r.get('test_env') or 'environment not given'} | {res}")
    print("Whether a broader step is lawful, and which owner changes first, are the person's calls.")


# ---------------------------------------------------------------- words
def strip_calls_and_cols(text):
    out, skip, drop_idx = [], False, None
    for ln in text.splitlines():
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
    body = strip_calls_and_cols(open(a.answer, encoding="utf-8").read())
    n = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.\-/%]*", body))
    print(f"Words counted: {n} (cap {CAP}; calls list and Source and Rows columns left out)")
    print("within the short-mode cap" if n <= CAP else
          f"over the cap by {n - CAP}: cut context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the question; never a gap, a stop or the record line")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("controls"); s.add_argument("--file", required=True); s.set_defaults(f=cmd_controls)
    s = sub.add_parser("vulns"); s.add_argument("--file", required=True); s.add_argument("--as-of", required=True)
    s.add_argument("--windows"); s.add_argument("--since"); s.set_defaults(f=cmd_vulns)
    s = sub.add_parser("consent"); s.add_argument("--purposes", required=True); s.add_argument("--processing", required=True)
    s.add_argument("--withdrawal"); s.set_defaults(f=cmd_consent)
    s = sub.add_parser("words"); s.add_argument("answer"); s.set_defaults(f=cmd_words)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
