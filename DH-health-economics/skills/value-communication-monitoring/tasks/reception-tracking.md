# A1 Reception tracking

Framework task: DH-01.07.4.2, Part A, task A1. Replaces the old "Reception measure" and "Reception score" tasks.

## What this task delivers

A tally of how each audience responded to each line (or claim) of the value narrative or dossier, from the person's own log, on the codes and measure the person names, with the notes kept verbatim and the base (number of responses) beside every share.

Why it matters: a payer that keeps asking for budget impact on its own membership is telling you which line does not land (HE-021, [PAPER] DOI 10.1016/j.jval.2013.08.2291); a share without its base, or a measure the model chose, tells you nothing.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.4.2 Part A, Reception tracking |
| Workflow | The steps below |
| Knowledge | `references/reception-measures.md`; `references/gap-rules.md` |
| Tool | None from the library. `scripts/reception_log.py` when code execution is available |
| Prompt | This guide |
| Template | `assets/reception-output.md` |
| Input | The person's log (one row per response: date, audience, organization, use, line id, claim id, response code, note); the measure; the minimum base; the flag rule if any |
| Governance | `references/governance.md` |
| Catalogue job | None |

## Read the request

- **The measure.** Old rule: use the measure the person named. Typical shapes: share of responses coded as a miss, per line; count of rejections per audience. If none is named, give counts only and ask (`[GAP]`).
- **The codes.** The person's. If the log uses free text, ask the person to code it, or propose codes labeled "proposed" and wait.
- **Grouping.** By line, claim, audience or use, as asked.
- **Score only with the person's result.** Old rule. The model does not add responses, infer a response from silence, or weight organizations.
- **Short or full?** "Which lines are landing" is short; "reception report for the quarter" is full.

## Workflow

### Step 1. Check the log

Required columns present; no row without a code or a line id; dates in range. Report rows dropped and why. Keep no patient-level or confidential deal data; if present, stop and ask the person to remove it.

### Step 2. Tally

Count responses per group and code. If code execution is available: `python3 scripts/reception_log.py LOG.csv --by line_id --numerator <codes> --min-n <n> --flag-at <share>` with the person's values. Without code, tally by hand and show the counts.

### Step 3. Apply the person's measure

Share = responses in the person's numerator codes over responses in the base. Keep "no response" out of the base unless the person counts it. Below the person's minimum base, report the count only.

### Step 4. Flag

Flag only where the person set a rule. Without a rule, nothing is flagged; say so.

### Step 5. Read the notes against the sources

For each line with misses, list every non-empty note verbatim, one per response; never drop or merge a note to save words. Where a note names something a source speaks to, add the row from `references/reception-measures.md` (for example a request for PMPM: HE-138, AMCP 6.0 draft; year-one savings: HE-122). Before handing over, count the notes listed against the misses in the tally. This explains the request; it does not decide that the stakeholder is right.

## Build the output

Follow `assets/reception-output.md`. Answer first: which lines land and which do not, on the person's measure, with the base.

## Before you hand it over

- Every share has its base and the person's measure named; no model-chosen threshold.
- No objection reported as evidence about the product.
- Count the words in short mode; record line.

## Boundaries

- Coverage decisions and formulary outcomes as access results belong to dh-market-access.
- No judgment of stakeholders or of the team.
