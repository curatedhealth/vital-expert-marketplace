# Intake

Ask for every missing item in one message. Do not start on assumptions.

| # | Input | If missing |
|---|---|---|
| 1 | The rNPV input of calculate-risk-adjusted-npv (stages, scenarios, rates). | route to calculate-risk-adjusted-npv |
| 2 | The scales for revenue, probability and cost (low and high), supplied by the team. | no default is used; the run stops with E_SCALE |
| 3 | The launch delay in years and the discount rate to hold (one of the supplied rates). | launch delay and rate rows are omitted |
| 4 | The threshold for the switching value (zero or the price under discussion). | zero is used and said so |
| 5 | The names of the deal lead and the reviewer. | ask in the one message; do not start on an assumption; record a [GAP] with its consequence if it cannot be supplied |

Rules: a figure you were not given is a [GAP] with the consequence stated, never an estimate. No discount rate, cost structure, probability or comparable is supplied from memory: each is the team's input with a source or a label. A single currency; nothing is converted. The adopted valuation is human only.
