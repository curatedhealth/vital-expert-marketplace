# A1 Research question and plan

Framework task: DH-02.03.1.1, Part A, task A1. Replaces the register task "Research question" (CF-12.02.03.1.1.1).

## What this task delivers

A one-page co-design plan: the decision the research serves, the question, who takes part and why, what the sessions will not decide, how participants are recruited and what that means for how far the results reach, the ethics, consent, conflict and payment questions laid out with their rows for the person's owners, and, if useful, published co-design studies for the same condition as comparables. It answers "what will patients help us answer, with whom, and what has to be settled before we recruit?"

Why it matters: recruiting before the question is written produces sessions that answer nothing in particular (R-4). Co-design samples are almost always non-probability samples, which FDA says may not represent the target population (PE-06). A paid panel member may later be unable to serve as an independent patient expert in EU joint clinical assessment work (PE-56).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.03.1.1 Part A, Research question and plan |
| Workflow | The steps below |
| Knowledge | `references/co-design-method.md` (sections 1 to 6); `references/research-ethics.md`; rows PE-04 to PE-27, PE-52 to PE-68, UX-M-11 to UX-M-19, UX-UK-19, CP-US-34 to CP-US-38 |
| Tools | `literature.list_sources` (free), `literature.search_literature` (counted, optional), `literature.get_record` (counted, optional) |
| Prompt | This guide |
| Template | `assets/research-plan-output.md` |
| Input | The request and its context: product and users, the decision at stake, who the person wants to hear from, markets, funding source, whether children take part, whether sessions are recorded, any payment planned |
| Governance | `references/governance.md`; ethics determinations, consent wording and payments stop for their owners |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **The decision.** What will change depending on what participants say? If the person cannot name one, ask; the question cannot be written without it (R-1).
- **Who.** Patients, carers or both, and why (R-2). Ask whether staff or clinicians will be in the room; their words are kept apart (R-5).
- **Non-goal.** What the sessions will not decide (R-3). Offer one example drawn from the person's own context, labeled "proposed".
- **Ethics facts.** Who funds the work (federal funding brings the Common Rule into play, UX-M-11), whether results are meant to generalize (UX-M-12), whether children take part (UX-M-18), whether sessions are recorded, whether anything of value goes to participants.
- **Regulatory use.** Will the output feed a submission, a preference study or an HTA dossier? If yes, flag the regulatory owner now (PE-22 to PE-27, PE-53).
- **Mode.** Short for a direct question; full for a plan to circulate.

## Workflow

### Step 1. Write the question

Write three lines: the decision served, the question, the non-goal (R-1 to R-3). The question names the people and the moment in the journey, not the feature the team prefers. If the question is about what matters in daily life, use FDA's meaningful-aspect-of-health frame and say it comes from drug and biologic guidance also issued by CDRH (PE-14, PE-10).

### Step 2. Participants and recruitment

List the participant types and why each is in. State plainly that recruitment through clinics, panels or advocacy groups is non-probability sampling and that the plan will say so when results are read (PE-06). Do not promise a number "for saturation": FDA says there are no set criteria (PE-09). No source here sets a co-design sample size `[GAP]`. If the person wants a range of people, cite the UK Standard on inclusive opportunities as a framework (PE-66). If carers take part, keep their words as carer words (PE-13). Name which groups the plan may miss in one line and point to the health equity skill for reach.

### Step 3. Comparable published co-design work (optional)

Call `literature.list_sources` (free) once. Then `literature.search_literature` with `{query: "co-design <condition> <product type> patients", limit: 5, filters: {date_from: "<year the person chooses>-01-01"}}`. Read `references/tools.md` first: the search is lexical and design labels are unreliable for qualitative work. Keep only records whose title says co-design, co-production, participatory or experience-based co-design. Report each by title, venue, year and DOI, with the design as the title states it. Never state a finding from a title. If a method point matters (for example how a study involved carers), the person reads the paper; a finding is used only after `verify.qualify_source` and `verify.check_claim` with a passage read in the same direction (register N3).

### Step 4. Ethics, consent, conflicts and payments

Lay out, from `references/research-ethics.md`, which row each feature of the plan touches:

- Common Rule applicability and whether the work is research (UX-M-11, UX-M-12); exemptions (d)(2) and (d)(3) and their limits (UX-M-14 to UX-M-17); children (UX-M-18).
- MHRA's stated expectation of informed consent where practicable, even in formative work (UX-UK-19, advisory).
- Conflicts: EU joint clinical assessment patient experts must declare interests and have none that affect impartiality (PE-56, PE-57).
- Payments or items of value: CP-US-34 to CP-US-38, laid out for the compliance owner.

State the consequence in one or two lines ("If this is federally funded and meant to generalize, the Common Rule applies and an exemption question goes to your IRB"). Never write "exempt", "no IRB needed" or "payment is fine". Consent elements, GDPR for recordings and UK approval routes are `[GAP]`.

### Step 5. Reporting plan

Name the reporting checklist: GRIPP2-SF (five items: aims, methods, results, outcomes, critical perspective) where involvement is secondary (PE-91), GRIPP2-LF (34 items) where it is the main focus (PE-90); both [PAPER] doi:10.1136/bmj.j3453 (PE-89). Plan the capture columns (`references/insight-log.md`) before the first session so A2 can count.

### Step 6. Stops and owners

List what goes to whom: ethics determination, consent wording, payments, regulatory use. Owners as the person named them, or "owner not named".

## Build the output

Follow `assets/research-plan-output.md`. Answer first: the question, the decision, the participants and the non-goal. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The decision is the person's and named; the question, participants and non-goal are written.
- Recruitment is described as what it is, with PE-06.
- No ethics, exemption, consent or payment conclusion is stated; each is a stop with its owner.
- Comparables are described by their records only.
- No participant name or identifier anywhere.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Planning co-design only. Usability tests, think-aloud protocols and human factors studies belong to the User Experience pack (`patient-and-clinician-user-research`).
- Advocacy organization partnerships and their funding go to `engagement-programs-and-advocacy-partnerships`; who is reached or left out goes to `health-equity-and-inclusive-design`; accessibility conformance goes to the User Experience pack.
- Clinical outcome assessment development and endpoints go to the person's evidence owner and the Clinical Validation pack.
- No prices, claims or payer wording: Commercial and Market Access packs.
