# BR-002 — Parent/child retrieval

**Use when:** IDMS reads parent rows and then reads children for each parent.

**Review logic:**
```text
FOR each parent
   fetch every parent value used later
   open/read children using this parent's key
   fetch every child value used later
   process children until source-defined end
   close/reset child state
END-FOR
```

Do not require an extra early-stop flag unless the original IDMS logic had an additional business stop condition. Complete child traversal is valid.

A serious defect exists when SQL fetches a DB2 host but later COBOL still reads an undeclared old IDMS field. The value has not reached the business logic.

**Block if:** parent/child ownership, field mapping or required order cannot be proven.
