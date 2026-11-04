# `tests/test_vmdz1526_lrf_update_integration.py`

Source: [tests/test_vmdz1526_lrf_update_integration.py](../../../tests/test_vmdz1526_lrf_update_integration.py) | 175 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `6da41ffc0bea1446c29f8d135b93040bdd249ce074279c8def1392568e22588b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from converter.infrastructure.logger_factory import LoggerFactory
from runners.update.update_input_loader import load_shared_inputs
from runners.update.update_program_converter import convert_one_program
from tests.workspace_fixtures import expanded_program
```

## Local dependency notes

- [converter/infrastructure/logger_factory.py](../converter/infrastructure/logger_factory.md)
- [runners/update/update_input_loader.py](../runners/update/update_input_loader.md)
- [runners/update/update_program_converter.py](../runners/update/update_program_converter.md)
- [tests/workspace_fixtures.py](workspace_fixtures.md)

## Symbol contracts and control points

### `_logical_cobol` - L10-L17

```python
_logical_cobol(text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `len`, `line[:6].isdigit`, `line[7:72].strip`, `logical_lines.append`, `line.strip`, `'\n'.join`.

Control points:

- L12: `for line in text.splitlines()`
- L13: `if len(line) >= 7 and line[:6].isdigit()`

### `_matching_paren` - L20-L38

```python
_matching_paren(text: str, open_index: int) -> int
```

Observed calls (lexical order): `len`, `AssertionError`.

Control points:

- L24: `while index < len(text)`
- L26: `if char == "'"`
- L27: `if quoted and index + 1 < len(text) and (text[index + 1] == "'")`
- L31: `if not quoted and char == '('`
- L33: `if not quoted and char == ')'`
- L35: `if depth == 0`

Explicit raises: `AssertionError('unbalanced SQL parentheses')`.

### `_split_top_level_commas` - L41-L65

```python
_split_top_level_commas(text: str) -> list[str]
```

Observed calls (lexical order): `len`, `text[start:index].strip`, `values.append`, `text[start:].strip`.

Control points:

- L47: `while index < len(text)`
- L49: `if char == "'"`
- L50: `if quoted and index + 1 < len(text) and (text[index + 1] == "'")`
- L54: `if not quoted and char == '('`
- L56: `if not quoted and char == ')'`
- L58: `if not quoted and depth == 0 and (char == ',')`
- L63: `if tail`

### `test_vmdz1526_lrf_store_and_update_generate_singleton_sql_without_cursor` - L68-L175

```python
test_vmdz1526_lrf_store_and_update_generate_singleton_sql_without_cursor(tmp_path)
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `expanded_program`, `source.exists`, `LoggerFactory.create_logger`, `load_shared_inputs`, `TemporaryDirectory`, `convert_one_program`, `output_path.read_text`, `re.search`, `len`, `re.findall`, `insert_match.group`, `_logical_cobol`, `logical.upper`, `logical.upper().index`.
Another 13 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L115: `for required in ('NR_ID_479EVEF', 'TS_CREATE_479EVEF', 'TS_UPDATE_479EVEF', 'ID_USERID_479EVEF', 'NS_IDMSKEY_479EVEF', 'NEXT VALUE FOR DZEVEFSQ', 'RIGHT(DIGITS')`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
