# `rules/update_audit_repair_rules.py`

Source: [rules/update_audit_repair_rules.py](../../../rules/update_audit_repair_rules.py) | 140 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `bbf849db6f1da92b06fc5dce7261c688e996b42a53d11ff5328b8d964bd35810`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Constants for re-asserting the update audit MOVEs after restart injection.

## Module-level bindings

`ENFORCE_UPDATE_AUDIT_MOVES` (L28), `AUDIT_TIMESTAMP_COLUMN_PREFIXES` (L37), `AUDIT_USERID_COLUMN_PREFIXES` (L38), `AUDIT_TIMESTAMP_SOURCE_FIELD` (L52), `AUDIT_USERID_SOURCE_FIELD` (L53), `MOVE_TEMPLATE` (L58), `CONTINUATION_SPLIT_TOKEN` (L59), `SEQUENCE_WIDTH` (L67), `INDICATOR_INDEX` (L68), `BODY_START_INDEX` (L69), `BODY_END_INDEX` (L70), `LINE_WIDTH` (L71), `STATEMENT_INDENT` (L72), `CONTINUATION_INDENT` (L73), `EXEC_SQL_TOKEN` (L78), `END_EXEC_TOKEN` (L79), `UPDATE_VERB` (L80), `SET_KEYWORD` (L81), `BLOCK_SCAN_LIMIT` (L82), `PARAGRAPH_SCAN_LIMIT` (L83), `MESSAGES` (L88), `__all__` (L118)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update/update_audit_repair_composer.py](../converter/composers/update/update_audit_repair_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
