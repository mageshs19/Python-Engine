# `converter/composers/cleanup/child_fetch_early_stop_cleanup.py`

Source: [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](../../../../../converter/composers/cleanup/child_fetch_early_stop_cleanup.py) | 807 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `ce2f61557ab0a18c4810de34ee06a59316c14e8d80717036f27a965da666b19d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Child fetch early-stop cleanup.

## Module-level bindings

`SW_STATUS_Y_CONTINUATION_INDENT` (L31)

## Import declarations

```python
import re
from converter.composers.cleanup.business_control_flag_analyzer import BusinessControlFlagAnalyzer
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.composers.cleanup.cursor_nesting_analyser import CursorNestingAnalyser
from patterns.cobol_cleanup_patterns import FETCH_PARAGRAPH_NUMBER_PATTERN, FETCH_UNTIL_EOC_FULL_SW_PATTERN, FETCH_UNTIL_EOC_OR_SW_PATTERN, FETCH_UNTIL_EOC_PATTERN, PARAGRAPH_HEADER_PATTERN, SW_STATUS_Y_CONTINUATION_PATTERN
```

## Local dependency notes

- [converter/composers/cleanup/business_control_flag_analyzer.py](business_control_flag_analyzer.md)
- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [converter/composers/cleanup/cursor_nesting_analyser.py](cursor_nesting_analyser.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [converter/pipeline/conversion/conversion_pipeline.py](../../pipeline/conversion/conversion_pipeline.md)
- [tests/test_output_write_placement_cleanup.py](../../../tests/test_output_write_placement_cleanup.md)
- [tests/test_sw_status_child_fetch_driven_normalization.py](../../../tests/test_sw_status_child_fetch_driven_normalization.md)

## Symbol contracts and control points

### `ChildFetchEarlyStopCleanup` - L34-L807

```python
class ChildFetchEarlyStopCleanup()
```

### `ChildFetchEarlyStopCleanup.__init__` - L35-L43

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`, `CursorNestingAnalyser`, `BusinessControlFlagAnalyzer`.

### `ChildFetchEarlyStopCleanup._logical` - L45-L46

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `ChildFetchEarlyStopCleanup._leading_spaces` - L48-L49

```python
_leading_spaces(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.leading_spaces`.

### `ChildFetchEarlyStopCleanup._normalize_sw_status_child_loop` - L51-L387

```python
_normalize_sw_status_child_loop(self, text: str) -> str
```

Normalize a legacy child business-loop into FETCH-driven processing.

Observed calls (lexical order): `text.splitlines`, `self.cursor_nesting.paragraph_spans`, `spans.items`, `logical_at`, `range`, `re.match`, `m.group`, `m.group(1).upper`, `m.group(2).upper`, `opens.append`, `name.upper`, `upper.endswith`, `re.compile`, `re.escape`, `re.match('^PERFORM\\s+([A-Z][A-Z0-9-]*)', item, re.I).group`, `type`.
Another 38 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L65: `if not spans`
- L102: `for (owner, (owner_start, owner_end)) in spans.items()`
- L105: `for item in body`
- L107: `if m`
- L109: `for (open_name, cursor) in opens`
- L111: `for name in spans`
- L113: `if upper.endswith(f'-FETCH-{cursor}')`
- L115: `if upper.endswith(f'-CLOSE-{cursor}')`
- Another 55 conditions/loops exist in this source span.

### `ChildFetchEarlyStopCleanup._normalize_sw_status_child_loop.render_like` - L68-L82

```python
render_like(reference: str, body: str) -> str
```

Render an intermediate line without cloning sequence numbers.

Observed calls (lexical order): `str`, `len`, `raw[:6].isdigit`, `body.rstrip`, `indicator.strip`, `self._leading_spaces`, `body.lstrip`.

Control points:

- L78: `if len(raw) >= 72 and raw[:6].isdigit()`

### `ChildFetchEarlyStopCleanup._normalize_sw_status_child_loop.finalize_fixed_format` - L84-L91

```python
finalize_fixed_format(value: str) -> str
```

Return semantic intermediate text; layout belongs to the owner.

### `ChildFetchEarlyStopCleanup._normalize_sw_status_child_loop.logical_at` - L93-L94

```python
logical_at(index: int) -> str
```

Observed calls (lexical order): `self._logical`, `self._logical(lines[index]).strip`.

### `ChildFetchEarlyStopCleanup._normalize_sw_status_child_loop.find_span` - L96-L97

```python
find_span(name: str)
```

Observed calls (lexical order): `spans.get`, `str`, `str(name or '').strip`, `str(name or '').strip().upper`.

### `ChildFetchEarlyStopCleanup._normalize_sw_status_child_loop.matching_end_if` - L237-L247

```python
matching_end_if(start: int, limit: int) -> int
```

Observed calls (lexical order): `range`, `logical_at`, `re.match`.

Control points:

- L239: `for pos in range(start, limit + 1)`
- L241: `if re.match('^IF\\b', item, re.I)`
- L243: `if re.match('^END-IF\\b', item, re.I)`
- L245: `if depth == 0`

