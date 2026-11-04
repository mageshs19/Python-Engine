# BR-006 — Direct keyed update

## Applies when
Legacy CALC/FIND/OBTAIN locates one record and MODIFY updates that same business row without intervening navigation-dependent behavior.

## Generic algorithm
1. Resolve the exact target table and key predicates from mapping/DCLGEN/source key behavior.
2. Build SET columns only from source assignments that are active at MODIFY time.
3. Preserve source calculations/defaults and audit-field requirements.
4. Execute keyed UPDATE.
5. Interpret SQLCODE/row count according to the source not-found/error behavior.
6. Preserve transaction/restart sequencing if this update participates in a checkpoint protocol.

## Refuse / block when
The source depends on currency/set membership, zero-row semantics differ, multiple rows are possible, assignments cannot be correlated, or a direct UPDATE would remove an observable not-found/business branch.
