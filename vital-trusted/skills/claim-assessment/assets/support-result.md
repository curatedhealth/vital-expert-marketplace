# Output format: fact-check result (Part B)

What the person sees. Plain language, no rule or pattern ids (TR-H13). Sized to the
stakes (TR-H12). A VERIFY status word may appear in brackets after the plain words when
the check ran with VERIFY; a manual check uses the manual result words only.

## Full result

```
Fact-check against the passages you supplied (draft, for your review)

<Checked with VERIFY. | Not tool-checked: I compared each sentence with your passages by hand.>
Checked against: <one line per source>

What a match means: the passage you gave says the same thing as the sentence. It does
not mean the sentence is true, that the source is good, or that the work is ready.

Keep (<n>)
1. "<sentence>" — "<quoted words>" (<source, locator>)

Rewrite to match (<n>)
1. "<before>" → "<after>". Your passage says <x>; it does not say <y>.
   <Rechecked with VERIFY. | Rewritten, not tool-checked.>

Removed (<n>)
1. "<sentence>". <Your passage does not say this. | This could not be checked: <reason>.>
   Left out, not replaced.

Ask you (<n>)
1. "<sentence>". Your passage says: "<quote>". Which is right?

For your judgment (<n>)
1. "<recommendation or opinion>". Not something a passage can settle.

Revised text
<the text with keeps and rewrites, removed sentences out, gaps only where you need to
see something is missing>

<If VERIFY is not connected:> VERIFY would test each sentence against its passage;
connect it if this needs to be shown.
<If the work leaves the company:> Next: source quality, the confidence figure and the
record can be added, and this goes through your <kind of review process> before use.

This check flags issues. It is not medical, legal, regulatory or ethics review.
```

## Short result (internal, low stakes)

```
Checked <n> figures, names and quotes against your passage (<with VERIFY | not
tool-checked>): <n> kept, <n> rewritten to match, <n> removed. <One line on the most
important change.> A match means your passage says it, not that it is true.

This check flags issues. It is not medical, legal, regulatory or ethics review.
```
