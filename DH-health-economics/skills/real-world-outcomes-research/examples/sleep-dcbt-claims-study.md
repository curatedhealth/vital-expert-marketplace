# Worked run: a claims-data study for a digital CBT-I app

Run on 19 October 2026. The product and the study log are **illustrative** (written for this example). The library calls and the two published papers are real; their outputs are quoted as returned. Mode: short, with the calls listed.

Request: "We have a DiGA-listed insomnia app. We want to use German statutory claims data to show it reduces hypnotic prescriptions. Frame the study, check our execution log, and tell us how to word a result like the published US one."

---

## A1 Outcomes question (short mode)

**Answer.** Your question as PICO: adults with insomnia in German statutory claims data (P), prescribed the app (I), compared with people with insomnia not prescribed it (C, your choice of comparator still open), hypnotic prescriptions after start (O). HETE or exploratory is your declaration; HETE is open only if nobody on the team has looked at outcome data in this claims source yet (HE-025, HE-026; DOI 10.1002/pds.4297); then the protocol and analysis plan go on a public registration site before analysis (HE-027, DOI 10.1002/pds.4297). If the hypothesis came from your own app data, testing it in claims data meets HE-029.

| Choice | Options with rows | Status |
|---|---|---|
| Study type | HETE or exploratory (HE-026, DOI 10.1002/pds.4297) | Yours, not made yet |
| Intercurrent event: stopping the app | Treatment policy (CV35) or while on treatment (CV38) | Yours, not made yet |
| Causal design | Target trial emulation, after a feasibility assessment (CV107, CV106) | Proposed |

**Data fitness gaps** (framework: FDA CDRH device guidance, because the app is a device; CV91, CV92):
1. Operational definition of "hypnotic prescription" (code list) and its validation are not supplied `[GAP]` (CV80, CV81).
2. Continuity of statutory coverage over the follow-up is not described `[GAP]` (CV83).
3. Linkage of app-use data to claims needs a prespecified rule for inconsistencies (CV24).

**Prior record** (read from the papers, not the library labels):
- Miller et al. 2025, US commercial and Medicare claims, retrospective difference-in-differences, 11 027 app users against 1:1 exact matched controls (n = 10 770); funded by the manufacturer, which played a role in design; analysis by an independent group. Library label `guideline` (0.6); no ClinicalTrials.gov link found. DOI 10.36469/001c.146434.
- No German claims study on this question was returned in two searches; that is a limit of the searches, not proof none exists.

**Record.** Question brief. Choices are yours. Clears it: owner not named. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. AI-assisted draft.

---

## A2 Study execution record (short mode, illustrative log)

**Answer.** Yes for the primary plan as first written: protocol (2 March 2026) and analysis plan (20 March 2026) were final before first outcome access (4 May 2026), and registration (25 March 2026) preceded analysis (11 May 2026). But analysis plan version 1.2 (1 June 2026) changed the primary outcome window after outcome access, so the 9-month primary result is a deviation, not prespecified (CV94; HE-028, DOI 10.1002/pds.4297). The conformance statement must carry two deviations plus that revision.

`python3 scripts/prespec_check.py examples/illustrative_study_log.json` returned the table in `examples/illustrative_study_log_check.md` (8 checks; 3 open).

Open items:
1. Registry id not given `[GAP]`.
2. One deviation (covariates dropped, 20 June 2026) has no reason `[GAP]`.
3. Linkage planned without an inconsistency rule `[GAP]` (CV24).

**Record.** Execution record draft. Dates are yours, from your documents. Clears it: owner not named. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. AI-assisted draft.

---

## B1 Outcome result: the wording check (demonstration on a published result)

The team asked how a result "like the published one" should be worded. The demonstration used a published real-world EHR study (Palacios et al. 2024, JMIR Mental Health, DOI 10.2196/59145), whose abstract reads: "App-augmented treatment was associated with a significant decrease in emergency department visits ( P <.001) ...".

| Sentence tested | Verify status | Read in the same direction and hedge? | Use |
|---|---|---|---|
| "... was associated with fewer emergency department visits than treatment as usual." | supported (54%) | Yes | Usable as a factual statement, draft for the owner |
| "The app causes a reduction in emergency department visits ..." | supported (44%) | No: "associated with" became "causes" | Declined; redrafted as the association |
| "... was associated with an increase in emergency department visits." | supported (100%) | No: direction reversed | Declined; shows why the tool's status is not enough (N3) |

For your own study: the result keeps the report's direction and hedge, carries its status from A2 (the 9-month window is a deviation), and starts from low GRADE certainty as non-randomized evidence (ES-90, ES-100); the rating is yours or the HTA body's.

**Record.** Result draft. Not evidence of efficacy or cost-effectiveness. Clears it: owner not named. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. AI-assisted draft.

---

## Calls made (19 October 2026)

1. `literature.search_literature {query: "digital cognitive behavioral therapy for insomnia real-world hypnotic prescriptions health care utilization", limit: 6}`
2. `literature.search_literature {query: "real-world effectiveness digital therapeutic observational cohort health care utilization", limit: 8}`
3. `literature.find_trial {record: {doi: "10.36469/001c.146434", ...}}`: no linked registration found
4. `literature.check_retraction {doi: "10.36469/001c.146434"}`: none (Crossref)
5. `literature.get_record {doi: "10.2196/59145"}`
6. `verify.qualify_source {doi: "10.2196/59145", question: ...}`: gold, 78
7. to 9. `verify.check_claim` three times with the full source object and the abstract passage (locator "Abstract, Results; PMC11635337")
Full texts read through Europe PMC (PMC12619666, PMC11635337) for design facts and passages.
