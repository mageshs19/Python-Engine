# `rules/field_naming_rules.py`

Source: [rules/field_naming_rules.py](../../../rules/field_naming_rules.py) | 44 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `4396622f6ac21ca6ef2ff53855f80f64e56120426de53b7a07f81cbd3510a410`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Deterministic field-naming rules.

## Module-level bindings

`INSERT_ONLY_AUDIT_PREFIXES` (L15), `UPDATE_AUDIT_PREFIXES` (L19)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/repositories/mapping_column_resolver.py](../converter/repositories/mapping_column_resolver.md)

## Symbol contracts and control points

### `canonical_field_key` - L28-L44

```python
canonical_field_key(name: str) -> str
```

Canonical comparison key: uppercase, strip a leading COBOL level number, and remove '-' and '_' separators.

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `text.split`, `parts[0].isdigit`, `' '.join`, `text.replace`, `text.replace('-', '').replace`, `text.replace('-', '').replace('_', '').replace`.

Control points:

- L41: `if parts and parts[0].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
