# Worked example: A1 endpoint and COA selection on live library data

Run on 19 October 2026. Request (illustrative product, real comparables): "We are planning an RCT of our app-based CBT-I program for adults with insomnia and mild depressive symptoms. We want to claim it reduces insomnia and helps prevent depression. We were thinking ISI, PHQ-9 and sleep from a wrist wearable. What did similar trials measure, and what should be primary?" No owner named.

Calls made (all saved in `live/connector_calls_2026-10-19.json` and `live/nct*.json`):
1. `literature.search_literature {query: "digital cognitive behavioral therapy insomnia randomized controlled trial app", limit: 6, filters: {designs: ["rct"]}}`: 23 merged, 5 shown; kept 2 that match the PICO (app-based CBT-I, randomized); dropped a 2015 single-session trial, a depression-only app trial and a conference abstract.
2. `literature.find_trial {record: PLoS Med 2025, DOI 10.1371/journal.pmed.1004510}`: NCT04069247.
3. `literature.find_trial {record: JAMA Netw Open 2023, DOI 10.1001/jamanetworkopen.2023.4866}`: NCT04779372.
4. ClinicalTrials.gov records read directly; `python3 scripts/registry_endpoints.py live/nct04069247.json live/nct04779372.json`.
5. `verify.qualify_source {doi: "10.1371/journal.pmed.1004510"}` (gold, current), then `verify.check_claim` with the paper's outcome sentence: "supported"; passage read and agrees.

---

**Answer.** Two registered app-based CBT-I trials match your question. One used diagnosed major depressive disorder as primary, the other the Insomnia Severity Index; both used PHQ-9 or ISI as secondary measures, and one recorded sleep from a "smart bracelet" as a secondary outcome. Which is primary is your choice, with the owner you name for statistics (owner not named: who decides?). The biggest open item: no verification or validation evidence is stated yet for the wearable in your population (CV46, CV48).

**Comparables (registry wording, read 19 October 2026)**

| Trial | Design, masking | Primary outcome | Time frame |
|---|---|---|---|
| NCT04069247 (DOI 10.1371/journal.pmed.1004510) | Randomized, parallel, prevention; outcome assessor masked; 708 actual | "Number of Participants With Major Depressive Disorder" (MINI) | "Up to 12-month follow-up" |
| NCT04779372 (DOI 10.1001/jamanetworkopen.2023.4866) | Randomized, parallel, treatment; no masking; 82 actual | "Insomnia Severity Index (ISI)" | "V2 and V4 visit ( 6, 18 weeks after recruitment)." |

The PLoS Medicine paper states its primary outcome as "time to onset of MDD" (section 2.4), a time-to-event metric, while the registry says "Number of Participants". Both are quoted as written; whether that is a change is for the monitoring skill (SP-16, CV114).

**Endpoint options**

| Option | Type | Elements still to define (SP-16) | Open items |
|---|---|---|---|
| ISI | PRO (PE-11) | metric, aggregation, time point | meaningful change anchor (PE-20, draft guidance); measurement properties for your population (PE-93) |
| PHQ-9 | PRO | same | same |
| Diagnosed depression onset (clinician interview) | ClinRO | metric (count or time to event), time point | interviewer masking (SP-24a) |
| Wearable sleep measure | Digital measure (DAT, CV20) | variable, tool and version, how nights combine (CV55) | V&V in your population, usability, own-device policy (CV46 to CV53) |

**Decisions for you.** Primary versus secondary, the time point, and whether the wearable is an endpoint or supportive. A novel wearable endpoint needs a justification on how patients feel, function or survive (CV56). FDA guidance cited is nonbinding.

**Record.** Endpoint options draft. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (without the calls list and the table source columns): 323, counted by script.

## What this run shows about the connector

- `trial_ids` was empty on both papers; `find_trial` was the only route to the NCT ids (N8).
- `find_trial` returns no outcomes or dates; the registry record had to be read directly (BUILD_NOTES).
- A claim stating the opposite metric from the same passage also returned "supported" (N3); the passage was read by the model.
- The script's "change" mark on NCT04779372 came from the outcome description ("change in scores of 8.4"), not from the metric: element marks are reading aids.
