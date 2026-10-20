# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. It fills the
True row's "checked with VERIFY" lines in the TRUSTED summary. Counts only; no verdict
words (TR-H3, TR-H13).

When VERIFY ran:

```
→ checked with VERIFY: <n> backed, <n> partly backed, <n> not backed, <n> contradicted, <n> could not be checked (<k> not factual, not counted)
→ faithfulness <n>% (support from supplied passages, not truth in the world); <m> open items
```

When nothing factual was checked:

```
→ checked with VERIFY: no factual statements (<k> not factual); no confidence figure
```

When VERIFY did not run:

```
→ not tool-checked: no confidence figure (VERIFY would check each statement against its passage)
```
