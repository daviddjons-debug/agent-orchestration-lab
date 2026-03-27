# Session Recap — 2026-03-27 — allowed_read_set diagnosis

## Current completion
100%

## What was proven
- `allowed_read_set` is currently a Builder-owned runtime enforcement field.
- The only real mechanical enforcement is in `scripts/builder.py`.
- `scripts/selftest.py` validates `allowed_read_set` only as a builder read-contract proof lane.
- `scripts/orchestrator.py` emits `allowed_read_set` into the shared manifest even though full stage-wide read sandboxing does not exist.
- `scripts/planner.py` propagates `allowed_read_set` forward unchanged and presents it as an execution-stage field.
- `scripts/reviewer.py` incorrectly elevates `allowed_read_set` into a full manifest-plan parity invariant through `CONTRACT_FIELDS`.
- `docs/roles/orchestrator.md` and `docs/roles/planner.md` still describe `allowed_read_set` too broadly.
- `docs/roles/builder.md` correctly reflects reality: Builder is the enforcement owner.
- `docs/HANDOFF_CONTRACT.md` contains the core contradiction:
  - it lists `allowed_read_set` as a required contract field;
  - it simultaneously states that the field is only mechanically enforced for Builder in the current runtime.

## Precise diagnosis
The system currently conflates two different concepts:
1. a Builder-specific compatibility read contract;
2. a supposedly general execution-stage contract field.

That conflation begins at the orchestrator/contract layer, is propagated by planner, is falsely universalized by reviewer, and is only actually enforced by builder.

## Proven code anchors
- `scripts/orchestrator.py`
  - emits profile-specific `allowed_read_set`
  - admits stage-wide read sandboxing is not implemented
- `scripts/planner.py`
  - requires and propagates `allowed_read_set`
  - prints it as “Execution-stage allowed read set”
- `scripts/builder.py`
  - enforces exact expected read sets by `path_decision`
  - this is the real owner of the current behavior
- `scripts/reviewer.py`
  - treats `allowed_read_set` as a full contract equality field
- `scripts/selftest.py`
  - negative/positive tests are specifically builder read-contract tests

## Proven doc anchors
- `docs/HANDOFF_CONTRACT.md`
  - says `allowed_read_set` is required
  - also says it is only Builder-enforced in current runtime
- `docs/roles/orchestrator.md`
  - declares `allowed_read_set` as baseline-required contract field
- `docs/roles/planner.md`
  - declares `allowed_read_set` as baseline-required execution-contract field
- `docs/roles/builder.md`
  - correctly treats it as Builder hard execution-stage read boundary
- `docs/BASELINE.md`
- `docs/NEXT_EXPERIMENT.md`
  - both already correctly frame the missing gap as stage-wide read-boundary enforcement beyond the current Builder-only contract

## Final interpretation
The next real runtime target is not another live substrate case.
Case 07 and Case 08 already closed that lane.

The next unresolved load-bearing control gap is:
- separating Builder read-contract compatibility from any future true stage-wide read-boundary model;
- then hardening runtime around that distinction instead of continuing the current semantic inflation.

## What should happen next
The next patch should be surgical and should likely:
1. rename or specialize the current field semantics so Builder ownership is explicit;
2. stop reviewer from pretending the field is a universal parity invariant unless that is truly intended;
3. align orchestrator/planner docs and trace wording to the actual current runtime;
4. preserve selftest proof for current Builder enforcement while removing false stage-wide implications.

## What must not be claimed
- Do not claim that `allowed_read_set` is already a true stage-wide runtime read sandbox.
- Do not claim that planner/reviewer/orchestrator are mechanically governed by the same read-boundary field in current runtime.
- Do not claim that the current manifest semantics are already clean. They are not.

## Honest project-state conclusion
The diagnosis phase is complete.
The defect is localized.
The remaining work is contract surgery, not further discovery.
