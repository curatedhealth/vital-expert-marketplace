# Intake

Ask for every missing item in one message. Do not start on assumptions.

| # | Input | If missing |
|---|---|---|
| 1 | The development risk and timeline register: phase probabilities (low, mid, high) with their rows, phase durations and the approval year range. | route to estimate-development-risk-and-timeline; a stage without a sourced probability is a GAP |
| 2 | The unrisked DCF inputs: net revenue by scenario and year, the cost structure, tax, capital (from build-dcf-model). | route to build-dcf-model |
| 3 | Stage costs (low, mid, high) and the years each stage runs, with owners. | a stage without a cost is a GAP; the rNPV is then an upper bound and says so |
| 4 | The discount-rate range and its documentation; the person who chooses the rate. | no value is shown; no default rate exists |
| 5 | The benchmark stratum for the comparison and its source (the due diligence benchmark), if the buyer wants it. | the comparison is a GAP |
| 6 | The names of the deal lead and the reviewer. | ask in the one message; do not start on an assumption; record a [GAP] with its consequence if it cannot be supplied |

Rules: a figure you were not given is a [GAP] with the consequence stated, never an estimate. No discount rate, cost structure, probability or comparable is supplied from memory: each is the team's input with a source or a label. A single currency; nothing is converted. The adopted valuation is human only.
