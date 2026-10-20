# B1 Mechanism miss review

Framework task: DH-01.01.2.2, Part B, task B1. Replaces the earlier "Mechanism miss" section (DH-01.01.2.2.3, register CF-12.01.01.2.2.3). Also carries the folded DH-01.06 miss-owner sections: "engagement retention miss owner" (DH-01.06.3.2.3, CF-12.01.06.3.2.3) and "therapeutic safety miss owner" (DH-01.06.2.2.3, CF-12.01.06.2.2.3), whose rule stays: "Do not close a failed element because the existing assessment skill already described it."

## What this task delivers

For each missed link from A2, each use measure outside the person's threshold from A3, and each signal that crossed the person's threshold in A4: what kind of miss it is (delivery, use, change, outcome, population), the owner the person names, the response options the sources name (fix delivery, refine the component, repeat a phase, narrow the claim, return to design), the person's choice between a component change and a narrowed claim, and the version that will carry it, or the date the person names to look again, or that the person stops the unit (old miss-owner step 3). It answers "which link broke, who owns it, and what changes in which version?"

Why it matters: a claim kept for a link that missed is a claim the product's own data do not support (old task rule), and the DiGAV asks that the claimed effect stay consistent with the product's functions and content (TM148).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.2 Part B, Mechanism miss review |
| Workflow | The steps below |
| Knowledge | A2, A3 and A4 outputs; `references/miss-rules.md` (section 4 for engagement and signal misses); `references/signal-read-rules.md`; `references/precedents.md`; rows TM3, TM9, TM13, TM19, TM20, TM31, TM62, TM73, TM84, TM86 to TM88, TM92, TM93, TM96, TM138, TM144, TM148; CS9, CS32, CS48 |
| Tools | `regulatory-dh.get_authorization` for a precedent's record; `analytics.rice` or `analytics.mcda` only to order responses the person scored |
| Prompt | This guide |
| Template | `assets/mechanism-miss-review-output.md` |
| Input | The request and its context; A2, A3 and A4 results; the claims the product makes, verbatim; named owners; the version scheme |
| Governance | `references/governance.md`; owners, responses, claims and versions are the person's |
| Catalogue job | none |

## The rule that shapes this task: people decide

The person names the owner of each miss, chooses between changing a component and narrowing the claim, and names the version. The model reads the miss, lays out the responses the sources name with the facts behind each, and drafts the facts the owner needs. It never assigns an owner, never chooses the response, and never rewrites a claim for external use.

## Workflow

### Step 1. Gather the misses

Use A2, A3 and A4 from the conversation, whichever the request concerns. If the one needed does not exist, run it first in short mode. Misses stated by the person without data are listed as "stated, not checked". A3 misses are use-link misses; A4 crossed signals are safety or efficacy signals and are read with miss-rules section 4.

### Step 2. Read each miss in order

Classify each miss by link (miss-rules section 1), or as a safety or efficacy signal (miss-rules section 4). A delivery or use miss comes first: downstream misses in the same cohort are listed as uninterpretable until delivery is addressed (CS32, TM92). Where delivery was adapted, compare it with the intervention theory to separate fit-to-context adaptation from changes that undermine fidelity (TM93).

### Step 3. Name the owner category and the owner

Label the category (component design, evidence or measure, population or claim; old task categories; for A4 signals add safety signal or efficacy signal). Ask the person who owns each, in their words. If none, write "owner not named" and ask. For a crossed safety signal, the reportability call belongs to the owner the person names for vigilance reporting, or owner not named; route it to `dh-regulatory-and-quality` audit-capa-and-complaints before any other response, and never decide it here.

### Step 4. Lay out the responses

For each miss, list the responses the sources name (miss-rules section 2) with the facts behind each, and none chosen:
- Delivery: fix delivery (CS48, CS9), not the product.
- Change or outcome: refine within agreed boundaries (TM13), repeat a phase (TM3), or return to design or abandon (TM62, TM73).
- Population: narrow the claim for that group. Precedent: reSET's primary opioid users became a labeled limitation (TM138).
- Engagement (A3): the mechanic is revisited in therapeutic mechanism and intervention design A3; the definitions or the threshold are revisited only by the person and only before the next read (SE87, Michie 2017, DOI 10.2196/jmir.7126; TM57, ORBIT, DOI 10.1037/hea0000161); low use is not read as a failed outcome (SE26).
- Safety signal (A4): reportability with `dh-regulatory-and-quality` audit-capa-and-complaints; the risk file with `dh-regulatory-and-quality` design-controls-and-risk-management; a mitigation in the design (therapeutic mechanism and intervention design A4); a labeling element with `dh-regulatory-and-quality` regulatory-submission-and-dossier (SE52, SE53).
- Efficacy signal (A4): read beside the claims as in step 5; the labeling-claims part of the malfunction definition is laid out (SE40), and the call is the owner's.
If the person wants the responses ordered, ask for their scores and call `analytics.rice` or `analytics.mcda` on those only, showing the inputs (N5, C17).

### Step 5. Component change or narrowed claim

Ask the person which, per miss (old task step 2). Put each claimed effect, verbatim, beside the link check result. Old task rule: do not keep a claim for a link that missed. Draft the facts for the claim owner (what was measured, in which cohort and version, what missed), labeled "draft for the owner"; the wording itself stops for `dh-regulatory-and-quality` regulatory-submission-and-dossier and the owner the person names. Note DiGAV § 9(2) consistency if Germany is in scope (TM148), as context.

### Step 6. The version that carries it, or the date to look again

Ask the person for the version identifier that will carry each change (old task step 3), or, for an A3 or A4 element, the date they name to look again or that they stop the unit (old miss-owner step 3). Never supply the date. Do not close a failed element because an earlier read already described it (old miss-owner rule). State that the change is recorded under `dh-regulatory-and-quality` document-and-change-control, that a component change goes back to therapeutic mechanism and intervention design A2, and that A2 here is re-run on that version with the same plan unless the person revises it before the data are read (TM57, TM31).

## Build the output

Follow `assets/mechanism-miss-review-output.md`. Short mode for a direct question: each miss with its category, owner, the person's choice (or the options), the version, and the one decision the person needs to make. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every owner, response and version is the person's, or open.
- No claim is kept beside a missed link without saying so; no claim is rewritten for external use.
- Delivery misses are read before mechanism misses.
- Precedents are described only by their records.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Claim wording, labeling and indications: `dh-regulatory-and-quality` regulatory-submission-and-dossier; marketing claims: `dh-go-to-market` pricing-and-value-message-monitoring.
- Change records and risk file updates: `dh-regulatory-and-quality` document-and-change-control and design-controls-and-risk-management.
- Redesigning the component: therapeutic mechanism and intervention design (DH-01.01.2.1) A2; engagement mechanics A3; safety by design A4.
- Reportability, reporting clocks, complaint handling and CAPA: `dh-regulatory-and-quality` audit-capa-and-complaints.
