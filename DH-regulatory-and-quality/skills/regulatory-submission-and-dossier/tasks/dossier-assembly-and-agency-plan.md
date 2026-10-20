# B1 Dossier assembly and agency plan

Framework task: DH-03.03.4.1, Part B, task B1. Replaces "Submission Dossier Compilation", "Agency Interaction Management" and "Generate a pathway report".

## What this task delivers

A working plan for getting the dossier out the door: section by section what is ready, in draft or missing, and who owns it, as the person names them; the gaps the content map exposes; the questions worth taking to the agency first; and the agency interaction plan with each channel's sourced clock (Pre-Sub, SIR, minutes, review interactions, notified body steps). It stops for the regulatory owner before anything is sent. It answers "what is left to do, who has it, and how do we work with the agency?"

Why it matters: in FY 2025 a 510(k) took on average 1.69 review cycles and a De Novo 1.68 (S-41, S-45); every Additional Information letter stops FDA's clock and starts the sponsor's (S-25). A plan that names owners and settles open questions early is how a team keeps those cycles down.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.4.1 Part B, Dossier assembly and agency plan |
| Workflow | The steps below |
| Knowledge | A1 content map and A2 clinical evaluation from the conversation; `references/agency-interaction.md`; `references/content-maps.md` |
| Tools | `scripts/dossier_gaps.py` (optional); `regulatory-dh.generate_report` only to describe a predicate or comparable the person named; `verify.build_record` on release |
| Prompt | This guide |
| Template | `assets/dossier-plan-output.md` |
| Input | The request and its context; the person's inventory (section, status, owner, file); their open questions for the agency; the route and class as decided |
| Governance | `references/governance.md`; the plan stops for the regulatory owner |

## Read the request

- **Inventory.** Ask for the list of what exists, in any form (a table, a folder listing, a sentence per section). Statuses and owners are the person's words.
- **Content map.** If A1 has not run for this route, run it in short mode first.
- **Open questions.** Ask what the team is unsure about (predicate choice, testing approach, clinical evidence, PCCP scope). These are the candidates for a Pre-Sub.

## Workflow

### Step 1. Status by section

Lay the inventory against the A1 map. With code execution: write the inventory as CSV (`section_id,status,owner,file,note`) and run `python3 scripts/dossier_gaps.py --route <route> [--software basic|enhanced] [--pccp] --inventory inventory.csv`. Without it, do the same by hand. For every section: the person's status, the person's owner or "owner not named", the file, the source row. A section the person did not mention is `[GAP]` not in the inventory. An item the map does not name goes to the regulatory owner to place.

### Step 2. Owners

List every section with no owner and ask who holds it. Use the owner or role the person names, in their words. Never propose a job title or a name. If the person asks for help assigning, lay out which sections share inputs (for example the risk management file feeds the software documentation and the benefit-risk section, S-03, S-21, RP EU-13) and let them decide.

### Step 3. What blocks what

Order the open sections by dependency the sources state, not by effort: the intended use and indications feed the classification, the predicate comparison and the labeling (S-13, S-14); the risk management file feeds the benefit-risk section; the CER sits inside Annex II 6.1(c) (S-54); a PCCP must be in the original submission (AI US-09). Do not estimate durations or set dates.

### Step 4. Agency interaction plan

From `agency-interaction.md`, pick the channels that fit the person's open questions and list each with its sourced clock:

- **Pre-Sub** for specific questions: feedback within 70 days or 5 days before a meeting; the team drafts minutes within 15 days (RP US-31, RP US-32, S-30). Context: FY 2025 average 61.89 FDA days to written feedback (S-47).
- **Breakthrough request**, if the person believes the criteria fit: decision within 60 days (RP US-40, RP US-42). The model lays out the criteria; the owner decides whether to request.
- **During review**: acceptance or screening (S-15, S-23), first substantive interaction (S-24, S-31), decision goals in FDA days (RP US-46 to RP US-48), escalation points (S-27, S-32), SIR for deficiency letters and its timing (S-33 to S-36), response deadlines where sourced (RP US-13, S-16) and the 510(k) Additional Information deadline as `[GAP]`.
- **EU notified body**: choice and no parallel applications (RP EU-12); the contractor study's timeline context, labeled as such (S-71, RP EU-44, S-74); the main refusal reasons to pre-empt: outside the body's designation scope, incomplete applications (S-72); expert panel for class III and certain IIb (RP EU-19); EUDAMED modules in force (RP EU-36).
- **Fees**: FY 2027 rates (RP US-55), stated as the person's budget fact.

Draft the Pre-Sub questions only as "draft for the regulatory owner", one question per open issue, each tied to the dossier section it unblocks.

### Step 5. Predicates and comparables, only as named

If the person names a predicate or comparable, call `regulatory-dh.generate_report(reference=<K/DEN/P>, template="regulatory")` and describe it only by what its record states: pathway, decision date, product code, the predicates its summary names, source URL. Give the retrieval date only as the record's own field; if the record has none, write 'retrieved through the library on <run date>'. On 19 October 2026 the report for K191716 showed EU status as `false` although the library's EUDAMED copy has no decision dates; say "not found in the library's EUDAMED copy" instead. Never choose a predicate.

### Step 6. Stop for the regulatory owner

Close with the decisions only the owner can take: filing route confirmed, level confirmed, open sections assigned, Pre-Sub questions approved, whether and when to file. Label the plan "draft for the regulatory owner".

## Build the output

Follow `assets/dossier-plan-output.md`. Answer first: how many sections are ready, in draft, missing and unknown, how many have no owner, and the one blocking item. Then the status table, the dependencies, the agency plan and the owner decisions.

## Before you hand it over

- Every status and owner is the person's; unnamed owners say "owner not named".
- Every clock carries its basis (FDA days or calendar days; goal or actual; cohort year).
- No date is promised; no outcome is predicted.
- Pre-Sub questions, SIRs and any text for an agency or notified body are labeled drafts for the regulatory owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model does not file, schedule meetings, or write to an agency.
- No route, class, predicate or documentation-level decision.
- Drugs, biologics and wellness apps are out of scope.
