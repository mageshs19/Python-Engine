# `converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.py) | 37 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `82c1310887b7636302671c0ce58fc118bb6d539d75b08989c2480ca567d57cb5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Classifies a cursor as parent or child.

## Module-level bindings

`PARENT_SERIES_DIGIT` (L11), `__all__` (L37)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_spec import CLASSIFY_PARENT_BY_ABSENT_WHERE, PARAGRAPH_NUMBER_SEPARATOR, PARENT_CURSOR_OPEN_NUMBER
```

## Local dependency notes

- [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)
- [tests/spec_builder/test_parent_classifier.py](../../../../tests/spec_builder/test_parent_classifier.md)

## Symbol contracts and control points

### `SpecParentClassifier` - L14-L34

```python
class SpecParentClassifier()
```

A cursor without predicates is the driving parent cursor.

### `SpecParentClassifier.is_parent` - L17-L25

```python
is_parent(self, where_conditions: list[str], fetch_paragraph: str) -> bool
```

Observed calls (lexical order): `self._legacy_series_result`.

Control points:

- L22: `if CLASSIFY_PARENT_BY_ABSENT_WHERE`

### `SpecParentClassifier._legacy_series_result` - L28-L34

```python
_legacy_series_result(fetch_paragraph: str) -> bool
```

Compatibility-only fallback for historical output comparison.

Observed calls (lexical order): `str`, `str(fetch_paragraph or '').split`, `bool`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
