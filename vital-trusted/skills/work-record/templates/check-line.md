# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. This file is the
one source for the Defensible line: `trusted-check` prints it in the Defensible row of the
TRUSTED summary, and `citation-and-record` adds only its own formal record line. Counts
only; no verdict words (TR-H3, TR-H13). Every line ends "(not tool-checked)".

```
Defensible · record: <n> materials, <n> assumptions, <n> open items (<n> without an owner); <status> (not tool-checked)
```

`<status>` is one of three forms, plus the "Uncleared draft (...)" placeholders in `status-line.md`, and no others:

- `Uncleared draft`
- `Uncleared draft, reviewed by <name>, as you told me` (only when the person said it)
- `Cleared by <name>, <role>, <date>`

Comments received are a note under "Uncleared draft", not a status:

```
  - comments from <name> received <date>, as you told me
```

Add when they apply:

```
Defensible · status words: <n> in the text with no named person behind them (not tool-checked)
Defensible · not known: <n> record entries the person could not supply, for example file versions (not tool-checked)
```

The formal record line comes from `citation-and-record`, not from this skill.

When no record was made, for example an internal quick note, return no line.
