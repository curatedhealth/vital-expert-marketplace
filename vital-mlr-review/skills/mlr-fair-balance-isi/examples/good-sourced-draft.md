# Good sourced draft — mlr-fair-balance-isi

Teaching material only (MLR-H2).

## Synthetic context (teaching only — MLR-H2)
- Markets: US, DE (person listed both).
- Artefact: 2-page HCP leave-behind. Page 1 efficacy bullets; page 2 dense ISI block in 7pt.
- Person asks: "Is fair balance OK?"

## Output cards

### Fair-balance / ISI card
| Check | Observation | Status |
|---|---|---|
| ISI present | Yes — page 2 block titled Important Safety Information | findings_only |
| Prominence vs claims | Efficacy on p1 in 12pt bold; ISI 7pt on p2 only | revise — prominence imbalance flagged for human Regulatory |
| Contraindications reflected | US boxed-warning theme mentioned; DE contraindications not mirrored in DE-facing panel | [GAP] DE fair-balance panel |
| Fair-balance standards ref | See `references/standards-by-market.md` (US 21 CFR 202.1 themes; DE HWG / Fachinfo balance) | findings_only |
| New ISI drafted by model | None — pack refuses to author approved ISI | N/A |

### Narrative
Presence ≠ balance. The skill records placement and type-size contrast; a named Regulatory reviewer decides whether revision is enough or the piece stays gated. No "fair-balanced / cleared" stamp.

### Offline checks
- Manual score against standards-by-market rows for US and DE.
- `tools/stamp_ready_line.py --skill mlr-fair-balance-isi --status revise`

### Why this is good
Separates presence from prominence. Keeps DE and US distinct. Does not generate substitute ISI copy presented as final.

### Liability
This prepares material for human MLR review. It is not medical, legal, or regulatory approval.

### Stamp
READY-local / mlr-fair-balance-isi: not tool-checked · revise · not metered · 2026-11-08

### Cross-links
Regulatory chair for process/format; Medical for safety statement accuracy vs label; Legal if omission could mislead.

## Prominence rubric (teaching)
| Factor | Weak | Stronger balance |
|---|---|---|
| Proximity | ISI only on last page | Risk cue near each major benefit |
| Type size | Benefit 12pt / ISI 7pt | Comparable visual weight |
| Market panel | US ISI pasted onto DE face | DE-specific safety from FI |
| Absolute language | "safe for all adults" | Qualified per label |

## Commands
```
$ python scripts/check_forbidden_phrases.py examples/good-sourced-draft.md
$ python tools/stamp_ready_line.py --skill mlr-fair-balance-isi --status revise
```

## Board-facing summary sentence
ISI present on page 2 but visually subordinate to page-1 benefits; DE panel incomplete versus FI — revise for human Regulatory, not a balance clearance.
