# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran. Counts only; no verdict words (TR-H3, TR-H13).

With VERIFY:

```
True · claims checked with VERIFY: <n> claims; <n> supported, <n> partial, <n> unsupported, <n> contradicted, <n> unverifiable, <n> out of scope (support from your passages, not truth in the world)
```

Without VERIFY:

```
True · claims compared by hand (not tool-checked): <n> claims; <n> found in your passage, <n> partly found, <n> not found, <n> passage says otherwise, <n> no passage, <n> opinion or recommendation [GAP: not checkable here — whether each sentence matches its passage — connect VERIFY]
```

Part A only:

```
True · claims listed: <n> to check first, <n> to check next, <n> with no passage supplied (<split by VERIFY | manual split>)
```

If no material was supplied:

```
True · claim assessment: not checkable — no passages supplied (<n> factual sentences in the draft)
```

Status counts with VERIFY go to `confidence-scoring` for the confidence figure. Manual
counts never produce a confidence figure.
