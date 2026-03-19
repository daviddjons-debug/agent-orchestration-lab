# Validation Case 01 — Evidence

## Evidence status
PASS for narrow contract execution in current runtime, with verified write-boundary controls.

## What was executed
- `python3 scripts/run_pipeline.py docs/runs`
- `python3 scripts/selftest.py`
- clean run folder created
- planner produced `02_plan.json` with propagated surgical contract fields
- builder produced only declared artifacts inside allowed write scope
- reviewer returned PASS on valid declared contract
- reviewer returned FAIL on contract corruption
- reviewer returned FAIL on undeclared output drift
- builder returned FAIL when artifact path was outside `allowed_change_set`

## Clean run evidence
- required prior artifacts existed
- `02_plan.json` matched full `run_manifest.json` contract
- contract fields matched between manifest and plan:
  - `objective`
  - `problem_locus`
  - `dependency_ring`
  - `allowed_read_set`
  - `allowed_change_set`
  - `forbidden_zone`
  - `verification_targets`
  - `blockers_or_uncertainties`
- declared artifacts existed and satisfied declared contract
- no undeclared output drift was detected

## Negative evidence
- reviewer returned FAIL after planner artifact contract corruption
- reviewer returned FAIL after `allowed_change_set` drift between manifest and plan
- reviewer returned FAIL after undeclared file creation (`output/rogue.txt`)
- builder returned FAIL when declared artifact path fell outside `allowed_change_set`

## What this PASS now proves
- current runtime supports explicit 4-stage separation
- planner-to-builder handoff is structured
- surgical contract fields propagate through runnable runtime
- reviewer validates full manifest-plan contract alignment, not only artifact presence
- reviewer detects undeclared output drift
- builder enforces declared write boundary through `allowed_change_set`
- builder enforces baseline-compatible declared read boundary through `allowed_read_set`
- selftest covers valid, corrupted, drifted, restored, relaxed-policy, undeclared-output, and builder-boundary cases

## What this PASS still does not prove
- real problem-locus reasoning in runtime beyond propagated contract fields
- real dependency-ring reasoning in runtime beyond propagated contract fields
- full runtime `allowed_read_set` enforcement beyond the baseline Builder contract
- tester as a runnable runtime stage
- security as a runnable runtime stage
- full surgical-runtime behavior on real code-patch tasks

## Final judgment
Validation Case 01 is passed as a narrow contract-execution scenario with verified reviewer-side contract checks, builder-side write-boundary controls, and baseline Builder read-boundary validation.

It is still not passed as a full surgical-runtime scenario.

