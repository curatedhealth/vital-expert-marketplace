# Tools: plan-the-delivery

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `delivery_check.py` | `scripts/delivery_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## C4 payload flags (7 November 2026)
`delivery_check.evaluate` refuses (CheckError) when present: `ai_named_owners`, `treat_unknown_capacity_as_feasible`, `dc05_equals_dc09`, `authorize_launch_g_gate` / `lex_pass`, `claim_mitchell_30_percent` / `premortem_success_guarantee`, `ai_failure_modes_as_facts`, `ai_chooses_tier`; step-level `owner_provenance`/`oversight_provenance`=`ai`; `capacity_status=unknown` with `capacity_feasible=true`. Optional `dc09` block requires `human_choice` and in-plugin DC09 codes/labels — no NIST→AEM invention (WR-C4-020). Not an Approach B offline_c_validator adapter.
