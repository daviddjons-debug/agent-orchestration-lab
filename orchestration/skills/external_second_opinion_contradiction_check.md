# Skill: external_second_opinion_contradiction_check

## Attached module
- `external_second_opinion`

## Purpose
Request a bounded independent contradiction check when the current task path may be wrong, incomplete, or under-validated.

## Use this skill when
- locus confidence is not high;
- blast-radius risk is medium or high;
- reviewer-blocking evidence conflicts with the assumed path;
- a previous local attempt failed without clearly resolving the blocker;
- a bounded independent check is justified before escalation or wider change.

## Core check sequence
1. Restate the current task claim in bounded form.
2. Restate the current assumed locus and planned or completed change contour.
3. Ask for the strongest bounded contradiction to the current path.
4. Check whether the contradiction implies:
   - wrong locus;
   - missing adjacent surface;
   - insufficient validation;
   - unjustified widening;
   - need for retriage.
5. Reject blind continuation if the contradiction is evidence-backed and materially changes the task shape.

## Required output
The second-opinion result should explicitly state:
- whether the current path still looks valid;
- the strongest credible contradiction, if any;
- whether retriage is required;
- whether the task may proceed unchanged, proceed with tighter boundaries, or must stop/escalate.

## Anti-fake rule
Do not use second opinion as decorative reassurance.
Use it only to test whether the current bounded path survives an independent contradiction check.
