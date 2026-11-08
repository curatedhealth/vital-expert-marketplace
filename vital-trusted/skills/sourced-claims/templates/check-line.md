# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13).

```
True · sources: <n> claims that need a source, <n> with a source you supplied, <n> with a source named but not supplied, <n> with no source (<not tool-checked | checked with VERIFY>)
True · kind of source: <n> claims resting on a source that cannot carry them for this reader (<e.g. 1 efficacy figure from a news story>) (<not graded with a tool | graded with VERIFY>)
True · citations: <n> references looked at, <n> missing details a reviewer needs, <n> guidance or "current" statements with no title or date (<not built with a tool | built with VERIFY>)
```

If no sources were supplied:

```
True · sources: not checkable — no sources supplied (<n> claims in the draft that would need one)
```
