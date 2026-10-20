# Script run: capture inventory check (illustrative data)

Run on 19 October 2026: `python3 scripts/capture_inventory_check.py evals/files/capture_inventory_illustrative.csv`. The input file is invented for testing and labeled illustrative. Note for A2: the ePRO validation flag points to COA development, which the FDA DHT guidance places out of its scope (CV45); route it to the study design skill.

# Capture inventory check

Streams: 4. Open attributes: 15. Each line is a missing record against a sourced requirement element, not a verdict on the stream.

| Stream | Endpoint role | Open attribute | Row |
|---|---|---|---|
| Daily step count (wrist accelerometer) | primary | Validation not shown in the trial population | CV48 |
| Daily step count (wrist accelerometer) | primary | Usability evaluation with the trial population not recorded | CV51 |
| Daily step count (wrist accelerometer) | primary | Critical-to-quality stream without a contingency for tool failure | CV99 |
| Resting heart rate (same wrist sensor) | safety | Unambiguous timestamps (for example UTC) not confirmed | CV14 |
| Resting heart rate (same wrist sensor) | safety | Can show abnormal values; safety review plan not recorded | CV62 |
| Pain score ePRO (app) | key_secondary | Validation evidence not recorded | CV46 |
| Pain score ePRO (app) | key_secondary | Source location (first durable repository) not named | CV60 |
| Pain score ePRO (app) | key_secondary | Same collection method in all arms not recorded | CV58 |
| Pain score ePRO (app) | key_secondary | Participant-entered data on a key_secondary endpoint without an entry safeguard | CV103 |
| Home spirometry | exploratory | No model and version named; minimum specifications cannot be checked | CV52 |
| Home spirometry | exploratory | Verification evidence not recorded | CV46 |
| Home spirometry | exploratory | Validation evidence not recorded | CV46 |
| Home spirometry | exploratory | Usability evaluation with the trial population not recorded | CV51 |
| Home spirometry | exploratory | Audit trail not confirmed | CV14 |
| Home spirometry | exploratory | Unambiguous timestamps (for example UTC) not confirmed | CV14 |
