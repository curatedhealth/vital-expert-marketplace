# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13).

```
True · sources: <n> claims that need a source, <n> with a source you supplied, <n> with a source named but not supplied, <n> with no source (not tool-checked)
True · kind of source: <n> claims resting on a source that cannot carry them for this reader (not tool-checked)
True · citations: <n> references looked at, <n> missing details a reviewer needs, <n> guidance or "current" statements with no title or date (not tool-checked)
```

Each line may carry up to three short plain notes after it, for the summary:

```
  - <note, e.g. "1 efficacy figure rests on a news story">
```

If no sources were supplied:

```
True · sources: not checked, no sources supplied (<n> statements affected)
```
