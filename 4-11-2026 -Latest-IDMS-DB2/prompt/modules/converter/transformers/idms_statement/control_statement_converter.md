# `converter/transformers/idms_statement/control_statement_converter.py`

Source: [converter/transformers/idms_statement/control_statement_converter.py](../../../../../converter/transformers/idms_statement/control_statement_converter.py) | 449 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `68b45f1be86e476dd78b883b063653663651b6eaf7dca1d51ee99450aed4c611`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> IDMS declarative and control statement conversion.

## Module-level bindings

`PROCEDURE_DIVISION_NAME` (L95), `CONTINUE_STATEMENT` (L96), `COMMIT_BLOCK_LINES` (L100), `__all__` (L449)

## Import declarations

```python
from __future__ import annotations
from patterns.idms_patterns import BIND_STATEMENT_PATTERN, COMMIT_PATTERN, CONNECT_STATEMENT_PATTERN, DISCONNECT_STATEMENT_PATTERN, FIND_CURRENT_PATTERN, FINISH_PATTERN, IDMS_ABORT_PERFORM_PATTERN, IDMS_STATUS_PERFORM_PATTERN, IDMS_STOP_PERFORM_PATTERN, READY_PATTERN, ROLLBACK_PATTERN, USAGE_MODE_PATTERN
from rules.idms_transformer_messages import COMMIT_OUTSIDE_PROCEDURE_TEMPLATE, FINISH_CONVERTED_TO_COMMIT, FINISH_OUTSIDE_PROCEDURE_TEMPLATE, FINISH_REMOVED_RETRIEVAL, TRANSFORMER_MESSAGES
from rules.manual_reference_rules import EMIT_COMMIT_IN_RETRIEVAL
```

## Local dependency notes

- [patterns/idms_patterns.py](../../../patterns/idms_patterns.md)
- [rules/idms_transformer_messages.py](../../../rules/idms_transformer_messages.md)
- [rules/manual_reference_rules.py](../../../rules/manual_reference_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/idms_statement_transformer.py](../idms_statement_transformer.md)

## Symbol contracts and control points

### `ControlStatementConverterMixin` - L108-L446

```python
class ControlStatementConverterMixin()
```

Converts IDMS declarative and control statements.

### `ControlStatementConverterMixin._convert_declarative_or_control` - L119-L148

```python
_convert_declarative_or_control(self, upper: str, stripped_line: str) -> list[str] | None
```

Remove an IDMS declarative statement.

Observed calls (lexical order): `str`, `str(stripped_line or '').strip`, `USAGE_MODE_PATTERN.search`, `self._is_declarative`.

Control points:

- L135: `if not statement`
- L140: `if USAGE_MODE_PATTERN.search(text)`
- L143: `if self._is_declarative(text)`

### `ControlStatementConverterMixin._convert_finish_or_commit` - L153-L194

```python
_convert_finish_or_commit(self, upper: str, stripped_line: str, current_division: str) -> list[str] | None
```

Convert FINISH, and police an explicit COMMIT.

Observed calls (lexical order): `str`, `str(stripped_line or '').strip`, `self._division`, `FINISH_PATTERN.search`, `self._finish_lines`, `COMMIT_PATTERN.search`, `self._commit_lines`, `ROLLBACK_PATTERN.fullmatch`, `getattr`, `callable`, `self._log_control`, `list`, `rollback`.

Control points:

- L166: `if not statement`
- L171: `if FINISH_PATTERN.search(statement)`
- L177: `if COMMIT_PATTERN.search(statement)`
- L183: `if ROLLBACK_PATTERN.fullmatch(statement)`
- L184: `if division != PROCEDURE_DIVISION_NAME`
- L187: `if callable(rollback)`

### `ControlStatementConverterMixin._convert_bind_ready_connect_disconnect` - L199-L248

```python
_convert_bind_ready_connect_disconnect(self, upper: str, stripped_line: str, current_division: str) -> list[str] | None
```

Remove run-unit and set-membership verbs.

Observed calls (lexical order): `str`, `str(stripped_line or '').strip`, `self._division`, `BIND_STATEMENT_PATTERN.search`, `self._remove`, `READY_PATTERN.search`, `CONNECT_STATEMENT_PATTERN.search`, `DISCONNECT_STATEMENT_PATTERN.search`, `FIND_CURRENT_PATTERN.search`.

