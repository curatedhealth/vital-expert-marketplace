# Good example (fictional asset RX-640; not a real product)

Inputs: signed registers upstream (market, timeline, exclusivity); BD buyer; US and DE; reference date 7 November 2026 (evals/fixtures/good-forecast-input.json and good-register.json).

**Answer first**
- US peak-year revenue, gross: low 134.4 million, mid 435.5 million, high 957.6 million USD; net (ASSUMPTION range set by a named deal-team member): low 73.9 million, mid 283.0 million, high 718.2 million USD. Ranges, not a forecast and not a deal value. [scripts/forecast_range.py on the input]
- The probability of success 7%, 11%, 15% is shown beside the ranges and not applied; no risk adjustment and no discounting are done here.
- Germany: erosion parameters are a GAP, so revenue after the exclusivity end year is unadjusted and marked [CHECK]; no total across USD and EUR is computed because no dated rate was supplied.
- Adopted forecast: HUMAN ONLY. Status: UNSIGNED.

US mid check by hand: 43,200 patients x 14% share x 80% adherence x 90,000 USD list = 435,456,000; net 0.65 x = 283,046,400.

## Fact patterns and the passages they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage.

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| revenue shown as low, mid, high with the note that forecasts run high | published forecasts have run high | VP-H-001, VP-H-002 |
| net price is an assumption range with a setter's name | net prices are confidential or differ by payer | VP-R-021, VP-R-023 |
| list price per country from a dated public page | CMS ASP files are dated by effective year | VP-R-030 |
| the funnel patients x share x adherence x price | eligible population by treatment mix | VP-R-050, VP-R-051 |
| sensitivity on every driver | alternative scenarios from the decision maker's view | VP-R-052 |
| no erosion applied without sourced parameters; price erosion context after generic entry | generic prices fall with the number of competitors | VP-R-001, VP-R-002 |
| the probability of success displayed, not applied | owner ruling R4 (no passage) | none |
