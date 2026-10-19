# A2 Value evidence check

Framework task: DH-02.02.3.2, Part A, task A2. Replaces the earlier "Value evidence check" section.

## What this task delivers

Every value note or QBR result sent in the period, matched to the account file: supported by the signal row, value differs, or unsupported (no row, or no measure named). Beside it, the wording each note uses that no signal row can carry: effect, forecast or saving, comparison, severity label, payment. It answers "is what we told customers backed by our data?"

Why it matters: the register's rules are "Match each claimed result to a signal row" and "Do not accept a narrative in place of the signal". A note can match its row and still overreach: uptake and customer-reported outcomes are not clinical evidence (CS32).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.3.2 Part A, Value evidence check |
| Workflow | The steps below |
| Knowledge | `references/value-evidence-rules.md`; `references/outcome-measures.md` |
| Tools | `scripts/account_health.py notes` (no connector); `verify.extract_claims` (counted, with the person's agreement to pass the note text); `literature.get_record`, `verify.qualify_source` and `verify.check_claim` (counted) only when a note cites a published paper |
| Prompt | This guide |
| Template | `assets/value-evidence-check-output.md` |
| Input | The request and its context: the notes sent (text, account, date, author as the record shows it, the measure and period each result refers to, the stated value), the account file, the person's rounding tolerance |
| Governance | `references/governance.md`; a match is backing on the number, not clearance of the wording |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **Notes.** The notes or deck slides sent, in the period the person names. If only the text is given, extract the results first (Step 1).
- **Tolerance.** How much rounding the person accepts (for example 0.005 on a share). Without it, match exactly and say so.
- **Mode.** Short for "is this note right"; full for a period audit.

## Workflow

### Step 1. List the claims

If a note is given as text, call `verify.extract_claims {text}` with the person's agreement, or split it by sentence by hand. For each claim record: account, measure (the person's signal name), period, stated value. Split sentences that join a number with a forecast; the tool marked such a sentence "checkable" in the live test (`references/tools.md`). A claim with no number and no measure is a narrative claim.

### Step 2. Match to signal rows

With code execution: `python3 scripts/account_health.py notes ACCOUNTS.csv --notes NOTES.csv --tol <their tolerance>`. By hand: find the row with the same account, measure and period; compare the values within the tolerance. Statuses in `value-evidence-rules.md`. A measure that is not tracked (for example a mean PHQ-9 drop when the plan tracks a share with a 5-point drop) has no row: unsupported.

### Step 3. Wording a match cannot clear

For every note, supported or not, flag wording by type (`value-evidence-rules.md`): effect, forecast or saving, comparison, severity label, payment. Severity labels are acceptable only with the PHQ-9 bands (CS92); GAD-7 and PAM bands are not sourced (CS93, CS95). Effect wording is flagged even when the number matches.

### Step 4. Published findings in a note

If a note cites a paper, call `verify.qualify_source {doi, question}`, then `verify.check_claim {claim, passage, source}` with a passage you have read and the `source` object the first call returned. Accept "supported" only if the passage states the claim in the same direction: in the live test the tool returned "supported" for "A PHQ-9 score of 10 represents severe depression" from a passage that says 10 is moderate (register N3). Cite from the record, not the returned citation (title null, register C18).

### Step 5. What it means for the person

Two or three consequences, conditional: "Note VN-01 told Northfield 62 percent of eligible members activated; the account file shows 455 of 1,000 (45.5 percent) for the same period." No cause, no judgment of the author.

## Build the output

Follow `assets/value-evidence-check-output.md`. Answer first: how many notes and results are supported, differ or are unsupported, and which wording goes beyond any row. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every status cites the row (account, measure, period, value) or says no row exists.
- Effect, forecast, comparison and payment wording is flagged even where numbers match.
- Authors appear only as the record names them; no judgment of people.
- Account data went into no library call; note text only with the person's agreement.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The check matches numbers and flags wording; it does not clear claims (the person's regulatory or legal owner; the Commercial pack can lay out the rules).
- What to withdraw or correct, and who owns it, is B1.
- Payment claims are Market Access `outcomes-contract-monitoring`.
