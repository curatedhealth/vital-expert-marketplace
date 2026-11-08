# What not to produce (FICTIONAL, for the poor-example screen)

Market register: FICTIONAL FX-801

- Peak sales of $2 billion are likely; this is a blockbuster.   <- a sales forecast the register must not state; no source, no analog, no range.
- Population: unknown. Germany has 100,000 patients, so the EU is about 400,000.   <- "unknown" instead of a GAP; one country's figure used as a proxy for the Union.
- Competitor C1 launches in 2027.   <- no dated source; no timing basis.
- FX-801 has fewer infusion reactions than C1 and best-in-class efficacy.   <- a cross-trial comparison and a sponsor statement, listed as supported.
- The product will be reimbursed at 80% in Germany.   <- a coverage assumption; the Market Access pack owns it and is not Released.

Why it fails: validate_register.py returns E_UNKNOWN, E_FORECAST, E_POP_FIELDS, E_GEO, E_PIPELINE, E_DIFF and E_ACCESS (evals/fixtures/poor-register.json is the machine-readable version).

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| a single prevalence figure from a textbook | a textbook statement is insufficient for a prevalence estimate | VP-G-013 |
| "competitor launches in 2029" from one registry entry | registry status often incorrect | VP-G-050 to VP-G-052 |
| "better than competitor" from two separate trials | trial rates cannot be directly compared | VP-G-040 |
| a peak-sales and price statement | consensus forecasts can be far above actual revenues; price belongs to the Market Access pack | VP-G-060 |
