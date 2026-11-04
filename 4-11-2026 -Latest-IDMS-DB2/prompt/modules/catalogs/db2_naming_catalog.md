# `catalogs/db2_naming_catalog.py`

Source: [catalogs/db2_naming_catalog.py](../../../catalogs/db2_naming_catalog.py) | 23 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `2a8c0dba64ba2b7f412b78e4823e58c36f6f4ea26bef6cc2bd6c5df0106a20b7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 naming catalog.

## Module-level bindings

`DB2_TABLE_SUFFIX_EQUIVALENTS` (L9), `DB2_CURSOR_SUFFIX` (L17), `DB2_DEFAULT_CURSOR_NAME` (L20), `DB2_HOST_REFERENCE_PREFIX` (L23)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/cursor_name_resolver.py](../converter/resolvers/cursor_name_resolver.md)
- [converter/resolvers/host_variable_resolver.py](../converter/resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
