# Worked example: A2 deployment sequence and prerequisites

Run on 19 October 2026. The plan is an illustrative file written for this example (`sample-data/deployment_plan.csv`): a US health system deploying a remote monitoring product at two pilot clinics, owners and dates as the example person gave them. No library call was needed for the sequence; the field-event call shown is a real call (`live/safety_events.json`).

**Request:** "Here's our plan for the two pilot clinics at the health system (US). Can you check the order before I send it to their IT team? Interface testing uses live records and the silent-mode run uses their data."

**Calls and runs**

1. `python3 scripts/plan_sequence.py sample-data/deployment_plan.csv` (output: `plan_sequence_run.md`)
2. Not called in this run: field events. Shown for the format only: `regulatory-dh.search_safety_events {manufacturer: "Philips", since: "2026-01-01", jurisdiction: "US", limit: 5}` returned one Class II recall (EPIQ Elite ultrasound software, 7 August 2026); not the example product.

## Answer (short mode)

**The checks found five conflicts in your plan.**

1. **PHI before the BAA.** "ADT and results interface tested with live records" starts 16 November 2026; the business associate agreement is planned to be signed 20 November 2026. A vendor may handle PHI only under a written contract meeting 164.504(e) (CS96).
2. **Interface test before configuration.** The same step starts 16 November 2026, before its own prerequisite "Day-one workflow configured" finishes 11 December 2026.
3. **Training before configuration.** "Super-user training" starts 7 December 2026, before configuration finishes 11 December 2026, and neither training step depends on configuration (register rule: no training before the day-one workflow is configured). Training knowledge decays over time (CS78).
4. **PHI before access is set.** The same step starts 16 November 2026, before user roles and minimum necessary access are set 27 November 2026 (CS103, CS104).
5. **No owner** for "Silent-mode run on local data": owner not named. Who owns it?

The go-live date in your plan is 18 January 2027 for the pilot clinics. Scale-up has no dates (unset).

**Order (dependency):** BAA signed (Health system legal, Dana) > user roles and access (Health system IT, Raj) > day-one workflow configured (Our implementation lead, Mia) > interface test with live records (Raj) > silent-mode run (owner not named) > go-live (Clinic medical director, Dr Park) > scale-up (Health system steering group). Training: super-user then end-user (Clinic nurse manager, Lee); proposed: both after configuration.

**Prerequisites your plan already covers or should show (US):**
- BAA elements to check with your legal owner: permitted uses, safeguards, incident and breach reporting, subcontractor flow-down, return or destroy at termination, termination right (CS97 to CS101); breach notice at most 60 calendar days after discovery (CS102).
- Role-based access by job need (CS104): in the plan.
- Site-owned, not in the plan, added: a standard protocol for the recurring ADT feed limiting PHI to what is reasonably necessary (CS105); workforce PHI and security training (CS82, CS83).

**What it means for you:** if the interface test keeps its date, PHI would reach you four days before the written contract exists. Moving the test after both the BAA and configuration also moves the silent-mode run and may move go-live; the dates are yours to reset.

**Stops:** the BAA terms are your legal or privacy owner's to judge. Sending this plan to the health system's IT team is a go-live plan issued to a health system: it stops for your accountable owner (who is that?).

**Record:** Sequence draft on your plan. Uncleared. AI-assisted.

The full version adds the step table with dates, the critical path (BAA > roles > configuration > interface test > silent mode, 90 planned calendar days of work) and the BAA element table.

## What this example shows

- The script found the conflicts; the rows gave the reason; no date or owner was proposed.
- The answer leads with conflicts, the go-live date stays the site's, and sending the plan to the customer is flagged as a stop.
- Word count of the answer section: under 450 (checked with `wc -w`).
