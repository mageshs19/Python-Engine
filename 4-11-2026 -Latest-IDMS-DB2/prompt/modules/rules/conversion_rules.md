# `rules/conversion_rules.py`

Source: [rules/conversion_rules.py](../../../rules/conversion_rules.py) | 34 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `044e09bf4a657bbc5b656ced8fe0ea7237f4cd4016fdfdb794095f23f8b6fe32`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> General IDMS to DB2 conversion rules.

## Module-level bindings

`CONVERSION_RULES` (L6), `MISSING_MAPPING_RULES` (L15), `UNMAPPED_RECORD_MARKER_TEMPLATE` (L28), `COMMENTED_IDMS_LINE_PREFIX` (L34)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/idms_statement/transformer_shared_mixin.py](../converter/transformers/idms_statement/transformer_shared_mixin.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
