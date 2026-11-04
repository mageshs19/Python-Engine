# BR-006 — Direct keyed UPDATE

**Use when:** IDMS locates one business row by key and then MODIFY changes it.

**Review logic:**
```text
Build WHERE from the proven source key
Build SET from values active at MODIFY
UPDATE one intended business row
Check SQL result
Preserve source not-found/error behavior
Participate in restart/commit protocol when applicable
```

Do not use this simplification if the source depends on IDMS currency/set membership, if multiple rows can match, or if zero updated rows have a business meaning that is not preserved.
