# `converter/transformers/lr_status_token_replacer.py`

Source: [converter/transformers/lr_status_token_replacer.py](../../../../converter/transformers/lr_status_token_replacer.py) | 230 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `558c91689324de1c7c6372d8e5a333d5abb13a8579ff72c13b76afe2cf82ba78`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Turns the DB-REC-FOUND token LrfPathExpander emits into a DB2 condition.

## Module-level bindings

`PROCEDURE_DIVISION_TOKEN` (L83), `COMMENT_INDICATORS` (L84), `DEFAULT_INDENT` (L85), `__all__` (L230)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.lrf_program_patterns import LR_STATUS_TOKEN_REPLACEMENT_PATTERN
from rules.lrf_conversion_rules import ENABLE_LR_STATUS_TOKEN_REPLACEMENT, LR_STATUS_TOKEN_MESSAGES, LR_STATUS_TOKEN_SQLCODE, RECORD_FOUND_TOKEN
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/lrf_program_patterns.py](../../patterns/lrf_program_patterns.md)
- [rules/lrf_conversion_rules.py](../../rules/lrf_conversion_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/lrf/test_lr_status_token_replacer.py](../../tests/lrf/test_lr_status_token_replacer.md)

## Symbol contracts and control points

### `LrStatusTokenReplacer` - L88-L227

```python
class LrStatusTokenReplacer()
```

Replaces the generated DB-REC-FOUND token with its SQLCODE test.

### `LrStatusTokenReplacer.__init__` - L91-L97

```python
__init__(self, *, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `LrStatusTokenReplacer.apply` - L100-L155

```python
apply(self, cobol_text: str) -> str
```

Observed calls (lexical order): `str`, `text.strip`, `LR_STATUS_TOKEN_REPLACEMENT_PATTERN.search`, `text.replace`, `text.replace('\r\n', '\n').replace`, `text.replace('\r\n', '\n').replace('\r', '\n').split`, `set`, `self._logical`, `logical.upper`, `output.append`, `self._is_comment`, `self._replace_tokens`, `unmapped.update`, `self._replace_body`, `sorted`, `self.messages.append`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L104: `if not text.strip() or not ENABLE_LR_STATUS_TOKEN_REPLACEMENT`
- L107: `if not LR_STATUS_TOKEN_REPLACEMENT_PATTERN.search(text)`
- L117: `for line in lines`
- L120: `if PROCEDURE_DIVISION_TOKEN in logical.upper()`
- L125: `if not in_procedure or self._is_comment(line) or (not logical)`
- L132: `if hits and new_logical != logical`
- L140: `for token in sorted(unmapped)`
- L145: `if not replaced`

### `LrStatusTokenReplacer._replace_tokens` - L159-L187

```python
_replace_tokens(logical: str) -> tuple[str, int, set[str]]
```

Substitute every mapped token. An unmapped token is LEFT.

Observed calls (lexical order): `set`, `LR_STATUS_TOKEN_REPLACEMENT_PATTERN.sub`.

### `LrStatusTokenReplacer._replace_tokens._replace` - L171-L182

```python
_replace(match) -> str
```

Observed calls (lexical order): `match.group`, `str`, `str(match.group('token') or '').upper`, `LR_STATUS_TOKEN_SQLCODE.get`, `missing.add`.

Control points:

- L177: `if condition is None`

### `LrStatusTokenReplacer._logical` - L190-L194

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `LrStatusTokenReplacer._is_fixed` - L196-L200

```python
_is_fixed(self, line: str) -> bool
```

Observed calls (lexical order): `bool`, `self.fixed_format.is_fixed_line`.

### `LrStatusTokenReplacer._body_indent` - L202-L210

```python
_body_indent(self, line: str) -> str
```

Observed calls (lexical order): `self._is_fixed`, `str`, `len`, `text.lstrip`, `self.fixed_format.split`, `body.lstrip`.

Control points:

- L203: `if not self._is_fixed(line)`

### `LrStatusTokenReplacer._replace_body` - L212-L220

```python
_replace_body(self, line: str, new_body: str) -> str
```

Observed calls (lexical order): `self._body_indent`, `new_body.strip`, `self._is_fixed`, `self.fixed_format.replace_body`.

Control points:

- L215: `if not self._is_fixed(line)`

### `LrStatusTokenReplacer._is_comment` - L223-L227

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L225: `if len(text) >= 7 and text[:6].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
