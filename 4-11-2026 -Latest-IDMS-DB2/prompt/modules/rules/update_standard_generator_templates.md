# `rules/update_standard_generator_templates.py`

Source: [rules/update_standard_generator_templates.py](../../../rules/update_standard_generator_templates.py) | 297 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `341d6e403fc4ddd52abb73e54a4a92ea7c8d62cd6b0f15797bc4e50fb72de542`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`RESTART_LENGTH_BASE` (L19), `EOF_NOT_SET_VALUE` (L20), `EOF_SET_VALUE` (L21), `COMMIT_COUNTER_RESET_VALUE` (L22), `CS_PROGRAM_FIELD` (L25), `DA_DD_MM_CCYY_FIELD` (L26), `COMMIT_COUNTER_LEGACY` (L27), `SQL_ERROR_PARAGRAPH` (L28), `SQL_LOCATION_FIELD` (L29), `ABEND_CALL_STATEMENT` (L30), `DISPLAY_PREVIOUS_RUN_COMPLETE` (L33), `DISPLAY_ERROR_REC_TEMPLATE` (L34), `COPYBOOK_INCLUDE_TEMPLATE` (L37), `DCLGEN_INCLUDE_TEMPLATE` (L38), `WORKING_STORAGE_TEMPLATE` (L45), `READ_FLAT_FILE_TEMPLATE` (L63), `RESTART_CONTROL_TEMPLATE` (L79), `RESTART_FOUND_TEMPLATE` (L108), `WRITE_RESTART_TEMPLATE` (L125), `PROCESS_COMMIT_TEMPLATE` (L150), `RESTART_SQL_TEMPLATE` (L195), `SQLERROR_PARAGRAPH_TEMPLATE` (L281), `USE_SHARED_SQL_ERROR_GENERATOR` (L289), `SQL_ERROR_INCLUDE_TOKEN` (L292), `MSG_SQLERROR_INJECTED` (L294), `MSG_SQLERROR_FROM_COPYBOOK` (L295)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/cobol_update_standard_generator.py](../converter/postprocess/cobol_update_standard_generator.md)
- [converter/postprocess/update_storage_include_manager.py](../converter/postprocess/update_storage_include_manager.md)
- [tests/restart/test_m5b_restart_found_nesting.py](../tests/restart/test_m5b_restart_found_nesting.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
