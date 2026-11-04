# `converter/composers/restart/process_paragraph_injector.py`

Source: [converter/composers/restart/process_paragraph_injector.py](../../../../../converter/composers/restart/process_paragraph_injector.py) | 714 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `756974b390404df04b8c4da51e39b983efec4a513b38167ec68aa9544fc4ce33`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Repairs the business processing paragraph of an update program.

## Module-level bindings

`SCOPED_VERBS` (L146), `EXEC_SQL_OPEN` (L148), `EXEC_SQL_CLOSE` (L149), `COMMIT_VERB` (L150), `PERFORM_VERB` (L151), `IF_VERB` (L152), `END_IF` (L153), `PERIOD` (L154), `SQL_LOCATION_TOKEN` (L156), `TAIL_READ_LOOKAHEAD` (L160), `__all__` (L710)

## Import declarations

```python
from __future__ import annotations
from converter.composers.restart.restart_line_utils import RestartLineUtils
from converter.generators.restart.restart_config import RestartConfig
from patterns.restart_patterns import ORPHAN_SCOPE_TERMINATOR_PATTERN
from rules.restart_standard_rules import COMMIT_BLOCK_SCAN_LIMIT, ROLE_COMMIT
from rules.restart_statement_templates import PROCESS_TAIL_TEMPLATE
```

## Local dependency notes

- [converter/composers/restart/restart_line_utils.py](restart_line_utils.md)
- [converter/generators/restart/restart_config.py](../../generators/restart/restart_config.md)
- [patterns/restart_patterns.py](../../../patterns/restart_patterns.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)
- [rules/restart_statement_templates.py](../../../rules/restart_statement_templates.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](restart_injection_composer.md)
- [tests/restart/test_m7_process_injector.py](../../../tests/restart/test_m7_process_injector.md)

## Symbol contracts and control points

### `ProcessParagraphInjector` - L163-L707

```python
class ProcessParagraphInjector()
```

Cleans and completes the business processing paragraph.

### `ProcessParagraphInjector.__init__` - L166-L172

```python
__init__(self, config: RestartConfig, line_utils=None) -> None
```

Observed calls (lexical order): `RestartLineUtils`.

### `ProcessParagraphInjector.inject` - L178-L217

```python
inject(self, lines: list[str]) -> list[str]
```

Return the repaired paragraph body.

Observed calls (lexical order): `self.config.is_usable`, `self.config.missing`, `self.messages.append`, `list`, `self._strip_inline_commit`, `self._strip_emptied_scopes`, `self._strip_orphan_terminators`, `self._strip_redundant_periods`, `self._strip_legacy_commit_test`, `self.tail`, `self._already_injected`, `self._strip_tail_read`.

Control points:

- L182: `if not self.config.is_usable()`
- L183: `for name in self.config.missing()`
- L204: `if self._already_injected(body, tail)`

### `ProcessParagraphInjector.tail` - L219-L222

```python
tail(self) -> tuple[str, ...]
```

The commit test and the tail read, rendered.

Observed calls (lexical order): `self.config.placeholders`, `line.format`, `tuple`.

### `ProcessParagraphInjector._strip_inline_commit` - L228-L291

```python
_strip_inline_commit(self, lines: list[str]) -> list[str]
```

Remove the per-record COMMIT block AND its label.

Observed calls (lexical order): `len`, `self._commit_block_span`, `out.append`, `self._drop_trailing_sql_location`, `self.messages.append`.

Control points:

- L268: `while index < len(lines)`
- L270: `if span is None`
- L278: `if removed`
- L284: `if orphans`

### `ProcessParagraphInjector._drop_trailing_sql_location` - L293-L307

```python
_drop_trailing_sql_location(self, out: list[str]) -> int
```

Drop a SQL-LOCATION label immediately above a removed block.

Observed calls (lexical order): `len`, `range`, `self._logical`, `logical.upper`.

