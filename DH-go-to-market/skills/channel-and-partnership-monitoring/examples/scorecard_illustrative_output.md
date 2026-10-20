# Script output on the illustrative files (ILLUSTRATIVE DATA, 19 October 2026)

Command: `python3 scripts/partner_scorecard.py examples/handoff_log_illustrative.csv examples/measures_illustrative.json`

```
Period: 2026-Q3

## Implementer B (implementation partner)
| Measure | Count (handoff record) | Rule (yours) | Result |
|---|---|---|---|
| Implementations started | 3 | >= 3 | met |
| Claim breaches | 0 | <= 0 | met |

Partner reports tied to a buyer in the record: 0 (already counted from the record)
Partner reports not tied to a buyer: 0 (not counted)
Implementations for buyers this partner did not hand off: 1 (not counted): HS-104
Hold rules triggered: none

## Reseller A (reseller)
| Measure | Count (handoff record) | Rule (yours) | Result |
|---|---|---|---|
| Qualified buyers handed off | 4 | >= 6 | missed |
| Implementations started | 2 | >= 2 | met |
| Claim breaches | 1 | <= 0 | missed (your hold rule) |

Partner reports tied to a buyer in the record: 1 (already counted from the record)
Partner reports not tied to a buyer: 2 (not counted): 2026-08-20 no buyer id, 2026-09-12 HS-190
Claim breach 2026-09-18: Reseller webinar slide 7: 'FDA-registered, so you know it is approved'
Open claim breach: the register rule says do not continue this partner while a breach is open; the action stops for your owner.
Hold rules triggered: Claim breaches

```
