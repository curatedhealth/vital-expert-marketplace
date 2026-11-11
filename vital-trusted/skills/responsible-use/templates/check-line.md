# Output format: check lines for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts, states and questions only; no verdict words
(TR-H3, TR-H13).

One line per task, in the grammar of `../../trusted-check/references/letter-lines.md`. No value reads as a verdict or as a decision on the company's policy.

```
Ethical · human review: stakes <internal | leadership | leaving the company>, reviewer <named as you gave it | not named>, <n> requests to send without review (not tool-checked)
Ethical · disclosure and authorship: AI use disclosure <present | not present>, expected by <your policy as you stated it | the venue's rules | not known: question asked>, <n> authorship questions (not tool-checked)
Ethical · inclusion: <n> phrases that could stigmatize or exclude, <n> changed, <n> questions on preferred terms, <n> evidence gaps for groups named from your material (not tool-checked)
```

Each line may carry up to three plain notes:

```
  - <e.g. "reply to a doctor; no reviewer named yet">
  - <e.g. "article for an external expert to sign; writing support not yet acknowledged">
```

When the work was internal and quick and nothing applied, return no line.

When the person stated their policy:

```
Ethical · disclosure and authorship: AI use disclosure <present | not present>, expected by your policy as you stated it: <their words, short> (not tool-checked)
  - policy as stated in the conversation; not compared with the policy text
```
