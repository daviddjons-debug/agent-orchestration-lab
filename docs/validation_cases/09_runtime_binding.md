# Validation Case 09 — Runtime Binding

## Goal
Bind the source-of-truth / stale-defect / adjacent-consistency triad to the runnable validation stack without pretending the lab already performs generic repository-scale dependency discovery.

## Current runtime reality
The repository and selftest now prove:
- explicit stage separation;
- builder-side write-boundary enforcement;
- current Builder-only read-boundary compatibility enforcement;
- reviewer-side manifest/plan drift detection;
- reviewer-side undeclared output drift detection;
- bounded coordinated-cluster consistency on declared artifact clusters;
- live bounded code-level verify-only gating in Case 07;
- live bounded cluster-consistency validation in Case 08;
- explicit source/stale/adjacent triad validation in Case 09.

## Practical target for Case 09
Use the persistent substrate under `lab_cases/case_09_source_truth_stale_consistency/` to validate that:
- one explicit canonical node is declared as the source of truth;
- one distinct node is declared as the stale defect surface derived from that source;
- one adjacent node is declared as a required consistency surface;
- stale-defect repair alone is insufficient while the adjacent consistency surface remains stale;
- full triad alignment is required for PASS.

## Explicit bridge from Case 08
Case 08 proved bounded live cluster consistency across a canonical primary node and two dependent surfaces.

Case 09 refines that logic into role-distinct triad semantics on a persistent live substrate:
- Case 08 = bounded live cluster consistency
- Case 09 = bounded live source/stale/adjacent role distinction with mandatory full alignment

This is stronger than generic cluster consistency alone because the reviewer/selftest meaning now depends on semantic role separation, not just field co-presence.

## Honest boundary
Case 09 is not yet a generic manifest-driven runtime case.
It is a dedicated automated selftest scenario on a persistent live substrate.

What is still not proven:
- generic repository-scale dependency discovery;
- automatic derivation of source/stale/adjacent roles from runtime analysis alone;
- planner-side stage-wide propagation of triad semantics into arbitrary live tasks;
- stage-level runtime read sandboxing across all roles;
- arbitrary multi-file surgical orchestration across unrelated repository regions.

The triad remains predeclared and purpose-built for falsifiable validation.

## Why this matters
This closes the gap between:
- bounded live cluster consistency; and
- bounded live semantic role distinction inside a dependency triad.

Case 09 proves the system can reject a fake pass where the stale defect is repaired but the adjacent consistency surface is still stale.
