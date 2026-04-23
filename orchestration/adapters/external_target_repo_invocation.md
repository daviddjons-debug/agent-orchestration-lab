# External Target Repo Invocation

## Purpose
This file defines how the orchestration control plane in this lab should invoke work against an external target repository.

The goal is to keep:
- the orchestration brain here;
- the target repo as an execution surface;
- legacy local agent packs inside target repos non-authoritative unless explicitly imported.

## Core rule
The lab is the control plane.
The target repo is the work surface.

Do not treat project-local legacy agent packs as the active orchestration authority when this protocol is used.

## Required invocation inputs
Every external target task must declare:

- `target_repo_path`
- `target_repo_name`
- `target_project_type`
- `task_objective`
- `requested_outcome`
- `best_current_locus`
- `task_surface_type`
- `allowed_target_read_scope`
- `allowed_target_change_scope`
- `donor_repo_path` (optional, read-only only when explicitly declared)

## Required authority order
When invoking work against an external target repo, use this authority order:

1. this lab's active orchestration layer
2. the target repo's truthful project-local files
3. the target repo's implementation files inside the declared bounded scope

Ignore:
- generic placeholders
- legacy local agent packs
- broad project scanning outside the declared scope

## Initial bounded workflow
1. confirm target repo presence
2. confirm bounded target scope
3. classify the task through the lab orchestration layer
4. activate only justified modules
5. inspect the target repo only inside declared scope
6. do not implement until routing and bounded locus are clear
7. report bounded completion or bounded refusal

## Output requirements
At minimum, the invocation result must state:
- target repo confirmed: yes / no
- routing complete: yes / no
- task_class
- profile_decision
- allowed_modules
- blocked_modules
- allowed_target_read_scope
- allowed_target_change_scope
- whether implementation is authorized

## Anti-drift rule
Do not silently inherit authority from files inside the target repo when the lab control plane is active.
