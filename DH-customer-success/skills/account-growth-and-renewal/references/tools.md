# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `commercial-dh_audit_claims`). Counted calls draw on the library key's monthly allowance.

This is a method pack: it runs mainly on the person's own account file and the sourced references. The library adds the authorization record behind a claim, a role echo for who pays, a ranking calculator for actions the person scored, and the record. The person's account data, prices and customer names never go into a library call unless the person says so. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## commercial-dh.audit_claims (counted)

- Arguments: `reference` (exact regulatory identifier, scheme identifier or normalized name), `claims` (up to 20 strings), optional `intended_use`.
- Returns per claim a label (`matches_record`, `exceeds_record`, `no_authorization_on_file`), a finding F1 for therapeutic or diagnostic wording without an authorization, plus the upstream regulatory blocks (`get_authorization`, `search_devices`, `classify_product`, `find_predicates`, `get_pathway_precedents`, `search_safety_events`) and an evidence maturity block.
- Observed:
  - `{reference: "DEN160018", claims: [4 renewal-deck claims]}`: the authorization block is good (reSet, Pear Therapeutics, De Novo, class 2, product code PWE, regulation 882.5801, decision 14 September 2017, FDA source URL). But `intended_purpose_from_record` is "[GAP]", and every claim, including a plain restatement of the product type, is labeled `exceeds_record`; "cures opioid addiction" gets no F1 finding.
  - `{reference: "somnio", claims: [4 claims]}`: `authorization_on_file` is false and every claim is labeled `no_authorization_on_file`, while the same response's `search_devices` block holds two EU MDR Class IIa records for the product (EUDAMED, retrieved 14 October 2026). `get_authorization` matches exact identifiers only. F1 is attached only to the "diagnoses" claim, not to the therapeutic "reduces insomnia severity" claim.
  - The response is long (the evidence maturity and source coverage blocks), and the evidence maturity score is a library convention, not an evidence grade.
- How to use it here: in A2 Step 4, call it with the product's exact regulatory identifier (K, DEN or P number, or the exact registered name) to fetch the authorization record and its source URL. Report the record's route, class, product code and date as the record states them. Do not report the claim labels as findings: with no intended purpose on file they cannot separate safe from unsafe wording. The claim check itself is done against `account-materials-claims.md`. A missing authorization in the response is not evidence that none exists.

## commercial-dh.map_money_flow (counted)

- Arguments: `reference`; `user`, `buyer`, `payer` and `note` as the person states them.
- Observed with `{reference: "DEN160018", user: "patients in outpatient substance use treatment", buyer: "health system outpatient behavioral health service", payer: "Medicare and Medicaid via practitioner billing (G0552 to G0554)"}`: echoes the three roles, `conflated: false`, and a payer listings block that is empty ("no listed product matches"), although the library holds three CMS DMHT rows. DMHT rows are code-level, so a product never matches them, and the response does not say whether the product's FDA regulation (882.5801) is one the code covers. Exhibit links run from user to buyer to payer, the opposite of the money direction.
- How to use it here: optional, in A2 Step 1, to record who uses, buys and pays as the person states it. It does not decide whether a Federal program pays; that stays with the compliance owner (`offer-rules.md`, Step 0).

## analytics.mcda (counted)

