# VS Code Verification Note

## Purpose
Define the minimum bounded verification procedure for the current VS Code attachment path.

This note does not prove automatic enforcement.
It does not prove extension-specific integration.
It defines only the smallest honest verification surface for the current phase.

## Verification target
Verify that the current VS Code attachment path is usable only when the following layers are present and consulted together:
- reusable core guidance
- project-local overlay
- bounded current-task surface
- VS Code adapter artifact
- VS Code usage proof card

## Minimum bounded verification checks

### Check 1 — overlay dependency is explicit
Confirm that broad execution is not treated as safe when project overlay minimum is missing.

### Check 2 — bounded task dependency is explicit
Confirm that task execution is not treated as safe when the current task is not explicitly bounded.

### Check 3 — adapter artifact remains thin
Confirm that the VS Code adapter artifact does not claim:
- automatic enforcement
- extension-specific configuration guarantees
- migrated core/roles
- full environment integration

### Check 4 — usage path remains layered
Confirm that the documented VS Code usage path still depends on:
- reusable core
- project overlay
- bounded current-task framing

### Check 5 — current boundary remains honest
Confirm that the VS Code path is described as:
- a thin operational bridge
- not a completed live integration proof

## Acceptance rule
The current VS Code attachment path is considered verified only in the bounded sense that:
- the required layers exist on disk,
- their dependency order is explicit,
- their non-claims remain explicit,
- and no document in the current VS Code path overstates enforcement or integration status.

## Non-claims
This verification note does not establish:
- live UI verification in VS Code
- extension-specific runtime behavior
- automatic attachment enforcement
- cross-environment parity

## Current repo linkage
- blueprint: `docs/VSCODE_ADAPTER_BLUEPRINT.md`
- adapter artifact: `orchestration/adapters/vscode.md`
- usage proof: `orchestration/adapters/vscode_usage.md`
- live verification checklist: `orchestration/adapters/vscode_live_verification_checklist.md`
- project overlay: `orchestration/overlays/project/`
- bounded task template: `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
