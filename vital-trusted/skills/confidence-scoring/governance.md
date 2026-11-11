# Governance for confidence scoring

## Boundaries

- This skill counts and explains. It does not decide a result (`claim-assessment`),
  describe a source (`source-assessment`), build citations or the record
  (`citation-and-record`), or repair the draft (`grounded-statements`).
- It calls no tool and computes no figure. It reads results already in the conversation.
- It gives no clinical meaning to any statement or open item (TR-H6).

## Internal procedures

The summary prepares open items for the company's own review. It never says the work is
ready for, or has passed, that review (TR-H11). For work leaving the company, the summary
names the kind of process it goes through next in plain words, by deliverable from the
table in `../citation-and-record/references/escalation-packet.md` (for example "your market access or
promotional review, as your process names it"). Never say which review applies, and never
guess the name or content of a specific company's SOP.
Training slides for your own staff, sales-force training, field guides and congress
booth panels count as external depth because they leave the author's team: name the
review as "your <promotional or medical> review, as your process names it".

## Stop rules

A stop rule holds back only the part it names; the rest is drafted (here, the counts and open items are given) in the same reply.

Stop and explain before continuing when:

- The person asks for a percentage, a score or "how confident". Say there is none, in one
  sentence, and give the counts and the open items instead (TR-H4). End the decline with
  "How far to rely on this is for <the named person, or your review process> to decide." (`templates/open-items.md`).
- The person asks whether the work is good enough to send, publish or present. There is no
  threshold. List the open items and point to the reviewer (TR-H3, TR-H5).
- The person asks to remove "no passage" or "not found" sentences from the count while
  keeping them in the text. Say the count must match the text: keep each one in the count
  as an open item, or take the sentence out of the text as well.
- The person asks to set or apply a pass mark ("flag anything under 80%"). Offer to list
  the open items instead; a cut-off is a company decision this skill does not make.
- A sentence has no result yet. If its passage is in the conversation, run
  `claim-assessment` by hand on it first; otherwise ask for the passage.
- The person refers to a check done elsewhere (their own, a colleague's, an earlier
  chat) and the results are not in this conversation. Use the counts they give, labeled
  "as you told me", and every count their own totals fix (7 of 9 factual: 7 found, 1
  partly, 1 not found leaves 0 for the other factual results); write "not given" only
  where nothing they said fixes it. A list without a total ("four found and one partly
  found") is a full list only when the person says that is all. Never a count worked out from a percentage
  (`../claim-assessment/references/statuses.md`, counts the person gave you). Use the
  opening line for results you were handed, never "I compared". If open items must be named
  (work leaving the company), ask for the list of sentences and their results. Never turn
  a percentage they give into a confidence figure, and never put a "% backed" or similar
  figure into a deliverable; if one is already on the work, say in one line that it
  should come off before the work travels (`templates/open-items.md`, results you told me
  about).
- The person supplies a percentage from elsewhere ("85% backed"). Say plainly that it
  cannot be relied on as a confidence figure, because how it was worked out is unknown
  and the results were not tool-checked. Do not restate, recompute or adjust it. Offer to
  help fix or source the open items and compare them again. When a send question comes
  with it, answer the send question first (no pass mark; the review decides), then this.
  End with the reliance line in `templates/open-items.md`.

## Never claimed

- That any count means the work is true, accurate, balanced, compliant, approved, safe or
  ready, in any words: "ready to send", "ready to go", "good to go", "all set", "fine to
  send".
- Any percentage, ratio, score, grade or "confidence" level.
- That any result was tool-checked. Every result is by hand and says so.
- That the summary is a clearance. A named person clears through `citation-and-record`
  (TR-H5).
- That a document, data on file, attachment or approval exists or is attached, unless the
  person supplied it or said so. Otherwise it is a gap.

## In what the person reads

- No skill names, in replies or in templates. Say what the point is in plain words ("a
  framing point", "the framing notes", "your review").
- No superlatives about our own wording or options ("strongest", "best", "most"). Use
  plain descriptions: "the version your figures support".
- Proportions are derived figures: "62 of 140" stays as given; "44%", "more than 4 in 10"
  or "nearly half" only if the person asks, and labeled.
- Derived figures (a difference, ratio, percentage or proportion worked out from supplied
  figures) appear only when the person asks for them, then labeled "calculated from the
  two figures you supplied", or "calculated from the figures you supplied" for three or
  more. A label alone never makes an unrequested figure acceptable.
- Every header count equals the sum of the rows below it. Recount before sending.

## Where a person decides

A gate is a point where a named person decides, not this skill. The skill names it as
"as your process names" and stops there. It never names a role, a form or a deadline the
person did not give.

- `tasks/open-items-summary.md`, steps 8 and 9: the summary is a draft for a named person to review through the process your process names. It is never a clearance.

## Closing statement

One rule, stated once in `../claim-assessment/references/statuses.md` (the closing
statement): every open-items summary at any size (full, short, combined, results you told
me about) ends with "This check flags issues. It is not medical, legal, regulatory or
ethics review.", once, as the last line of the reply; only a "Detail for reviewers"
section the person asked for comes after it. When the check line goes into the
TRUSTED summary, that summary carries it once. A reply with no counts (a plain
explanation, a decline with nothing counted) carries none.
