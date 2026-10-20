#!/usr/bin/env python3
"""Registration and reporting check for one trial: registry record against the
person's protocol or publication facts, with the clocks the sourced rows set.

Input:
  --registry FILE   study record saved from the ClinicalTrials.gov API v2
                    (https://clinicaltrials.gov/api/v2/studies/<NCT id>)
  --facts FILE      optional JSON with the person's facts, any of:
                    {"primary_outcome": "text from protocol or paper",
                     "primary_outcome_source": "protocol v3 section 2.4",
                     "masking": "outcome assessor", "target_enrollment": 700,
                     "applicable_clinical_trial": "yes" | "no" | "unknown",
                     "first_consent_date": "YYYY-MM-DD"}
  --as-of DATE      the date of the check (default today), YYYY-MM-DD

Rules applied (row ids from references/clinical-study-and-rwe-research.md):
  CV132 ICMJE: registered at or before first patient consent; the date first
        submitted to the registry counts. Without a consent date the registry
        start date is shown as a stand-in and labeled so.
  CV141 42 CFR 11.24: within 21 days after first enrollment, only for an
        applicable clinical trial (CV142, CV143).
  CV145 42 CFR 11.44(a): results within 1 year of primary completion, only for
        an applicable clinical trial; certified delays (CV146) and extensions
        (CV147) are not visible in the record.
  CV149 42 CFR 11.64: registration updated at least every 12 months (trials
        initiated on or after 18 January 2017), only for an applicable trial.
The script reports facts and day counts. Whether a rule applies, and whether a
difference matters, is the person's call with the owner they name for regulatory status.
"""
import argparse, datetime as dt, json, re

def d(s):
    if not s: return None
    s = s.strip()
    for f in ("%Y-%m-%d", "%Y-%m"):
        try: return dt.datetime.strptime(s, f).date()
        except ValueError: pass
    return None

def words(t):
    return set(re.findall(r"[a-z]+", (t or "").lower())) - {"the","of","a","an","and","or","with","by","in","at","to","for","was","is","be","will"}

METRIC = {"time to": r"\btime to\b", "number of": r"\bnumber of\b", "percentage": r"\bpercentage\b|\bproportion\b",
          "change": r"\bchange\b", "mean": r"\bmean\b", "onset": r"\bonset\b"}

