# Worked example: references and record for an advisory board pre-read

Invented case for teaching. "Velastrin Connect", "Northvale Therapeutics", the papers,
the authors and the people are fictional. The claim results below are fictional inputs
standing in for what `claim-assessment` would return; in a real run they come from
VERIFY, and nothing here shows a VERIFY output that a tool did not return.

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

Earlier in the conversation, `claim-assessment` checked the pre-read's eight factual
claims with VERIFY. Fictional results for teaching: six supported, two contradicted.

- Claim 4: "Velastrin Connect halved home visits." Passage (source 2, results):
  "home visits fell from 4.1 to 3.2 per patient-year".
- Claim 7: "No device-related adverse events were reported." Passage (source 1,
  safety): "two device-related adverse events (skin irritation) were reported in the
  monitoring arm".

## Depth

External advisory board, going to an agency: leaving the company. Full record, open
items handed on, pointer to the internal process (TR-H12, TR-H11).

## Step 1: references

No style named, so `style` is left out. One call per source:

```
build_citation({ "source": { ...source 1 as returned by qualify_source... } })
build_citation({ "source": { ...source 2... } })
build_citation({ "source": { ...source 3... } })
```

Each returned `formatted` line is pasted as the reference, with no caption. Source 2
has no year; nothing is added to its line.

Without VERIFY, the skill runs `scripts/plain_reference.py` on the supplied details.
This is the actual output of that script for these three sources:

```
1. Ferreira L, Haddad S, Moreno T. Remote monitoring with Velastrin Connect in adults with condition X: a randomized trial. Journal of Fictional Medicine. 2025;12(3):201-210. doi:10.0000/jfm.2025.0123
2. Okafor A, Lind M. Home visits after one year of Velastrin Connect: registry results. Fictional Society Annual Congress. https://example.org/abstracts/417
3. Velastrin Connect instructions for use. Northvale Therapeutics (fictional). 2026. https://example.org/velastrin/ifu

Missing from what you gave me:
  Source 2: year
  Source 3: authors

Reference lines built from the details you gave; not tool-built.
```

Note to the person, after the list: "The Okafor and Lind abstract has no year in what
you gave me; I left it out. Add it from the congress program if you have it. Source 2 is
a congress abstract; if the full paper is published, citing it is usually preferred."

## Step 2: the record

Priya asked to "clear it". She is a named person and can clear, but two claims are
contradicted by their own passages, and the pre-read goes outside the company. The
skill does not suggest clearing them. It hands them on and asks for her decisions.

What Priya sees:

> Uncleared draft
>
> What this covers: Velastrin Connect advisory board pre-read, two pages
> Sources: 3, in the reference list
> Claims checked against their passages: 8, with VERIFY
> 6 supported by the quoted passage, 2 contradicted by the passage
> Support means the quoted passage says it. It does not mean the claim is true in the
> world.
>
> Open item 1: home visits
> Where: page 1, second paragraph
> What the text says: "Velastrin Connect halved home visits."
> What the source says: "home visits fell from 4.1 to 3.2 per patient-year" (Okafor and
> Lind abstract, results)
> Why it is open: the passage says something different. 4.1 to 3.2 is a drop of about a
> fifth, not half.
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
> Why it is open: the passage says something different.
> Question: Replace the sentence with what the paper reports, or send it to your medical
> review process?
> Goes to: your medical review process
> Decision: not yet made
>
> To be cleared by: Priya Shah, Medical Lead, once both items have a decision.
> Next step: the pre-read and this record go through your medical review process, and
> your promotional review process if your company treats advisory board materials as
> promotional, before the agency lays it out. This record does not replace that review.
>
> Record written with VERIFY once you decide; until then this is a draft.

`build_record` is not called yet: two open items have no decision.

## Step 3: Priya decides

Priya replies: "Use the paper's figures for the visits. Send the adverse event line to
medical review, I don't want to rewrite safety wording myself. I'm clearing the rest."

Now every open item has a decision and a named clearer:

```
build_record({
  "text": "<the revised pre-read>",
  "claims": [ ...the eight claims as returned... ],
  "findings": [ ...the eight findings as returned... ],
  "sources": [ ...the three sources as returned... ],
  "clearances": [
    { "decision": "revised",
      "cleared_by": { "name": "Priya Shah", "role": "Medical Lead" },
      "time": "<the date Priya gives>",
      "note": "Home visit claim replaced with the abstract's figures: 4.1 to 3.2 per patient-year." },
    { "decision": "escalated",
      "cleared_by": { "name": "Priya Shah", "role": "Medical Lead" },
      "time": "<the date Priya gives>",
      "note": "Device-related adverse event sentence sent to medical review." }
  ]
})
```

Clearance fields other than `cleared_by.name` are `[CHECK]` against the VERIFY schema,
as is whether VERIFY expects one more clearance for the record as a whole (Priya's
"I'm clearing the rest").
The skill reports what `build_record` returned. The escalated item stays visible in the
record; the work still goes to medical review. No evidence table: Priya did not ask
for one.

## Why this is the right shape

- One reference per source, missing year named, not filled (TR-H1).
- "Clear it" did not become a cleared record over two contradictions (TR-H5).
- The open items are in plain words with the passage quoted and one question each
  (TR-H13).
- The internal review process is named as the next step, not replaced (TR-H11).
