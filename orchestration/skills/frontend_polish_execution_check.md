# Skill: frontend_polish_execution_check

## Attached module
- `browser_verification`

## Purpose
Guide bounded frontend polish execution so visual improvement does not degrade into generic slop, layout thrash, or decorative noise.

## Use this skill when
- the task is in `polish` or `redesign` mode;
- implementation is authorized;
- visible frontend quality is part of completion;
- the task risks overusing motion, effects, or density without improving clarity.

## Core execution rules
- prefer `transform` and `opacity` for motion
- avoid layout-thrashing animation
- avoid `transition: all`
- keep motion bounded and justified
- respect `prefers-reduced-motion`
- do not rely on hover behavior for touch-only contexts
- do not add visual density unless it improves hierarchy
- do not add “premium” styling that weakens readability or rhythm

## Anti-pattern checks
Reject or avoid:
- generic dark glossy slop
- card-inside-card clutter
- weak typography hierarchy
- decorative motion without functional value
- cramped spacing disguised as richness
- contrast loss from tinted overlays or washed-out text
- repeated UI treatment that flattens hierarchy

## Required output
When this skill is active, the result should explicitly state:
- what surface was polished
- what visual/execution changes were made
- what anti-patterns were intentionally avoided
- whether visible behavior still needs browser verification after the change

## Anti-fake rule
Do not treat added effects, gradients, depth, or animation as evidence of better design.
Polish must improve clarity, hierarchy, restraint, and interaction quality.
