# Good example (fictional asset FX-201; not a real product, company or license)

Inputs: evals/fixtures/good-exclusivity-input.json and evals/fixtures/good-register.json; BD buyer; asset unit; US and EU.

**Answer first**
- Effective exclusivity date, US: composition patent only 2029-06-29; all patents 2031-02-01. EU: both views 2031-06-30. The 5-year new-chemical-entity period ended 2022-03-01 and no longer protects the asset. [dates: scripts/exclusivity_dates.py; rules US-NCE-5Y, US-PTE-*, EU-SPC-DURATION, EU-DP-8Y, EU-MP-10Y]
- US patent term extension on P1 adds 1,095 days (1,461-day testing phase halved to 730, plus the 365-day approval phase), taking the expiry from 2026-06-30 to 2029-06-29; neither cap binds. Diligence reductions were given as 0 by the seller; counsel confirms. [rule ids US-PTE-TESTING-HALF, US-PTE-PHASES, US-PTE-APPROVAL-PHASE-FULL]
- EU SPC on E1 is capped at the five-year maximum (E1 expiry 2026-06-30 to 2031-06-30). [EU-SPC-DURATION, Art 13(2)]
- Biggest open questions for counsel: (1) written description support for the F1 composition claims (IP-01, cannot tell: file wrapper missing); (2) whether the change-of-control clause in the Alpha University license (s.12.1) needs consent for this deal (IP-02, triggered); (3) the freedom-to-operate opinion, including the paragraph IV notice letter D1. HUMAN ONLY.
- Status UNSIGNED. EU reform not yet law: current rules used.

**BD view (options only).** Tie a milestone to counsel confirming the written-description position on F1; make licensor consent a closing condition; ask for the file wrapper before signing.

**Why this is good:** every date names its rule and source; both effective dates are shown; the question that only counsel can answer is a question, not a conclusion; gaps say what they block.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| the 5-year new-chemical-entity period ended and no longer protects the asset | FDA exclusivity periods | VP-C-001 |
| patent term extension: testing phase halved, approval phase in full, caps checked, one patent | 35 U.S.C. 156(c), (g) | VP-C-010 to VP-C-017 |
| the EU SPC is capped at the five-year maximum | Regulation 469/2009 Art 13(2) | VP-C-061, VP-C-062 |
| EU reform not yet law, current rules used | the Commission SPC page: the 2023 reform proposal is not law | VP-C-091 |
| written description support for the composition claims (IP-01) | written description requirement separate from enablement | VP-C-110, VP-C-111, VP-C-112 |
| the change-of-control clause in the university license needs licensor consent; the chain from inventor to owner is mapped | chain of title: an IP map from inventor to owner; a present assignment beats a promise to assign | VP-C-130, VP-C-120 to VP-C-122 |
| counsel, not the agent, gives the opinion; a landscape is not an FTO opinion | WIPO guidelines on landscape and FTO reports | VP-C-100, VP-C-101 |
