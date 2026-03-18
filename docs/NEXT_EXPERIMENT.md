# Next Experiment — Structured Artifact

## Goal
Upgrade the orchestration test from a toy text artifact to a structured output artifact.

## New target artifact
`output/result.json`

## Required JSON shape
```json
{
  "status": "ok",
  "message": "multi-agent orchestration check passed"
}
```

## Why this matters
A plain text file is too weak as a proof target.
A structured artifact allows stricter validation:
- required file path
- valid JSON syntax
- required keys
- exact values
- future schema extension

## What will need to change
1. `planner.py` must define the required JSON artifact and expected values.
2. `builder.py` must read the planner output semantically and create `output/result.json`.
3. `reviewer.py` must validate:
   - file existence
   - valid JSON
   - required keys
   - exact expected values
4. `selftest.py` must corrupt JSON expectations and verify FAIL, then restore and verify PASS.

## Success criterion
The full scripted pipeline must pass on valid JSON output and fail on semantic corruption.

## Constraint
Do not remove the current baseline until the JSON pipeline is proven.
