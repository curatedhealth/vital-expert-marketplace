# A1 Economic evidence requirements

Framework task: DH-01.07.1.1, Part A, task A1. Replaces the earlier "Access pathway" section, re-scoped: the route itself (DiGA, PECAN, NICE, CMS) is chosen in dh-market-access; this task says what evidence and economic case each named body asks for on that route.

## What this task delivers

A profile, per body the person names, of the evidence and economic case that body asks for: which text governs, the evaluation type, perspective, horizon, discounting, utilities and value set, the budget impact expectations, the role of thresholds, and any conflict inside the body's own texts, each with its row and read date. It answers "what economic evidence does NICE (or HAS, IQWiG, ICER) need from us, and does the EU JCA look at it at all?"

Why it matters: economic cases fail on method before they fail on numbers. A societal-perspective model sent to NICE, a 3L value set on a topic launched after 27 August 2026, a cost-utility model where ICER-PHTI leads with one-year budget impact: each is visible before any modeling starts if the body's rules are laid side by side.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.1.1 Part A, Economic evidence requirements |
| Workflow | The steps below |
| Knowledge | `references/body-economic-standards.md`; `references/health-economics-methods-research.md`; `references/evidence-synthesis-research.md` (EU JCA rows) |
| Tools | `market-access-dh.list_schemes` (free, optional: which bodies the library holds decisions for); no counted calls |
| Prompt | This guide |
| Template | `assets/requirements-output.md` |
| Input | The request and its context: target bodies (or the route from dh-market-access), product type, intended purpose and device class, guidance type if known (NICE routine or early use), topic start date if a NICE topic exists |
| Governance | `references/governance.md` |
| Catalogue job | None. No library job returns economic method rules; `value-dossier` is design-partner only and not startable (`references/tools.md`) |

## Read the request

- **Bodies.** Take them from the request or from a route in the conversation. If none are named, ask which, offering NICE (HealthTech routine or early use, and the ESF for commissioners), HAS, IQWiG, ICER-PHTI and the EU JCA. Keep to the ones named.
- **Device facts.** Device class and intended purpose decide the ESF tier (`HE-082` to `HE-084`), whether the ESF applies at all (`HE-081`, SiMD excluded) and whether a JCA is possible (`HE-096`). If unknown, mark `[GAP]`, show the branches, and name as the source the owner the person names for device status (or owner not named) or dh-regulatory-strategy.
- **NICE timing.** A topic's launch or start date decides the governing text (`HE-066`) and the value set (`HE-062`, `HE-063`). If no topic exists yet, say the post-27 August 2026 rules would apply to a topic launched now.
- **Mode.** "Does NICE need a cost-utility model?" is short mode. "Requirements across our three markets for the steering group" is full mode.

## Workflow

### Step 1. Fix the governing text per body

From `references/body-economic-standards.md`, name the text and version that governs each body for this product, with rows: NICE PMG48 for HealthTech with PMG36 section 4.2 as reference case and PMG51 for utilities (`HE-064`, `HE-070`, `HE-057`); NICE ESF for commissioners (`HE-078`, `HE-079`); HAS 2020 guide (`HE-102`); IQWiG General Methods 8.0 (`HE-108`); ICER-PHTI framework (`HE-115`); EU HTA Regulation and Implementing Regulation (EU) 2025/2086 (`HE-093` to `HE-100`). Where a transitional rule applies, say which (`HE-066`).

### Step 2. Lay out the economic elements

For each body, one row per element the references hold: evaluation type, perspective, outcomes and utilities, value set, discount rate, horizon, results format, budget impact, thresholds or their absence. Use the summary table in the reference as the backbone. Every cell carries its row; an element the references do not hold is `[GAP]` with the authority to check (for example HAS economic-opinion triggers for devices; DiGA economics).

### Step 3. Place the product in the body's categories

- ESF tier (A, B or C, and the tier C group) from the intended purpose the person gives (`HE-083`, `HE-084`). Standard 17 applies to all tiers (`HE-087`); standard 18 only for "higher financial risk", which the commissioner and the owner judge (`HE-090`).
- NICE guidance type: early use or routine use (`HE-071`, `HE-073`). Early use changes what the economic evaluation must show (`HE-068`, `HE-069`).
- ICER-PHTI tier (`HE-125`): tier 1 self-directed without clinician involvement; tier 2 diagnostic and prognostic with professionals. Tiers 3a and 3b are named in the row without definitions: `[GAP]`.
- EU JCA: in scope only for class IIb or III devices with an expert-panel opinion that are selected (`HE-096`, `HE-097`); the first selection on 6 October 2026 held no digital-only product (`HE-101`). Whatever the scope, JCA does not assess cost or economics (`HE-094`). Where a JCA is in scope and the person asks what the clinical review must apply, list RoB 1's seven domains with their Low, High and Unclear criteria and the summary rule from `references/body-economic-standards.md` (`ES-163`, `ES-171` to `ES-193`), and say RoB 2 remains Cochrane's current tool; the review itself belongs to dh-clinical-validation.

Placement is a proposal from the person's facts, labeled "proposed"; the classification decision is the owner's.

### Step 4. Name the conflicts and the moved dates

State, where they touch the request: NICE thresholds (`HE-074` against `HE-050`, `HE-051`; research file conflict note 1); NICE value set (`HE-046` against `HE-058`; note 2); EVA renamed early use (`HE-067`; note 4); NICE budget impact test raised to £40 million in June 2025 (`HE-055`; note 5); AMCP 6.0 final not read, draft rows only (`HE-131`; note 11); RoB 1 against RoB 2 for a JCA (`ES-163`; ES conflicts). Each with the instrument that set it and its date.

### Step 5. Say what it means

Close with the consequence in facts: which economic deliverables each body expects (a reference-case CUA, a cost comparison, a BIA with stated elements, an early-use simplified model with key uncertainties), where one model can serve several bodies and where it cannot (perspective, discount rate and value set differ, conflict notes 6 and 7), and what the person must decide (target bodies, guidance type sought, which perspective to build first). Never say which body to approach; that is dh-market-access's and the person's.

## Build the output

Follow `assets/requirements-output.md`. Answer first: per body, one line on the economic case it asks for. Then the element table, the placement, the conflicts. Short mode keeps one table (element by body, with rows) and the conflict lines.

## Before you hand it over

- Every element carries its row id and the read date (19 October 2026).
- Both NICE threshold ranges appear whenever a threshold is mentioned, with "NICE decides".
- The JCA line says economics stays national.
- Placement (tier, guidance type) is labeled proposed and the owner's decision (owner as named, or "owner not named").
- Short mode counted: 450 words or fewer.
- Record line present.

## Boundaries

- No route choice, fees, clocks or submission mechanics: dh-market-access (`payer-engagement-and-hta-submission`).
- No price, threshold price or discount: dh-market-access (`coding-pricing-and-payer-contracting`).
- No device classification: dh-regulatory-strategy.
- Drugs, biologics and wellness apps are out of scope.
