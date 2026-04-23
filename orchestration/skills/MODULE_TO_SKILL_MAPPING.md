# Module to Skill Mapping

## Purpose
This file maps currently materialized modules to currently materialized skills.

It exists to prevent:
- orphan skills;
- decorative skill accumulation;
- unclear attachment between module activation and operational playbooks.

## Current mappings

### review
Attached skills:
- `skills/review_false_locality_check.md`
- `skills/frontend_design_audit_check.md`

Purpose:
- detect false-local success;
- block completion when adjacent or verify-only validation remains unresolved;
- run a bounded frontend design audit for critique, polish readiness, and redesign readiness without accepting generic frontend slop as sufficient.

### testing
Attached skills:
- `skills/testing_behavior_evidence_check.md`

Purpose:
- require explicit behavior-level evidence when completion depends on runnable validation.

### external_second_opinion
Attached skills:
- `skills/external_second_opinion_contradiction_check.md`

Purpose:
- run a bounded contradiction check when the current path may be wrong, incomplete, or under-validated.

### browser_verification
Attached skills:
- `skills/browser_visible_behavior_check.md`
- `skills/frontend_polish_execution_check.md`

Purpose:
- require explicit visible-behavior verification when completion depends on what actually appears or works in the browser;
- guide bounded frontend polish execution so visible improvement does not degrade into decorative noise, layout thrash, or generic premium styling.

### security
Attached skills:
- `skills/security_boundary_exposure_check.md`

Purpose:
- require bounded inspection of trust-boundary or exposure-relevant surfaces when the task may affect auth, permissions, secrets, parsing, uploads, or externally reachable behavior.

## Modules with no materialized skills yet
- `triage`
- `planning`
- `execution`
- `release_packaging`

## Rule
A module should not gain a skill unless the skill closes a specific failure mode that is not already sufficiently covered by:
- the core contract,
- routing,
- profile logic,
- or existing module behavior.
