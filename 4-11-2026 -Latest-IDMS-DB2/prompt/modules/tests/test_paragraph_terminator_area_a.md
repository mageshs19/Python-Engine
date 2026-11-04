# `tests/test_paragraph_terminator_area_a.py`

Source: [tests/test_paragraph_terminator_area_a.py](../../../tests/test_paragraph_terminator_area_a.py) | 42 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `bfc64a687f7c034f85acfc9a4511cbe072651c9c98bcdf3163df24ae80d6d42b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.paragraph_terminator_cleanup import ParagraphTerminatorCleanup
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](../converter/composers/cleanup/cleanup_message_collector.md)
- [converter/composers/cleanup/paragraph_terminator_cleanup.py](../converter/composers/cleanup/paragraph_terminator_cleanup.md)

## Symbol contracts and control points

### `test_area_b_single_word_continuation_is_not_misread_as_paragraph_header` - L5-L25

```python
test_area_b_single_word_continuation_is_not_misread_as_paragraph_header()
```

Observed calls (lexical order): `'\n'.join`, `CleanupMessageCollector`, `ParagraphTerminatorCleanup`, `cleanup.ensure_paragraph_termination`.

### `test_area_a_paragraph_header_still_terminates_previous_paragraph` - L28-L42

```python
test_area_a_paragraph_header_still_terminates_previous_paragraph()
```

Observed calls (lexical order): `'\n'.join`, `CleanupMessageCollector`, `ParagraphTerminatorCleanup`, `cleanup.ensure_paragraph_termination`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
