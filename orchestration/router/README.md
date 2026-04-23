# Routing Layer

## Purpose
This layer decides which execution contour should activate for a given task before any implementation or expansion begins.

It exists to prevent:
- default full-stack activation;
- role theater;
- unnecessary token burn;
- scope drift caused by activating the wrong execution path.

## Routing order
For every task, route in this order:

1. classify the task
2. estimate locus confidence
3. estimate false-locality risk
4. estimate blast-radius risk
5. decide the minimum justified execution profile
6. allow only the modules required by that profile and task class

## Initial routing outputs
The routing layer must produce at minimum:
- `task_class`
- `locus_confidence`
- `false_locality_risk`
- `blast_radius_risk`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

## Initial task classes
These are the first routing classes to support:

- `narrow_bugfix`
- `local_fix_with_adjacent_risk`
- `bounded_multi_file_patch`
- `regression_sensitive_change`
- `security_sensitive_change`
- `justified_local_hardening`
- `bounded_consistency_audit`
- `no_change_verification`
- `unknown`

## Task class selection guidance

### `narrow_bugfix`
Use when:
- a concrete local defect is already identified;
- implementation is expected;
- the likely repair surface is narrow;
- adjacent verification is not expected to be load-bearing.

### `local_fix_with_adjacent_risk`
Use when:
- implementation is expected;
- the primary repair still looks local;
- adjacent or verify-only surfaces may invalidate a purely local success claim.

### `bounded_multi_file_patch`
Use when:
- implementation is expected;
- more than one file or node is likely part of the minimum sufficient repair contour;
- the task is still bounded and not a broad refactor.

### `regression_sensitive_change`
Use when:
- implementation is expected;
- runnable behavior or regression surfaces are materially load-bearing for completion.

### `security_sensitive_change`
Use when:
- implementation is expected;
- the task has a real trust-boundary, auth, exposure, or security dimension.

### `justified_local_hardening`
Use when:
- implementation is expected;
- the change is still local;
- a narrow hardening step is justified by evidence, not by cleanup appetite.

### `bounded_consistency_audit`
Use when:
- the requested outcome is audit, consistency review, or bounded truth-alignment first;
- implementation is not yet authorized;
- the main goal is to determine whether current docs/artifacts/state are mutually consistent inside a declared boundary.

### `no_change_verification`
Use when:
- the requested outcome is to verify that no patch is needed;
- implementation is not authorized unless verification fails;
- the task is mainly about bounded confirmation rather than repair.

### `unknown`
Use when:
- the task cannot yet be honestly classified;
- implementation would be premature;
- retriage is needed before choosing a repair or audit path.

## Profile decision rule
- Default to the cheapest path that can still control the relevant failure class.
- Do not escalate by task-size narrative alone.
- Do not activate modules merely because they exist.

## Current status
This is the first materialized routing surface.
It is not yet the full activation matrix replacement.
It is the operator-facing bridge between task classification and future profile / skills activation.
