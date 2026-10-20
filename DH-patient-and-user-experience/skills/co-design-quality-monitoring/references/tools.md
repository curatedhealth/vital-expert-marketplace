# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `verify_check_claim`). Counted calls draw on the library key's monthly allowance; free calls do not.

This competency runs mainly on the person's own files (sessions, captures, insights, changes). The library adds a check that a published method is cited correctly, a ranking calculator for repairs the person scored, and the record. The person's files, participant words and codes never go into a library call. Behavior below was observed in live calls on 19 October 2026 during the sibling build (DH-02.03.1.1); trimmed outputs are in `examples/live/`.

## verify.qualify_source and verify.check_claim (counted)

- Use in A2 when a co-design report cites a published method (GRIPP2, a co-design framework) and the person wants the citation checked.
- Working sequence (register item C18): `qualify_source {doi, question}`, then `check_claim {claim: {text}, passage: {text, locator}, source: {doi}}` with a passage you have read.
- Observed: GRIPP2 (doi 10.1136/bmj.j3453) qualified as tier "gold", status current, score 67. A claim matching the passage returned "supported"; a claim the passage contradicts (34 items, main focus, for the short form) returned "partial", not "contradicted" (register N3). Treat "partial" as unverified and read the passage yourself.
- The citation object came back empty (title null, Harvard "Unknown (n.d.)"); build the citation from the research row instead.

## literature.search_literature and literature.get_record (counted, optional)

- Only if the person wants published co-design studies as context for their own practice. Observed: lexical search, unreliable design labels for qualitative work (a co-produced qualitative study labeled `rct`, a published qualitative study labeled `preprint`, scoping reviews labeled `systematic_review`), mostly empty excerpts. Describe records by title only; never compare the person's co-design quality with a paper's.

## analytics.rice (counted)

- Arguments: `initiatives`, each `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`; every number the person's.
- Pitfall: `confidence` is read as a percentage. 0.8 became 0.008 (score 9.6); 80 became 0.8 (score 960). Pass a whole-number percent and report what the tool echoed.
- Use in B1 only to order repairs or open points the person scored.

## analytics.mcda (counted, not called in this build)

- 0 to 4 scores with weights; every criterion higher-is-better; no robustness view (register C17, measured in other builds). An alternative to RICE in B1.

## regulatory-dh.retrieve_guidance (counted, not useful here)

- "patient preference information" returned nothing; "co-design" returned five journal-article chunks with `source_url` "[GAP]". Do not cite them (register C6).

## agent-pack.download_agent

- The Patient Experience Designer download (66,165 characters) is the source of `governance.md`. Its bound competencies do not include the co-design competencies, although its skill list carries all six old co-design tasks (`examples/live/agent_pack.json`).

## verify.build_record (counted)

- Refuses a clearance named "Claude" ("build_record refuses a record without a human cleared_by.name"). Call it only with the human the person names. Summarize by insight and change id; no participant words or codes.

## Not used here

- `watch_*` tools; `verify.verify_text` with bare DOIs (register C18).

## Local helper

- `scripts/insight_tracker.py` (no connector): `check`, `tally`, `status`, `trace`, `fit`. Tested on 19 October 2026 on `examples/sample-data/`.
