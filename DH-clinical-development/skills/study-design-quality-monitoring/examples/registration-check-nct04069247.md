# Worked example: A2 registration tracking on live library and registry data

Run on 19 October 2026. Request (a reviewer's view of a published trial): "Before we cite this app-based CBT-I prevention trial as our design model, check its registration against the paper: DOI 10.1371/journal.pmed.1004510." Applicability under US law: unknown. No owner named.

Calls made (saved in `live/connector_calls_2026-10-19.json`, `live/nct04069247.json`, `live/facts_nct04069247.json`):
1. `literature.find_trial {record: {doi: "10.1371/journal.pmed.1004510", pmid: "39836656"}}`: NCT04069247, COMPLETED, sponsor Chinese University of Hong Kong; one other registration cites the paper as background only and was not linked.
2. ClinicalTrials.gov API v2 record for NCT04069247, read 19 October 2026.
3. Europe PMC full text PMC11750088, section 2.4, for the outcome sentence.
4. `verify.qualify_source {doi}` (gold, current), then `verify.check_claim` with that sentence: "supported" (61 percent overlap); passage read and agrees. A claim with the opposite metric also returned "supported" (N3), so the passage reading decides.
5. `python3 scripts/registry_check.py --registry live/nct04069247.json --facts live/facts_nct04069247.json --as-of 2026-10-19` (output in `registry_check_nct04069247.md`).

---

**Answer.** NCT04069247 was first submitted to ClinicalTrials.gov on 15 August 2019, 21 days before its registered start date of 5 September 2019, so it was registered before the reference date (the start date stands in for first consent, which the record does not give; CV132). The main difference: the registry states the primary outcome as "Number of Participants With Major Depressive Disorder" ("Up to 12-month follow-up"), while the paper states "time to onset of MDD" at post-intervention, 6 and 12 months. That is a different analysis metric in the wording (a count versus time to event, SP-16, CV113). Whether it reflects a change is not shown here: the registry's History of Changes was not readable by script, and a reason would be reported under CONSORT item 10 (CV114). Read both before citing the design.

**Side by side**

| Element | Registry (read 19 October 2026) | Paper (PMC11750088) | Reading |
|---|---|---|---|
| Primary outcome | "Number of Participants With Major Depressive Disorder" | "time to onset of MDD" | worded differently: metric |
| Time point | "Up to 12-month follow-up" | post-intervention, 6- and 12-month follow-ups | consistent span |
| Masking | Single (outcomes assessor) | not checked in this run | not stated |
| Enrollment | 708 (actual) | 708 randomized | same |

**Clocks** (each applies only if this is a US applicable clinical trial, CV142: `[GAP]`, the owner the person names for regulatory status, or owner not named)

| Clock | Facts | Reading |
|---|---|---|
| 21-day registration (CV141) | submitted before start | submitted 21 days before start |
| Results within 1 year (CV145) | primary completion 18 January 2024; results submitted 17 April 2024 | 90 days after |
| Update every 12 months (CV149) | last update submitted 25 November 2024 | 693 days before the check; whether the duty runs after completion is not in the rows `[GAP]` |

**Stops.** Any statement to a journal or HTA body about this difference goes to the owner (owner not named: who?).

**Record.** Registration tracking draft. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (without the calls list and the table source columns): 315, counted by script.
