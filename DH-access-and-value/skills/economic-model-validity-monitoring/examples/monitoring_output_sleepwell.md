# Sensitivity summary: SleepWell + usual care vs Usual care
Net monetary benefit judged at the person's threshold: 20,000.
Base case: dCost -97.96, dQALY 0.0343, dominant (more QALYs, same or lower cost), net monetary benefit 784.55.

## One-way ranges (sorted by swing)

| Parameter | Base | Low | High | NMB at low | NMB at high | Swing | Sign change | Switching value | Quadrant change |
|---|---|---|---|---|---|---|---|---|---|
| u_gain | 0.02 | 0.0 | 0.03 | 97.96 | 1,127.84 | 1,029.88 | no | outside range | yes: no QALY difference (cost comparison only) to dominant (more QALYs, same or lower cost) |
| offset | 120 | 0 | 180 | 436.59 | 958.53 | 521.94 | no | outside range | yes: north-east (more QALYs, more cost) to dominant (more QALYs, same or lower cost) |
| c_uc | | | | | | | | | no range given |
| c_app | | | | | | | | | no range given |
| q_uc | | | | | | | | | no range given |
| waning | | | | | | | | | no range given |

## Scenarios the person chose

| Scenario | Changes | dCost | dQALY | Quadrant | ICER | NMB |
|---|---|---|---|---|---|---|
| Observed year 1 (illustrative): GP saving 70, utility gain 0.012 | {"set": {"offset": 70, "u_gain": 0.012}} | 47.02 | 0.0206 | north-east (more QALYs, more cost) | 2,283 | 364.93 |
| Observed year 1, GP saving only | {"set": {"offset": 70}} | 47.02 | 0.0343 | north-east (more QALYs, more cost) | 1,370 | 639.57 |
| Observed year 1, utility gain only | {"set": {"u_gain": 0.012}} | -97.96 | 0.0206 | dominant (more QALYs, same or lower cost) | see quadrant | 509.92 |

A switching value is where net monetary benefit is zero at the person's threshold; it is not a verdict. Ranges and scenarios are the person's. Results are hypotheses on the inputs.
