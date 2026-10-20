# Miss rules: reading and responding to a missed link

Interpretive reference for B1. Rows from `therapeutic-mechanism-research.md` (TM) and `implementation-research.md` (CS). The owner, the response and the version are the person's; this file lists what the sources say each kind of miss can lead to.

## 1. Read the miss before responding

| Where it missed | What it can mean | Rows |
|---|---|---|
| Delivery (fidelity, dose, reach) | The chain was not tested; the product may be fine and the deployment not. Treat downstream misses as uninterpretable until delivery is fixed. | CS32 (Proctor, DOI 10.1007/s10488-010-0319-7); TM92 (Moore, DOI 10.1136/bmj.h1258) |
| Delivery, adapted | Compare what was delivered with the intervention theory to separate fit-to-context adaptation from changes that undermine fidelity. | TM93 (Moore, DOI 10.1136/bmj.h1258) |
| Use | Engagement or fatigue; receptivity. | TM86, TM87 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Change (mediator did not move, delivery and use met) | The component may not produce the change in this population, or the measure may not capture it. | TM84, TM88 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Outcome (mediator moved, outcome did not) | The change may not drive the outcome here, or context may block it. | TM83 (JITAI, DOI 10.1007/s12160-016-9830-8), TM96 (Moore, DOI 10.1136/bmj.h1258) |
| Population (chain held overall, not in a subgroup) | The chain may not hold for that group. | TM9 (MRC/NIHR, DOI 10.1136/bmj.n2061); precedent TM138 |

## 2. Responses the sources name

| Response | Source wording or fact | Rows |
|---|---|---|
| Refine the component within agreed boundaries | Refinements follow the program theory, within boundaries agreed at the start of each phase, rationale reported; rare during efficacy or effectiveness evaluation. | TM13 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| Repeat a phase | Repeating phases is preferable to automatic progression while uncertainties remain. | TM3 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| Return to design or abandon | ORBIT: if the clinical criterion was not even approached, return to Phase I or decide whether to abandon. MOST: if the best feasible package is too weak, go back. | TM62 (ORBIT, DOI 10.1037/hea0000161), TM73 (MOST, DOI 10.1007/s10461-015-1145-4) |
| Fix delivery, not the product | ERIC strategies such as promote adaptability while naming fixed elements; quality of execution includes fidelity. | CS48 (ERIC, DOI 10.1186/s13012-015-0209-1); CS9 (CFIR, DOI 10.1186/1748-5908-4-50) |
| Narrow the claim | Precedent: reSET showed no abstinence benefit in self-identified primary opioid users, which became a labeled limitation. EndeavorRx's indication says behavioral symptoms such as hyperactivity may not improve. | TM138, TM144 |
| Keep claim and function consistent | DiGAV § 9(2): the claimed positive care effect must be consistent with intended purpose, functions, content and published statements. | TM148 |

The old task rule stays: do not keep a claim for a link that missed. Whether and how the claim narrows is the owner's decision with `dh-regulatory-and-quality` regulatory-submission-and-dossier; the model drafts the facts.

## 3. The version that carries the change

| Rule | Rows |
|---|---|
| Adaptations must keep key functions and be understood; a program theory shows what to retain. | TM19, TM20 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| Changes during a study are reported (what, why, when, how). | TM31 (TIDieR, DOI 10.1136/bmj.g1687) |
| Name the version (the person's identifier) that carries each change; the change itself is recorded under `dh-regulatory-and-quality` document-and-change-control. | old task rule; boundary |
| Re-run the link check on the version that carries the change (A2), with the same plan unless the person revises it before the data are read. | TM57 (ORBIT, DOI 10.1037/hea0000161) |

## 4. Owner categories

The old task named three owner categories: design, evidence, population. Keep them as categories of the miss (component design, the evidence or measure, the population or claim). The owner of each is the person the user names, in their words, or "owner not named". Never a job title chosen by the model.

## 4. Engagement and signal misses (folded DH-01.06.2.2 and DH-01.06.3.2)

Rows from `safety-and-engagement-research.md` (SE). The old miss-owner rule stays for both: name the owner the person gives for each failed element, the date they name to look again or that they stop the unit, and "Do not close a failed element because the existing assessment skill already described it."

| Miss | What it can mean | Responses the sources name (none chosen by the model) | Rows |
|---|---|---|---|
| Use measure outside the person's threshold (A3) | A use-link miss: later links in that cohort cannot separate a mechanism that did not hold from a product that was not used. Low use is not, by itself, a failed outcome; sustained use is not always required. | Revisit the mechanic (design skill A3); establish what "effective engagement" is for this intervention before changing the threshold | CS32 (Proctor, DOI 10.1007/s10488-010-0319-7); SE26; SE86, SE87 (Michie 2017, DOI 10.2196/jmir.7126) |
| Usage level the design tied to an overuse, screen-time or sleep risk (A3 to A4) | A candidate safety signal, read as a level | Read in A4 against the person's threshold | SE16, SE29 |
| Safety signal crossed (A4) | A crossed threshold; seriousness, causality and reportability are not decided here | Reportability and clocks: `dh-regulatory-and-quality` audit-capa-and-complaints; feed PMS data back into risk management and re-evaluate indicators and thresholds: `dh-regulatory-and-quality` design-controls-and-risk-management; preventive or corrective action means informing competent authorities and, where applicable, the notified body | SE63, SE52, SE53 |
| Efficacy signal crossed (A4) | The measure the person tracks fell past their threshold in that period and version | Read beside the claims (B1 step 5); the labeling-claims part of the malfunction definition is laid out for the owner; update of the clinical evaluation is a PMS use | SE40, SE52; TM148 |

The model never decides that a mechanic is "safe", "effective" or "compliant", never decides reportability, and never supplies the look-again date.
