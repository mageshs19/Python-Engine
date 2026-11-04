# `rules/sqlcode_wrapper_rules.py`

Source: [rules/sqlcode_wrapper_rules.py](../../../rules/sqlcode_wrapper_rules.py) | 56 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `894a18e27f6b9511bffcee6f78a48f38096fd52805534421b679d48e0b4917cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`OUTER_IF_TEXT` (L7), `INNER_IF_TEXT` (L8), `REMOVED_OBTAIN_NEXT_TEXT` (L9), `CLEANUP_COMMENT_TEXT` (L12), `TOKEN_IF` (L17), `TOKEN_END_IF` (L18), `TOKEN_MOVE` (L19), `TOKEN_TO` (L20), `TOKEN_OF_DCL` (L21), `DB2_COMMENT_PREFIX` (L22), `COMMENT_INDICATOR` (L23), `PAGE_INDICATOR` (L24), `BASE_INDENT` (L27), `CHILD_INDENT` (L28), `CONTINUATION_INDENT` (L29), `BODY_WIDTH` (L30), `FULL_LINE_WIDTH` (L31), `SEQUENCE_AREA_WIDTH` (L32), `INDICATOR_COLUMN` (L33), `BODY_START_COLUMN` (L34), `BODY_END_COLUMN` (L35), `RIGHT_SEQUENCE_START` (L36), `RIGHT_SEQUENCE_END` (L37), `MARKER_LOOKAHEAD` (L40), `INNER_IF_LOOKAHEAD` (L41), `COMMENT_PREFIXES` (L44), `PERIOD` (L51), `DIAG_PERIOD_RESTORED` (L53)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/sqlcode_wrapper_cleanup_composer.py](../converter/composers/sqlcode_wrapper_cleanup_composer.md)
- [converter/composers/sqlcode_wrapper_line_utils.py](../converter/composers/sqlcode_wrapper_line_utils.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
