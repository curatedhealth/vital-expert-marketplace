# Task: Scan for ISI / brief summary / PI pointers

## Formula

| Slot | In this task |
|---|---|
| Worker | READY prep specialist. Does not approve. |
| Workflow | Steps below; stop when the output card is filled. |
| Skill | MLR fair balance and ISI |
| Knowledge | `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Default: `python ../../tools/check_isi_presence.py`. Optional live MCP when keys present. |
| Prompt | Use only supplied fields. Imperative. |
| Template | `../../templates/isi-fair-balance-checklist.md` |
| Input | Person words + prior packet fields + tool JSON. |
| Governance | Root `governance.md`. Missing → `[GAP]`. |

## Steps

1. Confirm required intake fields.
2. Run the offline tool when useful.
3. Fill the template; never invent locators or approvals.
4. Stamp with stamp_ready_line.py.

## Output

Match `../../templates/isi-fair-balance-checklist.md`. Then the liability line and stamp.
