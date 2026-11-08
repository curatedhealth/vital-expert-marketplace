Input:    population, share and denominator sources with year and geography (intake items 3 and 4)
Atom:     extract-requirements-from-source
Tool:     python3 scripts/market_check.py input.json --pretty (fixture: evals/fixtures/good-market-input.json)
Template: none
Output:   per market: population figure, shares, addressable patients (low, central, high), orphan-threshold arithmetic, figure ages, gaps; for the revenue countries (US, DE, FR, IT, ES, UK) a country_patients block, each with source, year and geography, or a GAP
Check:    each figure states its measure (complete or partial prevalence), source, year and geography; extrapolation is justified; a textbook statement is not enough (VP-G-010, VP-G-011, VP-G-013); exit 0; every factor carries source, year and the market's own geography; the case definition is stated; the arithmetic is shown. Rule: a figure from another geography is a GAP, not a proxy; no figure from memory
Human:    the named reviewer with market and clinical knowledge reviews the output
