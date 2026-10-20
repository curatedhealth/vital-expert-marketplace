#!/usr/bin/env python3
"""Trial operations metrics by site, and disclosure clocks, from the person's own files.

Two subcommands.

1) sites: enrollment, retention, protocol deviations and data completeness by site.

   python3 trial_ops_metrics.py sites PARTICIPANTS.csv [--targets TARGETS.csv]
          [--as-of YYYY-MM-DD] [--rules RULES.json] [--json]

   PARTICIPANTS.csv, either
   (a) one row per participant (pseudonymous id only, never names):
       site, participant_id, arm, enrolled_on, status, deviations, important_deviations,
       expected_assessments, received_assessments
       status: active, completed, withdrawn or lost_to_follow_up
   or (b) one row per site (aggregates):
       site, enrolled, active, completed, withdrawn, lost_to_follow_up, deviations,
       important_deviations, expected_assessments, received_assessments
   Lines starting with "#" are ignored.

   TARGETS.csv (optional, the person's numbers): site, enrollment_target, activated_on

   RULES.json (optional, the person's rules, checked as written):
       [{"metric": "retention_pct", "op": ">=", "value": 85, "scope": "site",
         "owner": "Clinical Ops", "text": "person's own words"}]
   metrics: enrollment_pct_of_target, retention_pct, completeness_pct,
            important_deviations_per_participant, deviations_per_participant,
            completeness_gap_between_arms_pts
   scope: "site" (each site) or "all" (trial total). op: >=, >, <=, <, ==

   Definitions (references/execution-metrics.md):
     retention_pct = (active + completed) / enrolled x 100
     completeness_pct = received_assessments / expected_assessments x 100
     deviations_per_participant = deviations / enrolled
     enrollment_pct_of_target = enrolled / enrollment_target x 100 (target is the person's)
     enrollment_per_month = enrolled / months from activated_on to as-of (30.44-day months)
     completeness_gap_between_arms_pts = highest minus lowest arm completeness, in points

2) clocks: registration and results clocks from dates the person gives.

   python3 trial_ops_metrics.py clocks TRIAL.json [--json]

   TRIAL.json keys (all optional except as_of):
     as_of, first_consent, first_enrollment, registration_submitted,
     us_applicable_clinical_trial (true/false), initiated_on_or_after_2017_01_18 (true/false),
     last_registration_update, recruitment_status_changed_on, recruitment_status_updated_on,
     primary_completion, us_results_submitted, us_delay_certification_submitted,
     eu_end_of_trial_by_member_state {"DE": "YYYY-MM-DD", ...},
     eu_end_notified_by_member_state {"DE": "YYYY-MM-DD", ...},
     eu_end_of_trial_all_member_states, eu_results_summary_submitted,
     publication_date

   Each clock prints its due date, the as-of position and the row id of the rule. The
   script states dates; it does not decide whether a rule applies to the trial (for example,
   whether it is an applicable clinical trial): the owner the person names for registration does.
"""
import csv
import datetime as dt
import json
import sys

OPS = {">=": lambda a, b: a >= b, ">": lambda a, b: a > b, "<=": lambda a, b: a <= b,
       "<": lambda a, b: a < b, "==": lambda a, b: a == b}


def d(s):
    return dt.date.fromisoformat(s) if s else None