Control points:

- L213: `if not statement`
- L218: `if BIND_STATEMENT_PATTERN.search(statement)`
- L224: `if READY_PATTERN.search(statement)`
- L230: `if CONNECT_STATEMENT_PATTERN.search(statement)`
- L236: `if DISCONNECT_STATEMENT_PATTERN.search(statement)`
- L242: `if FIND_CURRENT_PATTERN.search(statement)`

### `ControlStatementConverterMixin._convert_status_abort_perform` - L253-L293

```python
_convert_status_abort_perform(self, upper: str, stripped_line: str, current_division: str) -> list[str] | None
```

Remove PERFORM IDMS-STATUS and PERFORM IDMS-ABORT.

Observed calls (lexical order): `str`, `str(stripped_line or '').strip`, `self._division`, `IDMS_STATUS_PERFORM_PATTERN.search`, `self._remove`, `IDMS_ABORT_PERFORM_PATTERN.search`, `IDMS_STOP_PERFORM_PATTERN.search`.

Control points:

- L266: `if not statement`
- L272: `if IDMS_STATUS_PERFORM_PATTERN.search(text)`
- L278: `if IDMS_ABORT_PERFORM_PATTERN.search(text)`
- L284: `if IDMS_STOP_PERFORM_PATTERN.search(text)`

### `ControlStatementConverterMixin._finish_lines` - L298-L320

```python
_finish_lines(self, *, statement: str, current_division: str) -> list[str]
```

FINISH -> COMMIT, but only when the program may commit.

Observed calls (lexical order): `FINISH_OUTSIDE_PROCEDURE_TEMPLATE.format`, `self._commit_allowed`, `self._log_control`, `self._remove`.

Control points:

- L310: `if current_division != PROCEDURE_DIVISION_NAME`
- L315: `if not self._commit_allowed()`

### `ControlStatementConverterMixin._commit_lines` - L325-L347

```python
_commit_lines(self, *, statement: str, current_division: str) -> list[str]
```

An explicit COMMIT already present in the source.

Observed calls (lexical order): `COMMIT_OUTSIDE_PROCEDURE_TEMPLATE.format`, `self._commit_allowed`, `self._log_control`, `self._remove`, `list`.

Control points:

- L337: `if current_division != PROCEDURE_DIVISION_NAME`
- L342: `if not self._commit_allowed()`

### `ControlStatementConverterMixin._commit_allowed` - L352-L364

```python
_commit_allowed(self) -> bool
```

True only when this program may carry a COMMIT.

Observed calls (lexical order): `bool`, `getattr`.

Control points:

- L362: `if bool(getattr(self, 'emit_commit', True))`

### `ControlStatementConverterMixin._division` - L370-L371

```python
_division(current_division: str | None) -> str
```

Observed calls (lexical order): `str`, `str(current_division or '').strip`, `str(current_division or '').strip().upper`.

### `ControlStatementConverterMixin._is_declarative` - L373-L387

```python
_is_declarative(self, upper: str) -> bool
```

Delegate to the host's declarative test when it exists.

Observed calls (lexical order): `getattr`, `callable`, `bool`, `helper`.

Control points:

- L382: `if callable(helper)`

### `ControlStatementConverterMixin._remove` - L389-L407

```python
_remove(self, message: str, current_division: str) -> list[str]
```

Route removal through the host helper when it exists.

Observed calls (lexical order): `getattr`, `callable`, `helper`, `list`, `self.procedure_safe_removal`.

Control points:

- L398: `if callable(helper)`

### `ControlStatementConverterMixin.procedure_safe_removal` - L409-L426

```python
procedure_safe_removal(self, *, message: str, current_division: str) -> list[str]
```

Comment the removed statement; keep the paragraph valid.

Control points:

- L421: `if current_division == PROCEDURE_DIVISION_NAME`

### `ControlStatementConverterMixin._log_control` - L431-L446

```python
_log_control(self, key: str, **values) -> None
```

Append to the HOST's message list; never create one.

Observed calls (lexical order): `TRANSFORMER_MESSAGES.get`, `getattr`, `messages.append`, `template.format`.

Control points:

- L439: `if not template`
- L443: `if messages is None`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
