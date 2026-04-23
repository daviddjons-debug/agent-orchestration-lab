# Module Trigger Matrix

## Purpose
This file defines the initial evidence-based triggers for modules that are not always on.

It is the bridge between:
- default routing outcomes
- module activation decisions
- future skill attachment

These triggers are intentionally conservative.
A module should activate only when bounded evidence justifies it.

## Triggers

### review
Activate when:
- a patch was applied;
- `verify_only_surfaces` are declared;
- adjacent consistency is load-bearing;
- undeclared drift risk is non-zero;
- the task is not a trivial validated no-op.

Do not activate merely because review exists as a module.

### testing
Activate when:
- runnable behavior changed;
- the symptom can be validated through executable behavior;
- regression-sensitive surfaces are part of acceptance;
- the contract requires explicit behavior evidence.

Keep off when:
- the task is purely textual, structural, or documentary with no runnable behavior surface.

### security
Activate when:
- the task is explicitly security-sensitive;
- auth, permissions, secrets, trust boundaries, parsing boundaries, or network exposure are materially involved;
- the change could affect data exposure or privilege handling.

Keep off when:
- the task is a low-risk isolated local change with no real security dimension.

### browser_verification
Activate when:
- the task has a real UI/browser surface;
- the acceptance criteria include visible client-side behavior;
- bounded browser smoke validation is required to verify completion.

Keep off when:
- no browser-visible surface is involved.

### external_second_opinion
Activate when:
- blast-radius risk is medium or high;
- locus confidence is not high;
- reviewer-blocking evidence conflicts with the assumed path;
- a bounded contradiction check is justified before escalation or wider change;
- a previous local attempt failed without clearly resolving the blocker.

Keep off when:
- the task remains narrow, localized, and well-bounded with aligned evidence.

### release_packaging
Activate when:
- the task explicitly includes handoff, packaging, release, or shipment outputs;
- completion requires a bounded release note, delivery note, or operator-facing artifact bundle.

Keep off when:
- the task ends at bounded implementation/verification and no packaging output is required.

## Notes
- Triggers do not override the need for bounded scope.
- Trigger activation must still respect the selected profile and allowed modules.
- If trigger evidence materially changes the task shape, retriage is allowed and may be required.
