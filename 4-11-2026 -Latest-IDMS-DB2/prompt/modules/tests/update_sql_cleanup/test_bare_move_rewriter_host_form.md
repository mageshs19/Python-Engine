# `tests/update_sql_cleanup/test_bare_move_rewriter_host_form.py`

Source: [tests/update_sql_cleanup/test_bare_move_rewriter_host_form.py](../../../../tests/update_sql_cleanup/test_bare_move_rewriter_host_form.py) | 79 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `f15a66ca8a4c1491118eb1f0e0d6eb02f47304240b481aae708d7805153434ac`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> A MOVE target must be COBOL, never a lookup key.

## Module-level bindings

`SQL_FORM` (L17), `KEY_FORM` (L18), `COBOL_FORM` (L19)

## Import declarations

```python
from __future__ import annotations
from converter.services.host_reference_normalizer import HostReferenceNormalizer
from converter.composers.update_sql_cleanup.sql_line_mixin import SqlLineMixin
from converter.composers.update_sql_cleanup.bare_move_rewriter import QUALIFIER_CONNECTORS
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/bare_move_rewriter.py](../../converter/composers/update_sql_cleanup/bare_move_rewriter.md)
- [converter/composers/update_sql_cleanup/sql_line_mixin.py](../../converter/composers/update_sql_cleanup/sql_line_mixin.md)
- [converter/services/host_reference_normalizer.py](../../converter/services/host_reference_normalizer.md)

## Symbol contracts and control points

### `_Resolver` - L22-L24

```python
class _Resolver()
```

### `_Resolver.host_reference_for_column` - L23-L24

```python
host_reference_for_column(self, table_name, column_name)
```

### `_Owner` - L27-L35

```python
class _Owner()
```

Declared class/data-model fields:

```python
host_variable_resolver = _Resolver()
_host_reference = SqlLineMixin._host_reference
_host_reference_key = SqlLineMixin._host_reference_key
_host_reference_cobol = SqlLineMixin._host_reference_cobol
```

### `test_the_sql_form_keeps_its_colon` - L41-L42

```python
test_the_sql_form_keeps_its_colon()
```

Observed calls (lexical order): `_Owner`, `_Owner()._host_reference`.

### `test_the_key_form_is_not_cobol` - L45-L48

```python
test_the_key_form_is_not_cobol()
```

Observed calls (lexical order): `_Owner`, `_Owner()._host_reference_key`.

### `test_the_cobol_form_carries_no_dot` - L51-L55

```python
test_the_cobol_form_carries_no_dot()
```

Observed calls (lexical order): `_Owner`, `_Owner()._host_reference_cobol`.

### `test_an_already_cobol_reference_is_unchanged` - L61-L62

```python
test_an_already_cobol_reference_is_unchanged()
```

Observed calls (lexical order): `HostReferenceNormalizer.to_cobol`.

### `test_an_empty_reference_yields_empty` - L65-L67

```python
test_an_empty_reference_yields_empty()
```

Observed calls (lexical order): `HostReferenceNormalizer.to_cobol`.

### `test_a_target_qualified_on_the_next_line_is_refused` - L73-L79

```python
test_a_target_qualified_on_the_next_line_is_refused()
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
