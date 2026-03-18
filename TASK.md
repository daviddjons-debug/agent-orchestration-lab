# First Experiment

Goal: prove whether a 4-role workflow can produce a small result with visible handoffs and a falsifiable verdict.

Success criterion:
- every role leaves a separate artifact;
- reviewer verdict can be checked by a human in under 2 minutes;
- reviewer must produce PASS on the valid case and FAIL on the broken case.

Next hardening target:
- stop generating the whole run in one command;
- execute the workflow in distinct steps:
  1. orchestrator creates handoff;
  2. planner creates plan only from orchestrator handoff;
  3. builder creates artifact only from planner output;
  4. reviewer evaluates only from files on disk.
