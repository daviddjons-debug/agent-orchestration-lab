# Leo_Agents_V2 Runtime Handoff Contract

## Purpose
This is the compact runtime handoff contract for `Leo_Agents_V2`.

It defines the minimum bounded semantics needed for real project work without carrying the lab’s full historical contract burden.

## Core rule
Do not begin from broad implementation.
Begin from:
1. task classification
2. best current locus
3. bounded read scope
4. bounded change scope
5. minimum justified execution profile
6. honest completion or honest refusal

## Minimum required contract fields
- `task_class`
- `objective`
- `requested_outcome`
- `best_current_locus`
- `task_surface_type`
- `allowed_read_scope`
- `allowed_change_scope`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

## Conditional but load-bearing fields
Use when relevant:
- `verify_only_surfaces`
- `allowed_target_read_scope`
- `allowed_target_change_scope`
- `donor_repo_path`
- `retriage_required_when_actual_blocker_differs`

## Read-scope rule
Only inspect the bounded surfaces required for the current task.
Do not widen reading because more repo context might be interesting.

## Change-scope rule
Only modify the minimum justified change contour.
No file outside declared change scope may be edited.

## Verify-only rule
If verify-only surfaces are declared, they are load-bearing for completion.
A primary target cannot be treated as “done” while declared verify-only surfaces remain unchecked or contradictory.

## Retriage rule
If actual blocking evidence differs from the assumed path, do not continue under the stale contract.
Reclassify or retriage first.

## Completion rule
A task is complete only if it is possible to state honestly:
- objective status
- whether the change stayed bounded
- whether required adjacent / verify-only surfaces were checked
- whether required behavior or boundary evidence was produced
- whether escalation is still needed

## Anti-fake rule
Do not claim completion from plausibility alone.
Do not widen silently.
Do not convert uncertainty into narrative certainty.
