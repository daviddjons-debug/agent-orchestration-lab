# Validation Case 01 — Runtime Binding

## Goal
Bind the first validation case to the current runnable 4-stage pipeline without pretending that the runtime already enforces the full surgical contract.

## Current runtime reality
The current runnable pipeline is still:
- orchestrator -> planner -> builder -> reviewer

It already proves:
- explicit stage separation;
- structured handoff via `02_plan.json`;
- manifest-to-plan contract alignment;
- falsifiable reviewer verdict.

It does not yet prove in runtime:
- true problem-locus reasoning;
- full runtime read-boundary enforcement beyond the baseline Builder contract;
- real allowed_change_set enforcement;
- scope-drift prevention by implementation logic alone.

## Practical target for Case 01
Use the current runtime to validate the narrowest credible scenario:
- one obvious locus;
- one narrow declared output surface;
- no unjustified multi-file widening;
- reviewer must fail if plan/artifact contract is corrupted.

## What must be implemented next
1. define a concrete runnable scenario for Case 01;
2. map that scenario to current run artifacts;
3. state what counts as localization evidence in the current runtime;
4. state what counts as fake surgical language without runtime backing.

## Constraint
Do not claim that Case 01 is passed until the runnable scenario and pass/fail evidence are both explicit.
