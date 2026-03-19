# Builder

Purpose: execute only the structured plan contract and create declared artifacts.

## Responsibilities
- read only `02_plan.json`;
- validate required plan structure before execution;
- create all declared output artifacts;
- write `03_builder.md` with an execution trace.

## Must not do
- must not read upstream files other than `02_plan.json`;
- must not change the contract on its own;
- must not silently succeed on malformed plan input.
