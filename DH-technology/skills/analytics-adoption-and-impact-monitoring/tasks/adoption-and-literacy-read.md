# A1 Adoption and literacy read

Framework task: DH-05.02.1.3 and DH-05.03.2, Part A, task A1. Carries the old tasks "Enablement task" and "Practice record" (DH-05.02.1.3.1 and .2), "Literacy objective", "Curriculum unit", "Curriculum owner" (DH-05.03.2.1.1 to .3), "Campaign audience", "Campaign activity", "Campaign result" (DH-05.03.2.2.1 to .3), "Champion role", "Champion roster" and "Champion load" (DH-05.03.2.3.1 to .3).

## What this task delivers

As of the person's read date and for their window: the adoption funnel from the roster and usage log, by role or site (in scope, invited, trained, practice task done, active, task completed in the product), both Proctor penetration figures with their denominators, export-only users, the people who attended but did not complete the practice task and the step they stopped on, champion load and sites with no champion, and the literacy objectives and curriculum currency as the person wrote them. It answers "of the people who should use it, how many can and do, and where do they stop?"

Why it matters: the old tasks warned "Do not count attendance as enablement" and "Do not report completers without the audience size". A training log with 90% attendance can sit beside a product nobody uses in production, and a rate over volunteers says nothing about the ward.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-governance-director` (old DH-05.02.1.3 and DH-05.03.2). Work as an adoption analyst who counts on the person's files |
| Skill | Analytics adoption and impact monitoring, Part A, Adoption and literacy read |
| Workflow | The steps below |
| Knowledge | `references/adoption-measurement.md`; rows CS8, CS22 to CS49, CS61, CS62, CS77, CS78; `references/governance.md` |
| Tools | None from the library (`literature.get_record` only if the person asks about a paper). `scripts/adoption_check.py funnel`, `champions`, `words`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/adoption-and-literacy-read-output.md` |
| Input | The request and its context: the product and the trained task, the roster, the usage log, the window and read date, the literacy objective and curriculum unit with its metric version, the campaign activities, the champion roster and question log |
| Governance | `references/governance.md`; the person judges |
| Catalogue job | none |

## Read the request

- Is a window and a read date given? Without them, write "not given" and ask; the funnel is not run.
- Who is in scope? The roster's `in_scope` column is the valid denominator (CS27, CS28). If the person gives only a list of attendees or licensed users, say which denominator that is and that it is not adoption.
- What is the trained task, in the person's words, and which event in the log records it? If no event records the task, "task completed" is "not instrumented `[GAP]`", never zero.
- By role, by site, or both? Report groups, not named individuals, unless the person asks for a named follow-up list for their own use.

## Workflow

### Step 1. Literacy objective and unit (old DH-05.03.2.1)

Write back the role, the task they will be able to do (for example read a certified metric, question a chart), the metric or template used, what the curriculum does not teach, the practice task, the mistaken reading the unit corrects, the proof that shows they can do the task, the unit owner and the metric version it matches. Missing elements are "not given". If the metric's certified version has changed since the unit was written (from A2 or the person's register), flag it: "Do not teach a metric version that has been corrected" (old DH-05.03.2.1.3).

### Step 2. Funnel

With code execution, run:

```
python3 scripts/adoption_check.py funnel --roster ROSTER.csv --events EVENTS.csv --since <window start> --as-of <read date> --by site
```

(and `--by role` if asked). Report each stage over the people in scope, with numerator and denominator: invited, trained (attended), practice task done (proof), active in the window, task completed in the product (penetration 1: completers / in scope, Proctor 2011, CS39, DOI 10.1007/s10488-010-0319-7), and penetration 2 (completers / trained). Report export-only users as "activity without the task in the product" (old DH-05.02.3.2.2). Report the flags: A1 no valid denominator, A2 attended without proof, A3 events outside the window (left out), A4 events for people not on the roster (left out, counted), A5 export-only, A6 practice task not done with the step stopped on.

### Step 3. Where people stop

From the roster's `stopped_step`, count the steps people stopped on after training (old DH-05.02.1.3.2, "Record who could not, and the step they stopped on"). Report the steps and counts by group. A repeated step is a fact for the design owner (task design, the template or the workflow), not a judgment of the people.

### Step 4. Campaign result (old DH-05.03.2.2)

Write back the campaign audience (role and count, or `[GAP]`), the objective, who is out of scope, each activity and date, and how attendance is recorded. Report completers against the audience size from step 2; "Do not count a mail send as completion". The follow-up for those who did not complete is the person's (B1).

### Step 5. Champions (old DH-05.03.2.3)

Run:

```
python3 scripts/adoption_check.py champions --roster ROSTER.csv --events EVENTS.csv --since <window start> --as-of <read date>
```

Report questions logged per champion in the window, champions with no record as "unmeasured (no record)", and sites in scope with no champion. Check the roster for the date each champion agreed; a champion listed without an agreement date is flagged (old DH-05.03.2.3.2, "Do not list a champion who has not agreed"). Champions drive implementation and overcome resistance (CFIR 2009, CS8, DOI 10.1186/1748-5908-4-50; ERIC, CS46, DOI 10.1186/s13012-015-0209-1); they do not certify metrics and are not the support desk for broken data.

### Step 6. Context the person may ask for

If the person asks which strategies exist for low uptake, list the ERIC names and definitions that match (audit and feedback CS44, training CS45, champions CS46, staged scale-up CS47, adaptability CS48, data relay CS49) as names, not effectiveness claims. If training is offered as the fix for a decision support error, state that FDA human factors guidance (reissued 3 August 2026) treats training as valid but not preferred because knowledge decays (CS77, CS78), labeled as device guidance used as context. In the NHS, usage is reported against an expected usage profile agreed at commissioning (NICE ESF standard 16, CS61); elsewhere the expected profile is the person's.

## Build the output

Follow `assets/adoption-and-literacy-read-output.md`. Answer first: penetration 1 and 2 by group with denominators, the stage where the largest drop sits (from the script's counts), export-only users, the most common stopped step, and sites with no champion. No verdict. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/adoption_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rate shows numerator, denominator and window; the denominator is the people in scope.
- Attendance is not counted as enablement; a missing event is "not instrumented", never zero.
- No target, benchmark or verdict came from the model; groups, not named individuals, unless the person asked.
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- `python3 scripts/adoption_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Designing the task, template or workflow people stop on: `analytics-products-and-decision-support` (this pack); usability `dh-patient-and-user-experience` usability-monitoring.
- Customer adoption of the company's own product: `dh-go-to-market` adoption-monitoring.
- Equity of reach across patient groups: `dh-patient-and-user-experience` health-equity-monitoring.
