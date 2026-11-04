# `tests/test_copybook_redefines_metadata.py`

Source: [tests/test_copybook_redefines_metadata.py](../../../tests/test_copybook_redefines_metadata.py) | 17 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `7ff8019f79d42354b2ebf1f61db0255e9fdafc6398262e99a26a45c03f63aeb0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.parsers.copybook_parser import CopybookParser
from converter.repositories.copybook_repository import CopybookRepository
```

## Local dependency notes

- [converter/parsers/copybook_parser.py](../converter/parsers/copybook_parser.md)
- [converter/repositories/copybook_repository.py](../converter/repositories/copybook_repository.md)

## Symbol contracts and control points

### `test_copybook_parser_retains_redefines_for_safe_group_width_resolution` - L5-L17

```python
test_copybook_parser_retains_redefines_for_safe_group_width_resolution()
```

Observed calls (lexical order): `CopybookParser`, `CopybookParser().parse`, `CopybookRepository`, `repository.redefines_for`, `repository.effective_picture_for`, `repository.group_width_for`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
