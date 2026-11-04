# BR-001 — Update with restart/checkpoint

## Applies when
The source performs database updates and uses restart/checkpoint state, or approved migration requirements explicitly require restart persistence.

## Generic algorithm
1. Determine the business unit considered complete: row, parent group, input record, batch unit, or another source-proven unit.
2. Read restart state before business processing.
3. Distinguish fresh start, valid resume, stale/invalid state and completed run.
4. Restore only state whose meaning is proven by source/manual/metadata.
5. Perform business SQL.
6. Persist checkpoint state representing the agreed completed position.
7. Commit only at the source-proven transaction boundary.
8. On failure, preserve the producing SQL diagnostic, rollback when required, and do not advance the checkpoint past uncommitted work.
9. At normal completion, write the source-equivalent completion state.

## Required invariants
- Checkpoint key uniquely identifies the intended run/partition.
- Resume predicate cannot silently skip or duplicate committed work.
- Business update and checkpoint ordering is explicit.
- Restart SQLCODE handling is operation-specific.
- A retrieval-only FINISH does **not** by itself create a DB2 COMMIT requirement.

## Refuse / block when
Checkpoint meaning, ordering, commit ownership, restart key, or replay semantics cannot be proven.
