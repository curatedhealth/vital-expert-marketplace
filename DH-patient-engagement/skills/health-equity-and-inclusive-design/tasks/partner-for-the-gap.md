# A2 Partner for the gap

Framework task: DH-02.03.4.1, Part A, task A2. Replaces the earlier "Partner for the gap" section (CF-12.02.03.4.1.3).

## What this task delivers

For each group marked `[GAP]` in A1: the kind of holder who could see it (the deploying provider, a patient organization, a community group, a public data owner), the partner the person names, the exact question to ask them, the aggregate data to request, and the rules that govern the relationship. It answers "who could see the group we cannot, and what do we ask them?"

Why it matters: a group the data cannot see cannot be shown to be reached, and a rate guessed for it is worse than a gap. The register's method is to name the group, name who could see it, and state the question, never to invent a rate (old task "Partner for the gap").

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.03.4.1 Part A, Partner for the gap |
| Workflow | The steps below |
| Knowledge | `references/inclusive-change-and-partners.md`; `references/equity-frames.md`; PE rows |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/partner-for-the-gap-output.md` |
| Input | The request and its context: A1's `[GAP]` groups (or the person's own list), the partners the person already works with or is considering, market, whether the company is an EFPIA or ABPI member |
| Governance | `references/governance.md`; partner choice is the person's; payments and free items stop for the compliance owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: aggregate questions, the person's partner, no invented rate

The model names kinds of holder and drafts the question; the person names the organization. Requests are for aggregate counts or described barriers, never patient-level records. A partner is described only by what its own record or public source states.

## Read the request

- **The unseen groups.** From A1 or the person. If none were marked, run A1 Step 5 first in short mode.
- **Candidate partners.** Organizations the person names. Do not supply organization names from memory.
- **Relationship.** Unpaid conversation, data-sharing agreement, contracted service, grant or sponsorship. Anything paid stops for the compliance owner.
- **Company status.** EFPIA or ABPI member, or neither (decides whether the [INDUSTRY] code rows are relevant).

## Workflow

### Step 1. One line per unseen group

For each `[GAP]` group: what is not recorded, at which step, and the record that would show it (from A1).

### Step 2. Kind of holder

Match each group to the holder types in `references/inclusive-change-and-partners.md`: the deploying provider's own records, a patient organization, a community or public involvement group, a public data owner (SVI, IMD). Say what each could plausibly see in their own terms, not what they hold, which only they can confirm. Go through all four holder types for each group and say in one line which do not fit. For area-level context (deprivation, housing type and transportation), name the public data owner (SVI, PE-120 to PE-123) and say it describes areas, not people.

### Step 3. The partner the person names

Record the organization and contact role the person names. If they named none: "partner not named", and ask. Where the person names a patient organization and EMA work is in view, list the EMA criteria rows as checks the person can make (PE-44, PE-50, PE-51); do not judge eligibility.

### Step 4. The question and the data request

Draft, for each partner, one question and one data request:

- Question: what the partner sees about the group at that step ("Which barriers do your members report at enrollment when help is offered only in English?").
- Data request: aggregate counts by the person's subgroup definitions, the period, and the person's small-cell rule. Never names, records or identifiers.

### Step 5. Relationship rules

List the rules that apply to the relationship type, with rows: independence, written agreement, no editorial influence, no sole funding, logo permission, disclosure (PE-70 to PE-75, PE-80 to PE-82; [INDUSTRY], not law). For UK public involvement work, the UK Standards (PE-65 to PE-68; a framework). If money, a free item or a service changes hands, write the stop: "Stops for your compliance or legal owner." Never say an arrangement is permitted.

## Build the output

Follow `assets/partner-for-the-gap-output.md`. Answer first: each unseen group with its partner (or "partner not named") and the one question. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every partner is named by the person, or "partner not named".
- Every data request is aggregate, with the small-cell rule stated or asked for.
- [INDUSTRY] rows are labeled as codes, not law.
- Any payment or free item is a stop, not advice.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Does not choose partners, negotiate agreements or judge a partner's independence or eligibility.
- Patient engagement programs and advocacy partnerships as a whole are DH-02.03.2.x; this task covers only the partner for an unseen group.
- Reimbursed services and payer data are dh-market-access.
