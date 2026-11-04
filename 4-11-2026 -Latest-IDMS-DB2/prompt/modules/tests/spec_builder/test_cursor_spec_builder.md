# `tests/spec_builder/test_cursor_spec_builder.py`

Source: [tests/spec_builder/test_cursor_spec_builder.py](../../../../tests/spec_builder/test_cursor_spec_builder.py) | 21 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `8a7addfbfa5e1bac8118dda3a3dc827e05ee9fab29e3ca8cfbc5d65f2cb102e6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.generators.db2_infrastructure.spec_builder.cursor_spec_builder import CursorSpecBuilder
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](../../converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.md)

## Symbol contracts and control points

### `test_builder_construction_does_not_require_line_utils` - L6-L9

```python
test_builder_construction_does_not_require_line_utils(owner_without_line_utils)
```

Observed calls (lexical order): `CursorSpecBuilder`.

### `test_reporter_is_created_only_when_include_names_is_called` - L12-L21

```python
test_reporter_is_created_only_when_include_names_is_called(owner_with_line_utils)
```

Observed calls (lexical order): `CursorSpecBuilder`, `builder.include_names`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
