#!/usr/bin/env python3
"""Helper for interoperability-and-ehr-integration (dh-technology).

Checks the person's own FHIR payloads, SMART scopes, token responses and code maps
against the person's own check sheet and the sourced rules. It never decides
conformance for a guide it was not given, never sets a pass rule, and never says
an integration is certified or ready. Use synthetic or de-identified sandbox data
only.

  resources   python3 fhir_check.py resources --sheet SHEET.json PAYLOAD.json [...]
              SHEET (the person's, built from the guide they chose):
              {"guide": "...", "version": "...", "profiles": {"Observation": [
                {"path": "code.coding.system", "min": 1, "system": "http://loinc.org",
                 "blocks_go_live": "yes|no|not given"}]}}
              A check fails if fewer than `min` values exist at `path`, or if
              `system` is given and no value at `path` equals it. Resource types with
              no sheet entry are listed as "not checked", never as conformant.
              Valid JSON is not conformance (old task DH-04.01.1.1.3).
  scopes      python3 fhir_check.py scopes --scopes "patient/Observation.rs launch/patient"
              [--user-facing yes|no] [--screens SCREENS.csv]
              SMART v2 suffixes are an ordered subset of c r u d s (EN-138);
              v1 .read maps to .rs and .write to .cud (EN-138); system/ scopes are for
              backend services with no user (EN-139). SCREENS.csv columns: screen,
              resource, interaction, write_back. Flags scopes no screen uses and
              screens with no scope.
  capability  python3 fhir_check.py capability CAPABILITYSTATEMENT.json
              Prints fhirVersion beside 4.0.1 (ONC certification, EN-133) and 5.0.0
              (HL7 current, EN-129), and the implementation guides it declares.
  token       python3 fhir_check.py token TOKEN.json --need patient,encounter,fhirUser
              Reads a sandbox token response the person saved; reports which context
              fields are present (top level, or claims in an unverified id_token
              payload), the scopes granted, and whether a refresh token was issued.
              A login page is not a SMART launch (old task DH-04.01.2.1.3).
  map         python3 fhir_check.py map MAP.csv [--labels equal,wider,narrower,unmatched]
              Columns: source_system, source_code, source_display, target_system,
              target_code, equivalence, map_version, terminology_version, status
              (production | hold). Flags: K1 unmatched or empty target in production;
              K2 map or terminology version missing; K3 label outside the person's
              list; K4 uncoded source mapped to a code (method needed); K5 duplicate
              source code with different targets in production.
  words       python3 fhir_check.py words ANSWER.md
              Counts a short answer without the "Calls made" block (up to the record
              block, which is counted) and without Source and Rows columns.
"""
import argparse
import base64
import csv
import json
import re
import sys
from collections import Counter, defaultdict

CAP = 450
CERT_FHIR = "4.0.1"   # 45 CFR 170.215, EN-133
CURRENT_FHIR = "5.0.0"  # HL7 current publication, EN-129


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


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


