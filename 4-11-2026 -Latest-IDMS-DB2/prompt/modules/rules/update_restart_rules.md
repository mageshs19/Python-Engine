# `rules/update_restart_rules.py`

Source: [rules/update_restart_rules.py](../../../rules/update_restart_rules.py) | 339 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `4d8a9b5466c4ff7a49995ac346617b1f66d460b1414cc596412b53c2ea18d42b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`UPDATE_RESTART_RULES` (L12), `RESTART_PARAGRAPH_NAMES` (L26), `RESTART_STATUS_INCOMPLETE` (L37), `RESTART_STATUS_COMPLETE` (L38), `RESTART_DEFAULT_PHASE` (L39), `RESTART_RETENTION_DAYS` (L40), `RESTART_DCLGEN_MIN_SCORE` (L43), `RESTART_DCLGEN_ROLE_TOKENS` (L45), `RESTART_VARCHAR_SUFFIXES` (L64), `UPDATE_RESTART_WS_NAMES` (L69), `UPDATE_LEGACY_RESTART_WS_NAMES` (L82), `UPDATE_STANDARD_DATE_WS_LINES` (L89), `UPDATE_MAIN_DATE_INITIALIZATION_LINES` (L117), `UPDATE_SUMMARY_DISPLAY_TEMPLATES` (L123), `UPDATE_SQL_PARAGRAPH_PREFIX` (L128), `UPDATE_COMMIT_THRESHOLD` (L129), `UPDATE_RESTART_DIAGNOSTICS` (L131), `__all__` (L179), `MAIN_FLOW_FIXED_BODY_WIDTH` (L202), `MAIN_FLOW_SEQUENCE_WIDTH` (L203), `MAIN_FLOW_INDICATOR_COLUMN` (L204), `MAIN_FLOW_BODY_START` (L205), `MAIN_FLOW_BODY_END` (L206), `MAIN_FLOW_FULL_WIDTH` (L207), `MAIN_FLOW_TOTAL_WIDTH` (L208), `MAIN_FLOW_RIGHT_SEQUENCE_WIDTH` (L209), `MAIN_FLOW_AREA_B_INDENT` (L210), `MAIN_FLOW_COMMENT_INDICATORS` (L211), `MAIN_FLOW_READ_FLAT_FILE_PARAGRAPH` (L214), `MAIN_FLOW_TOKEN_CLOSE` (L215), `MAIN_FLOW_LONE_PERIOD` (L216), `MAIN_FLOW_PERFORM_READ_BODY` (L219), `MAIN_FLOW_PERFORM_READ_BODY_DOT` (L220), `MAIN_FLOW_SET_NOT_EOF_TEMPLATE` (L221), `MAIN_FLOW_INITIALIZE_HELP_TEMPLATE` (L222), `MAIN_FLOW_RESTART_TEMPLATE_LINES` (L225), `MAIN_FLOW_LEGACY_RESTART_TOKENS` (L239), `MAIN_FLOW_RESTART_PARAGRAPH_PREFIXES` (L251), `MAIN_FLOW_OPEN_LOOKBACK` (L261), `MAIN_FLOW_CLOSE_LOOKBACK` (L262), `MAIN_FLOW_DIAGNOSTICS` (L265), `RESTART_ROLE_COLUMN_FIELD_SPEC` (L309), `RESTART_PAYLOAD_TOKEN_KEY` (L318), `RESTART_PAYLOAD_FALLBACK_TOKEN_KEY` (L319), `RESTART_PAYLOAD_LENGTH_SPEC` (L322), `RESTART_PAYLOAD_TEXT_SPEC` (L327), `LEGACY_ABEND_MARKER_LITERAL_PREFIX` (L332), `USE_SHARED_SQL_ERROR_GENERATOR` (L335), `SQLERROR_PARAGRAPH_TEMPLATE` (L338)

## Import declarations

```python
from __future__ import annotations
```

## Importers (17)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline_steps.py](../converter/pipeline/conversion/conversion_pipeline_steps.md)
- [converter/postprocess/cobol_update_standard_generator.py](../converter/postprocess/cobol_update_standard_generator.md)
- [converter/postprocess/main_flow/main_flow_line_utils.py](../converter/postprocess/main_flow/main_flow_line_utils.md)
- [converter/postprocess/main_flow/main_flow_locators.py](../converter/postprocess/main_flow/main_flow_locators.md)
- [converter/postprocess/main_flow/main_flow_paragraph_resolver.py](../converter/postprocess/main_flow/main_flow_paragraph_resolver.md)
- [converter/postprocess/restart_role/restart_role_field_resolver.py](../converter/postprocess/restart_role/restart_role_field_resolver.md)
- [converter/postprocess/storage_include/storage_include_injector.py](../converter/postprocess/storage_include/storage_include_injector.md)
- [converter/postprocess/storage_include/storage_ws_injector.py](../converter/postprocess/storage_include/storage_ws_injector.md)
- [converter/postprocess/update_business_sql/update_counter_declarer.py](../converter/postprocess/update_business_sql/update_counter_declarer.md)
- [converter/postprocess/update_business_sql/update_paragraph_normalizer.py](../converter/postprocess/update_business_sql/update_paragraph_normalizer.md)
- [converter/postprocess/update_business_sql/update_sql_block_extractor.py](../converter/postprocess/update_business_sql/update_sql_block_extractor.md)
- [converter/postprocess/update_business_sql_standardizer.py](../converter/postprocess/update_business_sql_standardizer.md)
- 5 further importers are recorded in [the source manifest](../../source_manifest.json).

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
