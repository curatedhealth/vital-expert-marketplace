# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `regulatory-dh_search_devices`). Counted calls draw on the library key's monthly allowance; free calls do not.

**How this file was written.** The connector was disconnected when this skill was built on 20 October 2026. Behavior below comes from live outputs saved on 19 October 2026 by earlier builds (copied unchanged into `examples/live/`, read on 20 October 2026; each origin is in `examples/live/README.md`) and from those builds' tools.md files. Where no saved output exists, the call is described from the earlier builds' notes only and marked **needs a live check**. Earlier builds twice saw "could not answer this call (503). Nothing was counted"; a retry a minute later worked.

## regulatory-dh.list_jurisdictions (free)

- No arguments. Saved run (`examples/live/list_jurisdictions_2026-10-19.json`): US 1,226 authorizations and 892 safety events, loaded 19 October 2026; EU 3,142 authorizations, decision date empty on all 3,142; UK 0 authorizations (MHRA device registration not loaded) and 10 safety alerts; CH nothing loaded; TW 32; CA 227 with `is_software` null on all, so a software-only search excludes them.
- Use it first in A1 and A2. It is the coverage note: what the scan cannot see.

## regulatory-dh.search_devices (counted)

- Required `query` (product or maker name, 3+ characters); optional `jurisdiction` (US, EU, UK, CH, all), `limit` 1 to 25, `software_only` ("true" default).
- Saved run: `{query: "Aidoc", jurisdiction: "all", limit: 10}` returned ten US 510(k) rows (product codes QAS, QFM, QIH), newest decision 14 May 2026 (K261317, BriefCase-Triage), each with FDA URL and `retrieved_at` 13 October 2026 (`examples/live/search_devices_aidoc_2026-10-19.json`). EU: "Briefcase" returned Aidoc's "Briefcase-Triage" and "Briefcase-Quantification", class IIa, "On the EU market", no decision date; "Viz" returned "no stored device matches 'Viz' in EU" (`examples/live/search_devices_eu_2026-10-19.json`).
- Pitfalls: it is a name search ("stroke" matched product names, not intended uses); no field says whether a device uses AI or carries a PCCP; EU rows have no decision date and point to the EUDAMED search screen (quote the Basic UDI-DI); the same product is spelled differently across registers ("BriefCase-Triage", "Aidoc Medical , Ltd." in the US; "Briefcase-Triage", "Aidoc Medical Ltd." in the EU), so match on identifiers.
- Use in A1 for authorization signals and in A2 for a named technology's record. `scripts/horizon_helpers.py signals` turns the output into signal rows.
- Saved run: `{query: "Brainomix", software_only: "false", limit: 25}` returned 19 rows, four of them US 510(k) clearances under QAS: K251983 (26 August 2025), K232496 (21 November 2023), K231837 (28 September 2023), K231195 (27 July 2023), retrieved 13 October 2026 (`examples/live/search_devices_brainomix_2026-10-19.json`).
- **Makers under a product code.** Because this is a name search, the library names only the makers searched by name. When a product code is in scope, run `python3 scripts/horizon_helpers.py makers --code QAS FILES` on every saved or live output: it lists every maker the records show under the code (search results, the De Novo grant in `get_pathway_precedents`, and the predicate chain from `find_predicates`), with decisions in and before the window, and how many decisions in each year are not yet tied to a maker. Saved records for QAS on 19 October 2026 show three makers: Aidoc Medical , Ltd. (eight QAS clearances in a search capped at 10 rows, five of them from 6 November 2025 to 14 May 2026), Brainomix Limited (four clearances, latest K251983, 26 August 2025) and Viz.Al, Inc. as stored (De Novo DEN170073, ContaCT, 13 February 2018). Of the 10 QAS decisions in 2026, 4 are Aidoc's; the other 6 are not tied to a maker in the saved records. Name all three, say how many decisions are untied, and name the public record that lists all of them: FDA's 510(k) database, which "can be searched by 510(k) number, applicant, device name or FDA product code" (FDA medical device databases page, read 20 October 2026; DL-131). Ask for maker names to search; never guess them.

## regulatory-dh.find_predicates (counted)

