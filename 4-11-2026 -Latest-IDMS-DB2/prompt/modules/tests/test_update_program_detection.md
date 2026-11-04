# `tests/test_update_program_detection.py`

Source: [tests/test_update_program_detection.py](../../../tests/test_update_program_detection.py) | 107 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `083eeec11770997b6f02516444a463ab1cfd62127950c8de496685830ca6d249`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Tests for UPDATE program detection with DB2 INSERT/UPDATE patterns.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.ui.conversion_actions import _is_update_program
```

## Local dependency notes

- [converter/ui/conversion_actions.py](../converter/ui/conversion_actions.md)

## Symbol contracts and control points

### `test_update_program_detection_idms_store` - L8-L22

```python
test_update_program_detection_idms_store()
```

Traditional IDMS STORE is detected as UPDATE.

Observed calls (lexical order): `_is_update_program`.

### `test_update_program_detection_db2_insert` - L25-L41

```python
test_update_program_detection_db2_insert()
```

DB2 INSERT patterns are detected as UPDATE.

Observed calls (lexical order): `_is_update_program`.

### `test_update_program_detection_db2_update` - L44-L60

```python
test_update_program_detection_db2_update()
```

DB2 UPDATE patterns are detected as UPDATE.

Observed calls (lexical order): `_is_update_program`.

### `test_retrieval_program_detection` - L63-L80

```python
test_retrieval_program_detection()
```

Pure retrieval programs (SELECT only) are not UPDATE.

Observed calls (lexical order): `_is_update_program`.

### `test_idms_retrieval_program_detection` - L83-L99

```python
test_idms_retrieval_program_detection()
```

IDMS OBTAIN/FIND are not write verbs - retrieval only.

Observed calls (lexical order): `_is_update_program`.

### `test_empty_source_is_retrieval` - L102-L107

```python
test_empty_source_is_retrieval()
```

Empty or None source is not detected as UPDATE.

Observed calls (lexical order): `_is_update_program`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
