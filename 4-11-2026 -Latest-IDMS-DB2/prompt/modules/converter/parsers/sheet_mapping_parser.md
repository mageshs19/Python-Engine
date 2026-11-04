# `converter/parsers/sheet_mapping_parser.py`

Source: [converter/parsers/sheet_mapping_parser.py](../../../../converter/parsers/sheet_mapping_parser.py) | 171 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `cafe5e62fa6f99e52cc398c5ea74527f36694872be91c13b3c615268dee5f134`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import csv
from io import BytesIO, StringIO
from openpyxl import load_workbook
from converter.domain.models import SheetMappingRow
from converter.parsers.sheet_mapping.sheet_mapping_cell_utils import SheetMappingCellUtils
from converter.parsers.sheet_mapping.sheet_mapping_diagnostics import SheetMappingDiagnostics
from converter.parsers.sheet_mapping.sheet_mapping_row_mapper import SheetMappingRowMapper
from rules.sheet_mapping_parser_rules import CSV_SAMPLE_LENGTH, CSV_TEXT_ENCODING, DIAG_CSV_DECODED_LEN_TEMPLATE, DIAG_CSV_EMPTY, DIAG_CSV_HEADERS_TEMPLATE, DIAG_CSV_NO_ROWS, DIAG_CSV_SAMPLE_TEMPLATE, DIAG_CSV_USEFUL_ROWS_TEMPLATE, DIAG_FILE_NAME_TEMPLATE, DIAG_FILE_SIZE_TEMPLATE, DIAG_NO_FILE, DIAG_SHEET_NO_HEADER_TEMPLATE, DIAG_SHEET_USEFUL_ROWS_TEMPLATE, DIAG_UNSUPPORTED_XLS, DIAG_XLSX_EMPTY, DIAG_XLSX_USEFUL_ROWS_TEMPLATE, LEGACY_XLS_SUFFIX, XLSX_SUFFIX
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/parsers/sheet_mapping/sheet_mapping_cell_utils.py](sheet_mapping/sheet_mapping_cell_utils.md)
- [converter/parsers/sheet_mapping/sheet_mapping_diagnostics.py](sheet_mapping/sheet_mapping_diagnostics.md)
- [converter/parsers/sheet_mapping/sheet_mapping_row_mapper.py](sheet_mapping/sheet_mapping_row_mapper.md)
- [rules/sheet_mapping_parser_rules.py](../../rules/sheet_mapping_parser_rules.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/input_loader.py](../ui/input_loader.md)
- [review/runner/workspace_inputs.py](../../review/runner/workspace_inputs.md)
- [runners/batch/shared_input_loader.py](../../runners/batch/shared_input_loader.md)
- [runners/retrieval/retrieval_input_loader.py](../../runners/retrieval/retrieval_input_loader.md)
- [runners/update/update_input_loader.py](../../runners/update/update_input_loader.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_lrf_select_projection_analysis.py](../../tests/test_lrf_select_projection_analysis.md)
- [tests/test_mapping_filler_layout_regression.py](../../tests/test_mapping_filler_layout_regression.md)
- [tests/test_parsers.py](../../tests/test_parsers.md)

## Symbol contracts and control points

### `SheetMappingParser` - L40-L171

```python
class SheetMappingParser(SheetMappingCellUtils, SheetMappingRowMapper, SheetMappingDiagnostics)
```

Parses Sheet Mapping files from CSV/text or XLSX.

### `SheetMappingParser.__init__` - L53-L54

```python
__init__(self) -> None
```

### `SheetMappingParser.parse_uploaded_file` - L56-L87

```python
parse_uploaded_file(self, uploaded_file) -> list[SheetMappingRow]
```

Observed calls (lexical order): `self.diagnostics.append`, `str`, `str(uploaded_file.name or '').lower`, `uploaded_file.getvalue`, `DIAG_FILE_NAME_TEMPLATE.format`, `DIAG_FILE_SIZE_TEMPLATE.format`, `len`, `file_name.endswith`, `self.parse_xlsx_bytes`, `raw_bytes.decode`, `DIAG_CSV_DECODED_LEN_TEMPLATE.format`, `text[:CSV_SAMPLE_LENGTH].replace`, `text[:CSV_SAMPLE_LENGTH].replace('\r', '\\r').replace`, `DIAG_CSV_SAMPLE_TEMPLATE.format`, `self.parse_csv_text`.

Control points:

- L59: `if uploaded_file is None`
- L69: `if file_name.endswith(XLSX_SUFFIX)`
- L72: `if file_name.endswith(LEGACY_XLS_SUFFIX)`
- L81: `if text`

### `SheetMappingParser.parse_csv_text` - L89-L117

```python
parse_csv_text(self, text: str) -> list[SheetMappingRow]
```

Observed calls (lexical order): `str`, `str(text or '').strip`, `self.diagnostics.append`, `csv.Sniffer`, `csv.Sniffer().sniff`, `text.partition`, `StringIO`, `csv.reader`, `tuple`, `self._cell_to_string`, `DIAG_CSV_HEADERS_TEMPLATE.format`, `self._parse_data_rows`, `DIAG_CSV_USEFUL_ROWS_TEMPLATE.format`, `len`, `self._add_population_diagnostics`.

Control points:

- L90: `if not str(text or '').strip()`
- L104: `if not raw_rows`

### `SheetMappingParser.parse_xlsx_bytes` - L119-L160

```python
parse_xlsx_bytes(self, raw_bytes: bytes) -> list[SheetMappingRow]
```

Observed calls (lexical order): `self.diagnostics.append`, `load_workbook`, `BytesIO`, `list`, `worksheet.iter_rows`, `self._find_header_row`, `DIAG_SHEET_NO_HEADER_TEMPLATE.format`, `self._cell_to_string`, `self._parse_data_rows`, `DIAG_SHEET_USEFUL_ROWS_TEMPLATE.format`, `len`, `output.extend`, `DIAG_XLSX_USEFUL_ROWS_TEMPLATE.format`, `self._add_population_diagnostics`.

Control points:

- L120: `if not raw_bytes`
- L129: `for worksheet in workbook.worksheets`
- L131: `if not rows`
- L137: `if header_index < 0`

### `SheetMappingParser._parse_data_rows` - L162-L171

```python
_parse_data_rows(self, *, headers: list[str], data_rows) -> list[SheetMappingRow]
```

Observed calls (lexical order): `self._row_to_dict`, `self._to_mapping_row`, `self._has_useful_content`, `output.append`.

Control points:

- L166: `for row in data_rows`
- L169: `if self._has_useful_content(mapping_row)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
