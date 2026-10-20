# Gap rules

A gap is information, not an apology. Each reason leads to a different next step, so the class matters.

| Class | When | How to word it | Next step for the person |
|---|---|---|---|
| Person's decision not yet made | The decision-maker, the reference case, a threshold, a range, a scenario, the comparator, the horizon or an owner the person has not given | "Threshold: not chosen yet `[GAP]`; net benefit not computed." | Ask once. If asked to propose, label it "proposed" with the row behind it. |
| Person's input missing | A cost, effect, utility, population or uptake figure the model needs | "Year 2 uptake: not given `[GAP]`; budget impact runs to year 1 only." | The person supplies it, or commissions the evidence (literature review in dh-clinical-development literature-and-real-world-evidence-review). |
| Input source not checked | A published figure without a DOI, or a passage not read in the same direction | "Utility gain 0.02: source not qualified `[GAP]`." | Give the DOI or the document; qualify it, then check the passage. |
| Not sourced | A method rule the research file does not hold (see its "Not sourced" list) | "IQWiG's value set requirement is not sourced here `[GAP]`." | Name the text to read (for example the HAS doctrine document); never fill from memory. |
| Rule in conflict | Two current texts from one body disagree (NICE PMG36 and PMG48 thresholds) | "NICE thresholds: two written ranges, open conflict (HE-050, HE-051, HE-074)." | The person chooses which to report against; both are shown. |
| Draft rule | A rule read only in a draft (AMCP 6.0 rows) | "AMCP draft text (HE-136); final wording not read `[GAP]`." | Check the final text before external use. |
| Tool failed | HTTP 422, 400 or 503 | "Budget impact calculator rejected the payload (HTTP 422, 19 October 2026); same arithmetic run with the scenario modeler." | Use the fallback in `tools.md`; never invent the number. |

## Never

- Never fill a threshold, a cost, an effect, a utility or a range from memory.
- Never turn a missing input into zero without saying so.
- Never treat a tool's citation as a source for a threshold.

When a source is open access, read the full text before marking a field `[GAP]` from its abstract.
