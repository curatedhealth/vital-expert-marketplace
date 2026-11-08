# Intake

Ask for every missing item in one message. Do not start on assumptions.

| # | Input | If missing |
|---|---|---|
| 1 | Buyer mode (bd or investor), unit (asset, or company with the list of pipeline assets; one run per asset, then a roll-up), the valuation date and the one currency. | ask in the one message; do not start on an assumption; record a [GAP] with its consequence if it cannot be supplied |
| 2 | The signed revenue register (forecast-revenue-and-price-ranges): net revenue by scenario and year, country by country, with the row each comes from. | route to the revenue skill; a scenario without a series is a GAP |
| 3 | The exclusivity register (assess-ip-portfolio-and-freedom-to-operate): the effective exclusivity end per market. | erosion timing is a GAP; the DCF states that revenue after the end may be overstated |
| 4 | Cost structure per scenario: cost of goods %, operating expense %, fixed costs by year, tax rate, capital expenditure %, working-capital % of the revenue change; each with a source or a named owner. | costs taken as zero and the value labelled a revenue-only upper bound |
| 5 | The discount-rate range with the method and the evidence the team documents, and the name of the person who chooses the rate. | no valuation is shown; the rate is a human choice and has no default |
| 6 | The terminal assumption (annual change, source) or the statement that there is none. | no terminal value; the value after the last explicit year is zero and the output says so |
| 7 | The name of the deal lead and of the reviewer who will sign the register. | ask in the one message; do not start on an assumption; record a [GAP] with its consequence if it cannot be supplied |

Rules: a figure you were not given is a [GAP] with the consequence stated, never an estimate. No discount rate, cost structure, probability or comparable is supplied from memory: each is the team's input with a source or a label. A single currency; nothing is converted. The adopted valuation is human only.
