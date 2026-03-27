# Validation Case 01 — Narrow Single-Node Fix

## Purpose
Prove that the system can stay local when the problem locus is obvious and does not widen scope without evidence.

## Class
Narrow single-node fix

## Expected profile
Lite

## Scenario shape
- one obvious locus
- one intended change surface
- no justified multi-file expansion
- no security dimension by default
- only local verification required

## Required orchestration behavior
- Orchestrator states a concrete problem_locus
- Planner defines a minimal dependency_ring
- Planner defines a narrow Builder-enforced read-boundary payload (`allowed_read_set`)
- Planner defines narrow allowed_change_set
- Builder stays inside the declared change zone
- Reviewer checks both correctness and boundary adherence

## Pass conditions
- fix is localized
- no unnecessary files are read or changed
- verification is explicit
- reviewer can falsify success if evidence is missing

## Fail conditions
- scope expands without proof
- dependency ring is vague or inflated
- builder touches undeclared surfaces
- reviewer passes despite incomplete evidence

## Notes
This is the first practical validation target for the surgical system.
It should be implemented before any broader multi-file or security-sensitive scenario.
