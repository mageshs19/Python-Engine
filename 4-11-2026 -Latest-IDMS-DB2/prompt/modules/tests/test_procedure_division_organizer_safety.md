# `tests/test_procedure_division_organizer_safety.py`

Source: [tests/test_procedure_division_organizer_safety.py](../../../tests/test_procedure_division_organizer_safety.py) | 25 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `61446d84581be023cdfbb26db0613e4b417cd01a9352183a7432829f1c4dea82`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.generators.procedure_division_organizer import ProcedureDivisionOrganizer
```

## Local dependency notes

- [converter/generators/procedure_division_organizer.py](../converter/generators/procedure_division_organizer.md)

## Symbol contracts and control points

### `test_legacy_organizer_preserves_original_execution_order_and_emits_no_placeholders` - L4-L25

```python
test_legacy_organizer_preserves_original_execution_order_and_emits_no_placeholders()
```

Observed calls (lexical order): `ProcedureDivisionOrganizer`, `organizer.organize`, `output.index`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
