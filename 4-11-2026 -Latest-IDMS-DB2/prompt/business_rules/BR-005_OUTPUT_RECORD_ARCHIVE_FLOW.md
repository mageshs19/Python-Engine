# BR-005 — Output-record/archive processing

## Applies when
The source writes fixed-format extract/archive/output records from retrieved database data.

## Generic algorithm
1. Prove the output record length from FD/copybook/materialized layout.
2. Initialize the output record at the source-equivalent per-record boundary.
3. Populate every business-required field from compatible DB2/business storage.
4. Preserve date/amount/identifier transformations before writing.
5. Preserve the source eligibility condition around WRITE.
6. Ensure a helper paragraph is not physically inside an unrelated PERFORM THRU range that can cause fall-through writes.
7. Increment treated/output counters at the same business event as the successful logical write.
8. Preserve filler/remainder storage needed to maintain exact record geometry.

## Refuse / block when
Output layout is incomplete, a required field has no proven source value, record width is unresolved, or a WRITE can occur outside its source business guard.
