# Maturity instruments — data readiness, change capacity, risk appetite

Capability: CF-01.06.01. Skill home: `assess-strategic-readiness`.
Trigger: client asks for maturity depth beyond readiness narrative. Until scored by named people, leave `[GAP]`.

**No universal pharma investment or GenAI maturity instrument is established here** (WR-C3-017; WR-C3-022). Default path: qualitative checklist in `method.md` §Lane A absorb — C3. Optional scored instruments below require **exact construct, version, population, unit, respondents, anchors, aggregation, adaptation and validation scope** before any "validated" label (LA-C3-012; LA-C3-013). **No validated GenAI composite.** ORIC (LA-C3-004) does not cover every readiness dimension; adapted questions do not inherit validation.

### Miake-Lye et al. 2020 — limits (LA-C3-012)

Systematic review of organizational readiness assessments (27 publications, 29 uses; search through June 2017): context tailoring, **no gold-standard** instrument, item bank includes repeated items — not 1,370 unique constructs. Transfer: explicit construct and context selection. Does not establish a pharma investment or GenAI instrument; does not validate each instrument's psychometric quality.

### Caci et al. 2025 — limits (LA-C3-013)

Healthcare systematic review (47 studies; literature through August 2022; **industry settings excluded**): heterogeneous definitions and measurements; ambiguous evidence on when readiness influences implementation. Transfer: refuse success-probability translation from readiness scores. Does not directly validate pharma enterprise readiness instruments.

## Design rules
1. Instruments are **worksheets**, not AI scores. People enter 1–5 ordinals; assistant attaches the sheet.
2. Never convert maturity into an investment recommendation without `compare-options` / owner choice.
3. Offline validator: `scripts/maturity_check.py` (schema only).

## Instrument A — Data readiness
| Dimension | 1 | 3 | 5 | Evidence class required |
|---|---|---|---|---|
| Source of truth | Tribal | Partial systems | Named SoT with owner | M or V for 4–5 |
| Freshness | Unknown | Quarterly | Measured SLA | M for 4–5 |
| Access | Ad hoc extract | Ticketed | Self-serve governed | O/V |
| Quality | Untested | Spot checks | Defined quality tier | M/V |

## Instrument B — Change capacity
| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Sponsor time | None named | Named part-time | Named with calendar hold |
| Team load | Already overcommitted | Contested | Protected capacity |
| Prior change debt | Untracked failures | Some learning | Pattern library in use |

## Instrument C — Risk appetite (investment)
| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Irreversibility comfort | Avoids all irreversible | Case-by-case | Explicit band with board |
| Evidence bar before Proceed | Always Investigate first | Mixed | Proceed allowed under named bar |
| Reopen triggers | None | Informal | Written thresholds |

## Output
Maturity sheet JSON validated by `maturity_check.py`. Blocking gaps listed. Feeds readiness narrative; does **not** auto-place portfolio.
