# Training rules: what a customer training plan must cover, and where training stops being enough

Interpretive reference for DH-02.02.4.1. Every rule cites its row in `customer-success-research.md` (CS), `ux-usability-research.md` (UX-) or the register task it replaces. Read on 19 October 2026 unless a row says otherwise. Not owner-reviewed.

## 1. Train the task, not the product

| Rule | Basis |
|---|---|
| Training names the task each role must be able to do from the day-one workflow, the steps the user performs (not the slides watched), and what the user does not need to learn in that session. | Register task CF-12.02.02.4.1.1 (task card); `examples/live/agent_pack_digital-adoption-lead.json` |
| Attendance is not completion. A session record states whether each attendee did the task once, and who in the role did not attend. | Register task CF-12.02.02.4.1.2 |
| Enablement does not end at the session: name the old step that should stop, who checks it after a number of days the person sets, and what happens if it did not stop. | Register task CF-12.02.02.4.1.3 |
| Map each role with the CFIR 2022 role names (high-level leaders, implementation leads, deliverers, recipients) and describe each role by need, capability, opportunity and motivation. Training addresses capability; it does not create opportunity (time, scope) or motivation. | CS18, CS19 |
| CFIR is a list of constructs, not a causal model; it must be made project-specific before use. Do not present a CFIR mapping as a prediction. | CS3, CS11 |

## 2. What official frameworks ask of training (England and NHS buyers)

| Rule | Basis |
|---|---|
| NICE Evidence Standards Framework (ECD7, last updated 9 August 2022): 21 standards in 5 groups; the 3 deployment-consideration standards apply to all tiers. | CS56, CS57 |
| ESF Standard 12: the pathway description covers the need for training and education for professionals or end users. | CS58 |
| ESF Standard 20: the company must have communication on outputs, features, benefits and limitations, and should describe its planned approach for training end users. | CS65 |
| ESF Standard 17: budget impact includes the costs of staffing and training. Training cost belongs in the customer's budget case, not hidden in onboarding. | CS63 |
| ESF Standard 15: a pilot-site statement may confirm the product "was used in line with expectation (who, how, for how long)". The training plan should say who is expected to use it and how, so that statement can be made. | CS59 |
| ESF Standard 16: usage is reported against an expected usage profile agreed at commissioning. The task card is the basis of that profile; adoption-monitoring measures it. | CS61 |
| NHS buyers may need DTAC (updated form from 24 February 2026) and the deploying organization's DCB0160 duty. Both rows were read by a summarizer [WF]; DCB0160 clause content is `[GAP]`. Clinical safety duties at the site are the customer's. | CS68, CS69, CS70, CS71 |

US and EU buyers: no row in this skill's research sets a training-plan requirement for a deploying customer. Say so (`[GAP]`) rather than borrow the NICE list as a legal duty.

## 3. Training as a risk control: where it stops being enough

These rows come from FDA's "Applying Human Factors and Usability Engineering to Medical Devices", reissued 3 August 2026 (originally 3 February 2016; nonbinding, "should" means recommended) and from the MDR and MHRA texts. They apply where the product is a medical device; whether it is one belongs to the person's regulatory owner.

| Rule | Basis |
|---|---|
| The user interface includes training materials. Changing training changes the user interface. | UX-US-31 |
| Order of preference for risk controls: inherent safety by design, then protective measures, then information for safety (labeling, training). | UX-US-33 |
| Design changes are usually more effective than labeling or training, because training depends on memory. | CS77 |
| Training is not the preferred strategy because knowledge gained through training can decay over time. | CS78 |
| Stating in a premarket submission that "additional training" will mitigate critical-task errors is not acceptable without data that it reduces the risk. The same applies to labeling changes. | CS79, UX-US-42 |
| Validation-test training should match what real users get; testing right after training is not valid because retention decays. A customer training plan for a device should match the training that was validated. | CS80, UX-US-41 |
| A change to training or labeling is one of the Decision Point B triggers in FDA's final guidance on human factors content (29 May 2026). A training change for a device goes to the regulatory owner before it ships. | UX-US-47, UX-US-49 |
| Critical task: a task which, if done wrong or not at all, would or could cause serious harm, including compromised medical care. | UX-US-28 |
| MDR Annex I section 5: the manufacturer reduces use-error risk by design and gives consideration to users' knowledge, experience, education and training. | UX-EU-14 |
| MHRA (advisory, v2.0 of January 2021): instructions for use should be validated with intended users in the same format as a summative test. | UX-UK-14, UX-UK-20 |

What this means for a training plan (stated as consequences, not as a regulatory verdict):

- If the person proposes training to fix a use error on a critical task, write: "Training is the least preferred control and decays (CS77, CS78); a submission cannot rely on 'additional training' without data (CS79). This goes to the regulatory owner and the design owner before training is planned." Then lay out the design option beside the training option for B1.
- If the product is a device, the customer's training should not shorten or change the training that was validated (CS80). Ask whether the validated training content is available; if not, `[GAP]`.
- Never state that training controls a risk, reduces a use error, or makes a product safe. That stops for the accountable owner (`governance.md`).

## 4. Training the customer must run itself

| Rule | Basis |
|---|---|
| A HIPAA covered entity must train its workforce on PHI policies, including new staff and after material changes. | CS82 |
| Covered entities and business associates run a security awareness and training program for all workforce members. | CS83 |

These are the customer's (and, for business associates, the vendor's own) duties. Product training does not discharge them, and this skill does not design them; point to the person's privacy or security owner.

## 5. Training strategies with names

ERIC names four training strategies (CS45): conduct ongoing training; make training dynamic; use train-the-trainer strategies; educational outreach visits (named in the row's topic; definition not quoted in the row, `[GAP]` for its text). Definitions and the other strategies are in `enablement-strategies.md`.

## Not sourced here

- Any number of training hours, session length, group size, refresher interval or retention rate. These are the person's or `[GAP]`.
- Learning-design frameworks (for example ADKAR or Kotter, which the expert's remit names): no primary source in the research. Do not apply their stages as rules.
- Training requirements for deploying customers in the US or EU outside HIPAA workforce training.
