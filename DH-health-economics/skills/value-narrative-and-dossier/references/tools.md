# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `literature_get_record`). Counted calls draw on the library key's monthly allowance. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## Catalogue jobs (find_job, get_job, list_jobs)

- `value-dossier` ("Payer value dossier outline", "A dossier skeleton, with every claim checked") has status `design_partners`, `startable: false`, `tools: []`. Do not try to start it. Say "the library's dossier job is open to design partners only; this skill builds the dossier with direct calls" and run task A2.
- `evidence-table` is available and lists `literature.search_literature`, `get_record`, `find_trial`, `grade_evidence`, `check_retraction`, `build_evidence_table` and the seven Verify tools. It is the one-call option for A1's evidence part; the task steps below remain the method, because the job does not run the same-direction reading.
- `budget-impact` is listed available ("buyer supplies inputs") but its tool returned HTTP 422 (see below).

## literature.search_literature (counted)

- `query`, optional `limit`, `filters` (`date_from`, `date_to`, `designs[]`).
- Pitfall (register N8): design labels are not reliable. Two trial protocols came back `design: "rct"` (0.78); in a cost-effectiveness search a published JMIR mHealth and uHealth article with a PMID was labeled `preprint` (0.95) because it has a preprint DOI. Check the design against the paper before using it.
- Pitfall: `trial_ids` empty on every record.
- Use it only to find records the person has not named. A review is the job of dh-clinical-validation (literature-and-real-world-evidence-review).

## literature.get_record (counted)

- `doi`, `pmid`, `pmcid` or `openalex_id`. Returns the merged record and an `excerpt`.
- Pitfall: the excerpt can stop before the Results. For Felder et al. 2020 it ended at "Design, setting, and participants". The Results passage had to be read from Europe PMC (`examples/live/abstract_felder_2020.txt`). Never check a claim against an excerpt that holds only aims or design.
- Pitfall (N8): `trial_ids: []` although the abstract names ClinicalTrials.gov NCT02805998.

## literature.grade_evidence (counted)

- `record` or `records`, `standard` (`cebm2011` default or `grade`), `question_type`.
- With `grade`: returned `level: "high"`, `draft: true`, `provisional: true`, rule "starting certainty 'high' from design 'rct'; downgrade factors left empty for a human reviewer". This is the starting level of ES-90 for one record, not a certainty for an outcome (ES-96). Never report it as certainty.

## literature.build_evidence_table (counted)

- `records`, optional `passages` (map of `record_id` to text), `question` (PICO), `question_type`, `standard`.
- Returned CEBM 2011 level "2" and a field `grade_confidence: 0.98` that equals the design-label confidence, not a GRADE rating. `population` came back `[GAP]` although the passage names the women randomized; `effect` was cut mid-word ("time-by-grou..."), dropping the confidence interval; `landing_url: null`. Use the table for identifiers and authors; take effects from the passage you read.

## literature.check_retraction and verify.check_currency (counted)

- Both by `doi`. Both answered from Crossref only ("none"; `current: true`). ES-123 notes retraction display is inconsistent across sources: say which source was checked.

## verify.qualify_source and verify.check_claim (counted)

- Sequence: `qualify_source` with the DOI (rated gold, score 67, for Felder 2020), then `check_claim` with `claim {text}`, `passage {text, locator}` and the full returned source object (register C18: a DOI alone returns "unverifiable").
- Pitfall (N3): overlap decides. Faithful claim "supported" (67 percent); population widened to all adults "supported" (77 percent); a claim the passage contradicts "unsupported" (17 percent), not "contradicted". Read the passage yourself; accept only same direction and same population.
- Pitfall (C18): the citation returned has DOI, PMID, authors and year empty. Cite from `qualify_source` or `build_evidence_table`.
- Guidance documents: the AMCP 6.0 draft PDF URL was rated "inadmissible", "no provenance", score 6 (register C1). Rules from guidance come from the research rows, not from Verify.

## verify.extract_claims (counted)

- Splits by sentence. "It is cost-effective for every US health plan and will save money in year one." came back as one factual, checkable claim, although it joins two forward-looking claims. Split joined claims yourself before `check_claim`.

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`. `{name: "Claude"}` returned "build_record refuses a record without a human cleared_by.name". Call it only when an output leaves the conversation, with the person the user names.

## market-access-dh.retrieve_guidance (counted)

- "AMCP Format formulary submission dossier" and "NICE evidence standards framework budget impact analysis" returned no passage (register C6). Do not use it for dossier or ESF rules; use the references.

## analytics.budget-impact-model (counted when it answers)

- Returned HTTP 422 ("Nothing was counted") with `current_mix` of two items and `uptake_curve` as `[{year, uptake}]` (register N5, fourth build). If the person needs BIA arithmetic, do it in the conversation on their numbers, labeled hypothesis, with the BIA II elements (HE-019, [PAPER] DOI 10.1016/j.jval.2013.08.2291), and point to DH-01.07.2 for the model.

## agent-pack.list_experts (free)

- `{function: "digital-regulatory-evidence"}` lists eleven experts; none is a health-economics or value-dossier role. `{query: "health economics"}` returned none. The bound worker stays `digital-health-access-reimbursement-lead`.

## Not used here

`watch_*` tools; `commercial-dh.audit_claims` (marketing claims belong to dh-commercial); market-access status tools (dh-market-access).