- Saved run: `{reference: "K261317"}` returned the predicate chain K261317 to K220709 to K203508 to K180647 to DEN170073 (ContaCT, Viz.Al, Inc., 13 February 2018), with the basis "named in the FDA 510(k) summary" (`examples/live/find_predicates_K261317_2026-10-19.json`).
- Pitfalls: predicates are read from 510(k) summary PDFs (openFDA has no predicate field); a predicate is a comparison device, not a competitor list.

## regulatory-dh.get_pathway_precedents (counted)

- Arguments: `product_code` or `emdn_code`; optional `jurisdiction`.
- Saved run: `{product_code: "QAS", jurisdiction: "US"}` returned 88 decisions (87 510(k), 1 De Novo), by year 2018: 3, 2019: 5, 2020: 12, 2021: 5, 2022: 15, 2023: 11, 2024: 12, 2025: 15, 2026: 10; first decision 13 February 2018 (DEN170073, ContaCT, Viz.Al, Inc.), last 16 September 2026; median 104 calendar days from submission to decision (n 88) (`examples/live/pathway_precedents_QAS_2026-10-19.json`).
- Pitfalls: a product code is a device type, so the count is not an AI count; days are between stored dates, not MDUFA "FDA days"; the current year is partial. `scripts/horizon_helpers.py byyear` prints the counts with the year-on-year change and these caveats.

## regulatory-dh.get_deltas and get_register_deltas (counted)

- Arguments: `product_code`, `emdn_code` or `manufacturer`; `since`; `jurisdiction`.
- Saved runs: QAS since 1 September 2026, Brainomix since 1 January 2026, EMDN Z11030592 since 1 September 2026: every call returned no rows and "no watch is registered for this scope; the change log has not started" (`examples/live/get_deltas_QAS_2026-10-19.json`, `examples/live/register_deltas_2026-10-19.json`). The same day, `search_devices` showed a QAS decision dated 14 May 2026 (K261317) inside the store.
- Rule: an empty result here is a log that has not started, never "no change". Read dated records with `search_devices` or `get_pathway_precedents` instead, filtered by date with `scripts/horizon_helpers.py signals --since`. Never call `watch_register` or any `watch_*` tool: watches are not separated by customer key in another suite (register N2), and the person's confidential technology names must not go into a watch.

## regulatory-dh.search_safety_events (counted)

- Saved run: `{product_code: "QAS", jurisdiction: "all", limit: 10}` returned ten recalls, all Siemens, none naming a QAS device; the product code filter applied to MAUDE counts (0 reports for QAS), not to recalls (`examples/live/safety_events_QAS_2026-10-19.json`).
- Use only when a scan asks for safety signals on a named product; describe each record by what it states, never judge its relevance to the person's product.

## literature.list_sources (free) and literature.search_literature (counted)

- `list_sources` on 19 October 2026: PubMed, Europe PMC, OpenAlex, Crossref, bioRxiv and medRxiv, ClinicalTrials.gov, Semantic Scholar and Unpaywall loaded; Cochrane, Embase, Scopus, Web of Science, PROSPERO and Consensus not queried.
- `search_literature` takes `query`, `limit` 1 to 50 and `filters` (`date_from`, `date_to`, `designs[]`). Saved run: "digital cognitive behavioral therapy for insomnia app randomized controlled trial", limit 8: 29 records after merge; off-topic records ranked in; excerpts empty on 7 of 8; `trial_ids` empty on every RCT (register N8); a conference abstract labeled `meta_analysis` (`examples/live/literature_search_2026-10-19.json`).
- Use in A1 for publication signals and in A2 for the evidence on record. A record is a signal that something was published, never a finding. Review method routes to `dh-clinical-development` literature-and-real-world-evidence-review.

## literature.find_trial (counted; needs a live check)

- Earlier build: `{record}` or `{nct_id}` linked an RCT to NCT04069247 via PubMed's secondary id. No saved output in this skill. **Needs a live check.**

## diligence-dh.get_deltas (counted)

- Required `companies` (1 to 12 legal names) and `since` (YYYY-MM-DD). Saved run: Big Health, Inc. and Akili Interactive Labs, Inc. since 1 January 2025: "no change recorded" for both; log first entry 12 October 2026, last sweep 19 October 2026, with three limits lines (`examples/live/diligence_get_deltas_BigHealth_Akili.json`).
- Rule: quote the log start and limits beside every "no change recorded"; for a window before 12 October 2026, read dated records instead. Company status is never read from this tool (`company-status.md`).

