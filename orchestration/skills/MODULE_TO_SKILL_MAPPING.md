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

Purpose:
- detect false-local success;
- block completion when adjacent or verify-only validation remains unresolved.

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

## Modules with no materialized skills yet
- `triage`
- `planning`
- `execution`
- `security`
- `browser_verification`
- `release_packaging`

## Rule
A module should not gain a skill unless the skill closes a specific failure mode that is not already sufficiently covered by:
- the core contract,
- routing,
- profile logic,
- or existing module behavior.
