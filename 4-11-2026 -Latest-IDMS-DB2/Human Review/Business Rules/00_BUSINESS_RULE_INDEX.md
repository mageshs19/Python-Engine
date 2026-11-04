# Human business-rule checklist

| Rule | When to use it | Human question |
|---|---|---|
| [BR-001](BR-001_UPDATE_RESTART_PROTOCOL.md) | Program updates DB2 and supports restart | Can the job restart without skipping or duplicating committed work? |
| [BR-002](BR-002_NESTED_PARENT_CHILD_RETRIEVAL.md) | Parent rows each have child traversal | Are all business-used parent/child values fetched and used for the correct parent? |
| [BR-003](BR-003_BOUNDED_LATEST_CHILD_SELECTION.md) | Navigation becomes “latest/first matching” SQL | Do filter, order, one-row behavior and no-row handling match the source? |
| [BR-004](BR-004_LEGACY_FIELD_MATERIALISATION.md) | DB2 values replace legacy record fields | Is each value converted/rebuilt in a compatible representation before business use? |
| [BR-005](BR-005_OUTPUT_RECORD_ARCHIVE_FLOW.md) | Program writes extract/archive records | Is each output record complete, correctly initialized and written only when eligible? |
| [BR-006](BR-006_DIRECT_KEYED_UPDATE.md) | CALC/FIND + MODIFY becomes UPDATE | Do key, SET fields and not-found/error behavior remain equivalent? |
