# Session Recap — 2026-03-27 — docs_alignment_green

## What was completed
- normalized Direct vs runnable `baseline` compatibility wording across:
  - `docs/ACTIVATION_MATRIX.md`
  - `docs/EXECUTION_PROFILES.md`
  - `docs/HANDOFF_CONTRACT.md`
  - `docs/NEXT_EXPERIMENT.md`
  - `docs/roles/orchestrator.md`
- aligned Validation Case 01 with Direct-at-policy-layer wording
- marked older session recaps as historical-state notes so they no longer compete with current canonical docs
- verified repo wording cleanup by grep
- ran full `python3 scripts/selftest.py`
- confirmed final `SELFTEST RESULT: PASS`
- created and pushed checkpoint tag:
  - `checkpoint_2026-03-27_docs_alignment_green`

## Verified state
- current runtime baseline remains operational
- lite reviewer path remains operational
- bounded falsification corpus still works
- docs now distinguish:
  - policy-layer Direct
  - runnable `baseline` compatibility path
- no dirty working tree remained at checkpoint time

## Why this mattered
This session did not add fake architecture.
It removed doc-layer contradiction pressure.

That is load-bearing because the project goal is not a decorative multi-agent pack.
The goal is a disciplined orchestration system whose runtime and policy language do not silently diverge.

## Current canonical direction
Authoritative activation/profile direction now lives in:
- `docs/ACTIVATION_MATRIX.md`
- `docs/EXECUTION_PROFILES.md`
- `docs/HANDOFF_CONTRACT.md`
- `docs/VALIDATION_MATRIX.md`
- `docs/NEXT_EXPERIMENT.md`

Older recap files must be treated as historical snapshots, not live authority.

## Project interpretation locked in
The agreed final target is:

A single disciplined orchestration brain that:
1. localizes first,
2. maps the nearest dependency ring,
3. narrows read scope,
4. narrows change scope,
5. applies the smallest sufficient patch,
6. verifies the symptom plus adjacent load-bearing surfaces,
7. escalates only on bounded evidence,
8. does not simulate rigor with extra roles, review theater, or framework inflation.

This project is **not** aiming for:
- more agents by default
- heavy ceremony for simple tasks
- fake runtime expansion before activation logic is coherent
- broad frameworkization before the operating contract is proven

## Remaining gap
The main remaining gap is no longer basic wording drift.

The remaining gap is operational:
- convert the policy-layer activation model into a truly coherent runtime decision model
- prove when Tester and Security activate on evidence
- avoid expanding runtime until that activation logic is genuinely load-bearing

## Best next step
Do not jump into broad runtime expansion yet.

The strongest next move is:
1. freeze this docs/runtime-alignment checkpoint as stable,
2. define the minimal evidence-trigger contract for Tester and Security,
3. only then decide whether the runtime should stay 4-stage or expand.

## Revision
### Refuted
- that the repo still needed more docs churn before stabilization
- that “Direct/Baseline” mixed wording was harmless
- that old recap recommendations should continue to be read as live direction

### Still unclear
- exact minimum runtime shape for evidence-triggered Tester/Security activation
- whether Lite should remain a distinct runtime path or stay policy-compressed longer
- when Planner can be truly collapsed out of Direct runtime rather than only described as compressed

### Required evidence next
- a concrete activation contract for Tester
- a concrete activation contract for Security
- proof that adding them would reduce a real failure class rather than just add ceremony
