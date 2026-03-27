# Validation Case 02 — Runtime Binding

## Goal
Bind the adjacent-dependency-risk case to the runnable 4-role runtime without pretending that the system already performs full dependency-aware reasoning automatically.

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

It does not yet prove automatically:
- genuine discovery of adjacent dependency risk
- full stage-wide runtime read-boundary enforcement beyond the current Builder-only read-boundary contract
- true dependency analysis beyond declared contract data
- real behavioral verification unless the scenario makes evidence explicit

## Practical target for Case 02
Use the runnable 4-role runtime to validate a narrowly scoped task where:
- one primary locus is declared
- one adjacent node is explicitly added to the dependency ring
- allowed read scope is still narrow
- allowed change scope remains local unless widening is justified
- reviewer can fail the case if adjacent-node verification evidence is missing

## What must be made explicit
- what the primary locus is
- what the adjacent dependency node is
- why that adjacent node is in scope
- what counts as direct symptom evidence
- what counts as adjacent-node safety evidence
- what exact failure should occur if adjacent risk is ignored

## Constraint
Do not claim Case 02 is passed until the runnable scenario includes explicit adjacent-risk evidence and an explicit fail mode for missing that evidence.

## Current interpretation
At this stage, Case 02 should be treated as:
- stronger than Case 01
- still bounded by the current 4-stage runtime
- valid only if the adjacent dependency check is concrete, local, and falsifiable

