#!/usr/bin/env python3
"""Check a customer deployment plan for order, dependencies and the rules this skill carries.

Nothing is sent anywhere. The script never sets a date, an owner or a go-live date: it orders
and checks what the person's plan already says.

PLAN file (CSV, one row per step), columns:
  step        short unique name (for example "BAA signed", "Day-one workflow configured")
  type        agreement | access | configure | integrate | silent_mode | train | go_live |
              scale_up | other
  owner       the owner the person named (blank = "owner not named")
  depends_on  semicolon list of step names that must finish first (the person's dependencies)
  start       planned start (YYYY-MM-DD, blank = unset)
  finish      planned finish (YYYY-MM-DD, blank = unset)
  phi         yes if this step makes protected health information or personal data flow to
              the vendor (test data from real patients, live interfaces, go-live); else no

Checks:
  1. Unknown prerequisites and circular dependencies.
  2. Dependency order: a step planned to start before a prerequisite's planned finish.
  3. Training before configuration (register rule for CF-12.02.02.1.1.2: "Do not schedule
     training before the day-one workflow is configured"): a train step whose start is before
     the latest finish of the configure steps, or that does not depend on them at all.
  4. Personal data before the written agreement: a phi=yes step planned to start before every
     agreement step has finished (HIPAA business associate contract, research row CS96; GDPR
     Article 28 written contract, CS110). If the plan has phi steps and no agreement step, says so.
  5. Personal data before access is set: a phi=yes step planned to start before an access step
     finishes, or that does not depend on it (minimum necessary and role-based access; US rows
     CS103, CS104; other markets [GAP]).
  6. Steps without a named owner, and steps without dates.
Then prints the dependency order (a topological order) and the longest chain of planned
durations (the critical path), in calendar days.

Usage: python3 plan_sequence.py PLAN.csv
"""
import csv
import sys
from datetime import date


def d(s):
    s = (s or "").strip()
    return date.fromisoformat(s) if s else None


