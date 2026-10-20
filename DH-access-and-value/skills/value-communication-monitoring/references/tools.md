# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them. Counted calls draw on the library key's monthly allowance. Observed in live calls on 19 October 2026; trimmed outputs in `examples/live/`. Task A1 and the tallying in B1 use no library call.

## Catalogue jobs

No catalogue job covers reception or narrative repair. `evidence-table` (available) can re-run the evidence rows for A2; the same-direction reading remains the method. `value-dossier` is design-partner only (measured in the sibling skill).

## literature.check_retraction and verify.check_currency (counted)

- Both by `doi`. For Felder et al. 2020 both answered from Crossref only: `status: "none"`; `retracted: false, corrected: false, superseded: false, withdrawn: false, current: true, notices: ["crossref"]`. Name the source checked (ES-123). A URL alone returns notices "not checked" (tool description).

## literature.search_literature (counted)

- Use `filters: {date_from: "<date the narrative was last checked>"}` to list candidate new studies. Live: `{query: "digital cognitive behavioral therapy insomnia cost-effectiveness", limit: 5, filters: {date_from: "2025-01-01"}}` returned 14 merged records, including two 2026 trials with economic outcomes and a 2025 meta-analysis.
- Pitfall (register N8): a published JMIR mHealth and uHealth article with a PMID was labeled `preprint` (0.95) because it carries a preprint DOI; two trial protocols were labeled `rct` in another search; `trial_ids` empty everywhere. Check each record against the paper.
- A hit is a candidate to read, never a finding that a claim changed.

## literature.get_record (counted)

- The `excerpt` can stop before the Results (Felder et al. 2020 stopped at the design). Re-read the Results passage from the paper or Europe PMC before any re-check.

## verify.qualify_source and verify.check_claim (counted)

- Sequence: `qualify_source` (DOI; gold, score 67 for Felder et al. 2020), then `check_claim` with the claim, the verbatim passage and the full source object (C18).
- Pitfall (N3): faithful claim "supported" (67 percent); population widened to adults "supported" (77 percent); a claim the passage states the opposite of "unsupported" (17 percent), not "contradicted". Your reading decides.
- Pitfall (C18): the returned citation has DOI, PMID, authors and year empty; cite from `qualify_source`.
- Guidance PDFs (AMCP 6.0 draft URL) rated "inadmissible", "no provenance" (C1). Guidance changes come from `references/currency-signals.md`, not from Verify.

## verify.extract_claims (counted)

- Splits a live narrative by sentence; a sentence joining two claims ("cost-effective for every US health plan and will save money in year one") comes back as one factual, checkable claim. Split joined claims yourself.

## verify.build_record (counted)

- Refuses a record without a human `cleared_by.name` (`{name: "Claude"}` refused). Use it only when the review or a repaired line leaves the conversation, with the person the user names.

## Not used here

`watch_*` tools (no watches); `analytics.*` (no ranking unless the person scores repair options; then `analytics.mcda` or `analytics.rice` with whole-number percent confidence, register N5); market-access status tools (dh-access-and-value); `commercial-dh.audit_claims` (dh-go-to-market).
