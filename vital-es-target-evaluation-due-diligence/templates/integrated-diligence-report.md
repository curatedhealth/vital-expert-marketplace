# Integrated diligence report: {asset or company} ({asset|company} mode, as of {as_of})

Prepared by: {agent or person}    Reviewed by: {name, role, date or UNSIGNED}    Version: {n}    Release state: Draft    Status: UNSIGNED
Structure: decision-ready order of the authoring anatomy 3.6 (house format; ENGINEERING RULE). This file lists the sections the tool writes; `tools/assemble_report.py --md` fills them. The report adds no finding of its own: every line below carries a pointer `<code>:<path>` to a register row of one of the nine skills (F A B C D E G R H). Nothing is recommended or certified.

## 1. The answer in three lines
- Line 1: workstreams by proposed status (green, yellow, red), confirmed by the deal lead.
- Line 2: open GAPs, [CHECK] items, triggered failure modes, cross-workstream conflicts, missing outputs.
- Line 3: the largest open items; "nothing is recommended or certified; the deal lead decides".

## 2. Workstream status (proposed)
| Workstream | Proposed status | Rule applied | Register | Deal-lead confirmation |
|---|---|---|---|---|
Proposed by rule R-STATUS from register counts (triggered failure modes, open GAPs, [CHECK] items, sign-off). Labelled ENGINEERING RULE: traffic-light severity is practitioner practice (Seimetz 2020, VP-A-142), not a standard, and no source sets thresholds. Defaults: red when the output is missing, triggered failure modes are 2 or more, open GAPs are 5 or more, or [CHECK] items are 8 or more; green when all four counts are zero and the sign-off is closed; yellow otherwise. The deal lead confirms or changes each status in the last column.

## 3. Top risks across workstreams
| Rank | Risk | Kind | Register pointers |
|---|---|---|---|
Ranked by rule R-RANK: conflicts, then triggered failure modes and H conditions marked not met, then failure modes marked cannot tell; ties by workstream order.

## 4. Conflicts between workstreams (side by side, not reconciled)
| Rule | Result | Left | Right | Detail |
|---|---|---|---|---|
R-CONF-1 launch timing (B) against effective exclusivity (C); R-CONF-2 regulatory route and timing (D) against the development timeline (B); R-CONF-3 differentiation claims (G) without support in A or F; R-CONF-4 commercial conditions (H) that depend on rows still open elsewhere; R-CONF-5 licensor obligations (E) against the licence chain (C); R-CONF-6 revenue launch years (R) against the approval years implied by the timeline (B); R-CONF-7 the exclusivity end year behind the erosion start (R) against the effective exclusivity in C. Two sides are shown; the report never says which is right.

## 5. Open gaps and what each blocks
| Workstream | Gap | Why it matters | Blocks | Pointer |
|---|---|---|---|---|
A missing workstream output is a GAP for that workstream with its consequence and the skill to run (REQUIRES routing).

## 6. Decision options (none recommended)
### Sign
Conditions that would have to hold, each with the rows that make it unmet.
### Sign with conditions
Conditions precedent: open GAPs, open conflicts, [CHECK] items, open sign-offs.
### Do not sign
Conditions present: red workstreams, triggered failure modes, commercial conditions not met, conflicts.

## 7. Sign-off
Prepared by: {name}    Reviewed by: {name, date or UNSIGNED}    Deal lead decision: PENDING (HUMAN ONLY)    Version: {n}    Release state: Draft    Status: UNSIGNED
The deal lead (BD head or investment lead) decides: sign, sign with conditions or do not sign. This is a human-only gate. The report records the decision, the deciding person and the date; it never makes or suggests it.

### Optional — Scope and limitations (PRACTITIONER; ICAEW CDD analog VP-CM-060)
Reviewed / not reviewed / cut-off date / access limits / data not provided / assumptions. Prefer this block over MD&A-style or Rule 175 safe-harbor boilerplate (VP-CM-070 — issuer filings only; not this pack).

### Optional — COI / independence note (PRACTITIONER; not attest engagement rules)
Relationships and activities of preparers/reviewers that a reasonable informed third party might view as impairing objectivity (ICMJE VP-CM-030/031; WHO DOI VP-CM-080/081; COPE VP-CM-090/091; ICAEW VP-CM-061: consider conflicts at outset). Disclose here or state "none disclosed — declared by {human}, {date}." Disclosure is not a clearance — do not invent independence findings. Does not replace deal-lead ownership of the decision. If AI-assisted drafting was used on this pack, disclose per ICMJE VP-CM-040/041 (humans remain responsible; AI is not an author). Prepared by: assemble_report (software). Reviewed by / Approved by: HUMAN PENDING — software never self-reviews (IIA re-performance analog VP-CM-050).

## 8. Rules applied
Thresholds in force (team-set defaults, client may override with --thresholds) and the rule list R-STATUS, R-CONF-1 to R-CONF-7, R-RANK, all ENGINEERING RULES of the tool.

## Roll-up across assets (company mode only)
| Asset | F | A | B | C | D | E | G | R | H |
|---|---|---|---|---|---|---|---|---|---|
Statuses side by side. Dates and ranges are never merged across assets.
