## Dependency order
1. Business associate agreement signed [agreement] owner: Health system legal (Dana); planned 2026-11-02 to 2026-11-20
2. Security questionnaire returned [other] owner: Our security lead (Omar); planned 2026-11-02 to 2026-11-13
3. User roles and access set (minimum necessary) [access] owner: Health system IT (Raj); planned 2026-11-23 to 2026-11-27
4. Day-one workflow configured [configure] owner: Our implementation lead (Mia); planned 2026-11-30 to 2026-12-11
5. Super-user training [train] owner: Clinic nurse manager (Lee); planned 2026-12-07 to 2026-12-09
6. ADT and results interface tested with live records [integrate] owner: Health system IT (Raj); planned 2026-11-16 to 2026-12-18
7. End-user training [train] owner: Clinic nurse manager (Lee); planned 2027-01-11 to 2027-01-15
8. Silent-mode run on local data [silent_mode] owner: owner not named; planned 2026-12-21 to 2027-01-15
9. Go-live at pilot clinics [go_live] owner: Clinic medical director (Dr Park); planned 2027-01-18 to 2027-01-18
10. Scale-up to remaining clinics [scale_up] owner: Health system steering group; planned unset to unset

Go-live date in the plan: Go-live at pilot clinics: 2027-01-18

## Longest chain of planned durations (critical path)
Business associate agreement signed -> User roles and access set (minimum necessary) -> Day-one workflow configured -> ADT and results interface tested with live records -> Silent-mode run on local data (90 planned calendar days of work, gaps between steps not counted)

## Findings
- Order: 'ADT and results interface tested with live records' starts 2026-11-16 before its prerequisite 'Day-one workflow configured' finishes 2026-12-11
- Training rule: 'Super-user training' does not depend on any configure step (register rule: no training before the day-one workflow is configured)
- Training rule: 'Super-user training' starts 2026-12-07 before configuration finishes 2026-12-11
- Training rule: 'End-user training' does not depend on any configure step (register rule: no training before the day-one workflow is configured)
- Data rule: 'ADT and results interface tested with live records' moves personal data from 2026-11-16, before agreement 'Business associate agreement signed' is planned to be signed 2026-11-20
- Access rule: 'ADT and results interface tested with live records' moves personal data from 2026-11-16 before 'User roles and access set (minimum necessary)' finishes 2026-11-27 (minimum necessary and role-based access; US: CS103, CS104; other markets [GAP])
- Owner: 'Silent-mode run on local data' has no owner: owner not named
- Dates: 'Scale-up to remaining clinics' has no planned start or finish (unset)

Dates, owners and the go-live date are the person's. This check proposes none.
