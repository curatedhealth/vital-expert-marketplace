# Tools: assess-strategic-readiness

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `maturity_check.py` | `scripts/maturity_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |
| `readiness_check.py` | `scripts/readiness_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## C3 connector boundaries (7 November 2026)

**Offline-first:** `readiness_check.py` and `maturity_check.py` validate team JSON — no inferred ORIC factor schema or AI ordinals.

| Path | Contract | Never |
|---|---|---|
| Worksheets + scripts | Human 1–5 ordinals on declared dimensions (`maturity-instruments.md`) | Maturity %; success probability; MLR waiver |
| `decide_attach_scores` | Named respondent readiness/maturity cells when brief open | Assistant as respondent |
| Live readiness/MCDA connectors | Use only when wired and shape-confirmed | Invented composite GenAI index |

Catalog: `references/lane-a-sources-c3-2026-11-07.md` (LA-C3-004…006, 012–013).
