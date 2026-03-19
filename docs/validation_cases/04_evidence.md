# Evidence — Case 04

## Scenario status
Executed in runtime.

## Executed run
- run directory: `docs/runs/orchestrated-2026-03-19_21-03-09`

## Observed failure path
The runtime produced a valid primary artifact:
- `output/result.json`

Reviewer returned `FAIL` when:
- the primary artifact satisfied its declared contract;
- `output/adjacent_status.txt` was declared as a verify-only surface;
- the verify-only surface was missing and therefore not satisfied.

Observed reviewer evidence:
- `output/result.json` exists
- `output/result.json` satisfies declared contract
- `verify-only surface satisfied: output/adjacent_status.txt` -> FAIL
- final verdict -> `FAIL`

## Observed success path
Reviewer returned `PASS` after:
- `output/adjacent_status.txt` was created as a verify-only surface;
- file content was set to exactly `adjacent verified`

Observed reviewer evidence:
- `output/result.json` exists
- `output/result.json` satisfies declared contract
- `verify-only surface satisfied: output/adjacent_status.txt` -> PASS
- final verdict -> `PASS`

## What this now proves
- manifest -> plan propagation for:
  - `verify_only_surfaces`
  - `excluded_neighbors`
  - `review_strictness`
- reviewer can reject false-local success when adjacent verify-only validation is missing
- reviewer can accept the same run once the verify-only adjacent condition is satisfied
- current bounded runtime now has real executable evidence for Case 04

## What this still does not prove
- repository-scale dependency discovery
- tester-stage execution
- full runtime enforcement of all Surgical Edition extension semantics
- code-level blast-radius control

## Current judgment
Validation Case 04 is passed as a bounded runtime false-locality verification scenario.
