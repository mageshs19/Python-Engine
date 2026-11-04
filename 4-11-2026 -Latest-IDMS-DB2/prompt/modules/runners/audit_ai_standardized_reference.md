# `runners/audit_ai_standardized_reference.py`

Source: [runners/audit_ai_standardized_reference.py](../../../runners/audit_ai_standardized_reference.py) | 251 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `86e24b075ce96de92f0f3b862e212cd9706712b91c4cabda88ba2008b1e14c6f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Compare the AI-standardized V6 COBOL examples with current Python output and manual references.

## Module-level bindings

`PROGRAMS` (L15), `TIMESTAMP_RE` (L23)

## Import declarations

```python
from __future__ import annotations
import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any
import difflib
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_ai_standardized_reference_audit.py](../tests/test_ai_standardized_reference_audit.md)

## Symbol contracts and control points

### `latest_python_output` - L26-L43

```python
latest_python_output(output_dir: Path, program: str) -> Path | None
```

Observed calls (lexical order): `list`, `output_dir.glob`, `TIMESTAMP_RE.search`, `'_'.join`, `datetime.strptime`, `match.groups`, `timestamped.append`, `max`, `path.stat`.

Control points:

- L28: `if not candidates`
- L32: `for path in candidates`
- L34: `if not match`
- L41: `if timestamped`

### `read_lines` - L46-L49

```python
read_lines(path: Path | None) -> list[str]
```

Observed calls (lexical order): `path.is_file`, `path.read_text`, `path.read_text(encoding='utf-8', errors='replace').splitlines`.

Control points:

- L47: `if path is None or not path.is_file()`

### `body_text` - L52-L54

```python
body_text(lines: list[str]) -> str
```

Observed calls (lexical order): `'\n'.join`, `(line[6:72] if len(line) >= 7 else line).upper`, `len`.

### `count` - L57-L58

```python
count(pattern: str, text: str) -> int
```

Observed calls (lexical order): `len`, `re.findall`.

### `inspect_program` - L61-L110

```python
inspect_program(path: Path | None, project_root: Path | None=None) -> dict[str, Any]
```

Observed calls (lexical order): `read_lines`, `'\n'.join`, `body_text`, `enumerate`, `re.search`, `max`, `re.findall`, `set`, `sorted`, `count`, `re.escape`, `label.strip`, `label.strip().rstrip`, `labels.count`, `path.relative_to`, `str`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L67: `for index in exec_sql_lines`
- L69: `if re.search('\\bMOVE\\b[^\\n]*\\bTO\\s+SQL-LOCATION\\b', prior, re.I)`
- L73: `for name in cursor_names`

### `normalized_diff_counts` - L113-L128

```python
normalized_diff_counts(left: list[str], right: list[str]) -> dict[str, int]
```

Observed calls (lexical order): `re.sub`, `re.sub('\\s+', ' ', line[6:72]).strip`, `re.sub('\\s+', ' ', line[6:72]).strip().upper`, `difflib.SequenceMatcher`, `matcher.get_opcodes`, `len`.

Control points:

- L123: `for (tag, i1, i2, j1, j2) in matcher.get_opcodes()`
- L124: `if tag in ('insert', 'replace')`
- L126: `if tag in ('delete', 'replace')`

### `build_report` - L131-L185

```python
build_report(project_root: Path, reference_dir: Path | None=None) -> dict[str, Any]
```

Observed calls (lexical order): `helper_audit_path.exists`, `helper_audit_path.read_text`, `json.loads`, `PROGRAMS.items`, `latest_python_output`, `inspect_program`, `py_info.items`, `ref_info.items`, `manual_info.items`, `normalized_diff_counts`, `read_lines`.

Control points:

- L169: `if helper_audit_path.exists()`
- L171: `for (program, manual_ext) in PROGRAMS.items()`

### `markdown_report` - L188-L226

```python
markdown_report(report: dict[str, Any]) -> str
```

Observed calls (lexical order): `report['programs'].items`, `Path`, `out.append`, `list`, `out.extend`, `'\n'.join`.

Control points:

- L197: `for item in report['policy_conflicts']`
- L200: `for (program, item) in report['programs'].items()`
- L208: `for (program, item) in report['programs'].items()`
- L210: `for (source_key, title) in [('python_output', 'Latest Python output'), ('ai_standardized_v6', 'V6 reference'), ('manual_output', 'Manual output')]`

### `main` - L229-L247

```python
main() -> int
```

Observed calls (lexical order): `argparse.ArgumentParser`, `Path`, `Path(__file__).resolve`, `parser.add_argument`, `parser.parse_args`, `build_report`, `json.dumps`, `json_out.write_text`, `markdown_report`, `md_out.write_text`, `print`, `report['programs'].items`, `len`.

Control points:

- L243: `for (program, item) in report['programs'].items()`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
