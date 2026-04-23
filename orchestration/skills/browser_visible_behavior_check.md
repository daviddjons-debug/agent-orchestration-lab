# Skill: browser_visible_behavior_check

## Attached module
- `browser_verification`

## Purpose
Require explicit visible-behavior verification for tasks where completion depends on what actually appears or works in the browser.

## Use this skill when
- the task has a real browser/UI surface;
- acceptance depends on visible client-side behavior;
- static code reasoning is insufficient to prove completion;
- the system risks claiming UI success without checking the actual rendered result.

## Core check sequence
1. Confirm the exact visible UI/browser symptom or expected behavior.
2. Confirm the minimum browser surface that must be checked.
3. Verify only the bounded visible surface relevant to the task.
4. Require explicit evidence that the visible behavior was checked.
5. Reject completion if:
   - the UI/browser-visible surface was not actually checked;
   - the result is inferred from code alone;
   - the checked surface is broader than the declared task contour without justification;
   - the visible symptom remains unresolved.

## Required output
The browser verification result should explicitly state:
- what visible surface was checked;
- what behavior or symptom was observed;
- whether the visible outcome supports completion, partial completion, or blockage;
- whether broader UI investigation or retriage is required.

## Anti-fake rule
Do not accept “the code change should fix the UI” as browser evidence.
Visible browser behavior must be checked directly when it is part of completion.
