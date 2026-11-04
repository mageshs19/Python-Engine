# `tests/cursor_contract/test_declare_clauses.py`

Source: [tests/cursor_contract/test_declare_clauses.py](../../../../tests/cursor_contract/test_declare_clauses.py) | 75 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `6998a19eca9a7a77390ab560c43e17830ee048aba0764de5f8e864949c6af644`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_declaration_carries_a_queryno` - L4-L6

```python
test_declaration_carries_a_queryno(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `any`, `body.startswith`.

### `test_queryno_is_the_last_clause_before_end_exec` - L9-L14

```python
test_queryno_is_the_last_clause_before_end_exec(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `lines[-2].startswith`.

### `test_queryno_is_derived_from_the_cursor_order` - L17-L23

```python
test_queryno_is_derived_from_the_cursor_order(declares, spec, bodies, names)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`.

### `test_two_cursors_never_share_a_queryno` - L26-L33

```python
test_two_cursors_never_share_a_queryno(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `queryno`.

### `test_two_cursors_never_share_a_queryno.queryno` - L30-L31

```python
queryno(items: list[str]) -> str
```

Observed calls (lexical order): `b.startswith`, `next`.

### `test_queryno_is_stable_across_runs` - L36-L37

```python
test_queryno_is_stable_across_runs(declares, spec)
```

Observed calls (lexical order): `declares.build`, `spec`.

### `test_a_child_cursor_keeps_where_and_order_by` - L40-L57

```python
test_a_child_cursor_keeps_where_and_order_by(declares, spec, bodies, clause_index)
```

Observed calls (lexical order): `spec`, `bodies`, `declares.build`, `clause_index`, `lines[-2].startswith`.

### `test_a_root_cursor_keeps_its_order_by` - L60-L66

```python
test_a_root_cursor_keeps_its_order_by(declares, spec, bodies, has_clause)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `has_clause`.

### `test_a_spec_without_a_table_produces_a_warning_not_sql` - L69-L75

```python
test_a_spec_without_a_table_produces_a_warning_not_sql(declares, spec, bodies)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
