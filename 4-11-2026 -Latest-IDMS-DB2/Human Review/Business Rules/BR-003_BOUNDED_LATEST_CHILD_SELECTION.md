# BR-003 — Latest / first matching child

**Use when:** repeated IDMS child navigation is intentionally replaced by one bounded SELECT.

**Review logic:**
```text
SELECT matching child
  using current parent keys
  using the same business filter
  ORDER BY the source-equivalent sequence
  FETCH FIRST ROW ONLY

IF no row
   perform the original no-child action
ELSE IF SQL error
   perform database error handling
END-IF
```

Check filter, ordering, tie behavior, selected fields and no-row behavior. Do not assume “latest” without evidence.
