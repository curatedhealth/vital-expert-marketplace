# Use error and critical tasks: definitions and design rules

Used by A2. `UX-` rows are in `ux-usability-research.md`; `CS` rows in `implementation-research.md`. FDA guidance is nonbinding ("should" means recommended, UX-US-26). The FDA human factors guidance quoted here is the 3 August 2026 reissue (UX-US-25); the 2016 text is superseded.

## 1. Definitions to use word for word

| Term | Definition as the source states it | Row |
|---|---|---|
| Use error (FDA) | "User action or lack of action that was different from that expected by the manufacturer and caused a result that (1) was different from the result expected by the user and (2) was not caused solely by device failure and (3) did or could result in harm." | UX-US-27 |
| Use error (MHRA) | Includes failure to complete a task; users may be unaware it happened; a device malfunction is not a use error. | UX-UK-15 |
| Critical task (FDA) | "A user task which, if performed incorrectly or not performed at all, would or could cause serious harm to the patient or user, where harm is defined to include compromised medical care." | UX-US-28 |
| Critical tasks (MHRA) | A subset of hazard-related use scenarios chosen by severity of harm. | UX-UK-18 |
| Usability engineering process | IEC 62366-1:2015+A1:2020 covers normal use (correct use and use errors), not abnormal use. Clause text is paywalled `[GAP]`. | UX-STD-36, UX-STD-37 |

A misread of a screen (wrong patient, wrong unit, stale value) is a use error under UX-US-27 only if the result differed from what the user expected and did or could cause harm. A wrong value caused solely by a software fault is not a use error (UX-US-27, UX-UK-15); it is a device failure and belongs to the person's risk file.

## 2. How the sources say to rank and control

| Rule for the skill | Rows |
|---|---|
| Severity of potential harm is more meaningful than probability when deciding what to design out, because use-error probability is hard to estimate. A2 asks the person for severity; it does not estimate probability. | UX-US-32 |
| Risk-control order of preference: inherent safety by design, then protective measures, then information for safety (labeling, training). | UX-US-33 |
| Design changes usually beat labeling or training: labeling may not be at hand and training depends on memory, which decays. | CS77, CS78 |
| After critical-task errors, stating that labeling or "additional training" mitigates the risk is not acceptable without data showing it works. A2 marks any control that is training or labeling only as "needs data". | UX-US-42, CS79 |
| EU: manufacturers must reduce use-error risk from ergonomic features and use environment, considering users' knowledge, training, use environment and medical and physical conditions, including disabled users (MDR Annex I section 5). | UX-EU-14 |
| EU lay use: reduce as far as possible the risk of error in handling and in interpreting results; where appropriate let users verify the device works and warn when no valid result was produced (MDR Annex I 22.2, 22.3). Use this for patient-facing screens that show a result. | UX-EU-18, UX-EU-19 |

## 3. Who is a distinct user

| Rule for the skill | Rows |
|---|---|
| FDA treats pediatric and adult users as distinct populations, and professionals and lay users as distinct populations. A2 lists critical tasks per population. | UX-US-36 |
| Where the condition causes functional limits (FDA's examples: diabetic retinopathy, neuropathy), a representative range of those limits belongs in evaluation; otherwise labeling must state required capabilities. | UX-US-37 |

## 4. Comparable field events (optional step)

`regulatory-dh.search_safety_events` returns recalls and alerts by product, manufacturer or product code. It has no use-error field or filter (`references/tools.md`). In the live calls of 19 October 2026, interface-related summaries included:

- Omnipod 5 iOS App, Class II, event date 23 May 2025: "a comma is not recognized as a decimal separator ... (e.g., 0.1 unit recognized as 1 unit)" (`examples/live/safety_events_insulin_us.json`).
- t:slim X2 with the t:slim mobile app, Class II, 3 July 2025: "when the phone is set to a right-to-left language, which causes app-pump pairing issues and graphical defects".
- Hologic Genius Review Station display, Class II, 23 March 2026: devices "operated outside the validated and FDA-cleared display configuration due to user modification of the manufacturer-installed settings" (`examples/live/safety_events_display_us.json`).

Use such records only as prompts for which misreads to look for (locale and units, language direction, user-changed settings). Describe each only by what its record states. Never infer a root cause, a use error or a design failure in someone else's product from a recall.

## 5. Not in the sources

- A severity scale. The person's risk management file sets it.
- Probability or frequency estimates for use errors.
- ISO 14971 and IEC 62366-1 clause text.
