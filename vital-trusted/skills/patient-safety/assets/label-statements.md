# Output format: safety statements from the label

Used when a dosing or safety table is asked for, or when a reply quotes several safety
statements. Every cell is label text quoted exactly, or a gap. Nothing from memory
(TR-H1). Shown to the person; plain headings, no rule ids.

```
Safety statements for <product, formulation> — from the label you supplied
Label: <title as given>, <market>, revision date <date as shown | [GAP: out of date or unclear date — revision date — confirm the current approved label]>

| Topic | What the label says (word for word) | Label section |
|---|---|---|
| Dose, adults | "<quoted text>" | <e.g. 4.2> |
| Dose, children | "<quoted text>" or [GAP: not supplied — dose in children — from section 4.2] | <section> |
| Elderly | "<quoted text>" | <section> |
| Kidney impairment | "<quoted text, with the label's own cut-offs>" | <section> |
| Liver impairment | "<quoted text, with the label's own classes>" | <section> |
| Contraindications | "<quoted text>" | <e.g. 4.3> |
| Warnings and precautions | "<quoted text>" | <e.g. 4.4> |
| Interactions | "<quoted text>" | <e.g. 4.5> |
| Pregnancy and breastfeeding | "<quoted text>" | <e.g. 4.6> |

Where a row says "not supplied", the part of the label you gave me does not cover it.
Where the label you gave me is complete and silent on a topic, the row says:
"The label does not address this in the text supplied."
```

Below the table, at most three plain lines:

```
I quoted the label you supplied; I did not check that it is the current approved version.
<If for a prescriber's question:> This gives the label's statements; the decision for the patient is the prescriber's.
Next step: <your medical information procedure | your medical review | your promotional review process> before it is used.
```

Drop rows that the request does not need. Never fill a row to make the table complete.
