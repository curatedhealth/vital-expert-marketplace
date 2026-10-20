| Rank | Option | Value (recomputed) |
|---|---|---|
| 1 | DE statutory insured, insomnia (DiGA prescription) | 76.25 |
| 2 | US Medicare behavioral health practices (DMHT codes) | 60.00 |
| 3 | US self-insured employers | 41.25 |

Check against analytics.mcda: all values match.

Where adjacent options would swap (one weight moved, the others kept in proportion):

| Pair | Criterion | Current weight | Swap at weight | Direction |
|---|---|---|---|---|
| DE statutory insured, insomnia (DiGA prescription) over US Medicare behavioral health practices (DMHT codes) | payer_route | 0.35 | 0.04 | if lowered below |
| DE statutory insured, insomnia (DiGA prescription) over US Medicare behavioral health practices (DMHT codes) | competition | 0.15 | 0.36 | if raised above |

Criteria not listed for a pair cannot swap that pair at any weight strictly between 0 and 1 (at most a tie at an end point).
