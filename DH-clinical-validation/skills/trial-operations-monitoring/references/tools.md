# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `literature_find_trial`). Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026. Saved outputs are in `examples/live/`. No library job covers trial operations: `find_job {query: "trial"}` returned no match and `list_jobs` lists none, so the Catalogue job slot in every task is "none".

## literature.list_sources (free)

- No arguments. Observed loaded: pubmed, europepmc, openalex, crossref, biorxiv, clinicaltrials, semantic_scholar, unpaywall. Not loaded (gap true): consensus, cochrane, prospero, embase, scopus, web_of_science.
- Say which indexes were searched whenever you report "no comparable trial found".

## literature.search_literature (counted)

- `query` (required), `limit` 1 to 50, `filters` (`date_from`, `date_to`, `designs[]`, `language`).
- Used in A2 step 4 only when the trial has no NCT number (for example a registry the library does not read): search by trial title or acronym to find publications. Otherwise use `find_trial`.
- Observed with `{query: "decentralized randomized trial remote enrollment wearable digital health technology", limit: 5, filters: {date_from: "2022-01-01"}}`: five records, 15 merged hits, a bioRxiv warning that it has no keyword search.
- Pitfalls seen:
  - `trial_ids` was empty on every record, including one labeled `rct` with confidence 0.98 (register item N8). Get the registration with `find_trial` instead.
  - Design labels are unreliable: a scoping review came back as `systematic_review` (0.78); a survey and a conference abstract came back as `other` (0.3). Read the abstract before naming a design (N8).
  - Authors can be empty and DOI null (a 2026 Europe PMC record). Cite by PMCID then.

## literature.find_trial (counted)

- `nct_id`, or `record` (a paper record). Returns `registrations` and `publications`.
- With `nct_id: "NCT04885530"`: the registration (title, `status` COMPLETED, `phases` PHASE3, `sponsor`) and five linked publications, three of them preprints.
- With a paper `record` carrying a PMID that the registry lists (JAMA Internal Medicine paper, PMID 40658388): the registration was found (`match_via: "pubmed_secondary_id"`).
- With a paper record the registry does not list (a participant-experience paper from the same trial): nothing, warning "no linked registration found". That is a gap of the link, not proof the trial is unregistered.
- Missing fields: no registration landing URL, first-submitted date, start date, primary completion date or results-posted date. Registration timing cannot be checked from this tool; ask the person or read ClinicalTrials.gov directly.

## How A2 uses find_trial

Call `{nct_id: "<the person's NCT number>"}`. Report `status`, `phases`, `sponsor` and each linked publication (preprint or journal) with its DOI. Then say that registration, primary completion and results dates are not in the library output and come from the person or the registry page. A registration found from a journal paper is reported with `match_via`.

## verify.qualify_source and verify.check_claim (counted)

- Working sequence for a paper: `qualify_source {doi, question}` then `check_claim {claim, passage: {text, locator}, source: <the whole qualify_source object>}` (register item C18; a DOI alone returns "unverifiable").
- V3 (DOI 10.1038/s41746-020-0260-4): `qualify_source` rated it gold. A faithful restatement of the verification passage returned "partial" with the rationale "the passage does not state the figure" although the claim had no figure; a negated claim returned "unsupported" (38 percent overlap), not "contradicted" (N3). Accept a claim only when you have read the passage in the same direction.
- The citation inside `check_claim` came back with authors empty, year null and identifiers null (C18). Build the citation from the research row or from `qualify_source`.
- Regulator guidance is not checkable: `qualify_source {url: "https://www.fda.gov/media/167696/download"}` (FDA DCT guidance) returned tier "inadmissible", "no provenance", and both a faithful claim and its negation then returned "unverifiable" (C1). Cite the research row and its quote instead.

## regulatory-dh.retrieve_guidance (counted)

- `{query: "decentralized clinical trial digital health technology remote data acquisition source data", limit: 5}` returned no passage. The store holds no trial-operations guidance (C6). Do not use it in this skill.

## agent-pack.list_experts and download_agent

- `list_experts {query: "clinical operations"}` returned nothing; `{query: "clinical"}` listed `clinical-informatics-lead`, `digital-clinical-trials-director` and `clinical-validation-director`. The worker bound here is `clinical-informatics-lead`; its stop rules are quoted in `examples/live/catalogue_and_experts.json`.

## verify.build_record (counted)

- Needs a named human in `cleared_by`; refuses a tool or model name. Use it only when an output leaves the conversation.

## Open access

- When a source is open access, read the full text before marking a field `[GAP]` from an abstract.

## Not used here

- `watch_*` tools: not called.
- `literature.grade_evidence` and `classify_study`: grading is the literature review skill's work (dh-clinical-validation 4.1, literature-and-real-world-evidence-review). Point there.
- `analytics.mcda` and `analytics.rice`: not needed; B1 checks rules, it does not rank sites. If the person wants a ranked repair list from their own scores, use `analytics.rice` (register N5: confidence is a percent).
