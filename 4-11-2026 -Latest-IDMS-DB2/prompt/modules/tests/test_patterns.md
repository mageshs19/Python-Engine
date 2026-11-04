# `tests/test_patterns.py`

Source: [tests/test_patterns.py](../../../tests/test_patterns.py) | 47 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `9663959e1a34c81c55961db65c48d9c3732ff211787642b3b191b920ef5d5207`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from patterns.cobol_patterns import PROGRAM_ID_PATTERN
from patterns.dclgen_patterns import DECLARE_TABLE_PATTERN
from patterns.idms_patterns import OBTAIN_CALC_PATTERN, STORE_PATTERN
from patterns.sql_patterns import EXEC_SQL_PATTERN, UPDATE_SQL_PATTERN
from patterns.validation_patterns import TODO_DB2_PATTERN
```

## Local dependency notes

- [patterns/cobol_patterns.py](../patterns/cobol_patterns.md)
- [patterns/dclgen_patterns.py](../patterns/dclgen_patterns.md)
- [patterns/idms_patterns.py](../patterns/idms_patterns.md)
- [patterns/sql_patterns.py](../patterns/sql_patterns.md)
- [patterns/validation_patterns.py](../patterns/validation_patterns.md)

## Symbol contracts and control points

### `test_program_id_pattern_matches` - L8-L9

```python
test_program_id_pattern_matches()
```

Observed calls (lexical order): `PROGRAM_ID_PATTERN.search`.

### `test_dclgen_declare_table_pattern_matches` - L12-L18

```python
test_dclgen_declare_table_pattern_matches()
```

Observed calls (lexical order): `DECLARE_TABLE_PATTERN.search`, `match.group`, `match.group(1).strip`.

### `test_obtain_calc_pattern_matches` - L21-L25

```python
test_obtain_calc_pattern_matches()
```

Observed calls (lexical order): `OBTAIN_CALC_PATTERN.search`, `match.group`.

### `test_store_pattern_matches` - L28-L32

```python
test_store_pattern_matches()
```

Observed calls (lexical order): `STORE_PATTERN.search`, `match.group`.

### `test_exec_sql_pattern_matches` - L35-L36

```python
test_exec_sql_pattern_matches()
```

Observed calls (lexical order): `EXEC_SQL_PATTERN.match`.

### `test_update_sql_pattern_matches_table` - L39-L43

```python
test_update_sql_pattern_matches_table()
```

Observed calls (lexical order): `UPDATE_SQL_PATTERN.search`, `match.group`.

### `test_todo_db2_validation_pattern_matches` - L46-L47

```python
test_todo_db2_validation_pattern_matches()
```

Observed calls (lexical order): `TODO_DB2_PATTERN.search`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
