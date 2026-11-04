# `catalogs/sheet_mapping_schema.py`

Source: [catalogs/sheet_mapping_schema.py](../../../catalogs/sheet_mapping_schema.py) | 246 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `5708ea52d8e579f407dbad3e4aa0f6866541c18497d59203c1a5fb5dffb3acdc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sheet Mapping schema catalog.

## Module-level bindings

`SHEET_MAPPING_COLUMN_IDMS_TO_DB2_MAPPING` (L9), `SHEET_MAPPING_COLUMN_COBOL_RECORD_IDMS` (L10), `SHEET_MAPPING_COLUMN_COBOL_ZONE` (L11), `SHEET_MAPPING_COLUMN_IDMS_KEY` (L12), `SHEET_MAPPING_COLUMN_IDMS_PIC_CLAUSE` (L13), `SHEET_MAPPING_COLUMN_LENGTH_OF_FIELD_BYTES` (L14), `SHEET_MAPPING_COLUMN_FIELD_END_POSITION` (L15), `SHEET_MAPPING_COLUMN_DB2_KEY` (L16), `SHEET_MAPPING_COLUMN_NEW_DB2_RECORD` (L17), `SHEET_MAPPING_COLUMN_NEW_DB2_FIELD_NAME` (L18), `SHEET_MAPPING_COLUMN_NEW_DB2_DATA_TYPE` (L19), `SHEET_MAPPING_COLUMN_HOPEX_EXPRESSION_TYPE_REMARK` (L20), `SHEET_MAPPING_COLUMN_REMARKS` (L21), `SHEET_MAPPING_COLUMN_RELATION` (L22), `SHEET_MAPPING_COLUMN_REFERENCE_FIELD_NAME_COPYBOOK` (L23), `SHEET_MAPPING_COLUMN_REFERENCE_FIELD_PIC_CLAUSE` (L24), `SHEET_MAPPING_COLUMN_CROSS_APPLICATION_DB2_TABLE` (L25), `SHEET_MAPPING_COLUMN_CROSS_APPLICATION_DB2_FIELD_NAME` (L26), `SHEET_MAPPING_COLUMN_CROSS_APPLICATION_DB2_DATA_TYPE` (L27), `SHEET_MAPPING_COLUMN_BASETYPE` (L28), `SHEET_MAPPING_CANONICAL_COLUMNS` (L31), `SHEET_MAPPING_FIELD_ALIASES` (L55), `SHEET_MAPPING_MODEL_FIELD_MAP` (L207), `SHEET_MAPPING_HEADER_DETECTION_GROUPS` (L230)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/sheet_mapping/sheet_mapping_row_mapper.py](../converter/parsers/sheet_mapping/sheet_mapping_row_mapper.md)
- [tests/test_imports.py](../tests/test_imports.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
