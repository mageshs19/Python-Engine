# `rules/sheet_mapping_parser_rules.py`

Source: [rules/sheet_mapping_parser_rules.py](../../../rules/sheet_mapping_parser_rules.py) | 64 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `42b9552c0ad14cfde7d4269e83926a4d5b2c4f83f5f063a189f027e7b156e910`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`CSV_TEXT_ENCODING` (L7), `XLSX_SUFFIX` (L8), `LEGACY_XLS_SUFFIX` (L9), `CSV_SAMPLE_LENGTH` (L12), `HEADER_SCAN_ROW_LIMIT` (L13), `HEADER_DEBUG_ROW_LIMIT` (L14), `DIAG_NO_FILE` (L17), `DIAG_FILE_NAME_TEMPLATE` (L18), `DIAG_FILE_SIZE_TEMPLATE` (L19), `DIAG_UNSUPPORTED_XLS` (L20), `DIAG_CSV_DECODED_LEN_TEMPLATE` (L23), `DIAG_CSV_SAMPLE_TEMPLATE` (L24), `DIAG_CSV_EMPTY` (L25), `DIAG_CSV_NO_ROWS` (L26), `DIAG_CSV_HEADERS_TEMPLATE` (L27), `DIAG_CSV_USEFUL_ROWS_TEMPLATE` (L28), `DIAG_XLSX_EMPTY` (L29), `DIAG_XLSX_USEFUL_ROWS_TEMPLATE` (L30), `DIAG_SHEET_NO_HEADER_TEMPLATE` (L31), `DIAG_SHEET_USEFUL_ROWS_TEMPLATE` (L34), `DIAG_SHEET_NORMALIZED_CELLS_TEMPLATE` (L35), `POPULATION_DIAGNOSTIC_SPEC` (L41), `USEFUL_CONTEXT_LABEL` (L58), `USEFUL_CONTEXT_GROUPS` (L59)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/sheet_mapping/sheet_mapping_diagnostics.py](../converter/parsers/sheet_mapping/sheet_mapping_diagnostics.md)
- [converter/parsers/sheet_mapping/sheet_mapping_row_mapper.py](../converter/parsers/sheet_mapping/sheet_mapping_row_mapper.md)
- [converter/parsers/sheet_mapping_parser.py](../converter/parsers/sheet_mapping_parser.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
