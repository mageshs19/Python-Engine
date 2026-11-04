# `tests/cursor_where/test_declare_clauses.py`

Source: [tests/cursor_where/test_declare_clauses.py](../../../../tests/cursor_where/test_declare_clauses.py) | 243 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e997c4c10c73df04319415fc693f09578ed5335225e79a6493c97ab345672d8e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Every way the declare builder REFUSES, and how it reports it.

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_rules import ENFORCE_WHERE_COLUMN_OWNERSHIP
from tests.cursor_where._fixtures import CHILD_TABLE, CURSOR, EXPECTED_PREDICATE, KEY_COLUMN, UNOWNED_COLUMN, UNOWNED_PREDICATE, assert_refusal, bodies, has_clause, spec
```

## Local dependency notes

- [rules/cursor_declaration_rules.py](../../rules/cursor_declaration_rules.md)
- [tests/cursor_where/_fixtures.py](_fixtures.md)

## Symbol contracts and control points

### `test_an_empty_column_list_refuses_instead_of_select_star` - L43-L52

```python
test_an_empty_column_list_refuses_instead_of_select_star(declares)
```

CHK-12.04 forbids SELECT *, and an implicit list breaks the SELECT / FETCH INTO positional parity. Refusing is the only safe answer.

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `assert_refusal`, `' '.join`, `' '.join(rendered).upper`.

### `test_the_empty_column_refusal_is_reported` - L55-L58

```python
test_the_empty_column_refusal_is_reported(declares)
```

Observed calls (lexical order): `declares.build`, `spec`, `any`.

### `test_select_star_never_appears_in_a_rendered_declare` - L61-L66

```python
test_select_star_never_appears_in_a_rendered_declare(declares)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `_first_column_line`, `rendered[select].strip`.

### `_first_column_line` - L69-L74

```python
_first_column_line(rendered: list[str]) -> int
```

Index of the line after SELECT. -1 when there is no SELECT.

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`.

Control points:

- L71: `for (index, body) in enumerate(rendered)`
- L72: `if body.upper().startswith('SELECT')`

### `test_ownership_guard_is_enabled_by_the_site_standard` - L80-L81

```python
test_ownership_guard_is_enabled_by_the_site_standard()
```

### `test_a_parent_column_on_the_left_is_refused` - L84-L91

```python
test_a_parent_column_on_the_left_is_refused(guarded_declares)
```

A parent column on the left of a child predicate binds as SQLCODE -206, so the whole program fails to run.

Observed calls (lexical order): `bodies`, `guarded_declares.build`, `spec`, `assert_refusal`.

### `test_the_ownership_refusal_names_the_column_in_the_report` - L94-L101

```python
test_the_ownership_refusal_names_the_column_in_the_report(guarded_declares)
```

A refusal with no diagnostic is worse than no guard at all: the cursor disappears and the report does not say which column did it.

Observed calls (lexical order): `guarded_declares.build`, `spec`, `any`.

### `test_an_owned_column_on_the_left_is_accepted` - L104-L110

```python
test_an_owned_column_on_the_left_is_accepted(guarded_declares)
```

Observed calls (lexical order): `bodies`, `guarded_declares.build`, `spec`, `has_clause`, `any`.

### `test_a_keyword_operator_predicate_is_not_refused` - L113-L126

```python
test_a_keyword_operator_predicate_is_not_refused(guarded_declares)
```

IS / BETWEEN / IN / LIKE carry no '=' character.

Observed calls (lexical order): `bodies`, `guarded_declares.build`, `spec`, `has_clause`.

### `test_a_qualified_operand_is_not_refused` - L129-L141

```python
test_a_qualified_operand_is_not_refused(guarded_declares)
```

T.NR_ID and NR_ID are the same column.

Observed calls (lexical order): `bodies`, `guarded_declares.build`, `spec`, `has_clause`.

### `test_the_guard_stands_down_when_no_column_list_is_available` - L144-L153

```python
test_the_guard_stands_down_when_no_column_list_is_available(declares)
```

No resolver injected: validate nothing rather than refuse a cursor that may be perfectly correct.

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `has_clause`.

### `test_the_stand_down_is_reported` - L156-L161

```python
test_the_stand_down_is_reported(declares)
```

A guard that stands down in SILENCE is how an unguarded builder reached production and stayed invisible across several runs.

Observed calls (lexical order): `declares.build`, `spec`, `any`.

### `test_the_stand_down_is_reported_once_per_table` - L164-L171

```python
test_the_stand_down_is_reported_once_per_table(declares)
```

The lookup is cached per table. Without the cache the same message was repeated per cursor and buried the signal.

Observed calls (lexical order): `declares.build`, `spec`, `len`.

### `test_a_spec_without_a_table_produces_a_warning_not_sql` - L177-L181

```python
test_a_spec_without_a_table_produces_a_warning_not_sql(declares)
```

Refusing beats guessing: no fabricated FROM clause.

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `assert_refusal`.

### `test_a_spec_without_a_table_is_reported` - L184-L187

```python
test_a_spec_without_a_table_is_reported(declares)
```

Observed calls (lexical order): `declares.build`, `spec`.

### `test_a_spec_without_a_cursor_name_produces_a_warning_not_sql` - L190-L193

```python
test_a_spec_without_a_cursor_name_produces_a_warning_not_sql(declares)
```

Observed calls (lexical order): `bodies`, `declares.build`, `spec`, `assert_refusal`.

### `test_a_spec_without_a_cursor_name_is_reported` - L196-L202

```python
test_a_spec_without_a_cursor_name_is_reported(declares)
```

Both spec-level refusals emitted a warning and logged NOTHING, so a cursor vanished from the program and the conversion report did not say why.

Observed calls (lexical order): `declares.build`, `spec`.

### `test_a_refusal_emits_no_fragment_of_a_declare` - L208-L234

```python
test_a_refusal_emits_no_fragment_of_a_declare(guarded_declares)
```

Observed calls (lexical order): `spec`, `bodies`, `guarded_declares.build`, `' '.join`, `' '.join(rendered).upper`, `assert_refusal`.

Control points:

- L233: `for fragment in forbidden_sql_fragments`

### `test_reset_clears_refusal_messages_between_programs` - L236-L243

```python
test_reset_clears_refusal_messages_between_programs(guarded_declares)
```

One instance renders every cursor of every program in a folder run, so an uncleared report carries program 1 into program 2.

Observed calls (lexical order): `guarded_declares.build`, `spec`, `guarded_declares.reset`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
