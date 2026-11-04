# Human Review — IDMS to DB2 business logic

Use this folder to review migration behavior without reading Python. The rules describe **what must be preserved in COBOL/DB2**, not how the engine is coded.

Start with [Business Rules/00_BUSINESS_RULE_INDEX.md](Business%20Rules/00_BUSINESS_RULE_INDEX.md).

For each converted program:
1. Identify which scenarios apply from the original IDMS COBOL.
2. Review the matching business-rule cards.
3. Confirm generated DB2 behavior is logically equivalent; names and paragraph numbering do not need to match the manual program.
4. Treat manual DB2 as comparison evidence. Do not copy a manual defect over original source/metadata evidence.
5. Mark unresolved representation, relationship, restart or transaction meaning as a blocker rather than guessing.
