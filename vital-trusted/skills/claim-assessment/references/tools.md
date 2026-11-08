# Tools — claim-assessment

## Offline (always available in this pack)

| Tool | Path | Purpose |
|---|---|---|
| split_claims | `tools/split_claims.py` | Split text into checkable claims |
| claim_structure | `tools/claim_structure.py` | Structural claim shape |
| passage_support | `tools/passage_support.py` | Local support status vs a passage (not world-truth) |
| faithfulness | `tools/faithfulness.py` | Aggregate support counts / card inputs |
| stamp_check_line | `tools/stamp_check_line.py` | Emit consistent check-lines |

Invoke via skill script: `scripts/split_claims.py` (wrapper) or:

```bash
python3 tools/split_claims.py --text "..." --json
python3 tools/passage_support.py --claim "..." --passage "..." --json
python3 tools/stamp_check_line.py --mode offline --skill claim-assessment
```

## Live (optional VERIFY MCP)

| Tool | Use when |
|---|---|
| extract_claims | Prefer when connected; same job as offline split_claims |
| check_claim | Prefer when connected with an admitted source object |
| verify_text | Batch path when connected |

Without VERIFY, never emit VERIFY status vocabulary as if a tool ran. Use **not tool-checked**.