def cmd_resources(a):
    sheet = load_json(a.sheet)
    profiles = sheet.get("profiles", {})
    print(f"Check sheet: {sheet.get('guide', 'guide not given')} {sheet.get('version', 'version not given')} "
          f"(the person's sheet; the model does not supply must-support lists)")
    fails, checked, unchecked = [], Counter(), Counter()
    per_type = defaultdict(lambda: [0, 0])
    for p in a.payloads:
        for r in resources_in(load_json(p)):
            rt, rid = r.get("resourceType"), r.get("id", "no id")
            if rt not in profiles:
                unchecked[rt] += 1
                continue
            checked[rt] += 1
            for c in profiles[rt]:
                path = c["path"]
                vals = [v for v in values_at(r, path.split(".")) if v not in ("", None)]
                need = int(c.get("min", 0))
                per_type[rt][0] += 1
                problem = None
                if len(vals) < need:
                    problem = f"missing: {len(vals)} value(s), sheet min {need}"
                elif c.get("system") and vals and c["system"] not in vals:
                    problem = f"binding: found {sorted(set(map(str, vals)))}, sheet system {c['system']}"
                elif c.get("system") and not vals and need == 0:
                    problem = None
                if problem:
                    per_type[rt][1] += 1
                    fails.append((p, rt, rid, path, problem, c.get("blocks_go_live", "not given")))
    print("\nChecked resources by type:")
    for rt, n in sorted(checked.items()):
        total, failed = per_type[rt]
        print(f"  {rt}: {n} resource(s), {total} check(s), {failed} failed")
    if unchecked:
        print("Not checked (no sheet entry; not conformant, not failed):")
        for rt, n in sorted(unchecked.items()):
            print(f"  {rt}: {n}")
    print(f"\nGap record ({len(fails)} miss(es)); blocks go-live is the person's flag:")
    print("| Payload | Resource | Element path | Result | Blocks go-live |")
    print("|---|---|---|---|---|")
    for p, rt, rid, path, prob, blk in fails:
        print(f"| {p.split('/')[-1]} | {rt}/{rid} | {path} | {prob} | {blk} |")
    if not fails:
        print("No miss against the sheet's checks. This says nothing about elements the sheet does not list.")
    return 0


def parse_scope(s):
    m = re.fullmatch(r"(patient|user|system)/([A-Za-z*]+)\.([A-Za-z*]+)(\?.*)?", s)
    return m.groups() if m else None


def cmd_scopes(a):
    scopes = a.scopes.split()
    used = set()
    screens = []
    if a.screens:
        with open(a.screens, encoding="utf-8", newline="") as f:
            screens = list(csv.DictReader(f))
    print("| Scope | Level | Resource | Permissions | Note (rows) |")
    print("|---|---|---|---|---|")
    for s in scopes:
        p = parse_scope(s)
        if not p:
            note = "launch or identity scope" if s.startswith("launch") or s in ("openid", "fhirUser", "offline_access", "online_access", "profile") else "not a SMART resource scope pattern; check"
            print(f"| {s} | | | | {note} |")
            continue
        level, res, perm, _ = p
        notes = []
        if perm in ("read", "write", "*"):
            v2 = {"read": ".rs", "write": ".cud", "*": ".cruds"}[perm]
            notes.append(f"SMART v1 syntax; v2 equivalent {v2} (EN-138)")
        else:
            order = "cruds"
            idx = [order.find(ch) for ch in perm]
            if -1 in idx or idx != sorted(idx) or len(set(perm)) != len(perm):
                notes.append("suffix is not an ordered subset of c r u d s (EN-138)")
        if level == "system" and a.user_facing == "yes":
            notes.append("system/ is for backend services with no user (EN-139); the app launches as a user")
        if res == "*":
            notes.append("all resource types requested; check each screen needs it")
        used.add(res)
        print(f"| {s} | {level} | {res} | {perm} | {'; '.join(notes) or 'syntax fits EN-138'} |")
    if screens:
        need = {r.get("resource", "").strip() for r in screens if r.get("resource", "").strip()}
        local = [r["screen"] for r in screens if not r.get("resource", "").strip()]
        extra = sorted(u for u in used if u != "*" and u not in need)
        missing = sorted(n for n in need if n not in used and "*" not in used)
        print(f"\nScopes no screen uses: {', '.join(extra) or 'none'}")
        print(f"Screens whose resource has no scope: {', '.join(missing) or 'none'}")
        print(f"Local-only screens (no FHIR call; not to be described as integrated): {', '.join(local) or 'none'}")
        wb = [r["screen"] for r in screens if r.get("write_back", "").lower() == "yes" and r.get("interaction", "").lower() in ("read", "search")]
        if wb:
            print(f"Write-back claimed on a read-only interaction: {', '.join(wb)}")
    return 0


