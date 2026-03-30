# VS Code Bounded Task Example

## Purpose
Provide one concrete bounded current-task surface for the current VS Code attachment path.

This example does not claim live UI enforcement.
It shows the minimum truthful task framing required before bounded execution begins.

## Current task objective
Verify that the current VS Code attachment path is used only with:
- reusable core guidance,
- project-local overlay,
- and explicit bounded task framing.

## Task class
bounded extension

## Primary current locus
- `orchestration/adapters/vscode.md`
- `orchestration/adapters/vscode_usage.md`
- `orchestration/adapters/vscode_verification.md`

## Locus confidence
high

## Allowed read scope
- `docs/VSCODE_ADAPTER_BLUEPRINT.md`
- `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
- `orchestration/adapters/vscode.md`
- `orchestration/adapters/vscode_usage.md`
- `orchestration/adapters/vscode_verification.md`
- `orchestration/overlays/project/PROJECT_SCOPE.md`

## Allowed change scope
- `orchestration/adapters/vscode.md`
- `orchestration/adapters/vscode_usage.md`
- `orchestration/adapters/vscode_verification.md`
- `orchestration/tasks/vscode_bounded_task_example.md`

## Forbidden zones
- `scripts/`
- `lab_cases/`
- `docs/validation_cases/`
- `docs/runs/`
- current runnable runtime behavior

## Adjacent / verify-only surfaces
- `docs/VSCODE_ADAPTER_BLUEPRINT.md`
- `docs/README.md`

## Required validation evidence
- the VS Code path remains explicitly layered
- the adapter artifact remains thin
- the usage card still requires overlay + bounded task
- the verification note still preserves non-claims

## Stop and retriage when
- the VS Code path requires extension-specific claims
- safe execution cannot be stated without broadening scope
- live UI behavior must be asserted rather than bounded documentation-level verification

## Special rule
- prefer no patch if the current VS Code path is already internally consistent
- do not widen into runtime, extension config, or generic multi-environment work
