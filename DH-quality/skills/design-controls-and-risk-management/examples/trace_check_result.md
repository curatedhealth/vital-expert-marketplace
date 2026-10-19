Items read: 26 (design_input 6, design_output 1, hazard 4, risk_control 4, user_need 3, validation 2, verification 6)
Findings: 17 (G2 1, G3 3, G4 1, G5 1, G6 1, G7 5, O1 1, O2 1, R1 1, R2 2)
Findings, not a score. Whether any finding blocks a release is the owner's decision.

| Item | Code | Detail | Check |
|---|---|---|---|
| UN-03 | G2 | no validation traces to this need | user need with no validation tracing to it |
| DI-04 | G3 | no verification traces to this input or its outputs | design input with no verification (directly or through a design output) |
| DI-05 | G3 | no verification traces to this input or its outputs | design input with no verification (directly or through a design output) |
| DI-06 | G3 | no verification traces to this input or its outputs | design input with no verification (directly or through a design output) |
| HZ-04 | G4 | no risk control traces to this hazard | hazard with no risk control |
| RC-04 | G5 | no verification traces to this control | risk control with no verification |
| RC-04 | G6 | no design input carries this control | risk control not carried into any design input (check; may sit in labeling) |
| DI-01 | G7 | no design output traces to this input (working convention) | design input with no design output (working convention; QS24) |
| DI-03 | G7 | no design output traces to this input (working convention) | design input with no design output (working convention; QS24) |
| DI-04 | G7 | no design output traces to this input (working convention) | design input with no design output (working convention; QS24) |
| DI-05 | G7 | no design output traces to this input (working convention) | design input with no design output (working convention; QS24) |
| DI-06 | G7 | no design output traces to this input (working convention) | design input with no design output (working convention; QS24) |
| DI-06 | O1 | design_input traces to nothing | item with no upward link (orphan) |
| VER-06 | O2 | links to DI-09, which is not in the file | link to an id not in the file |
| VER-03 | R1 | result recorded as fail | verification or validation recorded as fail |
| VAL-02 | R2 | no result recorded | verification or validation with no result recorded |
| VER-04 | R2 | no result recorded | verification or validation with no result recorded |
