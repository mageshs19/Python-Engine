# `converter/composers/cursor_guarantee/__init__.py`

Source: [converter/composers/cursor_guarantee/__init__.py](../../../../../converter/composers/cursor_guarantee/__init__.py) | 47 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `627f5c017ee3a3777c6a2cf08c66ab30c50962a6a71e0babd7964d94ab2686c5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Helpers for the cursor close-guarantee pass.

## Module-level bindings

`__all__` (L35)

## Import declarations

```python
from converter.composers.cursor_guarantee.cursor_models import COMMENT_INDICATORS, PARAGRAPH_NAME_TEMPLATE, UNTIL_KEYWORD, CursorParagraphSet, CursorPerform, LoopShape, MessageLog, ParagraphHeader
from converter.composers.cursor_guarantee.cursor_lines import CursorLines
from converter.composers.cursor_guarantee.cursor_scanner import CursorScanner
from converter.composers.cursor_guarantee.cursor_repair import CursorRepair
```

## Local dependency notes

- [converter/composers/cursor_guarantee/cursor_lines.py](cursor_lines.md)
- [converter/composers/cursor_guarantee/cursor_models.py](cursor_models.md)
- [converter/composers/cursor_guarantee/cursor_repair.py](cursor_repair.md)
- [converter/composers/cursor_guarantee/cursor_scanner.py](cursor_scanner.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
