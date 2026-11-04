# `converter/composers/lifecycle_standardization_composer.py`

Source: [converter/composers/lifecycle_standardization_composer.py](../../../../converter/composers/lifecycle_standardization_composer.py) | 957 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `f4e2d8c3816ed4b76a29f97610cfcc7f4c8e084cc2180627381e75ad82df8bc2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Source-aware, fail-closed COBOL lifecycle standardization.

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from rules.cursor_rules import cursor_paragraph_number
```

## Local dependency notes

- [rules/cursor_rules.py](../../rules/cursor_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_paragraph_numbering_composer.py](cursor_paragraph_numbering_composer.md)
- [converter/services/final_generated_output_service.py](../services/final_generated_output_service.md)
- [tests/pipeline/test_single_owner_transformations.py](../../tests/pipeline/test_single_owner_transformations.md)
- [tests/test_lifecycle_standardization_composer.py](../../tests/test_lifecycle_standardization_composer.md)
- [tests/test_lifecycle_standardization_six_programs.py](../../tests/test_lifecycle_standardization_six_programs.md)

## Symbol contracts and control points

### `_logical` - L15-L19

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `text[7:72].strip`, `text.strip`.

Control points:

- L17: `if len(text) >= 7 and text[:6].isdigit()`

### `_is_comment` - L22-L26

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L24: `if len(text) >= 7 and text[:6].isdigit() and (text[6] in '*/Dd')`

### `_is_area_a_paragraph` - L29-L35

```python
_is_area_a_paragraph(line: str) -> bool
```

Observed calls (lexical order): `_logical`, `re.fullmatch`, `str`, `len`, `raw[:6].isdigit`, `area.lstrip`.

Control points:

- L31: `if not re.fullmatch('[A-Z0-9][A-Z0-9-]*\\.', body, re.I)`

### `_append_period` - L38-L47

```python
_append_period(line: str) -> str
```

Observed calls (lexical order): `_logical`, `body.endswith`, `len`, `line[:6].isdigit`, `line[7:72].rstrip`, `ValueError`, `area.ljust`, `line.rstrip`.

Control points:

- L40: `if not body or body.endswith('.')`
- L42: `if len(line) >= 7 and line[:6].isdigit()`
- L44: `if len(area) > 65`

Explicit raises: `ValueError('cannot terminate final DISPLAY within fixed-format Area B')`.

### `_render` - L50-L52

```python
_render(body: str) -> str
```

### `_perform_thru_lines` - L55-L63

```python
_perform_thru_lines(start: str, end: str) -> list[str]
```

Observed calls (lexical order): `len`, `ValueError`.

Control points:

- L57: `if len(statement) <= 65`
- L61: `if len(first) > 65 or len(second) > 65`

Explicit raises: `ValueError('PERFORM THRU targets cannot be rendered within fixed-format Area B')`.

### `_Paragraph` - L67-L70

```python
class _Paragraph()
```

Declared class/data-model fields:

```python
name: str
start: int
end: int
```

### `LifecycleStandardizationComposer` - L73-L957

```python
class LifecycleStandardizationComposer()
```

Normalize recognized legacy lifecycle flows without rewriting inner loops.

### `LifecycleStandardizationComposer.__init__` - L76-L77

```python
__init__(self) -> None
```

### `LifecycleStandardizationComposer.compose` - L79-L125

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `source.splitlines`, `self._plan`, `any`, `self._plan_cursor_bounded_flow`, `self._plan_mainline_loop_flow`, `self._normalize_timestamp_paragraph`, `self._normalize_cursor_paragraph_numbers`, `'\n'.join`, `source.endswith`, `plan.get`, `self._apply_cursor_bounded_flow`, `self._apply_mainline_loop_flow`, `self._apply`, `self.messages.append`.

Control points:

- L82: `if not source`
- L87: `if plan is None and any(('Lifecycle standardization skipped:' in msg for msg in self.messages))`
- L89: `if plan is None`
- L92: `if plan is None and any(('Lifecycle standardization skipped:' in msg for msg in self.messages))`
- L94: `if plan is None`
- L97: `if plan is None`
- L100: `if renamed == lines`
- L104: `if plan.get('generic_cursor_bounded')`
- Another 2 conditions/loops exist in this source span.

### `LifecycleStandardizationComposer._plan` - L127-L341

```python
_plan(self, lines: list[str]) -> dict | None
```

Observed calls (lexical order): `next`, `enumerate`, `_logical`, `re.match`, `self.messages.append`, `self._paragraphs`, `p.name.upper`, `len`, `set`, `self._skip`, `any`, `range`, `_is_comment`, `m.group`, `re.fullmatch`, `m.group(1).upper`.
Another 32 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L133: `if pd_idx < 0`
- L137: `if not paragraphs`
- L141: `if len(paragraph_name_list) != len(set(paragraph_name_list))`
- L143: `if any((p.name.upper() == '0000-MAIN-PROCEDURE' for p in paragraphs))`
- L150: `if any((p.name.upper() in reserved for p in paragraphs))`
- L157: `if not top`
- L164: `if len(timestamps) > 1`
- L170: `for (pos, (line_idx, body)) in enumerate(top)`
- Another 35 conditions/loops exist in this source span.

