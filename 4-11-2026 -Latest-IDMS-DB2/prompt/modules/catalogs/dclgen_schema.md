# `catalogs/dclgen_schema.py`

Source: [catalogs/dclgen_schema.py](../../../catalogs/dclgen_schema.py) | 28 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a3bac6e0e828b7306dd6b769bb753c127fde7b4e17fd414e83479568f8c2f42a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DCLGEN schema catalog.

## Module-level bindings

`DCLGEN_GROUP_PREFIX` (L10), `DCLGEN_COLUMN_FIELDS` (L13), `DCLGEN_HOST_FIELD_SUFFIXES_TO_IGNORE` (L24)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/dclgen/dclgen_column_merger.py](../converter/parsers/dclgen/dclgen_column_merger.md)
- [converter/postprocess/update_restart_dclgen_role_builder.py](../converter/postprocess/update_restart_dclgen_role_builder.md)
- [converter/postprocess/update_restart_dclgen_row_mapper.py](../converter/postprocess/update_restart_dclgen_row_mapper.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
