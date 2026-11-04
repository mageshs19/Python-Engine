# `converter/ui/output_tabs.py`

Source: [converter/ui/output_tabs.py](../../../../converter/ui/output_tabs.py) | 371 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `e016c0787604c239183da73fb00d5fe1643a655a14de7c1eca23a73ee84cda9f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`_CLASSIFIER` (L60)

## Import declarations

```python
from __future__ import annotations
import csv
import io
import streamlit as st
from converter.analyzers.metadata_service import MetadataService
from converter.ui.message_classifier import ClassifiedMessage, MessageClassifier
from rules.validation_display_rules import COLUMN_CATEGORY, COLUMN_COUNT, COLUMN_FILE, COLUMN_MESSAGE, COLUMN_ROLE, COLUMN_SEVERITY, MESSAGE_TABLE_COLUMNS, SEVERITY_ERROR, SEVERITY_INFO, SEVERITY_ORDER, SEVERITY_WARNING, UI_CLEAN_RUN, UI_DIAGNOSTICS_HEADER, UI_DIAGNOSTICS_INTRO, UI_DOWNLOAD_DIAGNOSTICS, UI_DOWNLOAD_VALIDATION, UI_ERRORS_HEADER, UI_FILE_DIAGNOSTICS, UI_FILE_VALIDATION, UI_FILES_EMPTY, UI_FILES_HEADER, UI_FILTER_CATEGORY, UI_FILTER_SEARCH, UI_FILTER_SEARCH_PLACEHOLDER, UI_FILTER_SEVERITY, UI_INFO_CAPTION, UI_INFO_HEADER, UI_METRIC_ERRORS, UI_METRIC_INFO, UI_METRIC_TOTAL, UI_METRIC_WARNINGS, UI_MIME_CSV, UI_MIME_TEXT, UI_NO_MATCH, UI_NO_MESSAGES, UI_PARSER_EMPTY, UI_PARSER_HEADER, UI_RAW_HEADER, UI_VALIDATION_HEADER, UI_VALIDATION_INTRO, UI_WARNINGS_HEADER
```

## Local dependency notes

- [converter/analyzers/metadata_service.py](../analyzers/metadata_service.md)
- [converter/ui/message_classifier.py](message_classifier.md)
- [rules/validation_display_rules.py](../../rules/validation_display_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_page.py](main_page.md)

## Symbol contracts and control points

### `render_sheet_mapping_rows_tab` - L66-L78

```python
render_sheet_mapping_rows_tab() -> None
```

Observed calls (lexical order): `st.markdown`, `MetadataService`, `metadata_service.mapping_preview_rows`, `st.dataframe`, `st.info`.

Control points:

- L74: `if rows`

### `render_generated_cobol_tab` - L84-L109

```python
render_generated_cobol_tab() -> None
```

Observed calls (lexical order): `st.markdown`, `st.info`, `st.caption`, `st.download_button`, `st.text_area`.

Control points:

- L87: `if not st.session_state.converted_cobol`

### `render_validation_tab` - L115-L163

```python
render_validation_tab() -> None
```

Severity-aware validation report.

Observed calls (lexical order): `st.markdown`, `st.caption`, `st.session_state.get`, `st.info`, `_CLASSIFIER.classify_all`, `list`, `_CLASSIFIER.counts`, `_render_metrics`, `len`, `st.success`, `_render_filters`, `_render_band`, `_CLASSIFIER.of_severity`, `_render_info_band`, `st.download_button`, `_validation_csv`.

Control points:

- L127: `if not raw`
- L136: `if counts[SEVERITY_ERROR] == 0 and counts[SEVERITY_WARNING] == 0`
- L141: `if not filtered`

### `_render_metrics` - L166-L171

```python
_render_metrics(counts: dict[str, int], total: int) -> None
```

Observed calls (lexical order): `st.columns`, `columns[0].metric`, `columns[1].metric`, `columns[2].metric`, `columns[3].metric`.

### `_render_filters` - L174-L211

```python
_render_filters(items: list[ClassifiedMessage]) -> list[ClassifiedMessage]
```

Observed calls (lexical order): `st.columns`, `st.multiselect`, `list`, `_CLASSIFIER.categories`, `st.text_input`, `str`, `str(search or '').strip`, `str(search or '').strip().lower`, `item.text.lower`.

### `_render_band` - L214-L224

```python
_render_band(items: list[ClassifiedMessage], header: str, renderer) -> None
```

Observed calls (lexical order): `st.markdown`, `renderer`.

Control points:

- L219: `if not items`
- L223: `for item in items`

### `_render_info_band` - L227-L250

```python
_render_info_band(items: list[ClassifiedMessage]) -> None
```

Narration goes in a collapsed table, never eighty coloured boxes.

Observed calls (lexical order): `st.markdown`, `st.expander`, `UI_INFO_CAPTION.format`, `len`, `st.dataframe`, `list`.

Control points:

- L229: `if not items`

### `_validation_csv` - L253-L261

```python
_validation_csv(items: list[ClassifiedMessage]) -> str
```

Observed calls (lexical order): `io.StringIO`, `csv.writer`, `list`, `writer.writerow`, `buffer.getvalue`.

Control points:

- L258: `for item in items`

### `render_diagnostics_tab` - L267-L276

```python
render_diagnostics_tab() -> None
```

Parser diagnostics, grouped and searchable.

Observed calls (lexical order): `st.markdown`, `st.caption`, `_render_uploaded_files`, `_render_parser_diagnostics`.

### `_render_uploaded_files` - L279-L306

```python
_render_uploaded_files() -> None
```

Observed calls (lexical order): `st.markdown`, `st.session_state.get`, `st.info`, `uploaded.items`, `str`, `str(role).replace`, `str(role).replace('_', ' ').title`, `isinstance`, `rows.append`, `st.dataframe`.

Control points:

- L283: `if not uploaded`
- L288: `for (role, value) in uploaded.items()`
- L291: `if isinstance(value, (list, tuple, set))`
- L292: `for name in value`
- L294: `if value`
- L297: `if not rows`

### `_render_parser_diagnostics` - L309-L371

```python
_render_parser_diagnostics() -> None
```

Observed calls (lexical order): `st.markdown`, `st.session_state.get`, `st.info`, `_CLASSIFIER.classify_all`, `list`, `summary.get`, `st.dataframe`, `sorted`, `summary.items`, `st.text_input`, `str`, `str(search or '').strip`, `str(search or '').strip().lower`, `item.text.lower`, `st.expander`, `'\n'.join`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L313: `if not diagnostics`
- L320: `for item in items`
- L346: `if not visible`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
