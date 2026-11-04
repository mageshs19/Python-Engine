# `rules/cursor_paragraph_rules.py`

Source: [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.py) | 444 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `ba7f5da19ad042c79e74575b35e114b7dc68b2c989f44d798c0d0c1412f9da81`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor paragraph generation rules.

## Module-level bindings

`SQL_ERROR_PARAGRAPH_NAME` (L143), `LEGACY_SQL_ERROR_PARAGRAPH_NAME` (L144), `LONE_PERIOD` (L154), `ENFORCE_SQL_LOCATION_IN_ERROR_BRANCH` (L177), `BODY_FIRST_COLUMN` (L188), `BODY_LAST_COLUMN` (L189), `BODY_WIDTH` (L190), `COLUMN_STATEMENT` (L192), `COLUMN_SQL_BODY` (L193), `COLUMN_SQL_INTO` (L194), `COLUMN_SQL_INTO_NEXT` (L195), `COLUMN_WHEN` (L196), `COLUMN_WHEN_BODY` (L197), `IND_STATEMENT` (L199), `IND_SQL_BODY` (L200), `IND_SQL_INTO` (L201), `IND_SQL_INTO_NEXT` (L202), `IND_WHEN` (L203), `IND_WHEN_BODY` (L204), `TOKEN_EXEC_SQL` (L212), `TOKEN_END_EXEC` (L213), `TOKEN_EVALUATE_SQLCODE` (L214), `TOKEN_END_EVALUATE` (L215), `TOKEN_WHEN_ZERO` (L216), `TOKEN_WHEN_100` (L217), `TOKEN_WHEN_OTHER` (L218), `TOKEN_CONTINUE` (L219), `TOKEN_INTO` (L220), `TOKEN_HOST_SEPARATOR` (L221), `TOKEN_OF` (L222), `CURSOR_OPERATIONS` (L227), `CURSOR_EOC_SUFFIX` (L228), `CURSOR_NOT_EOC_SUFFIX` (L229), `CURSOR_FLAG_TEMPLATE` (L230), `COUNT_PARENT_FETCH_ONLY` (L259), `PARAGRAPH_HEADER_TEMPLATE` (L266), `OPEN_STATEMENT_TEMPLATE` (L267), `FETCH_STATEMENT_TEMPLATE` (L268), `CLOSE_STATEMENT_TEMPLATE` (L269), `SET_NOT_EOC_TEMPLATE` (L270), `SET_EOC_TEMPLATE` (L272), `DISPLAY_ERROR_TEMPLATE` (L273), `PERFORM_TEMPLATE` (L274), `COMMENT_BLOCK_TEMPLATE` (L275), `INTO_FIRST_TEMPLATE` (L276), `INTO_NEXT_TEMPLATE` (L277), `BANNER_RULE` (L282), `BANNER_TITLE_TEMPLATE` (L285), `BANNER_OPEN_CURSOR` (L287), `BANNER_FETCH_CURSOR` (L288), `BANNER_CLOSE_CURSOR` (L289), `EMIT_PARAGRAPH_BANNERS` (L291), `EMIT_DEBUG_TRACE_LINES` (L296), `DEBUG_INDICATOR` (L297), `DEBUG_TRACE_TEMPLATE` (L298), `DEBUG_BODY_INDENT` (L307), `DEBUG_SENTINEL` (L311), `EMIT_KEY_DIAGNOSTICS` (L320), `KEY_LABEL_SOURCE_MAPPING` (L324), `KEY_LABEL_SOURCE_HOST` (L325), `KEY_LABEL_SOURCE` (L326), `KEY_DISPLAY_TEMPLATE` (L329), `KEY_QUALIFIER_TEMPLATE` (L330), `KEY_LABEL_MIN_WIDTH` (L334), `ALIGN_KEY_QUALIFIER` (L337), `KEY_DIAGNOSTIC_LIMIT` (L341), `KEY_BODY_END_COLUMN` (L346), `KEY_HOST_TEMPLATE` (L348), `SKIP_UNQUALIFIED_KEY_HOSTS` (L350), `WRAP_KEY_DISPLAY` (L351), `KEY_DISPLAY_LITERAL_TEMPLATE` (L352), `COLUMN_KEY_CONTINUATION` (L353), `IND_KEY_CONTINUATION` (L354), `DCLGEN_TABLE_SUFFIX` (L355), `MAPPING_TABLE_SUFFIX` (L356), `MAPPING_TABLE_SEPARATOR` (L357), `KEY_DIAGNOSTIC_MESSAGES` (L359), `EMIT_JOIN_KEY_DIAGNOSTICS` (L389), `EMIT_FETCH_KEY_DIAGNOSTICS` (L390), `JOIN_KEY_DISPLAY_TEMPLATE` (L391), `FETCH_KEY_DISPLAY_TEMPLATE` (L392), `FETCH_KEY_WHERE_DISPLAY_TEMPLATE` (L393), `JOIN_KEY_QUALIFIER_TEMPLATE` (L394), `FETCH_KEY_HOST_TEMPLATE` (L395), `FETCH_KEY_DIAGNOSTIC_LIMIT` (L396), `FETCH_KEY_BODY_END_COLUMN` (L397), `FETCH_KEY_MESSAGES` (L398), `ERROR_OPEN_TEMPLATE` (L406), `ERROR_FETCH_TEMPLATE` (L407), `ERROR_CLOSE_TEMPLATE` (L408), `ENFORCE_FETCH_PROLOGUE` (L413), `INITIALIZE_HOST_GROUP_TEMPLATE` (L414), `HOST_GROUP_SEPARATOR` (L418), `HOST_REFERENCE_PREFIX` (L419), `DCLGEN_GROUP_PREFIX` (L420), `DIAG_NO_CURSOR_OPERATIONS` (L425), `DIAG_BLOCK_EXISTS` (L428), `DIAG_GENERATED_TEMPLATE` (L432), `DIAG_NO_HOST_VARIABLES_TEMPLATE` (L435), `STRIP_REDEFINES_SUFFIX_FROM_KEY_LABEL` (L444)

