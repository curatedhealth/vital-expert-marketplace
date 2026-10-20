# A2 Message fidelity audit

Framework task: DH-01.02.2.2, Part A, task A2. Replaces the "stayed fair-balanced" half of the old "Message Impact Monitoring" section.

## What this task delivers

A statement-by-statement table for the communication the person supplies (an abstract, a congress slide, a payer narrative, a lay summary, a press release, a medical-information letter, or a third-party review that restates the trial): each statement, the passage it should rest on, whether it matches in direction, population, comparator, outcome, time point and effect, the certainty it claims against the rating, the drift type and rows, a flag level, and a faithful wording for the owner. The task flags; it never clears.

Why it matters: evidence drifts in small steps. A waiting-list comparator becomes "versus usual care", "low certainty" becomes "strong evidence", a harm drops out of the slide. Each step looks harmless; together they make a communication the trial does not support, and in regulated material an omission is itself misleading (PC-US-03).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Bound: `cybersecurity-architect-digital-health` (binding under owner review; see SKILL.md) |
| Skill | DH-01.02.2.2 Part A, Message fidelity audit |
| Workflow | The steps below |
| Knowledge | `references/fidelity-checks.md`; `references/certainty-wording.md`; `references/audience-rules.md`; A1 statements from the sibling skill if they exist |
| Tools | `verify.extract_claims`; `literature.get_record`; `verify.check_currency` or `literature.check_retraction`; `verify.qualify_source` and `verify.check_claim` per statement; `literature.find_related {direction: "cited_by"}` only when the person asks where the trial is being restated; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/fidelity-audit-output.md` |
| Input | The request and its context; the communication text; its audience and market; the studies it rests on with their results passages (or the sibling skill's A1 statements); the person's certainty ratings with raters; the cleared or certified intended use per market |
| Governance | `references/governance.md`; every flag and faithful wording stops for the owner the person names for regulatory or legal review, or owner not named |
| Catalogue job | `evidence-table` (available) can rebuild the evidence base in one call; the checks below remain the method (`examples/live/jobs_and_experts.json`). |

## Read the request

- **Communication.** Take the text the person gives. Claims arrive as text; do not scrape a site.
- **Audience and market.** Changes which rows apply. Ask once if not stated; otherwise audit for the strictest audience the material could reach and say so.
- **Evidence base.** The A1 statements from the sibling skill, or the papers and passages. Without passages, every statement is `[GAP]` and the audit says it could not check them.
- **Is it marketing?** An ad, an app store text or a promotional claim set goes to dh-go-to-market (pricing-and-value-message-monitoring, claims audit). Audit the evidence statements in it and point there for the rest.
- **Short or full?** "Is this summary faithful" is short; "audit our launch evidence materials" is full.

## Workflow

### Step 1. Split the communication into statements

Call `verify.extract_claims` with the text. It splits by sentence; split compound sentences yourself and drop sentences with no factual content. Keep offsets.

### Step 2. Confirm the sources are current

For each paper the communication rests on, call `verify.check_currency` (or `literature.check_retraction`) with the DOI. A retracted source makes every statement resting on it Stop (drift 9). Say which source was checked (Crossref only in the live run).

### Step 3. Match each statement to its passage

Find the passage in the A1 statement or the paper. When a source is open access, read the full text before marking a field `[GAP]` from an abstract. Call `verify.qualify_source` with the DOI, then `verify.check_claim` with the statement, the verbatim passage and the full returned source object (register C18). Then read it yourself, field by field: direction, population, comparator, outcome and time point, effect as reported. The tool's status is a starting point only: in the live run a wrong comparator and an overstatement both came back "partial", the same as a faithful claim that named an instrument the passage lacked (register N3; `examples/live/verify_calls.json`).

### Step 4. Check certainty and required statements

Compare every certainty word and effect verb with the person's rating per outcome, using the Table 15.6.b wording for that rating (ES-203 to ES-207; `references/certainty-wording.md`, rule 5). Check the required statements for the audience and market (`references/audience-rules.md`): limitations and balanced information for US payors (PC-US-40), unfavorable findings for US clinicians (PC-US-31), study identification in German advertising (PC-DE-05).

### Step 5. Classify and flag

Name the drift type from `references/fidelity-checks.md` with its rows, and set Stop, Review or Note. For each Stop and Review, draft a faithful wording that keeps only what the passage and rating support, labeled "draft for the owner". Never write "accurate", "compliant" or "approved"; "no flag" means only that no check here found a difference.

### Step 6. Third-party restatements (only if asked)

If the person asks where the trial is being restated, call `literature.find_related {record, direction: "cited_by", limit}`. It lists citing papers (no total count, no citation intent). Audit a citing review only on text the person supplies. Describe what that publication says; never attribute error or intent to its authors.

### Step 7. List what the owner decides

Each Stop and Review, each faithful draft, each [INDUSTRY] or [WF] row relied on, each `[GAP]`. Name the owner the person gave, or "owner not named".

## Build the output

Follow `assets/fidelity-audit-output.md`. Answer first: N statements; Stop, Review, Note counts; the drift that matters most.

## Before you hand it over

- Every flag names the passage compared and the drift type with its rows.
- No result rests on a Verify status alone.
- Certainty is compared with a named rating, or the audit says none was given.
- Count the words in short mode.
- If the audit leaves the conversation, ask who clears it and call `verify.build_record`, recording that it is an audit, not a clearance; otherwise label it an uncleared draft.

## Boundaries

- The skill never clears a communication.
- Marketing claims and ads: dh-go-to-market (pricing-and-value-message-monitoring). Payer routes, submissions, prices and HTA dossiers: dh-access-and-value (payer-engagement-and-hta-submission). Device status: dh-regulatory-and-quality (regulatory-pathway-monitoring). Review method: dh-clinical-development (literature-and-real-world-evidence-review).
- No letters to editors or to third-party authors.
- Drugs and biologics are out of scope.
