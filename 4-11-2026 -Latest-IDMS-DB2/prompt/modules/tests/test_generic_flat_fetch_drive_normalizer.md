# `tests/test_generic_flat_fetch_drive_normalizer.py`

Source: [tests/test_generic_flat_fetch_drive_normalizer.py](../../../tests/test_generic_flat_fetch_drive_normalizer.py) | 146 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `fe80ed2ffa07d6301810fa2c68de41e3f42439f19cb364f3f9fee16d3fa0032c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic flat FETCH/control-flow and final layout regressions.

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.cursor_close_guarantee.flat_fetch_drive_normalizer import FlatFetchDriveNormalizer
from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import _body
from converter.composers.procedure_indent_normalizer import ProcedureIndentNormalizer
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.py](../converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.md)
- [converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.py](../converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.md)
- [converter/composers/procedure_indent_normalizer.py](../converter/composers/procedure_indent_normalizer.md)

## Symbol contracts and control points

### `_source` - L11-L57

```python
_source(cursor='APARENT', business='PROCESS-ROW', extra='')
```

### `_logical` - L60-L61

```python
_logical(text)
```

Observed calls (lexical order): `_body`, `_body(x).upper`, `text.splitlines`.

### `test_split_prime_and_advance_become_one_fetch_driver` - L64-L76

```python
test_split_prime_and_advance_become_one_fetch_driver()
```

Observed calls (lexical order): `_source`, `FlatFetchDriveNormalizer`, `n.apply`, `_logical`, `re.match`, `sum`, `any`, `x.startswith`.

### `test_identifiers_are_discovered_not_hardcoded` - L79-L83

```python
test_identifiers_are_discovered_not_hardcoded()
```

Observed calls (lexical order): `_source`, `FlatFetchDriveNormalizer`, `FlatFetchDriveNormalizer().apply`.

### `test_ambiguous_third_fetch_call_is_rejected` - L86-L88

```python
test_ambiguous_third_fetch_call_is_rejected()
```

Observed calls (lexical order): `_source`, `FlatFetchDriveNormalizer`, `FlatFetchDriveNormalizer().apply`.

### `test_existing_fetch_business_action_is_rejected` - L91-L94

```python
test_existing_fetch_business_action_is_rejected()
```

Observed calls (lexical order): `_source`, `_source().replace`, `FlatFetchDriveNormalizer`, `FlatFetchDriveNormalizer().apply`.

### `test_nonterminal_fetch_is_rejected` - L97-L100

```python
test_nonterminal_fetch_is_rejected()
```

Observed calls (lexical order): `_source`, `_source().replace`, `FlatFetchDriveNormalizer`, `FlatFetchDriveNormalizer().apply`.

### `test_final_indent_reanchors_close_after_multiline_perform` - L103-L107

```python
test_final_indent_reanchors_close_after_multiline_perform()
```

Observed calls (lexical order): `_source`, `ProcedureIndentNormalizer`, `ProcedureIndentNormalizer().compose`, `after.splitlines`, `any`, `x.startswith`.

### `test_unmatched_eoc_loop_is_rejected` - L110-L112

```python
test_unmatched_eoc_loop_is_rejected()
```

Observed calls (lexical order): `_source`, `_source().replace`, `FlatFetchDriveNormalizer`, `FlatFetchDriveNormalizer().apply`.

### `test_fixed_format_rewrite_has_no_leaked_sequence_tokens` - L115-L141

```python
test_fixed_format_rewrite_has_no_leaked_sequence_tokens()
```

Observed calls (lexical order): `_source`, `enumerate`, `source.splitlines`, `line.strip`, `logical.startswith`, `len`, `AssertionError`, `fixed.append`, `'\n'.join`, `FlatFetchDriveNormalizer`, `FlatFetchDriveNormalizer().apply`, `out.splitlines`, `all`, `line[72:80].isdigit`, `line[:6].isdigit`, `re.match`.

Control points:

- L122: `for (i, line) in enumerate(source.splitlines(), 1)`
- L124: `if not logical`
- L127: `if logical.startswith('*')`
- L134: `if len(body) > 65`

Explicit raises: `AssertionError(f'fixture line overflow {logical}')`.

### `test_setup_reused_outside_mainline_refuses_rewrite` - L144-L146

```python
test_setup_reused_outside_mainline_refuses_rewrite()
```

Observed calls (lexical order): `_source`, `FlatFetchDriveNormalizer`, `FlatFetchDriveNormalizer().apply`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
