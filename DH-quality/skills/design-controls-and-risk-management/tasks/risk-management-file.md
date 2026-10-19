# A2 Risk management file

Framework task: DH-03.02.1.1, Part A, task A2. Replaces the earlier "Risk control" task (CF-12.03.02.1.1.2).

## What this task delivers

A risk management file draft, or a review of the person's own: the structure as the public sources describe it, hazard-to-harm chains for the device, risk controls in the required priority order, residual risk laid out for the person's decision, and hazards seeded from what has actually gone wrong with comparable products. It answers "what goes in our risk file", "what hazards are we missing", and "are our controls in the right order".

Why it matters: FDA investigators use the risk file to steer the whole inspection (QS31), and the MDR makes risk management a lifecycle process that must absorb post-market information (EU14, EU15). A file built only from the team's imagination misses the failures that comparable products have already reported.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Product Development Lead (`product-development-lead`) |
| Skill | DH-03.02.1.1 Part A, Risk management file |
| Workflow | The steps below |
| Knowledge | `references/risk-management-requirements.md`; `references/quality-systems-sources.md` (rows EU12 to EU21, ST2 to ST5, QS20 to QS22, CH14); comparable safety events from the library |
| Tools | `regulatory-dh.list_jurisdictions` (free); `regulatory-dh.search_safety_events` (counted, two to four calls) |
| Prompt | This guide |
| Template | `assets/risk-file-output.md` |
| Input | The request and its context: device, intended use and users, the person's hazard list or risk file if any, their risk management policy (acceptability criteria, severity and probability scales), comparable products they name |
| Governance | `references/governance.md`; severity, probability and acceptability are the person's |

## The rule that shapes this task: the person's scales and criteria

ISO 14971 sets no acceptable risk level (ST4). Severity scales, probability scales and acceptability criteria come from the person's risk management policy. Ask for them. If the person has none yet, lay out the hazard chains without estimates and say the estimates wait for their policy. If asked to propose an estimate, give it with the fact behind it, mark it "proposed", and keep it out of any acceptability statement until the person confirms.

## Workflow

### Step 1. Frame the file

State the parts the sources require: a plan per device; hazards including reasonably foreseeable misuse; estimation and evaluation; controls in priority order; residual risk disclosed to users; overall benefit-risk; post-market feedback (EU14 to EU18). State that the column structure in the output is a working convention, not ISO 14971 text (`references/risk-management-requirements.md`, last section).

### Step 2. Write the hazard-to-harm chains

For each function of the device that can contribute to harm, write: hazard, sequence of events, hazardous situation, harm. For software, harm is often indirect: a decision made on wrong or late information (MDCG 2023-3 treats harm from decisions based on incorrect device output as indirect harm, VG14; a software error causing incorrect assessment is its malfunction example, VG15). Include foreseeable misuse and use error (EU14, EU17).

### Step 3. Seed hazards from comparable products

Call `regulatory-dh.list_jurisdictions` once to say which jurisdictions can contribute (today: US recalls and MAUDE counts, UK MHRA alerts; EU vigilance and Swiss field safety actions not loaded).

Then call `regulatory-dh.search_safety_events` two to four times, with arguments the store can match:
- `manufacturer` for each comparable firm the person names, and if they name none, for the main firms in the device class (for an insulin dosing app: Insulet with `since: "2025-01-01"`, and Dexcom). A `product` search does not catch every app recall: the 11 September 2025 Omnipod 5 magnifier recall returns only on the Insulet call (`examples/live/safety_events_insulet_since_2025.json`). Use the full four-call budget before writing.
- `product` with a generic device word (for example `{"product": "insulin", "jurisdiction": "US", "limit": 10}`);
- `product_code` only if the person gives the FDA code (for example `{"product_code": "PHV"}`).

Count events, not rows: one recall comes back once per app line or model. For each event, write the failure as a candidate hazard chain in the person's terms ("decimal separator misread under a regional number format, leading to a tenfold dose entry", from the 23 May 2025 Omnipod 5 iOS recall), and say whether the person's file already covers it. Cite each as "FDA enforcement report via the library, event date, firm, retrieved DATE"; the row carries no recall number or record link (`references/tools.md`). A comparable's recall shows the hazard is foreseeable. It is not evidence about the person's product.

An empty result is a store gap, not "no recalls".

### Step 4. Place the controls in priority order

For each hazard, list the controls and their type: safe design, protective measure (including alarms), or information for safety and training (EU16). Where a hazard is controlled only by information for safety, ask whether a design control was feasible and record the reason if not. Each control needs a verification of implementation and, later, of effectiveness (ST4); link them to the trace from A1 if it exists.

For a security hazard, record exploitability as its estimation basis, not probability (ST5), and note that the MDR names information security inside software risk management (EU19, EU21). Further cybersecurity method is `[GAP]` here; point to the Cybersecurity and Privacy pack.

### Step 5. Lay out residual risk for the person's decision

For each hazard: the residual severity and probability the person gave, where that falls against their criteria (computed only if they supplied criteria), and an empty "decision" cell for the person. Then the overall residual risk and the benefit-risk statement the MDR requires (EU12, EU18), both left for the person. Note users must be told of residual risks (EU16).

### Step 6. Name what makes the file change

From QS22 and EU15: new information about unforeseen or known risks triggers review. From CH14: a software change that creates or modifies a hazard, hazardous situation or cause in this file is one of FDA's tests for a new 510(k). Say which hazards in this file sit closest to planned changes, if the person named any.

## Build the output

Follow `assets/risk-file-output.md`. Short mode: what the file needs, the hazards the comparables add, the controls out of priority order, open items. Full mode: the full hazard table with controls, verification links and the residual-risk layout.

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Every severity, probability and criterion in the table is the person's, or marked "proposed".
- No cell says a risk is acceptable or a hazard closed. The decision column is for the person.
- Every comparable event carries date, firm, product line and retrieval date, and is labeled as a comparable.
- Every distinct event the searches returned is either in the table or listed in one line as left out, with the reason (not software, not relevant to this device's functions). If more than five events qualify for short mode, keep the five closest to the device's own functions and name the rest in one line.
- At least one line says that harm from a dose or decision based on wrong or late app output is indirect harm (VG14), and the candidate chains end in that harm.
- The output names the parts that are working convention, not standard text.
- A risk management report or benefit-risk conclusion that will be signed stops for the owner. If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft. AI-assisted draft.

## Boundaries

- No acceptability verdict, no severity scale of the model's own, no ISO 14971 clause text.
- No claim that the person's product has had an event, from a comparable's record.
- Device class and pathway are the regulatory owner's; this task does not set them.
- Drugs, biologics and non-device wellness apps are out of scope.
