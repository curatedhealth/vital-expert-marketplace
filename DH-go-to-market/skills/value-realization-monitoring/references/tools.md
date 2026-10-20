# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `verify_qualify_source`). Counted calls draw on the library key's monthly allowance.

This is a method pack: there is no customer success suite in the library, and `find_job {query: "customer health value realization outcomes"}` returned no job (19 October 2026). The skill runs on the person's own account file, target versions, sent notes, the sourced references and `scripts/account_health.py`. The library adds literature records for instruments, Verify for claim checks and sign-off, and a ranking calculator for actions the person scored. The person's account data never goes into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## literature.search_literature (counted)

- Arguments: `query`; optional `limit`, `filters`, `sources`.
- Observed: `{query: "PHQ-9 validity brief depression severity measure", limit: 5}` put "The PHQ-9" (Kroenke 2001, DOI 10.1046/j.1525-1497.2001.016009606.x, PMCID PMC1495268) first and Löwe 2003 on sensitivity to change fifth; ranks 3 and 4 were off-topic 2026 papers. `excerpt` was empty for both PHQ-9 papers; `design` "other" at 0.3 confidence.
- Use: in A2, only when a sent note cites a published paper, to find its record and identifiers. Do not take a cut point or band from a search result; use the CS rows.

## literature.get_record (counted)

- Arguments: one of `doi`, `pmid`, `pmcid`, `openalex_id`.
- Observed: `{pmid: "16717171"}` (GAD-7, Spitzer 2006) returned the record with `pmcid` null, `oa_url` null and an excerpt that stops at the methods. The cut point is not returned, so GAD-7 bands stay `[GAP]` (CS93).

## verify.qualify_source then verify.check_claim (counted)

- `qualify_source {doi, question}` rated the PHQ-9 DOI tier "gold". Pass its `source_id`, `tier` and `source_type` as the `source` object to `check_claim`; a bare DOI in `source` returns unverifiable (register C18).
- `check_claim {claim: {text}, passage: {text, locator}, source}` returned:
  - "supported" (87 percent overlap) for the PHQ-9 band claim with the CS92 passage;
  - "supported" (71 percent overlap) for the wrong claim "A PHQ-9 score of 10 represents severe depression" from the same passage, which says 10 is moderate;
  - "unsupported" (20 percent) for "The program is clinically proven to reduce depression".
- Pitfall: the status follows word overlap, not meaning (register N3). Accept "supported" only after reading the passage and confirming it states the claim in the same direction. The returned `citation` has title null, no authors, year null (register C18); cite from the research row instead.
- `qualify_source {url}` on the NICE ESF PDF returned "inadmissible", "no provenance" (register C1). Regulator and NICE documents cannot be checked through Verify; the research rows carry the quote and URL.

## verify.extract_claims (counted)

- `{text}` split a three-sentence value note into three claims, `kind` numeric, numeric and factual, all `checkable: true`. The third joined an effect claim and a forward cost promise ("will cut your behavioral health costs") into one claim marked checkable. Split such sentences yourself; a forecast is never checkable against a signal row.
- Use: in A2 Step 2, to list each claim in a sent note before matching it to a signal row, with the person's agreement to pass the note text.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. With "Claude" it refused: "build_record refuses a record without a human cleared_by.name". Call it only when an output leaves the conversation and the person names who clears it.

## analytics.rice (counted)

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. The person supplies every number.
- Observed: with confidence 0.8 and 0.5 the response showed confidence 0.008 and 0.005 and scores 0.48, 0.75 and 0.8, one hundredth of Reach x Impact x Confidence / Effort (expected 48, 75 and 80). Two retries returned 503, "Nothing was counted". A later call with confidence 80 and 50 returned confidence 0.8 and 0.5 and scores 80 and 50, as expected.
- Pitfall: pass `confidence` as a percent (80 for 80 percent). A fraction is divided by 100 again without warning; the order survives only if every confidence is scaled alike.
- Use in B1 only to rank corrections the person scored. Check the order by hand (Reach x Impact x Confidence / Effort) and report the person's own arithmetic, not the tool's score. If the tool fails, rank by hand and say so. `analytics.mcda` is the alternative when the person scores on criteria with weights (0 to 4 scale; every criterion higher-is-better, register C17).

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "adoption"}` returned six experts including the Digital Adoption Lead (`digital-adoption-lead`), the worker for this skill, and the Digital Adoption Manager.
- `download_agent {expert: "digital-adoption-lead"}` returned 79,671 characters. Its skills include "Health threshold review", "Value evidence check" and "Unsupported note owner", the register tasks this skill replaces. Its never and stop rules are the source of `references/governance.md`. Its "Bound competencies (6)" list does not name this competency (register C14) and the prompt carries plumbing such as "trust the foreign key" (register C15). Offer the download only when the person wants the role on their own assistant.

## Not used here

- `watch_*` tools; commercial-dh and market-access-dh tools (no public product view is needed to track a customer's own outcomes).

## Local helper

`scripts/account_health.py` (no connector, shared with the sibling `outcome-tracking-and-customer-health`): `thresholds` and `notes` for this skill; `attain` and `health` when a fresh read is needed. Tested on 19 October 2026 on the illustrative files in `examples/sample-data/` (labeled illustrative); outputs in `examples/runs/`.
