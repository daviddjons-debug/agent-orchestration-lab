# Validation Case 08 — Runnable Scenario

## Scenario
A bounded local cluster is defined under `lab_cases/case_08_live_cluster_consistency/src`.

## Primary locus
- `spec.json`

## Justified secondary nodes
- `generated_summary.txt`
- `generated_manifest.json`

## Expected local rule
The canonical message in `spec.json` must remain semantically aligned with:
- the human-readable message in `generated_summary.txt`
- the structured message field in `generated_manifest.json`

## Pass/Fail invariant
PASS iff all three declared cluster surfaces carry the same canonical message.

FAIL if any dependent surface diverges from the canonical message in `spec.json`, even when the other dependent surface still matches.

## Expected orchestration behavior
The system should:
1. localize `spec.json` as the primary node;
2. justify the two dependent surfaces as a bounded local cluster;
3. require coordinated consistency across all three surfaces;
4. fail when one dependent surface becomes stale;
5. restore PASS when the cluster is brought back into alignment.

## Failure mode
A cluster must not be treated as complete when:
- `spec.json` is valid,
- `generated_manifest.json` is valid,
- but `generated_summary.txt` is stale relative to the canonical message.

## Boundary
This case remains bounded to the declared cluster and does not yet prove generic repository-scale dependency discovery.

The cluster is explicitly declared in advance.
It is not automatically discovered by the runtime.
