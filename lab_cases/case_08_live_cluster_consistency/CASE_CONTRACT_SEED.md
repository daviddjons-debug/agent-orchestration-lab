# Case 08 Contract Seed

## Classification
- task_class: `bounded_cluster_consistency`
- path_decision: `baseline`
- false_locality_risk: `high`

## Primary locus hypothesis
- `src/spec.json`

## Justified secondary nodes
- `src/generated_summary.txt`
- `src/generated_manifest.json`

## Why this is not a single-node task
A change to `src/spec.json` is incomplete unless both dependent surfaces remain semantically aligned.

## Intended orchestration check
The system must prove that it can:
- localize the primary intervention node;
- justify the bounded cluster explicitly;
- avoid undeclared widening outside the cluster;
- fail when one dependent surface remains stale.

## Status
Contract seed is now exercised by automated `scripts/selftest.py` coverage on a persistent live substrate.
Runnable bounded case contract is now established and exercised by automated selftest coverage.
