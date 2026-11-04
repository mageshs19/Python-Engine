# `converter/ui/input_loader.py`

Source: [converter/ui/input_loader.py](../../../../converter/ui/input_loader.py) | 352 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `e6bdffd451f675d3c37b632c8ff42a09bdc58cb3a02843d93d3b79252236c259`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
import streamlit as st
from converter.infrastructure.file_loader import FileLoader
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from converter.ui.session_state import reset_generated_output_state
from converter.parsers.lrf_parser import LrfParser
from rules.lrf_rules import DIAG_LRF_FILE_COUNT_TEMPLATE, DIAG_LRF_FILE_TEMPLATE, DIAG_LRF_NOT_UPLOADED, DIAG_LRF_PARSED_ZERO, DIAG_LRF_PARSE_FAILED_TEMPLATE, DIAG_LRF_READ_FAILED_TEMPLATE, DIAG_LRF_TEXT_LEN_TEMPLATE, LRF_SOURCE_LABEL
```

## Local dependency notes

- [converter/infrastructure/file_loader.py](../infrastructure/file_loader.md)
- [converter/parsers/copybook_parser.py](../parsers/copybook_parser.md)
- [converter/parsers/dclgen_parser.py](../parsers/dclgen_parser.md)
- [converter/parsers/lrf_parser.py](../parsers/lrf_parser.md)
- [converter/parsers/sheet_mapping_parser.py](../parsers/sheet_mapping_parser.md)
- [converter/ui/session_state.py](session_state.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_tab.py](main_tab.md)

## Symbol contracts and control points

### `load_and_analyze_inputs` - L31-L112

```python
load_and_analyze_inputs(sheet_mapping_file, dclgen_files, copybook_files, lrf_files=None, idms_cobol_source_file=None) -> None
```

Observed calls (lexical order): `FileLoader`, `SheetMappingParser`, `DclgenParser`, `CopybookParser`, `LrfParser`, `diagnostics.append`, `_load_sheet_mapping`, `_load_dclgen_files`, `_load_copybook_files`, `_load_lrf_files`, `_load_idms_cobol_source`, `reset_generated_output_state`, `bool`, `idms_cobol_text.strip`, `st.success`, `st.warning`.

Control points:

- L106: `if required_inputs_loaded`

### `_load_sheet_mapping` - L114-L139

```python
_load_sheet_mapping(*, sheet_mapping_file, parser: SheetMappingParser, diagnostics: list[str], uploaded_file_names: dict[str, object]) -> list
```

Observed calls (lexical order): `diagnostics.append`, `str`, `parser.parse_uploaded_file`, `len`, `hasattr`, `diagnostics.extend`.

Control points:

- L121: `if sheet_mapping_file is None`
- L132: `if hasattr(parser, 'diagnostics')`

### `_load_dclgen_files` - L142-L196

```python
_load_dclgen_files(*, dclgen_files, file_loader: FileLoader, parser: DclgenParser, diagnostics: list[str], uploaded_file_names: dict[str, object]) -> list
```

Observed calls (lexical order): `diagnostics.append`, `len`, `enumerate`, `str`, `file_names.append`, `file_loader.read_uploaded_text`, `texts.append`, `hasattr`, `parser.parse_many_texts`, `parser.parse`, `columns.extend`, `diagnostics.extend`.

Control points:

- L150: `if not dclgen_files`
- L159: `for (index, file) in enumerate(dclgen_files, start=1)`
- L175: `if hasattr(parser, 'parse_many_texts')`
- L180: `for (index, text) in enumerate(texts, start=1)`
- L189: `if hasattr(parser, 'diagnostics')`

### `_load_copybook_files` - L199-L260

```python
_load_copybook_files(*, copybook_files, file_loader: FileLoader, parser: CopybookParser, diagnostics: list[str], uploaded_file_names: dict[str, object]) -> list
```

Observed calls (lexical order): `diagnostics.append`, `len`, `enumerate`, `str`, `file_names.append`, `file_loader.read_uploaded_text`, `text_parts.append`, `Path`, `Path(file_name).stem.upper`, `'\n'.join`, `copybook_text.strip`, `parser.parse`, `hasattr`, `diagnostics.extend`.

Control points:

- L207: `if not copybook_files`
- L218: `for (index, file) in enumerate(copybook_files, start=1)`
- L237: `if not copybook_text.strip()`
- L252: `if hasattr(parser, 'diagnostics')`

### `_load_idms_cobol_source` - L263-L285

```python
_load_idms_cobol_source(*, idms_cobol_source_file, file_loader: FileLoader, diagnostics: list[str], uploaded_file_names: dict[str, object]) -> tuple[str, str]
```

Observed calls (lexical order): `diagnostics.append`, `str`, `file_loader.read_uploaded_text`, `len`.

Control points:

- L270: `if idms_cobol_source_file is None`

### `_load_lrf_files` - L290-L352

```python
_load_lrf_files(*, lrf_files, file_loader: FileLoader, parser: LrfParser, diagnostics: list[str], uploaded_file_names: dict[str, object]) -> list
```

Observed calls (lexical order): `diagnostics.append`, `DIAG_LRF_FILE_COUNT_TEMPLATE.format`, `len`, `enumerate`, `str`, `file_names.append`, `file_loader.read_uploaded_text`, `text_parts.append`, `DIAG_LRF_FILE_TEMPLATE.format`, `DIAG_LRF_TEXT_LEN_TEMPLATE.format`, `DIAG_LRF_READ_FAILED_TEMPLATE.format`, `'\n'.join`, `lrf_text.strip`, `parser.parse`, `hasattr`, `diagnostics.extend`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L298: `if not lrf_files`
- L307: `for (index, file) in enumerate(lrf_files, start=1)`
- L327: `if not lrf_text.strip()`
- L340: `if hasattr(parser, 'diagnostics')`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
