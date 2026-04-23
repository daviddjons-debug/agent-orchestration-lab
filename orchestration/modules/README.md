# Modules Layer

## Purpose
This layer defines the functional modules that may be activated after routing and profile selection.

A module is not a role and not yet a skill.
A module is a bounded functional lane that may later attach:
- one or more skills,
- one or more host-specific execution patterns,
- profile-specific activation rules.

## Initial modules
The first bounded modules are:

- `triage`
- `planning`
- `execution`
- `review`
- `testing`
- `security`
- `browser_verification`
- `external_second_opinion`
- `release_packaging`

## Interpretation
- `triage` = classify, localize, bound, and decide path
- `planning` = shape the bounded execution contract
- `execution` = apply the smallest justified patch or no-op decision
- `review` = inspect for contract drift, false-local success, and undeclared widening
- `testing` = validate runnable behavior or regression surfaces when needed
- `security` = inspect trust-boundary or exposure risk when materially relevant
- `browser_verification` = run bounded UI/browser checks when the task has a real UI surface
- `external_second_opinion` = request bounded contradiction or independent review when evidence justifies it
- `release_packaging` = prepare bounded handoff/release outputs when the task includes packaging or shipment

## Current role
This layer is the bridge between:
- profile selection
- future module activation matrix
- future skills attachment

## Not yet materialized here
- per-profile allowed/blocked module rules
- per-task-class module defaults
- module trigger matrix
- module-to-skill mapping
