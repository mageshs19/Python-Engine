# `catalogs/output_sections.py`

Source: [catalogs/output_sections.py](../../../catalogs/output_sections.py) | 145 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b6d2ebf2033c813e7e0db91b6639375b66d6ba019d6e3be3150893873ef47b21`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Output section titles and generated block markers.

## Module-level bindings

`DB2_INFRASTRUCTURE_MARKER` (L35), `DB2_SQL_ERROR_LOCATION_MARKER` (L39), `DB2_CURSOR_FLAGS_MARKER` (L41), `DB2_CURSOR_DECLARATIONS_MARKER` (L42), `DB2_CURSOR_PARAGRAPH_MARKER` (L43), `DB2_GENERATED_TIMESTAMP_MARKER` (L47), `DB2_GENERATED_WORKING_STORAGE_MARKER` (L54), `DB2_GENERATED_ROW_COUNTERS_MARKER` (L55), `COMMENT_BODY_WIDTH` (L74), `COMMENT_MARKER_TEMPLATE` (L75), `COMMENT_RULE_LINE` (L76), `DB2_INFRASTRUCTURE_MARKER_SHORT` (L79), `COMMENT_TITLE_WIDTH` (L81), `MARKER_SHORT_FORMS` (L85), `MARKER_TRUNCATION_SUFFIX` (L91), `MARKER_MESSAGES` (L93), `SQLERRWS_INCLUDE_NAME` (L107), `SQLCA_INCLUDE_NAME` (L108), `SQLERROR_INCLUDE_NAME` (L109), `INFRASTRUCTURE_INCLUDE_NAMES` (L112), `INCLUDE_SINGLE_LINE` (L122), `INCLUDE_STATEMENT_TEMPLATE` (L123), `SQL_LOCATION_FIELD_NAME` (L128), `SQL_LOCATION_PICTURE` (L129), `DECLARE_SQL_LOCATION_FIELD` (L139), `DCLGEN_GROUP_PREFIX` (L144), `DCLGEN_INITIALIZE_TEMPLATE` (L145)

## Import declarations

```python
from __future__ import annotations
```

## Importers (10)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/dclgen_include_cleanup.py](../converter/composers/cleanup/dclgen_include_cleanup.md)
- [converter/composers/manual_layout_composer.py](../converter/composers/manual_layout_composer.md)
- [converter/composers/restart/restart_storage_injector.py](../converter/composers/restart/restart_storage_injector.md)
- [converter/generators/cursor_paragraph_generator.py](../converter/generators/cursor_paragraph_generator.md)
- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](../converter/generators/db2_infrastructure/infrastructure_block_builder.md)
- [converter/generators/db2_infrastructure/sql_location_builder.py](../converter/generators/db2_infrastructure/sql_location_builder.md)
- [converter/generators/db2_infrastructure_generator.py](../converter/generators/db2_infrastructure_generator.md)
- [rules/cursor_paragraph_rules.py](../rules/cursor_paragraph_rules.md)
- [rules/structural_safety_rules.py](../rules/structural_safety_rules.md)
- [tests/test_marker_banner_width.py](../tests/test_marker_banner_width.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
