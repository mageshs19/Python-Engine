# `tests/db2_date_sentinel/test_parm_sourced_date_has_no_sentinel.py`

Source: [tests/db2_date_sentinel/test_parm_sourced_date_has_no_sentinel.py](../../../../tests/db2_date_sentinel/test_parm_sourced_date_has_no_sentinel.py) | 80 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `088e116509b52dc40ee6b8072f14194f0d385d366e10392171cdea5534b2afc6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The null-date guard is emitted for DB2 columns and suppressed for PARM dates.

## Module-level bindings

`GUARD` (L26)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.services.db2_date_sentinel_policy import Db2DateSentinelPolicy
from rules.sql_generation_rules import DB2_DATE_NULL_SENTINEL
```

## Local dependency notes

- [converter/services/db2_date_sentinel_policy.py](../../converter/services/db2_date_sentinel_policy.md)
- [rules/sql_generation_rules.py](../../rules/sql_generation_rules.md)

## Symbol contracts and control points

### `policy` - L30-L31

```python
policy() -> Db2DateSentinelPolicy
```

Observed calls (lexical order): `Db2DateSentinelPolicy`.

### `test_a_parm_sourced_date_gets_no_guard` - L41-L42

```python
test_a_parm_sourced_date_gets_no_guard(policy, source) -> None
```

Observed calls (lexical order): `policy.guard_lines`.

### `test_the_suppression_is_reported` - L45-L47

```python
test_the_suppression_is_reported(policy) -> None
```

Observed calls (lexical order): `policy.guard_lines`, `any`.

### `test_a_possibly_unset_source_keeps_the_guard` - L61-L65

```python
test_a_possibly_unset_source_keeps_the_guard(policy, source) -> None
```

Observed calls (lexical order): `policy.guard_lines`, `lines[0].strip`, `lines[2].strip`.

### `test_a_dclgen_source_is_tested_before_the_parm_family` - L68-L70

```python
test_a_dclgen_source_is_tested_before_the_parm_family(policy) -> None
```

A DB2 column may be NULL whatever its name looks like.

Observed calls (lexical order): `policy.guard_lines`.

### `test_the_guard_respects_the_caller_indent` - L76-L80

```python
test_the_guard_respects_the_caller_indent(policy) -> None
```

Observed calls (lexical order): `policy.guard_lines`, `lines[0].startswith`, `lines[1].startswith`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
