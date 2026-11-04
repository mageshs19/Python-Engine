# `review/engine/__init__.py`

Source: [review/engine/__init__.py](../../../../review/engine/__init__.py) | 8 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `1af03377250476f52f2cd4423f63c66a52fbf9342f6e9e1206b38149f2e20da4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`__all__` (L5)

## Import declarations

```python
from review.engine.context import ReviewContext
from review.engine.models import CheckResult, Outcome, ReviewResult
from review.engine.reviewer import Reviewer, blockers, is_accepted
```

## Local dependency notes

- [review/engine/context.py](context.md)
- [review/engine/models.py](models.md)
- [review/engine/reviewer.py](reviewer.md)

## Importers (28)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/__init__.py](../__init__.md)
- [review/checks/chk_09_record_retrieval_conversion.py](../checks/chk_09_record_retrieval_conversion.md)
- [review/checks/chk_10_record_modification_conversion.py](../checks/chk_10_record_modification_conversion.md)
- [review/checks/chk_11_sqlcode_commit_conversion.py](../checks/chk_11_sqlcode_commit_conversion.md)
- [review/checks/chk_12_cursor_declaration.py](../checks/chk_12_cursor_declaration.md)
- [review/checks/chk_13_cursor_paragraph_structure.py](../checks/chk_13_cursor_paragraph_structure.md)
- [review/checks/chk_14_end_of_cursor_handling.py](../checks/chk_14_end_of_cursor_handling.md)
- [review/checks/chk_15_nested_cursor_processing.py](../checks/chk_15_nested_cursor_processing.md)
- [review/checks/chk_16_update_validation.py](../checks/chk_16_update_validation.md)
- [review/checks/chk_17_restart_logic.py](../checks/chk_17_restart_logic.md)
- [review/checks/chk_18_sql_statements.py](../checks/chk_18_sql_statements.md)
- [review/checks/chk_19_select_columns.py](../checks/chk_19_select_columns.md)
- 16 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
