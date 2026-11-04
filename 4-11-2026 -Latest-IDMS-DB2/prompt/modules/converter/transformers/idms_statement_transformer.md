# `converter/transformers/idms_statement_transformer.py`

Source: [converter/transformers/idms_statement_transformer.py](../../../../converter/transformers/idms_statement_transformer.py) | 331 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `093803293f47cfd48400eabe7d7002ae7d721446689fb1b2836c1515562ebf97`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ARITY_LINE` (L18), `ARITY_UPPER_LINE` (L19), `ARITY_WITH_DIVISION` (L20), `ARITY_WITH_SQL_ERROR` (L21), `NO_OPENED_SET` (L23), `__all__` (L331)

## Import declarations

```python
from __future__ import annotations
from converter.transformers.idms_statement.control_statement_converter import ControlStatementConverterMixin
from converter.transformers.idms_statement.data_statement_converter import DataStatementConverterMixin
from converter.transformers.idms_statement.transformer_shared_mixin import TransformerSharedMixin
```

## Local dependency notes

- [converter/transformers/idms_statement/control_statement_converter.py](idms_statement/control_statement_converter.md)
- [converter/transformers/idms_statement/data_statement_converter.py](idms_statement/data_statement_converter.md)
- [converter/transformers/idms_statement/transformer_shared_mixin.py](idms_statement/transformer_shared_mixin.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/transformers/cobol_transformer.py](cobol_transformer.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/test_db2_code_fixes.py](../../tests/test_db2_code_fixes.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `IdmsStatementTransformer` - L26-L328

```python
class IdmsStatementTransformer(TransformerSharedMixin, ControlStatementConverterMixin, DataStatementConverterMixin)
```

Converts executable IDMS statements to DB2-compatible COBOL.

### `IdmsStatementTransformer.__init__` - L100-L174

```python
__init__(self, sql_generator, sql_error_generator, table_name_resolver, cursor_name_resolver) -> None
```

Observed calls (lexical order): `set`.

### `IdmsStatementTransformer.reset` - L179-L193

```python
reset(self) -> None
```

Clear per-program OUTPUT state.

Observed calls (lexical order): `set`.

### `IdmsStatementTransformer.transform_line` - L198-L240

```python
transform_line(self, line: str, current_division: str, sql_error_paragraph: str) -> tuple[list[str], str]
```

Observed calls (lexical order): `str`, `str(line or '').strip`, `stripped_line.upper`, `self._run_plain_converters`, `self._run_cursor_converters`, `self._convert_store_modify_erase`, `self._is_converted`, `self._replace_idms_condition_tokens`.

Control points:

- L206: `if not stripped_line`
- L218: `if plain is not None`
- L227: `if cursor_lines is not None`
- L237: `if self._is_converted(store_lines)`

### `IdmsStatementTransformer._run_plain_converters` - L245-L267

```python
_run_plain_converters(self, *, upper: str, stripped_line: str, current_division: str, sql_error_paragraph: str) -> list[str] | None
```

First converter that returns a non-empty result wins.

Observed calls (lexical order): `self._invoke`, `self._is_converted`.

Control points:

- L254: `for (converter, arity) in self._plain_converters`
- L264: `if self._is_converted(result)`

### `IdmsStatementTransformer._run_cursor_converters` - L269-L287

```python
_run_cursor_converters(self, *, upper: str, stripped_line: str, current_division: str) -> tuple[list[str] | None, str]
```

Converters that may also report the IDMS set they opened.

Observed calls (lexical order): `converter`, `self._is_converted`, `str`.

Control points:

- L277: `for converter in self._cursor_converters`
- L284: `if self._is_converted(result)`

### `IdmsStatementTransformer._invoke` - L290-L313

```python
_invoke(*, converter, arity: int, upper: str, stripped_line: str, current_division: str, sql_error_paragraph: str)
```

Observed calls (lexical order): `converter`.

Control points:

- L299: `if arity == ARITY_LINE`
- L302: `if arity == ARITY_UPPER_LINE`
- L305: `if arity == ARITY_WITH_DIVISION`

### `IdmsStatementTransformer._is_converted` - L316-L328

```python
_is_converted(result) -> bool
```

True only for a real replacement.

Observed calls (lexical order): `len`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
