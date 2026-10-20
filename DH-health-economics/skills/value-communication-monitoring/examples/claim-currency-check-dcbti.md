# Worked example: A2 Claim currency check, short mode

Live run on 19 October 2026. The request is a test request; the narrative lines, the product and the owner are illustrative. The study, the passages and every tool result are real (`examples/live/`).

**Request (illustrative):** "Our payer dossier for our digital CBT-I app went out in January 2025. Are its claims still OK? Lines: L1 'In pregnant women with insomnia symptoms, digital CBT-I improved Insomnia Severity Index scores more than standard treatment at 10 weeks (Felder et al. 2020).' L2 'Digital CBT-I improves insomnia severity in adults with insomnia (Felder et al. 2020).' L3 'Sleep duration also improved.' The dossier follows AMCP Format 5.0 and the FDA 2018 payor guidance. Legal owner: Tom Reyes."

---

**Answer.** One of three lines holds. L1 holds: the source is not retracted or corrected (Crossref, checked today) and the Results passage still states it in the same direction. L2 and L3 are held: L2 widens the trial's population from pregnant women to adults, and for L3 the paper says sleep duration was the one secondary outcome that did not improve significantly. The dossier's guidance base has moved twice since January 2025, and two 2026 trials with economic outcomes are candidates to read.

| Line | Source status | Passage re-read | Status |
|---|---|---|---|
| L1 | none (Crossref); current | Same direction; tool "supported", 67% | Holds |
| L2 | as L1 | Tool "supported", 77%, but population widened (register N3) | Held |
| L3 | as L1 | "... with the exception of sleep duration ..."; tool "unsupported", 17%, not "contradicted" | Held |

**Guidance signals**

- FDA payor guidance: the 2018 final is still the final text; a June 2026 revised draft implements the 2023 statute and will replace it when finalized. The dossier names only 2018 (PC-US-47, PC-US-11).
- AMCP Format: 6.0 was released October 2026; only the March 2026 draft was read here, so what changed from 5.0 for this dossier is `[GAP]` (HE-131, AMCP 6.0 draft).

**Candidate new evidence (not read here).** Searched since 1 January 2025: Reesen et al. 2026, an RCT of guided digital CBT-I with a cost-effectiveness question (DOI 10.1037/ccp0001020); Kim et al. 2026, a cost-effectiveness analysis in South Korea (DOI 10.2196/71750; the library labels it a preprint although it is a published journal article, register N8); Hwang et al. 2025, a meta-analysis (DOI 10.1038/s41746-025-01514-4). Whether any changes the dossier is for Tom Reyes or a review update (dh-clinical-validation).

**Gaps.** Certainty for L1 not rated by a person `[GAP]`. AMCP 6.0 final text not read `[GAP]`. Retraction status checked against Crossref only (ES-123).

**Record.** Draft for the owner. AI-assisted. Clears it: Tom Reyes. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Calls made (19 October 2026): `literature.check_retraction {doi: "10.1001/jamapsychiatry.2019.4491"}`; `verify.check_currency {doi}`; `verify.qualify_source {doi, question}`; `verify.check_claim` three times with the Results passages from the Europe PMC abstract (the `get_record` excerpt stopped at the design); `literature.search_literature {query: "digital cognitive behavioral therapy insomnia cost-effectiveness", limit: 5, filters: {date_from: "2025-01-01"}}`. L2 and L3 go to B1 for repair.
