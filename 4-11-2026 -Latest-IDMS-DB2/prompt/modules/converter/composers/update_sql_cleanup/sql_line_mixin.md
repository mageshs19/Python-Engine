# `converter/composers/update_sql_cleanup/sql_line_mixin.py`

Source: [converter/composers/update_sql_cleanup/sql_line_mixin.py](../../../../../converter/composers/update_sql_cleanup/sql_line_mixin.py) | 140 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `c2a13b47ab4b99dba6ae62c2de7cac55adaea986ccda545b582094aee6adc11e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Host-reference and SET/WHERE/comma line-builder mixin.

## Module-level bindings

`__all__` (L140)

## Import declarations

```python
from __future__ import annotations
from converter.services.host_reference_normalizer import HostReferenceNormalizer
```

## Local dependency notes

- [converter/services/host_reference_normalizer.py](../../services/host_reference_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_base.py](../update_sql_cleanup_base.md)
- [tests/update_sql_cleanup/test_bare_move_rewriter_host_form.py](../../../tests/update_sql_cleanup/test_bare_move_rewriter_host_form.md)

## Symbol contracts and control points

### `SqlLineMixin` - L33-L137

```python
class SqlLineMixin()
```

### `SqlLineMixin._host_reference` - L37-L46

```python
_host_reference(self, table: str, column: str) -> str
```

':DCLGROUP.FIELD' - the SQL form. For EXEC SQL bodies only.

Observed calls (lexical order): `self.host_variable_resolver.host_reference_for_column`.

### `SqlLineMixin._host_reference_key` - L48-L70

```python
_host_reference_key(self, table: str, column: str) -> str
```

'DCLGROUP.FIELD' - a LOOKUP KEY. Never emit this.

Observed calls (lexical order): `hasattr`, `self.host_variable_resolver.host_reference_key`, `self._host_reference`, `reference.startswith`, `reference[1:].strip`.

Control points:

- L59: `if hasattr(self.host_variable_resolver, 'host_reference_key')`
- L67: `if reference.startswith(':')`

### `SqlLineMixin._host_reference_cobol` - L72-L87

```python
_host_reference_cobol(self, table: str, column: str) -> str
```

'FIELD OF DCLGROUP' - the COBOL form. For a MOVE.

Observed calls (lexical order): `HostReferenceNormalizer.to_cobol`, `self._host_reference`.

### `SqlLineMixin._set_lines` - L92-L107

```python
_set_lines(self, table: str, columns: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`, `self._host_reference`, `len`, `output.append`.

Control points:

- L100: `for (index, column) in enumerate(columns)`
- L102: `if not host`

### `SqlLineMixin._where_lines` - L109-L124

```python
_where_lines(self, table: str, columns: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`, `self._host_reference`, `output.append`.

Control points:

- L117: `for (index, column) in enumerate(columns)`
- L119: `if not host`

### `SqlLineMixin._comma_lines` - L126-L137

```python
_comma_lines(self, values: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`, `len`, `output.append`.

Control points:

- L133: `for (index, value) in enumerate(values)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
