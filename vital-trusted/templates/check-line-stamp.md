# Letter lines

The lines a skill hands to `trusted-check`. They go to `trusted-check` only. Never paste
them into a reply the person reads directly. If the skill ships its own check line template in its `templates/` folder,
that file is the source of truth and wins over this one.

## Shape

```text
<Letter word> · <aspect>: <count> <plain noun phrase>, <count> <plain noun phrase> (not tool-checked)
  <note: where and what, in everyday words>   (0 to 3 notes)
```

## Rules

- Letter words, never codes: Tangible, Rule-compliant, Unbiased, Safe, True, Ethical,
  Defensible. True has its own line.
- Counts only. Write a zero as 0. No verdict words.
- Every line for a check that ran ends "(not tool-checked)", because every result is read
  by hand.
- A line for a check that did not run reads `<Letter word> · <aspect>: not checked, <what
  is missing>`, optionally followed by `(<n> statements affected)`. It carries no
  "(not tool-checked)" suffix, because nothing was read. This is the one not-run form
  `trusted-check` accepts (`skills/trusted-check/references/letter-lines.md`).

## Example

```text
Tangible · usefulness: 2 generic sentences, 1 missing decision (not tool-checked)
Rule-compliant · claims and label: 1 comparative claim, 1 claim beyond the label (not tool-checked)
Unbiased · balance: 2 benefits without matching risks (not tool-checked)
Safe · possible safety reports: 1 mentioned in the draft or the material, to pass to your safety reporting procedure (not tool-checked)
True · claims compared by hand: not checked, no passages supplied (4 factual claims affected)
True · sources: 3 claims with no source, 1 figure to confirm (not tool-checked)
Ethical · responsible use: 1 input to confirm with your AI use owner (not tool-checked)
Defensible · record: 3 materials, 1 assumption, 2 open items (1 without an owner); Uncleared draft (not tool-checked)
```

## Tool

`python tools/stamp_check_line.py --letter 'True|sources|3 claims with no source' ...`
builds the same lines from letter words. It labels every line for a check that ran
"not tool-checked" and leaves a "not checked, ..." line without the label.
