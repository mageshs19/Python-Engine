# `converter/analyzers/lr_access/handwritten_obtain_calc_planner.py`

Source: [converter/analyzers/lr_access/handwritten_obtain_calc_planner.py](../../../../../converter/analyzers/lr_access/handwritten_obtain_calc_planner.py) | 221 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `54735b1aa10fad5927673313156afa79ef380bcd7285ac3c4cbffbfa1c4b7a34`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Conservative planner for hand-written retrieval OBTAIN CALC reads.

## Module-level bindings

`__all__` (L221)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline_steps.py](../../pipeline/conversion/conversion_pipeline_steps.md)
- [tests/test_handwritten_obtain_calc_planner.py](../../../tests/test_handwritten_obtain_calc_planner.md)

## Symbol contracts and control points

### `HandwrittenCalcReadPlan` - L17-L22

```python
class HandwrittenCalcReadPlan()
```

Declared class/data-model fields:

```python
record: str
table: str
key_columns: tuple[str, ...]
existence_column: str
dclgen_group: str
```

### `HandwrittenObtainCalcPlanner` - L25-L218

```python
class HandwrittenObtainCalcPlanner()
```

Declared class/data-model fields:

```python
_FIELD = re.compile('^\\s*(?P<level>\\d{1,2})\\s+(?P<name>[A-Z0-9-]+)', re.I)
_ACCESS = re.compile('\\bOBTAIN\\s+CALC\\s+(?P<record>[A-Z][A-Z0-9-]*)\\b', re.I)
_PARAGRAPH = re.compile('^[A-Z0-9][A-Z0-9-]*\\.$', re.I)
_MOVE_TO_FIELD = re.compile('\\bMOVE\\s+(?!CORR\\b)(?P<src>[A-Z0-9-]+(?:\\s+OF\\s+[A-Z0-9-]+)?)\\s+TO\\s+(?P<field>[A-Z][A-Z0-9-]*)\\s+(?:OF|IN)\\s+(?P<record>[A-Z][A-Z0-9-]*)\\b', re.I)
_IF_OPEN = re.compile('^IF\\b', re.I)
_IF_CLOSE = re.compile('^END-IF\\b', re.I)
_EVALUATE_OPEN = re.compile('^EVALUATE\\b', re.I)
_EVALUATE_CLOSE = re.compile('^END-EVALUATE\\b', re.I)
_SUPPORTED_STATUS_IF = re.compile('^IF\\s+ERROR-STATUS\\s+(?:NOT\\s+)?=\\s*([\'\\"])0000\\1\\s*\\.?$', re.I)
```

### `HandwrittenObtainCalcPlanner.__init__` - L42-L45

```python
__init__(self, mapping_repository, table_name_resolver, host_variable_resolver)
```

### `HandwrittenObtainCalcPlanner.plan` - L47-L83

```python
plan(self, source_text: str, *, excluded_records=()) -> tuple[dict[str, dict[str, str]], list[str]]
```

Observed calls (lexical order): `self._logical_lines`, `NameNormalizer.normalize`, `enumerate`, `self._ACCESS.search`, `match.group`, `accesses.setdefault`, `accesses.setdefault(record, []).append`, `accesses.items`, `len`, `diagnostics.append`, `self._plan_one`, `' '.join`.

Control points:

- L51: `for (index, line) in enumerate(lines)`
- L53: `if match`
- L59: `for (record, positions) in accesses.items()`
- L60: `if record in excluded`
- L62: `if len(positions) != 1`
- L70: `if plan is None`

### `HandwrittenObtainCalcPlanner._plan_one` - L85-L201

```python
_plan_one(self, lines: list[str], access_index: int, record: str)
```

Observed calls (lexical order): `list`, `self.mapping.rows_for_record`, `self.table_resolver.table_for_record`, `getattr`, `str`, `self._FIELD.match`, `NameNormalizer.to_cobol`, `field_match.group`, `NameNormalizer.normalize`, `self.hosts.host_reference_for_column`, `key_fields.append`, `dict.fromkeys`, `range`, `lines[index].strip`, `self._PARAGRAPH.match`, `enumerate`.
Another 20 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L91: `if not table`
- L95: `for row in rows`
- L98: `if not field_match`
- L107: `if not field_name or not column`
- L110: `if 'CALC' not in idms_key`
- L112: `if 'FOREIGN' in key_text or db2_key == 'FK'`
- L124: `if not is_key`
- L126: `if not self.hosts.host_reference_for_column(table, column)`
- Another 19 conditions/loops exist in this source span.

### `HandwrittenObtainCalcPlanner._logical_lines` - L204-L218

```python
_logical_lines(source_text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(source_text or '').splitlines`, `raw.rstrip`, `len`, `line[:6].strip`, `line[:6].strip().isdigit`, `output.append`, `line.lstrip`, `line.lstrip().startswith`, `line.upper`.

Control points:

- L206: `for raw in str(source_text or '').splitlines()`
- L208: `if len(line) > 6 and line[:6].strip().isdigit()`
- L210: `if indicator in '*/'`
- L214: `if line.lstrip().startswith(('*', '/'))`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
