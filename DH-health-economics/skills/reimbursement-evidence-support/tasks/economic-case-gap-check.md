# A2 Economic case gap check

Framework task: DH-01.07.1.1, Part A, task A2. Replaces the earlier "Submission readiness" section, re-scoped to the economic case: whether the model, the budget impact analysis and the studies behind them are ready against each body's rules. Readiness of the file itself (forms, fees, clocks) belongs to dh-market-access (`payer-engagement-and-hta-submission`, A2).

## What this task delivers

The person's economic case checked item by item against the rule set from A1: each item shown, not shown, departure, `[GAP]` or not applicable, with where it sits in their material; the studies behind the model resolved and graded "from design only"; each key result checked against a verbatim results passage; the person's budget impact and ratio recomputed on their own numbers, labeled hypotheses. It answers "does our model and evidence meet what NICE (or HAS, IQWiG, ICER-PHTI) asks for, and where are the gaps?"

Why it matters: a model built for one body rarely fits another. Perspective, discount rate, value set and the budget impact elements decide whether a body can use the model at all, before anyone looks at the result.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.1.1 Part A, Economic case gap check |
| Workflow | The steps below |
| Knowledge | `references/economic-case-checklist.md`; `references/body-economic-standards.md`; `references/gap-rules.md` |
| Tools | `literature.get_record`, `literature.search_literature` (only to find a DOI the person cannot give), `literature.classify_study`, `literature.grade_evidence`, `verify.check_currency`, `verify.qualify_source`, `verify.check_claim`; `analytics.scenario-modeler`, `analytics.risk-tornado` (budget impact arithmetic and one-way sensitivity on the person's numbers); `analytics.budget-impact-model` (try once; returned HTTP 422 on 19 October 2026); `scripts/model_check.py`; `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/gap-check-output.md` |
| Input | The request and its context: the A1 profile (or the bodies), the model report or a parameter list, the BIA if any, the DOIs of the studies the model rests on, the claims the person wants to make, thresholds the person wants tested |
| Governance | `references/governance.md` |
| Catalogue job | `evidence-table` (available) covers steps 3 and 4 for the studies; `budget-impact` (available, but its calculator returns HTTP 422; use step 5 instead). Calls and pitfalls: `references/tools.md` |

## Read the request

- **Bodies.** From A1 or the request. Without bodies, ask; the checklist differs per body.
- **The material.** A model report, a published economic evaluation, a spreadsheet description or a parameter list. Write a model description (the fields in `references/economic-case-checklist.md`) from what the material states; a field it does not state stays null and prints `[GAP]`. Never fill a field from what models usually do. Where `literature.get_record` returns a `pmcid` or an `oa_url`, read the methods section of the open-access full text (Europe PMC `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC<id>/fullTextXML`) before marking a field `[GAP]`: perspective and any alternative perspectives, utility instrument and weights, discounting, comparator, horizon, follow-up and attrition. Quote each with its section. A field stays `[GAP]` only when the full text is not available or is silent.
- **Studies.** A DOI or PMID for each study the effect, utility or resource-use inputs rest on. A product name is not enough.
- **Claims.** The economic claims the person wants to make (for example "cost saving at one year", "gains QALYs"). Without claims, skip step 4.
- **Numbers to run.** Only the person's: incremental cost and QALYs with intervals, population, uptake, unit costs, thresholds. Never supply a threshold, a cost, an uptake share or a utility.
- **Mode.** "Is our model good enough for NICE?" is short mode. "Full gap check for the dossier team" is full mode.

## Workflow

### Step 1. Write the model description

From the material, fill the fields for the named bodies. Quote the section each field comes from. Mark what the material is (a published paper, an internal report, a parameter list) and its date.

### Step 2. Check it against each body's items

Apply `references/economic-case-checklist.md` for each body. With code execution: `python3 scripts/model_check.py --spec <description.json> --body NICE_ROUTINE --body ESF --body HAS --body CHEERS` (add `--thresholds` only with the person's own numbers). Without code execution, apply the same items by hand. Specific checks that catch common misses:
- **Perspective.** A societal or payer perspective is a NICE departure (`HE-037`); a healthcare-system perspective needs justification at HAS (`HE-103`); IQWiG takes the SHI community (`HE-110`).
- **Value set.** For a NICE topic launched after 27 August 2026, UK 5L, and no 3L utilities even in sensitivity analyses (`HE-058`, `HE-061`); for earlier topics, 5L mapped to 3L (`HE-063`). Mapping is a departure (`HE-045`).
- **Costs.** ESF standard 17 wants UK costs tied to NHS and PSS resources (`HE-089`); a model costed in another currency or system is "not shown" for that standard, whatever its result.
- **BIA.** ESF: population and uptake, technology and implementation costs, comparator costs (`HE-088`). IQWiG: at least 3 years (`HE-112`). ICER-PHTI: 1 year first, with 2-to-5-year scenarios (`HE-122`).
- **Early use.** The key uncertainties named, and resolvable within 3 years (`HE-068`, `HE-072`).
- **CHEERS.** Reported or not reported per item; never a total (`HE-005`).
- **Instrument.** A non-EQ-5D instrument (for example SF-6D) is a mapping departure for NICE whatever its weights (`HE-045`).
- **Comparator.** Name the study's comparator and whether it is current NHS care in the person's scope. The references hold no NICE comparator rule row, so the fit is `[GAP]` for the owner to confirm, never passed.
- **Follow-up.** Report the completion share the paper states and the authors' own limitation sentence (for DOI 10.1016/j.lanepe.2026.101691: 587 of 1,720, 34.1%, at the final follow-up; "long-term certainty is limited by attrition").

### Step 3. Resolve and grade the studies

For each DOI: `literature.get_record`, then `literature.classify_study` and `literature.grade_evidence` (`question_type` "treatment"). Report design "decided by" and the CEBM level "from design only"; a trial-based economic evaluation is labeled `rct` from its title, which says nothing about the economic analysis (`references/tools.md`). Call `verify.check_currency` with the DOI for retraction, correction or supersession. An empty `trial_ids` means the library cannot confirm registration; take the registry id from the paper and print it with its locator (for example NCT02558647, abstract, Methods). Write `[GAP]` only if the paper names none.

### Step 4. Check the key results

For each claim: `verify.qualify_source {doi}`, then `verify.check_claim` with the claim, the results sentence quoted verbatim with its locator, and the full source object. Then read the passage yourself: direction, interval, horizon, comparator and currency must match the claim. A cost difference whose interval includes zero does not support "significantly lower cost"; Verify rated that overstated claim "partial", the same as the accurate one (`references/tools.md`). Record "checked" only when the passage states the finding as claimed.

### Step 5. Recompute on the person's numbers

- **Ratio and net benefit.** From the incremental cost and QALYs the person gives (or the paper reports), the ratio, the net monetary benefit at the person's thresholds and the switching values (`HE-077`) come from `scripts/model_check.py`. Report the source's own ratio beside any recomputation. A negative ratio with lower cost and more QALYs is not ranked against a threshold.
- **Budget impact.** Try `analytics.budget-impact-model` once with the person's population, mix, cost and uptake; on HTTP 422, use `analytics.scenario-modeler` with a formula the person agrees (for example `population * uptake * (new_cost - displaced_cost)`, periods labeled year 1 to N because the tool counts from `t: 0`).
- **Sensitivity.** `analytics.risk-tornado` with the person's low and high values; list parameters it skips (`skipped_parameters`).
Every result is a hypothesis on the person's inputs, shown beside them.

### Step 6. Say what it means

Per body, in facts: which items are shown, which are departures the owner must decide to justify or replace, which are not shown, and which are `[GAP]` because the material is silent. Name the body's written range beside any ratio (both NICE ranges, `HE-074`, `HE-050`, `HE-051`), and say the body concludes. Hand the open items to B1.

## Build the output

Follow `assets/gap-check-output.md`. Answer first: per body, one line on shown, departures and open items. Then the item table, the study table, the claim lines, the arithmetic. Short mode keeps the item table for the asked body, the claim lines and the arithmetic in three lines.

## Before you hand it over

- Every scenario the paper reports (for example a healthcare-sector perspective in an appendix) is listed beside the base case, with its location in the paper.
- Ask whether the person's product is the version that was studied; if not, say the study is about the trialled version and mark fit as the person's call.

- Every item carries its row; every study its identifiers; every checked claim its passage.
- No "meets", "cost-effective" or "cost saving" in your voice; ratios sit beside the body's written ranges with rows.
- CEBM level labeled "from design only"; Verify statuses read, not trusted.
- Every computed number shows its inputs and is labeled a hypothesis.
- Departures and methods choices flagged as the owner's decision (owner as named, or "owner not named").
- Short mode counted: 450 words or fewer.
- Record line present; `verify.build_record` only with a named clearer.

## Boundaries

- No judgment that the model is "good enough": the body and the owner decide.
- No new model build; B1 lays out options. Economic model development belongs to the pack's economic modeling competency (DH-01.07.2).
- No systematic review: dh-clinical-validation `literature-and-real-world-evidence-review`.
- No price, threshold price or discount: dh-market-access.
