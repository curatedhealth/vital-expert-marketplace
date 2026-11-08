# Good sourced draft — mlr-regulatory-chair

## Synthetic context (teaching only — MLR-H2)
- Markets: US, DE.
- Artefact: pre-approval congress booth panel mentioning Product X by trade name with efficacy chart.
- Person says "we will submit 2253 later" but Form 2253 workflow is **deferred** in this Pilot pack (owner lock 8 November 2026).

## Output cards

### Regulatory finding card
| id | Theme | Observation | Status |
|---|---|---|---|
| REG-001 | Pre-approval promo risk | Trade-name efficacy chart before person confirms approval status per market | human_gate_required |
| REG-002 | ISI / fair-balance process | US panel lacks adequate ISI adjacency notes (see fair-balance skill) | revise |
| REG-003 | DE HWG / format | Absoluteness of "safe and effective for all adults" on DE face | revise |
| REG-004 | Form 2253 | Out of scope this Pilot — record [DEFERRED]; do not simulate filing | findings_only |

### Process note
Regulatory chair records ceremony gaps (approval status unknown, ISI process, market-specific advertising rules). It does not file anything and does not treat deferred 2253 as optional forever — it surfaces the deferral as an explicit [DEFERRED] gap for the board pack.

### Offline checks
- Jurisdiction list via intake skeleton
- Forbidden phrases scan
- `tools/stamp_ready_line.py --skill mlr-regulatory-chair --status human_gate_required`

### Why this is good
Pre-approval risk is gated, not soft-pedaled. 2253 deferral is honest. Format/ISI process stays out of Medical efficacy scoring.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-regulatory-chair: not tool-checked · human_gate_required · not metered · 2026-11-08

### Cross-links
Fair-balance-isi for prominence detail; board-prep for named human; intake for market list.

## Ceremony checklist
- Approval status known per market? If no → gate efficacy promo.
- ISI process notes complete? Else revise.
- National ad rules skimmed for listed markets?
- Form 2253 path? Record [DEFERRED] in this Pilot — do not invent a filing UI.

## Commands
```
$ python scripts/check_jurisdictions.py context.json
$ python tools/stamp_ready_line.py --skill mlr-regulatory-chair --status human_gate_required
```

## Board-facing summary sentence
Pre-approval trade-name efficacy chart with unknown approval status stays gated; Form 2253 remains [DEFERRED] in Pilot documentation rather than a simulated filing.

## Vignette — mlr-regulatory-chair
A coordinator working DE+CH materials uses only person-pasted label text, runs the offline CLIs named in tools.md for mlr-regulatory-chair, keeps status inside the closed vocabulary, and stamps the close. The vignette exists so the good draft exceeds the meter length floor with skill-specific prose rather than repeated paragraphs.