def main(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        steps = [{k.strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]
    names = [s["step"] for s in steps]
    by = {s["step"]: s for s in steps}
    deps = {s["step"]: [x.strip() for x in s.get("depends_on", "").split(";") if x.strip()] for s in steps}
    findings = []

    for s, ds in deps.items():
        for x in ds:
            if x not in by:
                findings.append(f"Unknown prerequisite: '{s}' depends on '{x}', which is not a step in the plan")

    # topological order (Kahn), keeps file order among ready steps
    indeg = {s: len([x for x in deps[s] if x in by]) for s in names}
    children = {s: [] for s in names}
    for s in names:
        for x in deps[s]:
            if x in by:
                children[x].append(s)
    ready = [s for s in names if indeg[s] == 0]
    order = []
    while ready:
        s = ready.pop(0)
        order.append(s)
        for c in children[s]:
            indeg[c] -= 1
            if indeg[c] == 0:
                ready.append(c)
    cyc = [s for s in names if s not in order]
    if cyc:
        findings.append("Circular dependency among: " + ", ".join(cyc) + " (no order exists until the person breaks the loop)")

    # 2. dependency order against planned dates
    for s in names:
        st = d(by[s].get("start"))
        for x in deps[s]:
            if x in by:
                fx = d(by[x].get("finish"))
                if st and fx and st < fx:
                    findings.append(f"Order: '{s}' starts {st.isoformat()} before its prerequisite '{x}' finishes {fx.isoformat()}")

    # ancestors for rule checks
    def ancestors(s, seen=None):
        seen = seen if seen is not None else set()
        for x in deps.get(s, []):
            if x in by and x not in seen:
                seen.add(x)
                ancestors(x, seen)
        return seen

    configure = [s for s in names if by[s].get("type") == "configure"]
    agreements = [s for s in names if by[s].get("type") == "agreement"]
    cfg_finish = max([d(by[c].get("finish")) for c in configure if d(by[c].get("finish"))], default=None)
    for s in names:
        if by[s].get("type") != "train":
            continue
        st = d(by[s].get("start"))
        if not configure:
            findings.append(f"Training rule: '{s}' is training, but the plan has no configure step; the day-one workflow configuration is not in the plan [GAP]")
            continue
        if not (set(configure) & ancestors(s)):
            findings.append(f"Training rule: '{s}' does not depend on any configure step (register rule: no training before the day-one workflow is configured)")
        if st and cfg_finish and st < cfg_finish:
            findings.append(f"Training rule: '{s}' starts {st.isoformat()} before configuration finishes {cfg_finish.isoformat()}")

    phi_steps = [s for s in names if by[s].get("phi", "").lower() == "yes"]
    if phi_steps and not agreements:
        findings.append("Data rule: steps move personal data (" + ", ".join(phi_steps) + ") but the plan has no agreement step (BAA, CS96; Article 28 contract, CS110) [GAP]")
    ag_finish = [d(by[a].get("finish")) for a in agreements]
    for s in phi_steps:
        st = d(by[s].get("start"))
        for a, fa in zip(agreements, ag_finish):
            if fa is None:
                findings.append(f"Data rule: '{s}' moves personal data and agreement '{a}' has no planned finish [GAP]")
            elif st and st < fa:
                findings.append(f"Data rule: '{s}' moves personal data from {st.isoformat()}, before agreement '{a}' is planned to be signed {fa.isoformat()}")
            if a not in ancestors(s) and s != a:
                findings.append(f"Data rule: '{s}' moves personal data but does not depend on agreement '{a}'")

    # 5. personal data before user roles and access are set
    access = [s for s in names if by[s].get("type") == "access"]
    for s in phi_steps:
        st = d(by[s].get("start"))
        for a in access:
            if s == a:
                continue
            fa = d(by[a].get("finish"))
            if st and fa and st < fa:
                findings.append(f"Access rule: '{s}' moves personal data from {st.isoformat()} before '{a}' finishes {fa.isoformat()} (minimum necessary and role-based access; US: CS103, CS104; other markets [GAP])")
            if a not in ancestors(s):
                findings.append(f"Access rule: '{s}' moves personal data but does not depend on '{a}'")

    for s in names:
        if not by[s].get("owner"):
            findings.append(f"Owner: '{s}' has no owner: owner not named")
        if not by[s].get("start") or not by[s].get("finish"):
            findings.append(f"Dates: '{s}' has no planned start or finish (unset)")

    gl = [s for s in names if by[s].get("type") == "go_live"]
    print("## Dependency order")
    for i, s in enumerate(order, 1):
        r = by[s]
        print(f"{i}. {s} [{r.get('type')}] owner: {r.get('owner') or 'owner not named'}; planned {r.get('start') or 'unset'} to {r.get('finish') or 'unset'}")
    print()
    if gl:
        print("Go-live date in the plan: " + "; ".join(f"{g}: {by[g].get('start') or 'unset'}" for g in gl))
        print()

    # critical path by planned duration (calendar days), only if no cycle
    if not cyc:
        dur = {}
        for s in names:
            a, b = d(by[s].get("start")), d(by[s].get("finish"))
            dur[s] = (b - a).days if a and b else 0
        best, prev = {}, {}
        for s in order:
            cands = [(best[x], x) for x in deps[s] if x in best]
            base, p = max(cands) if cands else (0, None)
            best[s] = base + dur[s]
            prev[s] = p
        end = max(best, key=best.get) if best else None
        chain = []
        while end:
            chain.append(end)
            end = prev[end]
        print("## Longest chain of planned durations (critical path)")
        print(" -> ".join(reversed(chain)) + f" ({max(best.values()) if best else 0} planned calendar days of work, gaps between steps not counted)")
        print()

    print("## Findings")
    if findings:
        for f in findings:
            print(f"- {f}")
    else:
        print("- None of the checks found an issue.")
    print()
    print("Dates, owners and the go-live date are the person's. This check proposes none.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
