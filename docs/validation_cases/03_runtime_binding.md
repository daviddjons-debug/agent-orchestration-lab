# Validation Case 03 — Runtime Binding

## Goal
Bind the multi-file coordinated-change case to the runnable 4-role runtime without pretending that the lab already performs real repository-scale code reasoning.

## Current runtime reality
The runnable pipeline is still:
- orchestrator -> planner -> builder -> reviewer

It already proves:
- explicit stage separation
- structured plan handoff
- surgical contract field propagation
- reviewer-side contract drift detection
- reviewer-side undeclared output drift detection
- builder-side write-boundary enforcement through `allowed_change_set`
- current Builder-only read-boundary compatibility enforcement through `allowed_read_set`
- bounded adjacent-consistency checking from Case 02

It does not yet prove automatically:
- real repository-scale code dependency analysis
- planner-side Builder-boundary payload propagation only
- stage-level runtime read sandboxing
- genuine discovery of required widening without scenario structure
- tester-backed regression execution for coordinated multi-file changes

## Practical target for Case 03
Use the runnable 4-role runtime to validate a bounded pseudo-code coordinated-change task where:
- one explicit primary locus is declared
- two explicit secondary nodes are justified in the same local cluster
- widening remains bounded inside that declared cluster
- reviewer can fail the case if one dependent surface remains stale or inconsistent
- reviewer can fail the case if the local cluster is widened without declaration

## What must be made explicit
- what the primary locus is
- which secondary nodes are justified
- why those nodes are in scope
- what exact coordinated-consistency rule binds the cluster
- what exact failure should occur if only part of the cluster is updated
- what exact failure should occur if undeclared widening appears

## Constraint
Do not claim Case 03 is passed until the runtime has explicit positive evidence for coordinated multi-file consistency and explicit fail evidence for partial-cluster or undeclared-cluster drift.

## Explicit forward bridge to Case 08
Case 03 should now be interpreted as the bounded pseudo-code coordinated-cluster predecessor to Case 08.

The distinction is strict:
- Case 03 = bounded pseudo-code coordinated cluster inside the runnable manifest-driven runtime
- Case 08 = bounded live cluster-consistency substrate on persistent repository files

Case 08 does not replace Case 03.
It extends the same coordination invariant onto a persistent live substrate while keeping the cluster predeclared rather than runtime-derived.

## Current interpretation
At this stage, Case 03 should be treated as:
- stronger than Case 02
- still bounded by the current 4-stage runtime
- valid only if widening stays local, explicit, and falsifiable
- not yet evidence of real repository-scale code-patch orchestration
