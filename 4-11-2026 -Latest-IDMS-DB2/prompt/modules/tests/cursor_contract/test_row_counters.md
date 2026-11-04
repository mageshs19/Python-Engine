# `tests/cursor_contract/test_row_counters.py`

Source: [tests/cursor_contract/test_row_counters.py](../../../../tests/cursor_contract/test_row_counters.py) | 38 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `10370807aad6e19b7d147998374980e52df7574e96c40c06150696ad54e29217`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_a_parent_fetch_counts_rows` - L4-L6

```python
test_a_parent_fetch_counts_rows(fetch, names)
```

Observed calls (lexical order): `fetch`, `any`, `body.startswith`.

### `test_a_child_fetch_does_not_count_rows` - L9-L16

```python
test_a_child_fetch_does_not_count_rows(fetch)
```

Observed calls (lexical order): `fetch`, `any`, `body.startswith`.

### `test_no_counter_without_a_table` - L19-L21

```python
test_no_counter_without_a_table(fetch)
```

Observed calls (lexical order): `fetch`, `any`, `body.startswith`.

### `test_label_fallback_is_reported_when_no_repository_is_wired` - L24-L38

```python
test_label_fallback_is_reported_when_no_repository_is_wired(paragraphs, names)
```

Observed calls (lexical order): `paragraphs.fetch_paragraph`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