Control points:

- L295: `for position in range(len(out) - 1, -1, -1)`
- L298: `if not logical`
- L301: `if SQL_LOCATION_TOKEN in logical.upper()`

### `ProcessParagraphInjector._commit_block_span` - L309-L335

```python
_commit_block_span(self, lines: list[str], start: int) -> int | None
```

Index after a bare COMMIT block starting at `start`, else None.

Observed calls (lexical order): `self._logical`, `logical.startswith`, `logical.replace`, `logical.replace(PERIOD, ' ').split`, `len`, `min`, `range`, `inner.startswith`, `inner.rstrip`, `statements.append`.

Control points:

- L313: `if not logical.startswith(EXEC_SQL_OPEN)`
- L318: `if EXEC_SQL_CLOSE in tokens`
- L325: `for cursor in range(start + 1, limit)`
- L327: `if not inner`
- L329: `if inner.startswith(EXEC_SQL_CLOSE)`
- L330: `if statements == [COMMIT_VERB]`

### `ProcessParagraphInjector._strip_emptied_scopes` - L341-L379

```python
_strip_emptied_scopes(self, lines: list[str]) -> list[str]
```

Remove an IF / EVALUATE whose body this pass just deleted.

Observed calls (lexical order): `len`, `self._emptied_scope_end`, `out.append`, `self.messages.append`.

Control points:

- L364: `while index < len(lines)`
- L366: `if closer is None`
- L373: `if removed`

### `ProcessParagraphInjector._emptied_scope_end` - L381-L397

```python
_emptied_scope_end(self, lines: list[str], start: int) -> int | None
```

Index of the terminator closing an EMPTY scope at `start`.

Observed calls (lexical order): `self._logical`, `logical.replace`, `logical.replace(PERIOD, ' ').split`, `len`, `range`, `inner.rstrip`.

Control points:

- L385: `if not tokens or tokens[0] not in SCOPED_VERBS`
- L389: `for cursor in range(start + 1, len(lines))`
- L391: `if not inner`
- L393: `if inner.rstrip(PERIOD) == terminator`

### `ProcessParagraphInjector._strip_orphan_terminators` - L403-L437

```python
_strip_orphan_terminators(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._logical`, `ORPHAN_SCOPE_TERMINATOR_PATTERN.match`, `match.group`, `match.group('verb').upper`, `self.messages.append`, `out.append`, `self._track`.

Control points:

- L407: `for line in lines`
- L411: `if match`
- L413: `if verb not in depth`
- L420: `if depth[verb] <= 0`

### `ProcessParagraphInjector._track` - L440-L472

```python
_track(logical: str, depth: dict[str, int]) -> None
```

Count openers only.

Observed calls (lexical order): `logical.rstrip`, `logical.rstrip().endswith`, `logical.split`.

Control points:

- L461: `if logical.rstrip().endswith(PERIOD)`
- L462: `for verb in SCOPED_VERBS`
- L467: `if not tokens`
- L470: `for verb in SCOPED_VERBS`
- L471: `if tokens[0] == verb`

### `ProcessParagraphInjector._strip_redundant_periods` - L478-L512

```python
_strip_redundant_periods(self, lines: list[str]) -> list[str]
```

Remove a lone period after an already-terminated sentence.

Observed calls (lexical order): `self._logical`, `previous.endswith`, `out.append`, `self.messages.append`.

Control points:

- L495: `for line in lines`
- L498: `if logical == PERIOD and previous.endswith(PERIOD)`
- L502: `if logical`
- L506: `if removed`

### `ProcessParagraphInjector._strip_legacy_commit_test` - L518-L565

```python
_strip_legacy_commit_test(self, lines: list[str]) -> list[str]
```

Remove a commit test that carries no tail read.

Observed calls (lexical order): `self._commit_counter_name`, `self._commit_paragraph_name`, `self.messages.append`, `len`, `self._legacy_commit_block_end`, `out.append`, `self._has_tail_read`, `out.extend`.

