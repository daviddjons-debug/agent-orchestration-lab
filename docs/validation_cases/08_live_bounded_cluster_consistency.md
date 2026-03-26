# Validation Case 08 — Live bounded cluster consistency

## Purpose
Extend the lab from artifact-only cluster scenarios into a persistent live cluster substrate under `lab_cases/`.

## What this case tests
This case tests whether the orchestration model can:
- localize one explicit primary node;
- justify a bounded local cluster;
- require coordinated consistency across all declared dependent surfaces;
- fail when one dependent surface becomes stale;
- restore the cluster to PASS without widening beyond the declared boundary.

## Substrate
- `lab_cases/case_08_live_cluster_consistency/src/spec.json`
- `lab_cases/case_08_live_cluster_consistency/src/generated_summary.txt`
- `lab_cases/case_08_live_cluster_consistency/src/generated_manifest.json`

## Classification
- `task_class`: `bounded_cluster_consistency`
- `path_decision`: `baseline`
- `false_locality_risk`: `high`

## Why this case matters
Unlike `docs/runs/*`, this case uses a persistent substrate with a declared primary node and dependent local cluster.
It therefore acts as the first live cluster-consistency bridge between pseudo-code cluster validation and future real bounded repository work.

## Honest boundary
This still does not prove repository-scale orchestration.
It proves only a bounded live cluster-consistency pass on a persistent substrate.
