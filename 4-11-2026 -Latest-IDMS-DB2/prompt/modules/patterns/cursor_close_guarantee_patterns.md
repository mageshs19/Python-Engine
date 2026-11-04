# `patterns/cursor_close_guarantee_patterns.py`

Source: [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.py) | 133 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `3267d69ea9b8ed5f1e4f23893b4594ea40e23fd6cf9e7dccc6ac4558f2406c08`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for the cursor close-guarantee pass.

## Module-level bindings

`_NAME` (L31), `PARAGRAPH_HEADER_PATTERN` (L34), `SECTION_HEADER_PATTERN` (L39), `CURSOR_PARAGRAPH_HEADER_PATTERN` (L45), `PERFORM_CURSOR_PARAGRAPH_PATTERN` (L58), `PERFORM_PARAGRAPH_PATTERN` (L66), `PERFORM_INLINE_WITH_UNTIL_PATTERN` (L71), `PERFORM_SPAN_PATTERN` (L77), `PERFORM_SPAN_WITH_UNTIL_PATTERN` (L83), `UNTIL_ONLY_PATTERN` (L90), `WHEN_ZERO_PATTERN` (L96), `CONTINUE_PATTERN` (L101), `ANY_WHEN_PATTERN` (L111), `END_EVALUATE_PATTERN` (L117), `PERFORM_PLAIN_PATTERN` (L124), `HOST_GROUP_REFERENCE_PATTERN` (L130)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/business_paragraph_resolver.py](../converter/composers/cursor_close_guarantee/business_paragraph_resolver.md)
- [converter/composers/cursor_close_guarantee/cursor_scanner.py](../converter/composers/cursor_close_guarantee/cursor_scanner.md)
- [converter/composers/cursor_close_guarantee/line_utils.py](../converter/composers/cursor_close_guarantee/line_utils.md)
- [converter/composers/cursor_close_guarantee/loop_finder.py](../converter/composers/cursor_close_guarantee/loop_finder.md)
- [converter/composers/cursor_close_guarantee/loop_synthesiser.py](../converter/composers/cursor_close_guarantee/loop_synthesiser.md)
- [converter/composers/cursor_close_guarantee/paragraph_index.py](../converter/composers/cursor_close_guarantee/paragraph_index.md)
- [converter/composers/cursor_guarantee/cursor_repair.py](../converter/composers/cursor_guarantee/cursor_repair.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
