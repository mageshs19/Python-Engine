# `rules/move_alignment_rules.py`

Source: [rules/move_alignment_rules.py](../../../rules/move_alignment_rules.py) | 151 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `0e41cd2a9b4a745fdee836f9f9d31b6fd48ac19ac24d4e91fb75792eed183093`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Column alignment for runs of MOVE statements.

## Module-level bindings

`ENFORCE_MOVE_ALIGNMENT` (L31), `MIN_RUN_SIZE` (L37), `BLANK_LINE_BREAKS_RUN` (L42), `MULTI_RECEIVER_STANDS_ALONE` (L48), `MIN_GAP_BEFORE_TO` (L55), `MAX_ALIGN_PADDING` (L69), `RECEIVER_OFFSET` (L73), `VERB_MOVE` (L78), `TOKEN_TO` (L79), `SENTENCE_TERMINATOR` (L80), `QUOTE_CHARACTERS` (L82), `STATEMENT_OPENERS` (L86), `SKIPPABLE_INDICATORS` (L98), `SQL_BLOCK_START` (L102), `SQL_BLOCK_END` (L103), `MOVE_ALIGNMENT_MESSAGES` (L108), `__all__` (L134)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/lrf_group_move_decomposer.py](../converter/composers/lrf_group_move_decomposer.md)
- [converter/composers/move_alignment_composer.py](../converter/composers/move_alignment_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
