# `converter/composers/cleanup/error_status_flag_cleanup.py`

Source: [converter/composers/cleanup/error_status_flag_cleanup.py](../../../../../converter/composers/cleanup/error_status_flag_cleanup.py) | 112 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `07877e42d7e0810b48b907c6e865c2f8f7cd443e0669732e81460711ccf9542f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> ERROR-STATUS flag cleanup.

## Import declarations

```python
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from patterns.cobol_cleanup_patterns import ERROR_STATUS_MOVE_PATTERN, SW_STATUS_D_PIC_PATTERN, WORKING_STORAGE_PATTERN, WS_STATUS_PATTERN
from rules.cobol_cleanup_rules import SW_STATUS_D_DECLARATION, WS_DB2_FLAGS_GROUP
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)
- [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)

## Symbol contracts and control points

### `ErrorStatusFlagCleanup` - L26-L112

```python
class ErrorStatusFlagCleanup()
```

### `ErrorStatusFlagCleanup.__init__` - L27-L33

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `ErrorStatusFlagCleanup._logical` - L35-L36

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `ErrorStatusFlagCleanup._leading_spaces` - L38-L39

```python
_leading_spaces(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.leading_spaces`.

### `ErrorStatusFlagCleanup.replace_error_status_with_flag` - L41-L59

```python
replace_error_status_with_flag(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `self._logical`, `ERROR_STATUS_MOVE_PATTERN.match`, `self._leading_spaces`, `output_lines.append`, `self.messages.add`, `'\n'.join`, `'\n'.join(output_lines).rstrip`.

Control points:

- L45: `for line in text.splitlines()`
- L48: `if ERROR_STATUS_MOVE_PATTERN.match(logical)`
- L56: `if replaced`

### `ErrorStatusFlagCleanup.ensure_sw_status_d_declaration` - L61-L88

```python
ensure_sw_status_d_declaration(self, text: str) -> str
```

Observed calls (lexical order): `SW_STATUS_D_PIC_PATTERN.search`, `text.splitlines`, `output.append`, `self._logical`, `WS_STATUS_PATTERN.match`, `self.messages.add`, `'\n'.join`, `'\n'.join(output).rstrip`, `self._insert_sw_status_d_after_working_storage`.

Control points:

- L62: `if 'SW-STATUS-D' not in text`
- L65: `if SW_STATUS_D_PIC_PATTERN.search(text)`
- L72: `for line in lines`
- L75: `if inserted`
- L80: `if WS_STATUS_PATTERN.match(logical)`
- L85: `if inserted`

### `ErrorStatusFlagCleanup._insert_sw_status_d_after_working_storage` - L90-L112

```python
_insert_sw_status_d_after_working_storage(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `output.append`, `self._logical`, `WORKING_STORAGE_PATTERN.match`, `self.messages.add`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L95: `for line in lines`
- L98: `if inserted`
- L103: `if WORKING_STORAGE_PATTERN.match(logical)`
- L109: `if inserted`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
