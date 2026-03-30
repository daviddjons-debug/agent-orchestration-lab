# Portable Mode Canon

## Purpose
Provide the single operator-facing canon for the portable orchestration mode.

This document consolidates the portable-pack layer into one practical reading surface.
It does not replace the underlying canonical documents.

---

## What portable mode is
Portable mode is the reusable orchestration layer that sits above a chosen LLM / agent environment.

It is not:
- a new model,
- a new runtime framework by itself,
- or a role-theater swarm.

It is:
- a reusable bounded execution discipline,
- with a canonical contract,
- profile-aware activation logic,
- project-local overlay requirements,
- bounded current-task framing,
- and environment-specific attachment guidance.

---

## Canonical portable-mode layers

### 1. Reusable core
Defines the stable orchestration truth reused across projects.

Primary docs:
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`
- `docs/EXECUTION_PROFILES.md`
- `docs/BASELINE.md`
- `docs/VALIDATION_MATRIX.md`
- `docs/agent_pack_v2_rule_extraction.md`

### 2. Role behavior layer
Defines role behavior aligned to the core contract.

Primary docs:
- `docs/roles/orchestrator.md`
- `docs/roles/planner.md`
- `docs/roles/builder.md`
- `docs/roles/reviewer.md`
- `docs/roles/tester.md`
- `docs/roles/security.md`

### 3. Portable-pack design layer
Defines how the reusable core is packaged and attached across environments.

Primary docs:
- `docs/PORTABLE_PACK_BLUEPRINT.md`
- `docs/PORTABLE_PACK_LAYOUT.md`
- `docs/PROJECT_OVERLAY_MINIMUM.md`
- `docs/VSCODE_ADAPTER_BLUEPRINT.md`
- `docs/ANTIGRAVITY_ADAPTER_BLUEPRINT.md`
- `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
- `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md`

### 4. Evidence layer
Supports proof, validation, and historical truthfulness without becoming policy truth.

Primary surfaces:
- `docs/validation_cases/`
- `docs/session_recaps/`
- `docs/codex_eval/`
- `docs/runs/`

---

## Minimum safe attachment model
A project should only be treated as safely attached to portable mode when all of the following exist:
- reusable core is available,
- project-local overlay minimum exists,
- current task is bounded explicitly,
- an adapter model has been selected.

If any of these are missing, the correct state is:
- setup / triage only,
- not broad execution.

---

## Minimum project-local overlay
Before broad work begins, a project must define at least:
- `PROJECT_SCOPE.md`
- `PROJECT_CONSTRAINTS.md`
- `PROJECT_FORBIDDEN_ZONES.md`
- `PROJECT_VALIDATION_TARGETS.md`

These files provide local truth.
They must not fork or redefine the reusable core.

---

## Bounded task attachment
Portable mode should not execute against a project through vague freeform prompting.

Each current task must define at least:
- current objective,
- task class,
- current locus,
- allowed read/change scope,
- forbidden zones,
- adjacent / verify-only surfaces,
- required validation evidence,
- retriage condition.

The canonical source for this layer is:
- `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`

---

## Environment adapters
Portable mode currently defines blueprint-level adapter guidance for:
- VS Code
- Antigravity

These adapters are thin attachment layers.
They must not redefine core contract truth.

Current adapter docs:
- `docs/VSCODE_ADAPTER_BLUEPRINT.md`
- `docs/ANTIGRAVITY_ADAPTER_BLUEPRINT.md`

---

## Canonical bootstrap order
Use this order for a new project:
1. choose the target environment
2. establish the reusable core
3. create the minimum project-local overlay
4. classify the initial task mode
5. create the bounded current-task surface
6. apply the environment adapter
7. begin bounded execution

The canonical source for this order is:
- `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md`

---

## Reading order
For a compact practical understanding of portable mode, read in this order:
1. `docs/PORTABLE_MODE_CANON.md`
2. `docs/HANDOFF_CONTRACT.md`
3. `docs/ACTIVATION_MATRIX.md`
4. `docs/PROJECT_OVERLAY_MINIMUM.md`
5. `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
6. `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md`
7. relevant adapter blueprint

Then read deeper supporting docs only as needed.

---

## Practical validation status

The portable starter layer is now practically validated for:
- future project starts,
- truthful overlay initialization,
- bounded task shaping,
- tiny real coding tasks,
- bounded improvement steps,
- small multi-file validation loops with generated artifact output,
- honest PASS / FAIL behavior during early project phases.

This does **not** yet prove:
- medium-complexity project work,
- ambiguous multi-dependency engineering tasks,
- sustained correctness on real feature work,
- production-grade repo-scale orchestration,
- final optimality of the current pack.

So the correct boundary is:
- validated for future project starts and early bounded implementation loops;
- not yet validated for medium-complexity project work.

## Current boundary
What portable mode now has:
- bounded reusable orchestration core,
- indexed documentation map,
- portable-pack design canon,
- minimum overlay definition,
- adapter blueprints for VS Code and Antigravity,
- bounded task attachment template,
- canonical bootstrap sequence,
- a first minimal on-disk operational skeleton under `orchestration/`,
- a materialized project-overlay skeleton under `orchestration/overlays/project/`.

What portable mode does not yet claim:
- automatic enforcement in every external environment,
- finalized adapter implementation files under an `orchestration/` directory,
- repository-scale orchestration proof across arbitrary live codebases.

---

## Final operating rule
Portable mode must remain:
- core-first,
- overlay-grounded,
- bounded-task-driven,
- adapter-thin,
- evidence-aware,
- and hostile to scope drift.

It must never collapse into:
- freeform high-agency prompting,
- duplicated core logic per environment,
- or decorative multi-agent theater.
