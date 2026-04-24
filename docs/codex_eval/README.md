# Codex External Evaluation Artifacts

Authority note:
- `agent-orchestration-lab` is the R&D / validation / evidence lab;
- `Leo_Agents_V2` is the active exported authority/runtime pack for real project orchestration;
- this directory is historical/evaluation evidence, not current authority.

Purpose:
- store raw bounded external-evaluation prompts and responses for Codex behavior validation;
- preserve evaluator artifacts separately from canonical architecture docs;
- support later canon extraction without treating raw eval artifacts as contract truth.

Status:
- this directory is a raw evidence layer, not a canonical policy/contract layer;
- canonical conclusions belong in top-level docs such as `docs/agent_pack_v2_rule_extraction.md` and related session recaps.

Contents:
- `codex_smoke_pack_01_frozen_contract.md` — initial bounded external-eval prompt pack
- `codex_smoke_pack_02_min_patch_trap.md` — follow-up minimal-patch / no-patch trap
- `responses/` — saved model outputs tied to those eval packs

Rules:
- do not treat files here as source of truth for runtime semantics;
- do not edit runtime/docs based on these artifacts without proving a real mismatch in the live repo;
- prefer extracting durable conclusions into canonical docs rather than expanding this folder casually.
- this marker does not physically archive, move, or delete any eval artifact.
