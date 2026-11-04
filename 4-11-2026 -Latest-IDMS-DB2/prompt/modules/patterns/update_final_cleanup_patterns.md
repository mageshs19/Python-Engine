# `patterns/update_final_cleanup_patterns.py`

Source: [patterns/update_final_cleanup_patterns.py](../../../patterns/update_final_cleanup_patterns.py) | 118 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a0d604a8b4644031df9831bdd4880a274924d794fb6a6424d08264342086af9d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`CONVERTED_MODIFY_COMMENT_PATTERN` (L11), `UPDATE_PARAGRAPH_PATTERN` (L16), `PARAGRAPH_HEADER_PATTERN` (L21), `EXEC_SQL_PATTERN` (L26), `END_EXEC_PATTERN` (L31), `EVALUATE_SQLCODE_PATTERN` (L36), `END_EVALUATE_PATTERN` (L41), `WHEN_PATTERN` (L46), `PROCESS_COMMIT_IF_PATTERN` (L51), `PERFORM_PATTERN` (L56), `STOP_RUN_PATTERN` (L61), `NON_SQL_DCL_DOT_REFERENCE_PATTERN` (L67), `MOVE_SPACES_TO_BARE_RECORD_PATTERN` (L72), `INITIALIZE_DCL_PATTERN` (L77), `DCL_REFERENCE_PATTERN` (L82), `MOVE_TO_DCL_DOT_REFERENCE_PATTERN` (L99), `TO_DCL_DOT_REFERENCE_PATTERN` (L108), `NON_SQL_DCL_DOT_REFERENCE_STRICT_PATTERN` (L115)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/final_cleanup/final_cleanup_dcl_reference.py](../converter/postprocess/final_cleanup/final_cleanup_dcl_reference.md)
- [converter/postprocess/final_cleanup/final_cleanup_line_utils.py](../converter/postprocess/final_cleanup/final_cleanup_line_utils.md)
- [converter/postprocess/final_cleanup/final_cleanup_normalizer.py](../converter/postprocess/final_cleanup/final_cleanup_normalizer.md)
- [converter/postprocess/update_final_cleanup.py](../converter/postprocess/update_final_cleanup.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
