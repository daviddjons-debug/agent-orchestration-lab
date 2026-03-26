# Validation Case 03 — Runnable Scenario

## Scenario name
Bounded pseudo-code multi-file coordinated change

## Why this scenario fits Case 03
- the primary locus is still local and explicit;
- more than one dependent surface must be updated coherently;
- widening is required, but only inside a bounded local cluster;
- the case fails if the primary node is updated while one or more coordinated dependent nodes remain stale or inconsistent.

## Concrete runnable mapping
- Orchestrator declares one primary source-like artifact plus two dependent artifacts in the same bounded cluster.
- Planner carries forward the primary locus, the justified secondary nodes, and the narrow dependency ring.
- Builder updates all declared surfaces inside the allowed change boundary.
- Reviewer checks:
  - direct contract correctness for each declared artifact;
  - coordinated consistency across the declared local cluster;
  - absence of undeclared widening beyond that cluster.

## Primary locus
`src/spec.json`

## Justified secondary nodes
- `src/generated_summary.txt`
- `src/generated_manifest.json`

## Why the secondary nodes are in scope
They are not decorative extra files.
They represent coordinated downstream surfaces derived from the same local source-like specification.
If the primary spec changes but either generated surface remains stale, the change is not actually safe or complete.

## Minimal dependency ring
- `01_orchestrator.md`
- `run_manifest.json`
- `02_plan.json`
- `src/spec.json`
- `src/generated_summary.txt`
- `src/generated_manifest.json`
- `03_builder.md`
- `04_reviewer.md`

## Coordinated consistency rule
The semantic content declared in `src/spec.json` must remain consistent with both:
- the human-readable message in `src/generated_summary.txt`
- the structured fields in `src/generated_manifest.json`

## What counts as direct symptom evidence
- `src/spec.json` exists
- `src/spec.json` satisfies declared contract

## What counts as coordinated-change evidence
- `src/generated_summary.txt` exists and satisfies declared contract
- `src/generated_manifest.json` exists and satisfies declared contract
- both dependent surfaces remain semantically aligned with the primary spec
- reviewer can detect when only part of the local cluster was updated

## What counts as fail evidence
- primary artifact is correct but one dependent artifact is stale
- primary artifact is correct but the dependent artifacts disagree with each other
- reviewer passes despite missing coordinated-cluster consistency evidence
- scenario language claims justified widening without making the local cluster explicit

## Forward interpretation
This scenario now serves as the pseudo-code cluster template that is later re-expressed on a persistent live substrate in Case 08.

The invariant is the same in both cases:
- one explicit primary node
- explicitly justified dependent nodes
- hard FAIL on stale dependent state

What changes in Case 08 is not the logic but the substrate: the cluster moves from declared run artifacts to persistent repository files under `lab_cases/`.

## Current limitation
This is still a bounded pseudo-code dependency case, not a real repository-scale multi-file code patch.
Its purpose is to test whether the runtime can justify and verify a local coordinated change across multiple dependent surfaces without uncontrolled spread.