def metric_words(t):
    return sorted(k for k, p in METRIC.items() if re.search(p, t or "", re.I))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--facts")
    ap.add_argument("--as-of", default=dt.date.today().isoformat())
    a = ap.parse_args()
    rec = json.load(open(a.registry)); p = rec.get("protocolSection", {})
    facts = json.load(open(a.facts)) if a.facts else {}
    asof = d(a.as_of)
    st = p.get("statusModule", {}); ident = p.get("identificationModule", {})
    act = (facts.get("applicable_clinical_trial") or "unknown").lower()
    tag = {"yes": "applies (person says applicable clinical trial)",
           "no": "does not apply (person says not an applicable clinical trial)",
           "unknown": "applies only if an applicable clinical trial (CV142, CV143) [GAP]: ask"}[act if act in ("yes","no") else "unknown"]
    first = d(st.get("studyFirstSubmitDate")); start = d(st.get("startDateStruct", {}).get("date"))
    consent = d(facts.get("first_consent_date"))
    pcd = d(st.get("primaryCompletionDateStruct", {}).get("date")); pcd_type = st.get("primaryCompletionDateStruct", {}).get("type", "")
    res = d(st.get("resultsFirstSubmitDate")); upd = d(st.get("lastUpdateSubmitDate"))
    print(f"# Registration and reporting check: {ident.get('nctId','[GAP]')}\n")
    print(f"As of {asof.isoformat()}. Source: ClinicalTrials.gov record as saved.\n")
    print("| Check | Facts | Rule | Reading |"); print("|---|---|---|---|")
    ref = consent or start; reflabel = "first consent (person)" if consent else "registry start date, stand-in for first consent"
    if first and ref:
        gap = (first - ref).days
        r = "registered before the reference date" if gap < 0 else ("same day" if gap == 0 else f"registered {gap} days after")
        print(f"| Prospective registration | first submitted {first}; {reflabel} {ref} | CV132 | {r} |")
    else:
        print("| Prospective registration | [GAP] date missing | CV132 | not measurable |")
    if first and start:
        gap = (first - start).days
        r = f"submitted {-gap} days before start" if gap < 0 else f"submitted {gap} days after start"
        print(f"| 21-day registration | first submitted {first}; start {start} | CV141, {tag} | {r} |")
    if pcd:
        due = pcd.replace(year=pcd.year + 1) if not (pcd.month == 2 and pcd.day == 29) else pcd.replace(year=pcd.year + 1, day=28)
        if res:
            print(f"| Results within 1 year | primary completion {pcd} ({pcd_type}); results first submitted {res} | CV145, {tag} | {(res - pcd).days} days after primary completion |")
        else:
            left = (due - asof).days
            print(f"| Results within 1 year | primary completion {pcd} ({pcd_type}); no results submitted | CV145, {tag} | one year after primary completion is {due}; {left} days from the as-of date (negative means passed); certified delay or extension not visible (CV146, CV147) |")
    if upd:
        age = (asof - upd).days
        print(f"| Update at least every 12 months | last update submitted {upd} | CV149, {tag} | {age} days before the as-of date; status {st.get('overallStatus','[GAP]')}; whether the duty runs after completion is not in the rows [GAP] |")
    prim = p.get("outcomesModule", {}).get("primaryOutcomes", [])
    reg_txt = " ; ".join((o.get("measure","") + " (" + o.get("timeFrame","") + ")") for o in prim) or "[GAP]"
    if facts.get("primary_outcome"):
        fw, rw = words(facts["primary_outcome"]), words(reg_txt)
        overlap = round(100 * len(fw & rw) / max(1, len(fw | rw)))
        rm, fm = metric_words(reg_txt), metric_words(facts["primary_outcome"])
        flag = "metric words differ: read both texts (SP-16, SPIRIT 2025 DOI 10.1136/bmj-2024-081477; CV113, CV114, CONSORT 2025 DOI 10.1136/bmj-2024-081123)" if rm != fm else "metric words match; still read both"
        print(f"| Primary outcome | registry: {reg_txt.replace('|','/')}; {facts.get('primary_outcome_source','person')}: {facts['primary_outcome'].replace('|','/')} | SP-16 (SPIRIT 2025 DOI 10.1136/bmj-2024-081477), CV113 (CONSORT 2025 DOI 10.1136/bmj-2024-081123) | word overlap {overlap}%; metric words registry {rm or 'none'}, other {fm or 'none'}; {flag} |")
    else:
        print(f"| Primary outcome | registry: {reg_txt.replace('|','/')} | SP-16 (SPIRIT 2025 DOI 10.1136/bmj-2024-081477) | no protocol or paper text supplied [GAP] |")
    mask = p.get("designModule", {}).get("designInfo", {}).get("maskingInfo", {})
    if facts.get("masking"):
        print(f"| Masking | registry: {mask.get('masking','[GAP]')} {', '.join(mask.get('whoMasked', []))}; person: {facts['masking']} | SP-24a (SPIRIT 2025 DOI 10.1136/bmj-2024-081477) | compare |")
    enr = p.get("designModule", {}).get("enrollmentInfo", {})
    if facts.get("target_enrollment"):
        print(f"| Enrollment | registry: {enr.get('count','[GAP]')} ({enr.get('type','')}); target: {facts['target_enrollment']} | SP-19, SP-20 (SPIRIT 2025 DOI 10.1136/bmj-2024-081477) | {enr.get('count',0) - facts['target_enrollment'] if isinstance(enr.get('count'), int) else '[GAP]'} against target |")
    print("\nThe registry's change history is not in this record; read it on the registry before calling any difference a change (CV114).")

if __name__ == "__main__":
    main()