Control points:

- L532: `if not counter or not commit`
- L543: `while index < len(lines)`
- L546: `if end < 0`
- L551: `if self._has_tail_read(lines, end)`
- L559: `if removed`

### `ProcessParagraphInjector._legacy_commit_block_end` - L567-L608

```python
_legacy_commit_block_end(self, lines: list[str], start: int, counter: str, commit: str) -> int
```

Index of the END-IF closing a commit test at `start`, else -1.

Observed calls (lexical order): `self._logical`, `head.replace`, `head.replace(PERIOD, ' ').split`, `len`, `min`, `range`, `body.rstrip`, `body.startswith`.

Control points:

- L588: `if not tokens or tokens[0] != IF_VERB or counter not in tokens`
- L594: `for cursor in range(start + 1, limit)`
- L596: `if not body`
- L599: `if body.rstrip(PERIOD) == END_IF`
- L602: `if body.startswith(PERFORM_VERB) and commit in body`

### `ProcessParagraphInjector._has_tail_read` - L610-L628

```python
_has_tail_read(self, lines: list[str], end: int) -> bool
```

True when the tail read follows the block closed at `end`.

Observed calls (lexical order): `str`, `str(self.config.names.read_paragraph or '').strip`, `str(self.config.names.read_paragraph or '').strip().upper`, `len`, `range`, `self._logical`, `body.startswith`.

Control points:

- L613: `if not reader`
- L617: `for cursor in range(end + 1, len(lines))`
- L619: `if not body`
- L623: `if seen > TAIL_READ_LOOKAHEAD`

### `ProcessParagraphInjector._commit_counter_name` - L630-L632

```python
_commit_counter_name(self) -> str
```

Observed calls (lexical order): `getattr`, `str`, `str(getattr(names, 'commit_counter', '') or '').strip`, `str(getattr(names, 'commit_counter', '') or '').strip().upper`.

### `ProcessParagraphInjector._commit_paragraph_name` - L634-L641

```python
_commit_paragraph_name(self) -> str
```

Observed calls (lexical order): `getattr`, `callable`, `resolver`, `str`, `str(resolver(ROLE_COMMIT) or '').strip`, `str(resolver(ROLE_COMMIT) or '').strip().upper`.

Control points:

- L636: `if not callable(resolver)`

### `ProcessParagraphInjector._already_injected` - L647-L658

```python
_already_injected(self, body: list[str], tail: tuple[str, ...]) -> bool
```

Observed calls (lexical order): `line.strip`, `self._logical`, `len`.

Control points:

- L656: `if not wanted or len(present) < len(wanted)`

### `ProcessParagraphInjector._strip_tail_read` - L664-L688

```python
_strip_tail_read(self, body: list[str]) -> list[str]
```

Drop a trailing bare PERFORM of the reader.

Observed calls (lexical order): `self._reader_perform`, `len`, `range`, `self._logical`, `logical.rstrip`, `self.messages.append`.

Control points:

- L672: `if not target`
- L675: `for index in range(len(body) - 1, -1, -1)`
- L677: `if not logical`
- L679: `if logical.rstrip(PERIOD) != target`

### `ProcessParagraphInjector._reader_perform` - L690-L692

```python
_reader_perform(self) -> str
```

Observed calls (lexical order): `str`, `str(self.config.names.read_paragraph or '').strip`, `str(self.config.names.read_paragraph or '').strip().upper`.

### `ProcessParagraphInjector._logical` - L698-L707

```python
_logical(self, line: str) -> str
```

Columns 8-72, uppercased, whitespace collapsed.

Observed calls (lexical order): `self.line_utils.logical`, `str`, `self.line_utils.is_comment`, `' '.join`, `body.upper`, `body.upper().split`.

Control points:

- L705: `if self.line_utils.is_comment(body)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
