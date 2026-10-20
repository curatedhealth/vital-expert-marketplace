#!/usr/bin/env python3
"""Helper for integration-quality-monitoring (dh-technology).

Reads the person's own sample exchanges, launch matrix, map review sample and
workflow observations, and prints facts against the person's own check sheet,
pass rules and ceilings. It never sets a threshold, a pass rule, an owner or a
release, never averages a failing profile away, and never says an integration is
reliable, conformant or ready. Synthetic or de-identified sandbox data only.

  score      python3 integration_check.py score --sheet SHEET.json PAYLOAD.json [...]
             SHEET as in interoperability-and-ehr-integration: {"guide", "version",
             "profiles": {Type: [{"path", "min", "system", "blocks_go_live"}]}}.
             Prints pass or fail per check per payload, a score by profile with the
             failing payload and resource ids, and flags a profile that failed in
             every sample (S1), a profile with one sample only (S2), and resource
             types with no sheet entry (S3, not checked).
  launch     python3 integration_check.py launch MATRIX.csv [--token-ms N] [--read-ms N]
             Columns: cell_id, role, patient_state, encounter_state, scope_requested,
             http_status, context_needed (";"-separated), context_present,
             writeback_expected (yes|no), writeback_visible (yes|no|not run),
             token_ms, first_read_ms, mocked_token (yes|no), run_on, sandbox.
             The latency ceilings are the person's; without them latency is reported,
             not judged. Flags: L1 HTTP status not 2xx; L2 context field missing;
             L3 write-back expected, not visible; L4 latency over the person's
             ceiling; L5 mocked token (not an EHR launch); L6 cell not run;
             L7 only one cell (a single happy path is not a matrix).
  mapsample  python3 integration_check.py mapsample SAMPLE.csv --exact-labels equal
             [--max-unmatched R] [--min-exact R]
             Columns: row_id, map_version, code_system, source_code, target_code,
             mapper_label, mapper_id, reviewer_id, reviewer_blinded (yes|no),
             reviewer_accepts (yes|no|not reviewed), error_class, sampled_how.
             Exact-match rate = rows with a mapper label in --exact-labels that the
             reviewer accepted, over reviewed rows; unmatched rate = rows labeled
             unmatched over all sampled rows (the old task's two rates; the person
             may define them differently). Thresholds only if the person passes
             them. Flags: R1 reviewer is the mapper; R2 reviewer not blinded;
             R3 disagreement (reviewer rejects); R4 sample drawn from rows already
             hand-checked (sampled_how says so).
  workflow   python3 integration_check.py workflow OBS.csv
             Columns: obs_id, site, step, designed_action, observed (done|skipped|
             replaced), workaround, seconds, observed_on.
             Per designed action: done, skipped, replaced; workarounds quoted;
             time range with the number of observations (no mean from one: W1).
  words      python3 integration_check.py words ANSWER.md
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict

CAP = 450


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def resources_in(obj):
    if isinstance(obj, list):
        for x in obj:
            yield from resources_in(x)
    elif isinstance(obj, dict):
        if obj.get("resourceType") == "Bundle":
            for e in obj.get("entry", []) or []:
                if isinstance(e, dict) and isinstance(e.get("resource"), dict):
                    yield e["resource"]
        elif "resourceType" in obj:
            yield obj


def values_at(node, parts):
    if not parts:
        if node is None:
            return []
        return node if isinstance(node, list) else [node]
    if isinstance(node, list):
        out = []
        for n in node:
            out.extend(values_at(n, parts))
        return out
    if not isinstance(node, dict):
        return []
    return values_at(node.get(parts[0]), parts[1:])


def cmd_score(a):
    sheet = load_json(a.sheet)
    profiles = sheet.get("profiles", {})
    print(f"Check sheet: {sheet.get('guide', 'guide not given')} {sheet.get('version', 'version not given')} (the person's)")
    samples = defaultdict(list)   # type -> [(payload, rid, failed_paths)]
    unchecked = Counter()
    for p in a.payloads:
        name = p.split("/")[-1]
        for r in resources_in(load_json(p)):
            rt = r.get("resourceType")
            if rt not in profiles:
                unchecked[rt] += 1
                continue
            failed = []
            for c in profiles[rt]:
                vals = [v for v in values_at(r, c["path"].split(".")) if v not in ("", None)]
                if len(vals) < int(c.get("min", 0)):
                    failed.append(f"{c['path']} missing")
                elif c.get("system") and vals and c["system"] not in vals:
                    failed.append(f"{c['path']} binding")
            samples[rt].append((name, r.get("id", "no id"), failed))
    print("| Profile | Samples | Samples with a miss | Failing payload / resource: element | Flags |")
    print("|---|---|---|---|---|")
    for rt in sorted(samples):
        s = samples[rt]
        bad = [x for x in s if x[2]]
        flags = []
        if bad and len(bad) == len(s):
            flags.append("S1 failed in every sample")
        if len(s) == 1:
            flags.append("S2 one sample only")
        detail = "; ".join(f"{n} / {rt}/{rid}: {', '.join(f)}" for n, rid, f in bad) or "none"
        print(f"| {rt} | {len(s)} | {len(bad)} | {detail} | {'; '.join(flags) or ''} |")
    for rt, n in sorted(unchecked.items()):
        print(f"| {rt} | {n} | not checked | no sheet entry | S3 not checked (not conformant, not failed) |")
    return 0


def cmd_launch(a):
    rs = rows(a.file)
    fmt = lambda v: f"{v:g} ms" if v else "not given"
    print(f"{len(rs)} cell(s). Ceilings (the person's): token {fmt(a.token_ms)}, first read {fmt(a.read_ms)}.")
    print("| Cell | Role / patient / encounter | HTTP | Context missing | Write-back | Token ms | First read ms | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    failed = 0
    for r in rs:
        fl = []
        st = (r.get("http_status") or "").strip()
        if not st or st.lower() == "not run":
            fl.append("L6 not run")
        elif not st.startswith("2"):
            fl.append("L1 HTTP " + st)
        need = [x.strip() for x in (r.get("context_needed") or "").split(";") if x.strip()]
        have = [x.strip() for x in (r.get("context_present") or "").split(";") if x.strip()]
        miss = [x for x in need if x not in have]
        if miss and "L6 not run" not in fl:
            fl.append("L2 context missing")
        wbe = (r.get("writeback_expected") or "").lower()
        wbv = (r.get("writeback_visible") or "").lower()
        if wbe == "yes" and wbv != "yes":
            fl.append("L3 write-back not visible" + (" (not run)" if wbv == "not run" else ""))
        for key, ceil, label in (("token_ms", a.token_ms, "token"), ("first_read_ms", a.read_ms, "first read")):
            v = (r.get(key) or "").strip()
            if ceil and v and v.replace(".", "", 1).isdigit() and float(v) > ceil:
                fl.append(f"L4 {label} {v} ms over your {ceil:g} ms")
        if (r.get("mocked_token") or "").lower() == "yes":
            fl.append("L5 mocked token")
        if fl:
            failed += 1
        state = f"{r.get('role')} / {r.get('patient_state')} / {r.get('encounter_state')}"
        print(f"| {r.get('cell_id')} | {state} | {st or 'not run'} | {', '.join(miss) or 'none'} | "
              f"{wbv or 'n/a'} | {r.get('token_ms') or 'not given'} | {r.get('first_read_ms') or 'not given'} | {'; '.join(fl)} |")
    if len(rs) == 1:
        print("L7 only one cell: a single happy-path launch is not a matrix.")
    print(f"Cells with at least one flag: {failed} of {len(rs)}. A flagged cell stays failed until a later run passes it.")
    return 0


def cmd_mapsample(a):
    rs = rows(a.file)
    exact = {x.strip().lower() for x in a.exact_labels.split(",")}
    reviewed = [r for r in rs if (r.get("reviewer_accepts") or "").lower() in ("yes", "no")]
    ex = [r for r in reviewed if (r.get("mapper_label") or "").lower() in exact and r["reviewer_accepts"].lower() == "yes"]
    un = [r for r in rs if (r.get("mapper_label") or "").lower() == "unmatched"]
    dis = [r for r in reviewed if r["reviewer_accepts"].lower() == "no"]
    er = len(ex) / len(reviewed) if reviewed else None
    ur = len(un) / len(rs) if rs else None
    vers = sorted({r.get("map_version", "") for r in rs})
    print(f"Sample: {len(rs)} rows (map version(s) {', '.join(vers)}); reviewed: {len(reviewed)}")
    print(f"Exact-match rate (labels {sorted(exact)} accepted by the reviewer / reviewed rows): "
          f"{len(ex)}/{len(reviewed)} = {er:.1%}" if er is not None else "Exact-match rate: not computable (no reviewed rows)")
    print(f"Unmatched rate (labeled unmatched / sampled rows): {len(un)}/{len(rs)} = {ur:.1%}" if ur is not None else "Unmatched rate: not computable")
    if a.min_exact is not None and er is not None:
        print(f"  your minimum exact-match rate {a.min_exact:.1%}: {'met' if er >= a.min_exact else 'not met'}")
    else:
        print("  exact-match threshold: not given (no source sets one)")
    if a.max_unmatched is not None and ur is not None:
        print(f"  your maximum unmatched rate {a.max_unmatched:.1%}: {'met' if ur <= a.max_unmatched else 'not met'}")
    else:
        print("  unmatched threshold: not given (no source sets one)")
    print(f"Disagreements (reviewer rejects): {len(dis)}: {', '.join(r['row_id'] for r in dis) or 'none'}")
    fl = []
    for r in rs:
        if r.get("reviewer_id") and r.get("reviewer_id") == r.get("mapper_id"):
            fl.append(f"R1 row {r['row_id']}: reviewer is the mapper")
        if (r.get("reviewer_blinded") or "").lower() == "no":
            fl.append(f"R2 row {r['row_id']}: reviewer saw the mapper's label")
        if "hand-checked" in (r.get("sampled_how") or "").lower():
            fl.append(f"R4 row {r['row_id']}: drawn from rows already hand-checked")
    for f in fl:
        print(f)
    classes = Counter((r.get("map_version"), r.get("error_class")) for r in rs if (r.get("error_class") or "").strip())
    if classes:
        print("Error classes by map version (the class that blocks is the person's call):")
        for (v, c), n in classes.most_common():
            print(f"  {v}: {c}: {n}")
    return 0


def cmd_workflow(a):
    rs = rows(a.file)
    by = defaultdict(Counter)
    secs = defaultdict(list)
    wk = defaultdict(list)
    for r in rs:
        key = (r.get("step"), r.get("designed_action"))
        by[key][(r.get("observed") or "not recorded").lower()] += 1
        s = (r.get("seconds") or "").strip()
        if s.replace(".", "", 1).isdigit():
            secs[r.get("step")].append(float(s))
        if (r.get("workaround") or "").strip():
            wk[r.get("step")].append(f"{r.get('obs_id')} ({r.get('site')}): \"{r['workaround'].strip()}\"")
    print("| Step | Designed action | Done | Skipped | Replaced |")
    print("|---|---|---|---|---|")
    for (step, act), c in by.items():
        print(f"| {step} | {act} | {c['done']} | {c['skipped']} | {c['replaced']} |")
    for step in sorted({k[0] for k in by}):
        t = secs.get(step, [])
        if len(t) >= 2:
            print(f"{step}: time range {min(t):.0f} to {max(t):.0f} seconds over {len(t)} observations")
        elif len(t) == 1:
            print(f"{step}: one observation ({t[0]:.0f} seconds); W1 no mean or range from a single observation")
        else:
            print(f"{step}: no time recorded")
        print(f"{step}: workarounds {len(wk.get(step, []))}")
        for q in wk.get(step, []):
            print(f"  {q}")
    return 0


def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows")
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
    s = sub.add_parser("score")
    s.add_argument("--sheet", required=True)
    s.add_argument("payloads", nargs="+")
    l = sub.add_parser("launch")
    l.add_argument("file")
    l.add_argument("--token-ms", type=float)
    l.add_argument("--read-ms", type=float)
    m = sub.add_parser("mapsample")
    m.add_argument("file")
    m.add_argument("--exact-labels", default="equal")
    m.add_argument("--min-exact", type=float)
    m.add_argument("--max-unmatched", type=float)
    w = sub.add_parser("workflow")
    w.add_argument("file")
    c = sub.add_parser("words")
    c.add_argument("answer")
    a = ap.parse_args()
    return {"score": cmd_score, "launch": cmd_launch, "mapsample": cmd_mapsample,
            "workflow": cmd_workflow, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
