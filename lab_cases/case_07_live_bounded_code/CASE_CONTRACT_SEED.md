# Case 07 Contract Seed

## Classification
- task_class: `local_fix_with_adjacent_risk`
- path_decision: `baseline`
- false_locality_risk: `high`

## Primary locus hypothesis
- `src/parser.py`

## Adjacent surfaces
- read/adjacent dependency: `src/adjacent_contract.py`
- verify-only surface: `src/verify_only_status.txt`

## Why this is not a purely local task
A change in `src/parser.py` may appear locally successful while adjacent trustworthiness remains incomplete unless verify-only evidence is updated explicitly.

## Intended orchestration check
The system must prove that it can:
- localize the primary intervention node;
- keep the change set narrow;
- avoid silently widening into adjacent edits;
- require verify-only evidence before claiming trustworthy completion.

## Current status
Contract seed established.
Runnable bounded case contract still to be defined.
