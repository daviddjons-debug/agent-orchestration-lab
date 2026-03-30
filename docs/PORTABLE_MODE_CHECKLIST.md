# Portable Mode Checklist

## Use this when starting or attaching a new project

### 1. Select the environment
- choose the target environment first:
  - VS Code
  - Antigravity
  - or another supported bounded executor shell

### 2. Ensure the reusable core is the active brain
- the environment must have access to the portable reusable core
- do not start from freeform prompting alone

Core references:
- `docs/PORTABLE_MODE_CANON.md`
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`

### 3. Create the minimum project-local overlay
- create at least:
  - `PROJECT_SCOPE.md`
  - `PROJECT_CONSTRAINTS.md`
  - `PROJECT_FORBIDDEN_ZONES.md`
  - `PROJECT_VALIDATION_TARGETS.md`

- if these do not exist, the project is still in setup/triage mode

### 4. Classify the current task
- classify it before execution:
  - greenfield bootstrap
  - bounded extension
  - narrow fix
  - adjacent-risk fix
  - heavy uncertainty

### 5. Create the bounded current-task surface
- define at least:
  - current objective
  - expected bounded end state
  - current locus
  - allowed read scope
  - allowed change scope
  - forbidden zones
  - adjacent / verify-only surfaces
  - required validation evidence
  - retriage condition

Reference:
- `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`

### 6. Apply the relevant adapter
- use the environment adapter on top of:
  - reusable core
  - project-local overlay
  - bounded current-task surface

References:
- `docs/VSCODE_ADAPTER_BLUEPRINT.md`
- `docs/ANTIGRAVITY_ADAPTER_BLUEPRINT.md`

### 7. Start bounded execution only now
- execution may begin only after:
  - reusable core is active
  - local overlay exists
  - current task is bounded
  - adapter is selected

### 8. Stop and retriage when needed
- do not widen silently
- stop when actual blocking evidence breaks the assumed task contour
- prefer retriage over fake completion

### 9. Completion rule
- do not claim completion without the declared validation evidence
- prefer `NO_PATCH_REQUIRED` when no real defect/mismatch is proven
- prefer the smallest sufficient patch when a patch is required

---

## Red flags
- starting from freeform prompting only
- missing project-local overlay
- broad repo exploration without a bounded task surface
- adapter-specific behavior replacing core contract truth
- claiming attachment is safe before the minimum layers exist
- claiming completion without declared evidence

---

## Minimum practical reading order
1. `docs/PORTABLE_MODE_CANON.md`
2. `docs/PROJECT_OVERLAY_MINIMUM.md`
3. `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
4. relevant adapter blueprint
5. `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md`

---

## One-line rule
Core first. Overlay second. Bounded task third. Adapter fourth. Execution last.
