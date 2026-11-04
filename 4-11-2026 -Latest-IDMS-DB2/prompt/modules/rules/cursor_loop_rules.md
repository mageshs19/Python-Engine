# `rules/cursor_loop_rules.py`

Source: [rules/cursor_loop_rules.py](../../../rules/cursor_loop_rules.py) | 150 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `78fb2f24fcda77f20a29a7b37c5f2ffc07ff9f7073ae1acf14598167d39d9934`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor driving-loop rules.

## Module-level bindings

`ENFORCE_SPAN_LOOP_REWRITE` (L75), `REQUIRE_PLAN_FOR_OBTAIN_NEXT_CLEANUP` (L80), `LOOP_KIND_INLINE` (L83), `LOOP_KIND_SPAN` (L84), `SEARCH_BOTH_DIRECTIONS` (L89), `MAX_CORRELATION_DISTANCE` (L92), `CLOSE_PRESENCE_WINDOW` (L95), `UNTIL_TEMPLATE` (L98), `UNTIL_TERMINATED_TEMPLATE` (L99), `PERFORM_CLOSE_TEMPLATE` (L100), `STATEMENT_TERMINATOR` (L102), `CURSOR_LOOP_MESSAGES` (L117)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_eoc_rules import EOC_CONDITION_SUFFIX, EOC_CONDITION_TEMPLATE, LEGACY_EOC_CONDITIONS
```

## Local dependency notes

- [rules/cursor_eoc_rules.py](cursor_eoc_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_flow/loop_shape.py](../converter/composers/cursor_flow/loop_shape.md)
- [converter/composers/cursor_flow/span_loop_plan.py](../converter/composers/cursor_flow/span_loop_plan.md)
- [converter/composers/cursor_flow/span_loop_rewriter.py](../converter/composers/cursor_flow/span_loop_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
