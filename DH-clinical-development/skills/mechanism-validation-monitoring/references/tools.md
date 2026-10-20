# Tools: calls this skill uses, as measured on 20 October 2026

Every call below was made live on the VITAL Digital Health Library connector during the build of this skill and its sibling (therapeutic mechanism and intervention design); trimmed outputs are in `examples/live/connector_calls_2026-10-20.json`. Counted calls for the pair: 18 (get_authorization 2, find_job 1, search_safety_events 2, find_predicates 1, list_experts 2, search_literature 1, find_trial 2, classify_study 1, grade_evidence 1, qualify_source 2, check_claim 2, search_devices 1); `list_jobs` is free. This skill has no library suite of its own. Load tools with ToolSearch "+Vital_Digital_Health <keyword>". Stay under about 40 counted calls per run. Never call `watch_*`.

## Catalogue

- `list_jobs` (free) and `find_job {query: "therapeutic mechanism intervention design"}`: no job covers mechanism checks, fidelity or process evaluation (`matches: []` for mechanism design; nothing in the 21 listed jobs fits). Every task's Catalogue job row says "none". `evidence-table` (available) grades studies for a product's claims; it does not check links. `post-market-watch` would call `watch_register`, which this skill never calls.

## regulatory-dh.get_authorization (precedents)

- **Call:** `{reference: "DEN160018"}` and `{reference: "DEN200026"}`.
- **Returns:** product, manufacturer, pathway `FDA_DE_NOVO`, risk class "2", status "DENG", decision and submission dates, product code, regulation number, `source_url`, `retrieved_at`, coverage line ("US: 1226 authorizations loaded ... last load 2026-10-19").
- **Pitfalls:** no intended use, indication, therapy model or trial facts (register P5). Those come from the decision summary rows TM131 to TM144. Exact identifiers only (P2). Use it to confirm identity and dates, then quote the TM rows.

## regulatory-dh.find_predicates and search_devices (precedents in a code)

- `find_predicates {product_code: "PWE"}` listed reSET (DEN160018) and reSET-O (K173681, 10 December 2018), both with predicates `[GAP]`.
- `search_devices {query: "fibromyalgia", jurisdiction: "US"}` returned no device, although 21 CFR 882.5804 was codified 26 June 2026 (TM126). Search by product or manufacturer name; a condition word may return nothing. Absence is a store gap.

## regulatory-dh.search_safety_events (delivery failures and harms in a named product)

- `{product_code: "PWE"}`: two Class II recalls of 7 June 2021 describing a software issue in the contingency management reward (summary quoted in `precedents.md`), plus MAUDE counts (2 reports). `{product_code: "QFT"}`: no recalls, MAUDE 2 reports.
- **Use in A2 and B1:** for a named product's live cohort, check for recalls or reports that touch a component (here, the reward logic granted regardless of the screen result). A recall naming a component is a delivery-link fact for that period. Quote the summary; never infer cause or harm beyond it.
- **Pitfalls:** recall `source_url` is the API endpoint, not the recall record (C1, P1); the same text can appear twice for sister products; MAUDE counts are reports, not confirmed events.

## literature.search_literature and literature.get_record (a published study to check)

- **Call:** `{query: "internet-delivered community reinforcement approach contingency management substance use disorder randomized trial Therapeutic Education System", limit: 6, filters: {designs: ["rct"]}}`: 18 merged, 5 shown; three on topic (Campbell 2014, Murphy 2016, Levesque 2017), two off topic (not digital or a different behavior).
- **Pitfalls:** `trial_ids` empty and `excerpt` empty on every record (N8). A passage must come from the abstract or full text (Europe PMC) or the person. Screen by the person's question; never count hits as support.

## literature.find_trial

- With the main paper record: "no linked registration found" and "4 registrations cite this paper as background only". With `{nct_id: "NCT01104805"}`: the CTN-0044 registration and five papers, missing the main results paper and the mediation paper (N8). Registry content (outcomes, arms, dates) was read from the ClinicalTrials.gov API directly.

## literature.classify_study and literature.grade_evidence

- The mediation paper (a secondary analysis) came back `rct` 0.95, decided by `publication_type_raw` only, and CEBM level 2 ("rct for a treatment question"). A mediation analysis is not graded as a trial result here; check the design against the paper (N8). A2 does not need a grade; a graded review is `dh-clinical-development` literature-and-real-world-evidence-review.

## verify.qualify_source then verify.check_claim

- `qualify_source {doi: "10.1016/j.addbeh.2016.09.012", question}`: gold, score 67 (authority 15, recency 5, relevance 30, provenance 10).
- `qualify_source {url: DEN160018 decision summary PDF}`: "inadmissible", "no provenance", title and date null (C1). FDA decision summaries cannot be checked through Verify; quote the TM row and its read date instead.
- `check_claim` with the full qualify_source object and the abstract passage: the correct claim ("partial mediator") and its opposite ("did not mediate ... proven to be the active ingredient") both returned "partial", rationale "the passage does not state the figure", although neither claim has a figure (N3). Citation fields came back empty (C18). Accept a claim only when you have read the passage and it says the same thing.

## analytics.rice and analytics.mcda (only to order responses the person scored)

- Not called in this build. Measured in earlier builds: `rice` reads confidence as a percent (N5); `mcda` has no robustness view (C17). In B1, use them only to order responding work the person scored, and show the inputs.

## scripts/link_check.py (the person's cohort)

- Runs on the person's cohort file and check plan, outside the connector. Tested on `evals/files/cohort_illustrative.csv` with `evals/files/check_plan_illustrative.json` (output in `examples/link_check_illustrative_output.md`).

## agent-pack.list_experts

- `{query: "clinical validation"}` returned `clinical-validation-director` (the bound worker; remit truncated by the tool at "and the clinical"). `{query: "behavio"}` returned `behavioral-science-lead` ("COM-B diagnosis, a cited BCT map, and a measurement plan") and `behavior-change-designer`, whose remits match this competency more closely (BUILD_NOTES; binding not changed).

## verify.build_record

- Not called in the build: it needs a human name in `cleared_by`. Call it only after the named person clears the output.

## DH-01.06 fold (A3 and A4), 20 October 2026

The VITAL connector was not available in the session that added A3 and A4, so no new call was made. The tasks reuse the saved live records above: `get_authorization` for DEN160018 and DEN200026, `search_safety_events` for PWE (two Class II recalls of 7 June 2021, MAUDE 2 reports) and QFT (no recalls, MAUDE 2 reports), and the CTN-0044 reads. The calls A3 and A4 name (`regulatory-dh.search_safety_events`, `regulatory-dh.get_authorization`) behave as measured above; they need a live recheck when the connector returns (BUILD_NOTES, pd2).

- **A3** needs no library call. `scripts/engagement_read.py` runs on the person's usage export, outside the connector. Tested on `evals/files/usage_illustrative.csv` with `evals/files/engagement_definitions_illustrative.json` (output in `examples/engagement_read_illustrative_output.md`).
- **A4** uses `search_safety_events` only for a named product's public records. `scripts/signal_read.py` runs on the person's event and exposure files. Tested on `evals/files/signal_events_illustrative.csv`, `evals/files/signal_exposure_illustrative.csv` and `evals/files/signal_thresholds_illustrative.json` (worked example in `examples/signal-read-rewardpath-pwe.md`).
- **Catalogue:** no saved `list_jobs` output shows a job for engagement reads or safety signal reads; both Catalogue job rows say "none". `post-market-watch` would call `watch_register`, which this skill never calls.
