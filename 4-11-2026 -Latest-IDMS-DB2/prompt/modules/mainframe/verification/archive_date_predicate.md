# `mainframe/verification/archive_date_predicate.py`

Source: [mainframe/verification/archive_date_predicate.py](../../../../mainframe/verification/archive_date_predicate.py) | 47 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `558a8d722b8df2fae4ce828ae47609de68a79b6df0435f3ab148b007932f80c3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Restricted parity model for IDMS numeric dates and DB2 DATE fields.

## Module-level bindings

`ZERO_SENTINEL` (L11), `HIGH_SENTINEL` (L12)

## Import declarations

```python
from __future__ import annotations
from datetime import date
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_archive_date_predicate_parity.py](../../tests/test_archive_date_predicate_parity.md)

## Symbol contracts and control points

### `cobol_numeric_date` - L15-L23

```python
cobol_numeric_date(value: date) -> int
```

Result of the generator's 01.01.0001/31.12.9999 realignment.

Observed calls (lexical order): `isinstance`, `ValueError`.

Control points:

- L17: `if not isinstance(value, date)`
- L19: `if value == ZERO_SENTINEL`
- L21: `if value == HIGH_SENTINEL`

Explicit raises: `ValueError('DB2 DATE must be non-null and valid')`.

### `original_archive_decision` - L26-L32

```python
original_archive_decision(capitalized: date, created: date, cutoff: date) -> bool
```

Original COBOL rule, after DATE sentinel mapping into packed YYYYMMDD.

Observed calls (lexical order): `cobol_numeric_date`, `_cutoff`.

### `manual_sql_date_decision` - L35-L41

```python
manual_sql_date_decision(capitalized: date, created: date, cutoff: date) -> bool
```

Manual DB2 WHERE rule interpreted as typed DATE (not raw host text).

Observed calls (lexical order): `_cutoff`, `isinstance`, `ValueError`.

Control points:

- L38: `if not isinstance(capitalized, date) or not isinstance(created, date)`

Explicit raises: `ValueError('DATE columns must be non-null and valid')`.

### `_cutoff` - L44-L47

```python
_cutoff(value: date) -> int
```

Observed calls (lexical order): `isinstance`, `ValueError`.

Control points:

- L45: `if not isinstance(value, date)`

Explicit raises: `ValueError('archive cutoff must be a valid date')`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
