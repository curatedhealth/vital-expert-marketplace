# B1 Joint decision record

Framework task: DH-01.01.3.1, Part B, task B1. Replaces the earlier "Joint decision" section (DH-01.01.3.1.3).

## What this task delivers

A record of a decision that needed more than one function to agree: the decision in the person's words, the functions that had to agree, each function's agreement or disagreement as the person reports it, the evidence the decision rested on, who carries the result out, what it unblocks, and when it is looked at again. A meeting with no decision is recorded as that, not as a joint decision.

Why it matters: a decision remembered differently by each function is reopened at the next review. A written record with the dissent kept is the cheapest way to stop that.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.01.3.1 Part B, Joint decision record |
| Workflow | The steps below |
| Knowledge | `references/handoff-rules.md`; rows PL1, PL4, PL6 (design review functions and checks), PL2, PL66, PL67 (independent review), PL41 (Pre-Sub minutes pattern), PL120 (IDEAL-D consensus pattern), TM112, TM113 (evidence-to-decision conclusions pattern), TM117 (core components and adaptable aspects) |
| Tools | Optional: `verify.qualify_source` then `verify.check_claim` when the record cites a methods passage; `verify.build_record` once the person names who clears it |
| Prompt | This guide |
| Template | `assets/joint-decision-record-output.md` |
| Input | The request and its context: notes or the person's account of the discussion, the functions and people involved, the evidence used, A1 and A2 outputs |
| Governance | `references/governance.md`; the decision, agreement and disagreement are the person's report, never the model's judgment |
| Catalogue job | none |

## The rule that shapes this task: people decide

The model records; it never decides, breaks a tie, or reports a function as agreeing when the person has not said it did. If the person asks the model which option is right, it lays out the facts and the rows behind each option and labels any suggestion "proposed".

## Workflow

### Step 1. Is there a decision?

Ask what was decided, in the person's words. If nothing was decided, record "no decision" with the open question and who will bring it back; stop there. A meeting held is not a decision made.

### Step 2. Which functions had to agree, and why

List the functions the person names. Where the decision was taken at a design review, note the sourced rule on who attends (PL1) and what a review checks (PL4), and set the person's attendee list beside it. If the person used an independent reviewer, record who and why; if not, record that independence was a choice (PL2) and, for SaMD in serious or critical situations, that IMDRF N41 gives it more weight (PL66, PL67).

### Step 3. Agreement and disagreement

One line per function: agreed, disagreed, or not recorded, in the person's words. Keep disagreement verbatim and attributed to the function, as the person reports it. For an FDA Pre-Sub, the sourced rule is that minutes record agreements and action items and do not assign statements to individuals (PL41); offer that pattern for the internal record only as a labeled option.

### Step 4. What the decision rested on

List the evidence the person says was used: documents, data, rows. If the record cites a published method (for example the IDEAL-D consensus fallback, PL120), check it: `verify.qualify_source {pmcid or doi, question}`, then `verify.check_claim {claim, passage {text, locator}, source: full qualify_source object}`. Accept only a passage you read that says the same thing in the same direction (N3); take the citation from `qualify_source` (C18). Mark the person's assumptions as theirs (TM113 separates research evidence from additional considerations).

### Step 5. Structure the record

Use the evidence-to-decision conclusions as a pattern and say so in one line of the answer (TM112, [PAPER] DOI 10.1186/s12961-018-0320-2; a pattern, not an obligation): summary of what was weighed, options considered, the decision, the justification, conditions or restrictions, implementation (who carries it out, what it unblocks), and monitoring (what is looked at again, when, by whom). For a decision about what a site may change, record core components and adaptable aspects in the person's words (TM117). All content is the person's; empty slots stay `[GAP]`.

### Step 6. Carrier and what it unblocks

Name the person who carries the result out, as the person names them; if none, write "owner not named" and ask. Link the decision to the A2 items it unblocks or creates. If the decision changes what another function delivers (for example dosing instructions, labeling or a clinical claim), ask who carries that follow-up and write "owner not named" until the person says. Route any change record to `dh-regulatory-and-quality` document-and-change-control.

### Step 7. Clear it

Ask who clears the record. Once the person names them, call `verify.build_record` with `cleared_by` set to that name. Until then the record is an uncleared draft.

## Build the output

Follow `assets/joint-decision-record-output.md`. Answer first: the decision, the functions and their positions, the carrier, what it unblocks. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The decision and each function's position are the person's words; nothing is attributed that the person did not report.
- Dissent is kept, not smoothed.
- Patterns borrowed from PL41, PL120 or TM112 are labeled as patterns, not obligations.
- No gate is called passed; no record is called compliant.
- Each [PAPER] paper cited has its DOI once in prose, and beside its own row id in every table cell (rows from several papers each keep their own DOI).
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Design review records as quality records, and change control: `dh-regulatory-and-quality` design-controls-and-risk-management and document-and-change-control.
- Portfolio-level prioritization and decision rights across products: `dh-cross-functional-leadership` (old pack, heading DH-01.03.3 Governance & Portfolio).
- Decisions about device status: `dh-regulatory-and-quality` regulatory-pathway-and-classification; submissions: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- Choosing a mechanism or permissible variation: therapeutic-mechanism-and-intervention-design (DH-01.01.2.1); this task records such a decision once made.
