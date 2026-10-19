# B1 Adoption and governance plan

Framework task: DH-02.04.2.1, Part B, task B1. Replaces the register task "Adoption of the component" (CF-12.02.04.2.1.3) and carries the judgment the old task left implicit: which components to build, promote or retire, and who moves which product.

## What this task delivers

A plan with three parts: (1) the version map of products on the current and older versions of each component, with the owner of each product that is behind and the date or reason the owner gives for moving or not moving; (2) the governance the person chooses for the system: contribution and publication criteria, lifecycle statuses, version rule, how modifications and forks are handled; (3) a ranked component backlog, ranked only on the person's scores. It answers "what do we build, promote or retire, and who moves which product by when?"

Why it matters: a published component is not the component in the product (register rule: "Do not assume a published component is the one in the product"). Public systems publish their criteria and lifecycle (UX-UK-29 to UX-UK-32, DSX-24 to DSX-29) so that product teams know when a component is safe to adopt and when to move off one.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | UX/UI Designer, Digital Health (`ux-ui-designer-digital-health`) |
| Skill | DH-02.04.2.1 Part B, Adoption and governance plan |
| Workflow | The steps below |
| Knowledge | `references/governance-models.md`; `references/component-requirements.md` section 3; A1 contracts and A2 change notes in the conversation |
| Tools | `scripts/ds_adoption.py` (version map); `analytics.rice` or `analytics.mcda` (counted, only on the person's scores); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/adoption-and-governance-plan-output.md` |
| Input | The request and its context: the inventory, the person's current versions, owners, the governance choices they have made or want to make, backlog items and their scores |
| Governance | `references/governance.md`; people choose criteria, statuses and rules, score the backlog and name owners and dates |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: options from public practice, decisions by the person

GOV.UK, NHS and USWDS practice is laid out as options with their rows. The person adopts, adapts or rejects each one. The model never writes a criterion, status, rule, score, owner or date for them; anything it suggests is labeled "proposed". Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. An inventory owner owns the row it sits on. For a backlog item that is new or cross-product work (build, replace, migrate), write the owner the person named for that item, or 'owner not named' and ask; an inventory owner may be quoted only as the owner of the affected product row, labeled "row owner in your inventory".

## Read the request

- **Inventory.** Component, version, products, accessibility status, and if they have them owner, clinical and device flags, modification, lifecycle (columns in the header of `scripts/ds_adoption.py`). A pasted table is enough.
- **Current versions.** The version they declare current for each component.
- **Governance choices made.** Criteria, statuses, a version rule, a rule on forks, if they have any.
- **Backlog.** Items they want ranked (new components, migrations, fixes), and whether they have scores.
- **Mode.** Short for a direct question; full for a governance document.

## Workflow

### Step 1. Version map

Run `python3 scripts/ds_adoption.py INVENTORY.csv` (add `--products "A;B;C"` with their full product list). Without code execution, build the same table by hand. Report products behind current by owner, with clinical and device uses shown separately (register rule: "Do not hide a clinical task on an old component"). Forked uses get no system updates (DSX-33). Where no current version was declared, the script's fallback is labeled. Check the columns. Flag inconsistencies to the person: a product listed twice for the same component at different versions, a use "ahead of current", a clinical or device flag that differs for the same product across rows (split the row and ask). Do not state a product is a device surface while its rows disagree.

### Step 2. Owner and move per product behind

For each product behind current, record the owner the person names and the date they will move, or the reason they will not (register method). If either is missing: "owner not named" or "date or reason not given", and ask. The model proposes no date.

### Step 3. Governance options

For each governance element the person has not decided, lay out the public options with rows from `governance-models.md`:

| Element | Options from public systems | Rows |
|---|---|---|
| Proposal criteria | Useful, unique | UX-UK-29, DSX-15 |
| Publication criteria | Usable (tested with disabled people), consistent, versatile; NHS adds clinically safe | UX-UK-30, UX-UK-31, DSX-13, DSX-14, DSX-17, DSX-18 |
| Statuses | GOV.UK trial and stable; USWDS experimental, stable, use with caution, deprecated, retired | UX-UK-32, DSX-22, DSX-26 to DSX-29 |
| Version rule | GOV.UK: first digit marks a breaking release | DSX-35 |
| Modifications | Override classes for small changes; fork for large changes, losing updates; recheck accessibility of any modified component | DSX-31 to DSX-34 |
| Testing before release | Automated scan on every change; manual tests; testing with people | DSX-36, DSX-37, UX-UK-24 |
| Feedback from product teams | Ask whether a component is used and why not | DSX-23 |

Ask the person to choose. Write their choices back in their words. A rule on how far behind a product may be is the person's; GOV.UK's "no more than 3 months behind" applies to its community resources only (DSX-16) and is shown as an example of such a rule, not as a target.

### Step 4. Decisions on components

Lay out, per component the person asks about, the facts that bear on build, promote, keep in trial, mark for caution or deprecate: products using it and versions (Step 1), accessibility status as recorded, open issues they report, criteria from A1 with no evidence, clinical and device uses. Label any suggestion "proposed". The decision is theirs.

### Step 5. Rank the backlog (only on the person's scores)

If the person wants a ranking, ask for RICE inputs per item (reach, impact as 0.25, 0.5, 1, 2 or 3, confidence as a percent, effort) and call `analytics.rice`, passing confidence as a whole percent (80, not 0.8; see `references/tools.md`). Check each returned score by hand. Or, for weighted criteria, ask for criteria named so higher is better, weights and 0 to 4 scores, and call `analytics.mcda`. Report the order and the scores. Never fill a score. Say which item would move if one input changed, where that is visible from the numbers.

### Step 6. Stops

State what stops: release of a component version into a regulated interface; any statement that the system or a product is accessible or compliant; patient-facing copy or clinical content in a component; whether a component change to a device is significant (A2 questions).

## Build the output

Follow `assets/adoption-and-governance-plan-output.md`. Answer first: the products behind on clinical or device surfaces with their owners, the governance decisions open, and the top of the ranked backlog if scored. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every criterion, status, rule, score, owner and date is the person's, and the output says so; suggestions say "proposed".
- Clinical and device uses behind current are shown, not folded into totals.
- Public systems' practice is labeled as theirs.
- RICE confidence passed as a percent and scores checked.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Plans the system; measuring adoption, drift and contract breaches over time is the monitoring skill (DH-02.04.2.2).
- Product accessibility conformance belongs to the Accessibility & Inclusion skills (DH-02.04.1.x).
- No judgment of teams or people; no forecast of adoption.
