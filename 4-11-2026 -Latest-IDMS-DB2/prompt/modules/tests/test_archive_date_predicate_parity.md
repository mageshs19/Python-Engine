# `tests/test_archive_date_predicate_parity.py`

Source: [tests/test_archive_date_predicate_parity.py](../../../tests/test_archive_date_predicate_parity.py) | 47 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `fa0ec40e9167ea523d0b1fe5827636d77516c23bb7634297d9b20f924385bb24`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The rule's typed-date domain is only part of mainframe parity proof.

## Import declarations

```python
from datetime import date, timedelta
from random import Random
import pytest
from mainframe.verification.archive_date_predicate import original_archive_decision, manual_sql_date_decision, ZERO_SENTINEL, HIGH_SENTINEL
```

## Local dependency notes

- [mainframe/verification/archive_date_predicate.py](../mainframe/verification/archive_date_predicate.md)

## Symbol contracts and control points

### `_equal` - L13-L14

```python
_equal(cap, cr, cutoff)
```

Observed calls (lexical order): `manual_sql_date_decision`, `original_archive_decision`.

### `test_valid_db2_date_domain_matches` - L27-L28

```python
test_valid_db2_date_domain_matches(cap, cr, cutoff)
```

Observed calls (lexical order): `_equal`.

### `test_seeded_dates_around_cutoff_and_cross_year` - L31-L38

```python
test_seeded_dates_around_cutoff_and_cross_year()
```

Observed calls (lexical order): `Random`, `date`, `range`, `rand.randrange`, `timedelta`, `_equal`.

Control points:

- L34: `for _ in range(3000)`

### `test_reject_nulls_as_unproven_db2_semantics` - L41-L47

```python
test_reject_nulls_as_unproven_db2_semantics()
```

Observed calls (lexical order): `pytest.raises`, `date`, `original_archive_decision`, `manual_sql_date_decision`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
