# `review/runner/review_file.py`

Source: [review/runner/review_file.py](../../../../review/runner/review_file.py) | 338 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `7a8d500cc2cb5c1177cc4d85c8e9369a0220eb9ac3edaa3e51ade1237c547af3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Review a generated DB2 COBOL file, or every .cbl in a folder.

## Module-level bindings

`PROJECT_ROOT` (L43), `SRC_DIR` (L44), `VALID_KINDS` (L81), `KIND_COUNT_TEMPLATE` (L85), `KIND_SEPARATOR` (L86)

## Import declarations

```python
from __future__ import annotations
import sys
from pathlib import Path
import argparse
from collections import Counter
from review.engine.context import KIND_RETRIEVAL, KIND_UNKNOWN, KIND_UPDATE, ReviewContext
from review.engine.reviewer import Reviewer, blockers, is_accepted
from review.report import csv_writer, text_writer
from review.report.text_writer import render
from review.runner._bootstrap import COBOL_GLOB, EXIT_ACCEPTED, EXIT_ERROR, EXIT_REJECTED, REPORT_DIR, read_text, stamp
from review.standards import wording as w
from review.standards.program_kind_detector import detect_program_kind
from review.runner.workspace_inputs import WorkspaceReviewInputs
```

## Local dependency notes

- [review/engine/context.py](../engine/context.md)
- [review/engine/reviewer.py](../engine/reviewer.md)
- [review/report/__init__.py](../report/__init__.md)
- [review/report/csv_writer.py](../report/csv_writer.md)
- [review/report/text_writer.py](../report/text_writer.md)
- [review/runner/_bootstrap.py](_bootstrap.md)
- [review/runner/workspace_inputs.py](workspace_inputs.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/program_kind_detector.py](../standards/program_kind_detector.md)
- [review/standards/wording.py](../standards/wording.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)
- [tests/test_review_kind_wiring.py](../../tests/test_review_kind_wiring.md)

## Symbol contracts and control points

### `NothingToReview` - L89-L94

```python
class NothingToReview(Exception)
```

The folder exists but holds no generated .cbl.

### `NothingToReview.__init__` - L92-L94

```python
__init__(self, folder: Path) -> None
```

Observed calls (lexical order): `Path`, `super`, `super().__init__`, `w.MSG_NO_OUTPUT_FOUND.format`.

### `parse_arguments` - L97-L132

```python
parse_arguments() -> argparse.Namespace
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_mutually_exclusive_group`, `source.add_argument`, `parser.add_argument`, `str`, `parser.parse_args`.

### `resolve_targets` - L135-L158

```python
resolve_targets(args: argparse.Namespace) -> list[Path]
```

Observed calls (lexical order): `Path`, `path.is_file`, `FileNotFoundError`, `w.MSG_FILE_NOT_FOUND.format`, `folder.exists`, `w.MSG_FOLDER_NOT_FOUND.format`, `folder.is_dir`, `w.MSG_PATH_NOT_FOLDER.format`, `sorted`, `folder.glob`, `item.is_file`, `item.stat`, `NothingToReview`, `item.name.lower`.

Control points:

- L136: `if args.path`
- L138: `if not path.is_file()`
- L143: `if not folder.exists()`
- L145: `if not folder.is_dir()`
- L153: `if not files`
- L156: `if args.latest`

Explicit raises: `FileNotFoundError(w.MSG_FILE_NOT_FOUND.format(path=path))`; `FileNotFoundError(w.MSG_FOLDER_NOT_FOUND.format(folder=folder))`; `FileNotFoundError(w.MSG_PATH_NOT_FOLDER.format(folder=folder))`; `NothingToReview(folder)`.

### `resolve_kind` - L161-L164

```python
resolve_kind(value: str) -> str
```

The operator's --kind, or UNKNOWN when absent or unrecognised.

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`.

### `build_context` - L167-L200

```python
build_context(cbl_path: Path, kind: str, source_text: str, *, workspace_inputs=None) -> ReviewContext
```

Build the review input for ONE file.

Observed calls (lexical order): `read_text`, `workspace_inputs.for_program`, `detect_program_kind`, `ReviewContext`.

Control points:

- L181: `if metadata is not None`
- L185: `if resolved == KIND_UNKNOWN`

### `describe_kinds` - L203-L220

```python
describe_kinds(contexts: list[ReviewContext]) -> str
```

What the run actually resolved, in a stable order.

Observed calls (lexical order): `len`, `Counter`, `KIND_SEPARATOR.join`, `KIND_COUNT_TEMPLATE.format`, `counts.get`.

Control points:

- L210: `if not contexts`
- L212: `if len(contexts) == 1`

### `print_banner` - L223-L237

```python
print_banner(args, targets: list[Path], kind_summary: str, report_dir: Path) -> None
```

Observed calls (lexical order): `print`, `Path`, `w.MSG_REVIEWED_FOLDER.format`, `len`, `w.MSG_FILE_COUNT.format`, `w.MSG_PROGRAM_KIND.format`, `w.MSG_REPORT_FOLDER.format`.

Control points:

- L232: `if args.folder`

### `print_nothing_to_review` - L240-L248

```python
print_nothing_to_review(exc: NothingToReview) -> int
```

Observed calls (lexical order): `print`, `w.MSG_NO_OUTPUT_FOUND.format`.

### `run` - L251-L319

```python
run() -> int
```

Observed calls (lexical order): `parse_arguments`, `Path`, `report_dir.mkdir`, `resolve_kind`, `source_path.is_file`, `FileNotFoundError`, `w.MSG_SOURCE_NOT_FOUND.format`, `read_text`, `resolve_targets`, `getattr`, `WorkspaceReviewInputs`, `build_context`, `Reviewer`, `stamp`, `describe_kinds`, `print_banner`.
Another 17 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L260: `if args.source`
- L262: `if not source_path.is_file()`
- L274: `if getattr(args, 'workspace', None)`
- L288: `for (cbl_path, context) in zip(targets, contexts)`
- L296: `if args.quiet`
- L306: `if len(results) > 1`

Explicit raises: `FileNotFoundError(w.MSG_SOURCE_NOT_FOUND.format(path=source_path))`.

### `main` - L322-L334

```python
main() -> None
```

Observed calls (lexical order): `SystemExit`, `run`, `print_nothing_to_review`, `print`, `w.MSG_ERROR.format`.

Explicit raises: `SystemExit(run())`; `re-raise`; `SystemExit(print_nothing_to_review(exc))`; `SystemExit(EXIT_ERROR)`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
