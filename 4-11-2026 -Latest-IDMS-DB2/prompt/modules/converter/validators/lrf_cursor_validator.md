# `converter/validators/lrf_cursor_validator.py`

Source: [converter/validators/lrf_cursor_validator.py](../../../../converter/validators/lrf_cursor_validator.py) | 304 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `75aa6b9c75fc445a88b9a086db2b612cba9529154bd041594722e7553588fb7c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Validation and diagnostic module for LRF cursor WHERE clause generation.

## Import declarations

```python
from __future__ import annotations
import re
from typing import NamedTuple
```

## Symbol contracts and control points

### `CursorValidationIssue` - L16-L24

```python
class CursorValidationIssue(NamedTuple)
```

Represents a validation issue in a cursor.

Declared class/data-model fields:

```python
severity: str
cursor_name: str
record_name: str
issue_type: str
description: str
affected_element: str
```

### `LrfCursorValidator` - L27-L202

```python
class LrfCursorValidator()
```

Validates LRF cursor specs for correctness.

### `LrfCursorValidator.__init__` - L30-L32

```python
__init__(self, mapping_repository=None)
```

### `LrfCursorValidator.validate_cursor_spec` - L34-L131

```python
validate_cursor_spec(self, spec: dict[str, object], cobol_text: str='') -> list[CursorValidationIssue]
```

Validate a single cursor specification.

Observed calls (lexical order): `spec.get`, `str`, `issues.append`, `CursorValidationIssue`, `str(c).strip`, `str(c).strip().split`, `re.match`, `match.group`, `match.group(1).upper`, `spec.get('lrf_mode', '').upper`, `str(expr).upper`, `len`.

Control points:

- L61: `if is_lrf and (not where_conditions)`
- L79: `for condition in where_conditions`
- L82: `if match`
- L84: `if child_col not in select_columns`
- L99: `if is_lrf`
- L102: `if lrf_mode == 'NEXT'`
- L103: `for expr in order_by_columns`
- L105: `if 'ASC' in expr_str and 'DESC' not in expr_str`
- Another 1 conditions/loops exist in this source span.

### `LrfCursorValidator.validate_all_specs` - L133-L151

```python
validate_all_specs(self, specs: list[dict[str, object]], cobol_text: str='') -> list[CursorValidationIssue]
```

Validate all cursor specs in a conversion result.

Observed calls (lexical order): `self.validate_cursor_spec`, `all_issues.extend`.

Control points:

- L148: `for spec in specs or []`

### `LrfCursorValidator.generate_validation_report` - L153-L202

```python
generate_validation_report(self, specs: list[dict[str, object]], cobol_text: str='', program_name: str='') -> str
```

Generate a human-readable validation report.

Observed calls (lexical order): `self.validate_all_specs`, `lines.append`, `len`, `'\n'.join`.

Control points:

- L178: `if not issues`
- L185: `if errors`
- L187: `for issue in errors`
- L192: `if warnings`
- L194: `for issue in warnings`

### `CursorComparisonValidator` - L205-L304

```python
class CursorComparisonValidator()
```

Compare generated cursor specs with expected/manual versions.

### `CursorComparisonValidator.compare_where_clauses` - L209-L239

```python
compare_where_clauses(generated_where: list[str], expected_where: list[str]) -> tuple[bool, list[str]]
```

Compare WHERE clause sets.

Observed calls (lexical order): `str`, `str(w).strip`, `differences.append`, `', '.join`.

Control points:

- L230: `if missing`
- L234: `if extra`

### `CursorComparisonValidator.compare_select_columns` - L242-L269

```python
compare_select_columns(generated_cols: list[str], expected_cols: list[str]) -> tuple[bool, list[str]]
```

Compare SELECT column sets.

Observed calls (lexical order): `str`, `str(c).strip`, `str(c).strip().split`, `', '.join`, `differences.append`, `sorted`.

Control points:

- L263: `if missing`
- L265: `if extra`

### `CursorComparisonValidator.compare_order_by` - L272-L304

```python
compare_order_by(generated_order: list[str], expected_order: list[str]) -> tuple[bool, list[str]]
```

Compare ORDER BY specifications.

Observed calls (lexical order): `' '.join`, `str`, `str(o).strip`, `exp_str.replace`, `exp_str.replace('DESC', '').replace`, `gen_str.replace`, `gen_str.replace('DESC', '').replace`, `differences.append`.

Control points:

- L287: `if not generated_order and (not expected_order)`
- L293: `if gen_str.replace('DESC', '').replace('ASC', '') != exp_str.replace('DESC', '').replace('ASC', '')`
- L299: `if gen_str != exp_str`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
