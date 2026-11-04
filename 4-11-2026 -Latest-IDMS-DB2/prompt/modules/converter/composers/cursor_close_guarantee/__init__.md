# `converter/composers/cursor_close_guarantee/__init__.py`

Source: [converter/composers/cursor_close_guarantee/__init__.py](../../../../../converter/composers/cursor_close_guarantee/__init__.py) | 76 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `26037e066cba498cb156063251957c96217f90ba15a2d602d17102a54aa0f4b9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Helpers for the cursor close-guarantee pass.

## Module-level bindings

`__all__` (L57)

## Import declarations

```python
from converter.composers.cursor_close_guarantee.models import UNTIL_KEYWORD, CursorParagraphSet, CursorPerform, LoopShape, ParagraphHeader
from converter.composers.cursor_close_guarantee.message_log import MessageLog
from converter.composers.cursor_close_guarantee.line_utils import COMMENT_INDICATORS, CursorGuaranteeLineUtils
from converter.composers.cursor_close_guarantee.paragraph_index import ParagraphIndex
from converter.composers.cursor_close_guarantee.cursor_scanner import PARAGRAPH_NAME_TEMPLATE, CursorScanner
from converter.composers.cursor_close_guarantee.loop_finder import BusinessLoopFinder
from converter.composers.cursor_close_guarantee.condition_normaliser import ConditionNormaliser
from converter.composers.cursor_close_guarantee.close_guarantor import CloseGuarantor
from converter.composers.cursor_close_guarantee.loop_synthesiser import LoopSynthesiser
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/close_guarantor.py](close_guarantor.md)
- [converter/composers/cursor_close_guarantee/condition_normaliser.py](condition_normaliser.md)
- [converter/composers/cursor_close_guarantee/cursor_scanner.py](cursor_scanner.md)
- [converter/composers/cursor_close_guarantee/line_utils.py](line_utils.md)
- [converter/composers/cursor_close_guarantee/loop_finder.py](loop_finder.md)
- [converter/composers/cursor_close_guarantee/loop_synthesiser.py](loop_synthesiser.md)
- [converter/composers/cursor_close_guarantee/message_log.py](message_log.md)
- [converter/composers/cursor_close_guarantee/models.py](models.md)
- [converter/composers/cursor_close_guarantee/paragraph_index.py](paragraph_index.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
