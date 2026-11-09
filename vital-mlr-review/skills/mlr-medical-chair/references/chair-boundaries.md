# Medical vs Legal vs Regulatory — MECE

Industry MLR panels separate three questions. Keep them separate in findings.

| Chair | Core question | Typical artefacts |
|---|---|---|
| **Medical** | Is the science and clinical story true to the authorized use and fairly balanced? | Authorized labeling per supplied market (document named per `../../../references/label-basis-by-market.md`) / clinical references supplied by the user |
| **Legal** | Could this create a false or misleading impression, unfair comparison, privacy or IP exposure? | Same draft, viewed as a commercial statement |
| **Regulatory** | Does promotional control, format, and industry-code process allow this to go out? | ISI / brief summary, certification, audience gate, REMS/CDx boxes, pre-approval promo rules |

## Do not cross

- Medical does **not** write “this is misleading advertising” as a legal conclusion.
- Medical does **not** write a finding on a ranking / superiority / “#1” claim unless supplied clinical data or label text lets it judge clinical substantiation; with none supplied it records `[GAP]` and routes the claim to Legal with no medical severity.
- Legal does **not** give a verdict or severity on dose / label accuracy; it routes those to Medical.
- Medical does **not** certify ISI/brief-summary completeness (Regulatory).
- Legal does **not** invent clinical efficacy judgments (Medical).
- Regulatory does **not** re-litigate clinical superiority science (Medical) unless the rule is a format/process control.

When unsure which chair owns a finding, prefer the chair whose **primary standard** is cited in the ruleset `source_ref`, and note the overlap for compile.
