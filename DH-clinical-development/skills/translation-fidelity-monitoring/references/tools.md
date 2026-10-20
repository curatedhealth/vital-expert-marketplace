# Tools: calls this skill uses, as measured on 20 October 2026

Every call below was made live on the VITAL Digital Health Library connector during the build of this skill and its sibling (evidence-to-intervention translation); trimmed outputs are in `examples/live/connector_calls_2026-10-20.json`. Counted calls shared across both skills: 18 (get_authorization 2, search_safety_events 2, search_literature 1, find_trial 1, grade_evidence 1, classify_study 1, qualify_source 2, check_claim 4, extract_claims 1, list_experts 1, find_job 2). `list_jobs` is free. No watch calls.

## verify.extract_claims

- **Call:** `{text: "<product copy>"}` (at most 20,000 characters, per the tool description).
- **Returns:** one claim per sentence with `claim_id`, `kind` (factual or numeric), `checkable`. Method `sentence_splitter`.
- **Pitfalls:** every sentence is marked checkable, including a usage instruction ("Play 25 minutes a day, 5 days a week.") and a caveat ("Not a replacement for medication."). Keep instructions and caveats in a fidelity sample: a dropped caveat is a fail type (A1 step 3).

## literature.search_literature

- **Call:** `{query: "video game based digital therapeutic ADHD children randomized controlled trial STARS-ADHD", limit: 6}`.
- **Returns:** 18 merged records, 6 shown, from PubMed, Europe PMC, OpenAlex, Crossref and bioRxiv, each with DOI, PMID, design label, `trial_ids`, `excerpt`.
- **Pitfalls:** `trial_ids` empty on the RCT (register N8); excerpts empty on both primary studies; four of six results were reviews, a news item or off-question. Used here only when a shipped claim has no source on file; the claim map in DH-01.01.4.1 is the usual source.

## literature.find_trial

- **Call:** `{record: {doi: "10.1016/s2589-7500(20)30017-0", pmid: "33334505", title}}`.
- **Returns:** NCT02674633, status COMPLETED, sponsor Akili Interactive Labs, Inc., `match_via` "pubmed_secondary_id", and a warning that two registrations cite the paper as background only. The only route to the registry id.

## literature.grade_evidence and literature.classify_study

- **grade_evidence:** `{records: [...], question_type: "treatment"}` gave the STARS-ADHD RCT CEBM level 2 by the rule "rct for a treatment question -> level 2", and the open-label STARS-Adjunct study `[GAP]` ("design not established"). The level follows the design tag only (N8). It is a library label, not GRADE certainty (the certainty rows sit in the sibling skill, evidence-to-intervention translation).
- **classify_study:** given the STARS-Adjunct abstract, which says "open-label effectiveness study", returned `other` 0.3 with "no decisive metadata or text cue" (N8). Confirm design from the paper.

## verify.qualify_source then verify.check_claim

- **qualify_source:** `{doi: "10.1016/S2589-7500(20)30017-0", question}` returned tier gold, status current, source_score total 39 (authority 15, recency 5, relevance 5, provenance 10). `{url: "https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200026.pdf"}` returned tier "inadmissible", "no provenance" (register C1): FDA decision summaries cannot be checked by Verify. Quote them from the TM rows and say so.
- **check_claim:** pass `claim {text}`, `passage {text, locator}` quoted from the source, and the full object `qualify_source` returned (C18). Results against the STARS-ADHD interpretation sentence:
  - the sentence itself: "supported", 100 percent overlap;
  - a widened claim (hyperactivity, teenagers): "unsupported", 33 percent;
  - the negation ("does not improve"): "supported", 90 percent;
  - the hedge removed ("improves" for "might be used to improve"): "supported", 89 percent.
  Verify decides on word overlap (N3). It catches a widened claim with new words, but not a negation or a stronger verb. In a fidelity sample a "supported" status never passes a claim; set the words side by side with `scripts/fidelity_sample.py claims` and read them.
- **Citation returned:** identifiers null, authors empty, year null (C18). Build the citation from `qualify_source` or the record.

## regulatory-dh.get_authorization

- **Calls:** `{reference: "DEN200026"}` returned EndeavorRx, Akili Interactive Labs, Inc., De Novo, class 2, decision 15 June 2020, received 16 April 2020, product code QFT, regulation 882.5803; `{reference: "DEN160018"}` returned reSet, Pear Therapeutics, Inc., decision 14 September 2017, received 16 May 2016, product code PWE, regulation 882.5801.
- **Pitfalls:** `status` is FDA's raw code "DENG" (register C3). No indication, limitation or special-control text on the record: those come from the decision summary rows (TM132, TM138, TM144).

## regulatory-dh.search_safety_events

- **Calls:** `{product_code: "QFT", jurisdiction: "US"}` returned no recall and 2 MAUDE reports in 2023 (counts only). `{product_code: "PWE", jurisdiction: "US"}` returned two Class II recalls dated 7 June 2021 (reSET and reSET-O mobile apps): "patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results", and MAUDE counts of 1 in 2022 and 1 in 2025.
- **Use:** a recall summary can describe a decision rule behaving differently from its specification (A2 step 4). The reSET summary specified rewards for negative drug screens (TM135).
- **Pitfalls:** `source_url` is the API endpoint, not the recall record (C1). Report counts are reports, not confirmed events (the tool says so). The PWE query also returned reSET-O; describe each event by its own title.

## agent-pack.list_experts

- `{query: "clinical"}` lists the bound worker `clinical-validation-director` and, among others, `clinical-content-product-manager` ("what the product may say, which rules may fire, and which evidence each unit rests on") and `behavior-change-designer`. Descriptions are truncated by the tool.

## Catalogue jobs

`list_jobs` (20 October 2026): no job checks translation fidelity, samples shipped claims against their evidence or computes delivered dose. `find_job {query: "fidelity intervention design"}` returned no match. Nearest: `claim-labels` (available; `commercial-dh.audit_claims` labels up to 20 claims as matches_record, exceeds_record or no_authorization_on_file against the stored intended purpose). It compares claims with the regulatory record, not with the evidence passage, and is preparation for promotional review in `dh-go-to-market` pricing-and-value-message-monitoring. `post-market-watch` exists but this skill makes no watch calls.

## scripts/fidelity_sample.py

- `claims` run on `examples/focusplay-claim-sample.csv` (illustrative product text against real passages from the STARS-ADHD abstract and the EndeavorRx decision summary row TM144): output in `examples/claims-sample-output.txt`.
- `adherence` run on `examples/usage-log-illustrative.csv` (illustrative, 8 users, regimen 5 sessions per week for 4 weeks, 10 enrolled): output in `examples/adherence-output-illustrative.txt`.

## verify.build_record

Not called in this build. It needs a human name in `cleared_by` (tool instructions). Call it only with the name of the person who clears the output.
