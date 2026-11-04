# `tests/test_vmdz4310_manual_reference_parity.py`

Source: [tests/test_vmdz4310_manual_reference_parity.py](../../../tests/test_vmdz4310_manual_reference_parity.py) | 60 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `0ccc8e2bbf8bbc21d76a93f2e47d6ff3819178d44fe005f3b781846b9a2b387e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L6), `GENERATED` (L8), `MANUAL` (L9)

## Import declarations

```python
from __future__ import annotations
import re
from pathlib import Path
from tests.workspace_fixtures import generated_program
```

## Local dependency notes

- [tests/workspace_fixtures.py](workspace_fixtures.md)

## Symbol contracts and control points

### `_sql_block` - L12-L16

```python
_sql_block(text: str, table: str) -> str
```

Observed calls (lexical order): `text.index`, `text.rfind`.

### `test_parent_select_projection_is_minimal_and_into_aligned` - L19-L31

```python
test_parent_select_projection_is_minimal_and_into_aligned()
```

Observed calls (lexical order): `GENERATED.read_text`, `_sql_block`, `block.index`, `re.findall`, `len`, `c.replace`, `columns.count`.

### `test_input_and_treated_totals_are_both_counted_and_displayed` - L34-L40

```python
test_input_and_treated_totals_are_both_counted_and_displayed()
```

Observed calls (lexical order): `GENERATED.read_text`, `re.search`.

### `test_bounded_lrf_is_singleton_and_fixed_format_is_clean` - L43-L52

```python
test_bounded_lrf_is_singleton_and_fixed_format_is_clean()
```

Observed calls (lexical order): `GENERATED.read_text`, `all`, `generated.splitlines`, `len`, `line[7:72].rstrip`, `max`.

### `test_manual_reference_has_total_input_and_treated_counters` - L55-L60

```python
test_manual_reference_has_total_input_and_treated_counters()
```

Observed calls (lexical order): `MANUAL.read_text`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
