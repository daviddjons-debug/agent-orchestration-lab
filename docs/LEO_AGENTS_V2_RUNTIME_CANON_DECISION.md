# Leo_Agents_V2 Runtime Canon Decision

## Decision
`Leo_Agents_V2` will include a **condensed runtime docs layer** rather than attempting a docs-free orchestration-only pack.

## Chosen runtime authority model
The runtime pack will contain:

- `README.md`
- `START_HERE.md`
- `docs/README.md`
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`

These are runtime authority surfaces.
They must be rewritten/condensed for runtime use and must not be full lab-history copies.

## Why this direction was chosen
A docs-free pack was rejected because current launch templates and adapters already depend on:
- `docs/README.md`
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`

Removing docs entirely would force:
- template breakage, or
- hidden canon migration into multiple orchestration files and prompts.

That would reduce clarity, not improve it.

## What this means
`Leo_Agents_V2` should be:
- self-consistent
- small
- operational
- not historically burdened

The runtime docs layer must carry only active authority, not lab proof history.

## What remains outside the runtime pack
Still excluded from `Leo_Agents_V2`:
- session recaps
- validation case corpus
- codex eval evidence
- lab scripts
- selftest harness
- generated run artifacts
- historical proof clutter

## Consequence for next steps
The next steps are now:

1. define the runtime-condensed `docs/README.md`
2. define the runtime-condensed `docs/HANDOFF_CONTRACT.md`
3. define the runtime-condensed `docs/ACTIVATION_MATRIX.md`
4. then define runtime-pack `README.md`
5. then define runtime-pack `START_HERE.md`

Do not build `START_HERE.md` before the condensed runtime canon is defined.
