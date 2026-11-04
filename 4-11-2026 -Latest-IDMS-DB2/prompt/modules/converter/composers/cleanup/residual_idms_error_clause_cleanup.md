# `converter/composers/cleanup/residual_idms_error_clause_cleanup.py`

Source: [converter/composers/cleanup/residual_idms_error_clause_cleanup.py](../../../../../converter/composers/cleanup/residual_idms_error_clause_cleanup.py) | 88 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `14aba8fa48211a1e14bb376b059317a0f67337397bfc7edc94db0e4fb7932215`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Remove orphaned IDMS ON ANY-ERROR-STATUS clauses after IDMS DML removal.

## Module-level bindings

`_ON_ANY_ERROR` (L18), `_IDMS_STATUS_HANDLER` (L19), `_WARNING` (L20), `__all__` (L88)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [tests/test_residual_idms_error_clause_cleanup.py](../../../tests/test_residual_idms_error_clause_cleanup.md)

## Symbol contracts and control points

### `ResidualIdmsErrorClauseCleanup` - L26-L84

```python
class ResidualIdmsErrorClauseCleanup()
```

### `ResidualIdmsErrorClauseCleanup.__init__` - L27-L33

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `ResidualIdmsErrorClauseCleanup._logical` - L35-L36

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `ResidualIdmsErrorClauseCleanup.apply` - L38-L84

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `len`, `self._logical`, `_ON_ANY_ERROR.fullmatch`, `output.append`, `_WARNING.search`, `output.pop`, `_IDMS_STATUS_HANDLER.fullmatch`, `self.messages.add`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L45: `while index < len(lines)`
- L48: `if not _ON_ANY_ERROR.fullmatch(logical)`
- L56: `if output and _WARNING.search(self._logical(output[-1]))`
- L60: `while next_index < len(lines) and (not self._logical(lines[next_index]))`
- L67: `if _IDMS_STATUS_HANDLER.fullmatch(handler)`
- L80: `if removed`
- L82: `if unrecognized`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
