# `converter/composers/paragraph_entry_display_composer.py`

Source: [converter/composers/paragraph_entry_display_composer.py](../../../../converter/composers/paragraph_entry_display_composer.py) | 119 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `031c0f89ad71ea04c92aac6f10229890b26942827d783749438f4ee26e4544b0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Ensure every local COBOL procedure paragraph has an active entry DISPLAY.

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/final_generated_output_service.py](../services/final_generated_output_service.md)
- [runners/audit_cursor_control_ownership.py](../../runners/audit_cursor_control_ownership.md)
- [tests/pipeline/test_single_owner_transformations.py](../../tests/pipeline/test_single_owner_transformations.md)
- [tests/test_generic_final_sql_location_and_timestamp_regression.py](../../tests/test_generic_final_sql_location_and_timestamp_regression.md)
- [tests/test_paragraph_entry_display_composer.py](../../tests/test_paragraph_entry_display_composer.md)
- [tests/test_schema_driven_4310_generic_rules.py](../../tests/test_schema_driven_4310_generic_rules.md)

## Symbol contracts and control points

### `_logical` - L12-L16

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `text[7:72].strip`, `text.strip`.

Control points:

- L14: `if len(text) >= 7 and text[:6].isdigit()`

### `_is_comment` - L19-L23

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L21: `if len(text) >= 7 and text[:6].isdigit() and (text[6] in '*/')`

### `_is_paragraph` - L26-L42

```python
_is_paragraph(line: str) -> bool
```

Observed calls (lexical order): `_is_comment`, `_logical`, `re.fullmatch`, `body[:-1].upper`, `word.startswith`, `str`, `len`, `raw[:6].isdigit`, `area.lstrip`.

Control points:

- L27: `if _is_comment(line)`
- L30: `if not re.fullmatch('[A-Z0-9][A-Z0-9-]*\\.', body, re.I)`
- L35: `if word.startswith('END-') or word in {'ELSE', 'CONTINUE', 'EXIT', 'GOBACK', 'NEXT', 'STOP', 'INITIALIZE', 'CANCEL', 'COMMIT', 'ROLLBACK', 'RETURN'}`

### `_format_body` - L45-L52

```python
_format_body(line: str, body: str, indicator: str | None=None) -> str
```

Observed calls (lexical order): `str`, `len`, `raw[:6].isdigit`, `ValueError`, `body.ljust`.

Control points:

- L47: `if len(raw) >= 7 and raw[:6].isdigit()`
- L48: `if len(body) > 65`

Explicit raises: `ValueError(f'paragraph DISPLAY exceeds fixed-format Area B: {body}')`.

### `ParagraphEntryDisplayComposer` - L55-L119

```python
class ParagraphEntryDisplayComposer()
```

Insert or normalize a paragraph-name DISPLAY at each local paragraph entry.

### `ParagraphEntryDisplayComposer.__init__` - L58-L59

```python
__init__(self) -> None
```

### `ParagraphEntryDisplayComposer.compose` - L61-L119

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `source.splitlines`, `next`, `enumerate`, `_logical`, `re.match`, `self.messages.append`, `_is_paragraph`, `len`, `range`, `list`, `reversed`, `_is_comment`, `re.fullmatch`, `is_entry_name.group`, `is_entry_name.group(2).upper`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L64: `if not source`
- L72: `if procedure_idx < 0`
- L77: `if not paragraph_starts`
- L84: `for start_idx in reversed(paragraph_starts)`
- L88: `while next_idx < len(output) and (not _logical(output[next_idx]) or _is_comment(output[next_idx]))`
- L90: `if next_idx < len(output)`
- L96: `if is_display and is_entry_name and (is_entry_name.group(2).upper() == name.upper())`
- L99: `if len(raw) >= 7 and raw[:6].isdigit() and (raw[6] in 'Dd')`
- Another 1 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
