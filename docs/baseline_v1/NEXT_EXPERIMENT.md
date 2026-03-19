# Next Experiment — Beyond the Multi-File Baseline

## Current state
The lab already proves a structured multi-file artifact contract:
- planner writes `02_plan.json` as the source of truth;
- builder creates multiple manifest-declared artifacts;
- reviewer validates both contract alignment and artifact contents;
- selftest covers valid, broken, restored, relaxed, and invalid-schema cases.

## Next goal
Move from a minimal multi-file proof to a richer contract that is still falsifiable and easy to audit.

## Candidate upgrade paths
1. **Richer JSON schema**
   - nested objects;
   - arrays with exact expectations;
   - stricter reviewer assertions.

2. **Additional artifact types**
   - add a second structured file;
   - validate mixed artifact sets under one run contract.

3. **Nested output topology**
   - require artifacts in subdirectories;
   - confirm builder and reviewer handle multi-path outputs correctly.

4. **Planner hardening**
   - validate planner output shape before builder execution;
   - make planner defects fail earlier and more explicitly.

5. **More realistic task shape**
   - preserve strict contracts while moving beyond toy content generation.

## Success criterion
The upgraded pipeline must still satisfy all of the following:
- valid runs pass end-to-end;
- corrupted contract or corrupted output fails deterministically;
- restored state passes again;
- the reason for failure is visible in the run artifacts and console output.
