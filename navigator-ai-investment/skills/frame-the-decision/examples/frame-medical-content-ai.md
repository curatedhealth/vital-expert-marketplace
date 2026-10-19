# Worked example: "We want to use AI agents to write our medical content. Where do we start?"

A constructed example, shown so the model sees the shape of a good session and report. The people, answers and scores are illustrative, not a real client. The value themes are the catalogue's real active themes as read on 19 October 2026. The size was computed with `scripts/sizing_check.py` (the connector's allowance was used up when this example was written; replace with a live run). [CHECK on first live test]

## The session (turns condensed)

**Turn 1 (assistant).** We'll frame this as one decision in three steps: the decision, the goal behind it, and how big it is. About eight short questions. Your wording names a tool (AI agents), so I'll turn it into a decision with the tool as one option. Step 1 of 3. Who takes this decision, and who will be in the room?

**Person.** The Chief Medical Officer decides. I'm Head of Medical Excellence; the heads of Medical Information and Medical Compliance will join.

**Turn 2.** Recorded: the Chief Medical Officer owns it; C-suite plus two department heads (O). I'll pitch it at C-suite level. Step 1 of 3. Proposed wording: "The Chief Medical Officer decides whether, and where, AI should change how medical content is produced across Medical Affairs, before the next budget cycle." Accept or edit?

**Person.** Accepted.

**Turn 3.** Recorded. Step 1 of 3. What would a wrong call cost?

**Person.** If AI-written content goes out wrong we have a compliance problem; if we wait, we keep spending about half of our writers' time on routine updates.

**Turn 4.** Recorded (O). Step 1 of 3. What do you already know, and how do you know it?

**Person.** Writers spend roughly half their time on routine updates, that's our estimate. Two vendors have pitched. No pilot yet.

**Turn 5.** Recorded: the half-time figure is a team estimate (O), not measured. Step 2 of 3. Which strategic goal does this serve, in one sentence?

**Person.** Medical Affairs should be the trusted, fast source of medical information for clinicians.

**Turn 6.** Recorded (O). Step 2 of 3. Closest value themes in the catalogue: *Establish Scientific Authority & Shape Clinical Practice* (strategic), *Earn the Trust of Investors, Patients, Regulators & Society* (strategic), *Drive Operational Excellence & Reduce Cost-to-Serve* (operational). Which fits, if any?

**Person.** The first.

**Turn 7.** Recorded: chosen by the Chief Medical Officer. Step 3 of 3. Please send this sheet to the three of you; score alone, before discussing. [score sheet]

**Person.** [returns three sets of scores]

**Turn 8.** Recorded. Step 3 of 3, last question: is this decision hard to reverse, and does it commit money or people beyond one planning cycle or across functions? (Reversibility scores 4, 6, 2; horizon 7, 5, 7; functions 6, 5, 8.)

**Person.** Yes to both.

## The full report

**Summary.** The Chief Medical Officer decides whether, and where, AI should change how medical content is produced, in service of making Medical Affairs the trusted, fast source of medical information for clinicians. The decision is sizeable (6.9 of 10), hard to reverse and cross-functional, which points to a one-day session with the full record. The top outcomes will need a short field check before the decision.

**1. The decision.** Statement as accepted by the Chief Medical Officer (above). Original wording: "We want to use AI agents to write our medical content." Options on the table: AI agents for content production; do nothing; improve the process internally. Reversibility: hard to reverse (owner, O).

**What it will turn on (H).** Is there a measured baseline of writer time and error rates? Is the bottleneck drafting, or medical and compliance review? Who owns the promotional and medical accuracy checks for AI-assisted content?

**2. Strategic goal.** "Medical Affairs should be the trusted, fast source of medical information for clinicians" (O). Value theme: *Establish Scientific Authority & Shape Clinical Practice*, chosen by the Chief Medical Officer.

**3. What a wrong call costs.** Compliance exposure if AI-assisted content goes out wrong; continued loss of about half of writers' time if nothing changes (O). The money range is set in *Value-at-Stake Sizing*.

**4. Size of the decision.**

| Criterion | Group view | Range | Owner's view |
|---|---|---|---|
| Stakes | 8 | 7 to 9 | 8 |
| Reversibility (10 = easy to reverse) | 4 | 2 to 6 | 4 |
| Commitment horizon | 6.3 | 5 to 7 | 7 |
| Functions involved | 6.3 | 5 to 8 | 6 |
| **Composite** | **6.9** | | 7 |

Scorers: Chief Medical Officer, Head of Medical Information, Head of Medical Compliance. Widest disagreement: reversibility (Compliance sees it as much harder to undo than Medical Information); discuss before the session. Points to: one decision that matters, several functions, costly to reverse: a one-day session with the full record; the owner chooses. Field-test questions: hard to reverse, yes; wide commitment, yes (owner, O). The top outcomes need a short field check unless the owner records a reason to proceed without it.

**5. What is known.** About half of writers' time on routine updates (O, team estimate). Two vendors have pitched (O). No pilot run (O).

**Gaps.** `[GAP]` No measured baseline of time or error rates; needed to size the value. `[GAP]` Whether Regulatory and Legal join the session is not decided.

**6. Record.** Draft prepared with an AI assistant, 19 October 2026. Accepted by the decision owner: yes. Uncleared. Navigator brief: not opened (connector unavailable).

## Why this is good

Each turn asks one thing and says what was recorded. Nothing is drafted mid-session. The person never has to repeat themselves. The report stands alone: a reader who missed the session sees the decision, why it matters, how big it is, what it will turn on, and what is still missing.
