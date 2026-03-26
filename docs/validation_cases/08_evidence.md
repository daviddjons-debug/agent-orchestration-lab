# Validation Case 08 — Evidence

## Evidence status
PASS for a bounded live cluster-consistency scenario on a persistent substrate in current runtime.

## What was executed
- `python3 scripts/selftest.py`
- dedicated automated Case 08 scenario under:
  - `lab_cases/case_08_live_cluster_consistency/src/spec.json`
  - `lab_cases/case_08_live_cluster_consistency/src/generated_summary.txt`
  - `lab_cases/case_08_live_cluster_consistency/src/generated_manifest.json`

## Positive evidence
- baseline Case 08 cluster passed when all three surfaces agreed on the same canonical message
- the selftest explicitly checked:
  - canonical message presence in `spec.json`
  - summary consistency in `generated_summary.txt`
  - structured consistency in `generated_manifest.json`
- the case returned PASS again after restoring the stale dependent surface
- restoration did not require undeclared widening beyond the declared cluster

## Negative evidence
- the case returned FAIL when `generated_summary.txt` was made stale relative to `spec.json`
- the failure occurred while:
  - `spec.json` remained unchanged
  - `generated_manifest.json` remained unchanged
- this proves the cluster check is not fake single-node validation disguised as multi-file reasoning

## What this PASS proves
- current runtime now supports a persistent live bounded cluster-consistency scenario
- the system can distinguish:
  - primary correctness
  - dependent cluster staleness
  - restored coordinated consistency
- Case 08 is a live-substrate extension of the bounded coordinated-cluster logic first demonstrated in Case 03

## What this PASS does not prove
- generic repository-scale dependency discovery
- automatic cluster discovery without scenario structure
- planner-side read-boundary enforcement
- general runtime read sandboxing
- full real-world multi-file patch orchestration across arbitrary source trees

## Final judgment
Validation Case 08 is passed as a bounded live cluster-consistency scenario on a persistent repository substrate.

It is not yet passed as generic repository-scale orchestration.
