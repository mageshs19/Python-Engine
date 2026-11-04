# `converter/postprocess/update_storage_include_manager.py`

Source: [converter/postprocess/update_storage_include_manager.py](../../../../converter/postprocess/update_storage_include_manager.py) | 303 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `e7c5ed1eb395038715fdbf5e49d83687a980f1ef96711df7897928761e8e9f7b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`_ABEND_ONELINE` (L57), `_ABEND_VALUE_LINE` (L61), `_ABEND_77_HEADER_NAMED` (L65), `_PERFORM_SQLERROR` (L71), `_SQLERROR_HEADER` (L75), `_LEFT_SEQUENCE_WIDTH` (L81), `_RIGHT_SEQUENCE_START` (L82), `_RIGHT_SEQUENCE_END` (L83), `_FIXED_LINE_WIDTH` (L84)

## Import declarations

```python
from __future__ import annotations
import re
from converter.generators.sql_error_generator import SqlErrorGenerator
from converter.postprocess.cobol_update_standard_generator import CobolUpdateStandardGenerator
from converter.postprocess.storage_include.storage_include_injector import StorageIncludeInjector
from converter.postprocess.storage_include.storage_ws_injector import StorageWsInjector
from converter.postprocess.update_postprocess_line_utils import UpdatePostprocessLineUtils
from patterns.update_storage_include_patterns import LEGACY_77_DECLARATION_PATTERN_TEMPLATE
from rules.update_restart_rules import UPDATE_LEGACY_RESTART_WS_NAMES, UPDATE_RESTART_DIAGNOSTICS
from rules.update_standard_generator_templates import MSG_SQLERROR_FROM_COPYBOOK, MSG_SQLERROR_INJECTED, SQL_ERROR_INCLUDE_TOKEN, SQLERROR_PARAGRAPH_TEMPLATE, USE_SHARED_SQL_ERROR_GENERATOR
```

## Local dependency notes

- [converter/generators/sql_error_generator.py](../generators/sql_error_generator.md)
- [converter/postprocess/cobol_update_standard_generator.py](cobol_update_standard_generator.md)
- [converter/postprocess/storage_include/storage_include_injector.py](storage_include/storage_include_injector.md)
- [converter/postprocess/storage_include/storage_ws_injector.py](storage_include/storage_ws_injector.md)
- [converter/postprocess/update_postprocess_line_utils.py](update_postprocess_line_utils.md)
- [patterns/update_storage_include_patterns.py](../../patterns/update_storage_include_patterns.md)
- [rules/update_restart_rules.py](../../rules/update_restart_rules.md)
- [rules/update_standard_generator_templates.py](../../rules/update_standard_generator_templates.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `UpdateStorageIncludeManager` - L87-L303

```python
class UpdateStorageIncludeManager(StorageWsInjector, StorageIncludeInjector)
```

Manages update-program storage and include injection.

### `UpdateStorageIncludeManager.__init__` - L97-L104

```python
__init__(self, *, generator: CobolUpdateStandardGenerator, line_utils: UpdatePostprocessLineUtils) -> None
```

### `UpdateStorageIncludeManager._logical` - L110-L149

```python
_logical(line: str) -> str
```

Strip the fixed-format sequence areas, then strip whitespace.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[_RIGHT_SEQUENCE_START:_RIGHT_SEQUENCE_END].isdigit`, `text[:_LEFT_SEQUENCE_WIDTH].isdigit`, `text[_LEFT_SEQUENCE_WIDTH:].strip`, `text.lstrip`, `stripped[:_LEFT_SEQUENCE_WIDTH].isdigit`, `stripped[_LEFT_SEQUENCE_WIDTH:].strip`, `text.strip`.

Control points:

- L129: `if len(text) >= _FIXED_LINE_WIDTH and text[_RIGHT_SEQUENCE_START:_RIGHT_SEQUENCE_END].isdigit()`
- L135: `if len(text) >= _LEFT_SEQUENCE_WIDTH and text[:_LEFT_SEQUENCE_WIDTH].isdigit()`
- L143: `if len(stripped) >= _LEFT_SEQUENCE_WIDTH and stripped[:_LEFT_SEQUENCE_WIDTH].isdigit()`

### `UpdateStorageIncludeManager._field_reference_count` - L151-L156

```python
_field_reference_count(self, field_name: str, cobol_text: str) -> int
```

Observed calls (lexical order): `re.compile`, `re.escape`, `len`, `pattern.findall`.

### `UpdateStorageIncludeManager.remove_legacy_restart_working_storage` - L161-L233

```python
remove_legacy_restart_working_storage(self, cobol_text, diagnostics)
```

Observed calls (lexical order): `str`, `cobol_text.replace`, `cobol_text.replace('\r\n', '\n').replace`, `cobol_text.replace('\r\n', '\n').replace('\r', '\n').split`, `re.compile`, `LEGACY_77_DECLARATION_PATTERN_TEMPLATE.format`, `re.escape`, `len`, `self._logical`, `any`, `pattern.match`, `_ABEND_ONELINE.match`, `_ABEND_VALUE_LINE.match`, `_ABEND_77_HEADER_NAMED.match`, `named.group`, `self._logical(lines[look]).strip`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L181: `while index < total`
- L186: `if any((pattern.match(logical) for pattern in legacy_patterns))`
- L192: `if _ABEND_ONELINE.match(logical)`
- L198: `if _ABEND_VALUE_LINE.match(logical)`
- L205: `if named`
- L210: `while look < total and (not self._logical(lines[look]).strip())`
- L213: `if look < total and _ABEND_VALUE_LINE.match(self._logical(lines[look]))`
- L222: `if self._field_reference_count(field_name, cobol_text) <= 1`
- Another 1 conditions/loops exist in this source span.

### `UpdateStorageIncludeManager.ensure_sqlerror_paragraph` - L238-L291

```python
ensure_sqlerror_paragraph(self, cobol_text, diagnostics=None)
```

Append the SQLERROR routine once, if the program needs one.

Observed calls (lexical order): `str`, `_PERFORM_SQLERROR.search`, `_SQLERROR_HEADER.search`, `SQL_ERROR_INCLUDE_TOKEN.upper`, `text.upper`, `diagnostics.append`, `text.replace`, `text.replace('\r\n', '\n').replace`, `text.replace('\r\n', '\n').replace('\r', '\n').split`, `lines[-1].strip`, `lines.pop`, `lines.append`, `lines.extend`, `self._sql_error_lines`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L265: `if not _PERFORM_SQLERROR.search(text)`
- L269: `if _SQLERROR_HEADER.search(text)`
- L274: `if SQL_ERROR_INCLUDE_TOKEN.upper() in text.upper()`
- L275: `if diagnostics is not None`
- L282: `while lines and (not lines[-1].strip())`
- L288: `if diagnostics is not None`

### `UpdateStorageIncludeManager._sql_error_lines` - L293-L303

```python
_sql_error_lines(self) -> list[str]
```

The SQLERROR routine body, from the single shared generator.

Observed calls (lexical order): `SqlErrorGenerator`, `SqlErrorGenerator().paragraph_lines`, `list`.

Control points:

- L300: `if USE_SHARED_SQL_ERROR_GENERATOR`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
