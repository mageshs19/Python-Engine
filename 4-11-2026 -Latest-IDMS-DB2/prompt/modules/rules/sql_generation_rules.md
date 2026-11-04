# `rules/sql_generation_rules.py`

Source: [rules/sql_generation_rules.py](../../../rules/sql_generation_rules.py) | 42 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `11155326a76d87ea886e191728e386730503c4679d94351f9930216e388e0d14`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQL generation constant tuples.

## Module-level bindings

`SELECT_EXCLUDE_PREFIXES` (L10), `FALLBACK_KEY_PREFIXES` (L17), `DATE_COLUMN_PREFIXES` (L24), `DB2_DATE_NULL_SENTINEL` (L32), `DATE_STAGING_FIELDS` (L38)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/date_move_builder.py](../converter/composers/update_sql_cleanup/date_move_builder.md)
- [converter/generators/sql/sql_date_move_builder.py](../converter/generators/sql/sql_date_move_builder.md)
- [converter/postprocess/update_date_host_converter.py](../converter/postprocess/update_date_host_converter.md)
- [tests/db2_date_sentinel/test_parm_sourced_date_has_no_sentinel.py](../tests/db2_date_sentinel/test_parm_sourced_date_has_no_sentinel.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