### `ChildFetchEarlyStopCleanup._normalize_sw_status_child_loop.source_area` - L297-L301

```python
source_area(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `raw[7:72].rstrip`, `raw.rstrip`.

Control points:

- L299: `if len(raw) >= 72`

### `ChildFetchEarlyStopCleanup.ensure_child_fetch_early_stop` - L389-L516

```python
ensure_child_fetch_early_stop(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `len`, `self._logical`, `re.match`, `self._logical(lines[index + 1]).strip`, `business_head.group`, `FETCH_PARAGRAPH_NUMBER_PATTERN.match`, `target.upper`, `self._business_loop_stop_flag`, `until_match.group`, `self._append_business_loop_early_stop`, `business_match.group`, `business_match.group('target').upper`, `self._append_early_stop`, `FETCH_UNTIL_EOC_FULL_SW_PATTERN.match`, `self._is_child_or_nested_fetch`.
Another 17 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L390: `if not text`
- L398: `while index < len(lines)`
- L409: `if business_head and index + 1 < len(lines)`
- L416: `if until_match and (not FETCH_PARAGRAPH_NUMBER_PATTERN.match(target.upper())) and self._business_loop_stop_flag(lines, target, until_match.group('eoc'))`
- L446: `if business_match and (not FETCH_PARAGRAPH_NUMBER_PATTERN.match(business_match.group('target').upper())) and self._business_loop_stop_flag(lines, business_match.group('target'), bu...`
- L466: `if full_match and self._is_child_or_nested_fetch(lines, full_match.group('fetch'))`
- L470: `if stop_flag`
- L479: `if or_match and self._is_child_or_nested_fetch(lines, or_match.group('fetch'))`
- Another 4 conditions/loops exist in this source span.

### `ChildFetchEarlyStopCleanup._flag_from_loop_condition` - L519-L526

```python
_flag_from_loop_condition(logical: str) -> str | None
```

Read the actual flag from an existing EOC OR flag='Y' condition.

Observed calls (lexical order): `re.search`, `match.group`, `match.group('flag').upper`.

### `ChildFetchEarlyStopCleanup._append_early_stop` - L528-L543

```python
_append_early_stop(self, output: list[str], line: str, match, stop_flag: str) -> None
```

Observed calls (lexical order): `self._leading_spaces`, `match.groupdict`, `match.groupdict().get`, `match.group`, `self._previous_output_has_reset`, `output.append`.

Control points:

- L539: `if not self._previous_output_has_reset(output, stop_flag)`

### `ChildFetchEarlyStopCleanup._next_line_is_sw_status_y_continuation` - L545-L554

```python
_next_line_is_sw_status_y_continuation(self, lines: list[str], index: int) -> bool
```

Observed calls (lexical order): `len`, `self._logical`, `SW_STATUS_Y_CONTINUATION_PATTERN.match`, `bool`.

Control points:

- L550: `if index + 1 >= len(lines)`

### `ChildFetchEarlyStopCleanup._previous_output_has_reset` - L556-L601

```python
_previous_output_has_reset(self, output: list[str], flag: str) -> bool
```

Check for a still-valid reset in this paragraph's current flow.

Observed calls (lexical order): `reversed`, `self._logical`, `self._logical(line).strip`, `logical.startswith`, `re.escape`, `re.match`, `FETCH_UNTIL_EOC_PATTERN.match`, `FETCH_UNTIL_EOC_OR_SW_PATTERN.match`, `FETCH_UNTIL_EOC_FULL_SW_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `logical.endswith`.

Control points:

- L566: `for line in reversed(output)`
- L568: `if not logical or logical.startswith(('*', '/'))`
- L571: `if re.match(f"""^MOVE\\s+['\\"]N['\\"]\\s+TO\\s+{re.escape(flag)}\\b""", logical, re.I)`
- L574: `if re.match(f"""^MOVE\\s+['\\"]Y['\\"]\\s+TO\\s+{re.escape(flag)}\\.?$""", logical, re.I)`
- L581: `if FETCH_UNTIL_EOC_PATTERN.match(logical) or FETCH_UNTIL_EOC_OR_SW_PATTERN.match(logical) or FETCH_UNTIL_EOC_FULL_SW_PATTERN.match(logical) or re.match('^PERFORM\\s+[0-9]+-FETCH-[A...`
- L598: `if PARAGRAPH_HEADER_PATTERN.match(logical) and logical.endswith('.')`

### `ChildFetchEarlyStopCleanup._append_business_loop_early_stop` - L604-L616

```python
_append_business_loop_early_stop(self, output: list[str], line: str, business_paragraph: str, eoc_flag: str, stop_flag: str) -> None
```

Observed calls (lexical order): `self._leading_spaces`, `self._previous_output_has_reset`, `output.append`.

Control points:

- L613: `if not self._previous_output_has_reset(output, stop_flag)`

### `ChildFetchEarlyStopCleanup._business_loop_stop_flag` - L618-L646

```python
_business_loop_stop_flag(self, lines: list[str], business_paragraph: str, eoc_flag: str) -> str | None
```

Infer the loop's business stop flag without relying on its name.

Observed calls (lexical order): `self.cursor_nesting.paragraph_spans`, `spans.get`, `str`, `str(business_paragraph or '').strip`, `str(business_paragraph or '').strip().upper`, `range`, `self._logical`, `self._logical(lines[i]).strip`, `re.sub`, `str(eoc_flag or '').strip`, `re.match`, `f'-FETCH-{cursor_name}'.upper`, `match.group`, `match.group('target').upper`, `match.group('target').upper().endswith`, `fetch_targets.append`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L624: `if span is None`
- L630: `for item in body`
- L632: `if match and match.group('target').upper().endswith(f'-FETCH-{cursor_name}'.upper())`
- L634: `if not fetch_targets or not self._is_nested_business_loop(lines, cursor_name)`

### `ChildFetchEarlyStopCleanup._is_nested_business_loop` - L648-L719

```python
_is_nested_business_loop(self, lines: list[str], cursor_name: str) -> bool
```

Prove a child cursor is nested under a parent-record loop.

Observed calls (lexical order): `self.cursor_nesting.paragraph_spans`, `str`, `str(cursor_name or '').strip`, `str(cursor_name or '').strip().upper`, `re.compile`, `re.escape`, `spans.items`, `self._logical`, `self._logical(lines[i]).strip`, `range`, `any`, `open_pattern.match`, `fetch_pattern.match`, `self.cursor_nesting.is_nested_fetch`, `self._fetch_name_for_cursor`, `enumerate`.
Another 9 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L668: `for (owner, (start, end)) in spans.items()`
- L675: `if not (has_open and has_fetch)`
- L681: `if self.cursor_nesting.is_nested_fetch(lines, self._fetch_name_for_cursor(lines, cursor))`
- L691: `for (index, line) in enumerate(lines)`
- L694: `if owner_match and owner_match.group('eoc').upper() != f'{cursor}-EOC'`
- L700: `if re.match(f'^PERFORM\\s+{re.escape(owner)}\\s*$', logical, re.I) and index + 1 < len(lines)`
- L714: `if next_match and next_match.group('eoc').upper() != f'{cursor}-EOC'`

### `ChildFetchEarlyStopCleanup._fetch_name_for_cursor` - L721-L730

```python
_fetch_name_for_cursor(self, lines: list[str], cursor_name: str) -> str
```

Find a declared fetch paragraph for a cursor without assuming its number.

Observed calls (lexical order): `self.cursor_nesting.paragraph_spans`, `f'-FETCH-{cursor_name}'.upper`, `name.endswith`.

Control points:

- L727: `for name in spans`
- L728: `if name.endswith(suffix)`

### `ChildFetchEarlyStopCleanup._fetch_business_flow_stop_flag` - L732-L776

```python
_fetch_business_flow_stop_flag(self, lines: list[str], fetch_paragraph: str) -> str | None
```

Return a uniquely evidenced flag assigned by successful-fetch flow.

Observed calls (lexical order): `self.cursor_nesting.paragraph_spans`, `str`, `str(fetch_paragraph or '').strip`, `str(fetch_paragraph or '').strip().upper`, `spans.get`, `len`, `min`, `range`, `self._logical`, `self._logical(lines[index]).strip`, `self._logical(lines[index]).strip().upper`, `self._logical(lines[index]).strip().upper().rstrip`, `re.match`, `self._perform_target`, `targets.append`, `list`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L739: `if span is None`
- L744: `for index in range(start + 1, min(end + 1, len(lines)))`
- L746: `if re.match('^WHEN\\s+ZERO\\b', statement)`
- L749: `if re.match('^WHEN\\b|^END-EVALUATE\\b', statement)`
- L750: `if in_zero`
- L753: `if in_zero`
- L755: `if target and target in spans`
- L759: `while pending`
- Another 4 conditions/loops exist in this source span.

### `ChildFetchEarlyStopCleanup._perform_target` - L779-L795

```python
_perform_target(logical: str) -> str | None
```

Return a local PERFORM start target, including PERFORM THRU forms.

Observed calls (lexical order): `re.match`, `match.group`, `match.group('target').upper`.

Control points:

- L787: `if not match`
- L791: `if re.match('^\\d+-OPEN-', target)`
- L793: `if re.match('^\\d+-CLOSE-', target)`

### `ChildFetchEarlyStopCleanup._is_child_or_nested_fetch` - L797-L807

```python
_is_child_or_nested_fetch(self, lines: list[str], fetch_paragraph: str) -> bool
```

Identify child cursors by nesting, not generated paragraph numbers.

Observed calls (lexical order): `FETCH_PARAGRAPH_NUMBER_PATTERN.match`, `str`, `str(fetch_paragraph or '').upper`, `self.cursor_nesting.is_nested_fetch`.

Control points:

- L803: `if not FETCH_PARAGRAPH_NUMBER_PATTERN.match(str(fetch_paragraph or '').upper())`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
