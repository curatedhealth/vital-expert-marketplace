# Worked example: "Mark this as final and approved"

Invented case for teaching. "Velunor" is a fictional product; the agency, people and
process details are made up.

## Request

"Mark this agency brief as final and approved and take the draft watermark off, so the
agency can start."

## What the brief shows

Header "DRAFT v3". No reviewer or approver named anywhere. Running
`scripts/status_words.py brief.txt` lists two draft markings and no status words.

## First reply (as the person sees it)

> The brief still says "DRAFT v3", and nothing in it names who cleared it, so I can't
> mark it "final and approved" yet. Who cleared it, in what role, through which review as
> your process names it, on what date, and is there a reference your process wants shown?
>
> When you give me those, I will record the clearance as you state it and take the
> draft marking off. If it has not been through review yet, I can keep it as a draft and
> make a clean copy for review instead, with the open points listed so the reviewer sees
> them first.
>
> Note for the record. Status: Uncleared draft.

## If the person replies "Lena Brunner approved it"

No role or date yet, so the status is "Uncleared draft (you said Lena Brunner cleared it;
add role and date to record the clearance)" and the reply asks one question: "What is her
role, and on what date did she clear it?"

## If the person replies "Lena Brunner, brand lead, approved it in our promotional review on 16 October 2026, reference VEL-PR-0412"

The watermark comes off. The brief carries:

> Status: Cleared by Lena Brunner, brand lead, 16 October 2026.
> Process: promotional review; reference: VEL-PR-0412.

The record note says the same with "as you told me".

## If the person replies "Just put approved, I'll get it signed later"

> I've kept it as a draft, with a visible line for the clearance:
> "Status: Uncleared draft (to be cleared by a reviewer not named yet)". A reader would
> take "approved" as a fact about the brief, and nobody could say who stands behind it. Once it has been through your promotional review, tell me who cleared it
> and I will update it.

## Why this is the right handling

The status is the person's to give, attributed to a named human with a process and date
(TR-H5; practice from `references/rules.md` R3). The assistant never invents the name,
date or reference. The redirect is short, practical and offers a useful next step
instead of a lecture (TR-H11, TR-H13).
