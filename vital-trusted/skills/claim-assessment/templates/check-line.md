# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran. Counts only; no verdict words (TR-H3, TR-H13). The six results are defined
once in `../references/statuses.md`. The shape follows the shared stamp: letter word,
aspect, counts, then "(not tool-checked)" at the end.

```
True · claims compared by hand: <n> factual claims; <n> found in your passage, <n> partly found, <n> not found in your passage, <n> your passage says something different, <n> no passage to compare with; listed separately: <n> opinion, recommendation or definition (not tool-checked)
```

Part A only:

```
True · claims listed by hand: <n> to check first, <n> to check next, <n> with no passage supplied (not tool-checked)
```

If no material was supplied:

```
True · claims compared by hand: not checked, no passages supplied (<n> factual claims affected)
```

Counts go to `confidence-scoring` for the open-items summary. A hand check never produces a
confidence figure.
