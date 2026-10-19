# Trace matrix structure

No regulator in the research publishes a trace matrix template. `[GAP]`: a regulator-specified trace format. What the sources do require is that the design and development file contains or references every record needed to show compliance (QS24), that software is verified and validated (EU19), that IEC 62304 does not cover validation of the finished device (ST6), and that risk controls are implemented and their effectiveness monitored (ST4, EU14, EU16). The structure below is this skill's working convention to meet those requirements. Say so when you use it.

## Item types and the links between them

Each item has an id and traces **up** to the item(s) it comes from.

| Type | Traces up to | Why the link matters | Source of the need for it |
|---|---|---|---|
| User need | nothing (root) | Intended use, user, environment | Validation must answer it (EU19) |
| Hazard | nothing (root) | Known and foreseeable hazards, including misuse | EU14 |
| Risk control | hazard | A control exists for each hazard that needs one | EU16, ST4 |
| Design input | user need and/or risk control (and, in a column, the regulation or standard it implements) | Inputs come from needs, from controls, and from requirements such as Annex I 17 | EU20, EU21, QS13 |
| Design output | design input | Specification, code module, label | QS24 |
| Verification | design input, design output, or risk control | Output meets input; control is implemented | EU19, ST4 |
| Validation | user need | Device meets the need in use; 62304 does not cover it | EU19, ST6 |

## Checks (run by `scripts/trace_check.py`)

| Code | Finding | Plain meaning |
|---|---|---|
| G1 | User need with no design input | The need is not designed for |
| G2 | User need with no validation | Nobody has shown the need is met in use |
| G3 | Design input with no verification | The requirement is not shown to be met |
| G4 | Hazard with no risk control | An identified hazard is open |
| G5 | Risk control with no verification | The control is not shown to be in place |
| G6 | Risk control not carried into any design input | A control may live only in the risk file; if it is information for safety it may sit in labeling (person decides) |
| G7 | Design input with no design output | No specification, code module or label is recorded as implementing the requirement (working convention; QS24 requires the file to contain or reference the records) |
| O1 | Orphan | An item that traces to nothing: a requirement with no stated origin |
| O2 | Dangling link | A link to an id that does not exist in the export |
| O3 | Wrong link type | For example a validation tracing to a design input |
| R1 | Failed result | A verification or validation recorded as fail |
| R2 | No result | A verification or validation with no result recorded |

G4 and G5 restate the two fail conditions of the earlier task wording ("a hazard with no control, or a control with no verification").

These are findings. They are not a score, and none of them decides whether a release can go. That decision belongs to the person's named owner (task B1).

## Minimum CSV the script reads

`id, type, links` are required; `text, result, note` are optional. Types: `user_need, design_input, design_output, verification, validation, hazard, risk_control`. Links are ids separated by `;`. Most requirements tools export something close to this; map columns once and keep the mapping with the output.
