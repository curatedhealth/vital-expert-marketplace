# Risk management for device software: what the sources say

ISO 14971:2019 is paywalled. This file uses it only as FDA's recognition entry and the MDR restate it, plus the status pages on iso.org (marked [WF] in the research). Every rule carries its row id in `quality-systems-sources.md`. Where a clause is not restated, it is `[GAP]`.

## The standard and its status

| Fact | Row |
|---|---|
| ISO 14971:2019, edition 3, covers risk management of medical devices including software as a medical device; last reviewed and confirmed in 2025 [WF]. | ST2 |
| FDA's entry for ISO 14971 (public abstract): it sets a process to identify hazards, estimate, evaluate and control risks and monitor the effectiveness of controls across the lifecycle. It **does not specify acceptable risk levels** and does not require a QMS. | ST4 |
| FDA recognizes ISO 14971 in full, number 5-125, entered 23 December 2019, and lists ISO/TR 24971 as a supporting publication. | ST5 |
| ISO/TR 24971:2020 is non-mandatory guidance on applying ISO 14971:2019; iso.org shows it at stage "to be revised" since 6 July 2026 [WF]. | ST3 |
| The QMSR does not incorporate ISO 14971. In the EU, EN ISO 14971:2019 with A11:2021 is harmonized. | QS21, EU29 |

Consequence for every task: **acceptability criteria are the manufacturer's own**, written in its risk management policy or plan. The standard does not supply them (ST4). The model never supplies them either.

## The process, as the MDR restates it (Annex I Section 3)

The MDR text is public and binding; it is the most complete public restatement of the process. Annex I Section 3 requires the manufacturer to (EU14, EU15):

1. establish and document a risk management plan for each device;
2. identify and analyze known and foreseeable hazards for each device;
3. estimate and evaluate risks in intended use and in reasonably foreseeable misuse;
4. eliminate or control those risks (in the priority order below);
5. evaluate information from production and post-market surveillance on hazards and their frequency, risk estimates, overall risk, benefit-risk and acceptability;
6. amend control measures where needed.

Steps 2, 3, 4 and 6 are named in the research's summary of EU14 and EU15; only the plan (a), the lifecycle sentence and point (e) are quoted verbatim. Before using the wording of points (b) to (d) or (f) in a document that leaves the conversation, re-read Annex I Section 3 in the consolidated MDR (link in EU1).

Risk management is "a continuous iterative process throughout the entire lifecycle of a device, requiring regular systematic updating" (EU14).

## Risk control priority (Annex I Section 4)

In this order (EU16):

1. eliminate or reduce risks as far as possible through safe design and manufacture;
2. where appropriate, protection measures, including alarms if necessary;
3. information for safety (warnings, precautions, contraindications) and, where appropriate, training.

Users must be informed of residual risks (EU16). "As far as possible" means without adversely affecting the benefit-risk ratio (EU13). Use-error risks are reduced through ergonomic design and attention to users' knowledge, training and environment (EU17).

What this means for a risk file: a control that is only information for safety, when a design control was feasible, needs a recorded reason. The old task wording carried the same rule ("Do not close a hazard with a user instruction when a design control is feasible, without saying why").

## Acceptability: what the person decides against

- Each risk, and the overall risk, must be acceptable when weighed against benefits to the patient and compatible with a high level of protection, considering the generally acknowledged state of the art (EU12, EU18).
- All known and foreseeable risks and undesirable side-effects are minimized and acceptable against evaluated benefits (EU18).
- The standard sets no acceptable level (ST4). The person's policy does.

## Updating the file

- FDA expects risk documentation to be reviewed and updated when the manufacturer becomes aware of previously unforeseen risks or new information about known risks (QS22).
- The MDR requires post-market information to be evaluated against hazards, frequencies, estimates and acceptability (EU15).
- FDA's 2017 software-change guidance asks first whether a change "creates a new or modifies a hazard, hazardous situation, or cause in the risk management file", assessed on the pre-mitigation risk (CH14). The risk file therefore decides, in part, whether a US software change needs a new 510(k). The guidance predates the QMSR and FDA says so on it (CH10).

## Cybersecurity: the one sourced note

FDA's recognition entry for ISO 14971 notes that the standard's probabilistic model of harm does not apply to cybersecurity, substituting exploitability (ST5: "explicitly states this probabilistic model does not apply to cybersecurity, substituting exploitability"). In a risk file, security hazards therefore need their own estimation basis (exploitability) rather than a probability of occurrence. The MDR also names information security inside software risk management (EU19) and asks for stated IT security measures including protection against unauthorized access (EU21).

`[GAP]`: FDA's premarket cybersecurity guidance, any statutory cybersecurity requirement, and any exploitability scale. None is in the research. Point the person to the Cybersecurity and Privacy pack, and do not name a scoring scale.

## Structure of a risk file: what is sourced and what is a working convention

Sourced: a plan per device; hazards identified, including foreseeable misuse; risks estimated and evaluated; controls in priority order; residual risks disclosed; overall benefit-risk; post-market feedback (EU14 to EU18, ST4). In ISO 14971 terms as FDA's abstract uses them: identify hazards, estimate, evaluate, control, monitor (ST4).

Working convention used by this skill (not quoted from any standard; label it so in outputs): each hazard row carries hazard, sequence of events, hazardous situation, harm, severity, probability (or exploitability for a security hazard), initial risk, control(s) with their priority type, verification of implementation, verification of effectiveness, residual risk, and the acceptability decision with who made it. The terms "hazardous situation" and "cause" appear in FDA's software-change guidance (CH14). The ISO 14971 definitions and clause numbers for these terms are `[GAP]`.
