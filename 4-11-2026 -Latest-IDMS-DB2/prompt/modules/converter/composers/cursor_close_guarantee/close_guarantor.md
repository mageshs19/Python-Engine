# `converter/composers/cursor_close_guarantee/close_guarantor.py`

Source: [converter/composers/cursor_close_guarantee/close_guarantor.py](../../../../../converter/composers/cursor_close_guarantee/close_guarantor.py) | 70 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `65a2cbf25699ace958db997acba0ff7140bb4562edc1f3acb9eb7b9cf00e1b5e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Guarantees that a generated CLOSE paragraph is actually performed.

## Module-level bindings

`__all__` (L70)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_close_guarantee.line_utils import CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.message_log import MessageLog
from converter.composers.cursor_close_guarantee.models import CursorParagraphSet, CursorPerform
from rules.cursor_close_guarantee_rules import PERFORM_CLOSE_TEMPLATE
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

### `CloseGuarantor` - L27-L67

```python
class CloseGuarantor()
```

Inserts the missing PERFORM of a cursor CLOSE paragraph.

### `CloseGuarantor.__init__` - L30-L36

```python
__init__(self, line_utils: CursorGuaranteeLineUtils | None=None, log: MessageLog | None=None) -> None
```

Observed calls (lexical order): `CursorGuaranteeLineUtils`, `MessageLog`.

### `CloseGuarantor.guarantee` - L38-L67

```python
guarantee(self, lines: list[str], after_index: int, cursor_set: CursorParagraphSet, close_performs: list[CursorPerform]) -> list[str]
```

Insert PERFORM <close>. after `after_index` when it is absent.

Observed calls (lexical order): `self.log.log`, `len`, `self.lines_utils.format_like`, `PERFORM_CLOSE_TEMPLATE.format`, `list`, `output.insert`.

Control points:

- L46: `if close_performs`
- L50: `if not 0 <= after_index < len(lines)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
