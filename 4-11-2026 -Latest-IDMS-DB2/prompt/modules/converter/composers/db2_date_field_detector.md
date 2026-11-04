# `converter/composers/db2_date_field_detector.py`

Source: [converter/composers/db2_date_field_detector.py](../../../../converter/composers/db2_date_field_detector.py) | 153 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `931e856d623c50f9908b1453950145fe94c95e11412263f1af1d047662e300e7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Detects DB2 DATE hosts that take part in a COBOL comparison.

## Module-level bindings

`__all__` (L153)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from converter.composers.db2_date_condition_assembler import ConditionSpan, Db2DateConditionAssembler
from converter.composers.db2_date_line_utils import Db2DateLineUtils
from patterns.db2_date_patterns import COMPARISON_OPERATOR_PATTERN, DB2_DATE_HOST_OPERAND_PATTERN, DB2_SHARED_DATE_HELPER_USAGE_PATTERN, PROCEDURE_DIVISION_PATTERN, SQL_HOST_OPERAND_PATTERN
```

## Local dependency notes

- [converter/composers/db2_date_condition_assembler.py](db2_date_condition_assembler.md)
- [converter/composers/db2_date_line_utils.py](db2_date_line_utils.md)
- [patterns/db2_date_patterns.py](../../patterns/db2_date_patterns.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/db2_date_comparison_composer.py](db2_date_comparison_composer.md)
- [converter/composers/db2_date_comparison_rewriter.py](db2_date_comparison_rewriter.md)
- [tests/test_db2_date_comparison.py](../../tests/test_db2_date_comparison.md)

## Symbol contracts and control points

### `DateOperand` - L42-L50

```python
class DateOperand()
```

One `DA-xxx OF DCLyyy` reference inside a condition.

Declared class/data-model fields:

```python
field: str = ''
group: str = ''
```

### `DateOperand.reference` - L49-L50

```python
reference(self) -> str
```

### `Db2DateFieldDetector` - L53-L150

```python
class Db2DateFieldDetector()
```

### `Db2DateFieldDetector.__init__` - L54-L62

```python
__init__(self, line_utils: Db2DateLineUtils | None=None, assembler: Db2DateConditionAssembler | None=None) -> None
```

Observed calls (lexical order): `Db2DateLineUtils`, `Db2DateConditionAssembler`.

### `Db2DateFieldDetector.date_fields_used_in_comparisons` - L67-L85

```python
date_fields_used_in_comparisons(self, lines: list[str]) -> list[str]
```

Distinct DATE host field names compared anywhere, in order.

Observed calls (lexical order): `set`, `self.assembler.spans`, `self.operands_in`, `self.line_utils.clean_cobol_name`, `seen.add`, `output.append`.

Control points:

- L75: `for span in self.assembler.spans(lines)`
- L76: `for operand in self.operands_in(span)`
- L79: `if not name or name in seen`

### `Db2DateFieldDetector.operands_in` - L87-L123

```python
operands_in(self, span: ConditionSpan) -> list[DateOperand]
```

Every DATE operand of one condition, duplicates removed.

Observed calls (lexical order): `getattr`, `str`, `COMPARISON_OPERATOR_PATTERN.search`, `SQL_HOST_OPERAND_PATTERN.sub`, `set`, `DB2_DATE_HOST_OPERAND_PATTERN.finditer`, `found.group`, `self.line_utils.clean_cobol_name`, `seen.add`, `DateOperand`, `output.append`.

Control points:

- L96: `if not text`
- L99: `if not COMPARISON_OPERATOR_PATTERN.search(text)`
- L108: `for found in DB2_DATE_HOST_OPERAND_PATTERN.finditer(scannable)`
- L112: `if not field or not group`
- L117: `if key in seen`

### `Db2DateFieldDetector.shared_date_helpers_used_in_procedure` - L125-L150

```python
shared_date_helpers_used_in_procedure(self, lines: list[str]) -> bool
```

Observed calls (lexical order): `self.line_utils.logical`, `PROCEDURE_DIVISION_PATTERN.match`, `self.line_utils.is_comment_or_blank`, `DB2_SHARED_DATE_HELPER_USAGE_PATTERN.search`.

Control points:

- L131: `for line in lines`
- L134: `if not logical`
- L137: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L141: `if not in_procedure_division`
- L144: `if self.line_utils.is_comment_or_blank(logical)`
- L147: `if DB2_SHARED_DATE_HELPER_USAGE_PATTERN.search(logical)`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
