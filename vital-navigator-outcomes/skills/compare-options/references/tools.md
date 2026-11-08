# Tools: compare-options

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `options_check.py` | `scripts/options_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## Lane A absorb (7 November 2026)
`options_check.py` — MCDA compute + decoy refuse (LA-SDG-ALT). Catalog: plugin `references/lane-a-sources-c1-c2-2026-11-07.md`.

## C3 connector boundaries (7 November 2026)

| Tool | Scale / contract | Never |
|---|---|---|
| `methods_nav_compute` (`nav.options`) | Offline-first; human **1–10** criterion cells per I7 | AI scoring; silent 0–4 conversion |
| `methods_mcda_rank` | Human **0–4** criterion scores; human `criteria_weights` — **VITAL/API adaptation**, not claimed faithful 2008 EVIDEM (LA-C3-010) | Invented alternatives shape; EVIDEM compliance fiction; 0–4 ↔ 1–10 without declared adapter |
| `decide_attach_scores` / release | Named-person cells only | Assistant as rater |

Catalog C3: `references/lane-a-sources-c3-2026-11-07.md`. `methods_risk_tornado` is **not** this skill's weight sweep — see `run-weight-sensitivity`.
