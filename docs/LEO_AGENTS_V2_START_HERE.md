# START_HERE

Read in this order:

1. `docs/README.md`
2. `docs/HANDOFF_CONTRACT.md`
3. `docs/ACTIVATION_MATRIX.md`

Then load only the orchestration and adapter surfaces required for the current task.

## Runtime rule
This pack is the orchestration authority layer.

Do not:
- broaden the task by default;
- invent architecture or scaffolding without repo truth;
- silently inherit authority from legacy local agent packs in target repos;
- activate extra modules merely because they exist.

## Required starting behavior
For every task:
1. classify the task
2. identify the best current locus
3. declare bounded read scope
4. declare bounded change scope
5. choose the minimum justified profile
6. activate only justified modules
7. do not implement until the bounded path is clear

## If a target repo is involved
Treat:
- this pack as orchestration authority;
- truthful project-local files in the target repo as project truth;
- target implementation files as bounded execution surface.

## If the task is unclear
Do not guess.
Return a bounded routing result or bounded refusal first.
