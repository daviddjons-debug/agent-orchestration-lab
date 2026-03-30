# VS Code Live Verification Checklist

## Purpose
Define the minimum honest live verification checklist for the current VS Code attachment path.

This checklist does not claim automatic enforcement.
It does not claim extension-specific integration proof.
It defines only the smallest live-use verification surface for the current phase.

## Live verification target
Verify in real use that the current VS Code path is followed only when all of the following are actually consulted:
- reusable core guidance
- project-local overlay
- bounded current-task surface
- VS Code adapter artifact
- VS Code usage proof card
- VS Code verification note

## Minimum live checks

### Check 1 — overlay is actually consulted
Before broad work begins, confirm that `orchestration/overlays/project/` is explicitly consulted rather than assumed.

### Check 2 — bounded task is actually instantiated
Before execution begins, confirm that a concrete bounded task surface exists and is used, not skipped.

### Check 3 — adapter artifact is not treated as automation
Confirm that `orchestration/adapters/vscode.md` is used as guidance only, not as proof that VS Code automatically enforces the pack.

### Check 4 — usage path is followed in order
Confirm that the live path follows:
1. reusable core
2. project overlay
3. bounded task
4. VS Code execution

### Check 5 — non-claims remain explicit
Confirm that no live claim is made for:
- automatic enforcement
- extension-specific guarantees
- migrated core/roles
- full environment integration

## Acceptance rule
The current VS Code path is considered live-verified only in the bounded sense that:
- the documented path is followed in real use,
- the required layers are actually consulted,
- and no stronger enforcement/integration claim is made than the repo currently proves.

## Non-claims
This checklist does not establish:
- automatic VS Code enforcement
- extension-specific runtime proof
- UI-level reproducibility across all setups
- cross-environment parity
