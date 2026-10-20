# Handoff score, period 2026-09-01 to 2026-10-15

Rule applied (the person's, as confirmed): a handoff is received when received_on is on or before the period end and received_by matches receiver_named. A message sent is not a receipt. Rows due in the period, and rows due earlier still open at its start, are scored; none is dropped.

| id | Work product | Category | CTQ | Status | Fact | Note |
|---|---|---|---|---|---|---|
| H1 | Therapy model specification v2 (session content and sequence) | clinical evidence | yes | late | received 2026-09-08, due 2026-09-01 (7 days after) |  |
| H2 | SRS and SDS trace to the therapy model | clinical evidence | yes | open | not received by 2026-10-15 |  |
| H3 | Reward rule: drug screen result gates the reward | clinical evidence | yes | not measurable | received_by (Tom (QA)) is not the named receiver (Priya (software lead)); ask whether the person's rule counts it |  |
| H4 | Impact assessment: journaling feature on the device function | clinical evidence | yes | open | not received by 2026-10-15 |  |
| H5 | Physician labeling: summary of clinical testing | clinical evidence | yes | open | not received by 2026-10-15 |  |
| H6 | Clinical study report final | clinical evidence | yes | late | received 2026-10-02, due 2026-09-30 (2 days after) |  |
| H7 | App store description text | copy | no | received | received 2026-10-01, due 2026-10-03 |  |
| H8 | Deployment data dictionary for pilot site | implementation | no | not measurable | no due date [GAP]; ask the person for it |  |
| H9 | Design review 3 input pack | clinical evidence | yes | not measurable | receiver not named [GAP]; ask the person who receives it |  |
| H10 | End-user training approach description | implementation | no | received | received 2026-10-09, due 2026-10-10 |  |

Scored: 10 (late 2, not measurable 3, open 3, received 2). Outside the period: 0 (none).

To ask the person (not measurable until answered; nothing is filled in):
- H3: received_by (Tom (QA)) is not the named receiver (Priya (software lead)); ask whether the person's rule counts it
- H8: no due date [GAP]; ask the person for it
- H9: receiver not named [GAP]; ask the person who receives it

Received on time over measurable handoffs: 2 of 7. Not measurable kept out of this denominator and listed above.

By the person's category (each category counted separately, never merged):
- clinical evidence (CTQ marked by the person: yes): late 2, not measurable 2, open 3
- copy (CTQ marked by the person: no): received 1
- implementation (CTQ marked by the person: no): not measurable 1, received 1
