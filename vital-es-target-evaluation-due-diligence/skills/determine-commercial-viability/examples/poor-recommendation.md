# What not to produce (FICTIONAL, for the poor-example screen)

Commercial viability register: FICTIONAL FX-801

- We recommend GO. Peak sales of $2 billion are expected and the asset is commercially viable.   <- a recommendation, a single point and a verdict, none of which the skill may state.
- Analogs: two launches, both from memory.   <- fewer than three, no dated source, no stated basis: no range may be shown.
- Price will be $120,000 and the product will be reimbursed at 80%.   <- the Market Access pack owns price and coverage and it is not Released.
- Class risk: none.   <- two class flags exist and no sourced differentiation addresses them.
- Options: GO and NO-GO.   <- the conditional option is missing; all three are required, none ranked.
- Exclusivity: fine.   <- no required end date, no effective dates, no comparison.

Why it fails: validate_register.py returns E_DECISION_FIELD, E_RECOMMEND, E_POINT, E_RANGE, E_OPTIONS, E_ACCESS and E_FM_UNRESOLVED (evals/fixtures/poor-register.json is the machine-readable version).

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| a single peak-sales figure and "we recommend GO" | forecasts were on average too optimistic; analog selection needs review | VP-H-002, VP-H-030 |
| price and coverage assumed | access failure evidence; Market Access pack owns them | VP-H-020, VP-H-021, VP-H-022 |
| two analogs only | no source sets a number of analogs: ENGINEERING RULE | none |
