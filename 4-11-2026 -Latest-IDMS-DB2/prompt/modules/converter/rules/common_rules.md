# `converter/rules/common_rules.py`

Source: [converter/rules/common_rules.py](../../../../converter/rules/common_rules.py) | 45 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `674c464290738b728f84b9791be30b26d2c58498728ceea41928a1300cb74c48`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Canonical identifiers and policy constants shared by conversion stages.

## Module-level bindings

`TRANSFORMER_LRF_PATH_EXPANDER` (L9), `TRANSFORMER_LRF_UPDATE_EXPANDER` (L10), `TRANSFORMER_LR_STATUS_REPLACER` (L11), `TRANSFORMER_COBOL` (L12), `TRANSFORMER_FIELD_REFERENCE` (L13), `LABEL_LRF_READ` (L16), `LABEL_LRF_UPDATE` (L17), `LABEL_LR_STATUS` (L18), `METHOD_EXPAND` (L21), `METHOD_APPLY` (L22), `LRF_STAGE_NOT_WIRED_TEMPLATE` (L25), `LRF_STAGE_NO_METHOD_TEMPLATE` (L29), `LRF_STAGE_FAILED_TEMPLATE` (L33), `ENV_ENABLE_LRF_SINGLETON_SHORTCUT` (L40), `DEFAULT_ENABLE_LRF_SINGLETON_SHORTCUT` (L41), `TRUTHY_CONFIG_VALUES` (L42), `DB2_KEEP_MARKER` (L45)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
