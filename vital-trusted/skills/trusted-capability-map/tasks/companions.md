# Task TR-0.1.3 Companions

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague |
| Workflow | Say which companions exist, whether one is connected, what it adds, what stays method only |
| Skill | TR-0.1.3 |
| Knowledge | `references/tools.md` |
| Tool | None called. Detects whether VERIFY tools are present |
| Prompt | This guide |
| Template | `assets/companion-answer.md` |
| Input | The person's question; the assistant's current tool list |
| Governance | TR-H4, `references/governance.md` |

## Steps

1. **Check the tool list** for VERIFY tools (`references/tools.md`). Say plainly whether
   they are present.
2. **Explain what VERIFY adds** for the person's need: checking claims against supplied
   passages, qualifying sources, currency, citations, a record with a named clearer.
3. **Explain what VERIFY does not do**: it does not judge truth in the world; a support
   status is overlap with a supplied passage.
4. **If it is not connected**, explain that every TRUSTED skill still runs, and which
   checks will show as `[GAP: not checkable here]`. Give the connection steps from
   `references/tools.md`; if those are marked `[CHECK]`, say the steps are not yet
   published.
5. **Future companions** are candidates. Name them only if asked, and never as
   commitments.

## Boundaries

- Never describe a VERIFY result that no tool returned (TR-H4).
- No prices or plan details unless `references/tools.md` states them.
