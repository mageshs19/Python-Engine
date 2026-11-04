# `converter/parsers/cobol_parser.py`

Source: [converter/parsers/cobol_parser.py](../../../../converter/parsers/cobol_parser.py) | 199 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `fd82e6f6f4b8736aeba1564869cdddff919c0809f288bd9fa7a64d4ea7abdd96`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L197)

## Import declarations

```python
from converter.domain.models import IdmsOperation
from converter.parsers.base_text_parser import BaseTextParser
from patterns.cobol_patterns import PROGRAM_ID_PATTERN
from patterns.idms_patterns import ERASE_PATTERN, FIND_FIRST_PATTERN, MODIFY_PATTERN, OBTAIN_CALC_PATTERN, OBTAIN_CALC_REVERSED_PATTERN, OBTAIN_FIRST_NEXT_PATTERN, OBTAIN_OWNER_PATTERN, READY_UPDATE_PATTERN, STORE_PATTERN
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/parsers/base_text_parser.py](base_text_parser.md)
- [patterns/cobol_patterns.py](../../patterns/cobol_patterns.md)
- [patterns/idms_patterns.py](../../patterns/idms_patterns.md)

## Importers (11)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_transformer.py](../transformers/cobol_transformer.md)
- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [mainframe/verification/manual_direct_update_parity.py](../../mainframe/verification/manual_direct_update_parity.md)
- [mainframe/zowe_manifest.py](../../mainframe/zowe_manifest.md)
- [mainframe/zowe_semantic_release_gate.py](../../mainframe/zowe_semantic_release_gate.md)
- [review/runner/workspace_inputs.py](../../review/runner/workspace_inputs.md)
- [runners/batch_program_runner.py](../../runners/batch_program_runner.md)
- [runners/retrieval/retrieval_program_converter.py](../../runners/retrieval/retrieval_program_converter.md)
- [runners/update/update_program_converter.py](../../runners/update/update_program_converter.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_parsers.py](../../tests/test_parsers.md)

## Symbol contracts and control points

### `CobolParser` - L17-L194

```python
class CobolParser(BaseTextParser)
```

Parses IDMS COBOL source and identifies IDMS database operations.

### `CobolParser.program_id` - L28-L37

```python
program_id(self, cobol_text: str) -> str
```

Observed calls (lexical order): `PROGRAM_ID_PATTERN.search`, `match.group`, `match.group(1).upper`.

Control points:

- L34: `if not match`

### `CobolParser.analyze` - L39-L61

```python
analyze(self, cobol_text: str) -> list[IdmsOperation]
```

Observed calls (lexical order): `enumerate`, `str`, `str(cobol_text or '').splitlines`, `self._strip_sequence_area`, `clean_line.upper`, `self._operation_from_line`, `operations.append`.

Control points:

- L45: `for (line_number, line) in enumerate(str(cobol_text or '').splitlines(), start=1)`
- L58: `if operation is not None`

### `CobolParser._strip_sequence_area` - L63-L94

```python
_strip_sequence_area(self, line: str) -> str
```

Remove COBOL fixed-format sequence areas from a raw line.

Observed calls (lexical order): `getattr`, `super`, `callable`, `base_helper`, `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L79: `if callable(base_helper)`
- L87: `if len(text) > 6`
- L89: `if indicator in ('*', '/')`
- L91: `if text[:6].strip().isdigit()`

### `CobolParser._operation_from_line` - L96-L194

```python
_operation_from_line(self, line: str, upper: str, line_number: int) -> IdmsOperation | None
```

Observed calls (lexical order): `OBTAIN_CALC_PATTERN.search`, `IdmsOperation`, `match.group`, `match.group('record').upper`, `OBTAIN_CALC_REVERSED_PATTERN.search`, `OBTAIN_FIRST_NEXT_PATTERN.search`, `match.group('mode').upper`, `match.group('set').upper`, `OBTAIN_OWNER_PATTERN.search`, `FIND_FIRST_PATTERN.search`, `(match.group('record') or '').upper`, `STORE_PATTERN.search`, `MODIFY_PATTERN.search`, `ERASE_PATTERN.search`, `READY_UPDATE_PATTERN.search`.

Control points:

- L104: `if match`
- L114: `if match`
- L124: `if match`
- L135: `if match`
- L145: `if match`
- L156: `if match`
- L166: `if match`
- L176: `if match`
- Another 1 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
