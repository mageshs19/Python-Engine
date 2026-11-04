# `rules/idms_transformer_messages.py`

Source: [rules/idms_transformer_messages.py](../../../rules/idms_transformer_messages.py) | 197 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `69795f275ca4ba398ed4751a2c8af006a51211516996a617fa98da4ba7b614c2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`REMOVED_CONTROL_STATEMENT_TEMPLATE` (L29), `REMOVED_BIND_TEMPLATE` (L32), `REMOVED_USAGE_READY_TEMPLATE` (L33), `REMOVED_CONNECT_TEMPLATE` (L34), `REMOVED_DISCONNECT_TEMPLATE` (L35), `REMOVED_STATUS_ABORT_TEMPLATE` (L36), `REMOVED_FIND_CURRENT_TEMPLATE` (L39), `FINISH_OUTSIDE_PROCEDURE_TEMPLATE` (L44), `FINISH_CONVERTED_TO_COMMIT` (L47), `COMMIT_OUTSIDE_PROCEDURE_TEMPLATE` (L48), `FINISH_REMOVED_RETRIEVAL` (L51), `OBTAIN_CALC_OUTSIDE_PROCEDURE_TEMPLATE` (L80), `REMOVED_OBTAIN_CALC_SELECT_TEMPLATE` (L83), `RETRIEVAL_OBTAIN_CALC_RETAINED_TEMPLATE` (L86), `RETRIEVAL_OBTAIN_CALC_RETAINED_DIAGNOSTIC_TEMPLATE` (L89), `CONVERTED_OBTAIN_CALC_TEMPLATE` (L93), `DIRECT_UPDATE_COMPOSITE_KEY` (L94), `LRF_CALC_READ_CONVERTED_TEMPLATE` (L99), `LRF_CALC_READ_NO_SQL_TEMPLATE` (L104), `OBTAIN_OUTSIDE_PROCEDURE_TEMPLATE` (L111), `CONVERTED_OBTAIN_FIRST_TEMPLATE` (L114), `CONVERTED_OBTAIN_NEXT_TEMPLATE` (L117), `FIND_FIRST_OUTSIDE_PROCEDURE_TEMPLATE` (L122), `CONVERTED_FIND_FIRST_TEMPLATE` (L125), `STORE_MODIFY_ERASE_OUTSIDE_PROCEDURE_TEMPLATE` (L130), `PERFORM_OPEN_CURSOR_TEMPLATE` (L135), `PERFORM_FETCH_CURSOR_TEMPLATE` (L136), `OPERATION_STORE` (L139), `OPERATION_MODIFY` (L140), `OPERATION_ERASE` (L141), `REMOVED_REDUNDANT_OBTAIN_NEXT` (L144), `REMOVED_REDUNDANT_SQLCODE_WRAPPER` (L147), `REMOVED_FIELD_LINE_TEMPLATE` (L150), `REMOVED_FIELD_REFUSED_TEMPLATE` (L154), `ERROR_STATUS_MOVE_OWNED_ELSEWHERE` (L158), `TRANSFORMER_MESSAGES` (L165), `LRF_CALC_READ_MARKER_TEMPLATE` (L195)

## Import declarations

```python
from __future__ import annotations
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../converter/pipeline/conversion/conversion_component_factory.md)
- [converter/resolvers/business_paragraph_resolver.py](../converter/resolvers/business_paragraph_resolver.md)
- [converter/transformers/idms_residual_cleanup.py](../converter/transformers/idms_residual_cleanup.md)
- [converter/transformers/idms_statement/control_statement_converter.py](../converter/transformers/idms_statement/control_statement_converter.md)
- [converter/transformers/idms_statement/data_statement_converter.py](../converter/transformers/idms_statement/data_statement_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
