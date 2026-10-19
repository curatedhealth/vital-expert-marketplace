# A1 Obligation map

Framework task: DH-02.04.1.1, Part A, task A1. Replaces the first half of the earlier "Access requirement" section (name the standard and version).

## What this task delivers

A map from the person's own facts (who they are, who they sell to, where, and what surfaces they ship) to the accessibility instruments that may apply, the WCAG version and level or EN 301 549 edition each one cites, the dates with the instrument that set or moved them, the exceptions and burden routes each allows, and the questions still open. It answers "which accessibility rules apply to us, and what do they ask for?" It asks and maps; it never declares that the product conforms or that the organization is covered.

Why it matters: the same app can sit under WCAG 2.0 (Section 508, UX-US-02), WCAG 2.1 (ADA Title II and HHS 504, UX-US-08, UX-US-16) and WCAG 2.2 (GDS and NHS, UX-UK-08, UX-UK-22) at once, and two US dates moved in 2026 (UX-US-11, UX-US-18). A team that targets the wrong version, or plans on a stale date, builds the wrong release.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.04.1.1 Part A, Obligation map |
| Workflow | The steps below |
| Knowledge | `references/obligation-map.md`; `references/ux-accessibility-research.md`; `references/wcag-criteria-additions.md` |
| Tools | None required. Optional: `verify.qualify_source` then `verify.check_claim` for a Federal Register date that will leave the conversation; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/obligation-map-output.md` |
| Input | The request and its context: the person's role (Q1 to Q6 in the obligation map), size thresholds, markets, customers, product surfaces (Q7) |
| Governance | `references/governance.md`; the map is facts per instrument; whether an instrument binds them is their legal owner's call |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: ask and map, never declare

Coverage depends on facts only the person has: whether they are a public entity, an HHS recipient, a contractor to one, a federal supplier, an EU or UK public body, or a private seller to consumers. The model asks, maps each answer to the rows, and writes "applies if ..." where an answer is missing. It never says "you are covered", "you are exempt" or "you conform".

## Read the request

- **Role.** Ask Q1 to Q6 from `references/obligation-map.md` that the request does not answer. Take answers in the person's words. A private company selling to a covered hospital or state agency is asked whether its contracts pass the customer's duty on (UX-US-07, UX-US-16 name contractual arrangements); the contract is theirs to read.
- **Size.** Population (ADA) or employee count (HHS 504) decides the date; EAA microenterprise status decides the service exemption (UX-EU-07).
- **Markets.** US, EU (which Member States), UK. Others are `[GAP]`.
- **Surfaces.** Website, native app, app with web views, documents, kiosks (Q7).
- **Mode.** Short for a direct question ("when is the 504 deadline"); full for a compliance map.

## Workflow

### Step 1. Write back the facts

List the person's role, size, markets and surfaces as they gave them, and the questions still open. Confirm before mapping if more than one role is possible.

### Step 2. Map each instrument

For each instrument in the obligation map table, one line: applies if (the person's fact, or "if you are ... `[GAP]`"), what it cites (version, level, edition), dates with the instrument that set them, exceptions or burden route, rows. Leave out instruments the person's facts clearly exclude, and say in one line which were left out and why.

Specific checks:

- ADA Title II and HHS 504 dates: always the current dates with the interim final rule that moved them (UX-US-11, UX-US-18), and "interim; a later final rule could change them".
- Section 1557: never "requires WCAG 2.1 AA"; quote what 92.204 says (UX-US-21, Changes and conflicts 3).
- EAA and a health app: "inference, not a stated rule" with the route (e-commerce or consumer banking features) and UX-EU-04. Microenterprise exemption for services (UX-EU-07). National transposition `[GAP]`.
- EN 301 549: which edition each EU instrument relies on (V3.2.1 under the WAD, UX-EU-01; V4.1.1 for the EAA once cited, UX-STD-29, OJ citation `[GAP]`).
- Native apps and web views: clause 11 (UX-STD-31, UX-STD-32); Section 508 software exceptions (UX-US-03, UX-US-04).
- ONC certified health IT: the (g)(5) attestation, and the HTI-5 proposal to remove it, proposed only (UX-US-23, UX-US-24).
- A stale date the person quotes: say which original date it was and for whom (24 April 2026 was the original ADA date for public entities of 50,000 or more, not special districts; 11 May 2026 was the original HHS 504 date for 15 or more employees; UX-US-11, UX-US-18).

### Step 3. Show where versions differ

If the instruments that may apply cite different WCAG versions, say so in one line and run `scripts/criteria_lookup.py diff` (or read `references/data/wcag_criteria.csv`) to give the count and the criteria that differ, for example "2.1 AA to 2.2 AA adds six criteria and drops 4.1.1 (UX-STD-07, UX-STD-08)". Do not choose the target; that is B1 and the person's.

### Step 4. Optional: check a date that will leave the conversation

If the person will send a compliance date outside the conversation, call `verify.qualify_source {url: <Federal Register URL from the row>}` and then `verify.check_claim {claim: {text}, passage: {text: <the row's quote>, locator}, source: <the qualify_source result object>}`. Read the passage yourself: Verify returned "partial" for both the current and the superseded HHS date (`references/tools.md`), so the status does not prove which date is current. Do not send W3C text to Verify (rated inadmissible).

### Step 5. Open questions and stops

List at most three open questions, the role question first. State what stops for the owner: any legal conclusion that an instrument applies, any burden determination, any published statement.

## Build the output

Follow `assets/obligation-map-output.md`. Answer first: the instruments that apply on the person's stated facts, the version each cites and the nearest date in force with its instrument. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every instrument line has a row id and an "applies if" tied to the person's fact or a `[GAP]`.
- Every moved date names the instrument that moved it; no stale date (24 April 2026, 11 May 2026) appears as current.
- The EAA line says "inference" if it touches a health app.
- No sentence says the person is covered, exempt or conformant.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Facts per instrument, not a legal opinion. Coverage is the person's legal owner's call.
- Markets other than the US, EU and UK are `[GAP]`.
- Device status, human factors submissions and usability evidence belong to the UX 4.x skills and dh-regulatory-strategy. Who is reached and who is left out is Patient Engagement 4.x.
