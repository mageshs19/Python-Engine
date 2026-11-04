# `converter/parsers/copybook_parser.py`

Source: [converter/parsers/copybook_parser.py](../../../../converter/parsers/copybook_parser.py) | 239 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `bb28aea462f96129a192359142e4da660b455f016cf24b9a3ef231ddb8a3df78`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Parses COBOL copybook fields.

## Module-level bindings

`__all__` (L237)

## Import declarations

```python
from __future__ import annotations
import re
from converter.domain.models import CopybookField
from converter.parsers.base_text_parser import BaseTextParser
from patterns.copybook_patterns import COPYBOOK_COMMENT_OR_SKIP_PATTERN, COPYBOOK_FIELD_PATTERN, COPYBOOK_OCCURS_PATTERN, COPYBOOK_PIC_PATTERN, COPYBOOK_USAGE_PATTERN
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/parsers/base_text_parser.py](base_text_parser.md)
- [patterns/copybook_patterns.py](../../patterns/copybook_patterns.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/input_loader.py](../ui/input_loader.md)
- [review/runner/workspace_inputs.py](../../review/runner/workspace_inputs.md)
- [runners/batch/shared_input_loader.py](../../runners/batch/shared_input_loader.md)
- [runners/retrieval/retrieval_input_loader.py](../../runners/retrieval/retrieval_input_loader.md)
- [runners/update/update_input_loader.py](../../runners/update/update_input_loader.md)
- [tests/test_copybook_redefines_metadata.py](../../tests/test_copybook_redefines_metadata.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_parsers.py](../../tests/test_parsers.md)
- [tests/test_schema_driven_4310_generic_rules.py](../../tests/test_schema_driven_4310_generic_rules.md)

## Symbol contracts and control points

### `CopybookParser` - L29-L234

```python
class CopybookParser(BaseTextParser)
```

Declared class/data-model fields:

```python
RIGHT_SEQUENCE_PATTERN = re.compile('^(?P<body>.*?)(?:\\s+(?P<right>\\d{8}))\\s*$', flags=re.IGNORECASE)
REDEFINES_PATTERN = re.compile('\\bREDEFINES\\s+([A-Z0-9-]+)', re.I)
```

### `CopybookParser.__init__` - L37-L38

```python
__init__(self) -> None
```

### `CopybookParser.parse` - L40-L121

```python
parse(self, text: str, source_label: str='Copybook') -> list[CopybookField]
```

Observed calls (lexical order): `str`, `str(text or '').strip`, `self.diagnostics.append`, `self._logical_lines`, `COPYBOOK_FIELD_PATTERN.search`, `match.group`, `str(match.group('level') or '').strip`, `str(match.group('name') or '').strip`, `str(match.group('name') or '').strip().upper`, `self._redefines`, `CopybookField`, `output.append`, `self._picture`, `self._usage`, `self._occurs`, `len`.

Control points:

- L46: `if not str(text or '').strip()`
- L58: `for line in logical_lines`
- L61: `if not match`
- L68: `if not name`
- L71: `if name == 'FILLER'`
- L74: `if redefines`
- L91: `if level == '88'`

### `CopybookParser._picture` - L123-L132

```python
_picture(self, text: str) -> str
```

Observed calls (lexical order): `COPYBOOK_PIC_PATTERN.search`, `str`, `match.group`, `str(match.group('pic') or '').strip`, `str(match.group('pic') or '').strip().upper`, `str(match.group('pic') or '').strip().upper().rstrip`.

Control points:

- L129: `if not match`

### `CopybookParser._usage` - L134-L143

```python
_usage(self, text: str) -> str
```

Observed calls (lexical order): `COPYBOOK_USAGE_PATTERN.search`, `str`, `match.group`, `str(match.group('usage') or '').strip`, `str(match.group('usage') or '').strip().upper`, `str(match.group('usage') or '').strip().upper().rstrip`.

Control points:

- L140: `if not match`

### `CopybookParser._redefines` - L145-L147

```python
_redefines(self, text: str) -> str
```

Observed calls (lexical order): `self.REDEFINES_PATTERN.search`, `str`, `match.group`, `str(match.group(1) or '').strip`, `str(match.group(1) or '').strip().upper`.

### `CopybookParser._occurs` - L149-L158

```python
_occurs(self, text: str) -> str
```

Observed calls (lexical order): `COPYBOOK_OCCURS_PATTERN.search`, `str`, `match.group`, `str(match.group('occurs') or '').strip`.

Control points:

- L155: `if not match`

### `CopybookParser._logical_lines` - L160-L196

```python
_logical_lines(self, text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `self._copybook_body_line`, `line.strip`, `COPYBOOK_COMMENT_OR_SKIP_PATTERN.search`, `line.lstrip`, `line.lstrip().startswith`, `buffer.split`, `part.strip`, `output.append`, `parts[-1].strip`, `buffer.strip`.

Control points:

- L167: `for raw_line in str(text or '').splitlines()`
- L169: `if not line.strip()`
- L172: `if COPYBOOK_COMMENT_OR_SKIP_PATTERN.search(line)`
- L175: `if line.lstrip().startswith('*') or line.lstrip().startswith('/')`
- L178: `if buffer`
- L183: `if '.' in line`
- L186: `for part in parts[:-1]`
- L188: `if clean`
- Another 1 conditions/loops exist in this source span.

### `CopybookParser._copybook_body_line` - L198-L216

```python
_copybook_body_line(self, raw_line: str) -> str
```

Observed calls (lexical order): `str`, `str(raw_line or '').rstrip`, `str(raw_line or '').rstrip('\n').rstrip`, `text.strip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `self._remove_right_sequence`, `self._remove_right_sequence(body).strip`, `self._remove_right_sequence(text).strip`.

Control points:

- L204: `if not text.strip()`
- L207: `if len(text) > 6 and text[:6].strip().isdigit()`
- L210: `if indicator in ('*', '/')`

### `CopybookParser._remove_right_sequence` - L218-L234

```python
_remove_right_sequence(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').rstrip`, `self.RIGHT_SEQUENCE_PATTERN.match`, `match.group`, `str(match.group('body') or '').rstrip`, `right.isdigit`.

Control points:

- L225: `if not match`
- L230: `if not right`
- L232: `if not right.isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
