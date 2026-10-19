# A2 Insight actionability indicators

Framework task: DH-02.04.3.2, Part A, task A2. Replaces the earlier "Action trace" section (CF-12.02.04.3.2.1).

## What this task delivers

Indicators computed from the person's insight log and change log as of a stated date: insights with an action, a refusal or nothing; open insights with their age and owner; time from raised to decided; refusals without a reason; actions not yet shipped; shipped changes traced to an insight, and those with no insight ("not traced to this research"); broken links; and, where a SUS file has rounds, the difference of means with n. Critical-task stops are counted apart. It answers "did our research lead to decisions and shipped changes, and what is still sitting open?"

Why it matters: the register's rule is "do not attribute a roadmap item to research after the fact" and "do not leave the stop only in a recording". Both can only be checked from logs that tie each change to an insight and each insight to a session stop.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.04.3.2 Part A, Insight actionability indicators |
| Workflow | The steps below |
| Knowledge | `references/actionability-indicators.md`; rows UX-US-32, UX-M-07 to UX-M-10 |
| Tool | `scripts/research_log.py trace` and `sus` (local, no connector). `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/insight-actionability-output.md` |
| Input | The request and its context: insight log (from the sibling's B1 or the person's tracker), change log, as-of date, SUS file with rounds if any, critical-task flags |
| Governance | `references/governance.md`; numbers only; rules and verdicts are the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **As-of date.** Ask; without it, ages cannot be stated. Default to today only if the person agrees, and write it.
- **Insight log.** Columns in the script header. A tracker export works if the columns map; write the mapping.
- **Change log.** Shipped changes with release, ship date and the insight id they cite, if any.
- **Rules.** The person's, if they have any (for example "every repeated stop decided within one release"). None: numbers only.
- **Mode.** Short for "did we act on it"; full for a quarterly research review.

## Workflow

### Step 1. Run the trace

`python3 scripts/research_log.py trace INSIGHTS.csv --as-of YYYY-MM-DD --changes CHANGES.csv`. Without files, build the same counts by hand from what the person pasted and say "from your summary".

### Step 2. Status and open items

Report decision status with denominators. List open insights oldest first with age, owner ("owner not named" where blank) and participants hit. Report refusals without a reason and insights without an owner.

### Step 3. Trace to shipped changes

Report changes traced, changes with no insight ("not traced to this research"), broken links (insight id not in the log), and actions with no shipped change by the as-of date. A link shows that a change cites an insight; if the person asks for a full action trace, check the cited stop and the participants' words in the session log, and mark a change whose stop is not in the record as "not from this study" (register method).

### Step 4. Critical-task stops

Count open and decided insights on tasks the owner flagged critical apart from the rest; report each open one by id, whatever the totals (UX-US-32).

### Step 5. SUS across rounds (if a file is given)

`python3 scripts/research_log.py sus SUS.csv --by round`. Report n, mean and the difference between rounds; say whether respondents differ between rounds; no significance claim (`[GAP]`). Context figures labeled (UX-M-08, UX-M-09, [PAPER], DOI 10.2196/37290).

### Step 6. Against the person's rules (only if given)

Mark each rule met, missed or not measurable, with the number behind it. Without rules, no verdict; ask for them.

## Build the output

Follow `assets/insight-actionability-output.md`. Answer first: decided vs open with denominators, the oldest open insights, and the changes not traced to research. Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every number has a denominator and the as-of date.
- No verdict without the person's rule; no target from the model.
- Changes with no insight are labeled, not credited to research.
- Critical-task insights are reported apart.
- No cause stated for an open insight; hypotheses only in B1.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- What to do about open stops and who owns them: B1.
- Usability metrics of a released product: `usability-monitoring`.
- Team performance: out of scope; the indicators describe the research pipeline, not people.
