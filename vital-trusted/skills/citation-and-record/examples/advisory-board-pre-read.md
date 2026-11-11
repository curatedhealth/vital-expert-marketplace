# Worked example: references and record for an advisory board pre-read

Invented case for teaching. "Velastrin Connect", "Northvale Therapeutics", the papers,
the authors and the people are fictional. No tool was called. The claim results below are
fictional inputs standing in for what `claim-assessment` returns by hand, in the six
hand-check words.

## Request

A medical lead, Priya Shah, writes: "Here's the two-page pre-read for the
external advisory board on Velastrin Connect. Build the references from the three
sources below and build the record. Clear it, it needs to go to the agency for
layout."

Sources supplied:

1. Ferreira L, Haddad S, Moreno T. "Remote monitoring with Velastrin Connect in adults
   with condition X: a randomized trial." Journal of Fictional Medicine, 2025, 12(3),
   201-210. doi:10.0000/jfm.2025.0123
2. Okafor A, Lind M. "Home visits after one year of Velastrin Connect: registry
   results." Fictional Society Annual Congress abstract. https://example.org/abstracts/417
   (no year given)
3. "Velastrin Connect instructions for use", Northvale Therapeutics, 2026.
   https://example.org/velastrin/ifu

Earlier in the conversation, `claim-assessment` compared the pre-read's eight factual
claims with their passages by hand. Fictional results for teaching: six found in your
passage, one partly found and one where your passage says something different.

- Claim 4: "Velastrin Connect halved home visits." Passage (source 2, results):
  "home visits fell from 4.1 to 3.2 per patient-year".
- Claim 7: "No device-related adverse events were reported." Passage (source 1,
  safety): "two device-related adverse events (skin irritation) were reported in the
  monitoring arm".

## Depth

External advisory board, going to an agency: leaving the company. Full record, open
items handed on, pointer to the internal process (TR-H12, TR-H11).

## Step 1: references

No style named, so the lines are plain and in one order. This is the actual output of
`scripts/plain_reference.py` for these three sources:

```
1. Ferreira L, Haddad S, Moreno T. Remote monitoring with Velastrin Connect in adults with condition X: a randomized trial. Journal of Fictional Medicine. 2025;12(3):201-210. doi:10.0000/jfm.2025.0123
2. Okafor A, Lind M. Home visits after one year of Velastrin Connect: registry results. Fictional Society Annual Congress. Abstract. https://example.org/abstracts/417
3. Velastrin Connect instructions for use. Northvale Therapeutics. 2026. https://example.org/velastrin/ifu

Missing from what you gave me:
  Source 2: year

Reference lines built from the details you gave; not tool-checked.
```

Note to the person, after the list: "The Okafor and Lind abstract has no year in what
you gave me; I left it out. Add it from the congress program if you have it. Source 2 is
a congress abstract; if the full paper is published, citing it is usually preferred."
No access date was added to any line.

## Step 2: the record

Priya asked to "clear it". She is a named person and can clear, but two claims do not match
their own passages, and the pre-read goes outside the company. The skill does not suggest
clearing them. It hands them on and asks for her decisions.

What Priya sees:

> Uncleared draft (to be cleared by Priya Shah, Medical Lead)
>
> What this covers: Velastrin Connect advisory board pre-read, two pages
> Sources: 3, in the reference list
> Factual claims compared with their passages by hand: 8 (not tool-checked; counts only)
>   6 found in your passage
>   1 partly found
>   0 not found in your passage
>   1 your passage says something different
>   0 no passage to compare with
> Listed separately, not in the total: 0 opinion, recommendation or definition
> Found in your passage means the passage says it. It does not mean the claim is true in
> the world.
>
> Open item 1: home visits
> Where: page 1, second paragraph
> What the text says: "Velastrin Connect halved home visits."
> What the source says: "home visits fell from 4.1 to 3.2 per patient-year" (Okafor and
> Lind abstract, results)
> Why it is open: partly found: "halved" not in your passage. Your source gives 4.1 and
> 3.2 per patient-year; the text's "halved" does not match those figures.
> Question: Use the passage's figures, remove the sentence, or send it to your medical
> review process?
> Goes to: your medical review process
> Decision: not yet made
>
> Open item 2: device-related adverse events
> Where: page 2, safety paragraph
> What the text says: "No device-related adverse events were reported."
> What the source says: "two device-related adverse events (skin irritation) were
> reported in the monitoring arm" (Ferreira and colleagues, safety results)
> Why it is open: your passage says something different.
> Question: Replace the sentence with what the paper reports, or send it to your medical
> review process?
> Goes to: your medical review process
> Decision: not yet made
>
> Next step: the pre-read and this record go through your medical review process, and
> your promotional review process if your company treats advisory board materials as
> promotional, before the agency lays it out. This record does not replace that review.
>
> Record note written by hand; not tool-checked.

## Step 3: Priya decides

Priya replies: "Use the paper's figures for the visits. Send the adverse event line to
medical review, I don't want to rewrite safety wording myself. I'm clearing the rest. Date
is 9 November 2026."

Every open item now has a decision, and Priya has named herself, with her role and the
date, as the person who reviewed the six sentences. But item 2 is with medical review, and
the text still says something different from its source. So the record stays an uncleared
draft, and it records only the decisions Priya made:

> Uncleared draft (to be cleared by Priya Shah, Medical Lead)
>
> Decisions
> 1. "Velastrin Connect halved home visits": revised to the passage's figures, 4.1 to 3.2
>    per patient-year. Decided by Priya Shah, Medical Lead, 9 November 2026.
> 2. "No device-related adverse events were reported": escalated to your medical review
>    process. Decided by Priya Shah, Medical Lead, 9 November 2026.
> 3. The six sentences found in your passage: Cleared by Priya Shah, Medical Lead,
>    9 November 2026, who reviewed them.
>
> Still open (no decision yet)
> 1. "No device-related adverse events were reported": with your medical review process,
>    so the pre-read is not final.
>
> Next step: this record goes with the pre-read into your medical review process. It does
> not replace it.
>
> Record note written by hand; not tool-checked.

No tool was needed for the name to appear. Priya's own review is what clears the six
sentences, and the escalated item keeps the whole record an uncleared draft until it comes
back. No evidence table: Priya did not ask for one.

## Why this is the right shape

- One reference line per source, missing year named, not filled, no access date added
  (TR-H1).
- "Clear it" did not become a cleared record over two sentences that do not match their
  passages, and the record stays an uncleared draft while one of them is with medical
  review (TR-H5).
- The open items are in plain words with the passage quoted and one question each
  (TR-H13).
- The internal review process is named as the next step, not replaced (TR-H11).
