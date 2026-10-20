# CAPA: what the sources require, and what the person decides

Interpretive reference for task B1, and the basis for the effectiveness check in the monitoring skill. Rows from `quality-systems-sources.md` and `primary-text-additions.md`.

## What the sources require

| Requirement | Row |
|---|---|
| The QMSR incorporates ISO 13485's corrective action (8.5.2) and preventive action (8.5.3) clauses; FDA says this is no change in expectation | QS17 |
| CAPA depth is "appropriate to the magnitude of the problem and commensurate with the risks encountered", with procedures for assessing risk, actions for different risk levels, and methods that correct or prevent recurrence | QS18 |
| Complaint investigations, CAPA and management review inputs remain linked through ISO 13485 clauses 8.2.2, 8.5.2 and 8.3.1 | QS19 |
| Risk documentation is reviewed and updated when previously unforeseen risks or new information emerge | QS22 |
| EU: the QMS must include management of corrective and preventive actions and verification of their effectiveness (Art. 10(9)(l)) | EU4 |
| EU: production and PMS information is evaluated for its impact on hazards, risk estimates, overall risk and benefit-risk; controls are amended if needed | EU15 |
| EU: a manufacturer who considers a marketed device non-conforming immediately corrects, withdraws or recalls it, and informs authorities where there is a serious risk | EU7 |
| MDSAP: a repeat nonconformity within three years indicates a corrective action was not adequately taken or implemented | QS47, R3 |

## What the sources do not prescribe

- **A root cause method.** None of the sourced rows names one `[GAP]`. Use the method the person's CAPA procedure names. If it names none, ask; do not pick one for them.
- **Risk levels and the action per level.** FDA expects procedures that set them (QS18); the levels themselves are the person's.
- **Effectiveness criteria.** The EU requires verification of effectiveness (EU4) but no sourced row defines the test. The person sets it.
- **Timelines for CAPA closure.** None in the sourced rows `[GAP]`.

## The plan's parts

| Part | Content | Who decides |
|---|---|---|
| Problem statement | The nonconformity, complaint or finding ids, product and version, scope | Facts from A1 or A2 |
| Risk level | The level under the person's procedure, with the risk file entry it rests on | The person |
| Correction | What fixes this instance | The person approves |
| Cause | The result of the person's root cause method, with the evidence for it; "not yet established" is a valid state | The person's investigation |
| Corrective action | What removes the cause | The person approves |
| Preventive action | Where a potential nonconformity is addressed (other products, versions, sites with the same design or process) | The person approves |
| Effectiveness criteria | For each action: the record to read, the measure, the window, the pass condition | The person sets |
| Linked obligations | Risk file update (QS22, EU15), design change (change control), correction or removal record (VG22 to VG24), vigilance (task A2) | Routed, not decided |
| Owner | Named by the person | The person |

Method rules carried from the VITAL register (old skill text, kept): a CAPA that is only "retrain the person" fits only when the cause is that the person was not trained. A failed effectiveness check opens a new action; the old one is not reopened as if the check had not failed. A finding is not closed while a new action is open.

## Proportional depth

QS18 sets depth by "magnitude of the problem" and "risks encountered". The plan therefore scales on the person's risk level under their procedure. The model applies that procedure and shows where it did. If the person has no scaling rule, the model may draft one, labeled "proposed", for example: lower levels a correction and a short effectiveness check; higher levels a documented cause investigation, preventive action across affected products and a risk file update. It is not applied until the person confirms it.

## Where a CAPA leads elsewhere

- A software fix to a marketed device is a design change (CH9). Whether it needs a new 510(k) or is a significant change under MDCG 2020-3 is a change-control question (CH4 to CH16), outside this skill.
- A fix pushed to the field may be a correction under 806 (VG25) or an FSCA under the MDR (VG3, VG8). Route to A2 for the reporting clocks.
