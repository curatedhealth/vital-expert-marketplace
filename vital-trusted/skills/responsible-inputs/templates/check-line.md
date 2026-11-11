# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts and questions only; no verdict words (TR-H3,
TR-H13). Never include an identifier.

```
Ethical · what went in: <n> questions for your AI use policy (<kinds, e.g. unpublished study data, patient details>), <n> safer routes offered, <n> sensitive details kept out of the output (not tool-checked)
Ethical · other people's work: <n> items reproduced in full or close to it, <n> licensed or client-owned items, <n> questions for your licensing process (not tool-checked)
```

When the material was public or raised nothing, return no line: a task that does not
apply returns none (`../../trusted-check/references/letter-lines.md`).

When the person stated their policy covers the use:

```
Ethical · what went in: <n> items covered by your policy as you described it (not tool-checked; not compared with the policy text)
```
