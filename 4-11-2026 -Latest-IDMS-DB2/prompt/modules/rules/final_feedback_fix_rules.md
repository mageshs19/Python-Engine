# `rules/final_feedback_fix_rules.py`

Source: [rules/final_feedback_fix_rules.py](../../../rules/final_feedback_fix_rules.py) | 81 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `5a7db0540ff79917d729c87597e70c0c5064c9fd7e0c55ac01324c91a8386cc4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Final feedback fix rules.

## Module-level bindings

`FINAL_FEEDBACK_FIX_RULES` (L15), `AREA_A_BODY_INDENT` (L24), `AREA_B_BODY_INDENT` (L25), `SQL_BODY_INDENT` (L26), `SUPPORTED_DB2_DATE_FORMATS` (L28), `DATE_FORMAT_ALIASES` (L34), `DEFAULT_DB2_DATE_EXTERNAL_FORMAT` (L48), `DB2_DATE_HELPER_BY_FORMAT` (L50), `DB2_DATE_LOW_LITERAL_BY_FORMAT` (L56), `DB2_DATE_HIGH_LITERAL_BY_FORMAT` (L62), `ORDER_BY_COLUMNS_IN_SELECT_DEFAULT` (L68), `FINAL_FIX_STRING_START_BODY_INDENT` (L72), `FINAL_FIX_STRING_CONTINUATION_BODY_INDENT` (L73), `FINAL_FIX_STRING_INTO_BODY_INDENT` (L74), `FINAL_FIX_AREA_B_INDENT` (L76), `FINAL_FIX_NESTED_INDENT` (L77), `AREA_B_CONTINUATION_BODY_INDENT` (L81)

## Import declarations

```python
from __future__ import annotations
```

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../converter/composers/final_cobol_fix_composer.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../converter/pipeline/conversion/conversion_component_factory.md)
- [converter/services/cobol_area_alignment_reflow.py](../converter/services/cobol_area_alignment_reflow.md)
- [converter/services/cobol_area_alignment_service.py](../converter/services/cobol_area_alignment_service.md)
- [converter/services/cursor_select_minimizer_service.py](../converter/services/cursor_select_minimizer_service.md)
- [converter/services/db2_date_format_service.py](../converter/services/db2_date_format_service.md)
- [converter/services/procedure_block_indent_service.py](../converter/services/procedure_block_indent_service.md)
- [converter/services/string_block_format_service.py](../converter/services/string_block_format_service.md)
- [tests/test_db2_date_format_service.py](../tests/test_db2_date_format_service.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
