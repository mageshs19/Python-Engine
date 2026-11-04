# `converter/services/db2_date_format_service.py`

Source: [converter/services/db2_date_format_service.py](../../../../converter/services/db2_date_format_service.py) | 80 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `9797eca3d42d18328316f64883059fb3a7de431352c41fadff21baf8d4931891`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date format service.

## Import declarations

```python
from __future__ import annotations
from patterns.final_feedback_fix_patterns import DATE_HELPER_EUR_PATTERN, DATE_HIGH_EUR_LITERAL_PATTERN, DATE_LOW_EUR_LITERAL_PATTERN
from rules.final_feedback_fix_rules import DATE_FORMAT_ALIASES, SUPPORTED_DB2_DATE_FORMATS, DB2_DATE_HELPER_BY_FORMAT, DB2_DATE_HIGH_LITERAL_BY_FORMAT, DB2_DATE_LOW_LITERAL_BY_FORMAT, DEFAULT_DB2_DATE_EXTERNAL_FORMAT
```

## Local dependency notes

- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/final_feedback_fix_rules.py](../../rules/final_feedback_fix_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)
- [tests/test_db2_date_format_service.py](../../tests/test_db2_date_format_service.md)

## Symbol contracts and control points

### `Db2DateFormatService` - L27-L80

```python
class Db2DateFormatService()
```

Applies configured DB2 external date format to generated date conversion.

### `Db2DateFormatService.__init__` - L36-L42

```python
__init__(self, date_external_format: str | None=None) -> None
```

Observed calls (lexical order): `self.normalize_format`.

### `Db2DateFormatService.apply` - L44-L61

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `DATE_HELPER_EUR_PATTERN.sub`, `DATE_LOW_EUR_LITERAL_PATTERN.sub`, `DATE_HIGH_EUR_LITERAL_PATTERN.sub`.

Control points:

- L47: `if not source`
- L50: `if self.date_external_format == 'DD.MM.YYYY'`

### `Db2DateFormatService.normalize_format` - L63-L80

```python
normalize_format(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `DATE_FORMAT_ALIASES.get`, `', '.join`, `sorted`, `ValueError`.

Control points:

- L66: `if not text`
- L69: `if not text`
- L73: `if normalized is None or normalized not in SUPPORTED_DB2_DATE_FORMATS`

Explicit raises: `ValueError(f'Unsupported DB2 date external format {value!r}. Supported formats: {supported}.')`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
