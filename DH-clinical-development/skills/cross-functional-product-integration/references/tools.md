# Tools: calls this skill uses, as measured on 20 October 2026

Every call below was made live on the VITAL Digital Health Library connector during the build; trimmed outputs are in `examples/live/connector_calls_2026-10-20.json`. Counted calls for the pair (this skill and integration-and-handoff-monitoring share the measurement): 14 (get_authorization 2, search_devices 1, get_pathway_precedents 1, search_safety_events 2, retrieve_guidance 1, qualify_source 2, check_claim 2, find_job 1, agent-pack.list_experts 2); `list_jobs` is free.

This pack has no library suite of its own. The library helps in three places: reading a named product's authorization to anchor an integration map in a real classification (A1), reading public safety events the person asks about (A1, monitoring), and checking a methods passage before the skill relies on it (B1). Most of the work runs on the person's own log and the sourced rows.

## regulatory-dh.get_authorization

- **Call:** `{reference: "DEN160018"}` and `{reference: "DEN200026"}`.
- **Returns:** product, manufacturer, pathway `FDA_DE_NOVO`, class 2, status `DENG`, decision and submission dates, product code (PWE, QFT), regulation number (882.5801, 882.5803), `source_url` to the FDA De Novo database, `retrieved_at` 13 October 2026.
- **Pitfalls:**
  - No intended use, no special controls and no decision summary text (register P5). The special controls that name the work products come from the TM rows (TM120 to TM122 for 882.5801), not from this call.
  - Status is FDA's raw code `DENG` (register C3). Say "De Novo granted".
  - A product name works only where the store spells it the same way; prefer the K or DEN number.

## regulatory-dh.search_devices

- **Call:** `{query: "Pear Therapeutics", jurisdiction: "US", limit: 10}`.
- **Returns:** three rows: reSet (DEN160018, PWE), reSET-O (K173681, PWE, `predicate_source: "summary_pdf_pending"`), Somryst (K191716, QVO, regulation 882.5801, predicate DEN160018 "from record").
- **Use:** find the K or DEN number before `get_authorization`. A manufacturer query returns its products; do not infer anything about the firm beyond the rows.

## regulatory-dh.get_pathway_precedents

- **Call:** `{product_code: "PWE"}`.
- **Returns:** 2 decisions (1 De Novo 2017, 1 510(k) 2018), time from submission to decision between stored dates (median 430 days, n 2).
- **Use:** context only. Pathway questions belong to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

## regulatory-dh.search_safety_events

- **Call:** `{product_code: "PWE", limit: 10}` returned two FDA recall rows dated 7 June 2021 (reSET and reSET-O, Class II) with the summary "Due to a software issue, patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results. Positive UDS results should not have resulted in access to a wheel spin." MAUDE counts for PWE: 2 reports (2022: 1, 2025: 1). `{product_code: "QFT", limit: 10}` returned no recall rows and 2 MAUDE reports (2023).
- **Pitfalls:**
  - The recall `source_url` is the API endpoint, not the recall record (register C1 evidence).
  - The record states "a software issue". It does not state whether a handoff between clinical and software teams was involved. The skill never infers one and does not judge whether the event bears on the person's product; it quotes the library row and says the library row states no cause beyond the quote (FDA's recall page was not read `[GAP]`).
  - MAUDE counts are reports by date received, not confirmed events.

## regulatory-dh.retrieve_guidance

- **Call:** `{query: "design review representatives of functions concerned design transfer cross-functional", limit: 5}`.
- **Returns:** no passage, `[GAP]` (register C6). Design review and transfer rules come from PL1 to PL10.

## verify.qualify_source and verify.check_claim

- **Calls:** `qualify_source {pmcid: "PMC8683254", question}` returned tier gold, DOI 10.1097/sla.0000000000004907, PMID 33856386, year 2021 (the research row PL110 gives the issue, Ann Surg 2022;275(1):73-79; the library gives the online year). `check_claim` with the PL120 passage and the full `qualify_source` object returned "supported" (71 percent overlap) for a faithful claim and "unsupported" (29 percent) for a reversed claim.
- **Pitfalls:**
  - A reversed claim came back "unsupported", not "contradicted" (register N3). Read the passage yourself; accept only a passage that says the same thing in the same direction.
  - The citation inside `check_claim` has identifiers, authors and year empty although `qualify_source` held them (register C18). Take the citation from `qualify_source` or `build_citation`.
  - `qualify_source {url: "https://www.fda.gov/media/112671/download"}` (multiple function guidance) returned "inadmissible", "no provenance" (register C1). Regulator rules rest on the research rows read from raw files, not on Verify.

## verify.build_record

- Not called in the build: it needs a human `cleared_by`. Call it only when the person names who clears the output.

## Catalogue jobs

- `find_job {query: "cross-functional handoff integration design review"}` returned no match; `list_jobs` lists 22 jobs in four suites, none for integration, handoffs, dependencies or joint decisions. Every task's Catalogue job row is "none".

## Not used, and why

- `analytics.mcda` and `analytics.rice` rank only options the person scored. Integration work is ordered by dependency, not by score; the skill does not call them unless the person brings scores and asks for a rank.
- `literature.*`: no methods literature on handoffs was sourced for this pack. Literature reviews belong to `dh-clinical-development` literature-and-real-world-evidence-review.
- No `watch_*` calls.
