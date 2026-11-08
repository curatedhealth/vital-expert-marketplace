# Intake

Ask for every missing item in one message. Do not start on assumptions.

| # | Input | If missing |
|---|---|---|
| 1 | The DCF register and the rNPV register (inputs and results). | route to build-dcf-model and calculate-risk-adjusted-npv |
| 2 | The benchmark stratum and the cumulative probability it implies, with source (from the due diligence plugin). | check C4 is a gap |
| 3 | The analog peak-sales range (from determine-commercial-viability) with unit and source. | check C5 is a gap |
| 4 | The exclusivity end year (assess-ip-portfolio-and-freedom-to-operate) and the last explicit cash-flow year; whether erosion is modeled. | check C8 is a gap |
| 5 | The discount-rate method and evidence; whether risk is argued to be in the rate; whether the probability is applied to the cash flows. | checks C6 and C7 are flags or gaps |
| 6 | The names of the deal lead and the reviewer. | ask in the one message; do not start on an assumption; record a [GAP] with its consequence if it cannot be supplied |

Rules: a figure you were not given is a [GAP] with the consequence stated, never an estimate. No discount rate, cost structure, probability or comparable is supplied from memory: each is the team's input with a source or a label. A single currency; nothing is converted. The adopted valuation is human only.
