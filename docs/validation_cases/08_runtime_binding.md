# Validation Case 08 — Runtime Binding

## Goal
Bind live bounded cluster consistency to the current runtime without pretending that the lab already performs generic repository-scale multi-file reasoning.

## Current runtime reality
The runnable pipeline and selftest now prove:
- explicit stage separation;
- builder-side write-boundary enforcement;
- current Builder-only read-boundary compatibility enforcement;
- reviewer-side manifest/plan drift detection;
- reviewer-side undeclared output drift detection;
- bounded coordinated-cluster consistency on declared artifact clusters;
- live bounded code-level verify-only gating in Case 07;
- live bounded cluster-consistency validation in Case 08.

## Practical target for Case 08
Use the persistent substrate under `lab_cases/case_08_live_cluster_consistency/` to validate that:
- one explicit primary node is declared;
- two dependent nodes are justified;
- cluster consistency is checked explicitly;
- stale dependent state causes a hard FAIL;
- restoration of the dependent surface returns the case to PASS.

## Explicit bridge from Case 03
Case 03 proved bounded coordinated-cluster consistency only in a pseudo-code artifact scenario.

Case 08 extends that same logic onto a persistent live repository substrate:
- Case 03 = bounded pseudo-code coordinated cluster
- Case 08 = bounded live cluster-consistency substrate

This is a stronger validation surface than Case 03, but it is still not generic repository-scale orchestration.

## Honest boundary
Case 08 is not yet a generic manifest-driven runtime case.
It is a dedicated automated selftest scenario on a persistent live substrate.

What is still not proven:
- generic repository-scale dependency discovery;
- automatic cluster discovery from runtime analysis alone;
- planner-side Builder-boundary payload propagation only;
- stage-level runtime read sandboxing;
- arbitrary multi-file patch orchestration across unrelated repository regions.

The cluster in Case 08 is still predeclared, not runtime-derived.

## Why this matters
This closes the gap between:
- pseudo-code coordinated-cluster validation in Case 03; and
- persistent live cluster-consistency validation on repository files.
