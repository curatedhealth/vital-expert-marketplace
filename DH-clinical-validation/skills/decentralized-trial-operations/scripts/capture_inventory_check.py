#!/usr/bin/env python3
"""Check a remote data capture inventory against the attributes the sourced rules ask for.

Input: a CSV with one row per data stream (DHT, app, ePRO, EHR export). Columns
(case-insensitive; missing columns are treated as blank):

  stream, dht_model_version, endpoint_role, arms, same_method_all_arms, entered_by,
  first_durable_repository, audit_trail, timestamps_utc, verification_evidence,
  validation_evidence, validation_in_trial_population, usability_evidence,
  can_show_abnormal, safety_review_plan, critical_to_quality, contingency,
  participant_entry_safeguard

endpoint_role: primary, key_secondary, safety, secondary or exploratory.
entered_by: device, participant, staff or ehr. arms: separated by ";".
Yes/no fields accept yes, y, true, 1 (anything else counts as no; blank stays blank).

The script does not judge fitness for purpose. It lists, per stream, which required
attribute is not recorded, with the row id of the rule (references/remote-capture-rules.md).
Thresholds and acceptance are the person's.

Usage: python3 capture_inventory_check.py inventory.csv [--json]
"""
import csv
import json
import sys

YES = {"yes", "y", "true", "1"}
ENDPOINT_ROLES_PROTECTED = {"primary", "key_secondary", "safety"}


def val(row, key):
    return (row.get(key) or "").strip()


def is_yes(v):
    return v.strip().lower() in YES


def check(row):
    flags = []
    role = val(row, "endpoint_role").lower()
    arms = [a for a in val(row, "arms").split(";") if a.strip()]

    if not val(row, "dht_model_version"):
        flags.append(("No model and version named; minimum specifications cannot be checked", "CV52"))
    if not val(row, "verification_evidence"):
        flags.append(("Verification evidence not recorded", "CV46"))
    if not val(row, "validation_evidence"):
        flags.append(("Validation evidence not recorded", "CV46"))
    elif not is_yes(val(row, "validation_in_trial_population")):
        flags.append(("Validation not shown in the trial population", "CV48"))
    if not val(row, "usability_evidence"):
        flags.append(("Usability evaluation with the trial population not recorded", "CV51"))
    if not val(row, "first_durable_repository"):
        flags.append(("Source location (first durable repository) not named", "CV60"))
    if not is_yes(val(row, "audit_trail")):
        flags.append(("Audit trail not confirmed", "CV14"))
    if not is_yes(val(row, "timestamps_utc")):
        flags.append(("Unambiguous timestamps (for example UTC) not confirmed", "CV14"))
    same = val(row, "same_method_all_arms")
    if len(arms) > 1:
        if not same:
            flags.append(("Same collection method in all arms not recorded", "CV58"))
        elif not is_yes(same):
            flags.append(("Collection method differs between arms", "CV58"))
    if is_yes(val(row, "can_show_abnormal")) and not val(row, "safety_review_plan"):
        flags.append(("Can show abnormal values; safety review plan not recorded", "CV62"))
    if is_yes(val(row, "critical_to_quality")) and not val(row, "contingency"):
        flags.append(("Critical-to-quality stream without a contingency for tool failure", "CV99"))
    if (val(row, "entered_by").lower() == "participant" and role in ENDPOINT_ROLES_PROTECTED
            and not val(row, "participant_entry_safeguard")):
        flags.append(("Participant-entered data on a %s endpoint without an entry safeguard" % role, "CV103"))
    return flags


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    with open(argv[1], newline="", encoding="utf-8-sig") as f:
        lines = [ln for ln in f if not ln.lstrip().startswith("#")]  # skip comment lines
        rows = [{(k or "").strip().lower(): v for k, v in r.items()} for r in csv.DictReader(lines)]
    results = []
    for r in rows:
        fl = check(r)
        results.append({"stream": val(r, "stream") or "[GAP] unnamed stream",
                        "endpoint_role": val(r, "endpoint_role") or "[GAP]",
                        "open_attributes": [{"item": a, "row": b} for a, b in fl]})
    if "--json" in argv:
        print(json.dumps(results, indent=2))
        return 0
    total = sum(len(r["open_attributes"]) for r in results)
    print("# Capture inventory check\n")
    print("Streams: %d. Open attributes: %d. Each line is a missing record against a sourced "
          "requirement element, not a verdict on the stream.\n" % (len(results), total))
    print("| Stream | Endpoint role | Open attribute | Row |")
    print("|---|---|---|---|")
    for r in results:
        if not r["open_attributes"]:
            print("| %s | %s | none recorded as missing | |" % (r["stream"], r["endpoint_role"]))
        for o in r["open_attributes"]:
            print("| %s | %s | %s | %s |" % (r["stream"], r["endpoint_role"], o["item"], o["row"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
