# `rules/retrieval_commit_cleanup_rules.py`

Source: [rules/retrieval_commit_cleanup_rules.py](../../../rules/retrieval_commit_cleanup_rules.py) | 93 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `77dfe8e5814a63097533a243916278476343b31f841a812ddc69d0cf4526d51d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Retrieval COMMIT cleanup rules.

## Module-level bindings

`ENFORCE_RETRIEVAL_COMMIT_CLEANUP` (L22), `COMMIT_SQL_TOKEN` (L25), `COMMIT_LOCATION_TOKEN` (L26), `EXEC_SQL_TOKEN` (L27), `END_EXEC_TOKEN` (L28), `BLOCK_SCAN_LIMIT` (L31), `COMMIT_REMOVED_COMMENT` (L35), `RETRIEVAL_COMMIT_MESSAGES` (L39), `CURSOR_ORDER_CLEANUP_UNUSED` (L52), `ENFORCE_PARAGRAPH_NOT_EMPTIED` (L55), `CONTINUE_STATEMENT` (L57), `CONTINUE_INDICATOR` (L62), `CONTINUE_INDENT` (L63), `EMPTINESS_SCAN_LIMIT` (L69), `NON_PARAGRAPH_SINGLE_WORDS` (L73)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/retrieval_commit_cleanup_composer.py](../converter/composers/retrieval_commit_cleanup_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
