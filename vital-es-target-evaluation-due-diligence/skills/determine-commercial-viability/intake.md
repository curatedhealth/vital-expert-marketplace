# Intake

Ask for every missing item in one message. Do not start on assumptions.

| # | Input | If missing |
|---|---|---|
| 1 | Buyer mode (bd or investor), unit (asset, or company with the list of pipeline assets; one run per asset, then a roll-up), markets in scope (US, EU or both; another market is a [GAP]), and the reference date. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 2 | The signed market register (skill G), the clinical evidence register (A), the mechanism register (F), the development risk and timeline ranges (B), the exclusivity register (C) with the all-patents and composition-only effective dates, and the pathway map (D). Which of them exist and are signed. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 3 | The buyer's thresholds, each in the buyer's own words: the peak-sales hurdle (amount, currency, nominal), the years of exclusivity wanted after the expected launch date, the expected launch date (from B and D, or the buyer's), and the minimum number of supported differentiation claims. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 4 | Analog launches: each with name, indication class, modality, route, line of therapy, peak annual sales and the year it was reached, currency, geography (US, EU or worldwide), the eligible population if known, why it is comparable, and the source with its date. Say which analogs the person supplies and which were sourced. Analogs to exclude, with reasons. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 5 | The asset's addressable population (central) from skill G, if the buyer wants the scaled comparison view. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 6 | The state of the Market Access pack (draft or Released) and the records it holds for this asset: assumed listing date, restrictions, share of eligible patients with access, price corridor, access barriers. If none, say so. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 7 | The limit on the spread of peak years among analogs, if the buyer has one. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 8 | The name of the decision owner and of the reviewer who will sign the register. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied || 9 | The signed revenue and price register of skill forecast-revenue-and-price-ranges (owner ruling R7): per country ranges, state, and whether it is signed. If none, say so. | the condition C-RV is not evaluated when no block is supplied; supply the block as `revenue_inputs` (signed, countries) so that a missing or unsigned register shows as a GAP |

Rules: if 1 to 3 are missing, ask. A threshold you were not given is a [GAP] and the condition stays "gap". An analog you cannot source with a date is not used. Never estimate a peak-sales figure from memory.
