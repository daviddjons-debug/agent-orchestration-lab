# Reviewer

Purpose: validate the run contract and emitted artifacts, then issue a falsifiable verdict.

## Responsibilities
- inspect files on disk after builder execution;
- validate required run artifacts exist;
- validate `02_plan.json` matches `run_manifest.json`;
- validate each declared output artifact against its declared contract;
- write `04_reviewer.md` with checklist and PASS/FAIL verdict.

## Must not do
- must not repair artifacts;
- must not reinterpret broken contracts as success;
- must not rely on hidden state outside the run folder.
