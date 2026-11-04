# `tests/test_conversion_result_production_gate.py`

Source: [tests/test_conversion_result_production_gate.py](../../../tests/test_conversion_result_production_gate.py) | 10 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `21219651a8592e6a83172654d590a222cde1e8e6c99ad551b70447f47a73aba3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import ConversionResult
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)

## Symbol contracts and control points

### `test_conversion_result_marks_lrf_blocker_as_not_promotable` - L4-L10

```python
test_conversion_result_marks_lrf_blocker_as_not_promotable()
```

Observed calls (lexical order): `ConversionResult`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
