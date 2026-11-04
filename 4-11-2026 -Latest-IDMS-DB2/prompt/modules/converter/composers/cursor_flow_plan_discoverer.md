# `converter/composers/cursor_flow_plan_discoverer.py`

Source: [converter/composers/cursor_flow_plan_discoverer.py](../../../../converter/composers/cursor_flow_plan_discoverer.py) | 272 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `4f25a7c071c04eb0a4195248c10ad00d6f6a18f449a5a0ab41ea84c1b975cd88`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor flow plan discoverer.

## Import declarations

```python
import re
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from converter.composers.cursor_flow_models import CursorFlowPlan
from patterns.cursor_flow_patterns import PERFORM_BUSINESS_PATTERN, PERFORM_CURSOR_PATTERN, UNTIL_SQLCODE_100_PATTERN, UNTIL_CURSOR_EOC_PATTERN
from rules.cursor_flow_rules import LOOKAHEAD_LIMIT, UNTIL_LOOKAHEAD_LIMIT
```

## Local dependency notes

- [converter/composers/cursor_flow_line_formatter.py](cursor_flow_line_formatter.md)
- [converter/composers/cursor_flow_models.py](cursor_flow_models.md)
- [patterns/cursor_flow_patterns.py](../../patterns/cursor_flow_patterns.md)
- [rules/cursor_flow_rules.py](../../rules/cursor_flow_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_cursor_flow_plan_safety.py](../../tests/test_cursor_flow_plan_safety.md)

## Symbol contracts and control points

### `CursorFlowPlanDiscoverer` - L26-L272

```python
class CursorFlowPlanDiscoverer()
```

### `CursorFlowPlanDiscoverer.__init__` - L27-L32

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `CursorFlowPlanDiscoverer._logical` - L34-L35

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_formatter.logical`.

### `CursorFlowPlanDiscoverer.discover` - L37-L85

```python
discover(self, lines: list[str]) -> list[CursorFlowPlan]
```

Observed calls (lexical order): `len`, `self._logical`, `PERFORM_CURSOR_PATTERN.match`, `open_match.group`, `open_match.group('operation').upper`, `self._build_plan`, `plans.append`, `set`, `range`, `claimed.intersection`, `self.messages.append`, `accepted.append`, `claimed.update`.

Control points:

- L42: `while index < len(lines)`
- L46: `if not open_match`
- L50: `if open_match.group('operation').upper() != 'OPEN'`
- L60: `if plan is None`
- L75: `for plan in plans`
- L77: `if claimed.intersection(span)`

### `CursorFlowPlanDiscoverer._build_plan` - L87-L164

```python
_build_plan(self, lines: list[str], open_index: int, open_match) -> CursorFlowPlan | None
```

Observed calls (lexical order): `open_match.group`, `open_match.group('cursor').upper`, `int`, `self._find_cursor_call`, `self.messages.append`, `self._find_business_loop_after_fetch`, `range`, `self._logical`, `self._logical(lines[pos]).upper`, `re.search`, `PERFORM_CURSOR_PATTERN.match`, `other.group`, `other.group('cursor').upper`, `CursorFlowPlan`.

Control points:

- L98: `if fetch_call is None`
- L110: `if business_info is None`
- L121: `if close_call is None`
- L132: `for pos in range(open_index + 1, close_index)`
- L134: `if re.search('\\b(IF|ELSE|EVALUATE|WHEN|GO\\s+TO|GOTO|END-IF|END-EVALUATE)\\b', logical)`
- L141: `if other and other.group('cursor').upper() != cursor_name`

### `CursorFlowPlanDiscoverer._find_cursor_call` - L166-L196

```python
_find_cursor_call(self, lines: list[str], start_index: int, cursor_name: str, operation: str) -> tuple[int, int] | None
```

Find the first matching operation call and use its actual number.

Observed calls (lexical order): `len`, `min`, `range`, `PERFORM_CURSOR_PATTERN.match`, `self._logical`, `cursor_name.upper`, `match.group`, `match.group('cursor').upper`, `match.group('operation').upper`, `operation.upper`, `found.append`, `int`, `self.messages.append`.

Control points:

- L180: `for index in range(start_index, end_index)`
- L182: `if not match`
- L184: `if match.group('operation').upper() == operation.upper() and match.group('cursor').upper() == cursor_name.upper()`
- L187: `if match.group('cursor').upper() != cursor_name.upper() and match.group('operation').upper() in {'OPEN', 'CLOSE'}`

### `CursorFlowPlanDiscoverer._find_fetch_after_open` - L198-L222

```python
_find_fetch_after_open(self, lines: list[str], start_index: int, cursor_name: str, fetch_number: int) -> int
```

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `PERFORM_CURSOR_PATTERN.match`, `match.group`, `match.group('operation').upper`, `match.group('cursor').upper`, `int`.

Control points:

- L207: `for index in range(start_index, end_index)`
- L211: `if not match`
- L213: `if match.group('operation').upper() != 'FETCH'`
- L215: `if match.group('cursor').upper() != cursor_name`
- L217: `if int(match.group('number')) != fetch_number`

### `CursorFlowPlanDiscoverer._find_business_loop_after_fetch` - L224-L255

```python
_find_business_loop_after_fetch(self, lines: list[str], start_index: int) -> tuple[int, int, str] | None
```

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `logical.startswith`, `PERFORM_CURSOR_PATTERN.match`, `PERFORM_BUSINESS_PATTERN.match`, `business_match.group`, `business_match.group('paragraph').upper`, `self._find_until_sqlcode_100`.

Control points:

- L231: `for index in range(start_index, end_index)`
- L234: `if not logical`
- L236: `if logical.startswith('*') or logical.startswith('/')`
- L238: `if PERFORM_CURSOR_PATTERN.match(logical)`
- L242: `if not business_match`
- L250: `if until_index < 0`

### `CursorFlowPlanDiscoverer._find_until_sqlcode_100` - L257-L272

```python
_find_until_sqlcode_100(self, lines: list[str], start_index: int) -> int
```

Observed calls (lexical order): `len`, `min`, `range`, `self._logical`, `UNTIL_SQLCODE_100_PATTERN.match`, `UNTIL_CURSOR_EOC_PATTERN.match`.

Control points:

- L264: `for index in range(start_index, end_index)`
- L266: `if UNTIL_SQLCODE_100_PATTERN.match(logical) or UNTIL_CURSOR_EOC_PATTERN.match(logical)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
