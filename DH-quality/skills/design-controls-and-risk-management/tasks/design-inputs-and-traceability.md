# A1 Design inputs and traceability

Framework task: DH-03.02.1.1, Part A, task A1. Replaces the earlier "Design input" task (CF-12.03.02.1.1.1).

## What this task delivers

Two things, sized to the request. First, the requirements picture for this device: which design-control rules apply in the US and the EU, what IEC 62304 does and does not give in each, and which MDR Annex I software requirements become design inputs. Second, a trace from user needs and risk controls through design inputs and outputs to verification and validation, with every orphan and gap found. Answer first, then the support.

Why it matters: a requirement that traces to nothing cannot be defended, and a need that traces to no validation has not been shown to be met. Inspectors read the risk file first and follow its controls into the design records (QS31). Gaps found here cost a day; gaps found by an investigator cost a 483.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Product Development Lead (`product-development-lead`) |
| Skill | DH-03.02.1.1 Part A, Design inputs and traceability |
| Workflow | The steps below |
| Knowledge | `references/design-control-requirements.md`; `references/trace-structure.md`; `references/quality-systems-sources.md` (rows QS, EU, ST) |
| Tools | None required. `scripts/trace_check.py` on the person's trace export when code execution is available. `regulatory-dh.list_jurisdictions` only if the person asks what the library holds |
| Prompt | This guide |
| Template | `assets/traceability-output.md` |
| Input | The request and its context: the device and its intended use, target markets, the person's requirements or trace export (CSV, spreadsheet, ALM export), their risk file if A2 ran |
| Governance | `references/governance.md` |

## Read the request

Decide three things. Ask at most one question, and only if the device or the markets are unknown and the answer depends on them.

- **Rules or trace, or both?** "What applies", "does 62304 count in the EU", "what are the software requirements under the MDR" is the rules path (steps 1 and 2). A file, a spreadsheet or "check our trace" is the trace path (steps 3 to 5). "Set up traceability for our new product" is both.
- **Which markets?** US, EU, or both. Keep to the ones named. The UK and other markets are `[GAP]` in the sourced reference for design controls; say so.
- **Short or full?** A direct question gets the short mode (450 words maximum, counted without the source column of tables). A document to share, "full", "for the design review" or "for the notified body" gets the full mode.

Device class matters for the US scope (QS9). If nobody knows it, write the rule both ways ("if class II or III, or class I automated with software...") and mark the class `[GAP]` for the person's regulatory owner. Never decide the class.

## Workflow

### Step 1. Set the rule base for the named markets

From `references/design-control-requirements.md`, write one line per applicable rule with its row id. For the US: QMSR in force since 2 February 2026, ISO 13485 Clause 7.3 by reference, the scope rule for class I software devices, design and development file in place of the DHF (QS1, QS4, QS9, QS24). For the EU: Article 10(9) QMS elements, Annex I 17.1 to 17.4, Annex IX documentation (EU3, EU19 to EU21, EU23). Name every clause that the research does not restate as `[GAP]` with the free read-only route (ST13).

### Step 2. State what IEC 62304 gives, market by market

US: recognized in full, edition 1.1, number 13-79 (ST9). EU: not in the harmonized list through the 11 June 2026 amendment, so no presumption of conformity (EU30). In both: 62304 does not cover validation of the finished device (ST6). Edition 2.0 is forecast for 26 October 2028 (ST8). If the person relies on 62304 for the EU, say plainly that conformity to Annex I 17.2 must be argued directly.

### Step 3. Turn requirements into design inputs

For each Annex I software requirement that applies (EU20, EU21) and each QMSR addition that bears on the product (for example labeling examination, QS13), write a candidate design input in testable form, with its origin in the source column. Mark each "proposed": the person adopts or rejects it. A design input that cannot be verified is not a design input; rewrite it until a test could pass or fail it (this rule comes from the earlier task wording).

### Step 4. Build or read the trace

If the person has no trace, give them the structure from `references/trace-structure.md` and the CSV columns. If they have one, map their columns once to `id, type, links, text, result`, say how you mapped them, and keep the mapping in the output.

### Step 5. Find orphans and gaps

With code execution, run `python3 scripts/trace_check.py trace.csv` (add `--json` for a machine-readable list). Without it, apply the same checks by hand on the rows you were given. Report each finding with the item id, the code (G1 to G7, O1 to O3, R1, R2; G7 is a working-convention finding, say so) and the plain meaning. Check every item; do not sample only the items that trace. A finding is "not in the files provided", never "does not exist".

If the risk file from A2 is in the conversation, check that every risk control appears in the trace (G5, G6). If it is not, say the risk side was not checked.

## Build the output

Follow `assets/traceability-output.md`. Short mode: the answer (what applies, or how many findings of which kind), the rule table or the findings table, and the open items. Full mode adds the column mapping, the proposed design inputs, and the full findings list.

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Every rule carries its row id. No clause text appears that a row does not restate.
- Every finding names the item id from the person's file.
- Proposed design inputs are labeled "proposed".
- The output says these are findings, not a compliance verdict. Anything that enters the design and development file as a decision stops for the owner (`references/governance.md`).
- If it will leave the conversation, ask who clears it and call `verify.build_record` with that name in `cleared_by`; otherwise label it an uncleared draft. AI-assisted draft.

## Boundaries

- No compliance verdict, no release decision, no device class.
- No paraphrase of ISO 13485, ISO 14971 or IEC 62304 clauses beyond what the rows restate.
- The UK, Switzerland and other markets: the sourced reference has no design-control rows for them; say `[GAP]` and stop there.
- Drugs, biologics and wellness apps that are not medical devices are out of scope.
