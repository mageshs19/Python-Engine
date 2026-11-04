# `tests/test_no_site_names_in_rules_and_patterns.py`

Source: [tests/test_no_site_names_in_rules_and_patterns.py](../../../tests/test_no_site_names_in_rules_and_patterns.py) | 140 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `494bedfcc38e554a3371c50cd42255bf3a90fc4f9929f62e0d89a831c24a95be`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> No customer site name may appear in rules/ or patterns/.

## Module-level bindings

`SITE_TOKENS` (L36), `ROOT` (L38), `SCANNED_DIRS` (L39), `OWNED_VOCABULARY` (L42), `KNOWN_SITE_NAME_DEBT` (L56)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
import pytest
```

## Symbol contracts and control points

### `_modules` - L83-L87

```python
_modules() -> list[Path]
```

Observed calls (lexical order): `(ROOT / directory).rglob`, `found.extend`, `sorted`.

Control points:

- L85: `for directory in SCANNED_DIRS`

### `_tokens_in` - L90-L92

```python
_tokens_in(path: Path) -> list[str]
```

Observed calls (lexical order): `path.read_text`, `path.read_text(encoding='utf-8', errors='replace').upper`.

### `test_module_carries_no_site_name` - L98-L111

```python
test_module_carries_no_site_name(path: Path) -> None
```

A module must be clean, owned, or within its recorded debt.

Observed calls (lexical order): `pytest.skip`, `_tokens_in`, `set`, `KNOWN_SITE_NAME_DEBT.get`, `sorted`, `path.relative_to`, `', '.join`.

Control points:

- L100: `if path.stem in OWNED_VOCABULARY`

### `test_debt_list_is_not_stale` - L115-L134

```python
test_debt_list_is_not_stale(stem: str) -> None
```

A cleared module must be REMOVED from the debt list.

Observed calls (lexical order): `_modules`, `_tokens_in`, `set`, `sorted`, `', '.join`.

### `test_the_two_lists_do_not_overlap` - L137-L140

```python
test_the_two_lists_do_not_overlap() -> None
```

A module is either owned or in debt. Never both.

Observed calls (lexical order): `set`, `sorted`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
