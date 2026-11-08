# Tools: capability map

| Tool | Path | Use for | Never for |
|---|---|---|---|
| Integrated report assembler | `tools/assemble_report.py` | Merge signed skill outputs into UNSIGNED report | Inventing findings; recommending a deal |
| Assemble report tests | `tools/test_assemble_report.py` | Offline regression | Live network |
| KA suite runner | `evals/known-answer/run_ka_suite.py` | Inventory + unit smoke | Claiming independent grade Pass |
| Refuse content smoke | `evals/known-answer/refuse_content_smoke.py` | Anti-pattern probes | Marketplace Done |

Live connectors: plugin `connectors.md`.
