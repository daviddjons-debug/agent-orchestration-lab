# Portable Pack Layout

## Purpose
Define the canonical directory/layout model for the future portable orchestration pack.

This document does not claim that the layout is already implemented as a runnable adapter system.
It defines the target structure and ownership boundaries only.

---

## Canonical target layout

```text
orchestration/
  core/
    HANDOFF_CONTRACT.md
    ACTIVATION_MATRIX.md
    EXECUTION_PROFILES.md
    BASELINE.md
    VALIDATION_MATRIX.md
    RULE_EXTRACTION.md

  roles/
    orchestrator.md
    planner.md
    builder.md
    reviewer.md
    tester.md
    security.md

  adapters/
    vscode.md
    antigravity.md
    codex.md
    claude.md

  overlays/
    project/
      PROJECT_SCOPE.md
      PROJECT_CONSTRAINTS.md
      PROJECT_FORBIDDEN_ZONES.md
      PROJECT_VALIDATION_TARGETS.md

  evidence/
    validation_cases/
    session_recaps/
    codex_eval/
    runs/
```

---

## Layer ownership

### `core/`
Portable global orchestration truth.
This layer is environment-independent and project-independent.

Contains:
- contract semantics
- activation / escalation logic
- profile model
- bounded runtime proof boundary
- validation coverage map
- extracted architecture rules

This is the load-bearing reusable core.

### `roles/`
Role behavior layer aligned to `core/`.
This layer must not drift from contract semantics.
It is reusable across projects and should remain environment-independent.

### `adapters/`
Environment-specific attachment guidance.
This layer explains how a concrete environment should consume the pack.
It must not redefine the core contract.

Examples:
- how VS Code user/workspace customization should load the pack
- how Antigravity should consume the same core
- how external Codex-style evaluators should be constrained

### `overlays/project/`
Project-local additions only.
This layer is allowed to describe:
- project objective
- local constraints
- forbidden zones
- architecture notes
- project-local validation targets

This layer must not mutate or fork the reusable core.

### `evidence/`
Non-canonical proof surfaces and historical records.
This layer supports truthfulness and auditing but is not policy truth.

---

## Mapping from current repo

### Current files that belong conceptually to `core/`
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`
- `docs/EXECUTION_PROFILES.md`
- `docs/BASELINE.md`
- `docs/VALIDATION_MATRIX.md`
- `docs/agent_pack_v2_rule_extraction.md`

### Current files that belong conceptually to `roles/`
- `docs/roles/*.md`

### Current files that belong conceptually to `evidence/`
- `docs/validation_cases/`
- `docs/session_recaps/`
- `docs/codex_eval/`
- `docs/runs/`

### Current missing layers
Not yet defined as canon:
- adapter docs
- project-local overlay docs
- implemented `orchestration/` directory

---

## Design constraints

### Required
- one reusable portable core
- one role layer aligned to that core
- thin adapters only
- project-local overlays separated from reusable core
- evidence separated from contract truth

### Forbidden
- duplicating core semantics inside adapters
- placing raw evidence inside the policy core
- letting project overlays redefine profile logic
- using environment-specific wording as if it were core truth
- claiming the directory layout is already operational before adapter proof exists

---

## Migration rule
The current repo remains doc-first.
No mass file move is required yet.

Before any future directory migration:
1. freeze canonical mappings;
2. define adapter docs;
3. define project overlay docs;
4. only then decide whether to physically materialize `orchestration/`.

---

## Next required step
After this layout doc, the next canonical document should define:
- the minimum required contents of the project-local overlay;
- what a new project must supply before the portable pack can be attached safely.
