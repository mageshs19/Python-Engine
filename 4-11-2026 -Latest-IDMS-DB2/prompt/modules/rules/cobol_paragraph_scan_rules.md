# `rules/cobol_paragraph_scan_rules.py`

Source: [rules/cobol_paragraph_scan_rules.py](../../../rules/cobol_paragraph_scan_rules.py) | 53 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `58c3861f55288cdd5145e9369050038b94f806fc4b250252131bc1907111550b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Constants for resolving the paragraph a statement sits inside.

## Module-level bindings

`NON_PARAGRAPH_SENTENCE_WORDS` (L33), `PARAGRAPH_SCAN_LIMIT` (L48), `__all__` (L50)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](../converter/composers/update_sql_cleanup/modify_update_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
