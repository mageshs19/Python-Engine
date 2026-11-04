# `review/report/__init__.py`

Source: [review/report/__init__.py](../../../../review/report/__init__.py) | 3 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `d2ea34f275bf18b8f6e24b5c429200ad3bf22b472ed0848f439e4a72fcc06cd9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`__all__` (L3)

## Import declarations

```python
from review.report import csv_writer, text_writer
```

## Local dependency notes

- [review/report/csv_writer.py](csv_writer.md)
- [review/report/text_writer.py](text_writer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/runner/review_file.py](../runner/review_file.md)
- [review/ui/review_panel.py](../ui/review_panel.md)

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
