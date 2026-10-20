# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Behavior below was observed in live calls on 19 October 2026 (condensed outputs in `examples/live_calls_2026-10-19.json`). Patient-level data never goes into a library call.

## The short version

The library resolves papers, links ClinicalTrials.gov registrations, checks retractions and currency, and drafts a GRADE starting level. It does not assess risk of bias, does not read methods sections, and its design labels are unreliable. Every domain fact in A1 comes from the paper's full text, quoted with a locator.

## literature.get_record (A1 step 1)

`{doi: "10.2196/59145"}`: merged record with PMID, PMCID (PMC11635337), six source provenance entries, `design: cohort` (0.45), `trial_ids: []`, and an excerpt from the abstract background only. Use the PMCID or `oa_url` to open the full text.

## literature.classify_study (A1 cross-check only)

`{record: <the same record>}`: `cohort`, 0.45, decided by `publication_type_raw: observational study`, rule `metadata:weak`. The same DOI was labeled `preprint` (0.95) by `search_literature`, and a claims matched-control study was labeled `guideline` (0.6) (register N8). Record the label beside the design read from the paper; never the other way round.

## literature.find_trial (A1 step 4)

`{record: ...}` for both studies measured: `registrations: []`, "no linked registration found". Only ClinicalTrials.gov is searched. Write "no ClinicalTrials.gov link found by the library; registration not confirmed `[GAP]`". `literature.list_sources` shows PROSPERO not loaded and no source for ENCePP or the HMA-EMA Catalogue of RWD studies.

## literature.check_retraction and verify.check_currency (A1 step 5)

`check_retraction {doi: "10.36469/001c.146434"}`: `none`, Crossref only. `check_currency {doi: "10.2196/59145"}`: current; not retracted, corrected, superseded or withdrawn; notices from Crossref. Name the source checked; Cochrane notes that retraction status displays inconsistently (ES-123).

## literature.grade_evidence (context only)

`{record, standard: "grade", question_type: "treatment"}`: `low`, draft, provisional: "starting certainty 'low' from design 'cohort'; downgrade factors left empty for a human reviewer". It reads the design label, so a wrong label gives a wrong start (N8). Report it as "draft starting level from the library", never as the certainty.

## verify.qualify_source and verify.check_claim (when a domain fact is restated)

- `qualify_source {doi: "10.2196/59145", question}`: `gold`, 78. Pass the full object as `source` (C18).
- `check_claim` returned `supported` for a faithful association (54%), a causal overstatement (44%) and a reversed claim (100%) against the same results passage (register N3). Use it only as a record of which passage you relied on; the reading is yours.
- `qualify_source {url: "https://www.fda.gov/media/190201/download"}`: `inadmissible`, "no provenance" (C1). Cite regulator rules to their CV row.

## verify.build_record (B1 sign-off)

Refused `cleared_by.name: "Claude"`: "build_record refuses a record without a human cleared_by.name". Intended. Call only when an output leaves the conversation, with the person's named clearer; aggregates only.

## Catalogue jobs

`find_job {query: "evidence table"}`: `evidence-table` (available; owner Access and Reimbursement Lead). It grades from design labels and flags retractions; it does not assess risk of bias. `find_job {query: "real-world evidence outcomes study"}`: no match.

## scripts/rigor_tally.py (local)

Tested on `examples/illustrative_judgments.csv` with `examples/illustrative_rule.json` and with an empty rule: applies ES-77 (ROBINS-I critical) and ES-74 (RoB 2 least favorable) always; the ROBINS-I overall otherwise only under the person's rule; scores only when the person gave points for every judged level and every domain is judged.

## Not used here

`watch_*` tools; analytics tools (ranking studies by an MCDA would turn judgments into a score the sources do not support; if the person insists on a ranking, it is their scores and their weights, labeled as such).
