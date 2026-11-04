# `rules/db2_output_date_conversion_rules.py`

Source: [rules/db2_output_date_conversion_rules.py](../../../rules/db2_output_date_conversion_rules.py) | 55 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `e9033186592fd1b255dd109078ff39c1d9a7670e9e0ef2a79b2bb994061e58cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 output date conversion rules.

## Module-level bindings

`DB2_OUTPUT_DATE_CONVERSION_RULES` (L24), `DB2_OUTPUT_DATE_LOW_VALUE_LITERAL` (L33), `DB2_OUTPUT_DATE_HIGH_VALUE_LITERAL` (L34), `DB2_OUTPUT_DATE_HIGH_NUMERIC_LITERAL` (L35), `DB2_OUTPUT_DATE_CONVERSION_LINE_TEMPLATES` (L37), `EMIT_OUTPUT_FIELD_BLANKING_MOVE` (L54), `OUTPUT_FIELD_BLANKING_LITERAL` (L55)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/db2_date_output_cleanup.py](../converter/composers/cleanup/db2_date_output_cleanup.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
