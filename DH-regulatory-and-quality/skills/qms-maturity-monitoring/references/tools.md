# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_safety_events`). Counted calls draw on the library key's monthly allowance; free calls do not.

This competency runs mainly on the person's own data (management reviews, audit findings, CAPA). The library adds external signals (safety events), a ranking calculator for repair options the person scored, and the record. The person's QMS data never goes into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Returns, per jurisdiction, authorization and safety-event counts, last load date and sources, plus a list of closed jurisdictions with the reason.
- Observed: US 892 safety events (openFDA recalls and MAUDE counts); UK 10 MHRA alerts; EU 0 safety events; CH not loaded. Japan, Australia, Brazil and Singapore are closed.
- Use it once before A2 Step 5 to know which markets the library can show safety events for.

## regulatory-dh.search_safety_events (counted)

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction` (US, EU, UK, CH, all), `since` (YYYY-MM-DD), `limit` 1 to 25.
- With no manufacturer, product or code it returns nothing and the gap "give manufacturer, product or product_code".
- Returns per event: source type (`fda_recall`, `mhra_alert`), title, event date, severity (recall class or MHRA alert type), manufacturer, summary, source URL, retrieval time. US calls may add `maude_counts` by product code and year, labeled "counts are reports, not confirmed events".
- Pitfalls seen:
  - `product_code` did not filter recalls: `QIH` returned an ultrasound system, a PACS and robotic surgical systems. Treat code-filtered results as unfiltered and read each title.
  - `product_code: "LLZ"` returned no events. Absence is not evidence of no events.
  - A manufacturer query (`Medtronic`) returned MAUDE counts for product codes `QIH` and `QQC` without saying why those codes belong to the query.
  - Recall `source_url` is the openFDA API endpoint, not the recall record; no recall number is returned. Cite the title and event date and say "openFDA enforcement report, record not linked".
  - MHRA alerts: `manufacturer` is often empty while the summary names the manufacturer; one alert named "AI Medical AG" while its summary says "Manufactured by B. Braun Avitum AG". Quote the summary.
  - The `event_date` basis (recall initiation, classification or report date) is not stated `[GAP]`.
- Use it in this competency as an external signal: whether events for the person's own product or manufacturer reached the field, and which process each stated problem touches, per its summary. Describe each event only by what its record states. Never infer a root cause, a QMS failure or a maturity level from a recall or an alert, and never read "no events" as evidence that a process works.

## regulatory-dh.retrieve_guidance (counted)

- Arguments: `query`; optional `namespace` (guidance, ontology-navigation), `limit`.
- Observed: multi-word questions ("QMSR management review internal audit records inspection", "MDR Article 10(9) quality management system person responsible for regulatory compliance") returned no passages. A short term ("ISO 13485") returned five passages, all with `source_url` "[GAP]" and no retrieval date; one restates the QMSR as taking effect in the future ("This final rule will take effect on February 2, 2026"), which is stale.
- Do not cite a passage without a source URL. The sourced references in this skill replace the guidance store for QMS questions.

## analytics.mcda (counted)

- Arguments: `alternatives` (each `id` plus `scores`, a map of criterion to number) and `criteria_weights` (the person's weights; should sum to 1).
- Method returned: "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)". Each `value_estimate` is the weighted sum of score divided by 4, times 100; `contributions` break it down by criterion.
- Pitfalls seen: every criterion is treated as "higher is better" (`negative_criteria` came back empty and the schema offers no way to set it). Name criteria so that a higher score is better ("audit burden avoided", not "audit burden"). No robustness view is returned; the QMS design skill (DH-03.02.3.1) ships a helper, mcda_swap.py, that shows the weights at which options swap.
- In B1 it can rank repair options the person scored (for example by risk addressed and effort avoided). It ranks only what the person scored. Never fill a score for them. Measured during the sibling build (DH-03.02.3.1); the call is saved in `examples/live/mcda_operating_model.json`.

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts` needs `query` or `function`. Query "quality" returned the Quality & Software Lifecycle Director (`quality-systems-director-software`), the worker for this skill, among ten experts. Its bound skills include "QMS maturity check", "QMS score" and "QMS repair", the register tasks this skill replaces.
- `download_agent` returns the expert as files (76,920 characters in the live call). Its stop rules are the source of `references/governance.md`. Offer it only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. Observed: with the name "Claude" it refused ("build_record refuses a record without a human cleared_by.name").
- Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `verify.check_claim` and `verify.verify_text` on regulatory text: the sourced rows already carry the quote and URL. If a literature claim is ever needed, use `verify.qualify_source` then `verify.check_claim` with a passage you have read that states the finding in the same direction (register item N3).
- `watch_*` tools.

## Local helper

- `scripts/qms_indicators.py` (no connector): `capa`, `findings`, `mr` on the person's CSV files; `fda483` on `references/data/fda_483_fy2025_devices.csv` (the FDA FY 2025 spreadsheet, Devices tab, as saved in the research pass). Tested on 19 October 2026: `fda483` reproduces the research totals (185 cite rows, 2,660 citations, QS53); the other subcommands were run on the illustrative files in `examples/sample-data/`.
