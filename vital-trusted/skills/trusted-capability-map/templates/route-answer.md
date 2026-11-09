# Output format: routing answer

Plain business language (TR-H13). The person reads what to do next, not the plugin's
internal names. Do not show skill names, letter codes or raw `[GAP: …]` syntax in a
routing or explaining answer. Name a skill only if the person asks which skill to use,
and then in parentheses after the plain description.

No gap marker, even when another skill would give a gapped structure (a pregnancy line
with no leaflet supplied): say it in a sentence instead ("The pregnancy line can only
come from the approved leaflet; send it and I will draft the line from it.").

If any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem, patient-safety's flag comes first, above this answer,
in its template wording (`../../patient-safety/templates/safety-flag.md`) (TR-H14).

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

When explaining a letter instead of routing (two to four sentences; one line when the
person asks for one):

```
<Letter word>: <its question>. <What it covers, in one sentence.> <Where it trips people up: the "fails on its own" example.> [<The nearest neighbor, in one sentence.>]
```

When someone asks what TRUSTED does for their work, use the table "Which letters matter
most, by work type" in `../references/standard.md` (guidance, not a rule). Name all seven
letters, one plain line each, so none is only listed; say which usually matter most for
their work, and that depth follows the stakes:

```
TRUSTED checks your work for seven things, all on unless you turn some off:
- Tangible: <one plain line, tied to their work>
- Rule-compliant: <one plain line>
- Unbiased: <one plain line>
- Safe: <one plain line>
- True: <one plain line>
- Ethical: <one plain line>
- Defensible: <one plain line>
For <their work, e.g. board updates and business reviews>, <letter words> usually matter most: <one plain reason each>.
Depth follows the stakes: a quick internal email gets a light look; anything for a board, payer, doctor or patient, or leaving the company, gets the full check. You do not have to ask for the depth.
<What each needs from you, e.g. "the sources behind the figures".>
TRUSTED supports your company's review processes and never replaces them: <kind of internal process, e.g. "your review for board material" or "your promotional review process"> still decides whether work can be used, and a named person clears it.
```

The line on review processes is always there in this answer, also for internal work
such as board updates: it is what TRUSTED is, not a step for one piece.

No closing statement on routing or explaining answers. The closing statement belongs on
check outputs only (`governance.md`).

## A stamp or footer

When the person asks for a line such as "Reviewed and validated by TRUSTED", decline that
wording in one sentence and give a plain line instead (TR-H3, TR-H5). Whether to mention
AI help follows their AI use policy.

```
I can't add "<the wording asked for>": TRUSTED flags issues, it does not review or validate work, and no one has cleared this yet. A line you could use instead:
Drafted with an AI assistant. <Uncleared draft | Cleared by <name>, <role>, <date>>.
```
