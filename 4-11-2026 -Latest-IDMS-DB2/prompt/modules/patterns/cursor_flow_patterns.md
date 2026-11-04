# `patterns/cursor_flow_patterns.py`

Source: [patterns/cursor_flow_patterns.py](../../../patterns/cursor_flow_patterns.py) | 75 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `0ff0bbd578006825ef0241bb0c08695da97b4887d8445b28bf5c824ba189b40a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor flow regex patterns.

## Module-level bindings

`PERFORM_CURSOR_PATTERN` (L10), `PERFORM_BUSINESS_PATTERN` (L19), `_LEGACY_EOC_ALTERNATION` (L26), `UNTIL_LEGACY_EOC_PATTERN` (L31), `UNTIL_SQLCODE_100_PATTERN` (L37), `UNTIL_CURSOR_EOC_PATTERN` (L38), `CURSOR_PARAGRAPH_HEADER_PATTERN` (L43), `ANY_PARAGRAPH_HEADER_PATTERN` (L52), `WHEN_ZERO_PATTERN` (L57), `CONTINUE_PATTERN` (L62), `CONVERTED_OBTAIN_NEXT_COMMENT_PATTERN` (L67), `CONVERTED_OBTAIN_COMMENT_PATTERN` (L72)

## Import declarations

```python
import re
from rules.cursor_eoc_rules import LEGACY_EOC_CONDITIONS
```

## Local dependency notes

- [rules/cursor_eoc_rules.py](../rules/cursor_eoc_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_flow_obtain_next_cleanup.py](../converter/composers/cursor_flow_obtain_next_cleanup.md)
- [converter/composers/cursor_flow_plan_discoverer.py](../converter/composers/cursor_flow_plan_discoverer.md)
- [converter/composers/cursor_flow_rewriter.py](../converter/composers/cursor_flow_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
