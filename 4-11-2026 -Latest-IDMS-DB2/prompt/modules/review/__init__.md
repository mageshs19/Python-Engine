# `review/__init__.py`

Source: [review/__init__.py](../../../review/__init__.py) | 18 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `2ad71feaa7e894a3f9b191d6e891f48ef8b98fe61d556bcf6a58c67e77fc18ef`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Automated code review of generated DB2 COBOL.

## Module-level bindings

`__all__` (L15)

## Import declarations

```python
from review.engine import CheckResult, Outcome, ReviewContext, ReviewResult, Reviewer, blockers, is_accepted
```

## Local dependency notes

- [review/engine/__init__.py](engine/__init__.md)

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
