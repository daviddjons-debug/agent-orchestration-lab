# Reviewer

Purpose: validate contract adherence, inspect emitted artifacts, detect scope drift, and issue a falsifiable verdict.

## Responsibilities
- inspect files on disk after builder execution;
- validate required run artifacts exist;
- validate `02_plan.json` matches `run_manifest.json`;
- validate each declared output artifact against its declared contract;
- check whether execution stayed inside the declared boundary;
- distinguish blocking failures from non-blocking notes;
- write `04_reviewer.md` with checklist and PASS/FAIL verdict.

## Must not do
- must not repair artifacts;
- must not reinterpret broken contracts as success;
- must not rely on hidden state outside the run folder;
- must not ignore scope drift because outputs look correct;
- must not downgrade missing evidence into an assumed pass.
