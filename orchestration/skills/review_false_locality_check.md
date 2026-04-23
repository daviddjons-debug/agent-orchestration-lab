# Skill: review_false_locality_check

## Attached module
- `review`

## Purpose
Detect false-local success: cases where the primary target appears fixed, but adjacent or verify-only surfaces still invalidate completion.

## Use this skill when
- a patch was applied;
- `verify_only_surfaces` are declared;
- adjacent consistency is load-bearing;
- the fix looks local, but the failure class may not be purely local;
- the system risks declaring success from the primary target alone.

## Core check sequence
1. Confirm what the declared primary target was.
2. Confirm whether the patch stayed inside the declared change set.
3. Check whether any verify-only or adjacent consistency surfaces were declared.
4. Check whether those surfaces were actually validated.
5. Reject completion if:
   - adjacent surfaces were required but not checked;
   - verify-only evidence contradicts the success claim;
   - the patch appears locally correct but leaves the declared consistency contour unresolved.

## Required output
The review result should explicitly state:
- whether the primary target appears repaired;
- whether adjacent/verify-only surfaces were checked;
- whether completion is valid, partial, or blocked;
- whether retriage or escalation is required.

## Anti-fake rule
Do not accept “the main file looks fixed” as completion when the task contract or evidence says adjacent validation is load-bearing.
