# Skill: testing_behavior_evidence_check

## Attached module
- `testing`

## Purpose
Require explicit behavior-level evidence when the task changes runnable behavior or when completion depends on executable symptom validation.

## Use this skill when
- runnable behavior changed;
- the symptom can be checked through execution;
- regression-sensitive behavior is part of acceptance;
- the task is not safely closable through static inspection alone.

## Core check sequence
1. Confirm which behavior or symptom the task claims to affect.
2. Confirm whether that behavior is actually executable or directly testable.
3. Identify the minimum sufficient behavior check for the declared task.
4. Require explicit evidence that the behavior check was performed.
5. Reject completion if:
   - behavior-level validation was required but not performed;
   - only plausibility or static reasoning is provided instead of executable evidence;
   - the claimed fix changes runtime behavior but no direct symptom/regression check exists.

## Required output
The testing result should explicitly state:
- what behavior or symptom was tested;
- what evidence was collected;
- whether the result supports completion, partial completion, or blockage;
- whether additional testing or retriage is required.

## Anti-fake rule
Do not accept “this should now work” as testing evidence when the task requires runnable behavior validation.
