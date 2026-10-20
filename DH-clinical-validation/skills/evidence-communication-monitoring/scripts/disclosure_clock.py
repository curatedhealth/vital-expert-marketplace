#!/usr/bin/env python3
"""Registration tests and results clocks per trial, from the person's dates and confirmed regimes.

Usage:
  python3 disclosure_clock.py trials.csv [--as-of YYYY-MM-DD]

CSV columns (blank means not given; yes/no fields are the person's answers, never inferred):
  trial_id, registry, icmje_journal (yes/no), us_act (yes/no), eu_ctr (yes/no), who_signatory (yes/no),
  first_consent, first_enrolled, registration_submitted,
  primary_completion, study_completion, eu_end_of_trial_all_ms,
  us_delay_certification, us_approval_or_clearance, us_extension_to,
  us_results_submitted, eu_results_submitted, who_results_posted, journal_published

Rules (row ids from the research file clinical-study-and-rwe-research.md):
  ICMJE registration at or before first consent (CV132).
  US registration within 21 calendar days after first enrollment (CV141).
  US results 1 year after primary completion (CV145); with a delay certification, 30 days after approval
    or clearance and no later than 2 years after certification (CV146); an extension the person reports
    replaces the due date (CV147). The 210-day withdrawal route is not computed: give the date as
    us_extension_to or read it by hand.
  EU results 1 year after the end of the trial in all Member States (CV152).
  WHO joint statement (signatories only): summary results 12 months from primary completion; journal
    publication indicative 24 months from study completion (CV140).
The counting convention for "1 year" is not in the sourced rows: this script adds one calendar year
(29 February becomes 28 February). It never decides whether a regime applies.
"""
import csv
import sys
from datetime import date, timedelta


def d(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit(f"Refused: '{s}' is not a date in YYYY-MM-DD form.")


def add_years(x, n):
    try:
        return x.replace(year=x.year + n)
    except ValueError:  # 29 February
        return x.replace(year=x.year + n, day=28)


def add_months(x, m):
    y, mo = divmod(x.month - 1 + m, 12)
    y, mo = x.year + y, mo + 1
    for day in (x.day, 30, 29, 28):
        try:
            return date(y, mo, day)
        except ValueError:
            continue


def full(x):
    return f"{x.day} {x.strftime('%B')} {x.year}" if x else "[GAP]"


def status(due, done, as_of):
    if due is None:
        return "not computed [GAP]"
    if done:
        delta = (done - due).days
        return f"reported {full(done)}: " + ("on or before due date" if delta <= 0 else f"{delta} days after due date")
    delta = (due - as_of).days
    return f"not reported as of {full(as_of)}: " + (f"due in {delta} days" if delta >= 0 else f"{-delta} days past due date")


def yes(v):
    v = (v or "").strip().lower()
    return True if v == "yes" else False if v == "no" else None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    as_of = date.today()
    if "--as-of" in sys.argv:
        as_of = d(sys.argv[sys.argv.index("--as-of") + 1])
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    if not rows:
        sys.exit("Refused: no trials in the file.")
    print(f"# Disclosure clocks as of {full(as_of)}\n")
    print("Regimes are the person's answers; blank means not confirmed and nothing is computed for it.\n")
    for r in rows:
        tid = r.get("trial_id") or "[GAP]"
        print(f"## {tid} ({r.get('registry') or 'registry not given'})")
        consent, enrolled, reg = d(r.get("first_consent")), d(r.get("first_enrolled")), d(r.get("registration_submitted"))
        pcd, scd, eot = d(r.get("primary_completion")), d(r.get("study_completion")), d(r.get("eu_end_of_trial_all_ms"))
        lines = []
        # ICMJE
        ic = yes(r.get("icmje_journal"))
        if ic is None:
            lines.append("| ICMJE registration | CV132 | not confirmed | | |")
        elif ic:
            if consent and reg:
                gap = (reg - consent).days
                res = "at or before first consent" if gap <= 0 else f"after first consent by {gap} days; ICMJE journals may not consider it"
                lines.append(f"| ICMJE registration | CV132 | first consent {full(consent)} | registration submitted {full(reg)} | {res} |")
            else:
                lines.append("| ICMJE registration | CV132 | first consent or registration date missing | | [GAP] |")
        # US
        act = yes(r.get("us_act"))
        if act is None:
            lines.append("| US registration and results | CV141, CV145 | applicable clinical trial status not confirmed | | not computed [GAP] |")
        elif act:
            if enrolled:
                due = enrolled + timedelta(days=21)
                lines.append(f"| US registration | CV141 | first enrolled {full(enrolled)} + 21 days | due {full(due)} | {status(due, reg, as_of)} |")
            else:
                lines.append("| US registration | CV141 | first enrollment date missing | | [GAP] |")
            cert, appr, ext = d(r.get("us_delay_certification")), d(r.get("us_approval_or_clearance")), d(r.get("us_extension_to"))
            if ext:
                due, basis = ext, f"extension to {full(ext)} reported by the person (CV147)"
            elif cert:
                cap = add_years(cert, 2)
                if appr:
                    due = min(appr + timedelta(days=30), cap)
                    basis = f"certification {full(cert)}; approval or clearance {full(appr)} + 30 days, capped at certification + 2 years (CV146)"
                else:
                    due = cap
                    basis = f"certification {full(cert)} + 2 years (outer limit, CV146); earlier if cleared or withdrawn"
            elif pcd:
                due, basis = add_years(pcd, 1), f"primary completion {full(pcd)} + 1 year (CV145)"
            else:
                due, basis = None, "primary completion date missing"
            lines.append(f"| US results | CV145 to CV147 | {basis} | due {full(due) if due else '[GAP]'} | {status(due, d(r.get('us_results_submitted')), as_of)} |")
        else:
            lines.append("| US registration and results | CV141, CV145 | person says not an applicable clinical trial | | no US clock |")
        # EU
        eu = yes(r.get("eu_ctr"))
        if eu is None:
            lines.append("| EU results summary and lay summary | CV152 | EU CTR scope not confirmed | | not computed [GAP] |")
        elif eu:
            due = add_years(eot, 1) if eot else None
            lines.append(f"| EU results summary and lay summary | CV152 | end of trial in all Member States {full(eot)} + 1 year | due {full(due) if due else '[GAP]'} | {status(due, d(r.get('eu_results_submitted')), as_of)} |")
        else:
            lines.append("| EU results | CV152 | person says not under the EU CTR | | no EU clock |")
        # WHO
        who = yes(r.get("who_signatory"))
        if who:
            due = add_months(pcd, 12) if pcd else None
            lines.append(f"| WHO pledge, summary results | CV140 | primary completion {full(pcd)} + 12 months | due {full(due) if due else '[GAP]'} | {status(due, d(r.get('who_results_posted')), as_of)} |")
            due = add_months(scd, 24) if scd else None
            lines.append(f"| WHO pledge, publication (indicative) | CV140 | study completion {full(scd)} + 24 months | indicative {full(due) if due else '[GAP]'} | {status(due, d(r.get('journal_published')), as_of)} |")
        elif who is None:
            lines.append("| WHO pledge | CV140 | signatory status not confirmed | | not computed |")
        print("| Clock | Rule | Basis | Date | Status |\n|---|---|---|---|---|")
        print("\n".join(lines))
        print()
    print("One calendar year was added for each '1 year' rule; the counting convention is not in the sourced rows [GAP].")
    print("Regime answers are the person's; the script decides none of them. Registry actions stop for the person responsible for the registry.")


if __name__ == "__main__":
    main()
