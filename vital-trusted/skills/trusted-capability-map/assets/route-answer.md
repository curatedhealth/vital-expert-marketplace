# Output format: routing answer

Plain business language (TR-H13). The person reads what to do next, not the plugin's
internal names. Do not show skill names, letter codes or raw `[GAP: …]` syntax in a
routing answer. Name a skill only if the person asks which skill to use, and then in
parentheses after the plain description.

```
<One or two sentences on what the person needs, in their words.>

What I'd do first: <the first step, described plainly, e.g. "check who the reply is for
and which market, because that changes what can be said">
Then: <the next step, e.g. "keep every dosing statement exactly as the label puts it">
[And: <a second concern only if the request clearly spans two>]

<If the work leaves the company:> After that it goes through your <kind of internal
process>, which decides whether it can be used.

<One line offer, e.g. "Want me to start on the draft?">
```

When something must be decided by someone else, say it in a sentence ("Your AI use
policy owner decides whether this tool can take unpublished data"), not as a gap marker.

When explaining a letter instead of routing:

```
<Letter word>: <its question>

What it covers: <one or two sentences>
Where it trips people up: <the "fails on its own" example>
Not to be confused with: <the nearest neighbor, in one line>
```

No closing statement on routing or explaining answers. The closing statement belongs on
check outputs only (`references/governance.md`).