## analytics.mcda (counted)

- Arguments: `alternatives` [{`id`, `scores` {criterion: 0 to 4}}], `criteria_weights` {criterion: weight}. Returns "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)" with `value_estimate` (0 to 100) and contributions per criterion (`examples/live/mcda_partner_options.json`, illustrative scores: 77.5, 63.75, 62.5).
- Pitfalls: no robustness view (register C17); every criterion is treated as higher-is-better. Run `scripts/horizon_helpers.py swap` on the saved output for the recomputation check and swap points. A criterion where lower is better must be rescored by the person.

## analytics.rice (counted)

- `initiatives` [{`id`, `reach`, `impact`, `confidence`, `effort`}]. `confidence` is read as a percent: pass 80, not 0.8 (`examples/live/rice_percent_confidence.json`). Check scores with `scripts/horizon_helpers.py rice-check`. The method citation is a vendor article (Intercom 2016): a calculator the person chooses, not a sourced rule.

## analytics.scenario-modeler (counted)

- Arguments: `parameters` (name to number, or a list with one value per period), `formula` (arithmetic over the names and `t`), `periods`, `aggregate` (`sum`, `cumulative`, `none`). `t` starts at 0. `^` is rejected with HTTP 400: use `**`. Saved run: `population * uptake * (device_cost - offset)` returned 65,000, 130,000 and 195,000 over three periods on illustrative inputs (`examples/live/analytics_calls_2026-10-19.json`).
- Use in B1 only on the person's parameters. Output is "computed on your inputs".

## analytics.risk-tornado (counted)

- Same arguments plus `variation_pct` (default 0.2) and `parameter_ranges`. Saved runs: list parameters are skipped (`skipped_parameters: ["uptake"]`); parameters without a range get plus or minus 20 percent; a ratio formula produced a negative output that the tool ranked as the smallest swing with no flag (`examples/live/analytics_calls_2026-10-19.json`). Run `scripts/horizon_helpers.py tornado-check` on the output.

## verify.build_record (counted)

- Needs a human `cleared_by.name`; `{name: "Claude"}` returned "build_record refuses a record without a human cleared_by.name" (`examples/live/verify_build_record_refusal.json`). Call only when an output leaves the conversation and the person names who clears it.
- `verify.qualify_source` rated an FDA guidance URL "inadmissible, no provenance" in an earlier build (register C1): do not spend calls checking regulator rows; the rows in `references/` carry their own URL, quote and read date.

## Catalogue job

- `list_jobs` on 19 October 2026 (`examples/live/list_jobs_2026-10-19.json`) listed jobs in the Commercial, Diligence and Evidence and Reimbursement suites; none covers horizon scanning, technology evaluation or scenarios. Every task's formula table says "Catalogue job: none"; the direct calls are the method. `partner-prioritization` (mcda and rice) is scoped to partners and indications; call the calculators directly.

## Steps that need a live check

1. `literature.find_trial` in A1 (no saved output in this skill).
2. `regulatory-dh.search_devices` for a technology class not yet searched (only Aidoc, Brainomix, Briefcase, stroke and Viz are saved).
3. `regulatory-dh.get_pathway_precedents` for product codes other than QAS.
4. `diligence-dh.get_deltas` with a non-empty change row (no saved run contains a change).
5. `analytics.mcda` and `analytics.scenario-modeler` with the person's real numbers (saved runs use illustrative inputs).
6. Whether `get_deltas` starts returning rows once a watch exists elsewhere (never set one here).

## Not used here

Every `watch_*` tool; `market-access-dh.*` (coverage routes to `dh-access-and-value` coverage-pathway-and-access-strategy); `diligence-dh.screen_market`, `build_company_profile`, `compare_portfolio` (investment questions route to `market-and-target-screening`, `company-and-evidence-assessment`, `funding-and-portfolio-comparison`, this pack); `commercial-dh.*` (partner design routes to `dh-go-to-market` channel-and-partner-design).
