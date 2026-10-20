# A2 Partner terms and compliance check

Framework task: DH-02.01.4.1, Part A, task A2. Replaces the register task "Partner terms to confirm" (CF-12.02.01.4.1.2).

## What this task delivers

A term list for one partner (or a partner type): each term that must be true before the partner starts, its required elements with rows, its status as the person states it (agreed, in draft, absent), the partners on hold under the person's hold rule, and every fraud-and-abuse stop with the safe-harbor or exception elements laid out for the compliance or legal owner. It answers "what has to be in place before this partner starts, and what goes to legal?"

Why it matters: a BAA missing a required clause, a processor without sub-processor authorization, or a per-referral fee can each undo a channel after launch. A per-referral fee is a felony exposure regardless of intent to break the law (CP-US-01, CP-US-03).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.01.4.1 Part A, Partner terms and compliance check |
| Workflow | The steps below |
| Knowledge | `references/partner-terms.md`; `references/fraud-and-abuse-stops.md`; A1 role cards and handoffs if present |
| Tools | `diligence-dh.get_funding_signals` (optional, to see whether a party files with the SEC) |
| Prompt | This guide |
| Template | `assets/partner-terms-output.md` |
| Input | The request and its context: partner, role, markets, data the partner touches, compensation model, draft agreement or term sheet if any, the person's hold rule, owners |
| Governance | `references/governance.md`; legal and compliance owners decide |
| Catalogue job | none. The term list runs on the sourced references and the person's terms; `diligence-dh.get_funding_signals` stays a direct call. |

## Read the request

- **Partner and role.** From A1 or the person.
- **Data.** Does the partner touch PHI (US) or personal data (EU)? For whom (you, a covered entity, a controller)?
- **Compensation.** Fixed fee, margin on resale, per referral, per patient, outcomes-based, free items or technology. Ask if not stated; it decides the stops.
- **Pharma partner.** If a drug maker pays, funds, co-promotes or pilots, ask who pays whom, on what basis (fixed fee, per patient, per outcome), and whether anything reaches patients free. These answers decide the T-P lines.
- **Draft terms.** If the person shares a draft, read it and report which required elements it states. Do not interpret ambiguous clauses; mark them "unclear, for the owner".
- **Mode.** Short for one question ("can we pay per referral"); full for a pre-signature checklist.

## Workflow

### Step 1. Pick the term families that apply

From `references/partner-terms.md`: data (T-D) if the partner touches health data; claim use (T-C) always; buyer contact and handoff (T-B) always; compensation (T-M) always; disclosure (T-S) if a party is an SEC reporting company; launch prerequisites (T-L) if the partner imports, distributes or deploys; pharma partner pilot (T-P) if a drug maker pays, funds, co-promotes or pilots.

### Step 2. List each term with its required elements

One row per term: the elements, the row ids, and what the person's draft or statement says. Status is the person's word: agreed, in draft, absent. Never mark a term agreed on your own reading.

### Step 3. Apply the hold rule

Offer the register's default rule (a partner whose claim-use term is absent is held) and ask the person to confirm or replace it. Apply only the rule they confirm. List the partners on hold and the term that holds them.

### Step 4. Lay out the fraud-and-abuse stops

For each trigger hit (T1 to T8 in `references/fraud-and-abuse-stops.md`), write:

1. The trigger in the person's words and its row.
2. The elements of the safe harbor or exception that could apply (E1 to E11), one line each with its row, marked "stated in your terms", "not stated" or "not applicable". Never "met".
3. Exclusions and precedents that apply on the facts (for example: outcomes-based payments by a device maker or distributor are excluded, CP-US-13). Where the free or loaned item is a general-purpose device (tablet, smartphone, laptop), add the AO 19-02 reasoning: OIG said a phone with general functions such as a browser, camera or other apps would likely change the outcome (CP-US-41); the opinion binds only its requestor (CP-US-43).
4. "Stops for your compliance or legal owner (NAME as you gave it, or owner not named)."

Do not write that the arrangement is protected, compliant or low risk, and do not suggest a restructuring as the answer. If the person asks for options, list the elements that a restructured design would need to state, labeled "proposed, for the owner".

### Step 4b. Pharma partner pilot terms

If T-P applies, write one line per term P1 to P5 from `references/partner-terms.md`, with its row and the person's facts against it. Start with P1: if any payment depends on outcomes and the payer is the drug maker or the device maker, write "Outcomes-based payments made by pharmaceutical manufacturers or device manufacturers are excluded from the outcomes-based payments safe harbor (CP-US-13). Stops for your compliance or legal owner." Do not suggest a structure that avoids the exclusion; if asked, list the elements a restructured design would need to state, labeled "proposed, for the owner". The pilot's sites, length, success measures and exit are the person's; lay them out as given, labeled "method, not a sourced rule". In Germany, add P4 and stop.

### Step 5. Disclosure check (if a party is public)

If the person says a party is an SEC reporting company, or `diligence-dh.get_funding_signals` shows it files 10-K or 8-K reports, lay out S1 to S3 (CP-US-79 to CP-US-83): whether the agreement is material is that company's call with its counsel. Filing rows in the library carry no 8-K item number; open the filing URL to read what an earlier 8-K covered.

### Step 6. Launch prerequisites the partner depends on

If the partner imports, distributes or deploys: FDA registration and listing (CP-US-71 to CP-US-73), UDI (CP-US-75 to CP-US-78), EUDAMED actor and device registration (CP-EU-10 to CP-EU-15), DTAC and DCB0129 evidence for NHS deployers (CP-UK-01 to CP-UK-10). State each as a dependency, not a deadline.

## Build the output

Follow `assets/partner-terms-output.md`. Answer first: what blocks this partner from starting (absent terms, holds) and what stops for legal or compliance. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every element has a row; every status is the person's.
- Every fraud-and-abuse trigger is laid out for the owner; no element is marked "met"; no arrangement is called protected.
- Commercial terms (price, margin, territory, exclusivity) are the person's; none is proposed as a number.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- A checklist for the owner, not a legal review or a contract draft.
- Claim clearance is the regulatory or legal owner's; the claims audit task flags claims.
- Payer contracts and reimbursement are Market Access.
- Drugs, biologics and wellness apps are out of scope.
