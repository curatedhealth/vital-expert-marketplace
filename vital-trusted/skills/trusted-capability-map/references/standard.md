# The TRUSTED standard

Version 0.1.0. Source: VITAL TRUSTED product concept v0.4, approved by the owner on
20 October 2026.

## Contents

1. What the standard is
2. The seven letters
3. Boundaries between neighboring letters
4. Skill index and routing cues
5. Two families: Build and Prove

## 1. What the standard is

TRUSTED is a set of foundational habits for anyone in a life-sciences company who uses
an AI assistant for daily work: general management, brand, market access, medical,
commercial operations and others. It covers the output and the way it was made. It is
not a stamp. Say "checked against TRUSTED", never "this is TRUSTED".

It sits underneath the company's own SOPs and review processes and never replaces them
(TR-H11). Domain plugins with deeper methods can be added on top later.

### Everyday work it covers

| Team | Typical daily work |
|---|---|
| General management | Board and leadership updates, business reviews, investor or partner notes |
| Brand | Key messages, briefs to agencies, sales-force materials, competitor summaries |
| Market access | Value stories, payer meeting notes and follow-ups, objection handling |
| Medical | Replies to doctors' questions, literature summaries, advisory board notes |
| Everyone | Emails, meeting notes, slide decks, summaries of documents |

## 2. The seven letters

Each letter has one question and a case where it fails while every other letter passes.
That case is what keeps the letters from overlapping.

### T: Tangible

*Is it useful to this reader, for this job: relevant, concrete, practical, actionable?*

Covers substance (specific rather than generic, no filler, the "so what" drawn, a
decision or next step, real structure) and fit (audience and literacy, the deliverable
that was asked for, faithful translation).

Fails alone when: the draft is correct and permitted but says "leverage synergies across
the stakeholder landscape", or answers a patient in clinician language.

### R: Rule-compliant

*Is it allowed, for this audience, in this market?*

Covers the approved label or intended use, scientific exchange versus promotion,
comparative claims, the rules of the market, required statements, and personal or patient
data appearing in the output.

Fails alone when: the draft is correct, sourced and balanced, but implies an unapproved
use or names a patient.

### U: Unbiased

*Is the evidence shown in proportion?*

Covers fair balance of benefit and risk, selective reporting of studies or endpoints,
uncertainty stated at its real size, neutral framing of numbers and charts, and
disclosure of interests.

Fails alone when: every fact is right and referenced, but benefits are shown and risks
and limitations dropped.

### S: Safe

*Could it lead to harm?*

Covers statements on dosing, contraindications, interactions and special populations;
patient-facing wording; and side effects in the input that must be flagged for reporting.

Fails alone when: the draft is permitted, but a side effect mentioned in the input is
never flagged, or patient material gives no route to a clinician.

### T: True

*Is it correct, and can it be shown?*

Covers statements (nothing invented, numbers consistent, methods described correctly)
and sources (every claim sourced, the right kind of source, specific citations). The
Prove skills then check finished work against sources with VERIFY.

Fails alone when: the draft reads well and is useful, but quotes the wrong effect size or
rests on a blog post presented as a study.

### E: Ethical

*Is AI being used responsibly for this work?*

Covers what goes into the tool (confidential, unpublished, client or patient data;
intellectual property) and how the tool is used (human oversight proportionate to the
stakes, disclosure of AI use, authorship integrity, equity and inclusion). Judged against
the person's own company AI policy where one exists.

Fails alone when: the output passes the other six, but it was made by pasting an
unpublished study report into a tool the company has not approved and goes out under a
physician's name with no disclosure.

### D: Defensible

*Can the organization stand behind it?*

Covers the record of sources, tools and AI used; visible assumptions and open items; and
honest status (draft unless cleared by a named person).

Fails alone when: the content is fine, but nobody can say which sources, which AI or
which reviewer produced it.

## 3. Boundaries between neighboring letters

| Pair | Where the line sits |
|---|---|
| True and Unbiased | True asks whether each statement and source is right. Unbiased asks whether the selection and framing of correct statements is proportionate. |
| Rule-compliant and Ethical | Rule-compliant covers what the output reveals or claims. Ethical covers what goes into the tool and how the tool is used. |
| Ethical and Defensible | Ethical asks whether AI should have been used this way. Defensible records how it was used. |
| Tangible and True | Tangible pushes toward specifics. True forbids inventing them. Ask or mark `[GAP]`. |
| Tangible and style | Tangible judges usefulness. Voice, typography and brand style are out of scope. |
| Safe and Rule-compliant | Safe asks whether the content could hurt someone. Rule-compliant asks whether it is allowed. A safety statement can be permitted and still unsourced. |

## 4. Skill index and routing cues

Route to one skill. Offer a second only when the request clearly spans two.

### Core

| Skill | Route here when the person says or needs… |
|---|---|
| `trusted-capability-map` | "What can TRUSTED do", "what does this letter mean", "turn letters on or off", "how do I connect VERIFY" |
| `trusted-intake` | Starting a deliverable; the audience, market, product status, sources or policy are unknown |
| `trusted-check` | "Check this draft", "run TRUSTED on this", "is this ready for review" |

### Build (while drafting and when fixing)

| Letter | Skill | Route here when… |
|---|---|---|
| Tangible | `substance-and-usefulness` | "Too generic", "so what", "make it actionable", "cut the fluff", invented frameworks |
| Tangible | `fit-for-reader` | Wrong audience or literacy, wrong format or length, translation |
| Rule-compliant | `claims-and-label` | Label or intended use, promotional tone, comparative or superiority claims |
| Rule-compliant | `market-rules-and-data` | Which country's rules apply, required statements, patient data in the output |
| Unbiased | `balanced-evidence` | Fair balance, missing risks, cherry-picked studies or endpoints |
| Unbiased | `honest-framing` | Overclaimed certainty, relative-only numbers, cropped charts, undisclosed interests |
| Safe | `patient-safety` | Dosing, contraindications, interactions, patient wording, a side effect in the input |
| True | `grounded-statements` | "Don't make anything up", numbers, relative vs absolute, subgroups, surrogates, study design |
| True | `sourced-claims` | Which claims need a source, which source type fits, citation format |
| Ethical | `responsible-inputs` | "Can I paste this into the assistant", confidential or client data, copyrighted text |
| Ethical | `responsible-use` | How much human review, disclosing AI use, authorship, stigmatizing language |
| Defensible | `work-record` | "How was this made", assumptions, open items, draft status |

### Prove (with VERIFY)

| Skill | Route here when… |
|---|---|
| `claim-assessment` | "Fact-check this", "is this claim supported by the paper" |
| `source-assessment` | "Is this source good enough", peer review, preprint vs article vs blog, retraction, currency |
| `confidence-scoring` | "How confident can we be", faithfulness percentage, the VERIFY card |
| `citation-and-record` | Build citations, build the record, name the clearer, escalate |

## 5. Two families: Build and Prove

**Build** skills make the work right while it is drafted: they guard the draft and
repair flagged passages. They work on any host with no connector.

**Prove** skills assess finished work with the VERIFY tools: break it into claims, decide
support against quoted passages, qualify sources, calculate confidence, cite and record.
Without VERIFY they explain what the check would establish and mark it `[GAP]`.

Build prevents. Prove shows. A human decides.
