# Output format: change decision record

Short mode is the default for a direct question. 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line.

## Short mode

1. **Decision (owner's words):** quoted, with who decided and the date they gave; or "not yet stated by the owner".
2. **Rationale (owner's words):** one paragraph with evidence ids.
3. **Where the decision and the question sheet sit apart:** each with question id and row, or "none".
4. **Open questions:** ids.
5. **Approval:** "Approver: NAME as given / owner not named. Not signed by the model."
6. **Record:** "AI-assisted draft. Uncleared." or the clearer's name.

## Full mode

### 1. Identification
| Field | Value |
|---|---|
| Change id | |
| Item and version (from, to) | |
| Device and markets | |
| Baseline (most recently cleared device; certificate) | |
| Record created | date the record is written (never backdated) |

### 2. The change
Description, split into separate changes where bundled; changes since the baseline (QX12, QX13).

### 3. Frameworks applied
| Framework | Why it applies | Status and date of the guidance | Row |
|---|---|---|---|

### 4. Question sheet
Copied from A2: question, answer, basis, what the source says, row. Open questions marked.

### 5. Decision
Owner's words, verbatim. Who decided, the date they gave.

### 6. Rationale
Owner's words, with evidence ids (risk file, V&V reports, labeling).

### 7. Where the decision and the sheet sit apart
| Question | Answer | What the source says | How the rationale addresses it |
|---|---|---|---|

### 8. Consequences checked
| Item | Status | Row |
|---|---|---|
| Risk file reviewed and updated | | QS22, EU15 |
| V&V results; reopen rule | | QX15, QX16 |
| Field action: correction, removal, FSCA | | VG22 to VG25, VG3, VG8 |
| Submission or notification to prepare | | owner |
| Retention of this record | | `document-and-record-control.md` section 4 |

### 9. Approval
Approver: NAME as the person gives it. Date: as the approver signs in the QMS. The model does not sign or date.

### 10. Record
AI-assisted draft. Submissions, notified body notifications and field actions stop for the owner. Cleared by NAME via `verify.build_record`, or uncleared.
