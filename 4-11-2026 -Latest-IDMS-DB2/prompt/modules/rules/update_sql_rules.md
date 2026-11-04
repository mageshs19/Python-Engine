# `rules/update_sql_rules.py`

Source: [rules/update_sql_rules.py](../../../rules/update_sql_rules.py) | 46 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `25641e06fd3f20f8750f2a99334a559adb4e8f4e1bf3d7b65eda5fc44d283985`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Update SQL generation rules.

## Module-level bindings

`CONSERVATIVE_UPDATE_RULES` (L14), `UPDATE_AUDIT_COLUMN_PREFIXES` (L24), `INSERT_ONLY_AUDIT_COLUMN_PREFIXES` (L32), `KEY_TEXT_MARKERS` (L36), `DATE_COLUMN_PREFIXES` (L43)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
