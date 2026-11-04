# BR-001 — Update + restart

**Use when:** the program changes database data and stores restart/checkpoint state.

**Review logic:**
```text
Read restart state
IF fresh run
   start from first business item
ELSE
   restore the proven committed position
END-IF

Process business work
Save checkpoint for completed work
COMMIT at the proven transaction boundary

On error:
   do not advance checkpoint beyond uncommitted work
   preserve the SQL error and rollback when required
```

Check that the checkpoint means the same thing as the original program, resume does not skip/duplicate work, and completion is recorded correctly. A retrieval-only IDMS FINISH does not automatically mean DB2 COMMIT.

**Block if:** checkpoint meaning, key, ordering or commit sequence is unknown.

## Review clarification in V129
A COBOL period can close an IF implicitly. The scope reviewer now recognizes this, while continuing to reject unmatched END-IF statements. This correction does not certify restart ordering, checkpoint payloads or missing-row semantics. Singleton success/failure handling is not an end-of-cursor requirement merely because the source used logical records.
