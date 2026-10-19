# A1 Renewal and retention definitions

Framework task: DH-02.02.2.2, Part A, task A1. Replaces the earlier "Renewal rate definition" section (CF-12.02.02.2.2.1).

## What this task delivers

A definitions card the team will report against: the cohort, the unit, what counts as renewed, lost and open, the exclusions, the value basis, how expansion and contraction are counted, what counts as a signed offer, the formula for each figure, and the owner of the definitions. It also checks the card for internal consistency and says plainly that these are the person's definitions, not a standard. It answers "what exactly will we report as our renewal rate and retention?"

Why it matters: no source defines these measures for digital health (`references/renewal-measures.md`). Two teams can report "90 percent renewal" from the same accounts with different denominators. Writing the definition down before the figures are computed is the only way the number means the same thing next period.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.02.2.2 Part A, Renewal and retention definitions |
| Workflow | The steps below |
| Knowledge | `references/renewal-measures.md`; `references/starter-rules.md` (SR12 to SR22) |
| Tools | None from the library; writes the definitions file the script reads |
| Prompt | This guide |
| Template | `assets/renewal-definitions-output.md` |
| Input | The request and its context: the measures the team reports today and how, the account file's columns, contract types in use (annual, multi-year, pilot), the value fields available, the owner of the definitions |
| Governance | `references/governance.md`; every definition is the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: say what is not sourced

Open with one line: no primary or peer-reviewed source defines renewal rate, churn, NRR or expansion for digital health, so these are your definitions and will be labeled owner-stated. Then help the person choose. Offer the register starter rules (SR12 to SR22) labeled "register starter rule, yours to adopt". Never describe one choice as "the standard" or "best practice".

## Read the request

- **What they report today.** Their names for the measures and their formulas, if any.
- **The account file's columns.** Which field holds status, renewal date, contract type, value before and after, loss reason, offer and outcome.
- **The owner.** Who answers for the definitions, in the person's words, or "owner not named".
- **Mode.** Short for "how should we define renewal rate"; full for a metrics definition document.

## Workflow

### Step 1. Say what is sourced

One line from `references/renewal-measures.md`: no source defines these measures; the skill computes the person's. Where the person asks "what is NRR", answer that the term has no sourced definition here and show the formula the script uses under that name, as one option.

### Step 2. Walk the choices

Go through the "Choices the person must make" table in `references/renewal-measures.md` in one message, with the register starter rule beside each where one exists. Ask the person to choose; do not choose for them. Where a published counting rule supports a choice, give it as a reason the person may borrow, labeled: "a valid denominator, not volunteers, is how RE-AIM counts reach (CS27); the same logic keeps open accounts in the denominator (SR18)".

### Step 3. Check the card for consistency

Check and say plainly where the card fails:

- Every account in the period lands in exactly one of renewed, lost, open or excluded.
- Open accounts are either in the denominator or explicitly outside it; never silently dropped.
- Exclusions are stated by field and value (for example contract type = pilot), not by account name.
- The value basis is one field, one currency, with before and after values per account.
- Expansion counts only what the definition says (renewed accounts only, or also mid-term additions); the formula matches.
- "Renewed" and "signed" require a document the person names; a verbal intent or a meeting is not counted unless the person says so (SR15, SR22).
- A definition changed from last period is flagged, with both versions written down.

### Step 4. Write the definitions file

Write the JSON file the script reads (keys in `references/tools.md`), mapping the person's column names. Show it to the person for confirmation. This file is the record of the definitions; the A2 output quotes it.

### Step 5. Say what it means for the person

Two lines. Examples: "Your current rate leaves open accounts out of the denominator; with them in, the same file gives a different number. Your call which you report, but say which." "Pilots are excluded by contract type, so a pilot that converted to annual is counted from its annual contract on."

## Build the output

Follow `assets/renewal-definitions-output.md`. Answer first: the definitions as chosen, any consistency failure, and the one line that they are owner-stated. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The output says the definitions are the person's and not a standard.
- Every register starter rule used is labeled adopted, by SR id.
- No benchmark, typical rate or target appears.
- The definitions file matches the card.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Definitions only; the figures are A2 and the offer review is B1.
- Customer health score definitions are the Customer Health skills (`value-realization-monitoring`).
- Accounting treatment of revenue is not in scope; the skill counts contract values as the person supplies them.
