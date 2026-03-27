# Unified Handoff Contract — Canon v4

## Read contract
- `allowed_read_set` is a hard Builder read contract.
- Builder must read only declared execution inputs.
- Any required read outside `allowed_read_set` must stop execution and trigger escalation.
- `allowed_read_set` must remain minimal-first and must not be described as a stage-wide sandbox.

## Change contract
- `allowed_change_set` is the declared write boundary for execution.
- Builder must execute only inside the declared `allowed_change_set`.
- `allowed_change_set` must begin at the smallest sufficient repair surface.
- `allowed_change_set` may expand only by explicit contract revision, not by execution convenience.
- Any required edit outside `allowed_change_set` must stop execution and trigger escalation.
- Completion requires evidence that execution stayed inside `allowed_change_set`.
- For bounded dependent repair, `allowed_change_set` must permit minimum sufficient dependent change, not automatic whole-cluster rewrite.

## Verify-only surfaces
- `verify_only_surfaces` must be explicit when present.
- Verify-only surfaces are part of required completion evidence even when they are not part of the write set.
- Passing the primary target is insufficient when a declared verify-only surface fails.

## Retriage policy
- `retriage_required_when_actual_blocker_differs` must be explicit when the assumed failure mode may be overridden by execution or validation evidence.
- If actual blocker evidence differs from the assumed blocker, execution must not silently continue under the stale contract.
- Blocker mismatch must trigger retriage or explicit contract revision before further change.

## Required linked contract fields
- `problem_locus`
- `allowed_read_set`
- `allowed_change_set`
- `verify_only_surfaces`
- `verification_targets`
- `evidence_required`
- `expansion_trigger`
- `retriage_required_when_actual_blocker_differs`
