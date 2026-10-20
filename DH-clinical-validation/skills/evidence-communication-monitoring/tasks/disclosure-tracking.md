# A1 Disclosure tracking

Framework task: DH-01.02.2.2, Part A, task A1. New in this version: the old skill had no disclosure check; it fills the "did the evidence reach the record" half of message impact monitoring.

## What this task delivers

A per-trial table, as of a stated date: which regimes the person confirmed apply, whether registration met the ICMJE test and (for an applicable clinical trial) the 21-day rule, each results clock with its due date and status, and the publication status, each with its rule and arithmetic. Plus the trials where nothing could be computed and why.

Why it matters: an unposted result is a legal miss for an applicable trial (CV145) or an EU CTR trial (CV152), and a late registration can close ICMJE journals to the paper (CV132). The clocks are fixed facts; tracking them is arithmetic on the right dates, and the common failure is using the wrong date (registry start date for first consent, completion date for primary completion).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Bound: `cybersecurity-architect-digital-health` (binding under owner review; see SKILL.md) |
| Skill | DH-01.02.2.2 Part A, Disclosure tracking |
| Workflow | The steps below |
| Knowledge | `references/disclosure-rules.md`; `references/clinical-study-and-rwe-research.md` (CV rows) |
| Tools | `literature.find_trial` (status and sponsor for an NCT id; registration link for a paper), optional; `literature.search_literature` or `get_record` for a publication the person names; `scripts/disclosure_clock.py`; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/disclosure-tracking-output.md` |
| Input | The request and its context: the trial list; per trial the registry and id, the person's answers on regimes (ICMJE journal, US applicable clinical trial, EU CTR, WHO signatory), and the dates (first consent, first enrollment, registration submitted, primary completion, study completion, end of trial in all EU Member States, any certification, approval, extension, and the dates results were submitted or a paper published) |
| Governance | `references/governance.md`; registry actions stop for the person responsible for the registry |
| Catalogue job | none. The catalogue has no disclosure job. |

## Read the request

- **Trials in scope.** Take the person's list. Never assemble a sponsor's trial portfolio by searching; the library cannot list a sponsor's trials.
- **Regimes.** Ask for the person's answers. The tests are in `references/disclosure-rules.md` (CV133, CV142, CV143). An unanswered regime is not computed and is `[GAP]`; the skill never infers applicable clinical trial status from phase, sponsor country or device type.
- **Dates and their meaning.** Registry "start date" is not first consent or first enrollment; "completion date" is not primary completion. Ask which date the person means when a registry record is the source.
- **As of when?** Today unless the person names a date.
- **Short or full?** "Are we overdue on X" is short; "disclosure status for the portfolio" is full.

## Workflow

### Step 1. Confirm each trial's identity

For an NCT id, call `literature.find_trial {nct_id}` once if the person wants the library's view: it returns title, overall status, phase and sponsor, and no dates (`references/tools.md`). For other registries (DRKS, CTIS, ISRCTN) the library holds nothing; work from the person's record. Registry facts are not sent to Verify (register C1).

### Step 2. Collect the dates and answers

Put the person's dates and regime answers into the CSV layout in `scripts/disclosure_clock.py`. Where the person gives a registry record instead of dates, copy the dates from it and label which registry field each came from. Missing dates stay blank.

### Step 3. Compute the clocks

With code execution, run `python3 scripts/disclosure_clock.py trials.csv --as-of YYYY-MM-DD`. Without it, compute by hand, showing each line: ICMJE (CV132), US registration (CV141), US results with certification, approval and extension (CV145 to CV147), EU results (CV152), WHO pledge (CV140). One calendar year is added for "1 year"; the counting convention is not sourced `[GAP]`, say so once.

Keep the word 'pledge' on every WHO row and say once that the 18 May 2017 joint statement is a pledge, not law (CV140). In the answer line, count 'not met' registration tests alongside past-due clocks.

### Step 4. Publication status

For each trial the person says should be published, take the publication date from the person, or check a named paper with `literature.get_record`. Do not search for a sponsor's unpublished trials and do not conclude "unpublished" from an empty search: the library does not reach Embase or Cochrane (`literature.list_sources`). Registry posting is not prior publication (CV137).

### Step 5. Content checks the person asked for

If the person asks whether a posting was complete, list the US content items (CV148) or the EU lay summary duty (CV152, Annex V content `[GAP]`), and compare against what the person shows. No judgment on quality beyond the listed items.

## Build the output

Follow `assets/disclosure-tracking-output.md`. Answer first: how many clocks are past due, due, met or not computed, and the one that matters most, each with its rule.

## Before you hand it over

- Every status names the rule, the input date (with its source field) and the arithmetic.
- No regime applied that the person did not confirm; no "unregistered" or "unpublished" concluded from the library's silence.
- Past-due items are stated as facts, without urgency language.
- Count the words in short mode.
- If the table leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The skill does not post results, request extensions, certify delays or contact registries.
- No legal opinion on penalties or enforcement (not sourced).
- Planning disclosure for a new study belongs to the sibling skill (evidence-translation-and-communication, task A2).