### `LifecycleStandardizationComposer._plan_cursor_bounded_flow` - L344-L427

```python
_plan_cursor_bounded_flow(self, lines: list[str]) -> dict | None
```

Recognize a conservative non-BEGIN/EINDE mainline by cursor boundaries.

Observed calls (lexical order): `next`, `enumerate`, `_logical`, `re.match`, `self._paragraphs`, `p.name.upper`, `any`, `len`, `set`, `range`, `_is_comment`, `re.search`, `re.fullmatch`, `match.group`, `match.group(1).upper`, `by_name.get`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L356: `if pd_idx < 0`
- L359: `if not paragraphs`
- L362: `if len(names) != len(set(names)) or any((name in {'0000-MAIN-PROCEDURE', '1000-INITIALIZE-PROGRAM', '2000-PROCESS-PROGRAM', '2000-TREAT-PROGRAM', '3000-FINALIZE-PROGRAM'} for name ...`
- L371: `if not top`
- L374: `if any((re.search('\\bPERFORM\\s+[A-Z0-9][A-Z0-9-]*\\s+(?:THRU|THROUGH)\\b', body, re.I) for _, body in top))`
- L379: `if len(exits) != 1`
- L383: `for (line_index, body) in top`
- L388: `if not match`
- Another 7 conditions/loops exist in this source span.

### `LifecycleStandardizationComposer._plan_mainline_loop_flow` - L429-L551

```python
_plan_mainline_loop_flow(self, lines: list[str]) -> dict | None
```

Split a clearly bounded mainline loop into lifecycle wrappers.

Observed calls (lexical order): `next`, `enumerate`, `_logical`, `re.match`, `self._paragraphs`, `p.name.upper`, `any`, `len`, `set`, `list`, `range`, `find_loop`, `re.fullmatch`, `sum`, `re.compile`, `re.escape`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L442: `if pd_idx < 0`
- L446: `if len(names) != len(set(names)) or any((name in {'0000-MAIN-PROCEDURE', '1000-INITIALIZE-PROGRAM', '2000-PROCESS-PROGRAM', '3000-FINALIZE-PROGRAM'} for name in names))`
- L480: `if not loops and first_para`
- L492: `if len(candidate_loops) == 1 and len(terminal_indices) == 1 and (perform_count >= 2)`
- L500: `for (i, line) in enumerate(lines)`
- L501: `if i == controller.start or _is_comment(line)`
- L503: `if ref.search(_logical(line))`
- L505: `if len(loops) != 1`
- Another 5 conditions/loops exist in this source span.

### `LifecycleStandardizationComposer._plan_mainline_loop_flow.executable` - L456-L457

```python
executable(index: int) -> bool
```

Observed calls (lexical order): `_is_comment`, `_logical`, `bool`.

### `LifecycleStandardizationComposer._plan_mainline_loop_flow.find_loop` - L459-L474

```python
find_loop(indices: list[int]) -> list[tuple[int, int]]
```

Observed calls (lexical order): `executable`, `enumerate`, `_logical`, `re.match`, `re.search`, `match.group`, `loops.append`, `len`.

Control points:

- L462: `for (pos, index) in enumerate(executable_indices)`
- L465: `if not match or re.search('\\bTHRU\\b|\\bTHROUGH\\b', body, re.I)`
- L468: `if re.search('\\bUNTIL\\b', tail, re.I)`
- L470: `if pos + 1 < len(executable_indices) and re.match('^UNTIL\\b', _logical(lines[executable_indices[pos + 1]]), re.I)`

### `LifecycleStandardizationComposer._apply_mainline_loop_flow` - L553-L605

```python
_apply_mainline_loop_flow(self, original: list[str], plan: dict) -> list[str]
```

Wrap a single source-proven mainline loop without changing SQL policy.

Observed calls (lexical order): `set`, `retained_range`, `range`, `max`, `terminate_last_statement`, `generated.extend`, `generated.append`.

Control points:

- L601: `if controller`

### `LifecycleStandardizationComposer._apply_mainline_loop_flow.retained_range` - L562-L566

```python
retained_range(start: int, end: int) -> list[str]
```

Observed calls (lexical order): `range`, `_logical`.

### `LifecycleStandardizationComposer._apply_mainline_loop_flow.terminate_last_statement` - L575-L581

