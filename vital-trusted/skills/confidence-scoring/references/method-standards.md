# Method standards (Q1)

| Id | Standard | Source and version | Scope | Status | Verification note | URL |
|---|---|---|---|---|---|---|
| C1 | The summary gives counts by result and nothing else. No percentage, ratio, score, grade, threshold, color or "high, medium, low" label. | Owner decision of 9 November 2026 (Option 2, no live tools); TRUSTED hard rules TR-H1, TR-H4 |  | VERIFIED | In force |  |
| C2 | The six results come from `claim-assessment/references/statuses.md` and are used by pointer. | `claim-assessment/references/statuses.md` |  | VERIFIED | In force |  |
| C3 | Open items are: your passage says something different, not found in your passage, no passage to compare with, partly found. Opinions, recommendations and definitions are not open items. | `claim-assessment/references/statuses.md` |  | VERIFIED | In force |  |
| C4 | A count is not a verdict on truth, source quality, balance or readiness. | TRUSTED hard rule TR-H3 |  | VERIFIED | In force |  |
| C5 | Source notes stay separate from the counts. | Owner decision of 9 November 2026 |  | VERIFIED | In force |  |
| C6 | Order: counts, open items in order of risk, one recommendation, the fixed line. | Owner decision of 9 November 2026 |  | VERIFIED | In force |  |
| C8 | RAGAS splits an answer into atomic claims and tests each against context. TRUSTED uses the splitting idea only, by hand, and computes no ratio. | RAGAS Faithfulness docs |  | PARTIAL | Accessed 8 November 2026. Primary document not read in this build. Reference only, not applied. | https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/ |
| C9 | Relative risk without absolute risk can mislead on clinical impact. | ABPI Code 2024 Cl. 6.1 guidance |  | PARTIAL | Clause 6.1 text re-read 9 November 2026 in the PMCPA interactive 2024 Code. The relative-risk wording is supplementary information to clause 6.1 and was not re-read `[CHECK]`. | https://www.pmcpa.org.uk/the-code/2024-interactive-abpi-code-of-practice/clause-6-information-claims-comparisons-and-disparagement/ |
| WC-FActScore | Atomic claims, scored against a knowledge source (reference only; TRUSTED gives no score). | Min et al. EMNLP 2023 |  | PARTIAL | Read through a secondary digest on 8 November 2026; the primary document has not been read. Reference only, not applied. | https://aclanthology.org/2023.emnlp-main.741/ |

Rows marked PARTIAL are not yet checked against the primary document; check before relying on them.
