# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; "Corvelan" (corvelastat) and every person named
are fictional.

## Contents

- Part B, the flag: P1 to P10
- Part A, safety statements: C1 to C10
- Part A, patient language: L1 to L9

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

## Part B: the flag

**P1 The side effect lost in the reply.** A doctor's question email mentions a reaction in
their patient; the draft answers the question and says nothing about the reaction.
Why: the company now knows about it; if nobody passes it on, the safety function never
sees it (S4, S7).
Before: a polished reply on dosing only. After: a three-line flag first, then the reply. (TR-H6, TR-H11)

**P2 The reportability call.** "This is a known side effect, so no report is needed."
Why: whether and how it is reported is the safety function's decision; listed effects
are still passed on (S0, S1).
After: "The email mentions a rash after starting Corvelan. Pass it to your safety
reporting procedure." (TR-H6)

**P3 The causality call.** "The dizziness is more likely due to her blood pressure
tablets." Why: only the safety function, with the full case, assesses this (S1, S9).
After: quote the writer's words; say nothing about cause. (TR-H6)

**P4 The seriousness grade.** "Mild, resolved, low priority." Why: seriousness is defined
and assessed by the safety function, and a hospital stay mentioned in passing can change
it (S4).
After: report what was said, quoted, and let the procedure decide. (TR-H6, TR-H3)

**P5 The invented deadline.** "You must report this within 15 days." Why: that is a
company-to-regulator limit for some cases, not the person's deadline; internal timing is
shorter and set by the procedure (S0, S4).
After: "Pass it on as soon as you can, in the time your safety reporting procedure sets." (TR-H8, TR-H11)

**P6 Waiting for detail.** "Ask the doctor for the patient's age and dose before
reporting." Why: the clock usually starts when anyone in the company has the
information; collecting missing detail is the safety function's job (S3, S4).
After: flag now with what is there. (TR-H6)

**P7 The aside nobody reads.** A pregnancy mentioned in a market research verbatim, a
"stopped working" in call notes, a broken pen in a complaint. Why: these are other
observations or quality complaints the safety function collects (S2, S8, S9).
After: flag each one, named in plain words. (TR-H6)

**P8 The AI summary as the record.** The flag is built only from an assistant's summary
of a transcript. Why: a summary can drop or change the detail that matters (S9).
After: flag, and say the safety function should get the original transcript or notes.

**P9 The public reply that diagnoses.** "Sorry to hear about your headaches, this usually
settles in a week." Why: clinical advice to a member of the public, and a judgment about
the event (TR-H6).
After: "Thank you for letting us know. Please talk to your doctor or pharmacist about
this. [GAP: needs a decision — contact route — from your safety reporting procedure]".

**P10 Health details collected in public.** The reply asks the commenter for their age,
dose and other medicines under the post. Why: follow-up is the safety function's job, by
the route its procedure sets, and health details in public expose the person (S5;
privacy good practice).
After: point to a private route the procedure sets, or leave a gap for it.

## Part A: safety statements

**C1 The remembered dose.** A dosing table filled in from what the assistant "knows".
Why: doses differ by market, formulation and label version, and a wrong dose can harm
(S10 to S12).
Before: "Adults: 20 mg once daily." (No label supplied.) After: `[GAP: not supplied —
adult dose — from section 4.2 of the approved label]`. (TR-H1, TR-H8)

**C2 The generalized population.** Label: "No dose adjustment is required in patients with
mild hepatic impairment (Child-Pugh A)." Draft: "No dose change needed for liver
problems." Why: moderate and severe impairment are not covered by the label statement.
After: quote the label sentence with its Child-Pugh class. (S11)

**C3 Silence read as safety.** The label lists no interaction with a drug; the draft says
"no interaction with X". Why: not listed is not shown to be absent.
After: "The label does not list an interaction with X in the supplied text. Ask your
medical information function." (TR-H1)

**C4 No data read as safe in pregnancy.** Label: "There are no data from the use of
corvelastat in pregnant women." Draft: "Safe in pregnancy."
After: quote the label sentence, and any recommendation it gives, exactly. (S11, S12)

**C5 The softened warning.** Label: "must not be used"; draft: "should be used with
caution". Why: a contraindication became a precaution.
After: the label's words, in the right section. (S11)

**C6 The rounded or converted dose.** Label: "0.5 mg/kg"; draft: "about 35 mg for an adult".
Why: a derived dose the label does not give.
After: the label's dose and unit. (TR-H1)

**C7 The other market's label.** A US prescribing information sentence used in a Swiss
reply. Why: approved wording differs by market (S10, S12).
After: ask for the label for the market the work is for. (TR-H7)

**C8 The merged sentence.** Two label statements from different sections combined into
one that neither says. After: one statement, one section, quoted.

**C9 The advice to the prescriber.** "Your patient can safely continue at a lower dose."
Why: a clinical decision for that patient (TR-H6).
After: the label's statements on dose reduction, quoted, with no recommendation for this
patient.

**C10 The undated label.** Safety content quoted from a label with no revision date.
After: `[GAP: out of date or unclear date — label revision date — confirm the current
approved label]`.

## Part A: patient language

**L1 Complete safety.** "Corvelan is completely safe." After: say what the leaflet says
about side effects; drop "safe". (TR-H3, TR-H6)

**L2 No side effects.** "Most people have no side effects." (Not in the leaflet.)
After: the leaflet's side-effect wording, or a gap.

**L3 The stop instruction.** "You can stop taking it once you feel better." After: "Talk
to your doctor before stopping or changing your treatment," or the leaflet's own words.

**L4 The double dose.** "If you miss a dose, take two next time." After: the leaflet's
missed-dose instruction, quoted, or a gap.

**L5 No route out.** A two-page leaflet with no line telling the reader whom to ask.
After: "If you have any questions, or if something does not feel right, talk to your
doctor, nurse or pharmacist." (S13, good practice)

**L6 The fear lever.** "Skipping doses can be deadly." After: the leaflet's wording on
taking it as prescribed, and the route line.

**L7 Natural therefore harmless.** "Made from a plant extract, so it is gentle on the
body." After: remove; give the leaflet's safety information.

**L8 Everyone's experience.** "Patients tell us they hardly notice it." After: remove, or
quote a supplied, dated source with its size; `grounded-statements` owns the figure.

**L9 The invented hotline.** A phone number or reporting website added to "help". After:
only a route the person supplied; otherwise a gap. (TR-H1)
