# Tools and companion slot

## Companion slot

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| No fabrication | Test each claim against the quoted passage it rests on | VERIFY `check_claim`, `verify_text`, through `claim-assessment` | Method runs; check line says "not tool-checked" |
| Number consistency | Test that each figure appears in its passage | VERIFY `check_claim`, through `claim-assessment` | Method and scripts run; "not tool-checked" |
| Method description | Test that design and endpoint statements match the passage | VERIFY `check_claim`, through `claim-assessment` | Method runs; "not tool-checked" |

This skill never calls VERIFY directly. It hands finished text to `claim-assessment`,
which owns the tool calls and their interpretation. That keeps the tool contract in one
place. [CHECK: VERIFY argument and return contracts to be confirmed in claim-assessment.]

## Scripts

Run them where the host can execute code. Where it cannot, do the same steps by hand and
show the arithmetic.

### `scripts/extract_numbers.py`

Lists every number in a text with its surrounding words, line number and any unit or
percent sign, so each can be matched to the source.

```
python scripts/extract_numbers.py draft.txt
python scripts/extract_numbers.py draft.txt --json
```

### `scripts/risk_metrics.py`

Computes absolute and relative effects for a binary outcome from arm rates or counts and,
optionally, compares figures stated in the draft.

```
python scripts/risk_metrics.py --treat-events 10 --treat-n 500 --ctrl-events 20 --ctrl-n 500
python scripts/risk_metrics.py --treat-rate 0.02 --ctrl-rate 0.04 --check rrr=50 --check arr=2
```

Outputs: each arm's risk, risk difference in percentage points, relative risk, relative
risk reduction, and NNT (or NNH) with direction. Every output is labeled "derived from
supplied values".

Pitfalls:

- Use the same analysis population and timepoint for both arms.
- Do not compare a derived crude figure with an adjusted or model-based figure from the
  source as if one corrects the other.
- NNT is rounded up to a whole number by convention; the unrounded value is shown too.
