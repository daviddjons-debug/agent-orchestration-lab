# Case 08 Execution Target

## First bounded task
Apply a coordinated local update so that all declared cluster surfaces agree on the same message.

## Desired behavior
- `src/spec.json` contains the canonical message
- `src/generated_summary.txt` matches that message
- `src/generated_manifest.json` matches that message

## Boundary expectations
### Allowed change candidates
- `src/spec.json`
- `src/generated_summary.txt`
- `src/generated_manifest.json`

## Explicit failure expectation
The case must fail if one dependent surface is stale relative to `src/spec.json`.

## Status
Execution target is now exercised by automated `scripts/selftest.py` coverage on a persistent live substrate.
