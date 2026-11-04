# `runners/pytest_runner.py`

Source: [runners/pytest_runner.py](../../../runners/pytest_runner.py) | 323 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `ee31572a67d37c14407f98642fab9a3fd3d13b79d28087fecce688fa41776985`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Runs the project's pytest suite and returns structured results.

## Import declarations

```python
from __future__ import annotations
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ElementTree
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from rules.test_runner_rules import ALL_TESTS_LABEL, FAILING_OUTCOMES, JUNIT_ARG_TEMPLATE, KEYWORD_ARG, OUTCOME_ERROR, OUTCOME_FAILED, OUTCOME_PASSED, OUTCOME_SKIPPED, PYTEST_BASE_ARGS, PYTEST_MODULE, PYTHONPATH_ENTRIES, PYTHONPATH_SEPARATOR_KEY, RUN_TIMEOUT_SECONDS, TEST_FILE_GLOB, TESTS_FOLDER, TIMESTAMP_FORMAT, VERBOSE_ARG
```

## Local dependency notes

- [rules/test_runner_rules.py](../rules/test_runner_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/test_panel.py](../converter/ui/test_panel.md)

## Symbol contracts and control points

### `TestCaseResult` - L58-L70

```python
class TestCaseResult()
```

One pytest test case.

Declared class/data-model fields:

```python
module: str
name: str
outcome: str
duration: float
message: str = ''
detail: str = ''
```

### `TestCaseResult.is_failure` - L69-L70

```python
is_failure(self) -> bool
```

### `TestRunResult` - L74-L119

```python
class TestRunResult()
```

The outcome of one pytest invocation.

Declared class/data-model fields:

```python
command: str
exit_code: int
duration: float
started_at: str
cases: list[TestCaseResult] = field(default_factory=list)
stdout: str = ''
stderr: str = ''
timed_out: bool = False
error: str = ''
```

### `TestRunResult.total` - L89-L90

```python
total(self) -> int
```

Observed calls (lexical order): `len`.

### `TestRunResult.passed` - L93-L94

```python
passed(self) -> int
```

Observed calls (lexical order): `sum`.

### `TestRunResult.failed` - L97-L98

```python
failed(self) -> int
```

Observed calls (lexical order): `sum`.

### `TestRunResult.errors` - L101-L102

```python
errors(self) -> int
```

Observed calls (lexical order): `sum`.

### `TestRunResult.skipped` - L105-L106

```python
skipped(self) -> int
```

Observed calls (lexical order): `sum`.

### `TestRunResult.failing` - L109-L110

```python
failing(self) -> list[TestCaseResult]
```

### `TestRunResult.is_green` - L113-L119

```python
is_green(self) -> bool
```

### `PytestRunner` - L122-L323

```python
class PytestRunner()
```

Discovers and runs the project's pytest suite.

### `PytestRunner.__init__` - L125-L126

```python
__init__(self, project_root: Path | None=None) -> None
```

Observed calls (lexical order): `self._resolve_project_root`.

### `PytestRunner.tests_dir` - L132-L133

```python
tests_dir(self) -> Path
```

### `PytestRunner.available_targets` - L135-L145

```python
available_targets(self) -> list[str]
```

Selectable targets: the whole suite, then each test module.

Observed calls (lexical order): `self.tests_dir.exists`, `sorted`, `self.tests_dir.glob`, `path.is_file`.

Control points:

- L137: `if not self.tests_dir.exists()`

### `PytestRunner.has_tests` - L147-L148

```python
has_tests(self) -> bool
```

Observed calls (lexical order): `len`, `self.available_targets`.

### `PytestRunner.run` - L153-L204

```python
run(self, target: str=ALL_TESTS_LABEL, keyword: str='', verbose: bool=False) -> TestRunResult
```

Observed calls (lexical order): `datetime.now`, `Path`, `tempfile.gettempdir`, `started.strftime`, `self._build_command`, `TestRunResult`, `' '.join`, `subprocess.run`, `str`, `self._environment`, `(datetime.now() - started).total_seconds`, `report_path.exists`, `self._parse_report`, `self._discard`.

Control points:

- L200: `if report_path.exists()`

### `PytestRunner._build_command` - L209-L234

```python
_build_command(self, target: str, keyword: str, verbose: bool, report_path: Path) -> list[str]
```

Observed calls (lexical order): `str`, `str(target or '').strip`, `Path`, `command.append`, `command.extend`, `str(keyword or '').strip`, `JUNIT_ARG_TEMPLATE.format`.

Control points:

- L219: `if selected and selected != ALL_TESTS_LABEL`
- L226: `if verbose`
- L230: `if clean_keyword`

### `PytestRunner._environment` - L236-L246

```python
_environment(self) -> dict[str, str]
```

Observed calls (lexical order): `dict`, `str`, `env.get`, `entries.append`, `os.pathsep.join`.

Control points:

- L243: `if existing`

### `PytestRunner._parse_report` - L251-L290

```python
_parse_report(self, report_path: Path) -> list[TestCaseResult]
```

Observed calls (lexical order): `ElementTree.parse`, `tree.iter`, `child.tag.lower`, `child.get`, `str`, `str(child.get('message', '') or '').strip`, `str(child.text or '').strip`, `cases.append`, `TestCaseResult`, `element.get`, `self._module_of`, `self._float_of`.

Control points:

- L259: `for element in tree.iter('testcase')`
- L264: `for child in element`
- L266: `if tag == 'failure'`
- L268: `if tag == 'error'`
- L270: `if tag == 'skipped'`

### `PytestRunner._module_of` - L293-L301

```python
_module_of(classname: str) -> str
```

tests.test_reflow.TestClass -> tests.test_reflow

Observed calls (lexical order): `str`, `str(classname or '').strip`, `text.split`, `len`, `parts[-1][:1].isupper`, `'.'.join`.

Control points:

- L296: `if not text`
- L299: `if len(parts) > 1 and parts[-1][:1].isupper()`

### `PytestRunner._float_of` - L304-L308

```python
_float_of(value: str) -> float
```

Observed calls (lexical order): `float`, `round`.

### `PytestRunner._discard` - L311-L315

```python
_discard(path: Path) -> None
```

Observed calls (lexical order): `path.unlink`.

### `PytestRunner._resolve_project_root` - L321-L323

```python
_resolve_project_root() -> Path
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
