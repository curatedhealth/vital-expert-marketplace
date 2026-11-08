# Output format: check lines for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts, states and questions only; no verdict words
(TR-H3, TR-H13).

These follow the shape proposed for this skill in `trusted-check`'s letter-lines
contract, with three wording changes so that no value reads as a verdict or as a
decision on the company's policy. The changes are listed at the end for the owner to
carry into the contract.

```
Ethical · human review: stakes <internal | leadership | leaving the company>, reviewer <named as you gave it | not named>, <n> requests to send without review (asked, not checked: no AI-policy companion)
Ethical · disclosure and authorship: AI use disclosure <present | not present>, expected by <your policy as you stated it | the venue's rules | not known: question asked>, <n> authorship questions (asked, not checked)
Ethical · inclusion: <n> phrases that could stigmatize or exclude, <n> changed, <n> questions on preferred terms, <n> evidence gaps for groups named from your material (not tool-checked)
```

Each line may carry up to three plain notes:

```
  - <e.g. "reply to a doctor; no reviewer named yet">
  - <e.g. "article for an external expert to sign; writing support not yet acknowledged">
```

When the work was internal and quick and nothing applied, return no line, or:

```
Ethical · use: nothing to raise (internal note)
```

When the person stated their policy:

```
Ethical · disclosure and authorship: AI use disclosure <present | not present>, expected by your policy as you stated it: <their words, short> (not checked against the policy text)
```

## Differences from the proposed contract

| Proposed in letter-lines | Used here | Why |
|---|---|---|
| review planned `<in line with | lighter than>` the stakes | stakes `<…>`, reviewer `<named | not named>`, `<n>` requests to send without review | "In line with" reads as a judgment that review is enough; counts and states let the reviewer judge (TR-H3) |
| disclosure `<present | missing | not required by your policy as stated | policy not stated>` | disclosure `<present | not present>`, expected by `<…>` | "Missing" implies the skill decided disclosure is required; the skill never decides the policy (U0, TR-H6) |
| `<n>` phrases that could stigmatize or exclude | adds changed, questions and evidence gaps named | The task repairs as well as counts, and names evidence gaps for groups |
