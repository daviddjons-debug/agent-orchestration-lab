# Project Validation Targets

## Minimum load-bearing validation surfaces
- orchestration/README.md accurately states the checkpoint scope
- overlay minimum files exist in orchestration/overlays/project/
- overlay files contain truthful bootstrap content rather than empty placeholders

## Acceptance evidence
- on-disk orchestration skeleton exists
- overlay files are non-empty
- no existing runtime/docs layers are rewritten beyond the bounded checkpoint need

## Adjacent / verify-only surfaces
- docs/PORTABLE_MODE_CANON.md
- docs/PROJECT_OVERLAY_MINIMUM.md
- docs/PORTABLE_PACK_LAYOUT.md

## Completion rule
This checkpoint is complete only if the on-disk skeleton remains explicitly minimal and does not overclaim implementation status.
