#!/usr/bin/env python3
"""Clock table for FDA submissions and EUDAMED device registration.

Input: one JSON file, either
  A. the person's own data:
     {"as_of": "YYYY-MM-DD",
      "submissions": [{"name": str, "route": "510k" | "denovo" | "pma",
                        "submitted": "YYYY-MM-DD", "decided": "YYYY-MM-DD" (optional),
                        "sponsor_hold_days": int (optional),
                        "info_request_date": "YYYY-MM-DD" (optional, De Novo),
                        "info_response_date": "YYYY-MM-DD" (optional)}],
      "eu_devices": [{"name": str, "first_placed_on_market": "YYYY-MM-DD",
                      "udi_registered": true | false}]}
  B. a saved live call file (examples/live/*.json): every result row that has
     a submission_date and a decision_date is read as a decided submission.

Output: per submission, calendar days (submission to decision, or to as_of),
FDA days when the person gave hold days, and the sourced reference numbers
beside them, each labeled for what it measures. Per EU device, which
EUDAMED rule applies. Nothing here forecasts a decision.

Sources (rows in references/reg-pathways-sources.md and multi-region-sources.md,
read 19 October 2026): RP US-11, RP US-13, RP US-14, RP US-46 to US-48, RP US-58, RP US-61;
JX-39, JX-40.

Usage: python3 review_clock.py FILE
"""
import json
import sys
from datetime import date, timedelta

REF = {
    "510k": {"label": "510(k)", "mdufa_fda_days": 90, "mdufa_row": "RP US-46",
             "observed_total": (141.24, 143.64), "observed_row": "RP US-58",
             "reg_clock": None},
    "denovo": {"label": "De Novo", "mdufa_fda_days": 150, "mdufa_row": "RP US-47, RP US-60",
               "observed_total": (247.51, 278.12), "observed_row": "RP US-61",
               "reg_clock": "120 days from acceptance (RP US-11)"},
    "pma": {"label": "PMA", "mdufa_fda_days": 180, "mdufa_row": "RP US-48",
            "observed_total": None, "observed_row": None,
            "reg_clock": "180 days from filing, up to 180 more after a major amendment (RP US-14, RP US-15)"},
}
PATHWAY_MAP = {"FDA_510K": "510k", "FDA_DE_NOVO": "denovo", "FDA_PMA": "pma"}
EUDAMED_MANDATORY = date(2026, 5, 28)      # JX-36
EUDAMED_EXISTING_DEADLINE = date(2026, 11, 28)  # JX-39


def d(s):
    return date.fromisoformat(s) if s else None


def from_live(data):
    rows, seen = [], set()
    for call in data.get("calls", []):
        for r in call.get("results", []) or []:
            if not isinstance(r, dict):
                continue
            route = PATHWAY_MAP.get(r.get("pathway"))
            if route and r.get("submission_date") and r.get("decision_date"):
                key = r.get("reference") or r.get("product")
                if key in seen:
                    continue
                seen.add(key)
                rows.append({"name": f"{r.get('product')} ({key})", "route": route,
                             "submitted": r["submission_date"], "decided": r["decision_date"]})
    return {"as_of": data.get("as_of", "2026-10-19"), "submissions": rows, "eu_devices": []}


def submission_lines(s, as_of):
    ref = REF[s["route"]]
    sub, dec = d(s["submitted"]), d(s.get("decided"))
    end = dec or as_of
    cal = (end - sub).days
    state = f"decided {dec.isoformat()}" if dec else f"open as of {as_of.isoformat()}"
    out = [f"{s['name']} | {ref['label']} | submitted {sub.isoformat()} | {state}",
           f"  calendar days: {cal}"]
    hold = s.get("sponsor_hold_days")
    if hold is not None:
        fda_days = cal - int(hold)
        rel = "within" if fda_days <= ref["mdufa_fda_days"] else "beyond"
        out.append(f"  FDA days (calendar minus {hold} hold days you gave): {fda_days}; "
                   f"{rel} the MDUFA goal of {ref['mdufa_fda_days']} FDA days ({ref['mdufa_row']}). "
                   f"The goal applies to a share of submissions, not to each one.")
    else:
        out.append(f"  FDA days: not computable without your hold days. MDUFA goal: "
                   f"{ref['mdufa_fda_days']} FDA days ({ref['mdufa_row']}).")
    if ref["observed_total"]:
        lo, hi = ref["observed_total"]
        out.append(f"  FDA observed average total days, FY 2023 to FY 2025: {lo} to {hi} "
                   f"({ref['observed_row']}); calendar days are comparable with this figure.")
        if cal < lo:
            place = "below FDA's average total time (under the lowest yearly average)"
        elif cal <= hi:
            place = "within the range of yearly averages"
        else:
            place = "above the highest yearly average"
        so_far = " so far" if not dec else ""
        out.append(f"  {cal} calendar days{so_far}: {place}.")
        if sub < date(2022, 10, 1):
            out.append("  note: submitted before FY 2023 (MDUFA V started 1 October 2022, RP US-45); "
                       "the averages above describe later cohorts.")
    if ref["reg_clock"]:
        out.append(f"  regulation clock: {ref['reg_clock']}")
    if s["route"] == "denovo" and s.get("info_request_date"):
        req = d(s["info_request_date"])
        limit = req + timedelta(days=180)
        if s.get("info_response_date"):
            out.append(f"  information request {req.isoformat()} answered {s['info_response_date']}.")
        else:
            out.append(f"  information request {req.isoformat()}: a De Novo is withdrawn if not fully "
                       f"answered within 180 days, that is by {limit.isoformat()} "
                       f"({(limit - as_of).days} days after {as_of.isoformat()}) (RP US-13).")
    return out


def eu_lines(dev, as_of):
    first = d(dev["first_placed_on_market"])
    reg = dev.get("udi_registered")
    if reg:
        return [f"{dev['name']} | registered in the UDI/device module (as you stated)."]
    if first < EUDAMED_MANDATORY:
        days = (EUDAMED_EXISTING_DEADLINE - as_of).days
        return [f"{dev['name']} | first placed {first.isoformat()}, before 28 May 2026 | not registered "
                f"(as you stated) | rule: register within 12 months of the notice; Commission "
                f"timeline gives {EUDAMED_EXISTING_DEADLINE.isoformat()}, {days} days after "
                f"{as_of.isoformat()} (JX-39)."]
    return [f"{dev['name']} | first placed {first.isoformat()}, on or after 28 May 2026 | not registered "
            f"(as you stated) | rule: registration must precede placing the first unit (JX-40). "
            f"Check with your regulatory owner."]


def main(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if "calls" in data:
        data = from_live(data)
    as_of = d(data.get("as_of")) or date.today()
    print(f"Clock table as of {as_of.isoformat()}\n")
    for s in data.get("submissions", []):
        print("\n".join(submission_lines(s, as_of)))
        print()
    if data.get("eu_devices"):
        print("EUDAMED UDI/device registration")
        for dev in data["eu_devices"]:
            print("\n".join(eu_lines(dev, as_of)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
