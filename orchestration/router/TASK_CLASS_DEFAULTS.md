# Task Class Defaults

## Purpose
This file defines the initial default routing outcome for each supported task class.

It is the bridge between:
- task classification in `orchestration/router/`
- execution profiles in `orchestration/profiles/`
- module activation in `orchestration/modules/`

These are defaults, not irreversible locks.
Evidence may still escalate or narrow the path.

## Defaults

### narrow_bugfix
Default profile:
- `direct`

Default modules:
- `triage`
- `planning`
- `execution`

Trigger-based modules:
- `review`

Blocked by default:
- `testing`
- `security`
- `browser_verification`
- `external_second_opinion`
- `release_packaging`

### local_fix_with_adjacent_risk
Default profile:
- `lite`

Default modules:
- `triage`
- `planning`
- `execution`
- `review`

Trigger-based modules:
- `testing`
- `external_second_opinion`

Blocked by default:
- `security`
- `browser_verification`
- `release_packaging`

### bounded_multi_file_patch
Default profile:
- `lite`

Default modules:
- `triage`
- `planning`
- `execution`
- `review`

Trigger-based modules:
- `testing`
- `external_second_opinion`

Blocked by default:
- `security`
- `browser_verification`
- `release_packaging`

### regression_sensitive_change
Default profile:
- `heavy`

Default modules:
- `triage`
- `planning`
- `execution`
- `review`

Trigger-based modules:
- `testing`
- `external_second_opinion`

Blocked by default:
- `security`
- `browser_verification`
- `release_packaging`

### security_sensitive_change
Default profile:
- `heavy`

Default modules:
- `triage`
- `planning`
- `execution`
- `review`

Trigger-based modules:
- `testing`
- `security`
- `external_second_opinion`

Blocked by default:
- `browser_verification`
- `release_packaging`

### justified_local_hardening
Default profile:
- `lite`

Default modules:
- `triage`
- `planning`
- `execution`
- `review`

Trigger-based modules:
- `testing`
- `security`
- `external_second_opinion`

Blocked by default:
- `browser_verification`
- `release_packaging`

### bounded_consistency_audit
Default profile:
- `lite`

Default modules:
- `triage`
- `planning`
- `review`

Trigger-based modules:
- `external_second_opinion`

Blocked by default:
- `execution`
- `testing`
- `security`
- `browser_verification`
- `release_packaging`

### no_change_verification
Default profile:
- `direct`

Default modules:
- `triage`
- `planning`
- `review`

Trigger-based modules:
- `external_second_opinion`

Blocked by default:
- `execution`
- `testing`
- `security`
- `browser_verification`
- `release_packaging`

### unknown
Default profile:
- `heavy`

Default modules:
- `triage`
- `planning`

Trigger-based modules:
- `execution`
- `review`
- `testing`
- `security`
- `browser_verification`
- `external_second_opinion`
- `release_packaging`

Blocked by default:
- none until the task is reclassified, but execution should not begin while the task remains `unknown`

## Notes
- `unknown` is not a normal execution class; it is a re-triage state.
- Browser verification stays off by default unless the task has a real UI/browser surface.
- Release packaging stays off by default unless the task explicitly includes handoff or shipment outputs.
- Security is not auto-on except where the task class itself is security-sensitive or evidence forces activation.
