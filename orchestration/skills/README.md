# Skills Layer

## Purpose
This layer contains narrow reusable playbooks attached to modules.

A skill is:
- not a role;
- not a profile;
- not a free-floating prompt fragment.

A skill is a bounded operational playbook that attaches to:
- a module,
- a trigger condition,
- a narrow task surface.

## Rules
- Skills must stay narrow and load-bearing.
- Skills must not duplicate the full contract, profile, or routing system.
- Skills must not become a giant warehouse of generic prompts.
- A skill should exist only if it improves execution quality for a specific module and failure mode.

## First intended skill attachments
The initial target skills should attach to:

- `review`
- `testing`
- `external_second_opinion`

## Not yet materialized here
- individual skill files
- module-to-skill mapping
- skill activation rules
- host-specific skill invocation patterns
