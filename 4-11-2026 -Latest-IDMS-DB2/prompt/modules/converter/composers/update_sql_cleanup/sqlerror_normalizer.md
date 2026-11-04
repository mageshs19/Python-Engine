# `converter/composers/update_sql_cleanup/sqlerror_normalizer.py`

Source: [converter/composers/update_sql_cleanup/sqlerror_normalizer.py](../../../../../converter/composers/update_sql_cleanup/sqlerror_normalizer.py) | 36 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `74133df42ad65b9ce9d34208912a01efc147124f1278743a6ac7a536eb0789bf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Normalizes malformed 'PERFORM SQLERROR.END-IF.' lines.

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)

## Symbol contracts and control points

### `SqlerrorNormalizer` - L9-L36

```python
class SqlerrorNormalizer()
```

### `SqlerrorNormalizer.__init__` - L10-L11

```python
__init__(self, owner) -> None
```

### `SqlerrorNormalizer.normalize` - L13-L36

```python
normalize(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `self.owner._logical`, `self.owner.MALFORMED_SQLERROR_ENDIF_PATTERN.match`, `output.append`, `self.owner._leading_spaces`, `self.owner.messages.append`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L17: `for line in text.splitlines()`
- L21: `if not match`
- L30: `if changed`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
