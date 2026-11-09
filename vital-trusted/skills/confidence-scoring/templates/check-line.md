# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. It fills the
True row's counts in the TRUSTED summary. Counts only; no verdict words (TR-H3, TR-H13).
The shape follows the shared stamp: letter word, aspect, counts, then "(not tool-checked)".
The six results are defined once in `../../claim-assessment/references/statuses.md`.

```
True · open items: <n> factual claims; <n> found in your passage, <n> partly found, <n> not found in your passage, <n> your passage says something different, <n> no passage to compare with; listed separately: <n> opinion, recommendation or definition; <m> open items (not tool-checked)
True · No confidence figure: these results were not tool-checked.
```

When nothing factual was compared:

```
True · open items: 0 open items, nothing factual compared, <k> opinion, recommendation or definition (not tool-checked)
True · No confidence figure: these results were not tool-checked.
```
