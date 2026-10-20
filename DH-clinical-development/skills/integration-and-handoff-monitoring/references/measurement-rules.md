# Measurement rules: scoring handoffs without inventing a standard

Interpretive reference for DH-01.01.3.2 (Integration Effectiveness Assessment & Cross-Functional Alignment Monitoring). Row ids refer to the research files copied in this folder (PL, CV, CS, TM). The sourced anchors for where handoffs happen are in `handoff-rules.md`.

No source read for this pack defines a handoff measure, a handoff score, a lateness threshold or a target for cross-functional work. Every measure in this skill is therefore the person's. What the sources do give is a small set of patterns about measuring well: fix the measure before the data come in, count against everything that was due, keep categories apart, and feed results back to the people who did the work. The skill offers those patterns, labeled as patterns, and applies only the rule the person confirms.

## 1. Patterns the skill may offer (labeled)

| # | Pattern | Source says | Rows | How the skill uses it |
|---|---|---|---|---|
| 1 | Fix the measure before scoring | ORBIT: milestones specified a priori prevent "moving the target" after the data are in. StaRI: outcomes pre-specified, with any pre-determined targets documented. | TM57 ([PAPER] ORBIT, DOI 10.1037/hea0000161); TM118 ([PAPER] StaRI, DOI 10.1136/bmj.i6795) | The person writes the received rule, the period and any target before the score is run (A1). A rule changed after scoring is a new rule with a new date |
| 2 | Count against what was due | RE-AIM computes reach on a valid denominator of eligible people, not volunteers who expressed interest; adoption is the percent of settings approached. | CS27, CS28 (re-aim.org) | Default offered: score every handoff due in the period plus earlier ones still open, not only those someone reported. Never drop an open item |
| 3 | Timeliness is one dimension of execution quality | CFIR 2009: quality of execution may consist of fidelity to plan, intensity, timeliness of task completion and engagement of key people. | CS9 ([PAPER] CFIR 2009, DOI 10.1186/1748-5908-4-50) | Lateness is reported as one dimension, not as a verdict on the team |
| 4 | Receipt means complete receipt | BfArM confirms receipt of a complete application within 21 days. | PL94 | Analogy only: a regulator counts a complete set received, not a set sent. Supports the default "received by the named receiver, not a message sent" |
| 5 | Keep critical items apart | ICH E8(R1): critical-to-quality factors are attributes whose integrity is fundamental to participant protection and reliable results. | CV29 | The person marks which handoffs carry a CTQ factor; the score reports them separately, never merged with the rest |
| 6 | Report against an agreed profile | NICE ESF standard 16: usage reported against an expected usage profile agreed at commissioning. | CS61 | Analogy only: a handoff score is read against the profile the teams agreed, not against an outside benchmark |
| 7 | Feed results back | ERIC audit and feedback: collect and summarize performance data over a specified period and give it to the people involved to monitor, evaluate and modify. | CS44 ([PAPER] ERIC, DOI 10.1186/s13012-015-0209-1) | The score goes back to the functions whose handoffs it counts, for the period it names |
| 8 | A documented assessment is the received record | Multiple function impact assessments are performed and documented as design validation, and are inspectable. | PL25 | For this kind of handoff, "received" can be tied to the documented assessment in the design file, if the person chooses |

## 2. The person's rules (not sourced)

- The received rule. Default offered from the old framework: "received by the named receiver, not a message sent". The person confirms or rewrites it.
- The period scored, and whether items due earlier and still open are carried in.
- What "late" means (any day after due, or a grace the person sets).
- The categories (the old framework separated "a late clinical evidence handoff from a late copy handoff") and the CTQ marks.
- Any score formula beyond counts, any target, any threshold for action.
- Who owes each repair, the blocked decision, and the date to look again.

## 3. What a score is not

- A count of received, late and open handoffs is not a measure of a team's quality or a person's performance.
- A score is not evidence that a product is safe, effective or compliant, and not evidence about the cause of any public event.
- "Not measurable" is its own result. A handoff without a due date, a named receiver or a named recipient of the work is shown as not measurable `[GAP]` and kept out of the measurable denominator, never counted as received. A missing named receiver makes the handoff not measurable whether it is open or has arrived; `scripts/handoff_log.py` checks it before open or received and prints a question for the person. The answer asks who receives it and does not rule.
