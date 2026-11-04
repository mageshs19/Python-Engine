# `rules/procedure_indent_rules.py`

Source: [rules/procedure_indent_rules.py](../../../rules/procedure_indent_rules.py) | 205 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b28e97577c8135926f00077ed3bd49beea4c04b21dab6e13d8524aa0901fed69`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Procedure Division indentation rules.

## Module-level bindings

`ENFORCE_PROCEDURE_INDENT` (L34), `AREA_A_INDENT` (L39), `AREA_B_INDENT` (L40), `NEST_STEP` (L41), `WHEN_OFFSET` (L44), `WHEN_BODY_OFFSET` (L45), `SQL_BODY_OFFSET` (L48), `LONE_PERIOD` (L51), `LONE_PERIOD_INDENT` (L52), `MAX_NESTING_DEPTH` (L60), `BLOCK_KIND_IF` (L65), `BLOCK_KIND_EVALUATE` (L66), `BLOCK_KIND_PERFORM` (L67), `BLOCK_KIND_SQL` (L68), `BLOCK_KIND_OTHER` (L69), `SCOPE_TERMINATORS` (L72), `SCOPED_OPENERS` (L91), `NON_PARAGRAPH_SINGLE_WORDS` (L99), `PROCEDURE_INDENT_MESSAGES` (L114), `ENFORCE_AREA_ALIGNMENT_REFLOW` (L132), `PRESERVE_SQL_BODY_INDENT` (L154), `RESPECT_STATEMENT_CONTINUATIONS` (L170), `PRESERVE_INDENT` (L174), `CONTINUATION_OPENERS` (L177), `CONTINUATION_TRAILERS` (L185), `STATEMENT_VERBS` (L193)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/procedure_indent/indent_models.py](../converter/composers/procedure_indent/indent_models.md)
- [converter/composers/procedure_indent/indent_resolver.py](../converter/composers/procedure_indent/indent_resolver.md)
- [converter/composers/procedure_indent_normalizer.py](../converter/composers/procedure_indent_normalizer.md)
- [tests/test_transaction_verb_not_paragraph.py](../tests/test_transaction_verb_not_paragraph.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
