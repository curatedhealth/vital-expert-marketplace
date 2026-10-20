# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was disconnected during this build (20 October 2026; a tool search for the library returned no tools), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026). Where a tool has no saved output for this skill's use, the step is marked **needs a live check**. Most of this skill runs on the person's own files through `scripts/prep_check.py`; the library is used only to find and read a published paper the person needs (a validation of an operational definition, a method paper) and to clear the record.

## literature.search_literature (counted; A1 step 2, A2 step 3, optional)

- Arguments: `query` (plain words, not a Boolean string), `limit` 1 to 50, `filters` {`date_from`, `date_to`, `designs[]`}, `sources[]`.
- Saved: `literature_search_2026-10-19.json` (a digital CBT for insomnia query, limit 8, retrieved 19 October 2026): 32 hits, 29 after merge, 8 returned; sources answering PubMed, Europe PMC, OpenAlex, Crossref, bioRxiv; Semantic Scholar and ClinicalTrials.gov did not answer; off-topic records ranked in; `trial_ids` empty on every RCT (register N8); excerpts mostly empty.
- Use here: to find a published validation study of the person's operational definition (for example a heart failure readmission code algorithm) or a method paper. **Needs a live check** for that query type. A record found is a candidate; its sensitivity, PPV or method statement is accepted only from a passage read in the paper (CV81).

## literature.get_record (counted)

- One of `doi`, `pmid`, `pmcid`, `openalex_id`.
- Saved: `get_record_malloy.json` (`{doi: "10.1177/20552076231219117"}`, retrieved 19 October 2026): a scoping review stored as `systematic_review`; the excerpt is the introduction only, with no results passage.
- Pitfalls: design labels can be wrong (register N8); an excerpt without results cannot support a performance figure. Read the paper's results section before quoting any figure.

## verify.qualify_source then verify.check_claim (counted)

- Saved: `qualify_source_fabbri.json` (`{doi: "10.1136/bmj.l6925", question: ...}`): tier "gold", status "current", source_score 67. `check_claim_fabbri.json`: two calls with only `{doi, source_id}` as source returned 502 (nothing counted); passing the full `qualify_source` result worked (register C18). A claim stating the passage's figure and its reversal ("Most ... disclosed") both returned "supported" on word overlap (register N3). The returned citation had no DOI, authors or year (register C18).
- Rule: accept a published figure only when you read the passage and it states the figure in the same direction; record the tool status beside your reading. Use the paper's own citation, not the tool's.

## verify.build_record (counted)

- Saved: `verify_build_record_refusal.json`: `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when an output leaves the conversation and the person names who clears it.

## Catalogue jobs

- `list_jobs_2026-10-19.json` lists no job for cohort definition, data preparation, statistical analysis, prediction modeling or forecasting. Every task's formula row says "Catalogue job: none".

## Not used here

- `analytics.*`: no analytics tool computes cohort attrition, leakage, splits, Bayesian posteriors, holdout metrics or forecast baselines; `scripts/prep_check.py` does this on the person's files. `analytics.scenario-modeler` and `analytics.risk-tornado` apply default ranges of plus or minus 20 percent (saved in other builds) and are not a substitute for the person's prior sensitivity.
- `regulatory-dh.*`: device status and AI device records route to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Every `watch_*` tool: never called.

## Steps that need a live check

- `literature.search_literature` for a phenotype or code-algorithm validation query (A1 step 2).
- `literature.get_record` on a statistics method paper the person names (A2 step 3).
