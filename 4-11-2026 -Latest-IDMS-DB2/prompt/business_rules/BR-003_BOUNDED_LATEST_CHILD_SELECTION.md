# BR-003 — Bounded/latest child selection

## Applies when
Legacy navigation searches child rows until a business condition is met, and equivalent relational behavior can be expressed as a bounded singleton query.

## Generic algorithm
1. Preserve all parent-key predicates.
2. Preserve the child business filter.
3. Derive the ordering that makes the selected row equivalent to legacy FIRST/NEXT behavior.
4. Use a one-row bound only when that ordering/cardinality is supported.
5. Bind every selected value to the correct DCLGEN host.
6. Distinguish success, no matching child and SQL failure.
7. Preserve the original no-child business action; do not treat every +100 as a generic success/skip.

## Refuse / block when
Ordering/ties are not established, the source distinguishes partial/filtered child states that a singleton cannot represent, or path/LRF status semantics are missing.
