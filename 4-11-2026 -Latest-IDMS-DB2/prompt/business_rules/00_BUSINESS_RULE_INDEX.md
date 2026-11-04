# IDMS to DB2 business-rule index

These rules describe reusable business migration scenarios proven or exposed by the current source/manual/generated corpus. They are **not program-name rules**. Apply a rule only when source behavior and metadata satisfy its applicability conditions.

| Rule | Scenario | Core obligation |
|---|---|---|
| BR-001 | Update with restart/checkpoint | Preserve fresh-start/resume, durable checkpoint meaning, commit order and completion behavior. |
| BR-002 | Nested parent/child retrieval | Fetch every downstream-used value, bind child access to the current parent, and preserve complete-vs-early-stop traversal. |
| BR-003 | Bounded/latest child selection | Preserve filter, ordering, cardinality, no-row behavior and tie semantics when navigation collapses to a singleton SELECT. |
| BR-004 | Legacy field materialization and representation | Direct-use only compatible scalars; convert temporal values; reconstruct split groups; block conflicting serialized layouts. |
| BR-005 | Output-record/archive processing | Preserve eligibility guard, record initialization, complete fixed-record population, one-write-per-business-unit and counters. |
| BR-006 | Direct keyed update | Replace CALC/MODIFY with keyed UPDATE only when assignments, predicates and zero-row/error semantics are proven. |

Manual DB2 code is comparison evidence, not an automatic specification. When manual output conflicts with original IDMS behavior, mapping, DCLGEN or copybook evidence, preserve the conflict and block or review rather than copying the manual pattern.
