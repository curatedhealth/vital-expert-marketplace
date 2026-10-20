# A2 Change impact assessment

Framework task: DH-03.02.2.1, Part A, task A2. Replaces the analysis half of the earlier "Change record" section.

## What this task delivers

A question sheet for one software change: every question of each framework that applies to the device (FDA's 2017 software-change questions, the PCCP, MDCG 2020-3 for legacy EU devices, MDR Annex IX 4.10 for certified devices, and the field-action rules), the answer the person gave with its basis, what the source says that answer points to, and which questions are still open. It answers "what do the rules say about this change?" It does not answer "do we submit?"; that is the owner's decision, recorded in B1.

Why it matters: FDA's Change Control inspection area exists to confirm changes are "adequately evaluated for risk and impact on products and processes prior to implementation" (QS34). A sheet that shows each question, answer and source is that evaluation in a form an investigator or notified body can follow.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (`quality-assurance-manager-software`) |
| Skill | DH-03.02.2.1 Part A, Change impact assessment |
| Workflow | The steps below |
| Knowledge | `references/change-significance.md`; `references/QUALITY_SYSTEMS.md` (CH, VG, QS rows); `references/AI_ML_REGULATION.md` (PCCP rows); `references/supplementary-rows.md` (QX10 to QX38) |
| Tools | `regulatory-dh.list_jurisdictions`, `regulatory-dh.search_devices`, `regulatory-dh.get_authorization`, `regulatory-dh.search_safety_events`; `scripts/change_questions.py` |
| Prompt | This guide |
| Template | `assets/change-impact-assessment-output.md` |
| Input | The change description; device, markets, authorization numbers and certificates; risk file references; whether a PCCP was authorized; earlier changes since the last clearance |
| Governance | `references/governance.md`; the owner decides |

## Read the request

- **The change.** What changes in code, behavior, outputs, labeling. Split it into separate changes if it bundles several (QX12).
- **The device's status per market.** 510(k) or De Novo, PMA or exempt in the US; legacy MDD device, MDR technical documentation certificate or type examination in the EU; UK. This picks the frameworks (`change-significance.md` section 0).
- **The baseline.** The most recently cleared device (QX18, QX33) and the changes made since then (QX13).
- **Mode.** "Does this need a 510(k)?" gets short mode: the frameworks that apply, the answers that point toward a submission or approval, the open questions. A change board pack gets full mode.

## Workflow

### Step 1. Choose the frameworks

Use `change-significance.md` section 0 and say which frameworks apply and why, each with its row. Say when a framework does not apply (for example the 2017 guidance for a PMA device, QX10; MDCG 2020-3 for an MDR-certified device). For the UK, say no change-significance rule is sourced (`[GAP]`) and note MHRA's stated PCCP draft guidance (AI UK-04).

### Step 2. Fix the baseline from the library

- Call `regulatory-dh.list_jurisdictions` (free) to state what the library holds for each market.
- Call `regulatory-dh.get_authorization` with the person's K, DEN or P number. Record product, decision date, product code and predicate as the record states them. If the person gives only a name, call `regulatory-dh.search_devices` with the manufacturer name (full product names can miss; `references/tools.md`).
- The record does not show whether a PCCP was authorized. Ask the person and cite their authorization letter.
- Never pass confidential change details to the library; only public identifiers.

### Step 3. Walk the questions

Ask the person each question of each framework, in order, and record answer and basis (document id, version, test report). With code execution, write the answers to JSON and run `python3 scripts/change_questions.py answers.json`; without it, fill the same table by hand from `change-significance.md`. Rules while walking:

- Use the source's question wording. Do not answer for the person. If the person asks what you think, lay out the facts that bear on the question and say the answer is theirs.
- Q3a needs all three criteria answered (CH14).
- A "yes" that the body text lists among significant examples (MDCG 2020-3) is reported with the example it matches; a non-significant example is reported with the benefit-risk caveat (CH7).
- Unanswered questions stay open.

### Step 4. Add field-action and risk-file questions

If the change reaches devices already in use, walk the `field` questions (VG22 to VG25, VG3, VG8). Ask whether the risk file has been updated (QS22, EU15).

### Step 5. Context from comparable products (optional)

Call `regulatory-dh.search_safety_events` with the product code or a comparable manufacturer to show how released software changes of similar devices failed in the field. Describe each row only by what it states (firm, product, version, event date, class, summary). Flag rows that do not concern software (the filter matches title text). This is context for the person's risk questions, never evidence about their change.

### Step 6. Summarize without deciding

List, per framework: the answers the source associates with a submission, notification or approval; the answers the source associates with documenting the change instead; and the open questions. End with: "Decision: for the owner (name, or owner not named)."

## Build the output

Follow `assets/change-impact-assessment-output.md`. Answer first: which frameworks apply, which answers point where, what is open. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Every question carries its row; every answer is the person's, with its basis or "basis not given".
- No sentence says "a 510(k) is needed", "not significant" or "no notification needed" as a conclusion.
- Library rows are cited with source URL and retrieval date; recalls are context only.
- Guidance status and date are stated (2017 final, predates the QMSR; PCCP final reissued 18 August 2025; MDCG 2020-3 Rev.1 May 2023).
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Assesses one change at a time against sourced frameworks. The decision and its record are B1.
- Does not write the 510(k), the PMA supplement, or the notified body notification.
- Does not classify the device or set its pathway; that is DH-03.03 Regulatory Strategy.
