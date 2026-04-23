# Skill: security_boundary_exposure_check

## Attached module
- `security`

## Purpose
Require bounded inspection of trust-boundary or exposure-relevant surfaces when the task may affect auth, permissions, secrets, parsing, uploads, or externally reachable behavior.

## Use this skill when
- the task is explicitly security-sensitive;
- the change may alter auth or permission behavior;
- the task touches secrets, uploads, parsing, network-facing endpoints, or trust boundaries;
- completion would be misleading without checking exposure implications.

## Core check sequence
1. Confirm the exact security-relevant surface under review.
2. Confirm the specific trust or exposure boundary that may be affected.
3. Check only the bounded surface relevant to the declared task.
4. Require explicit reasoning about whether the change alters exposure, trust, permission, or parsing behavior.
5. Reject completion if:
   - the task has a real boundary dimension but no explicit security reasoning was performed;
   - “looks safe” is used instead of bounded inspection;
   - the task may widen exposure but this was not evaluated.

## Required output
The security result should explicitly state:
- what exact boundary-relevant surface was checked;
- what trust/exposure implication was considered;
- whether the bounded result supports completion, partial completion, or blockage;
- whether residual risk remains;
- whether retriage or escalation is required.

## Anti-fake rule
Do not accept “no obvious security issue” as sufficient evidence when the task changes a real trust or exposure boundary.
