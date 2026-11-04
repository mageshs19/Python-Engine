# `converter/composers/update_sql_cleanup/composer_patterns.py`

Source: [converter/composers/update_sql_cleanup/composer_patterns.py](../../../../../converter/composers/update_sql_cleanup/composer_patterns.py) | 40 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `e7e68817a17101b83f4c425b44d5c3bbaf88024179887ff5f7a588120643915e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex patterns used only by the update SQL cleanup composer passes.

## Module-level bindings

`MOVE_TO_DCL_DOT_HOST_PATTERN` (L12), `STRING_INTO_DCL_HOST_PATTERN` (L17), `STRING_INTO_DCL_DOT_HOST_PATTERN` (L22), `ANY_DCL_OF_REFERENCE_PATTERN` (L27), `ANY_DCL_DOT_REFERENCE_PATTERN` (L32), `DATE_COLUMN_PREFIXES` (L37)

## Import declarations

```python
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](modify_update_rewriter.md)
- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
