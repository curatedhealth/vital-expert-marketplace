# A1 Program purpose and activities

Framework task: DH-02.03.2.1, Part A, task A1. Replaces the earlier "Programme purpose" (CF-12.02.03.2.1.1) and "Programme activity" (CF-12.02.03.2.1.2) sections, and takes the unbound "Insight Capture" and "Synthesis" entries as inputs (the insights the person brings).

## What this task delivers

A program charter draft: the audience and the one action the program asks of them, the action it will not ask for, the partner's role if one is involved, each activity tied to that purpose (or dropped), the content each activity is allowed to use and who approved it, the wording in draft material that needs the owner's review with the rule behind each flag, and the data rule that applies to what the program collects. It answers "what is this program for, and what may it say and do?"

Why it matters: program text that describes what a product does for a condition helps set its intended use (PC-US-17, PC-EU-03), and patient-facing material is judged from the vulnerable reader's view in the EU (PC-EU-06). A purpose that drifts into recruitment or promotion turns an education program into something else (CP-US-28, PE-70).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.03.2.1 Part A, Program purpose and activities |
| Workflow | The steps below |
| Knowledge | `references/program-material-rules.md`; rows PE-, PC-, CP- as cited there |
| Tools | `commercial-dh.audit_claims` (optional, counted); `verify.qualify_source` and `verify.check_claim` for any published figure in the material (counted) |
| Prompt | This guide |
| Template | `assets/program-purpose-and-activities-output.md` |
| Input | The request and its context: product and its authorization status as the person states it (identifier if any), markets, audience, the action wanted, partner if any, planned activities, draft material, the allowed claims list and who approved it, insights the person brings |
| Governance | `references/governance.md`; patient-facing wording stops for the review owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Product and status.** Name, identifier (510(k), De Novo, CE certificate, DiGA listing) and intended use as the person states them. Unknown status is `[GAP]`; the model does not decide device status. If the person gives an identifier and a record for it is in this conversation or in `examples/live/` (for K191716: Somryst, Pear Therapeutics, 510(k) 23 March 2020, `examples/live/audit_claims_K191716.json`), state the product and holder on record and ask the person to confirm they hold it. Until they confirm, material that cites the identifier as theirs is flagged for the owner (false approval claims, PC-US-01 for US material, PC-EU-11 for EU, PC-UK-08 for UK). The holder on record can be out of date after a transfer or acquisition: ask who holds it now, and do not treat the record as proof either way.
- **Audience and action.** Who, and the one action wanted. If the person gives several, ask which is the purpose.
- **Partner.** Name and role, if any. Terms are A2.
- **Activities and material.** The list, with cadence the person sets, and any draft text.
- **Allowed claims.** The list and its approver, in the person's words. Without one, every claim in the material is "not on an approved list".
- **Mode.** Short for a direct question; full for a charter.

## Workflow

### Step 1. Write the purpose

One sentence each: audience; the action asked; the partner and its role (if any); the action not asked. Take all four from the person. If they have no "action not asked", offer the candidates in section 2 of `references/program-material-rules.md`, each labeled "proposed" with its row (CP-US-28; PE-70 [INDUSTRY]). Apply the kept rule: do not make advocacy recruitment the purpose of an education program.

### Step 2. Map the purpose to an input route (when it is patient input)

If the purpose is to bring patient input to FDA, EMA, NICE, an EU joint clinical assessment or research, name the route and its sourced rules from section 1 of the reference (for example: PPI is voluntary and most useful when decisions are preference sensitive, PE-24, PE-25; EU HTA patients act in an individual capacity and declare interests, PE-56, PE-57). Say what the route needs from the program, such as representativeness (PE-06) or declarations (PE-45).

### Step 3. Tie each activity to the purpose

One row per activity: activity, audience, cadence (the person's), how it serves the purpose, the content it may use (from the allowed list), the approver. An activity that does not serve the purpose is listed as "drop, per the purpose" for the person to confirm. An activity that hands out anything of value to patients is marked "support: B1" and goes no further here.

### Step 4. Flag material for the owner

Read each sentence of the draft material against section 3 of the reference for the person's markets. For each flagged sentence give: the sentence, the rule and row, and why it is flagged ("names a disease for a wellness app, PC-US-63"). Where the person asks, add safer wording labeled "draft for the owner". Never mark a sentence cleared. Testimonials repeated in material are flagged as manufacturer claims in the UK (PC-UK-03) and in German public device advertising (PC-DE-11).

### Step 5. Library label check (optional)

If the person wants a second view, call `commercial-dh.audit_claims` with `reference` set to the exact identifier (not the product name) and the claims as `claims`. Read `references/tools.md` first. If `intended_purpose_from_record` is `[GAP]`, say the labels are not readable and do not report them as findings. If the person cites a published figure in the material, run `verify.qualify_source {doi, question}`, read the paper's passage yourself, then `verify.check_claim` with the claim, the passage you read and the `qualify_source` result as `source`. Accept only when the passage states the claim in the same direction (register N3).

### Step 6. Name the data rule

From section 4 of the reference, state which rule applies to the data the program collects, conditional on the person's status ("if you are a HIPAA covered entity ...; if you are outside HIPAA ..."). The status is the privacy owner's call.

## Build the output

Follow `assets/program-purpose-and-activities-output.md`. Answer first: the purpose in one line, activities kept or dropped, and the number of sentences flagged for the owner. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Purpose, audience, action, partner role and cadence are the person's; proposals are labeled "proposed".
- Every flag carries its row; [INDUSTRY] and [WF] rows are labeled.
- No sentence is called cleared, compliant or approved.
- Support to patients is routed to B1, not judged here.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Program design only. Partnership terms are A2; support and launch are B1; results are the monitoring skill (DH-02.03.2.2).
- Claims clearance is the person's owner's; value messages are Commercial 3.x.
- Accessibility conformance is UX 1.x; who the program reaches is Patient Engagement 4.x.
