# `converter/transformers/idms_residual_cleanup.py`

Source: [converter/transformers/idms_residual_cleanup.py](../../../../converter/transformers/idms_residual_cleanup.py) | 409 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `238efe96f60e713b712007700784bcf63a75c69e7c809a426f206b20aa8a9289`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Removes residual IDMS lines the main converters leave behind.

## Module-level bindings

`_LITERAL_PATTERN` (L102), `_PUNCTUATION` (L105), `_DISPLAY_VERB_PATTERN` (L109), `__all__` (L407)

## Import declarations

```python
from __future__ import annotations
import re
from patterns.cobol_cleanup_patterns import ERROR_STATUS_MOVE_PATTERN
from patterns.cobol_transformer_patterns import BIND_STATEMENT_PATTERN, EXIT_LINE_PATTERN, FIND_CURRENT_STATEMENT_PATTERN, FINISH_STATEMENT_PATTERN, IDMS_ABORT_PARAGRAPH_PATTERN, IDMS_DECLARATIVE_PATTERNS, IDMS_EXECUTABLE_PATTERNS, ON_ANY_ERROR_STATUS_PATTERN
from patterns.idms_patterns import DISPLAY_STATEMENT_PATTERN, MOVE_TO_STATEMENT_PATTERN, REMOVED_COPYBOOK_FIELD_PATTERN
from rules.idms_transformer_messages import ERROR_STATUS_MOVE_OWNED_ELSEWHERE, REMOVED_FIELD_LINE_TEMPLATE, REMOVED_FIELD_REFUSED_TEMPLATE
```

## Local dependency notes

- [patterns/cobol_cleanup_patterns.py](../../patterns/cobol_cleanup_patterns.md)
- [patterns/cobol_transformer_patterns.py](../../patterns/cobol_transformer_patterns.md)
- [patterns/idms_patterns.py](../../patterns/idms_patterns.md)
- [rules/idms_transformer_messages.py](../../rules/idms_transformer_messages.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_transformer.py](cobol_transformer.md)

## Symbol contracts and control points

### `IdmsResidualCleanup` - L112-L404

```python
class IdmsResidualCleanup()
```

Detects and removes residual IDMS lines.

### `IdmsResidualCleanup.__init__` - L120-L121

```python
__init__(self) -> None
```

### `IdmsResidualCleanup.reset` - L123-L129

```python
reset(self) -> None
```

Drop diagnostics from the previous program.

### `IdmsResidualCleanup.is_idms_declarative_or_control` - L134-L144

```python
is_idms_declarative_or_control(self, logical_line: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `str(logical_line or '').strip().rstrip`, `pattern.search`.

Control points:

- L140: `for pattern in IDMS_DECLARATIVE_PATTERNS`
- L141: `if pattern.search(statement)`

### `IdmsResidualCleanup.removed_declarative_lines` - L146-L153

```python
removed_declarative_lines(self, logical_line: str) -> list[str]
```

### `IdmsResidualCleanup.is_idms_executable_cleanup` - L158-L168

```python
is_idms_executable_cleanup(self, logical_line: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `str(logical_line or '').strip().rstrip`, `pattern.search`.

Control points:

- L164: `for pattern in IDMS_EXECUTABLE_PATTERNS`
- L165: `if pattern.search(statement)`

### `IdmsResidualCleanup.removed_executable_lines` - L170-L216

```python
removed_executable_lines(self, *, logical_line: str, current_division: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `FINISH_STATEMENT_PATTERN.search`, `BIND_STATEMENT_PATTERN.search`, `self.procedure_safe_removal`, `FIND_CURRENT_STATEMENT_PATTERN.search`.

Control points:

- L178: `if FINISH_STATEMENT_PATTERN.search(statement)`
- L179: `if current_division == 'PROCEDURE'`
- L193: `if BIND_STATEMENT_PATTERN.search(statement)`
- L201: `if FIND_CURRENT_STATEMENT_PATTERN.search(statement)`

### `IdmsResidualCleanup.procedure_safe_removal` - L218-L232

```python
procedure_safe_removal(self, *, message: str, current_division: str) -> list[str]
```

Control points:

- L224: `if current_division == 'PROCEDURE'`

### `IdmsResidualCleanup.is_idms_abort_paragraph` - L237-L243

```python
is_idms_abort_paragraph(self, logical_line: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `IDMS_ABORT_PARAGRAPH_PATTERN.match`, `bool`.

### `IdmsResidualCleanup.is_exit_line` - L245-L251

```python
is_exit_line(self, logical_line: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `EXIT_LINE_PATTERN.match`, `bool`.

### `IdmsResidualCleanup.references_removed_field` - L256-L283

```python
references_removed_field(self, logical_line: str) -> bool
```

True when this line names a field whose copybook was removed.

Observed calls (lexical order): `str`, `statement.strip`, `self._owned_by_cleanup_composer`, `self.messages.append`, `_LITERAL_PATTERN.sub`, `bool`, `REMOVED_COPYBOOK_FIELD_PATTERN.search`.

Control points:

- L272: `if not statement.strip()`
- L275: `if self._owned_by_cleanup_composer(statement)`

### `IdmsResidualCleanup.removed_field_lines` - L285-L356

```python
removed_field_lines(self, logical_line: str) -> list[str]
```

Comment the line, or refuse and say why.

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `self._owned_by_cleanup_composer`, `_LITERAL_PATTERN.sub`, `REMOVED_COPYBOOK_FIELD_PATTERN.search`, `match.group`, `match.group('field').upper`, `MOVE_TO_STATEMENT_PATTERN.match`, `self.messages.append`, `REMOVED_FIELD_LINE_TEMPLATE.format`, `self._only_dead_operands`, `REMOVED_FIELD_REFUSED_TEMPLATE.format`.

Control points:

- L306: `if not statement`
- L312: `if self._owned_by_cleanup_composer(statement)`
- L318: `if not match`
- L324: `if MOVE_TO_STATEMENT_PATTERN.match(statement)`
- L336: `if self._only_dead_operands(statement)`

### `IdmsResidualCleanup._owned_by_cleanup_composer` - L362-L375

```python
_owned_by_cleanup_composer(statement: str) -> bool
```

True when another pass owns this statement outright.

Observed calls (lexical order): `str`, `str(statement or '').strip`, `bool`, `ERROR_STATUS_MOVE_PATTERN.match`, `ON_ANY_ERROR_STATUS_PATTERN.fullmatch`.

### `IdmsResidualCleanup._only_dead_operands` - L377-L404

```python
_only_dead_operands(self, statement: str) -> bool
```

True when nothing live survives the strip.

Observed calls (lexical order): `_LITERAL_PATTERN.sub`, `str`, `DISPLAY_STATEMENT_PATTERN.match`, `_DISPLAY_VERB_PATTERN.sub`, `REMOVED_COPYBOOK_FIELD_PATTERN.sub`, `residue.replace`, `residue.strip`.

Control points:

- L396: `if DISPLAY_STATEMENT_PATTERN.match(statement)`
- L401: `for character in _PUNCTUATION`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