```python
terminate_last_statement(section: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `_is_comment`, `_logical`, `_append_period`.

Control points:

- L578: `if executable_section`

### `LifecycleStandardizationComposer._normalize_cursor_paragraph_numbers` - L607-L774

```python
_normalize_cursor_paragraph_numbers(self, lines: list[str]) -> list[str]
```

Normalize existing cursor operation paragraphs from SQL source evidence.

Observed calls (lexical order): `next`, `enumerate`, `_logical`, `re.match`, `self._paragraphs`, `re.fullmatch`, `match.group`, `match.group('operation').upper`, `_is_comment`, `' '.join`, `' '.join((re.sub('\'(?:\'\'|[^\'])*\'|\\"(?:\\"\\"|[^\\"])*\\"', ' ', body) for body in code_lines)).upper`, `re.sub`, `re.findall`, `len`, `set`, `sql_names[0].upper`.
Another 29 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L622: `if pd_idx < 0`
- L626: `for para in paragraphs`
- L632: `if not match`
- L647: `if len(set(sql_names)) != 1`
- L650: `if cursor_name not in match.group('suffix').upper()`
- L665: `if not operation_labels`
- L684: `if declaration_order`
- L685: `if any((cursor not in declaration_order for cursor in discovered_cursors))`
- Another 16 conditions/loops exist in this source span.

Explicit raises: `ValueError('SQL-LOCATION update exceeds fixed-format Area B')`.

### `LifecycleStandardizationComposer._normalize_timestamp_paragraph` - L776-L808

```python
_normalize_timestamp_paragraph(self, lines: list[str]) -> list[str]
```

Rename one existing timestamp paragraph to 1100 when that number is free.

Observed calls (lexical order): `next`, `enumerate`, `_logical`, `re.match`, `self._paragraphs`, `p.name.upper`, `len`, `self.messages.append`, `timestamp.name.upper`, `p.name.upper().startswith`, `self._replace_identifiers`.

Control points:

- L788: `if pd_idx < 0`
- L792: `if len(timestamps) != 1`
- L793: `if len(timestamps) > 1`
- L798: `if timestamp.name.upper() == target`
- L801: `if occupied_1100`

### `LifecycleStandardizationComposer._apply_cursor_bounded_flow` - L810-L840

```python
_apply_cursor_bounded_flow(self, original: list[str], plan: dict) -> list[str]
```

Wrap the original mainline slices without changing their statements.

Observed calls (lexical order): `self._paragraphs`, `_is_comment`, `_logical`, `prefix.append`, `len`, `generated.extend`, `generated.append`.

Control points:

- L818: `for line in original[pd_idx + 1:plan['open_idx']]`
- L819: `if _logical(line) and (not _is_comment(line))`

### `LifecycleStandardizationComposer._apply` - L842-L898

```python
_apply(self, original: list[str], plan: dict) -> list[str]
```

Observed calls (lexical order): `list`, `sorted`, `lines.pop`, `_logical`, `enumerate`, `next`, `re.match`, `self._paragraphs`, `_is_comment`, `generated.append`, `self._standard_begin_name`, `_perform_thru_lines`, `generated.extend`, `_append_period`, `_render`, `self._replace_identifiers`.

Control points:

- L848: `for index in sorted(plan['cursor_setup_indices'], reverse=True)`
- L870: `if plan['timestamp']`
- L886: `if totals`

### `LifecycleStandardizationComposer._standard_begin_name` - L901-L909

```python
_standard_begin_name(original: str) -> str
```

Number an existing BEGIN paragraph as 1200 without inventing one.

Observed calls (lexical order): `original.upper`, `name.startswith`, `re.sub`.

Control points:

- L904: `if name.startswith('1200-')`

### `LifecycleStandardizationComposer._paragraphs` - L912-L920

```python
_paragraphs(lines: list[str], start: int) -> list[_Paragraph]
```

Observed calls (lexical order): `len`, `range`, `_is_area_a_paragraph`, `_is_comment`, `_logical`, `starts.append`, `_Paragraph`, `enumerate`.

Control points:

- L914: `for i in range(start, len(lines))`
- L915: `if not _is_comment(lines[i]) and _is_area_a_paragraph(lines[i])`

### `LifecycleStandardizationComposer._replace_identifiers` - L922-L947

```python
_replace_identifiers(self, lines: list[str], mapping: dict[str, str]) -> list[str]
```

Observed calls (lexical order): `re.compile`, `_is_comment`, `out.append`, `len`, `line[72:80].isdigit`, `line[:6].isdigit`, `line[start:end].rstrip`, `literal_pattern.finditer`, `match.start`, `chunks.append`, `self._replace_segment`, `match.group`, `match.end`, `''.join`, `ValueError`, `rewritten.ljust`.

Control points:

- L925: `for line in lines`
- L926: `if _is_comment(line)`
- L934: `for match in literal_pattern.finditer(body)`
- L941: `if fixed`
- L942: `if len(rewritten) > 65`

Explicit raises: `ValueError('renamed paragraph/reference exceeds fixed-format Area B')`.

### `LifecycleStandardizationComposer._replace_segment` - L950-L953

```python
_replace_segment(segment: str, mapping: dict[str, str]) -> str
```

Observed calls (lexical order): `len`, `mapping.items`, `sorted`, `re.escape`, `re.sub`.

Control points:

- L951: `for (old, new) in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True)`

### `LifecycleStandardizationComposer._skip` - L955-L957

```python
_skip(self, reason: str)
```

Observed calls (lexical order): `self.messages.append`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