## Import declarations

```python
from __future__ import annotations
from catalogs.output_sections import DECLARE_SQL_LOCATION_FIELD
from rules.sql_location_rules import SQL_LOCATION_FIELD, SQL_LOCATION_NAME_TEMPLATE, SQL_LOCATION_NUMBER_PAD, SQL_LOCATION_NUMBER_TEMPLATE, SQL_LOCATION_USES_PARAGRAPH_NUMBER
```

## Local dependency notes

- [catalogs/output_sections.py](../catalogs/output_sections.md)
- [rules/sql_location_rules.py](sql_location_rules.md)

## Importers (12)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_error_branch.py](../converter/generators/cursor_paragraph/cursor_error_branch.md)
- [converter/generators/cursor_paragraph/cursor_fetch_paragraph.py](../converter/generators/cursor_paragraph/cursor_fetch_paragraph.md)
- [converter/generators/cursor_paragraph/cursor_host_reference.py](../converter/generators/cursor_paragraph/cursor_host_reference.md)
- [converter/generators/cursor_paragraph/cursor_key_diagnostics.py](../converter/generators/cursor_paragraph/cursor_key_diagnostics.md)
- [converter/generators/cursor_paragraph/cursor_line_geometry.py](../converter/generators/cursor_paragraph/cursor_line_geometry.md)
- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](../converter/generators/cursor_paragraph/cursor_paragraph_body_builder.md)
- [converter/generators/cursor_paragraph/cursor_perform_rewriter.py](../converter/generators/cursor_paragraph/cursor_perform_rewriter.md)
- [converter/generators/cursor_paragraph/cursor_sql_location.py](../converter/generators/cursor_paragraph/cursor_sql_location.md)
- [converter/generators/cursor_paragraph/cursor_statement_blocks.py](../converter/generators/cursor_paragraph/cursor_statement_blocks.md)
- [converter/generators/cursor_paragraph/join_key_label_resolver.py](../converter/generators/cursor_paragraph/join_key_label_resolver.md)
- [converter/generators/cursor_paragraph_generator.py](../converter/generators/cursor_paragraph_generator.md)
- [tests/test_fetch_error_diagnostics.py](../tests/test_fetch_error_diagnostics.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
