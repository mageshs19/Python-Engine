# `converter/composers/cursor_close_guarantee/message_log.py`

Source: [converter/composers/cursor_close_guarantee/message_log.py](../../../../../converter/composers/cursor_close_guarantee/message_log.py) | 44 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `578221efb02031e18e136690ba60b4ee7c336041b4aff11f89da5a4cd27d7c69`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared diagnostic collector for the cursor close-guarantee pass.

## Module-level bindings

`__all__` (L44)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_close_guarantee_rules import CURSOR_CLOSE_GUARANTEE_MESSAGES
```

## Local dependency notes

- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)
- [converter/composers/cursor_close_guarantee/business_paragraph_resolver.py](business_paragraph_resolver.md)
- [converter/composers/cursor_close_guarantee/close_guarantor.py](close_guarantor.md)
- [converter/composers/cursor_close_guarantee/condition_normaliser.py](condition_normaliser.md)
- [converter/composers/cursor_close_guarantee/loop_synthesiser.py](loop_synthesiser.md)

## Symbol contracts and control points

### `MessageLog` - L22-L41

```python
class MessageLog()
```

Ordered diagnostic messages for one conversion run.

### `MessageLog.__init__` - L25-L26

```python
__init__(self) -> None
```

### `MessageLog.reset` - L28-L29

```python
reset(self) -> None
```

### `MessageLog.log` - L31-L41

```python
log(self, key: str, **values) -> None
```

Observed calls (lexical order): `CURSOR_CLOSE_GUARANTEE_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L34: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