def cmd_capability(a):
    cs = load_json(a.file)
    v = cs.get("fhirVersion", "not stated")
    print(f"fhirVersion declared: {v}")
    print(f"  ONC certification API base: {CERT_FHIR} (45 CFR 170.215, EN-133); match: {'yes' if v == CERT_FHIR else 'no'}")
    print(f"  HL7 current publication: {CURRENT_FHIR} (EN-129); the current publication is not a certification requirement")
    igs = cs.get("implementationGuide") or []
    print(f"Implementation guides declared: {', '.join(igs) if igs else 'none declared'}")
    print("  US Core for certification: 6.1.0 (EN-134); HL7 current: 9.0.0 (EN-132)")
    return 0


def jwt_claims(tok):
    try:
        part = tok.split(".")[1]
        part += "=" * (-len(part) % 4)
        return json.loads(base64.urlsafe_b64decode(part))
    except Exception:
        return {}


def cmd_token(a):
    t = load_json(a.file)
    claims = jwt_claims(t["id_token"]) if isinstance(t.get("id_token"), str) else {}
    print("Token response (sandbox, saved by the person). id_token claims read without signature verification.")
    for field in [f.strip() for f in a.need.split(",") if f.strip()]:
        where = "top level" if t.get(field) else ("id_token" if claims.get(field) else None)
        print(f"  {field}: {'present (' + where + ')' if where else 'MISSING'}")
    print(f"  scope granted: {t.get('scope', 'not stated')}")
    print(f"  refresh token issued: {'yes' if t.get('refresh_token') else 'no'}")
    print(f"  expires_in: {t.get('expires_in', 'not stated')}")
    if "access_token" not in t:
        print("  no access_token: this is not a completed SMART launch")
    return 0


def cmd_map(a):
    labels = [x.strip() for x in a.labels.split(",")]
    with open(a.file, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    flags = []
    eq = Counter()
    seen = defaultdict(set)
    hold = 0
    for i, r in enumerate(rows, start=2):
        status = (r.get("status") or "").strip().lower()
        e = (r.get("equivalence") or "").strip().lower()
        eq[e or "blank"] += 1
        src = (r.get("source_code") or "").strip()
        tgt = (r.get("target_code") or "").strip()
        if status == "hold":
            hold += 1
        if status == "production" and (e == "unmatched" or not tgt):
            flags.append((i, "K1", f"{src or 'uncoded'}: unmatched or no target in the production map"))
        if not (r.get("map_version") or "").strip() or not (r.get("terminology_version") or "").strip():
            flags.append((i, "K2", f"{src or 'uncoded'}: map or terminology version missing"))
        if e and e not in labels:
            flags.append((i, "K3", f"{src or 'uncoded'}: label '{e}' outside your list {labels}"))
        if not src and tgt:
            flags.append((i, "K4", f"uncoded source '{r.get('source_display', '')}' mapped to {tgt}: method needed"))
        if status == "production" and src:
            seen[(r.get("source_system"), src)].add(tgt)
    for (sys_, src), tg in seen.items():
        if len(tg) > 1:
            flags.append(("-", "K5", f"{src} ({sys_}) maps to {sorted(tg)} in production"))
    print(f"{len(rows)} map rows; on hold: {hold}; labels: {dict(eq)}")
    print("| Line | Flag | Fact |")
    print("|---|---|---|")
    for line, fl, fact in flags:
        print(f"| {line} | {fl} | {fact} |")
    if not flags:
        print("No flag. Equivalence labels are the person's; the script does not judge them.")
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
    r = sub.add_parser("resources")
    r.add_argument("--sheet", required=True)
    r.add_argument("payloads", nargs="+")
    s = sub.add_parser("scopes")
    s.add_argument("--scopes", required=True)
    s.add_argument("--user-facing", default="yes", choices=["yes", "no"])
    s.add_argument("--screens")
    c = sub.add_parser("capability")
    c.add_argument("file")
    t = sub.add_parser("token")
    t.add_argument("file")
    t.add_argument("--need", default="patient,encounter,fhirUser")
    m = sub.add_parser("map")
    m.add_argument("file")
    m.add_argument("--labels", default="equal,wider,narrower,unmatched")
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"resources": cmd_resources, "scopes": cmd_scopes, "capability": cmd_capability,
            "token": cmd_token, "map": cmd_map, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
