# Handoff log check as of 2026-10-20

Rule applied: a field left blank is printed as [GAP]. The log is the person's; nothing is filled in.

| id | Work product | Sender to receiver | Blocked decision | Owner owes | Asked on | Days open | Late path | Missing |
|---|---|---|---|---|---|---|---|---|
| H1 | Therapy model specification v2 (session content and sequence) | Clinical science to Software engineering | SRS freeze for release 2.0 | Dr Lena Kraus | 2026-08-04 | received | Software builds against model v1 and flags differences | none |
| H2 | SRS and SDS trace to the therapy model | Software engineering to Clinical science | Design review 3 go or no-go | Priya (software lead) | 2026-09-08 | 42 | Design review 3 moves to the next slot | none |
| H3 | Reward rule: drug screen result gates the reward | Clinical science to Software engineering | Verification protocol for the reward module | Dr Lena Kraus | 2026-09-01 | received | [GAP] | late_path |
| H4 | Impact assessment: journaling feature on the device function | Wellness feature team to Device software team | Design validation sign-off | [GAP] | 2026-09-10 | 40 | Hold release of the journaling feature | owner_owes |
| H5 | Physician labeling: summary of clinical testing | Clinical science to Regulatory | Labeling freeze | Dr Lena Kraus | 2026-09-15 | 35 | [GAP] | late_path |
| H6 | Clinical study report final | Clinical operations to Clinical science | Physician labeling draft | Marco (clinical operations) | 2026-08-01 | received | Labeling drafted from the interim report | none |
| H7 | App store description text | Marketing to Regulatory | Store listing update | Jonas (marketing) | 2026-09-20 | received | Keep current listing | none |
| H8 | Deployment data dictionary for pilot site | Product to Customer implementation | Pilot site go-live plan | Priya (software lead) | 2026-09-22 | 28 | [GAP] | late_path |
| H9 | Design review 3 input pack | Software engineering to Design review attendees | Design review 3 go or no-go | Priya (software lead) | 2026-09-29 | 21 | [GAP] | receiver_named, late_path |
| H10 | End-user training approach description | Clinical science to Customer implementation | Pilot site go-live plan | Dr Lena Kraus | 2026-09-22 | received | Use interim training slides | none |

Records: 10. Fields missing across the log: 6.
Open handoffs in dependency order (each after the open items it waits on): H2, H4, H5, H8, H9
