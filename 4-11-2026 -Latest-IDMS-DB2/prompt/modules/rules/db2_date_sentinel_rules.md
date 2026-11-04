# `rules/db2_date_sentinel_rules.py`

Source: [rules/db2_date_sentinel_rules.py](../../../rules/db2_date_sentinel_rules.py) | 101 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `51992ae1749acb64e4b27438e533af795f98f6e011ab31afc340c357e0da325c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 null-date sentinel policy constants.

## Module-level bindings

`ENFORCE_DB2_DATE_NULL_SENTINEL` (L33), `PARM_DATE_SOURCE_SUFFIXES` (L41), `PARM_DATE_SOURCE_PREFIXES` (L50), `PARM_DATE_SOURCE_NAMES` (L53), `DCLGEN_QUALIFIER_TOKENS` (L60), `DCLGEN_NAME_PREFIX` (L61), `SENTINEL_GUARD_OPEN` (L66), `SENTINEL_GUARD_MOVE` (L67), `SENTINEL_GUARD_CLOSE` (L68), `SENTINEL_GUARD_BODY_INDENT` (L69), `DB2_DATE_SENTINEL_MESSAGES` (L74), `__all__` (L89)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/db2_date_sentinel_policy.py](../converter/services/db2_date_sentinel_policy.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
