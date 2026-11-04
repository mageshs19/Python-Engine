# BR-002 — Nested parent/child retrieval

## Applies when
IDMS navigates a parent collection and, for each parent, navigates one or more child records/sets.

## Generic algorithm
1. Identify the parent key and every parent field used after retrieval.
2. Build the parent DB2 SELECT/cursor projection from those downstream uses, not only relationship keys.
3. For each fetched parent, bind the child query from that **current parent**.
4. Project every child field used by business logic, conditions, output, calculations or later calls.
5. Reset child status/data state before each parent where stale state could leak.
6. Iterate child rows until the source-defined end condition.
7. Add a business early-stop condition only if the original source has one. A plain IDMS end/status loop means complete traversal.
8. Close child and parent cursor paths on normal and error exits as required.

## Critical verification
A SELECT/FETCH count match is insufficient. If downstream COBOL still reads an undeclared legacy IDMS field while the corresponding DB2 host was fetched, the business value is not materialized and the conversion fails.

## Refuse / block when
Field ownership is ambiguous, parent/child relationship metadata is unresolved, ordering affects behavior but is unknown, or a mapped business field cannot be safely materialized.
