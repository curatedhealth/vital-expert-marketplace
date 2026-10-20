# A2 Link-by-link check

Framework task: DH-01.01.2.2, Part A, task A2. Replaces the earlier "Mechanism score" section (DH-01.01.2.2.2, register CF-12.01.01.2.2.2).

## What this task delivers

One study or one live cohort, on one named version, checked against the A1 plan: for each measurable link, the observed value, its denominator and missing data, and "met" or "missed" by the person's threshold; links without a measure or with a measure chosen after the data were read are listed as not scored. The count of met links over measurable links closes the check; it is not a quality score.

Why it matters: a check read in order (delivered, used, changed, outcome) tells a failed deployment from a mechanism that did not hold (CS32). Scoring only prespecified links keeps the result from bending to the data (TM57).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.2 Part A, Link-by-link check |
| Workflow | The steps below |
| Knowledge | A1 plan; `references/check-plan-rules.md`; `references/precedents.md`; rows TM57, TM84, TM92 to TM98, TM102; CS27, CS32, CS39 |
| Tools | Own cohort: `scripts/link_check.py`. Published study: `literature.search_literature`, `literature.find_trial`, ClinicalTrials.gov record read, `verify.qualify_source` then `verify.check_claim`. Named product: `regulatory-dh.get_authorization`, `regulatory-dh.search_safety_events` |
| Prompt | This guide |
| Template | `assets/link-by-link-check-output.md` |
| Input | The request and its context; the A1 plan with thresholds; the cohort file or the study; the version and data cut |
| Governance | `references/governance.md`; thresholds and verdict rules are the person's |
| Catalogue job | none |

## Read the request

- **Plan.** Is there an A1 plan with thresholds set before the data? If not, run A1 first; values may be reported, but nothing is scored without a prespecified measure and threshold.
- **Cohort and version.** Name both, and the data cut date, as the person gave them; any not given is written "not given" and asked. A check spans one version only.
- **Source.** The person's own data (file), or a published study (DOI or NCT id), or a named product's public record.
- **Privacy.** Cohort data stay local; never send patient rows to a library call.

## Workflow

### Step 1. Name the cohort, version and data cut

Write them first, in the person's words. A version or data cut the person did not give is "not given" and asked; never supply today's date or a date from a file name; mixed versions are reported, not pooled, unless the person says so (old task step 1).

### Step 2a. The person's cohort: run the check

With code execution, run `python3 scripts/link_check.py --plan PLAN.json --data COHORT.csv --version "<version>"`, adding `--as-of YYYY-MM-DD` only with the data cut the person gave. Never pass today's date; without a cut the script prints "data cut not given" and the answer says so and asks. It reports, per link: n with data, n missing, the observed value, the threshold, met or missed, or "not scored" with the reason (no measure, measure not prespecified, no threshold). It prints the reading order and warns when a delivery or use link missed and later links are being read. Check its output against the file before quoting; never impute missing values. If the person says a measure "dropped", "rose" or "improved" and the file holds only one time point for it, say the change cannot be computed from this file; a single-time-point value is reported as a level, not a change.

### Step 2b. A published study: read the record

Find the paper (`literature.search_literature`), the registration (`literature.find_trial` with the record, then with the NCT id if the first returns nothing; registry content read from the ClinicalTrials.gov API), and check whether each link's measure was prespecified in the registration. For each result you will quote, take the sentence from the abstract or full text, call `verify.qualify_source {doi, question}` then `verify.check_claim` with the full qualify_source object and the passage `{text, locator}`. Accept only when you have read the passage and it says the same thing (N3). Apply the person's verdict rule to what the passage states; where the passage is silent for a link, that link is "not measurable from the records read" `[GAP]`.

### Step 3. Named product: delivery-link events

For a named product, call `regulatory-dh.search_safety_events {product_code}` or `{manufacturer}` with `since` set to the cohort period. Set `since` only from a cohort period the person gave. Quote what each record states, with its date and class (example: the PWE recalls of 7 June 2021 describe the reward granted "regardless of the UDS results"). Do not judge whether a record bears on the person's product or cohort; infer nothing more.

### Step 4. Read in order and mark

Mark each link met, missed or not scored, with the value, denominator and source. If a delivery or use link missed, say later links cannot separate an ineffective mechanism from failed delivery (CS32, TM92). Report context the person gave (TM96).

### Step 5. Count, without scoring

Write "N of M measurable links met against your thresholds", list the not-scored links, and say the count is not a quality score (old task rule: do not score a `[GAP]` link; governance).

### Step 6. Hand misses to B1

List each missed link with its value and source for the miss review.

## Build the output

Follow `assets/link-by-link-check-output.md`. Answer first: cohort and version, links met and missed, not scored, and the first link in reading order that missed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Only prespecified measures with the person's thresholds are marked met or missed.
- No proxy appears that the plan did not name.
- Engagement is never reported as the outcome.
- Published results are quoted from passages read in the same direction, with DOI or NCT id; registry facts carry their read date.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Statistical tests, mediation models and their assumptions: whoever the person names for the analysis (owner not named if none); `dh-clinical-development` study-protocol-and-endpoint-design.
- Grading a body of published evidence: `dh-clinical-development` literature-and-real-world-evidence-review.
- Usability findings behind a use-link miss: `dh-patient-and-user-experience` usability-monitoring.
