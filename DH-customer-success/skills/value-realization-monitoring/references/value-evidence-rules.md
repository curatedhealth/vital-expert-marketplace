# Value evidence rules: thresholds over time and notes sent to customers

Interpretive reference for A1, A2 and B1. Rows are CS rows in `customer-success-research.md`. Register rules are the VITAL register's earlier task sections for this competency (evidence class V): offered to the person, applied only if adopted.

## Thresholds over time (A1)

| Check | What it finds | Basis |
|---|---|---|
| Target no account has met in any period | A target that may not match the offer, or a deployment problem everywhere | Register: "Flag a threshold no account has ever met" |
| Signal with no data in the latest period | A field the product or the customer report no longer provides | Register: "Flag a signal that is no longer stored"; NICE ESF Std 19 data dictionary (CS64) |
| Signal with no data for some accounts | A reporting gap per account; outcome shares cannot be read | Denominator logic, CS87 |
| Denominator basis differs from the target's | A share that is not reach (enrolled or interested instead of eligible) | CS27 |
| Target eased between versions, turning accounts to met | A change that may make accounts green without any change in use or outcome | Register: "Do not lower a threshold only to turn accounts green" |
| Account-specific target added or changed | Same, at account level | Same |
| Usage profile changed since commissioning | The expected profile was agreed with the customer; changing it is a change to the agreement | NICE ESF Std 16 (CS61) |
| Product changed in a way that affects performance | Agreed reporting on performance changes, to whom | NICE ESF Std 16 (CS62) |
| Maintenance window reached | Setting-level maintenance can be checked 6 or more months after support ends (this skill's analogy from study funding) | CS26, CS30 |

What the skill never does: decide that a target was wrong, or that an eased target was unjustified. It shows the change, its date and version, who set it, and which accounts it turned. The person decides.

## Notes sent to customers (A2)

A value note is backed when each result it states matches a signal row: same account, measure and period, and a value within the rounding tolerance the person sets. The register's rules: "Match each claimed result to a signal row"; "Mark a note with no signal row as unsupported"; "Do not accept a narrative in place of the signal."

| Status | Meaning |
|---|---|
| Supported by the signal row | The stated number matches the row within the person's tolerance |
| Value differs from the signal row | A row exists; the stated number does not match it |
| Unsupported: no signal row | No row for that account, measure and period (for example a mean drop that is not a tracked measure) |
| Unsupported: the note names no measure | A narrative claim with no number to trace |
| Signal row exists; no value stated | The note cites a measure but states no figure |

A matched number is not a cleared claim. Separate, for every note, the wording questions the match cannot answer:

| Wording type | Example | Why it is a separate question |
|---|---|---|
| Effect | "reduced depression", "clinically proven" | Uptake and customer-reported outcomes are not clinical evidence; no comparator (CS32) |
| Forecast or saving | "will cut your costs" | Not checkable against any row; observed `verify.extract_claims` marks it checkable (`tools.md`) |
| Comparison | "outperforms", "better than" | Needs comparative evidence this skill does not hold |
| Severity label | "moderate or worse symptoms" | Only with the PHQ-9 bands (CS92); no GAD-7 or PAM bands are sourced (CS93, CS95) |
| Payment | "qualifies for full payment" | Market Access `outcomes-contract-monitoring` |

The law on promotional claims is not in this skill's sources `[GAP]`. Flag the wording to the person's regulatory or legal owner; the Commercial pack's claims check (dh-commercial) can lay out the rules; neither clears.

## Correction (B1)

Register rules, offered: "Name the author of the note"; "State whether the note is withdrawn or the signal is added"; "Name the date of the correction"; "Do not leave an unsupported note in the account record." In this skill the author is named only as the person's record shows it; the choice between withdrawing the note and adding a signal, the owner, and the date are the person's. A signal may be added only from data the product stores; it never retrofits a number to fit the note.
