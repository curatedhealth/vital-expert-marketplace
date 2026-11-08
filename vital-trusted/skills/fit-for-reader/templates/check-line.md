# Output format: check lines for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13).

```
Tangible · fit for the reader: written for <reader as stated | reader not stated>, <n> passages above or below that reader's level, <n> terms or abbreviations not explained (not tool-checked)
Tangible · format: asked for <format and length as asked>, delivered <as asked | differs: what> (not tool-checked)
Tangible · translation: <n> passages where the meaning differs from the original, <n> numbers or units changed, <n> terms left for a qualified translator or approved wording (not tool-checked)
```

- The translation line is returned only when a translation was made or checked.
- The format line is returned only when a format, length or limit was asked for or is
  on the context card.
- For patient material, "passages above that reader's level" counts passages, not
  scan hits. The scan output is never pasted into the line.

Each line may carry up to three short plain notes, for the summary:

```
  - <where and what, e.g. "second paragraph: 'concomitant therapy' in a letter for patients">
  - <e.g. "asked for one page, delivered four">
  - <e.g. "hazard ratio 0.66 written as 0,7 in the German version">
```

If the reader is not known and the work leaves the company:

```
Tangible · fit for the reader: not checkable — reader not stated (<n> passages affected)
```

If a translation was asked to be checked but the original was not supplied:

```
Tangible · translation: not checkable — original not supplied (<n> passages affected)
```

## Change from the contract in `trusted-check/references/letter-lines.md`

The contract proposes one line for audience and format together:
`Tangible · fit for the reader: written for <reader as stated>, <n> passages above or
below that reader's level, format <as asked | differs: what>`. This skill returns one
line per task instead, as the contract's own grammar requires ("one line per task that
ran"), adds a count of unexplained terms, adds two counts to the translation line
(numbers or units changed; terms left for a qualified translator), and ends each line
with the tool status. The owner of `trusted-check` should update `letter-lines.md` to
match, or tell this skill's author to revert.
