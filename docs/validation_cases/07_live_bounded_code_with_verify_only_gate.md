# Validation Case 07 — Live bounded code with verify-only completion gate

## Purpose
Extend the lab beyond run-residue-only scenarios by using a persistent code substrate under `lab_cases/`.

## What this case tests
This case tests whether the orchestration model can:
- localize a plausible primary code locus;
- keep the initial change surface narrow;
- avoid unnecessary adjacent edits;
- require explicit verify-only evidence before trustworthy completion is claimed.

## Substrate
- `lab_cases/case_07_live_bounded_code/src/parser.py`
- `lab_cases/case_07_live_bounded_code/src/adjacent_contract.py`
- `lab_cases/case_07_live_bounded_code/src/verify_only_status.txt`

## Classification
- `task_class`: `local_fix_with_adjacent_risk`
- `path_decision`: `baseline`
- `false_locality_risk`: `high`

## Why this case matters
Unlike `docs/runs/*`, this case uses a persistent code surface.
It therefore provides a reusable bounded code-level validation substrate rather than a one-off artifact emission scenario.

## Current boundary
This still does not prove repository-scale code orchestration.
It proves only a bounded live code-level pass on a minimal persistent substrate.

## Explicit bridge from Case 04
Case 07 should be interpreted as the persistent live-substrate successor to Case 04.
Case 04 established verify-only rejection in a bounded runtime artifact scenario.
Case 07 carries the same completion discipline into a persistent code substrate under `lab_cases/`.
