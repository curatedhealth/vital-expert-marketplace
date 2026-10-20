# Output format: risk management file

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line.

## Short mode (default for a direct question)

1. **Answer:** two or three sentences: what the file needs or lacks, and the hazards the comparables add.
2. **Hazards from comparable products:** at most five events (counted as events, not rows): Event date · Firm and product line · Failure · Candidate hazard chain · In your file? (yes / no / partly).
3. **Controls to look at:** hazards controlled only by information for safety, controls with no verification.

Proposed hazards that do not come from a comparable event, and the security note, go to full mode. In short mode, name them in one line ("also proposed: wrong-sensor pairing, link spoofing; in the full version"). Count the words before sending.

4. **Open items:** the person's scales or criteria if missing; store gaps (EU vigilance and Swiss field safety actions not loaded).
5. **Record:** "Draft for the owner. Severity, probability and acceptability are yours. Uncleared AI-assisted draft." or the clearer's name.

## Full mode

### What the file must contain
The parts from EU14 to EU18 and ST4, each with its row. A note that the column structure is a working convention, not ISO 14971 text.

### Hazard table
| Hazard id | Hazard | Sequence of events | Hazardous situation | Harm | Severity (yours) | Probability or exploitability (yours) | Controls (type: design / protective / information) | Verification of implementation | Verification of effectiveness | Residual (yours) | Decision (yours) |
|---|---|---|---|---|---|---|---|---|---|---|---|

Proposed values are marked "proposed". Decision cells are empty until the person fills them.

### Hazards seeded from comparable products
| Event date | Firm, product line | Failure as recorded | Candidate hazard chain | Covered by | Source, retrieved |
|---|---|---|---|---|---|

Labeled: a comparable's event shows a hazard is foreseeable; it is not evidence about this product.

### Control priority check
Hazards where information for safety is the only control, and the reason recorded (or `[GAP]`).

### Residual and overall risk
Laid out against the person's criteria; overall benefit-risk left for the person (EU12, EU18).

### What would change this file
Triggers from QS22, EU15 and CH14.

### Gaps and sources
Store coverage line from `list_jurisdictions`; clause text not sourced; numbered sources with retrieval dates.

### Record
Draft for the owner. Cleared by NAME, or uncleared. AI-assisted draft.
