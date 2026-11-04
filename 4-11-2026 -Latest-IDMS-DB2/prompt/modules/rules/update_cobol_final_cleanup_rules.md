# `rules/update_cobol_final_cleanup_rules.py`

Source: [rules/update_cobol_final_cleanup_rules.py](../../../rules/update_cobol_final_cleanup_rules.py) | 112 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `12b1c333911e4402cef8563e93b7bd0d36b787c0052ec36ccbcde4dc9cd7e535`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`UPDATE_FINAL_CLEANUP_RULES` (L12), `UPDATE_FINAL_LOOKAHEAD_LIMIT` (L24), `UPDATE_FINAL_LOOKBACK_DUPLICATE_LIMIT` (L25), `PROTECTED_BARE_TARGET_PREFIXES` (L28), `TIMESTAMP_AUDIT_PREFIXES` (L50), `USER_AUDIT_PREFIXES` (L55), `AUDIT_SOURCE_BY_KIND` (L63), `FINAL_CLEANUP_BODY_WIDTH` (L71), `FINAL_CLEANUP_SEQUENCE_WIDTH` (L72), `FINAL_CLEANUP_INDICATOR_COLUMN` (L73), `FINAL_CLEANUP_BODY_START` (L74), `FINAL_CLEANUP_BODY_END` (L75), `FINAL_CLEANUP_FULL_WIDTH` (L76), `FINAL_CLEANUP_TOTAL_WIDTH` (L77), `FINAL_CLEANUP_RIGHT_SEQUENCE_WIDTH` (L78), `FINAL_CLEANUP_AREA_B` (L81), `FINAL_CLEANUP_SQL_BODY` (L82), `FINAL_CLEANUP_WHEN_INDENT` (L83), `FINAL_CLEANUP_ACTION_INDENT` (L84), `FINAL_CLEANUP_COMMENT_INDICATORS` (L87), `FINAL_CLEANUP_COMMENT_CHARS` (L88), `FINAL_CLEANUP_DEBUG_PREFIX` (L89), `FINAL_CLEANUP_TOKEN_MOVE` (L92), `FINAL_CLEANUP_TOKEN_TO` (L93), `FINAL_CLEANUP_TOKEN_EXEC_SQL` (L94), `FINAL_CLEANUP_TOKEN_END_EXEC` (L95), `FINAL_CLEANUP_TOKEN_EVALUATE_SQLCODE` (L96), `FINAL_CLEANUP_TOKEN_END_EVALUATE` (L97), `FINAL_CLEANUP_TOKEN_END_IF` (L98), `FINAL_CLEANUP_TOKEN_STOP_RUN` (L99), `FINAL_CLEANUP_TOKEN_END_IF_DOT` (L100), `FINAL_CLEANUP_TOKEN_PROCEDURE_DIVISION` (L101), `FINAL_CLEANUP_DCL_PREFIX` (L102), `FINAL_CLEANUP_LONE_PERIOD` (L103), `FINAL_CLEANUP_DOT` (L104), `FINAL_CLEANUP_MOVE_TEMPLATE` (L107), `FINAL_CLEANUP_FIELD_OF_GROUP_TEMPLATE` (L108), `FINAL_CLEANUP_TO_FIELD_OF_GROUP_TEMPLATE` (L109), `FINAL_CLEANUP_MAX_CONSECUTIVE_BLANKS` (L112)

## Import declarations

```python
from __future__ import annotations
```

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/final_cleanup/final_cleanup_dcl_reference.py](../converter/postprocess/final_cleanup/final_cleanup_dcl_reference.md)
- [converter/postprocess/final_cleanup/final_cleanup_line_utils.py](../converter/postprocess/final_cleanup/final_cleanup_line_utils.md)
- [converter/postprocess/final_cleanup/final_cleanup_normalizer.py](../converter/postprocess/final_cleanup/final_cleanup_normalizer.md)
- [converter/postprocess/update_final_cleanup.py](../converter/postprocess/update_final_cleanup.md)
- [converter/services/update_audit_move_inserter.py](../converter/services/update_audit_move_inserter.md)
- [converter/services/update_cobol_final_cleanup_utils.py](../converter/services/update_cobol_final_cleanup_utils.md)
- [converter/services/update_cobol_reference_cleanup.py](../converter/services/update_cobol_reference_cleanup.md)
- [converter/services/update_diagnostic_label_normalizer.py](../converter/services/update_diagnostic_label_normalizer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
