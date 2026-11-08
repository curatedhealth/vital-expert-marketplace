# Tools: run-weight-sensitivity

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `sensitivity_exhibit.py` | `scripts/sensitivity_exhibit.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## C3 connector boundaries (7 November 2026)

| Tool | Use | Never |
|---|---|---|
| `sensitivity_exhibit.py` | One-way / declared weight sweeps on **frozen** human score matrix (1–10 offline path) | Proceed/close; invented bounds |
| `methods_mcda_rank` | Base rank input only when team already used live 0–4 path — **no silent rescale** to offline exhibit | Sensitivity-as-choice; substitute for `sensitivity_exhibit` without same matrix |
| `methods_risk_tornado` | Risk/driver tornado on a **different** declared model | MCDA criterion weight sweep (conflation refused — SEN-05) |

Catalog: `references/lane-a-sources-c3-2026-11-07.md`.
