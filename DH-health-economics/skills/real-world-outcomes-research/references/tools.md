# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Behavior below was observed in live calls on 19 October 2026. Patient-level data never goes into a library call.

## literature.list_sources (free)

Loaded: PubMed, Europe PMC, OpenAlex, Crossref, bioRxiv/medRxiv, ClinicalTrials.gov, Semantic Scholar, Unpaywall. Not loaded (`gap: true`): Cochrane Library, PROSPERO, Embase, Scopus, Web of Science, Consensus. No source for the HMA-EMA Catalogue of RWD studies or ENCePP. So the library cannot check an EU non-interventional study registration (CV108) or a review protocol on PROSPERO; ask the person for the registration record.

## literature.search_literature (A1: prior record)

- `{query: "digital cognitive behavioral therapy for insomnia real-world hypnotic prescriptions health care utilization", limit: 6}` returned 6 of 16 merged records; two were on topic (a 2025 US claims matched-control cost study, DOI 10.36469/001c.146434; a 2026 short paper), the rest were reviews or off topic.
- `{query: "real-world effectiveness digital therapeutic observational cohort health care utilization", limit: 8}` returned 8 of 29; four on topic.
- Pitfalls: design labels are unreliable (register N8). The claims cost study was labeled `guideline` (0.6); an EHR cohort study published in JMIR Mental Health was labeled `preprint` (0.95) in search and `cohort` (0.45) by `get_record` for the same DOI. `trial_ids` was empty on every record. Read the paper's methods before stating a design. Results rank loosely; run two or three phrasings and keep only records you have read.

## literature.get_record

`{doi: "10.2196/59145"}` returned the merged record with PMCID, six source provenance entries and an excerpt from the abstract background only. The excerpt is not the result. For a passage, open the full text (the `oa_url` or Europe PMC) and quote it with a locator.

## literature.find_trial (A1 and A2)

`{record: {doi: "10.2196/59145", ...}}` and `{record: {doi: "10.36469/001c.146434", ...}}` both returned `registrations: []` with the warning "no linked registration found". Only ClinicalTrials.gov is searched. "No linked registration found" is not "not registered": write "no ClinicalTrials.gov link found by the library; registration not confirmed `[GAP]`" and ask the person for the registry and id.

## literature.classify_study and literature.grade_evidence

- `classify_study` on the JMIR record: `cohort`, confidence 0.45, decided by `publication_type_raw: observational study`, rule `metadata:weak`.
- `grade_evidence {standard: "grade"}`: level `low`, draft, provisional, "starting certainty 'low' from design 'cohort'; downgrade factors left empty for a human reviewer". That matches ES-90 as a starting point only. Never report it as the certainty of the evidence; the factors are the person's.

## literature.check_retraction and verify.check_currency

`check_retraction {doi: "10.36469/001c.146434"}`: `status: none`, checked Crossref only. `check_currency {doi: "10.2196/59145"}`: current, not retracted, corrected, superseded or withdrawn, notices from Crossref. State the source checked.

## verify.qualify_source then verify.check_claim (B1 wording check)

- `qualify_source {doi: "10.2196/59145", question: ...}`: tier `gold`, score 78. Pass the whole returned object as `source` to `check_claim` (register C18: a bare DOI returns unverifiable).
- `check_claim` with the abstract's results passage ("App-augmented treatment was associated with a significant decrease in emergency department visits ...") returned `supported` for the faithful claim (54% overlap), for a causal overstatement ("The app causes a reduction ...", 44%) and for the reversed claim ("associated with an increase in emergency department visits", 100%). The tool decides on word overlap (register N3). Accept a claim only when you have read the passage and it says the same thing in the same direction, with the same hedge ("associated with" is not "causes"). The returned citation had empty identifiers and null year (C18).
- `qualify_source {url: "https://www.fda.gov/media/190201/download"}` (FDA device RWE guidance): tier `inadmissible`, "no provenance" (register C1). Cite regulator rules to their CV row instead.

## verify.build_record (counted)

With `cleared_by.name: "Claude"` it refused: "build_record refuses a record without a human cleared_by.name". That is intended. Call it only when an output leaves the conversation and a named person clears it. Put aggregates in the record, never patient-level data.

## market-access-dh.retrieve_guidance

`{query: "real-world evidence study protocol analysis plan prespecified before outcome data relevance reliability", limit: 5}`: `results: []`, "no passage retrieved" (register C6). The guidance store holds no RWE method; use `references/`.

## Catalogue jobs

`find_job {query: "real-world evidence outcomes study"}`: no match. `find_job {query: "evidence table"}`: `evidence-table` (available, owner Access and Reimbursement Lead, tools literature and Verify). It tabulates published studies; it does not design or execute a study. A1 may use it for the prior record.

## scripts/prespec_check.py (local, not a library call)

Reads a JSON study log and checks prespecification order, revision stamps and deviations. Tested on `examples/illustrative_study_log.json`.

## Not used here

`watch_*` tools; analytics tools (no computation in this competency needs them; budget impact belongs to dh-health-economics 2.x).
