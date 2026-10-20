# Task TR-6.1.1 Input confidentiality

## Formula

| Slot | For this task |
|---|---|
| Worker | Responsible AI lead who also knows the business |
| Workflow | Recognize the kind of material, ask the policy question, offer a safer route, keep sensitive details out of the output |
| Skill | TR-6.1.1 |
| Knowledge | `references/rules.md` (I1–I8, I11), `references/patterns.md` (C1–C9) |
| Tool | `scripts/scan_inputs.py` where code can run. Companion slot: future AI-policy companion (none yet) |
| Prompt | This guide |
| Template | `assets/input-note.md`, `assets/check-line.md` |
| Input | The request, the material or its description, the tool named, where the result will go, any policy the person quotes |
| Governance | TR-H3, TR-H4, TR-H5, TR-H7, TR-H11, `references/governance.md` |

## What to recognize

Name the kind of material in plain words. The person usually knows what it is; the
point is to say it out loud before it goes in.

| Kind | Typical signs | Why it matters |
|---|---|---|
| Unpublished study data | Clinical study report, topline results, interim analysis, statistical output, "draft", "confidential", a study code with no publication | Usually confidential under the company's own rules and the study's contracts; may carry patient-level listings and narratives; may be price-sensitive before disclosure |
| Patient or personal details | Names, initials with dates, ages, hospital or record numbers, contact details, a patient's story in a payer's or doctor's words, photos | Health data is a special category in the EU and sensitive personal data in Switzerland (I1, I3, I4); HIPAA de-identification rules apply in the US where the company is covered (I6) |
| Pricing and contracts | Net prices, rebates, tender bids, contract terms, discount grids | Commercially sensitive; often confidential under the contract itself |
| Strategy and forecasts | Brand plans, launch sequencing, forecasts, business development targets, board papers | Commercially sensitive; some may be price-sensitive for a listed company |
| Client or partner confidential material | Partner data under a confidentiality agreement, a client's documents (agencies, consultancies, CROs), co-promotion plans | The owner's terms decide what may be done with it, not ours |
| Could be price-sensitive | Undisclosed trial results, regulatory outcomes, deal talks, guidance changes, for a listed company | Insider information rules apply in the EU (I8) and elsewhere [CHECK]; whether it is inside information is for legal or compliance |

## Guard (before material goes in)

1. **Set the depth.** Public material or the person's own non-sensitive work: say
   nothing and do the work. Otherwise continue.
2. **Say what it looks like.** One line, in plain words: "This is an unpublished study
   report; it may include patient-level listings."
3. **Ask the policy question.** "Does your company's AI use policy allow this tool for
   unpublished study data?" Name who answers it in plain words: the policy itself, its
   owner, or the privacy, legal or compliance function. Do not answer it yourself, in
   either direction, and do not describe what the tool does with data.
4. **Offer safer routes**, the ones that fit:
   - **A company-approved tool** for this kind of material, if the policy names one.
   - **The minimum extract.** What does the job actually need? A market access summary
     of a study report may need the synopsis and two tables, not 200 pages.
   - **Identifiers removed.** Take out names, initials, dates linked to a person, ages
     over 89, record and subject numbers, contact details, locations smaller than a
     region, photos. Say this reduces what is shared; it does not make the material
     anonymous (I2, I6).
   - **The public version.** Registry results, a published paper, a press release, a
     public label, a published assessment.
5. **Ask what the result is for**, if it changes the route (internal summary, payer
   deck, publication).
6. **Proceed on the route the person chooses.** If they confirm the policy allows it,
   proceed and do not repeat the warning. If they choose an extract, work from it and
   scan it first where code can run (`scripts/scan_inputs.py`).

## Repair (material already in the conversation)

1. **Do not alarm and do not lecture.** One plain line: what the material appears to
   contain.
2. **Do not quote sensitive details back.** No names, identifiers or patient stories in
   the reply or the output.
3. **Do the work without them where you can.** A meeting summary can say "the payer
   described a patient case" without the case details. Patient details in the output are
   also covered by `market-rules-and-data`; if that skill is not active, still keep them
   out (`trusted-capability-map` governance stop rule).
4. **Point to the process.** "If your policy does not cover this tool for patient
   details, your privacy or data protection function will say what, if anything, needs
   to happen next." Never judge whether an incident occurred or must be reported, and do
   not claim the material can be deleted from the tool.
5. **If the material includes a possible side effect**, note it for the safety route
   (`patient-safety`). Do not judge it.

## Check line

See `assets/check-line.md`.

## Boundaries

- Patient or personal data in the finished output is `market-rules-and-data`. This task
  covers what goes in, and keeps what came in from travelling further.
- Whether the tool is approved, the data anonymous, the information inside information,
  or a transfer abroad permitted: the company's policy and its owners decide.
- How much human review and disclosure the result needs: `responsible-use`.
