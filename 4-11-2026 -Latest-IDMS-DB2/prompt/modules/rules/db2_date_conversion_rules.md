# `rules/db2_date_conversion_rules.py`

Source: [rules/db2_date_conversion_rules.py](../../../rules/db2_date_conversion_rules.py) | 153 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `6accb800ec63bb362544118cd0bedda29fc1d3b388dd1df5187eea5f5ae8d395`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date conversion rules.

## Module-level bindings

`DB2_DATE_COMPARISON_RULES` (L20), `DB2_DATE_COMPARISON_WS_MARKER` (L29), `DB2_DATE_BASE_WORKING_STORAGE_LINES` (L32), `DB2_DATE_HELPER_FIELD_TEMPLATE` (L53), `DB2_DATE_LOW_VALUE_LITERAL` (L58), `DB2_DATE_HIGH_VALUE_LITERAL` (L59), `DB2_DATE_HIGH_NUMERIC_LITERAL` (L60), `DB2_DATE_CONVERSION_LINE_TEMPLATES` (L63), `DB2_DATE_IF_REPLACEMENT_TEMPLATE` (L81), `ENFORCE_DATE_COMPARISON_CONVERSION` (L94), `CONDITION_SCAN_LIMIT` (L97), `MAX_DATE_OPERANDS_PER_CONDITION` (L100), `DB2_DATE_IF_CONDITION_TEMPLATE` (L104), `DB2_DATE_CONVERSION_BANNER_TEMPLATE` (L107), `EMIT_DATE_REFUSAL_COMMENT` (L118), `DB2_DATE_REFUSAL_COMMENT_TEMPLATE` (L120), `DB2_DATE_MESSAGES` (L125)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/db2_date_comparison_composer.py](../converter/composers/db2_date_comparison_composer.md)
- [converter/composers/db2_date_comparison_rewriter.py](../converter/composers/db2_date_comparison_rewriter.md)
- [converter/composers/db2_date_condition_assembler.py](../converter/composers/db2_date_condition_assembler.md)
- [converter/composers/db2_date_working_storage_manager.py](../converter/composers/db2_date_working_storage_manager.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
