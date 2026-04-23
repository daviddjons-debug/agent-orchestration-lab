# Leo_Agents_V2 Export File List

## Purpose
Define the exact files that should be exported from the lab into the first clean runtime pack.

## Export from lab

### Root entry surfaces
- `README.md` -> runtime-pack `README.md` (rewrite/condense for runtime use)
- `docs/LEO_AGENTS_V2_EXTRACTION_PLAN.md` -> lab-only planning source, not exported as-is
- new runtime-pack `START_HERE.md` -> to be authored separately

### Core orchestration surfaces
- `orchestration/README.md`
- `orchestration/router/README.md`
- `orchestration/router/TASK_CLASS_DEFAULTS.md`
- `orchestration/profiles/README.md`
- `orchestration/modules/README.md`
- `orchestration/modules/ACTIVATION_MATRIX.md`
- `orchestration/modules/TRIGGER_MATRIX.md`

### Runtime skills
- `orchestration/skills/README.md`
- `orchestration/skills/MODULE_TO_SKILL_MAPPING.md`
- `orchestration/skills/review_false_locality_check.md`
- `orchestration/skills/testing_behavior_evidence_check.md`
- `orchestration/skills/external_second_opinion_contradiction_check.md`
- `orchestration/skills/browser_visible_behavior_check.md`
- `orchestration/skills/security_boundary_exposure_check.md`

### Host-facing adapters / launch surfaces
- `orchestration/adapters/vscode_codex_bounded_invocation.md`
- `orchestration/adapters/vscode_codex_launch_template.md`
- `orchestration/adapters/vscode_codex_audit_launch_template.md`
- `orchestration/adapters/vscode_codex_browser_ui_launch_template.md`
- `orchestration/adapters/vscode_codex_security_launch_template.md`
- `orchestration/adapters/external_target_repo_invocation.md`

## Do not export
- `docs/session_recaps/`
- `docs/validation_cases/`
- `docs/codex_eval/`
- `docs/runs/`
- `docs/baseline_v1/`
- `lab_cases/`
- `scripts/`
- obsolete / removed / duplicate canon files
- raw test evidence and generated artifacts

## Notes
- Export means “candidate for the runtime pack,” not “copy blindly without rewrite.”
- Root `README.md` and future `START_HERE.md` should be rewritten for runtime-pack use.
- The runtime pack should not carry the lab’s historical proof burden; it should carry only live operational authority.
