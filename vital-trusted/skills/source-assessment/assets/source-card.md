# Output format: source card

What the person reads, one card per source. Plain language, no rule ids or pattern ids
(TR-H13). "What it can carry" and "What it cannot carry" are always present. Never a
verdict word (TR-H3).

## Full card (anything leaving the company)

```
Source: <title or description as the source shows it>, <issuer or authors>, <date in full, or "date not shown">
Identifier: <DOI, PMID, document number or link as supplied, or "none supplied">

What it is: <kind, e.g. "a company press release", "a preprint", "a peer-reviewed trial publication">
Peer review: <peer reviewed | not peer reviewed | status not confirmed: what would confirm it>
Who made it: <authors or issuer>; funded by <as disclosed, or "not stated in the source">; <interests, as disclosed>
Fits your question: <which of population, comparison, outcome, setting match, and which do not>

How strong: <design as the source states it>; <one study | several studies that agree | several that disagree>
Up to date: <date>; <retraction or correction status: as VERIFY returned it, or "not checked">; <for guidance or labels: newer version known / asked / not checked>

What it can carry for <reader>: <the narrowest true statement it supports>
What it cannot carry: <what it should not be used to say>

To use it: <what would close the gap, e.g. "the published article", "the event rates", "the 2026 version">
Next step: this goes through your <kind of review process> before it is used.

<"Not tool-checked." or the VERIFY block from assets/verify-block.md>
```

## Short card (board, leadership, internal brief)

```
<Source, date>: <what it is>; <peer review status>; <who made it, if it matters>.
Can carry: <one line>. Cannot carry: <one line>. <Not tool-checked | VERIFY block>
```

## One line (quick internal note)

```
<Source> is <kind>, <date>; it can be mentioned as <what it can carry>, not as <what it cannot carry>.
```

## When the person asked for a verdict

Open with one sentence that reframes, then the card:

```
I can't tell you whether it is good enough; your <review process> decides that. Here is
what it can and cannot carry for <reader>, so you can decide where to use it.
```

## On a check output for a reviewer

End with the closing statement from `references/governance.md`.
