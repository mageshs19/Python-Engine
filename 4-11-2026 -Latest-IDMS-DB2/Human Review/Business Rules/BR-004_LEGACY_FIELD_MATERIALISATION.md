# BR-004 — DB2 value to business field

For every legacy field used after database access, classify it:

```text
One DB2 scalar + compatible layout
    -> use/move DCLGEN value directly

DB2 DATE/TIME + legacy numeric/display date
    -> explicitly convert representation

One legacy group split across DB2 columns
    -> rebuild from proven components

CHAR width/type conflicts with packed/binary legacy group
    -> STOP; do not group-MOVE or truncate by guess
```

A COBOL group MOVE copies bytes. It does not convert display characters into COMP/COMP-3 values.

After conversion, no business statement should still depend on an undeclared old IDMS field merely because the mapped DB2 column was fetched.

## Generic fixes in V129
A statement containing one converted DB2 field can still contain another legacy field: each operand is checked separately. An unqualified scalar is converted only when metadata identifies one owner and it does not name local or copybook storage. A mapped date in a condition must pass through the established date conversion; changing the field name alone is insufficient. Ambiguous names and composite binary/display representation conflicts remain blockers.

A mapped DB2 date used in a comparison is realigned after field resolution, including when its DCLGEN group qualifier continues on the next fixed-format line.
