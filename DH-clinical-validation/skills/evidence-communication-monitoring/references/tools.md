# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `literature_get_record`). Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026 on one test paper (Schuffelen et al., Depression and Anxiety 2025, DOI 10.1155/da/2171041, PMID 40458292). Trimmed outputs: `examples/live/`.

## literature.list_sources (free)

- Loaded: PubMed, Europe PMC, OpenAlex, Crossref, bioRxiv and medRxiv, ClinicalTrials.gov, Semantic Scholar, Unpaywall. Gap: Cochrane Library, PROSPERO, Embase, Scopus, Web of Science, Consensus. Say so whenever a statement depends on a search: a missing paper is a limit of these sources, not proof of absence.

## literature.search_literature and literature.get_record (counted)

- `search_literature {query, limit}` returns merged records with `design`, `design_confidence`, `trial_ids`, `excerpt` (the start of the abstract only) and per-source retrieval dates. `get_record {doi | pmid | pmcid}` resolves one paper.
- Pitfall (register N8): `trial_ids` was empty on every record, including a trial whose abstract names its registry id (DRKS00030919). A study protocol came back labeled `rct` (0.78). Check design and registry id against the paper, never from the label.
- Pitfall: `excerpt` is not the results. Ask the person for the results passage or the full text; do not build a statement from the excerpt.

## verify.qualify_source then verify.check_claim (counted)

- Sequence: `qualify_source {doi, question}` (the DOI rated `gold`, `status: current`), then `check_claim {claim: {text}, passage: {text, locator}, source: <the full qualify_source object>}` (register C18: a DOI alone returns "unverifiable").
- Pitfall (register N3), measured on one passage: the faithful claim with the outcome instrument named ("PHQ-9") returned `partial`, "the passage does not state the figure", because "9" is not in the passage; the same claim without it returned `supported` (62 percent overlap). A wrong comparator (antidepressants instead of waiting list) returned `partial` (50 percent). An overstatement ("proven to cure depression in all patient groups") returned `partial` (56 percent). So `partial` covers a faithful claim, a wrong comparator and an overstatement alike. Read every passage yourself: same direction, population, comparator, time point. Keep numbers and instrument names in a claim only if the passage states them.
- Pitfall (register C18): the citation inside `check_claim` has DOI, PMID, authors and year empty. Cite from `literature.build_citation` or the `qualify_source` result.

## literature.grade_evidence (counted)

- `standard: "grade"` returns `level: "high"`, `draft: true`, `provisional: true`, and every downgrade and upgrade factor `null`, rule "starting certainty 'high' from design 'rct'; downgrade factors left empty for a human reviewer". This is a starting level from the design label (ES-90), never a rating. Do not print it as certainty.

## literature.build_evidence_table (counted)

- `records`, `passages` (map of `record_id` to passage text), `question` (PICO), `question_type`, `standard`.
- Pitfall: with the results passage passed under the right `record_id`, `outcome` and `effect` still came back `[GAP]` and the warning asked for the passage that had been passed. Population was `[GAP]`; intervention and comparator were filled with arm sizes. Fill outcome and effect yourself from the passage read, and say the table was completed by hand.
- Pitfall: the row says `evidence_level: "high"` (GRADE start) while its citation says `evidence_level: "2"` with no standard named and `grade_confidence: 0.98` (the design confidence). Do not print either as a grade.

## literature.build_citation (counted) and verify.build_citation (free)

- `literature.build_citation {record, passage}` returned the full Chicago line with DOI, PMID and PMCID. Use it for references in a faithful wording. It reported `grade_confidence: 0.78` for the same record that `build_evidence_table` reported at 0.98; ignore both.

## literature.check_retraction and verify.check_currency (counted)

- Both returned "none" or `current: true` for the test DOI, checking Crossref only. Run one of them for every paper in a statement and say which source was checked.

## literature.find_trial (counted)

- `find_trial {record}` returned no registration for a DRKS-registered trial: it reaches ClinicalTrials.gov only. `find_trial {nct_id}` returned title, overall status, phase, sponsor, but no start, primary completion, first-submitted or results-posted dates and no landing URL. Registration and results clocks cannot be computed from it; take the dates from the registry record the person supplies.
- `verify.qualify_source` rated a ClinicalTrials.gov study page `inadmissible`, "no provenance" (register C1). Do not send registry facts to Verify.

## verify.extract_claims (counted)

- Splits by sentence, not by claim; every sentence is `checkable: true`, including "Certainty of evidence: high." Split compound sentences yourself.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Use only when an output leaves the conversation.

## literature.find_related (counted)

- `find_related {record, direction: "cited_by", limit}` returned ten citing papers via Semantic Scholar for the test paper, with no total count, empty citation intent and empty authors and venue on every row (`examples/live/find_related_cited_by.json`). One citing review came back with year 2026 and design `meta_analysis`, while `search_literature` returned the same DOI with year 2025 and design `systematic_review` (register N8). Use it to find where a trial is restated, for A2; never as an impact count.

## Catalogue jobs

- `evidence-table` (available): search, record, trial link, grade, retraction, evidence table, Verify. It is the buyer's one-call option for rebuilding an evidence base; the A2 checks remain the method, because its grade and table steps carry the pitfalls above.
- `value-dossier` (design partners, not startable): not used.
- `find_job {query: "evidence table literature citation"}` returned no match although `evidence-table` is listed by `list_jobs`. Use `list_jobs`.
