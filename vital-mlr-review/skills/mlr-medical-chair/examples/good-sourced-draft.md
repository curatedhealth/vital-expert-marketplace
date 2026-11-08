# Good sourced draft — mlr-medical-chair

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, CH.
- Claim under review: "Product X is indicated for adults and adolescents ≥12 years with type 2 diabetes."
- Pasted DE Fachinformation indication: adults only. CH excerpt: adults only.
- Adolescent extension not in supplied labels.

## Output cards

### Medical finding card
| Field | Value |
|---|---|
| Finding id | MED-001 |
| Topic | Indication population over-claim |
| Observation | Artefact includes adolescents ≥12; pasted DE/CH authorized-use text is adults only |
| Evidence | Person paste DE FI §4.1; CH Swissmedic excerpt §Indications |
| Gap | Adolescent indication not in supplied label → do not invent PIP/study support |
| Chair | Medical only (Legal/Regulatory not blended) |
| Status | revise |
| Suggested human action | Strike adolescent claim or supply label/variation text that includes ≥12 |

### Second finding (dose)
| Field | Value |
|---|---|
| Finding id | MED-002 |
| Topic | Dose frequency |
| Observation | "Twice daily" in body vs "once daily" in DE posology excerpt |
| Status | revise |
| Evidence | Fachinformation §4.2 line pasted by person |

### Offline checks
- Finding shape: `scripts/check_finding_shape.py`
- Forbidden approval phrases: `scripts/check_forbidden_phrases.py`
- `tools/stamp_ready_line.py --skill mlr-medical-chair --status revise`

### Why this is good
Each finding cites pasted label lines. Population expansion is blocked without label support. No "medically accurate / approved" language.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-medical-chair: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Claims matrix rows C* for locator hygiene; Regulatory if variation procedure is the path; never Legal privacy topics here.

## Finding template (filled)
MED-001 population over-claim — adolescents vs adults-only FI.
MED-002 dose frequency conflict — BID body vs OD FI.
Both cite person pastes; both status revise; neither says the piece is medically cleared.

## Commands
```
$ python scripts/check_finding_shape.py findings.json
$ python scripts/check_forbidden_phrases.py findings.json
$ python tools/stamp_ready_line.py --skill mlr-medical-chair --status revise
```

## Board-facing summary sentence
MED-001 adolescent over-claim and MED-002 BID/OD conflict both cite pasted FI lines — revise language or supply variation text; Medical does not clear the piece.
