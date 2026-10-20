# Tools: calls this skill uses, as measured on 20 October 2026

Every call below was made live on the VITAL Digital Health Library connector during the build of this skill and its sibling (mechanism validation monitoring); trimmed outputs are in `examples/live/connector_calls_2026-10-20.json`. Counted calls for the pair: 18 (get_authorization 2, find_job 1, search_safety_events 2, find_predicates 1, list_experts 2, search_literature 1, find_trial 2, classify_study 1, grade_evidence 1, qualify_source 2, check_claim 2, search_devices 1); `list_jobs` is free. This skill has no library suite of its own. Load tools with ToolSearch "+Vital_Digital_Health <keyword>". Stay under about 40 counted calls per run. Never call `watch_*`.

## Catalogue

- `list_jobs` (free) and `find_job {query: "therapeutic mechanism intervention design"}`: no job covers mechanism design, component specification or assumptions (`matches: []`). Every task's Catalogue job row says "none". `evidence-table` (available) grades studies for a product's claims and can serve A1 step 3 if the person wants the therapy model's studies graded; the steps below remain the method.

## regulatory-dh.get_authorization (precedents)

- **Call:** `{reference: "DEN160018"}` and `{reference: "DEN200026"}`.
- **Returns:** product, manufacturer, pathway `FDA_DE_NOVO`, risk class "2", status "DENG", decision and submission dates, product code, regulation number, `source_url`, `retrieved_at`, coverage line ("US: 1226 authorizations loaded ... last load 2026-10-19").
- **Pitfalls:** no intended use, indication, therapy model or trial facts (register P5). Those come from the decision summary rows TM131 to TM144. Exact identifiers only (P2). Use it to confirm identity and dates, then quote the TM rows.

## regulatory-dh.find_predicates and search_devices (precedents in a code)

- `find_predicates {product_code: "PWE"}` listed reSET (DEN160018) and reSET-O (K173681, 10 December 2018), both with predicates `[GAP]`.
- `search_devices {query: "fibromyalgia", jurisdiction: "US"}` returned no device, although 21 CFR 882.5804 was codified 26 June 2026 (TM126). Search by product or manufacturer name; a condition word may return nothing. Absence is a store gap.

## regulatory-dh.search_safety_events (what went wrong in a precedent's delivery)

- `{product_code: "PWE"}`: two Class II recalls of 7 June 2021 describing a software issue in the contingency management reward (summary quoted in `precedents.md`), plus MAUDE counts (2 reports). `{product_code: "QFT"}`: no recalls, MAUDE 2 reports.
- **Use in A2:** a recall that names a component (here, the reward logic) shows that a component's software implementation is itself a link that can fail. Quote the summary; never infer cause or harm beyond it.
- **Pitfalls:** recall `source_url` is the API endpoint, not the recall record (C1, P1); the same text can appear twice for sister products; MAUDE counts are reports, not confirmed events.

## literature.search_literature and literature.get_record (evidence for the therapy model)

- **Call:** `{query: "internet-delivered community reinforcement approach contingency management substance use disorder randomized trial Therapeutic Education System", limit: 6, filters: {designs: ["rct"]}}`: 18 merged, 5 shown; three on topic (Campbell 2014, Murphy 2016, Levesque 2017), two off topic (not digital or a different behavior).
- **Pitfalls:** `trial_ids` empty and `excerpt` empty on every record (N8). A passage must come from the abstract or full text (Europe PMC) or the person. Screen by the person's question; never count hits as support.

## literature.find_trial

- With the main paper record: "no linked registration found" and "4 registrations cite this paper as background only". With `{nct_id: "NCT01104805"}`: the CTN-0044 registration and five papers, missing the main results paper and the mediation paper (N8). Registry content (outcomes, arms, dates) was read from the ClinicalTrials.gov API directly.

## literature.classify_study and literature.grade_evidence

- The mediation paper (a secondary analysis) came back `rct` 0.95, decided by `publication_type_raw` only, and CEBM level 2 ("rct for a treatment question"). A mediation analysis is not graded as a trial result here; check the design against the paper (N8).

## verify.qualify_source then verify.check_claim

- `qualify_source {doi: "10.1016/j.addbeh.2016.09.012", question}`: gold, score 67 (authority 15, recency 5, relevance 30, provenance 10).
- `qualify_source {url: DEN160018 decision summary PDF}`: "inadmissible", "no provenance", title and date null (C1). FDA decision summaries cannot be checked through Verify; quote the TM row and its read date instead.
- `check_claim` with the full qualify_source object and the abstract passage: the correct claim ("partial mediator") and its opposite ("did not mediate ... proven to be the active ingredient") both returned "partial", rationale "the passage does not state the figure", although neither claim has a figure (N3). Citation fields came back empty (C18). Accept a claim only when you have read the passage and it says the same thing.

## analytics.mcda and analytics.rice (only to rank what the person scored)

- Not called in this build. Measured in earlier builds: `mcda` has no robustness view and treats every criterion as higher-is-better (C17); `rice` reads confidence as a percent (N5). Use them only on scores and weights the person supplied, and show the inputs.

## agent-pack.list_experts

- `{query: "clinical validation"}` returned `clinical-validation-director` (the bound worker; remit truncated by the tool at "and the clinical"). `{query: "behavio"}` returned `behavioral-science-lead` ("COM-B diagnosis, a cited BCT map, and a measurement plan") and `behavior-change-designer`, whose remits match this competency more closely (BUILD_NOTES; binding not changed).

## verify.build_record

- Not called in the build: it needs a human name in `cleared_by`. Call it only after the named person clears the output.

## A3 and A4 (added in the DH-01.06 fold, 20 October 2026)

- **Connector not available for the fold.** The VITAL connector was not available in the session that added A3 and A4, so no new call was made. The A3 and A4 worked example (`examples/safety-by-design-reset-precedent.md`) reuses the live outputs saved earlier on 20 October 2026: `regulatory-dh.get_authorization {reference: "DEN160018"}` and `{reference: "DEN200026"}`, `regulatory-dh.search_safety_events {product_code: "PWE"}` and `{product_code: "QFT"}`. Before relying on them, recheck those four calls live and note any difference (BUILD_NOTES).
- **Calls A3 and A4 use.** `regulatory-dh.get_authorization` to confirm a precedent's identity, date and regulation; `regulatory-dh.search_safety_events {product_code}` for recalls that name a component or mechanic (PWE: the reward wheel, 7 June 2021). Behavior and pitfalls are as described above (no intended use, P5; recall `source_url` is the API endpoint, C1 and P1; MAUDE counts are reports, not confirmed events).
- **Catalogue job.** No saved `list_jobs` output shows a job for engagement mechanics or safety design; the Catalogue job row says "none". Recheck `find_job {query: "engagement mechanics"}` and `{query: "safety by design hazard"}` when the connector returns.
- **Not tool-checked.** The FTC rows (SE109 to SE113, SE117, SE118) are [WF]; regulator PDFs are not checkable through Verify (C1). Quote the SE row and its read date instead.