def add_years(day, n):
    try:
        return day.replace(year=day.year + n)
    except ValueError:  # 29 February
        return day.replace(year=day.year + n, day=28)


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        lines = [ln for ln in f if not ln.lstrip().startswith("#")]
    return [{(k or "").strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(lines)]


def num(v):
    return float(v) if v not in (None, "") else 0.0


def pct(a, b):
    return round(100.0 * a / b, 1) if b else None


def aggregate(rows):
    sites = {}
    participant_level = "participant_id" in rows[0]
    for r in rows:
        s = sites.setdefault(r["site"], {"enrolled": 0, "active": 0, "completed": 0, "withdrawn": 0,
                                         "lost_to_follow_up": 0, "deviations": 0, "important_deviations": 0,
                                         "expected": 0, "received": 0, "arms": {}})
        if participant_level:
            s["enrolled"] += 1
            st = r.get("status", "").lower()
            if st in ("active", "completed", "withdrawn", "lost_to_follow_up"):
                s[st] += 1
            else:
                s.setdefault("status_unknown", 0)
                s["status_unknown"] += 1
            exp, rec = num(r.get("expected_assessments")), num(r.get("received_assessments"))
            arm = r.get("arm") or "[GAP]"
            a = s["arms"].setdefault(arm, [0, 0])
            a[0] += exp
            a[1] += rec
        else:
            for k in ("enrolled", "active", "completed", "withdrawn", "lost_to_follow_up"):
                s[k] += int(num(r.get(k)))
            exp, rec = num(r.get("expected_assessments")), num(r.get("received_assessments"))
        s["deviations"] += int(num(r.get("deviations")))
        s["important_deviations"] += int(num(r.get("important_deviations")))
        s["expected"] += exp
        s["received"] += rec
    return sites, participant_level


def metrics(s, target=None, activated=None, as_of=None):
    m = {"enrolled": s["enrolled"], "withdrawn": s["withdrawn"], "lost_to_follow_up": s["lost_to_follow_up"],
         "retention_pct": pct(s["active"] + s["completed"], s["enrolled"]),
         "deviations": s["deviations"], "important_deviations": s["important_deviations"],
         "deviations_per_participant": round(s["deviations"] / s["enrolled"], 2) if s["enrolled"] else None,
         "important_deviations_per_participant": round(s["important_deviations"] / s["enrolled"], 2) if s["enrolled"] else None,
         "completeness_pct": pct(s["received"], s["expected"]),
         "status_unknown": s.get("status_unknown", 0)}
    arms = {k: pct(v[1], v[0]) for k, v in s.get("arms", {}).items() if v[0]}
    m["completeness_by_arm_pct"] = arms
    m["completeness_gap_between_arms_pts"] = round(max(arms.values()) - min(arms.values()), 1) if len(arms) > 1 else None
    m["enrollment_target"] = target
    m["enrollment_pct_of_target"] = pct(s["enrolled"], target) if target else None
    if activated and as_of and as_of > activated:
        months = (as_of - activated).days / 30.44
        m["months_active"] = round(months, 1)
        m["enrollment_per_month"] = round(s["enrolled"] / months, 2)
    return m


def check_rules(rules, per_site, total):
    out = []
    for rule in rules:
        targets = [("All sites", total)] if rule.get("scope") == "all" else sorted(per_site.items())
        for name, m in targets:
            v = m.get(rule["metric"])
            if v is None:
                res = "not measurable [GAP]"
            else:
                res = "pass" if OPS[rule["op"]](v, rule["value"]) else "miss"
            out.append({"site": name, "rule": rule.get("text") or "%s %s %s" % (rule["metric"], rule["op"], rule["value"]),
                        "metric": rule["metric"], "value": v, "result": res,
                        "owner": rule.get("owner") or "owner not named"})
    return out


def cmd_sites(argv):
    path = argv[0]
    as_json = "--json" in argv
    rest = [a for a in argv[1:] if a != "--json"]
    opts = dict(zip(rest[0::2], rest[1::2]))
    rows = read_csv(path)
    sites, participant_level = aggregate(rows)
    targets = {}
    if "--targets" in opts:
        for t in read_csv(opts["--targets"]):
            targets[t["site"]] = (int(num(t.get("enrollment_target"))) or None, d(t.get("activated_on")))
    as_of = d(opts.get("--as-of"))
    per_site = {}
    for name, s in sites.items():
        tg, act = targets.get(name, (None, None))
        per_site[name] = metrics(s, tg, act, as_of)
    tot = {"enrolled": 0, "active": 0, "completed": 0, "withdrawn": 0, "lost_to_follow_up": 0,
           "deviations": 0, "important_deviations": 0, "expected": 0, "received": 0, "arms": {}}
    for s in sites.values():
        for k in ("enrolled", "active", "completed", "withdrawn", "lost_to_follow_up", "deviations",
                  "important_deviations", "expected", "received"):
            tot[k] += s[k]
        tot["status_unknown"] = tot.get("status_unknown", 0) + s.get("status_unknown", 0)
        for arm, v in s.get("arms", {}).items():
            a = tot["arms"].setdefault(arm, [0, 0])
            a[0] += v[0]
            a[1] += v[1]
    all_target = sum(t[0] for t in targets.values() if t[0]) or None
    total = metrics(tot, all_target)
    rule_results = check_rules(json.load(open(opts["--rules"])), per_site, total) if "--rules" in opts else []
    result = {"input": path, "participant_level": participant_level, "as_of": str(as_of) if as_of else None,
              "by_site": per_site, "all_sites": total, "rules": rule_results}
    if as_json:
        print(json.dumps(result, indent=2))
        return 0
    print("# Trial execution metrics by site\n")
    print("Input: %s (%s). As of: %s. Targets and rules are the person's; no verdict without a rule.\n"
          % (path, "one row per participant" if participant_level else "one row per site", result["as_of"] or "[GAP] not given"))
    print("| Site | Enrolled | Target | % of target | Per month | Retention % | Withdrawn | Lost | Deviations (important) | Dev. per participant | Completeness % | Completeness by arm % |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for name in sorted(per_site) + ["All sites"]:
        m = per_site.get(name, total)
        arms = "; ".join("%s %s" % (k, v) for k, v in sorted(m["completeness_by_arm_pct"].items())) or "n/a"
        print("| %s | %d | %s | %s | %s | %s | %d | %d | %d (%d) | %s | %s | %s |" % (
            name, m["enrolled"], m["enrollment_target"] or "[GAP]", m["enrollment_pct_of_target"] or "[GAP]",
            m.get("enrollment_per_month", "[GAP]"), m["retention_pct"], m["withdrawn"], m["lost_to_follow_up"],
            m["deviations"], m["important_deviations"], m["deviations_per_participant"], m["completeness_pct"], arms))
    if total.get("status_unknown"):
        print("\nRows with a status outside active, completed, withdrawn, lost_to_follow_up: %d (counted as enrolled, not retained)." % total["status_unknown"])
    if rule_results:
        print("\n## Your rules\n")
        print("| Site | Rule (your words) | Value | Result | Owner |")
        print("|---|---|---|---|---|")
        for r in rule_results:
            print("| %s | %s | %s | %s | %s |" % (r["site"], r["rule"], r["value"], r["result"], r["owner"]))
    return 0


def clock_line(name, due, done, as_of, row, note=""):
    if due is None:
        return {"clock": name, "due": "[GAP] start date not given", "status": "not computable", "row": row, "note": note}
    if done:
        status = "submitted %s (%s)" % (done, "on or before the date" if done <= due else "%d days after the date" % (done - due).days)
    elif as_of > due:
        status = "not recorded as submitted; date passed %d days before as-of" % (as_of - due).days
    else:
        status = "not yet due; %d days from as-of" % (due - as_of).days
    return {"clock": name, "due": str(due), "status": status, "row": row, "note": note}


def cmd_clocks(argv):
    t = json.load(open(argv[0]))
    as_of = d(t["as_of"])
    out = []
    fc, fe, reg = d(t.get("first_consent")), d(t.get("first_enrollment")), d(t.get("registration_submitted"))
    if fc or reg:
        out.append(clock_line("ICMJE: registration at or before first patient consent", fc, reg, as_of, "CV132"))
    if t.get("us_applicable_clinical_trial"):
        out.append(clock_line("US 42 CFR 11.24: registration within 21 calendar days after first enrollment",
                              fe + dt.timedelta(days=21) if fe else None, reg, as_of, "CV141"))
        pc = d(t.get("primary_completion"))
        note = ""
        if t.get("us_delay_certification_submitted"):
            cert = d(t["us_delay_certification_submitted"])
            note = ("Delay certification submitted %s: results due 30 days after approval, clearance or 210-day withdrawal, "
                    "and no later than %s (CV146)." % (cert, add_years(cert, 2)))
        out.append(clock_line("US 42 CFR 11.44(a): results no later than 1 year after primary completion date",
                              add_years(pc, 1) if pc else None, d(t.get("us_results_submitted")), as_of, "CV145", note))
        if t.get("initiated_on_or_after_2017_01_18", True):
            lu = d(t.get("last_registration_update"))
            out.append(clock_line("US 42 CFR 11.64: registration information updated at least every 12 months",
                                  add_years(lu, 1) if lu else None, None, as_of, "CV149"))
            rc = d(t.get("recruitment_status_changed_on"))
            if rc:
                out.append(clock_line("US 42 CFR 11.64: recruitment status updated within 30 days of a change",
                                      rc + dt.timedelta(days=30), d(t.get("recruitment_status_updated_on")), as_of, "CV149"))
    for ms, end in (t.get("eu_end_of_trial_by_member_state") or {}).items():
        out.append(clock_line("EU CTR Art 37: end-of-trial notification in %s within 15 days" % ms,
                              d(end) + dt.timedelta(days=15), d((t.get("eu_end_notified_by_member_state") or {}).get(ms)),
                              as_of, "CV151", "Applies to trials under Regulation (EU) No 536/2014 (CVB7)."))
    eu_all = d(t.get("eu_end_of_trial_all_member_states"))
    if eu_all:
        out.append(clock_line("EU CTR Art 37(4): results summary and lay summary within 1 year of end of trial in all Member States",
                              add_years(eu_all, 1), d(t.get("eu_results_summary_submitted")), as_of, "CV152",
                              "Applies to trials under Regulation (EU) No 536/2014 (CVB7)."))
    pc = d(t.get("primary_completion"))
    if pc:
        out.append(clock_line("WHO joint statement (funder pledge, not law): summary results within 12 months of primary completion",
                              add_years(pc, 1), d(t.get("us_results_submitted")) or d(t.get("eu_results_summary_submitted")), as_of, "CV140"))
        out.append(clock_line("WHO joint statement (indicative): journal publication within 24 months of study completion",
                              add_years(pc, 2), d(t.get("publication_date")), as_of, "CV140",
                              "The statement anchors publication to study completion; primary completion used here as given."))
    if "--json" in argv:
        print(json.dumps({"as_of": str(as_of), "clocks": out}, indent=2))
        return 0
    print("# Registration and results clocks\n")
    print("As of %s. Dates are the person's; whether each rule applies is the call of the owner the person names for registration, or owner not named.\n" % as_of)
    print("| Clock | Date | Position at as-of | Row | Note |")
    print("|---|---|---|---|---|")
    for c in out:
        print("| %s | %s | %s | %s | %s |" % (c["clock"], c["due"], c["status"], c["row"], c["note"]))
    return 0


def main(argv):
    if len(argv) < 3 or argv[1] not in ("sites", "clocks"):
        print(__doc__)
        return 2
    return cmd_sites(argv[2:]) if argv[1] == "sites" else cmd_clocks(argv[2:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
