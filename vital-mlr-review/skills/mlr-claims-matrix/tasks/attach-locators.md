# Task: Require paragraph-level locators or [GAP]

## Formula

| Slot | In this task |
|---|---|
| Worker | READY prep specialist. Does not approve. |
| Workflow | Steps below; stop when the output card is filled. |
| Skill | MLR claims matrix |
| Knowledge | `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Default: `python ../../tools/mlr_claims_matrix_offline.py`. Optional live MCP when keys present. |
| Prompt | Use only supplied fields. Imperative. |
| Template | `../../templates/claims-matrix-card.md` |
| Input | Person words + prior packet fields + tool JSON. |
| Governance | Root `governance.md`. Missing → `[GAP]`. |

## Steps

1. Confirm required intake fields.
2. Run the offline tool when useful.
3. Fill the template; never invent locators or approvals.
4. Stamp with stamp_ready_line.py.

## Output

Match `../../templates/claims-matrix-card.md`. Then the liability line and stamp.
