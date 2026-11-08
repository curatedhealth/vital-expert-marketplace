# Failure modes for the estimate

This skill screens against the same library as skill A (../../review-clinical-data-quality/references/failure-modes.md, FM-01 to FM-08). The ones that change a number are restated here with their sources and statuses (as in skill A; each finding is registered in skill A's `verbatim-passages.json`; the passage ids are skill A's). The detection questions are written for this skill and are labeled ENGINEERING RULE in grounding-register.md.

| Id | How it enters the estimate | Detection question for this skill | Documented for | Source (skill A row) | Passage ids (skill A register) | Status |
|---|---|---|---|---|---|---|
| FM-01 | The estimate or the seller's plan sits above the benchmark | Is the adjusted mid above the benchmark? If yes, is the reason stated and tied to a register finding? | benchmarks of drug development (US) | BIO/Informa/QLS 2021 and Wong 2019 (A FM-01) | VP-A-072 to VP-A-074 | VERIFIED (re-opened) |
| FM-02 | Phase 2 result not repeated in phase 3 | Is the phase 2 to 3 adjustment sized to the register's replication status? | FDA review experience, 22 cases | FDA 22 case studies (A FM-02) | VP-A-080, VP-A-081 | VERIFIED (re-opened) |
| FM-03 | Subgroup claim carried into the plan | Does any upward adjustment rest on a subgroup that is unreplicated or not prespecified? | randomized trials with subgroup claims | Wallach 2017 (A FM-03) | VP-A-088, VP-A-089 | VERIFIED (re-opened) |
| FM-04 | Surrogate or accelerated route not confirmed | Does the timeline assume an expedited route the register does not support? | FDA accelerated approvals (US) | HHS OIG snapshot (A FM-04): incomplete confirmatory trials and overdue applications — passages registered on skill A as VP-A-160 to VP-A-163 (NLM dual-read). This skill cites those A passages; no new PoS invented | VP-A-160 to VP-A-163 | VERIFIED (via skill A register) |
| FM-06 | Safety signal | Is there a signal with an adjustment, or a reason there is none? | products withdrawn for adverse reactions | Onakpoya 2016 (A FM-06; fit caveat there) | VP-A-086, VP-A-087 | VERIFIED (re-opened) |
| FM-08 | Manufacturing | Is the regulatory-stage adjustment linked to CMC evidence or its absence? | FDA complete response letters, as reported by trade press | trade-press statement only (A FM-08) | none | PARTIAL (summary only) |

No estimate-specific mode is added without a published analysis behind it.