- Arguments: `alternatives` (each `id` plus `scores`, a map of criterion to number) and `criteria_weights` (the person's weights, summing to 1).
- Method returned: "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)". Each `value_estimate` is the weighted sum of score over 4, times 100, with `contributions` by criterion.
- Observed with three renewal actions and weights 0.5, 0.25, 0.25: values 75, 68.75 and 68.75. Two actions tie and the response does not say so. Every criterion is treated as higher-is-better (`negative_criteria` returned empty; the schema has no way to set it). No robustness view.
- How to use it here: B1 Step 5, only on scores and weights the person gave. Name criteria so higher is better ("effort avoided", not "effort"). Report ties in plain words. Never fill a missing score.

## analytics.rice (counted, not measured here)

- Ranks initiatives with reach, impact, confidence and effort the person supplies. An alternative to `analytics.mcda` in B1 if the person already scores that way. Not called in this build; read its returned method before relying on it.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. Observed: with the name "Claude" it refused ("build_record refuses a record without a human cleared_by.name").
- Call it only when an output leaves the conversation and the person names who clears it.

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "partnerships"}` returned the Digital Partnerships Director (`digital-partnerships-director`), the worker for this skill, with the Partnerships Manager and the Access & Reimbursement Lead. Queries "customer success" returned nothing and "implementation" returned unrelated experts: no customer success expert is in the catalogue.
- `download_agent {expert: "digital-partnerships-director"}` returned 108,025 characters, version 16 October 2026. Its bound skills include the six old tasks of this competency and its sibling (Renewal horizon, Growth offer, Renewal risk note, Renewal rate definition, Cohort score, Expansion result). Its stop rules are a source of `governance.md`. Its prompt says "50 bound" skills and "29" tools while the file carries 87 skills and 45 tools, including UniProt, ChEMBL and PubChem.
- Offer the download only when the person wants the role on their own assistant.


## Catalogue jobs (list_jobs, get_job, find_job, start_job)

Measured 19 October 2026 (`examples/live/list_jobs_commercial.json`). `list_jobs` returned 13 Commercial jobs, all `available`. `start_job` takes only `job_id`; it returns the method steps, the tool names and the inputs of the non-Verify tools, and "does not run the buyer's model". The assistant then makes the calls itself. Every job closes with the seven `verify.*` tools; `verify.build_record` still needs a named human. Prices in the job list are hypotheses, not charges.

Connector finding (all three new jobs): the jobs list `analytics.segmentation`, `analytics.scenario-modeler` and `analytics.risk-tornado`, and `start_job` describes their inputs, but the connector exposes only four analytics tools (`mcda`, `rice`, `budget-impact-model`, `vba-price-anchor`). A search for those names returned none of them. When a job reaches one of these steps the output shows `[GAP] ...: tool not exposed`; nothing is computed in its place.

### health-system-value-brief (pricing A2 and B1; account growth A2), live run on somnio with illustrative numbers

- Steps returned: price corridor and, if asked, literature first; a collected number enters a calculator only if the seller adopts it; budget impact; price anchor; scenario and tornado when the seller gives a formula and a period count; print a gap if a calculator rejects the payload; do not store; close with Verify.
- Calls made: `get_pricing_corridor {reference: "somnio"}`; `literature.search_literature {query: "digital cognitive behavioral therapy for insomnia health care costs", limit: 3}`; `analytics.budget-impact-model` (population 2,000, two-option current mix, new cost 400, uptake [0.1, 0.2, 0.3], all ILLUSTRATIVE); `analytics.vba-price-anchor {comparator_cost_per_patient: 900, incremental_qalys: 0.02, wtp_thresholds: [50000, 100000]}` (ILLUSTRATIVE). Saved: `examples/live/job_health_system_value_brief_somnio.json`.
- What came back: corridor of 12 rows, one of them somnio's own price (224.99 EUR, DiGA 00508, with source URL), a duplicate without URL, and ten other DiGA prices with no product names (register N4); literature answered with three records, none carrying a cost figure, and labeled a published BJGP Open paper "preprint"; budget impact HTTP 422 (nothing counted; register N5); price anchor 1,900 and 2,900 (900 + 0.02 x threshold; defaults offset 0, units 1).
- Pitfalls: (1) scenario-modeler and risk-tornado are not exposed; (2) the budget impact calculator still rejects every payload shape tried; (3) corridor rows other than the product's own must be dropped before any number is offered for adoption.
- What it leaves as a gap: budget impact (calculator), scenario and sensitivity (tools not exposed), any number the seller has not typed or adopted.

## Not used here

- `find_job`: `{query: "renewal expansion customer success"}` returned no job. The library has no customer success job.
- `verify.check_claim` for a literature result quoted in a deck: if needed, `verify.qualify_source` first, then `check_claim` with a passage read in the same direction as the claim (register item N3). Not called in this build.
- `watch_*` tools.

## Local helper

- `scripts/renewal_metrics.py horizon ACCOUNTS.csv DEFINITIONS.json` lists renewals inside the person's horizon with readiness on the person's rule, and flags open accounts whose renewal date has passed. It refuses to run without an as-of date and a horizon. Tested on 19 October 2026 on `examples/sample-data/`.
