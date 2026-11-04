# `tests/test_parsers.py`

Source: [tests/test_parsers.py](../../../tests/test_parsers.py) | 96 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a38061910b77e647cf418593a6fcf7d602437605cb366d0b5e5b0b83cd49b2b4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.parsers.cobol_parser import CobolParser
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.sheet_mapping_parser import SheetMappingParser
```

## Local dependency notes

- [converter/parsers/cobol_parser.py](../converter/parsers/cobol_parser.md)
- [converter/parsers/copybook_parser.py](../converter/parsers/copybook_parser.md)
- [converter/parsers/dclgen_parser.py](../converter/parsers/dclgen_parser.md)
- [converter/parsers/sheet_mapping_parser.py](../converter/parsers/sheet_mapping_parser.md)

## Symbol contracts and control points

### `test_cobol_parser_detects_program_id` - L7-L10

```python
test_cobol_parser_detects_program_id()
```

Observed calls (lexical order): `CobolParser`, `parser.program_id`.

### `test_cobol_parser_detects_obtain_calc` - L13-L20

```python
test_cobol_parser_detects_obtain_calc()
```

Observed calls (lexical order): `CobolParser`, `parser.analyze`, `len`.

### `test_cobol_parser_detects_store` - L23-L30

```python
test_cobol_parser_detects_store()
```

Observed calls (lexical order): `CobolParser`, `parser.analyze`, `len`.

### `test_copybook_parser_parses_field` - L33-L44

```python
test_copybook_parser_parses_field()
```

Observed calls (lexical order): `CopybookParser`, `parser.parse`, `len`.

### `test_dclgen_parser_parses_inline_sql_declare` - L47-L69

```python
test_dclgen_parser_parses_inline_sql_declare()
```

Observed calls (lexical order): `DclgenParser`, `parser.parse`, `len`.

### `test_sheet_mapping_parser_detects_tab_delimited_csv_export` - L74-L83

```python
test_sheet_mapping_parser_detects_tab_delimited_csv_export()
```

Observed calls (lexical order): `SheetMappingParser`, `parser.parse_csv_text`, `len`.

### `test_sheet_mapping_parser_parses_csv_text` - L85-L96

```python
test_sheet_mapping_parser_parses_csv_text()
```

Observed calls (lexical order): `SheetMappingParser`, `parser.parse_csv_text`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
