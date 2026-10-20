# Adoption measurement

Interpretive reference for tasks A1 and B1. Each sourced rule carries its row; `implementation-and-adoption-research.md` holds the URL, verbatim quote and read date. Where this file states a step from the old framework tasks (DH-05.02.1.3, DH-05.03.2), it says so.

Scope note from the research file: implementation frameworks give definitions and heuristics, not thresholds. No source sets an adoption level, a penetration target or a literacy pass mark. Those are the person's.

## 1. Denominators

| Rule | Source and rows |
|---|---|
| Reach is computed on a valid denominator of eligible people, not of volunteers who expressed interest | RE-AIM, re-aim.org, read 19 October 2026 (CS27) |
| Setting-level adoption is the percent of settings approached that participate; staff-level is the percent of staff invited that participate | RE-AIM (CS28) |
| Adoption is the number, proportion and representativeness of settings and delivery staff willing to start | RE-AIM (CS24) |
| Implementation: staff fidelity, consistency, time and cost; at the individual level, use of the intervention | RE-AIM (CS25) |
| Maintenance: institutionalization; setting-level check is whether the program still runs 6 or more months after support ends | RE-AIM (CS26, CS30) |

In this skill the "people in scope" on the person's roster are the valid denominator. A rate computed over attendees, volunteers or licensed seats is labeled with that denominator and is not called adoption.

## 2. Proctor implementation outcomes

Proctor 2011, DOI 10.1007/s10488-010-0319-7 (the library record gives 2010, online first; cite by DOI):

| Outcome | Use here | Rows |
|---|---|---|
| Eight outcomes, distinct from service and clinical outcomes | Name which one each figure is | CS31 |
| Implementation outcomes are preconditions for service or clinical outcomes; a failed deployment is separated from an ineffective product | A product never used cannot be judged on its outcome | CS32 |
| Acceptability; appropriateness (fit), kept distinct | Survey or interview results the person brings | CS33, CS35 |
| Adoption (uptake): intention, decision or action to try | Invited and trained stages | CS34 |
| Fidelity | Task done in the product as the curriculum defines it | CS37 |
| Implementation cost | The person's figure, if given | CS38 |
| Penetration: eligible users who use the service / all eligible; providers delivering / providers trained or expected to deliver | `funnel` prints both, named "penetration 1" and "penetration 2" | CS39 |
| Sustainability (maps to RE-AIM maintenance) | Later reads | CS40 |

Overlapping terms (research file, "Changes and conflicts"): adoption is defined in both Proctor and RE-AIM; pick one definition per metric and name it.

## 3. The funnel stages (old task method with the rows)

| Stage | Counted from | Rule |
|---|---|---|
| In scope | Roster `in_scope` | The valid denominator (CS27, CS28). Old DH-05.03.2.2.1: name the role and the count, or mark the count `[GAP]`; "Do not campaign to everyone" |
| Invited | `invited_on` | Staff-level adoption counts invited staff (CS28) |
| Trained (attended) | `trained_on` | Attendance only; "Do not count attendance as enablement" (old DH-05.02.1.3.2); "Do not count a mail send as completion" (old DH-05.03.2.2.2) |
| Practice task done | `practice_task_done` | The proof the curriculum names (old DH-05.03.2.1.2, "Name how you will know they can do the task"); who could not, and the step they stopped on (old DH-05.02.1.3.2) |
| Active in window | Any usage event in the window | Activity, not adoption |
| Task completed in product | `task_completed` event in the window | The decision recorded in the product: penetration 1 (CS39) |
| Export only | Activity with exports and no task completed | Old DH-05.02.3.2.2: "Do not claim the workflow changed if the user must export" |

Report completers with the audience denominator (old DH-05.03.2.2.3, "Do not report completers without the audience size").

## 4. Strategies the person may be reading against (ERIC)

ERIC (Powell 2015, DOI 10.1186/s13012-015-0209-1) is an expert-consensus list of 73 named strategies (CS41). Rows that match analytics enablement:

| Strategy | Rows |
|---|---|
| Audit and feedback: summarize performance data over a period and give it to clinicians and administrators | CS44 |
| Ongoing, dynamic and train-the-trainer training | CS45 |
| Identify and prepare champions; identify early adopters | CS46 |
| Stage the scale-up from pilots | CS47 |
| Promote adaptability while naming the elements that must stay fixed | CS48 |
| Relay near-real-time data to providers | CS49 |

These are names and definitions, not effectiveness claims. The person chooses the strategy.

## 5. Champions

Champions drive an implementation and overcome resistance (CFIR 2009, CS8, DOI 10.1186/1748-5908-4-50; ERIC, CS46). Old task method (DH-05.03.2.3): a champion has a role they already hold and agreed on a date; they help (office hours, chart review) but do not certify metrics and are not the support desk for broken data; count questions taken in the period if a record exists, mark a champion with no record as unmeasured, and name who replaces a champion who left; name a domain or site with no champion. `champions` prints questions logged per champion and sites in scope with no champion.

## 6. Training as a control

Where enablement is offered as the fix for a decision support error, the FDA human factors guidance (reissued 3 August 2026) treats training as a valid but not preferred strategy, because knowledge from training decays (CS77, CS78). This is device human factors guidance, used here as context for internal analytics; say so. Usability evidence for a device is `dh-regulatory-and-quality` and `dh-patient-and-user-experience` usability-monitoring.

## 7. Usage against an expected profile (NHS context)

NICE Evidence Standards Framework (last updated 9 August 2022), standard 16: the company and evaluator agree a plan to report ongoing usage against an expected usage profile agreed at commissioning, with anonymized aggregate outcomes (CS61), and for products that change over time how and when performance changes are reported and to whom (CS62). For an internal analytics product, the "expected usage profile" is the person's own; NICE ESF is cited as NHS context.

## 8. Curriculum currency (old task method)

Old DH-05.03.2.1.3: name the owner of a curriculum unit, the event that forces an update (a metric version change) and the last version the unit matches. "Do not teach a metric version that has been corrected." A unit that teaches a metric whose certified version changed (A2 governance read) is flagged as a fact.

## 9. What is not sourced

- Any adoption, penetration, literacy or champion-load target or benchmark `[GAP]`.
- A validated data-literacy assessment instrument: none in the research files `[GAP]`.
- Customer health, renewal or NPS rules: not sourced, and out of scope here (`dh-go-to-market` value-realization-monitoring).
