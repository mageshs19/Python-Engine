# `converter/composers/cleanup/business_control_flag_analyzer.py`

Source: [converter/composers/cleanup/business_control_flag_analyzer.py](../../../../../converter/composers/cleanup/business_control_flag_analyzer.py) | 182 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `40bf47ac31439a95f543b0ca26466ddba87646e6144f897aea85be0074dc72ad`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic discovery of COBOL business-control flags.

## Module-level bindings

`_Y_ASSIGNMENT` (L18), `_SET_TRUE` (L22), `_FLAG_DECLARATION` (L26), `_IF_START` (L30), `_CONDITION_READ` (L31), `__all__` (L182)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
import re
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.composers.cleanup.cursor_nesting_analyser import CursorNestingAnalyser
```

## Local dependency notes

- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [converter/composers/cleanup/cursor_nesting_analyser.py](cursor_nesting_analyser.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](child_fetch_early_stop_cleanup.md)
- [tests/test_business_control_flag_analyzer.py](../../../tests/test_business_control_flag_analyzer.md)

## Symbol contracts and control points

### `BusinessFlagEvidence` - L38-L52

```python
class BusinessFlagEvidence()
```

Declared class/data-model fields:

```python
name: str
declared: bool = False
assignments: list[dict[str, object]] = field(default_factory=list)
condition_reads: list[dict[str, object]] = field(default_factory=list)
output_reads: list[dict[str, object]] = field(default_factory=list)
```

### `BusinessFlagEvidence.trigger_conditions` - L46-L52

```python
trigger_conditions(self) -> list[str]
```

Observed calls (lexical order): `assignment.get`, `str`, `str(assignment.get('condition') or '').strip`, `values.append`.

Control points:

- L48: `for assignment in self.assignments`
- L50: `if condition and condition not in values`

### `BusinessControlFlagAnalyzer` - L55-L179

```python
class BusinessControlFlagAnalyzer()
```

Extract evidence for flags without relying on their names.

### `BusinessControlFlagAnalyzer.__init__` - L58-L60

```python
__init__(self, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`, `CursorNestingAnalyser`.

### `BusinessControlFlagAnalyzer.analyze` - L62-L129

```python
analyze(self, text_or_lines: str | list[str]) -> dict[str, BusinessFlagEvidence]
```

Observed calls (lexical order): `isinstance`, `list`, `text_or_lines.splitlines`, `self.cursor_nesting.paragraph_spans`, `set`, `self.line_utils.logical`, `self.line_utils.logical(line).strip`, `_FLAG_DECLARATION.match`, `declared.add`, `match.group`, `match.group('flag').upper`, `enumerate`, `logical.startswith`, `logical.endswith`, `logical[:-1].upper`, `_IF_START.match`.
Another 21 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L67: `for line in lines`
- L70: `if match`
- L75: `for (index, line) in enumerate(lines)`
- L77: `if not logical or logical.startswith(('*', '/'))`
- L80: `if header in spans`
- L86: `if if_match`
- L88: `if re.match('^END-IF\\b', logical, re.IGNORECASE)`
- L89: `if active_conditions`
- Another 12 conditions/loops exist in this source span.

### `BusinessControlFlagAnalyzer.discover_unique_yes_flag` - L131-L179

```python
discover_unique_yes_flag(self, lines: list[str], paragraphs: set[str] | list[str] | tuple[str, ...], *, cursor_name: str | None=None, require_control_read: bool=False) -> str | None
```

Return one flag only when its assignment is scoped to the requested flow.

Observed calls (lexical order): `self.analyze`, `str`, `str(p).upper`, `evidence.items`, `assignment.get`, `str(assignment.get('paragraph', '')).upper`, `f'-FETCH-{cursor_name}'.upper`, `any`, `int`, `self.line_utils.logical`, `self.line_utils.logical(lines[int(assignment['line']) - 1]).upper`, `self.cursor_nesting.paragraph_spans`, `self.line_utils.logical(lines[i]).upper`, `re.match`, `self.line_utils.logical(lines[i]).strip`, `range`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L148: `for (name, item) in evidence.items()`
- L153: `if not scoped_assignments`
- L155: `if cursor_name`
- L162: `if not flow_has_fetch`
- L174: `if not flow_has_fetch`
- L176: `if require_control_read and (not item.condition_reads)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
