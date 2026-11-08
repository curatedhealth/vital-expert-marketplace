# Output format: check lines for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in the shape set in `trusted-check/references/letter-lines.md`. Counts
and routing only; no verdict words and no clinical, causality or reportability judgment
(TR-H3, TR-H6, TR-H13). Build skills have no tool today, so every line ends "not
tool-checked".

```
Safe · safety statements: <n> statements on dosing, warnings, interactions or special populations, <n> not as the label states them, label <supplied | not supplied> (not tool-checked)
Safe · patient wording: <n> passages for patients with no route to a doctor, nurse or pharmacist (not tool-checked)
Safe · possible side effects: <n> mentioned in the draft or the material, to pass to your safety reporting procedure (not tool-checked)
```

Up to three plain notes per line, saying where and what:

```
  - <e.g. "dose for children is stated but the label supplied covers adults only">
  - <e.g. "leaflet says 'completely safe' and tells readers they can stop when they feel better">
  - <e.g. "doctor's email, second paragraph: rash after starting treatment">
```

Rules for these lines:

- **Patient wording** runs only for patient material. Advice, false reassurance and
  alarming framing go in its notes; the count in the line stays the one in the contract.
- **Possible side effects** counts every mention Part B flagged, of every kind: side
  effects, pregnancy or breastfeeding, overdose, misuse, medication errors, lack of
  effect, off-label use as reported, product quality problems. The notes name the kind.
  Never add "serious", "known" or "reportable".
- This line also surfaces in `trusted-check` as an open item when the Safe letter is off.

When no label was supplied and the draft has safety content:

```
Safe · safety statements: not checkable — no label supplied (<n> statements affected)
```

When the material holds nothing to flag:

```
Safe · possible side effects: 0 mentioned in the draft or the material (not tool-checked)
```
