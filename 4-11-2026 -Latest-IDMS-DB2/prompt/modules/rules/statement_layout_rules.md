# `rules/statement_layout_rules.py`

Source: [rules/statement_layout_rules.py](../../../rules/statement_layout_rules.py) | 112 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `71c90585f99daed227b9212ef92dab79be19dfe0af7ae713024a21f41c607048`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Paragraph separation in the generated PROCEDURE DIVISION.

## Module-level bindings

`ENFORCE_STATEMENT_LAYOUT` (L40), `BLANK_LINE_BEFORE_PARAGRAPH` (L45), `SENTENCE_TERMINATOR` (L50), `NON_PARAGRAPH_WORDS` (L56), `SKIPPABLE_INDICATORS` (L72), `SEPARATOR_INDICATORS` (L76), `SQL_BLOCK_START` (L80), `SQL_BLOCK_END` (L81), `STATEMENT_LAYOUT_MESSAGES` (L86), `PROCEDURE_DIVISION_TOKEN` (L96), `__all__` (L101)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/statement_layout_composer.py](../converter/composers/statement_layout_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
