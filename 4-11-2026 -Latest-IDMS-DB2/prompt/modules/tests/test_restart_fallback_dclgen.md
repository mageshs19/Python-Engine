# `tests/test_restart_fallback_dclgen.py`

Source: [tests/test_restart_fallback_dclgen.py](../../../tests/test_restart_fallback_dclgen.py) | 74 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `35d9d8352bfd6af0e892cd517b7a138433ae8ca397310cc01f7b6db479fd02a8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Tests for DZ01RSTV fallback when restart DCLGEN metadata is missing.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.postprocess.update_restart_fallback_dclgen import create_fallback_restart_dclgen_role
```

## Local dependency notes

- [converter/postprocess/update_restart_fallback_dclgen.py](../converter/postprocess/update_restart_fallback_dclgen.md)

## Symbol contracts and control points

### `TestFallbackRestartDclgenRole` - L12-L74

```python
class TestFallbackRestartDclgenRole()
```

Verify fallback DZ01RSTV role generation.

### `TestFallbackRestartDclgenRole.test_fallback_role_creation` - L15-L21

```python
test_fallback_role_creation(self)
```

Fallback role has all required fields for restart SQL generation.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

### `TestFallbackRestartDclgenRole.test_fallback_program_field` - L23-L28

```python
test_fallback_program_field(self)
```

Program field mapping correct.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

### `TestFallbackRestartDclgenRole.test_fallback_phase_field` - L30-L35

```python
test_fallback_phase_field(self)
```

Phase field mapping correct.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

### `TestFallbackRestartDclgenRole.test_fallback_date_field` - L37-L42

```python
test_fallback_date_field(self)
```

Date field mapping correct.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

### `TestFallbackRestartDclgenRole.test_fallback_status_field` - L44-L49

```python
test_fallback_status_field(self)
```

Status field mapping correct.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

### `TestFallbackRestartDclgenRole.test_fallback_retention_field` - L51-L56

```python
test_fallback_retention_field(self)
```

Retention field mapping correct.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

### `TestFallbackRestartDclgenRole.test_fallback_payload_fields` - L58-L65

```python
test_fallback_payload_fields(self)
```

Payload and LEN fields mapping correct.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

### `TestFallbackRestartDclgenRole.test_fallback_deterministic` - L67-L74

```python
test_fallback_deterministic(self)
```

Fallback creation is deterministic across calls.

Observed calls (lexical order): `create_fallback_restart_dclgen_role`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
