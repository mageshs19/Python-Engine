# `converter/services/host_reference_normalizer.py`

Source: [converter/services/host_reference_normalizer.py](../../../../converter/services/host_reference_normalizer.py) | 65 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `ba38643b274d5a8cd9baf731752a64fa0394a8b0f4ccff6cd985d77e81f50572`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQL host reference -> COBOL qualified reference. ONE owner.

## Module-level bindings

`HOST_PREFIX` (L30), `SQL_GROUP_SEPARATOR` (L31), `COBOL_QUALIFIER_TEMPLATE` (L32), `__all__` (L60)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/sql_line_mixin.py](../composers/update_sql_cleanup/sql_line_mixin.md)
- [tests/update_sql_cleanup/test_bare_move_rewriter_host_form.py](../../tests/update_sql_cleanup/test_bare_move_rewriter_host_form.md)

## Symbol contracts and control points

### `HostReferenceNormalizer` - L35-L57

```python
class HostReferenceNormalizer()
```

Total: an unparsable reference yields '', never an exception.

### `HostReferenceNormalizer.to_cobol` - L39-L52

```python
to_cobol(reference) -> str
```

Observed calls (lexical order): `str`, `str(reference or '').strip`, `str(reference or '').strip().lstrip`, `text.partition`, `host.strip`, `host.strip().upper`, `group.strip`, `group.strip().upper`, `text.upper`, `COBOL_QUALIFIER_TEMPLATE.format`.

Control points:

- L41: `if not text`
- L44: `if SQL_GROUP_SEPARATOR in text`
- L48: `if not host or not group`

### `HostReferenceNormalizer.is_sql_form` - L55-L57

```python
is_sql_form(reference) -> bool
```

Observed calls (lexical order): `str`, `str(reference or '').strip`, `str(reference or '').strip().lstrip`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
