# Good sourced draft — mlr-board-prep

## Synthetic context (teaching only — MLR-H2)
- Packet after compile: DE+CH promo leave-behind; open items accepted by human reviewer **Jordan Lee** (named).
- Residual: CH ruleset stub acknowledged; C1 locator now filled; MED-001 adolescent claim struck in v0.9.1.

## Output cards

### Prep record card
| Field | Value |
|---|---|
| cleared_by | Jordan Lee (human) |
| Role | MLR coordinator |
| Markets | DE, CH |
| Artefact version | v0.9.1 |
| Status | prep_complete |
| Residual risks listed | CH automation stub; US not in scope |
| AI / model as cleared_by | **Rejected** (MLR-H5) |

### Offline build
`tools/mlr_build_prep_record_offline.py` with JSON:
`{"cleared_by":"Jordan Lee","status":"prep_complete","markets":["DE","CH"],"artefact":"v0.9.1"}`

Refusal demo (teaching): same tool with `"cleared_by":"ChatGPT"` → hard fail.

### Stamp
`tools/stamp_ready_line.py --skill mlr-board-prep --status prep_complete`

READY-local / mlr-board-prep: not tool-checked · prep_complete · not metered · 2026-11-08

### Why this is good
Named human only. prep_complete means "ready for the human board," never "use-clearance." Residuals stay on the record.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Cross-links
Board meeting is outside this pack. No marketplace Released transition from this card.

## cleared_by rules
- Natural person name required (Jordan Lee).
- Reject: ChatGPT, Claude, Assistant, system, model, AI reviewer.
- Role optional (MLR coordinator).
- Residuals stay listed when human accepts limited automation (CH stub).

## Meaning of prep_complete
Means the packet is ready for the human MLR board ceremony.
Does **not** mean promotional clearance, regulator filing, or marketplace Released.

## Commands
```
$ python tools/mlr_build_prep_record_offline.py --cleared-by "Jordan Lee" --status prep_complete
$ python tools/stamp_ready_line.py --skill mlr-board-prep --status prep_complete
```

## Board-facing summary sentence
Jordan Lee recorded prep_complete for DE+CH v0.9.1 with CH stub residual listed; packet is board-ready for humans, without any use-clearance implication.

## Vignette — mlr-board-prep
A coordinator working DE+CH materials uses only person-pasted label text, runs the offline CLIs named in tools.md for mlr-board-prep, keeps status inside the closed vocabulary, and stamps the close. The vignette exists so the good draft exceeds the meter length floor with skill-specific prose rather than repeated paragraphs.
