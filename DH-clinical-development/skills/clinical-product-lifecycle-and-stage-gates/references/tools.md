# Tools: calls this skill uses, as measured on 20 October 2026

Every call below was made live on the VITAL Digital Health Library connector during the build; trimmed outputs are in `examples/live/regulatory_records_2026-10-20.json`. Counted calls in the pd1 build (shared with lifecycle-quality-monitoring): 14 (get_authorization 2, search_devices 1, find_predicates 1, search_safety_events 2, retrieve_guidance 1, qualify_source 1, check_claim 2, find_job 1, agent-pack.list_experts 3). `list_jobs` is free.

This pack has no library suite of its own. The connector is used for named products (how a comparable product moved through its authorizations), for literature behind a gate, and for Verify. Stage maps, evidence plans and gate records run on the person's material and the references.

## regulatory-dh.get_authorization

- **Call:** `{reference: "DEN200026"}`. Returned EndeavorRx, Akili Interactive Labs, Inc., De Novo, class 2, `status` "DENG", decision 15 June 2020, submission 16 April 2020, product code QFT, regulation 882.5803, source URL and retrieval date (13 October 2026).
- **Call:** `{reference: "DEN160018"}`. Returned reSet, Pear Therapeutics, Inc., De Novo, decision 14 September 2017, submission 16 May 2016, product code PWE, regulation 882.5801.
- **Pitfalls:** `status` is FDA's raw code ("DENG"), not plain words (register C3). The submission date of reSET (16 May 2016) is the De Novo receipt date; TM research "Changes and conflicts" item 5 says the same. The record holds no marketing status, no ownership change and no withdrawal: never infer that a product is still marketed.

## regulatory-dh.search_devices

- **Call:** `{query: "Akili", jurisdiction: "US"}`. Returned three rows: EndeavorRx De Novo (DEN200026, 15 June 2020), EndeavorRx 510(k) K231337 (decision 13 December 2023, predicate DEN200026 "from record"), EndeavorOTC 510(k) K233496 (decision 14 June 2024, predicate DEN200026).
- **Use:** the comparable product's authorization sequence for A1. Save the output and run `scripts/lifecycle_timeline.py` for a dated table with days from submission to decision and days between decisions.
- **Pitfalls:** a record says what was authorized and when; it does not say why a later submission was made. Never state the reason for a 510(k) after a De Novo from the record alone.

## regulatory-dh.find_predicates

- **Call:** `{product_code: "PWE"}`. Returned reSET-O (K173681, 10 December 2018) and reSet (DEN160018) with `predicates` "[GAP]" on both. For QFT, `search_devices` returned predicates "from record"; for PWE this tool did not. A [GAP] predicate is a gap in the store, not a statement that no predicate exists.

## regulatory-dh.search_safety_events

- **Call:** `{product: "EndeavorRx"}`. No recall or alert rows; MAUDE counts for QFT: 2 reports, both 2023, "counts are reports, not confirmed events".
- **Call:** `{product_code: "PWE"}`. Two FDA recall rows dated 7 June 2021, Class II, reSET and reSET-O: "Due to a software issue, patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results." MAUDE: 2 reports (2022: 1, 2025: 1).
- **Use in this skill:** context in A1 for what a marketed comparable met after release. The monitoring skill uses it as a post-market input.

## regulatory-dh.retrieve_guidance

- **Call:** `{query: "design review at major decision points design transfer QMSR ISO 13485 7.3", limit: 3}`. Returned no passage and "[GAP] no passage retrieved in this namespace" (register C6). The QMSR, IMDRF, MDCG, DiGAV and FDA software facts come from this skill's references only.

## verify.qualify_source then verify.check_claim

- **qualify_source:** `{doi: "10.1136/bmj.n2061", question: "..."}` returned tier gold, status current, retraction none, score 39.
- **check_claim:** with the claim, the passage `{text, locator}` quoted from TM3 and the full qualify_source object, returned `status: "unverifiable"`, rationale "scorer unavailable: no claim verdict", for both the claim in the passage's direction and its opposite. On 20 October 2026 Verify gave no verdict at all. The citation again had DOI, PMID, authors and year empty (C18).
- **Rule:** accept a literature claim only when you have read the passage and it says the same thing in the same direction (N3). If Verify is unverifiable, say so and rest the rule on the read passage and its row id.

## literature.search_literature (when a gate needs published evidence)

Not measured in this build for this skill; the clinical validation builds measured it on 19 October 2026 (`trial_ids` empty, design labels from metadata, register N8). For a review of the evidence behind a gate, route to `dh-clinical-development` literature-and-real-world-evidence-review rather than repeating its method.

## agent-pack.list_experts

- `{query: "product manager"}` lists `digital-health-product-manager` (the bound worker: "Turns clinical and market intent into SaMD/DTx product requirements, sequences the roadmap against design-control and risk obligations, and assesses release readiness."), `product-development-lead` ("phase-gated plans, ISO 13485 design-control process ...") and `clinical-content-product-manager`.

## Catalogue jobs

`list_jobs` (20 October 2026): no job covers lifecycle stages, development increments or gate records. `find_job {query: "product lifecycle stage gate"}` returned no match. Every task's Catalogue job row is "none". `pathway-assessment` and `predicate-chain` (Regulatory suite) belong to `dh-regulatory-and-quality` regulatory-pathway-and-classification; this skill names them only when routing.

## verify.build_record

Not called. It needs a human `cleared_by`; call it only with the name of the person who clears the output.
