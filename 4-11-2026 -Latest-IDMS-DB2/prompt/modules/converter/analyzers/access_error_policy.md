# `converter/analyzers/access_error_policy.py`

Source: [converter/analyzers/access_error_policy.py](../../../../converter/analyzers/access_error_policy.py) | 93 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `468c7a68b51f762e97d39b67c6cf6958bf8127d1955a359a1eedcc2fe6b4daba`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Access-pattern-aware DB2 SQL result and error policy.

## Module-level bindings

`POLICIES` (L33), `__all__` (L93)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/idms_statement/data_statement_converter.py](../transformers/idms_statement/data_statement_converter.md)
- [converter/validators/generated_cobol_release_validator.py](../validators/generated_cobol_release_validator.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../tests/test_generic_cursor_numbering_and_perform_integrity.md)

## Symbol contracts and control points

### `AccessPattern` - L15-L22

```python
class AccessPattern(str, Enum)
```

Declared class/data-model fields:

```python
CURSOR_OPEN = 'cursor_open'
CURSOR_FETCH = 'cursor_fetch'
CURSOR_CLOSE = 'cursor_close'
SINGLETON_SELECT = 'singleton_select'
LR_OBTAIN_FIRST = 'lr_obtain_first'
LR_OBTAIN_NEXT = 'lr_obtain_next'
UNKNOWN = 'unknown'
```

### `AccessErrorPolicy` - L26-L30

```python
class AccessErrorPolicy()
```

Declared class/data-model fields:

```python
pattern: AccessPattern
sqlcode_zero: str
sqlcode_100: str
unexpected_sqlcode: str = 'route_to_shared_sqlerror'
```

### `classify_access` - L44-L64

```python
classify_access(*, sql: str='', source_statement: str='', cursor_operation: str='') -> AccessPattern
```

Classify one access using explicit operation metadata first, then text.

Observed calls (lexical order): `(cursor_operation or '').strip`, `(cursor_operation or '').strip().lower`, `_mask_literals`, `_mask_literals(source_statement).upper`, `re.search`, `_mask_literals(sql).upper`.

Control points:

- L52: `if operation in {'open', 'fetch', 'close'}`
- L56: `if re.search('\\bOBTAIN\\s+FIRST\\b', source)`
- L58: `if re.search('\\bOBTAIN\\s+NEXT\\b', source)`
- L62: `if re.search('\\bSELECT\\b', statement) and re.search('\\bINTO\\b', statement) and re.search('\\bFROM\\b', statement)`

### `policy_for` - L67-L68

```python
policy_for(pattern: AccessPattern) -> AccessErrorPolicy
```

Observed calls (lexical order): `POLICIES.get`.

### `_mask_literals` - L71-L90

```python
_mask_literals(text: str) -> str
```

Mask SQL/COBOL literals so keywords inside strings do not classify code.

Observed calls (lexical order): `list`, `str`, `len`, `''.join`.

Control points:

- L76: `while i < len(chars)`
- L78: `if quote`
- L80: `if ch == quote`
- L81: `if i + 1 < len(chars) and chars[i + 1] == quote`
- L86: `if ch in ("'", '"')`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
