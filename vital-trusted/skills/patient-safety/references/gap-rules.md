# Gap rules applied to patient safety

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/gap-rules.md`.

Same format and classes as every TRUSTED skill:
`[GAP: <class> — <what is missing> — <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | No label, or the supplied part of the label does not hold the dose, warning, interaction or population the draft needs |
| `conflicting` | Two supplied labels (two versions, two markets, SmPC and leaflet) give different wording for the same statement |
| `out of date or unclear date` | The label has no revision date, or the person is unsure it is the current approved version |
| `not checkable here` | Whether the supplied label is the current approved one for this market, when no label-source companion is connected |
| `needs a decision` | How a reply mentions a reported event; which contact route a public reply gives; whether a product named in a report is the company's |

Wording rules:

- Name the exact item and the label section: "adult dose in moderate renal impairment,
  section 4.2", not "dosing information".
- Never hint at a value inside a gap ("usually 10 mg").
- "The label does not address X" is a finding only when the complete label was supplied
  and read. Otherwise use `not supplied`.
- **A safety flag is never a gap.** A possible side effect, pregnancy, overdose, misuse,
  medication error, lack of effect or quality problem is always written as a flag in the
  format of `assets/safety-flag.md`, never as `[GAP]`, and never left for later.
- A gap never stands in for a judgment the skill must not make. Do not write
  `[GAP: needs a decision — whether reportable]`; write the flag and point to the
  procedure.
