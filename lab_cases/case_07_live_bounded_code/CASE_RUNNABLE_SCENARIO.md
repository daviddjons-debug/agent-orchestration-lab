# Case 07 Runnable Scenario

## Scenario type
Bounded live code-level validation case using a persistent substrate.

## Proposed task shape
A narrow change is proposed in `src/parser.py`.

The change may look locally successful if judged only by direct parser output, but trustworthy completion must still depend on verify-only evidence tied to the adjacent surface.

## Scenario boundary
### Primary target
- `src/parser.py`

### Adjacent read node
- `src/adjacent_contract.py`

### Verify-only surface
- `src/verify_only_status.txt`

### No-change expectation
The initial bounded pass should avoid modifying:
- `src/adjacent_contract.py`

## Expected orchestration behavior
The system should:
1. localize `src/parser.py` as the most likely intervention node;
2. read `src/adjacent_contract.py` as the nearest adjacent dependency surface;
3. keep the change set narrow unless stronger evidence appears;
4. treat `src/verify_only_status.txt` as required completion evidence;
5. refuse a trustworthy pass if verify-only evidence remains stale.

## Failure mode this case should expose
A superficially successful local fix in `src/parser.py` must not be accepted as trustworthy completion when verify-only status is still pending.

## Status
Runnable scenario drafted.
Execution contract not yet bound into runtime.
