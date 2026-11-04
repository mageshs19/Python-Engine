# `converter/composers/db2_date_line_utils.py`

Source: [converter/composers/db2_date_line_utils.py](../../../../converter/composers/db2_date_line_utils.py) | 55 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `a62ede77fdbe6420a283c6d11985fd640870f2077503dabf762d93c76849bc44`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date line utilities.

## Import declarations

```python
from patterns.sequence_patterns import strip_sequence_numbers
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/db2_date_comparison_composer.py](db2_date_comparison_composer.md)
- [converter/composers/db2_date_comparison_rewriter.py](db2_date_comparison_rewriter.md)
- [converter/composers/db2_date_condition_assembler.py](db2_date_condition_assembler.md)
- [converter/composers/db2_date_field_detector.py](db2_date_field_detector.md)
- [converter/composers/db2_date_working_storage_manager.py](db2_date_working_storage_manager.md)
- [converter/composers/schema_date_transfer_composer.py](schema_date_transfer_composer.md)

## Symbol contracts and control points

### `Db2DateLineUtils` - L12-L55

```python
class Db2DateLineUtils()
```

### `Db2DateLineUtils.normalize_line_endings` - L13-L14

```python
normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `Db2DateLineUtils.logical` - L16-L17

```python
logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

### `Db2DateLineUtils.is_comment_or_blank` - L19-L25

```python
is_comment_or_blank(self, logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `stripped.startswith`.

Control points:

- L22: `if not stripped`

### `Db2DateLineUtils.leading_spaces_from_line` - L27-L42

```python
leading_spaces_from_line(self, line: str, default: str='') -> str
```

Observed calls (lexical order): `str`, `len`, `value.lstrip`.

Control points:

- L34: `if not value`
- L39: `if count <= 0`

### `Db2DateLineUtils.clean_cobol_name` - L44-L52

```python
clean_cobol_name(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `text.replace`, `text.rstrip`.

Control points:

- L49: `while ' ' in text`

### `Db2DateLineUtils.helper_name` - L54-L55

```python
helper_name(self, field_name: str) -> str
```

Observed calls (lexical order): `self.clean_cobol_name`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
