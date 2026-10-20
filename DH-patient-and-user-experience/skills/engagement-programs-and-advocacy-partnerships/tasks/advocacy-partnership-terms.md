# A2 Advocacy partnership terms

Framework task: DH-02.03.2.1, Part A, task A2. Replaces the earlier "Partner boundary" section (CF-12.02.03.2.1.3).

## What this task delivers

A boundary note and term sheet draft for working with a patient organization or community: what the partner will and will not do (co-author, review or only distribute), how it is paid or supported, who approves patient-facing words, the elements the written agreement must hold under the code that binds the company, the independence and editorial rules, what must be disclosed and when, and the extra rules if the partner's members give input to EMA or an EU joint clinical assessment. It answers "on what terms do we work with this group?"

Why it matters: under the industry codes a written agreement stating amount and purpose is required before financial or significant support (PE-71, PE-80), the company may not shape the group's material in its commercial favor (PE-72, PE-81), and support is disclosed per organization (PE-75, PE-82). A patient funded by a developer's sector may be unable to take part in EU joint clinical work (PE-56).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.03.2.1 Part A, Advocacy partnership terms |
| Workflow | The steps below |
| Knowledge | `references/partnership-terms.md`; rows PE-, CP- as cited there |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/advocacy-partnership-terms-output.md` |
| Input | The request and its context: the partner as the person names it, markets, the codes the company is bound by, the planned role, payment or support, the approver of patient-facing words, whether the partner will handle personal data, whether its members will join regulatory or HTA work |
| Governance | `references/governance.md`; agreement terms and amounts stop for the legal owner; payments that could relate to referrals stop for the compliance owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: three facts stated, never filled

Role, payment and approver of patient-facing words come from the person. If any is missing, write "not stated `[GAP]`" and ask once for all missing ones. The model never proposes an amount, a fee or an approver.

## Read the request

- **Partner.** Name and type as the person describes it. Describe it only by what its own public statements or the person's facts say.
- **Codes.** Is the company bound by the EFPIA Code, the ABPI Code, or neither? If unknown, lay out each as conditional.
- **Markets.** The rule set differs (section 1 of the reference).
- **Data.** Will the partner receive or process personal health data?
- **Regulatory or HTA input.** Will the partner's members give input to EMA, an EU joint clinical assessment or NICE?
- **Mode.** Short for a direct question; full for a term sheet.

## Workflow

### Step 1. Write the boundary note

Three lines: role, payment, approver. Add what the partner will not do, from the person (for example "will not distribute product material"). Where the person wants co-authorship, note that editorial control stays with the partner under PE-72 and PE-81 [INDUSTRY].

### Step 2. Pick the rule set

From section 1 of `references/partnership-terms.md`, list the rule sets that apply to the person's facts, each labeled [INDUSTRY] or law. Where the person is US-only, say that no US code read has a patient-organization chapter (PE-83, PE-84) `[GAP]` and that the Anti-Kickback Statute applies to any payment that could induce referrals or purchases (CP-US-01, CP-US-08).

### Step 3. Lay out the agreement elements

Use the table in section 3. For each element, write the person's term or "not stated". Where only one code names an element, say which. Do not fill EFPIA elements beyond the quoted text.

### Step 4. Independence, logo and material

List the rules from section 4 that the person's plan touches: sole funding (PE-73), logo use (PE-74), editorial influence (PE-72, PE-81), and, for an independent charity, donor influence and fund breadth (PE-85 to PE-88). Flag plan items that conflict, citing the row, for the owner.

### Step 5. Disclosure

From section 5, write what is disclosed, by whom, and when, under the code that applies. Where the timing is not in the quoted text, write `[GAP]`.

### Step 6. Regulatory and HTA input, and data

If the partner's members will give input to EMA or EU HTA, list the declaration, eligibility and conflict rules (PE-45, PE-49 to PE-51, PE-56, PE-57). If the partner handles personal health data, list the business associate or Article 28 elements that would apply (CP-US-44 to CP-US-49, CP-EU-01 to CP-EU-07); which applies is the privacy owner's call.

### Step 7. Stops

Name the owner for: the agreement and amount (legal owner), any payment that could relate to referrals (compliance owner), any support to patients through the partner (compliance owner, B1), patient-facing wording (review owner). Use the owners the person named, or "owner not named".

## Build the output

Follow `assets/advocacy-partnership-terms-output.md`. Answer first: the boundary note, the missing terms, and the rule set that applies. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Role, payment, approver and amounts are the person's, or `[GAP]`.
- Every code rule is labeled [INDUSTRY]; no code is presented as law.
- The partner is described only by its own statements or the person's facts.
- No statement that the partnership is compliant or that the agreement is final.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Terms with patient organizations and communities. Deal structuring with commercial partners is Commercial 4.x; payer contracts are Market Access.
- Support to patients through the partner is judged in B1.
- Measuring the partnership's results is DH-02.03.2.2.
