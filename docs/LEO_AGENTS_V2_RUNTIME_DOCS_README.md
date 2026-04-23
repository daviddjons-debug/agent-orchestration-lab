# Leo_Agents_V2 Runtime Documentation Map

## Purpose
This is the compact runtime documentation map for `Leo_Agents_V2`.

It exists to:
- define the minimum reading spine for real project work;
- keep the runtime pack self-consistent;
- avoid dragging lab history into the runtime authority layer.

## Runtime authority surfaces
These are the minimum canonical docs surfaces in the runtime pack:

1. `docs/README.md` — runtime reading map
2. `docs/HANDOFF_CONTRACT.md` — bounded handoff and scope semantics
3. `docs/ACTIVATION_MATRIX.md` — profile activation and escalation logic

## Operational orchestration surfaces
These are the main orchestration surfaces used during execution:

- `orchestration/README.md`
- `orchestration/router/README.md`
- `orchestration/router/TASK_CLASS_DEFAULTS.md`
- `orchestration/profiles/README.md`
- `orchestration/modules/README.md`
- `orchestration/modules/ACTIVATION_MATRIX.md`
- `orchestration/modules/TRIGGER_MATRIX.md`
- `orchestration/skills/README.md`
- `orchestration/skills/MODULE_TO_SKILL_MAPPING.md`

## Host-facing invocation surfaces
These are used when launching bounded tasks through Codex:

- `orchestration/adapters/vscode_codex_bounded_invocation.md`
- `orchestration/adapters/vscode_codex_launch_template.md`
- `orchestration/adapters/vscode_codex_audit_launch_template.md`
- `orchestration/adapters/vscode_codex_browser_ui_launch_template.md`
- `orchestration/adapters/vscode_codex_security_launch_template.md`
- `orchestration/adapters/external_target_repo_invocation.md`

## Reading order

### Minimum runtime reading order
1. `README.md`
2. `START_HERE.md`
3. `docs/README.md`
4. `docs/HANDOFF_CONTRACT.md`
5. `docs/ACTIVATION_MATRIX.md`

### Then read execution surfaces as needed
6. `orchestration/README.md`
7. `orchestration/router/README.md`
8. `orchestration/router/TASK_CLASS_DEFAULTS.md`
9. `orchestration/profiles/README.md`
10. `orchestration/modules/README.md`
11. `orchestration/modules/ACTIVATION_MATRIX.md`
12. `orchestration/modules/TRIGGER_MATRIX.md`
13. `orchestration/skills/README.md`
14. `orchestration/skills/MODULE_TO_SKILL_MAPPING.md`

### Then load only the host-facing adapter needed for the current task
- generic bounded task
- audit-only task
- browser/UI task
- security-sensitive task
- external target repo task

## What is intentionally not in the runtime pack
The runtime pack should not carry:
- session recap archives
- validation case corpus
- codex eval raw evidence
- lab scripts
- selftest harness internals
- generated run artifacts
- historical proof clutter

## Runtime rule
The runtime pack is an operational authority layer, not an R&D archive.
