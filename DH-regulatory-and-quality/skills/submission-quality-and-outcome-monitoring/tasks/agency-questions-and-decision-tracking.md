# A2 Agency questions and decision tracking

Framework task: DH-03.03.4.2, Part A, task A2. Replaces "Submission Approval Outcome Monitoring".

## What this task delivers

A dated view of where a filed submission stands: FDA days and sponsor days used, which escalation points apply, the hold letters and their response routes, set beside the MDUFA goals and FDA's actual reported performance, plus how comparable devices in the same product code were decided, and for the EU the notified body timeline context labeled as a contractor study. It answers "where are we in review, what is the agency waiting for, and how did similar devices go?"

Why it matters: review time has two owners. In FY 2025 an average De Novo spent 132.16 days under FDA review and 145.96 days with the sponsor (S-45). Tracking both clocks shows which part the team controls.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.4.2 Part A, Agency questions and decision tracking |
| Workflow | The steps below |
| Knowledge | `references/outcome-signals.md`; `references/submission-sources-supplement.md`; `references/REG_PATHWAYS_SUBMISSIONS.md` |
| Tools | `regulatory-dh.list_jurisdictions` (free), `search_devices`, `get_pathway_precedents`, `get_authorization`, `find_predicates`; `scripts/review_clock.py` (optional) |
| Prompt | This guide |
| Template | `assets/tracking-output.md` |
| Input | Pathway, the event dates (received, each hold letter, each response, decision), the content of any open agency questions as the person summarizes them, the product code, comparables the person names |
| Governance | `references/governance.md`; responses to the agency stop for the regulatory owner |

## Read the request

- **Pathway and events.** Ask for the received date and every hold and response date. Without them FDA days cannot be counted; say so.
- **Open questions.** The person's summary of the agency's questions, not the letter text, unless they paste it. Never send it to the library.
- **Product code or comparables.** From the person, or from the predicate in their submission.
- **Mode.** "Where are we?" gets short mode; a status pack gets full mode.

## Workflow

### Step 1. Count the clocks

From the events, count FDA days (clock stops at each hold letter, restarts at the response; S-25, S-26), sponsor days and total calendar days. With code execution: `python3 scripts/review_clock.py events --file events.csv --pathway 510k|denovo|pma --as-of <today>`. Report against the goal for the pathway in FDA days (RP US-46 to RP US-48) and the escalation point (S-27 for 510(k) at 100 FDA days; S-32 for De Novo at 180). State that the script counts calendar-day differences and FDA's own same-day rules are not sourced.

### Step 2. Open agency questions

For each hold letter: what stopped the clock, the response options and timelines from `outcome-signals.md`: SIR within 60 days for 21-day feedback (S-33, S-34), the formal response still due on the letter's timeline (S-35), De Novo 180-day response rule (RP US-13), eSTAR replacement within 180 days (S-16). The 510(k) Additional Information deadline is `[GAP]` in the files read: the letter governs. Group the person's open questions by dossier section; this feeds B1.

### Step 3. Goals beside actual performance

From `outcome-signals.md`, give the goal and FDA's actual figures for the pathway, each with basis and cohort year (for example 510(k): 97.94% of FY 2025 decisions within 90 FDA days, RP US-57; average total 141.24 calendar days, RP US-58; shared total-time goal 112 calendar days on a trimmed cohort, S-28, S-29). Flag that the FY 2026 cohort is still open.

### Step 4. Comparables

1. `regulatory-dh.list_jurisdictions` (free) once.
2. If the person named a device, `regulatory-dh.search_devices(query=<name>, jurisdiction="US")` to get its reference and product code.
3. `regulatory-dh.get_pathway_precedents(product_code=<code>, jurisdiction="US")` for counts by pathway and year.
4. `regulatory-dh.find_predicates(product_code=<code>)` to list the decisions in the code, then `regulatory-dh.get_authorization(reference=...)` for each one the person cares about.
5. With code execution, save the authorization rows and run `python3 scripts/review_clock.py comparables --file <saved.json>` to get calendar days per record.

Report each comparable by what its record states: pathway, received and decided dates, calendar days, predicate named, source URL, retrieval date. Say that the median from `get_pathway_precedents` mixes pathways and is calendar days, not FDA days; that De Novo `status` "DENG" means granted; and that the record does not show earlier submissions for the same device. Never forecast the person's decision from comparables.

### Step 5. EU or notified body, if relevant

Use the notified body survey figures as context, labeled "contractor study commissioned by the Commission, data to 28 February 2026" (RP EU-40, RP EU-44, S-71 to S-74). The library cannot give EU time to certificate (EUDAMED decision dates empty). The person's own notified body dates are the only measure of their file.

### Step 6. What it means for the person

Close with consequences in sourced terms only, for example: "You are at 88 FDA days of the 90-day goal with the clock running; if no decision by 100 FDA days, FDA provides written feedback on all outstanding issues (S-27)." No predicted decision date.

## Build the output

Follow `assets/tracking-output.md`. Answer first: where the clock stands, what the agency is waiting for, and the next sourced trigger.

## Before you hand it over

- Every figure says FDA days or calendar days, goal or actual, and its cohort year.
- Comparables are described only by their records, with dates and sources.
- The notified body survey is labeled a contractor study.
- Any response wording is a draft for the regulatory owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No prediction of the decision or its date.
- No legal reading of a deficiency letter; the person's regulatory owner and counsel interpret it.
- Drugs, biologics and wellness apps are out of scope.
