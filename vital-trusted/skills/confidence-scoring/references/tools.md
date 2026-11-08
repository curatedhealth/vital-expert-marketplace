# Tools — confidence-scoring

## Offline

| Tool | Path | Purpose |
|---|---|---|
| faithfulness | `tools/faithfulness.py` | Faithfulness % from status counts |
| stamp_check_line | `tools/stamp_check_line.py` | Card / check-line stamps |

Formula (team default):  
`(supported + 0.5 × partial) / (supported + partial + unsupported + contradicted + unverifiable)`  
Leave `out_of_scope` out of the denominator.

```bash
python3 tools/faithfulness.py --supported 2 --partial 1 --unsupported 1 --json
```

## Live

VERIFY may return the same counts after tool-checked runs. Do not mix tool-checked and not-tool-checked rows in one percentage without labeling both.
