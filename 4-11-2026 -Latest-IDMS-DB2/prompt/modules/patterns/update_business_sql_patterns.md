# `patterns/update_business_sql_patterns.py`

Source: [patterns/update_business_sql_patterns.py](../../../patterns/update_business_sql_patterns.py) | 81 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `2ec33813869d5ef1ec9bda80794b07c06a4d1a284e6cb908985a9454eeb84471`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`CONVERTED_MODIFY_COMMENT_PATTERN` (L13), `SQL_LOCATION_UPDATE_PATTERN` (L18), `EXEC_SQL_START_PATTERN` (L23), `EXEC_SQL_UPDATE_PATTERN` (L28), `END_EXEC_PATTERN` (L33), `EVALUATE_SQLCODE_PATTERN` (L38), `WHEN_ZERO_PATTERN` (L43), `WHEN_OTHER_PATTERN` (L48), `CONTINUE_PATTERN` (L53), `END_EVALUATE_PATTERN` (L58), `DCL_HOST_GROUP_PATTERN` (L63), `PERFORM_UPDATE_PARAGRAPH_PATTERN` (L68), `PERFORM_READ_FLAT_FILE_PATTERN` (L73), `PARAGRAPH_HEADER_PATTERN` (L78)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_business_sql/update_paragraph_normalizer.py](../converter/postprocess/update_business_sql/update_paragraph_normalizer.md)
- [converter/postprocess/update_business_sql/update_sql_block_extractor.py](../converter/postprocess/update_business_sql/update_sql_block_extractor.md)
- [converter/postprocess/update_business_sql_standardizer.py](../converter/postprocess/update_business_sql_standardizer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
