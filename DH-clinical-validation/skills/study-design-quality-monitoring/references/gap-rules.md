# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it | The fact plus the row id ("registration within 21 days after first enrollment, CV141") | None |
| Applicability unknown | A clock whose instrument may not apply (US applicable clinical trial, EU CTR) | "Applies only if an applicable clinical trial (CV142) `[GAP]`" | Regulatory owner decides |
| Published method | [PAPER] row | "SPIRIT 2025 item 27c (SP-27c), DOI 10.1136/bmj-2024-081477" | Cite the DOI |
| Nonbinding or draft | FDA guidance; DAP guidance draft | "Nonbinding guidance (CV42)"; "draft, not for implementation (PE-41)" | Do not treat as law or in force |
| Not in the sources | ISO 14155, MDR investigation rules, EU CTR transition dates, risk-of-bias judgments | "Not in this skill's sources `[GAP]`" | Ask the named owner |

## Library and registry facts

| Situation | How to word it |
|---|---|
| `find_trial` returns no registration | "No ClinicalTrials.gov link found by the library; other registries not searched `[GAP]`. Absence is not evidence the trial is unregistered." |
| `trial_ids` empty on a library record | "Registry id not on the library record; found with find_trial" or `[GAP]` |
| Registry history not read | "Registry change history not read (endpoint returned 403 to the build); read the History of Changes page before calling a difference a change" |
| Consent date unknown | "First consent date not supplied; registry start date used as a stand-in, labeled" |
| Certification or extension | "Not visible in the record `[GAP]`" (CV146, CV147) |
| Verify returns "supported" | Reported as support only when the passage was read and says the same thing (N3) |

## The person's facts

| Situation | How to word it |
|---|---|
| Protocol section not supplied | "Not checkable: section not supplied `[GAP]`" |
| No pass rule for a check | Report the facts; no verdict |
| No owner named | "Owner not named"; ask. Never suggest a job title |
| Protocol version or date missing | "Version not stated `[GAP]`"; comparisons across versions wait for it (SP-2) |

## Never

- Never call silence "not relevant" (CV117).
- Never call a wording difference a change, an outcome switch or misconduct.
- Never treat a missing registry link, a missing clock or a missing item as compliance.
- Never compute a score from item counts.
