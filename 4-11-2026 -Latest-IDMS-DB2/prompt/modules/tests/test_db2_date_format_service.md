# `tests/test_db2_date_format_service.py`

Source: [tests/test_db2_date_format_service.py](../../../tests/test_db2_date_format_service.py) | 44 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e75196710c17fa6d55a14606e95446d0754ede6abbb269669ceca6c303767ce9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.services.db2_date_format_service import Db2DateFormatService
from rules.final_feedback_fix_rules import DEFAULT_DB2_DATE_EXTERNAL_FORMAT
```

## Local dependency notes

- [converter/services/db2_date_format_service.py](../converter/services/db2_date_format_service.md)
- [rules/final_feedback_fix_rules.py](../rules/final_feedback_fix_rules.md)

## Symbol contracts and control points

### `test_supported_formats_and_aliases_normalize` - L21-L22

```python
test_supported_formats_and_aliases_normalize(configured, expected)
```

Observed calls (lexical order): `Db2DateFormatService`.

### `test_blank_format_keeps_legacy_default` - L25-L27

```python
test_blank_format_keeps_legacy_default()
```

Observed calls (lexical order): `Db2DateFormatService`.

### `test_unsupported_explicit_format_fails_closed` - L31-L33

```python
test_unsupported_explicit_format_fails_closed(configured)
```

Observed calls (lexical order): `pytest.raises`, `Db2DateFormatService`.

### `test_format_change_updates_helpers_and_sentinels_consistently` - L36-L44

```python
test_format_change_updates_helpers_and_sentinels_consistently()
```

Observed calls (lexical order): `Db2DateFormatService`, `Db2DateFormatService('ISO').apply`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
