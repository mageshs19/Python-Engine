# `patterns/cursor_loop_patterns.py`

Source: [patterns/cursor_loop_patterns.py](../../../patterns/cursor_loop_patterns.py) | 72 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `9c4c3de51e942b7e2676fd2e8381565a7390db18b3acb5cd282590e6f6450385`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for COBOL driving-loop idioms around a generated cursor.

## Module-level bindings

`_NAME` (L14), `PERFORM_SPAN_WITH_UNTIL_PATTERN` (L17), `PERFORM_SPAN_PATTERN` (L24), `PERFORM_INLINE_WITH_UNTIL_PATTERN` (L31), `PERFORM_SIMPLE_PATTERN` (L38), `UNTIL_LINE_PATTERN` (L44), `PERFORM_CURSOR_PARAGRAPH_PATTERN` (L50), `EOC_CONDITION_PATTERN` (L58), `PARAGRAPH_HEADER_PATTERN` (L64), `DIVISION_OR_SECTION_PATTERN` (L69)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_flow/loop_shape.py](../converter/composers/cursor_flow/loop_shape.md)
- [converter/composers/cursor_flow/span_loop_plan.py](../converter/composers/cursor_flow/span_loop_plan.md)
- [converter/composers/cursor_flow/span_loop_rewriter.py](../converter/composers/cursor_flow/span_loop_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
