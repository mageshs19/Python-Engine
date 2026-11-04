# `rules/cursor_flow_rules.py`

Source: [rules/cursor_flow_rules.py](../../../rules/cursor_flow_rules.py) | 47 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `539d982deda2a42e77a6b414e5db74fd210d1157e534b2c3354d4c8ed8163fe3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor flow rule constants.

## Module-level bindings

`LOOKAHEAD_LIMIT` (L11), `UNTIL_LOOKAHEAD_LIMIT` (L14), `NON_PARAGRAPH_DOTTED_LINES` (L17), `NON_PARAGRAPH_HEADER_PREFIXES` (L29), `REMOVED_OBTAIN_NEXT_COMMENT` (L45)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_flow_obtain_next_cleanup.py](../converter/composers/cursor_flow_obtain_next_cleanup.md)
- [converter/composers/cursor_flow_plan_discoverer.py](../converter/composers/cursor_flow_plan_discoverer.md)
- [converter/composers/cursor_flow_rewriter.py](../converter/composers/cursor_flow_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
