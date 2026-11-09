# Output format: full TRUSTED summary (work leaving the company)

Sits after the deliverable. Plain language: letter words, no codes, no skill names, no
gap syntax (TR-H13). Counts and notes, no verdicts (TR-H3).

```
[Only if any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem, first, before everything else (TR-H14), in the wording of `../../patient-safety/templates/safety-flag.md`:]
Before anything else: something to pass to your safety reporting procedure
<Source line: who reported it and the setting, e.g. "A nurse at Hillcrest clinic, in Dr. Weber's email of 14 October 2026"> mentions:
- "<exact words from the input, without patient identifiers>" (<product name and strength, as given>): <kind in plain words>
Please pass this to your safety reporting procedure as soon as you can, in the time it sets. Forward the original <email | notes | transcript> as received (for a post: send a screenshot or link); your safety procedure decides what personal details it needs.
<Fixed sentence for what was reported, from the safety-flag template; for an event: "I have not judged whether it is related to <product>, how serious it is, or whether it needs reporting. Your safety team decides that, and they will follow up for any detail that is missing." A defect with no patient event has no "whether it is related" sentence.>

TRUSTED check: <what the draft is>, for <reader>. <record status, one of the forms below>.

[Only if the person asked "is it OK to send" or similar:]
Before it goes, fix these <n> things. <Kind of internal process> decides whether it can be used.
[If n is 1:] Before it goes, fix this 1 thing. <Kind of internal process> decides whether it can be used.
[If nothing was flagged, instead:] Nothing flagged in what was checked. <Kind of internal process> decides whether it can be used.
[If nothing else was flagged but the safety flag was given:] Nothing else flagged in what was checked; the safety item above goes to your safety reporting procedure. <Kind of internal process> decides whether it can be used.

Tangible        <count in plain words | nothing flagged in what was checked | not checked: why | off by choice>
                <note: where and what>
Rule-compliant  ...
Unbiased        ...
Safe            ...
True            ...
                [If sources were supplied:] Compared by hand with your sources (not tool-checked): <n> factual claims: <n> found in your passage, <n> partly found, <n> not found in your passage, <n> your passage says something different, <n> no passage to compare with.
                [If any:] Listed separately, not in the total: <n> opinion, recommendation or definition.
                [If sources were supplied:] No confidence figure: these results were not tool-checked. Found in your passage means the passage says it, not that the statement is true.
Ethical         ...
Defensible      record: <n> materials, <n> assumptions, <n> open items (<n> without an owner); <record status, one of the forms below>
                [If a formal record was written:] Formal record written by hand: <n> sources, <n> open items, <n> handed on to a review process; <record status, one of the forms below> (not tool-checked)

Open for a person
1. <item>. <Who decides, if not you.>
2. ...

Could not be checked
- <check>: <why, e.g. "no sources were supplied; a hand check would compare the 3 figures with them">
- <check>: <why, e.g. "no approved label was supplied">

Next step: this goes through your <kind of internal process> before it is used.

[If reference lines were written: the reference lines, then the recommendation from the open-items summary.]

This check flags issues. It is not medical, legal, regulatory or ethics review.
```

Status forms, and only these (TR-H5): "Uncleared draft"; "Uncleared draft, reviewed by
<name>, as you told me"; "Cleared by <name>, <role>, <date>". A placeholder for a clearance still to come is "Uncleared draft (to be cleared by <name>, <role if given>)", or "Uncleared draft (to be cleared by a reviewer not named yet)" when no name is given. A clearance the person reports in the past without role or date is "Uncleared draft (you said <name> cleared it; add role and date to record the clearance)".

The safety flag at the top follows TR-H14: it comes before the rows whatever letters are
active. It is not repeated elsewhere in the summary: not under "Open for a person", not
in "Next step", not in another letter's notes. When Safe is on, its row gives the count
with the note "see the flag above" ("1 safety mention: see the flag above"). The flagged
sentence is not counted or noted under any other letter, and is not in the header totals.

Count wording:

| Situation | Write |
|---|---|
| Something to change in the draft | "<n> to fix" |
| Something the person must supply | "<n> missing" |
| Something only the person or a process can decide | "<n> question(s) for you" or "for <process>" |
| Checks ran and found nothing | "nothing flagged in what was checked" |
| Check could not run | "not checked: <why>" |
| Letter turned off | "off by choice" |
| Already counted under another letter | "see <letter> above" (no count) |
| A safety mention that got the flag | "<n> safety mention(s): see the flag above" (not in the header totals) |

Keep notes to one line each, at most three per letter. If a letter has more, give the
count and the three that matter most to the reader.

Each finding is counted once, in one row. Every header count equals the sum of the rows
below it: "fix these <n> things" is the sum of the "to fix" counts, "supply <k> missing
items" the sum of the "missing" counts, "answer <q> questions" the sum of the questions.
Recount before sending.
Wrong: header "fix these 3 things", rows 2 + 1 + 1 to fix. Right: header "fix these 4
things", or count the shared finding in one row and write "see <letter> above" in the
other.

Figures in notes and suggested fixes: both figures as the person supplied them, never a
difference or proportion worked out from them unless the person asked, and then labeled
"calculated from the two figures you supplied" ("calculated from the figures you
supplied" for three or more). A label alone never makes an unrequested figure acceptable.
Wrong: "Unbiased: 1 to fix. Say the response rate rose 15 points." Right: "Unbiased: 1 to
fix. Say the response rate rose from 22% to 37%, the two figures you give."

The closing statement is the last line of the reply, with one exception: a "Detail for
reviewers" section the person asked for (raw lines or a per-claim table) comes after
it. An offer or a question goes above it, inside the summary.
