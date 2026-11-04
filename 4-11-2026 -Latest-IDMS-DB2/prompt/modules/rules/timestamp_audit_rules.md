# `rules/timestamp_audit_rules.py`

Source: [rules/timestamp_audit_rules.py](../../../rules/timestamp_audit_rules.py) | 223 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `13eafa892acaaad2eafc5a14d86fafeb4a081a7e19a1c59956984d1a11d14cd5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`TIMESTAMP_AUDIT_RULES` (L3), `AUDIT_COLUMN_PREFIXES` (L14), `UPDATE_AUDIT_COLUMN_PREFIXES` (L24), `INSERT_EXCLUDE_AUDIT_PREFIXES` (L32), `DATE_COLUMN_PREFIXES` (L36), `TIMESTAMP_WS_MARKER` (L41), `TIMESTAMP_DEFAULT_PROGRAM_ID` (L42), `TIMESTAMP_PROGRAM_ID_LENGTH` (L43), `CS_PROGRAM_FIELD` (L45), `PROGRAM_NAME_FIELD` (L46), `PROGRAM_NAME_MOVE_TEMPLATE` (L47), `CS_PROGRAM_PICTURE` (L48), `CS_PROGRAM_PREFERRED_LEVEL` (L49), `CS_PROGRAM_FALLBACK_LEVEL` (L50), `CS_PROGRAM_LEVELS` (L51), `CS_PROGRAM_NAME_COLUMN` (L52), `CS_PROGRAM_PICTURE_COLUMN` (L53), `CS_PROGRAM_VALUE_COLUMN` (L54), `CS_PROGRAM_CHILD_INDENT` (L55), `PREFER_WORK_GROUP_FOR_CS_PROGRAM` (L56), `ALLOW_STANDALONE_CS_PROGRAM_FALLBACK` (L57), `CS_PROGRAM_TEMPLATE` (L59), `TIMESTAMP_CS_PROGRAM_TEMPLATE` (L64), `TIMESTAMP_WS_LINES` (L68), `TIMESTAMP_MOVE_FIELDS` (L100), `TIMESTAMP_PARAGRAPH_NAME` (L111), `TIMESTAMP_PARAGRAPH_EXIT_NAME` (L112), `TIMESTAMP_PARAGRAPH_HEADER_TEMPLATE` (L113), `TIMESTAMP_PARAGRAPH_DEBUG_TEMPLATE` (L114), `TIMESTAMP_PARAGRAPH_SOURCE_MOVE` (L115), `TIMESTAMP_PARAGRAPH_FIELD_MOVE_TEMPLATE` (L118), `TIMESTAMP_PARAGRAPH_DISPLAY` (L121), `TIMESTAMP_PARAGRAPH_TERMINATOR` (L122), `TIMESTAMP_PERFORM_TEMPLATE` (L123), `TIMESTAMP_MOVE_ALIGN_COLUMN` (L124), `EMIT_TIMESTAMP_DEBUG_LINE` (L125), `ENFORCE_PROGRAM_NAME_CONSTANT` (L126), `TIMESTAMP_MESSAGES` (L128), `__all__` (L179)

## Import declarations

```python
from __future__ import annotations
```

## Importers (10)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/cs_program_declarator.py](../converter/generators/timestamp/cs_program_declarator.md)
- [converter/generators/timestamp/program_id_resolver.py](../converter/generators/timestamp/program_id_resolver.md)
- [converter/generators/timestamp/program_name_binder.py](../converter/generators/timestamp/program_name_binder.md)
- [converter/generators/timestamp/timestamp_paragraph_builder.py](../converter/generators/timestamp/timestamp_paragraph_builder.md)
- [converter/generators/timestamp/timestamp_ws_builder.py](../converter/generators/timestamp/timestamp_ws_builder.md)
- [converter/generators/timestamp_generator.py](../converter/generators/timestamp_generator.md)
- [converter/resolvers/cursor_column_filter.py](../converter/resolvers/cursor_column_filter.md)
- [converter/resolvers/cursor_column_resolver.py](../converter/resolvers/cursor_column_resolver.md)
- [converter/services/update_audit_move_inserter.py](../converter/services/update_audit_move_inserter.md)
- [rules/initialization_placement_rules.py](initialization_placement_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
