# `converter/composers/cursor_close_guarantee/condition_normaliser.py`

Source: [converter/composers/cursor_close_guarantee/condition_normaliser.py](../../../../../converter/composers/cursor_close_guarantee/condition_normaliser.py) | 148 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `8e823f7b3f6fac92572c583393489f3230b00eb06eabfbda93e390fba86c80e6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Rewrites a legacy loop exit test to the cursor end-of-cursor flag.

## Module-level bindings

`__all__` (L148)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.line_utils import CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.message_log import MessageLog
from converter.composers.cursor_close_guarantee.models import LoopShape
from rules.cursor_close_guarantee_rules import STATEMENT_TERMINATOR, UNTIL_TEMPLATE
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/line_utils.py](line_utils.md)
- [converter/composers/cursor_close_guarantee/message_log.py](message_log.md)
- [converter/composers/cursor_close_guarantee/models.py](models.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)

## Symbol contracts and control points

### `ConditionNormaliser` - L29-L145

```python
class ConditionNormaliser()
```

Normalises loop exit conditions onto the cursor EOC flag.

### `ConditionNormaliser.__init__` - L32-L38

```python
__init__(self, line_utils: CursorGuaranteeLineUtils | None=None, log: MessageLog | None=None) -> None
```

Observed calls (lexical order): `CursorGuaranteeLineUtils`, `MessageLog`.

### `ConditionNormaliser.normalise_perform_line` - L43-L73

```python
normalise_perform_line(self, lines: list[str], index: int, condition: str, cursor: str) -> list[str]
```

Observed calls (lexical order): `len`, `self.lines_utils.logical`, `self.lines_utils.partition_until`, `tail.rstrip`, `tail.rstrip(STATEMENT_TERMINATOR).strip`, `self._needs_rewrite`, `UNTIL_TEMPLATE.format`, `head.rstrip`, `self._write`, `self.lines_utils.is_terminated`.

Control points:

- L50: `if not 0 <= index < len(lines)`
- L56: `if not keyword or not tail`
- L61: `if not self._needs_rewrite(current, condition)`

### `ConditionNormaliser.normalise_loop` - L78-L111

```python
normalise_loop(self, lines: list[str], loop: LoopShape, condition: str, cursor: str) -> list[str]
```

Observed calls (lexical order): `len`, `self._needs_rewrite`, `self.lines_utils.logical`, `self.lines_utils.is_until_only`, `UNTIL_TEMPLATE.format`, `self.lines_utils.partition_until`, `head.rstrip`, `self._write`.

Control points:

- L87: `if not 0 <= index < len(lines)`
- L90: `if not self._needs_rewrite(loop.condition, condition)`
- L95: `if self.lines_utils.is_until_only(logical)`

### `ConditionNormaliser._needs_rewrite` - L116-L123

```python
_needs_rewrite(self, current: str, condition: str) -> bool
```

Only a recognised legacy test is ever rewritten.

Observed calls (lexical order): `self.lines_utils.compress`, `self.lines_utils.is_legacy_condition`.

Control points:

- L118: `if self.lines_utils.compress(current) == self.lines_utils.compress(condition)`

### `ConditionNormaliser._write` - L125-L145

```python
_write(self, lines: list[str], index: int, body: str, terminated: bool, cursor: str, condition: str) -> list[str]
```

Observed calls (lexical order): `list`, `self.lines_utils.format_like`, `self.log.log`.

Control points:

- L134: `if terminated`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
