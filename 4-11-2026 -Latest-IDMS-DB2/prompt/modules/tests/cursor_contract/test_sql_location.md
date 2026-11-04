# `tests/cursor_contract/test_sql_location.py`

Source: [tests/cursor_contract/test_sql_location.py](../../../../tests/cursor_contract/test_sql_location.py) | 51 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `46d01280e7a418e643bdcf59556a0fcc8ed76fc62270c770212079d16684d199`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import pytest
```

## Symbol contracts and control points

### `test_entry_point_sql_location_is_emitted_before_the_sql` - L6-L13

```python
test_entry_point_sql_location_is_emitted_before_the_sql(fetch, sql_moves)
```

Observed calls (lexical order): `fetch`, `sql_moves`, `lines.index`.

### `test_sql_location_is_set_exactly_once` - L16-L17

```python
test_sql_location_is_set_exactly_once(fetch, sql_moves)
```

Observed calls (lexical order): `fetch`, `len`, `sql_moves`.

### `test_error_branch_does_not_restate_sql_location` - L27-L35

```python
test_error_branch_does_not_restate_sql_location(cursor_paragraph, names, sql_moves, when_other, shape, key)
```

Observed calls (lexical order): `cursor_paragraph`, `len`, `sql_moves`, `any`, `body.endswith`, `when_other`.

### `test_fetch_error_branch_does_not_restate_sql_location` - L38-L44

```python
test_fetch_error_branch_does_not_restate_sql_location(fetch, names, when_other)
```

Observed calls (lexical order): `fetch`, `when_other`, `any`, `body.endswith`.

### `test_error_branch_reports_and_routes` - L47-L51

```python
test_error_branch_reports_and_routes(fetch, names, when_other)
```

Observed calls (lexical order): `fetch`, `when_other`, `any`, `body.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
