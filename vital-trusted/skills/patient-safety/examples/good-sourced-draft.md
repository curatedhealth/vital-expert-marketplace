# Rendered example: doctor email with safety flag first (sourced draft)

Invented teaching case ("Corvelan" fictional). Bundle order: Part B flag, then draft
reply, repair note, stamp.

## Safety flag (`templates/safety-flag.md`, person sees this first)

Before the draft: something to pass to your safety reporting procedure

Dr. Weber's email of 14 October 2026 mentions:
- "came out in an itchy rash on her arms about ten days after starting Corvelan last month"
  — possible side effect

Please pass this to your safety reporting procedure as soon as you can, in the time it
sets. Forward the original email, unchanged.

I have not judged whether it is related to Corvelan, how serious it is, or whether it
must be reported. Your safety team decides that.

## Draft reply (excerpt, label quoted)

Dear Dr. Weber,

The Swiss Summary of Product Characteristics for Corvelan (revision March 2026) states:

- Section 4.2: "Moderate renal impairment (creatinine clearance 30 to 50 mL/min): the
  recommended dose is 10 mg once daily. Corvelan is not recommended in patients with
  creatinine clearance below 30 mL/min."
- Section 4.5: "Concomitant use with strong CYP3A4 inhibitors (for example clarithromycin)
  increases corvelastat exposure. Concomitant use with strong CYP3A4 inhibitors should be
  avoided."

[GAP: needs a decision — whether and how this reply mentions the rash — ask medical
information or safety]

## Label statements table (`templates/label-statements.md`, excerpt)

| Question in draft | Label section | Match |
|---|---|---|
| Dose in moderate renal impairment | 4.2 quoted verbatim | yes |
| Clarithromycin interaction | 4.5 quoted verbatim | yes |
| Rash after starting product | (not answered in reply) | gap — procedure |

## Repair note (`templates/repair-note.md`, excerpt)

Part B: flag written before reply. Part A: two SmPC sections quoted word for word; no
dose advice for this patient. Removed any draft wording that said the rash was "probably
unrelated" in the company's voice.

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. Acknowledgment of reported rash in outbound reply — company procedure not supplied — next: Ask

Not yet checked
- Whether SmPC March 2026 is current approved text for Switzerland — needs label-source tool
```

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / patient-safety: not tool-checked (offline tools) · Part B: 1 possible AE flagged; Part A: 2 label quotes, 0 paraphrase errors
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Safe · safety statements: 2 label-backed statements, 0 mismatch with supplied label (not tool-checked)
Safe · possible side effects: 1 item to pass to your safety reporting procedure (not tool-checked)
```
