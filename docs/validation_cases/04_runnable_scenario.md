# Validation Case 04 — Runnable Scenario

## Scenario shape
A bounded run produces one primary artifact and one adjacent verify-only artifact.

### Primary artifact
`output/result.json`

Expected direct contract:
```json
{
  "status": "ok",
  "message": "primary success"
}
```

### Adjacent verify-only artifact
`output/adjacent_status.txt`

Expected verification condition:
- file must exist;
- file content must be exactly:
  `adjacent verified`

## Intended constraint model
- `output/result.json` is change-allowed
- `output/adjacent_status.txt` is verify-only
- the run must not silently treat primary success as sufficient if adjacent verification is missing or stale

## Failure mode to falsify
Reviewer must not return a trustworthy pass when:
- `output/result.json` is correct;
- but `output/adjacent_status.txt` is missing, stale, or not verified as required.

## Success criterion
The runtime can distinguish:
- true local success: primary artifact correct and adjacent verify-only condition satisfied
- false-local success: primary artifact correct but adjacent verify-only condition unsatisfied
