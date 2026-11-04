# `rules/manual_reference_rules.py`

Source: [rules/manual_reference_rules.py](../../../rules/manual_reference_rules.py) | 86 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `4d5325d5d910c2a7a1d89c7606fdf937fafc1c038d39e07d9367f5439a15c0d5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Manual COBOL reference standard constants.

## Module-level bindings

`REPLACE_IDENTIFICATION_HEADER` (L17), `IDENTIFICATION_RULE_LINE` (L19), `PROGRAM_ID_TEMPLATE` (L20), `AUTHOR_TEMPLATE` (L21), `DATE_WRITTEN_TEMPLATE` (L22), `DEFAULT_AUTHOR` (L28), `DEFAULT_DATE_WRITTEN` (L29), `BANNER_RULE` (L35), `BANNER_TITLE_TEMPLATE` (L36), `BANNER_OPEN_CURSOR` (L38), `BANNER_FETCH_CURSOR` (L39), `BANNER_CLOSE_CURSOR` (L40), `SECTION_BANNER_TEMPLATE` (L43), `SECTION_BANNER_WIDTH` (L44), `SECTION_BANNER_FILL` (L45), `SECTION_DB2_INCLUDE` (L47), `SECTION_DB2_VIEWS` (L48), `INLINE_BANNER_PREFIX` (L51), `INLINE_BANNER_TEMPLATE` (L52), `INLINE_BANNER_PARENT_READ` (L54), `INLINE_BANNER_CHILD_READ` (L55), `INLINE_BANNER_WRITE_CHECK` (L56), `CURSOR_BANNER_TITLE_TEMPLATE` (L61), `CURSOR_BANNER_UNDERLINE` (L62), `CURSOR_BANNER_BLANK` (L63), `EMIT_DEBUG_TRACE_LINES` (L68), `DEBUG_INDICATOR` (L69), `DEBUG_TRACE_TEMPLATE` (L70), `EMIT_COMMIT_IN_RETRIEVAL` (L78), `EMIT_PAGE_EJECT_BETWEEN_PARAGRAPHS` (L85), `PAGE_EJECT_INDICATOR` (L86)

## Import declarations

```python
from __future__ import annotations
from rules.program_metadata_loader import get_author, get_date_written
```

## Local dependency notes

- [rules/program_metadata_loader.py](program_metadata_loader.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/legacy_banner_builder.py](../converter/generators/cursor_declaration/legacy_banner_builder.md)
- [converter/transformers/cobol_identification_transformer.py](../converter/transformers/cobol_identification_transformer.md)
- [converter/transformers/idms_statement/control_statement_converter.py](../converter/transformers/idms_statement/control_statement_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
