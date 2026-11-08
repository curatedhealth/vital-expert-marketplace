# Good sourced draft — mlr-channel-intent

## Synthetic context (teaching only — MLR-H2)
- Markets: DE, US (person listed both; US not defaulted).
- Draft claim: "Product X reduces HbA1c in adults with type 2 diabetes."
- Person initially said "scientific exchange" but supplied no unsolicited-request record and the piece is a branded leave-behind with ISI footer.

## Output cards

### Channel intent card
| Gate | Result |
|---|---|
| Declared channel | scientific exchange (person) |
| Artefact signals | branded leave-behind + ISI footer + efficacy claim |
| Unsolicited request on file | No → [GAP] |
| Recommended posture | Treat as **promotional** until person supplies exchange record OR revises channel |
| Status | human_gate_required |

### Decision narrative (findings, not approval)
Scientific-exchange framing cannot ride on a branded efficacy leave-behind without an unsolicited medical-information request trail. The gate does not rewrite the piece; it forces a human choice: (a) reclassify as promo and continue chairs, or (b) supply the MI request record and strip branding/claims that break exchange rules.

### Offline checks
- Channel enum from intake skeleton (`promo` | `scientific_exchange` | `mixed` | `unknown`).
- `tools/stamp_ready_line.py --skill mlr-channel-intent --status human_gate_required`

### Why this is good
Surfaces channel conflict instead of silently accepting the person's label. Does not invent FDA/EMA channel law text. Hands Medical/Legal/Regulatory their own cards.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-channel-intent: not tool-checked · human_gate_required · not metered · 2026-11-08

### Cross-links
After human resolves channel → mlr-claims-matrix + chairs. If still unknown → stay gated.

## Signal checklist
| Signal | Suggests promo | Suggests exchange |
|---|---|---|
| Trade name + efficacy chart | Yes | Rarely |
| ISI footer | Yes | Sometimes (if MI letter) |
| Unsolicited MI request ID | Weak | Strong when present |
| Branded leave-behind PDF | Yes | No |

## Worked conflict
Person: scientific exchange. Artefact: branded HbA1c chart + ISI. Record: none.
→ status human_gate_required. Do not silently flip to promo in the artefact; flip only after human chooses.

## Offline stamp example
```
$ python tools/stamp_ready_line.py --skill mlr-channel-intent --status human_gate_required
```

## Board-facing summary sentence
Declared scientific exchange conflicts with branded efficacy leave-behind lacking MI request record — human must reclassify or supply the record before chairs proceed.
