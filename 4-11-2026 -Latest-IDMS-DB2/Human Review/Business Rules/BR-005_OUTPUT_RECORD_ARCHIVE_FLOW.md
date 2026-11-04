# BR-005 — Output / archive record

**Review logic:**
```text
For each eligible business row:
   initialize the complete output record
   populate all required fields
   perform required date/amount/key conversion
   WRITE exactly once
   increment the correct treated/output counter
```

Confirm exact fixed-record length, filler/remainder bytes, field population and the original WRITE guard. A WRITE must not fall through from a PERFORM THRU range when the source intended it to be conditional.
