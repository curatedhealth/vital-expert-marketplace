> Shared origin: authored in the co-design execution skill (patient-research-and-co-design, DH-02.03.1.1), 19 October 2026, copied unchanged below this line so this package stands alone. R-1 to R-13 are listed in this skill's references/quality-criteria.md.

# The insight log: from capture to decision

Shared by the co-design execution skill (DH-02.03.1.1) and the co-design quality monitoring skill (DH-02.03.1.2). The columns are a VITAL method choice; the rules each column serves cite their row. `scripts/insight_tracker.py` reads these files.

## Four files, one chain

capture (what was said) → insight (a point the team tracks) → decision (accept, defer, refuse) → change (what shipped, in which version)

| File | One row per | Columns |
|---|---|---|
| `sessions.csv` | session | session_id, date, planned_types (for example "patient;carer"), attended (for example "patient:4;carer:1;staff:1") |
| `captures.csv` | thing a participant said or did | capture_id, session_id, captured, participant_ref (a code, never a name), participant_type (patient, carer, staff, clinician, other), kind (request or observation), insight_id, words |
| `insights.csv` | insight | insight_id, summary, status (open, accepted, deferred, refused), decision_date, reason, owner, decision_due (optional), linked_change, version, safety_constraint (yes, no, blank) |
| `changes.csv` | design change in a release | change_id, description, credited_to_codesign (yes or no), insight_ids, in_backlog_before (optional date), shipped_version, shipped_date (optional) |

## What each column is for

| Column | Serves | Row |
|---|---|---|
| words | Record claims in their words; do not turn them into a requirement in the capture. | R-6, R-9 |
| kind | Separate a request from an observation. | R-7 |
| participant_ref and participant_type | Count how many participants raised a point; keep carers and staff apart from patients. | R-8, R-5, PE-13 |
| status, reason, owner | Accept, defer or refuse with a reason. | R-11 |
| version, linked_change | Name the product version that will show an accepted change. | R-12 |
| safety_constraint | Say so when a change contradicts a safety constraint. | R-13 |
| in_backlog_before | Do not credit co-design for a change the team already planned. | R-14 |
| decision_due | The person's date for writing the decision on an unresolved point. | R-15 |

R-14 and R-15 come from the monitoring tasks of the old skill (CF-12.02.03.1.2.1 "Do not credit co-design for a change the team already planned"; CF-12.02.03.1.2.3 "Name the date the accept, defer, or refuse will be written"), read 19 October 2026. R-1 to R-13 are in `co-design-method.md`.

## Rules that are the person's

- **Repeated point.** The register's starting rule is "points raised by more than one participant" (R-10). The person may adopt it or set another. The script takes it as `--repeat N` and sets no default.
- **Who counts.** By default the script counts patients and carers as patient-side participants and lists staff and clinicians apart (R-5). Whether carer words count toward a patient point is the person's call; say which way the tally went.
- **Status vocabulary.** open, accepted, deferred, refused. "Open" covers captured but not yet decided.
- **Decision dates.** Only the person sets `decision_due`. The script reports "past the decision_due you set", never "overdue" against its own clock.

## Never in the log

Names, initials, email addresses, phone numbers, addresses, dates of birth, record numbers, photographs, or any detail that could identify a participant. The `check` subcommand scans for these before any other step.
