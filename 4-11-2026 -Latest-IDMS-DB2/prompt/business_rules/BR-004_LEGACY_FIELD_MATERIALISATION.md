# BR-004 — Legacy field materialization and representation

## Purpose
A DB2 FETCH is useful only if later COBOL receives the same business value in a compatible representation.

## Classify each downstream source field

### A. Compatible scalar
One source field maps uniquely to one DB2 column/host and representations are compatible.

**Rule:** downstream use may reference the DCLGEN host directly or move it to proven compatible business storage.

### B. Temporal representation
Legacy numeric/display date maps to DB2 DATE/TIME/TIMESTAMP storage.

**Rule:** generate an explicit representation conversion before legacy-format comparison/output. Preserve source-proven sentinel values and date ordering semantics.

### C. Composite / split field
One legacy group is represented by multiple DB2 columns.

**Rule:** reconstruct the legacy business value from mapped components only when component order, width and representation are proven. Do not invent a helper solely to imitate manual code; use existing compatible storage when safe.

### D. Serialized representation conflict
Mapping width/type, DCLGEN declaration and legacy group layout disagree, especially character hosts copied into COMP/COMP-3/binary groups.

**Rule:** block. A COBOL group MOVE copies bytes; it does not perform numeric serialization.

## Post-conversion check
If a mapped legacy source field is still used in PROCEDURE DIVISION but has no declared/materialized generated storage, fail review even if the DB2 cursor fetched its mapped column.
