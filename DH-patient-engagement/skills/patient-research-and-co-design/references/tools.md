# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `literature_search_literature`). Counted calls draw on the library key's monthly allowance; free calls do not.

This competency runs mainly on the sourced references and the person's own session files. The library adds published co-design studies as comparables, a check that a quoted passage supports a claim, a ranking calculator for points the person scored, and the record. The person's session data, words and codes never go into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## literature.list_sources (free)

- No arguments. Observed: PubMed, Europe PMC, OpenAlex, Crossref, bioRxiv/medRxiv, ClinicalTrials.gov, Semantic Scholar and Unpaywall loaded; Consensus, Cochrane Library, PROSPERO, Embase, Scopus and Web of Science not loaded (gap true).
- Say once when a search matters: Cochrane, Embase and Scopus are not searched.

## literature.search_literature (counted)

- Arguments: `query`; optional `limit` (1 to 50), `filters` (`date_from`, `date_to`, `designs[]`, `language`), `sources`.
- Use in A1 Step 3 to find published co-design studies for the same condition or product type, as comparables for method choices. Query shape that worked: "co-design" plus condition plus product type plus "patients", for example `{query: "co-design type 2 diabetes self-management app patients", limit: 5, filters: {date_from: "2020-01-01"}}` (16 merged records; one of five shown was a co-design study by title).
- Pitfalls seen:
  - The search is lexical: "co-design" in the query does not restrict results to co-design studies. Read each title; keep only records whose title or excerpt says co-design, co-production, participatory or experience-based co-design.
  - Design labels are unreliable for qualitative work: a "co-produced qualitative study" came back as `rct` (0.6); a published JMIR Diabetes qualitative study came back as `preprint` (0.95) because its preprint DOI was merged in; scoping reviews come back as `systematic_review`. Report the design as the title states it and say the library label differs.
  - Most records have an empty `excerpt`; where present it is usually the introduction or aims. `trial_ids` was empty on every record.
  - Two calls returned "could not answer this call (503) ... Nothing was counted"; a retry about two minutes later worked.
- Describe a study only by what its record states (title, venue, year, design as titled). Never state its findings from the title.

## literature.get_record (counted)

- Arguments: one of `doi`, `pmid`, `pmcid`, `openalex_id`. Returns the merged record with identifiers, venue, OA URL and per-source provenance.
- Observed on doi 10.1177/20552076231219117: full identifiers and OA URL; `publication_type_raw` includes "Scoping Review" while `design` says `systematic_review`; the excerpt is the introduction only, so no finding can be checked from the record alone.

## literature.classify_study (counted)

- Argument: `record`. Observed on the "co-produced qualitative study": `other` at 0.3, "no decisive metadata or text cue", although the same record carried `rct` in the search. Do not rely on it for qualitative or co-design designs.

## verify.qualify_source and verify.check_claim (counted)

- Working sequence (register item C18): `qualify_source {doi, question}` first, then `check_claim {claim: {text}, passage: {text, locator}, source: {doi}}` with a passage you have read in the paper.
- Observed: GRIPP2 (doi 10.1136/bmj.j3453) qualified as tier "gold", status current, score 67. A claim matching the quoted passage returned "supported" (64 percent overlap).
- Pitfall (register item N3): a claim the passage contradicts (34 items instead of five, main focus instead of secondary) returned "partial" (42 percent overlap), not "contradicted". Accept a claim only when the passage states the same thing in the same direction; read the passage yourself and treat "partial" as unverified.
- The returned citation was empty (title null, no authors, Harvard "Unknown (n.d.)"). Build the citation from the research row or `qualify_source` output instead.
- Use it when a plan or report cites a published method beyond the research rows.

## analytics.rice (counted)

- Arguments: `initiatives`, each `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. Every number is the person's.
- Pitfall: `confidence` is read as a percentage. Passing 0.8 returned confidence 0.008 and a score of 9.6; passing 80 returned 0.8 and a score of 960. The order did not change, but the scores are a hundredfold off. Pass confidence as a whole-number percent and report back what the tool echoed.
- `name` is null in every result; the note about price figures is unrelated to RICE.
- Use in B1 only to order design changes the person scored. Reach and effort come from the person's own figures; the model never estimates them.

## analytics.mcda (counted, not called in this build)

- Ranks options the person scored on a 0 to 4 scale with weights; every criterion is treated as higher-is-better and no robustness view is returned (register C17, measured in other builds). Offer it in B1 if the person prefers weighted criteria to RICE.

## regulatory-dh.retrieve_guidance (counted)

- Observed: "patient preference information" returned no passage; "co-design" returned five chunks of journal articles, each with `source_url` "[GAP]" and `retrieved_at` null, one carrying its own DOI in the text. The store does not hold the PFDD, PPI, HTA Regulation or Common Rule texts. Do not cite these passages; the research rows replace the store for this skill (register C6).

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "patient"}` returned ten of sixteen matches, including the Patient Experience Designer (the worker for this skill), the UX Research Lead and the Health Equity & Digital Access Lead.
- `download_agent {expert: "patient-experience-designer"}` returned 66,165 characters: a system prompt, 56 bound skills (including the six old co-design tasks) and 36 tool names. Its stop rules are the source of `governance.md`. Offer it only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. Observed: with the name "Claude" it refused ("build_record refuses a record without a human cleared_by.name").
- Call it only when an output leaves the conversation and the person names who clears it. Never put participant words or codes in the record text; summarize decisions by insight id.

## Not used here

- `watch_*` tools.
- `verify.verify_text` with bare DOIs (returns unverifiable, register C18).

## Local helper

- `scripts/insight_tracker.py` (no connector): `check`, `tally`, `status`, `trace`, `fit` on the person's CSV files (`references/insight-log.md`). Tested on 19 October 2026 on the illustrative files in `examples/sample-data/`; `check` also flagged a test row holding an email address and a phone number.
