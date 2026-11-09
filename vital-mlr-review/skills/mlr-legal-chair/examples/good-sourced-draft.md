# Good sourced draft — mlr-legal-chair

Teaching material only (MLR-H2).

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, US.
- Artefact line: "The #1 prescribed T2D therapy among endocrinologists — better tolerated than Product Y."
- No IMS/IQVIA citation supplied. No head-to-head CSR. Footer collects email "for updates" without privacy notice link on DE panel.

## Output cards

### Legal finding card
| id | Theme | Observation | Status |
|---|---|---|---|
| LEG-001 | Comparative superiority | "Better tolerated than Product Y" without supplied H2H evidence | human_gate_required |
| LEG-002 | Ranking / #1 claim | "#1 prescribed" with no auditable data source on packet | revise — [GAP] source |
| LEG-003 | Privacy / notice | DE email capture without visible privacy notice / lawful-basis cue | revise |
| LEG-004 | Misleading omission risk | Efficacy bullets without adjacent risk cue on same panel (cross-ref fair-balance) | findings_only → hand Regulatory |

### Chair isolation
Medical owns whether tolerability language matches label; Legal owns comparative and ranking substantiation + privacy presentation. This card does not score HbA1c numerics.

### Offline checks
- `scripts/check_finding_shape.py` on findings JSON
- `scripts/check_forbidden_phrases.py`
- `tools/stamp_ready_line.py --skill mlr-legal-chair --status human_gate_required`

### Why this is good
Comparative and ranking claims stay gated without invented market-share data. Privacy gap named for DE. No "legally cleared" wording.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-legal-chair: not tool-checked · human_gate_required · not metered · 2026-11-08

### Cross-links
Medical for clinical truth of tolerability; Regulatory for ISI placement; claims-matrix for locator rows.

## Theme map
| Theme | Example trigger | Typical status |
|---|---|---|
| Comparative | better than Y | human_gate_required without H2H |
| Ranking | #1 prescribed | revise / [GAP] source |
| Privacy | email field no notice | revise |
| Misleading omission | benefits without risk cue | findings_only + hand Regulatory |

## Commands
```
$ python scripts/check_finding_shape.py legal_findings.json
$ python tools/stamp_ready_line.py --skill mlr-legal-chair --status human_gate_required
```

## Board-facing summary sentence
Comparative tolerability and #1 ranking lack packet sources; DE email capture misses privacy notice — human_gate_required on superiority until substantiation lands.
