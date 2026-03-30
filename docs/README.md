# Documentation Map

## Canonical top-level documents
1. `docs/HANDOFF_CONTRACT.md` — canonical handoff / field semantics
2. `docs/ACTIVATION_MATRIX.md` — profile activation and escalation logic
3. `docs/EXECUTION_PROFILES.md` — profile summary / compatibility layer
4. `docs/BASELINE.md` — current bounded runtime proof boundary
5. `docs/VALIDATION_MATRIX.md` — validation-case coverage and status
6. `docs/UNIFIED_HANDOFF_CONTRACT_CANON_V4.md` — unified canon snapshot
7. `docs/agent_pack_v2_rule_extraction.md` — extracted architecture rules from observed bounded validation behavior
8. `docs/NEXT_EXPERIMENT.md` — current next-step target, if still active

## Supporting directories
- `docs/roles/` — role-level behavior docs aligned to the canonical contract
- `docs/validation_cases/` — per-case runtime binding / evidence docs
- `docs/session_recaps/` — session-level historical recap layer
- `docs/baseline_v1/` — preserved older baseline role pack / reference layer

## Evidence layers
- `docs/codex_eval/` — raw external evaluation artifacts; not a canonical policy/contract layer
- `docs/runs/` — generated run artifacts; archival evidence only, not editable source-of-truth docs

## Reading order
For current architecture/runtime understanding, start with:
1. `docs/README.md`
2. `docs/HANDOFF_CONTRACT.md`
3. `docs/ACTIVATION_MATRIX.md`
4. `docs/BASELINE.md`
5. `docs/VALIDATION_MATRIX.md`
6. `docs/agent_pack_v2_rule_extraction.md`

Then read supporting material as needed:
- `docs/roles/`
- `docs/validation_cases/`
- `docs/session_recaps/`
- `docs/codex_eval/` only when reviewing raw external evaluator evidence
