# Leo_Agents_V2

## Purpose
`Leo_Agents_V2` is the battle-ready portable orchestration runtime pack.

It is intended to be:
- the default orchestration authority for real projects;
- separate from the lab;
- minimal, bounded, and reusable;
- usable across multiple target repos without copying the full lab into each project.

## What this pack is
This pack is:
- a runtime control-plane;
- a portable bounded execution brain;
- a clean operational subset extracted from the lab.

## What this pack is not
This pack is not:
- the R&D lab;
- a historical archive;
- a validation-case corpus;
- a proof log;
- a full framework;
- a repo-wide autonomous agent swarm.

## Core operating rule
Do not start from broad implementation.

Start from:
1. bounded reading
2. bounded classification
3. bounded module activation
4. minimum justified change scope
5. honest completion or honest refusal

## Minimum reading spine
For normal runtime use, start with:
1. `START_HERE.md`
2. `docs/README.md`
3. `docs/HANDOFF_CONTRACT.md`
4. `docs/ACTIVATION_MATRIX.md`

Then load only the orchestration and adapter surfaces required for the current task.

## Main contents
- `docs/` — compact runtime canon
- `orchestration/router/` — routing layer
- `orchestration/profiles/` — execution profiles
- `orchestration/modules/` — modules and activation logic
- `orchestration/skills/` — bounded operational playbooks
- `orchestration/adapters/` — host-facing launch / invocation surfaces

## Expected project model
The runtime pack should be used together with:
- one target repo for execution
- optional truthful project-local files in that target repo
- optional donor repo only when explicitly declared

Do not duplicate this pack into every project by default.

## Authority model
1. `Leo_Agents_V2` = orchestration authority
2. truthful target-repo local files = project truth
3. target implementation files = bounded execution surface

## Anti-drift rule
Do not let legacy local agent packs override this runtime pack when this pack is the declared authority layer.
