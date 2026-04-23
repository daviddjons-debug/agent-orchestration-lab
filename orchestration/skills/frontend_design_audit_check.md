# Skill: frontend_design_audit_check

## Attached module
- `review`

## Purpose
Run a bounded frontend design audit when the task is about visual quality, interface polish, critique, or redesign readiness.

## Use this skill when
- the task is design-first or frontend-polish-first;
- visual hierarchy, spacing, motion, contrast, or responsiveness are materially part of the result;
- the task requires critique before implementation;
- the system risks accepting generic frontend slop as “good enough.”

## Audit lenses
Check only the bounded relevant surface through these lenses:
- typography hierarchy
- spacing rhythm
- contrast and readability
- component density and visual clutter
- interaction clarity
- responsive coherence
- motion appropriateness
- obvious frontend anti-patterns

## Core check sequence
1. Confirm the exact UI surface under review.
2. Confirm whether the task is `audit`, `polish`, or `redesign`.
3. Evaluate only the declared surface, not the whole product.
4. Identify the strongest bounded weaknesses and strongest bounded strengths.
5. Reject vague “make it nicer” output.
6. Require concrete critique that can guide a bounded next step.

## Required output
The design audit result should explicitly state:
- what exact surface was reviewed;
- strongest bounded weaknesses;
- strongest bounded strengths;
- whether the next step should be audit-only, bounded polish, or bounded redesign;
- a compact `Before / After / Why` framing for the most important improvements.

## Anti-fake rule
Do not describe a UI as strong merely because it looks modern, dark, animated, or premium.
Generic polish without hierarchy, rhythm, clarity, and restraint is not sufficient.
