# `converter/analyzers/lr_access/lr_access_analyser.py`

Source: [converter/analyzers/lr_access/lr_access_analyser.py](../../../../../converter/analyzers/lr_access/lr_access_analyser.py) | 803 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `b3d7195021cfe2d434f084fdb7aa648279e6539023246b3263267a9a5fff0cd1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Conservative whole-block classifier for expanded IDMS logical-record access.

## Module-level bindings

`__all__` (L803)

## Import declarations

```python
from __future__ import annotations
import re
from collections import Counter
from rules.lr_access_rules import END_OF_SET_CONDITIONS, END_OF_SET_STATUS_FIELDS, LR_ACCESS_MESSAGES
```

## Local dependency notes

- [rules/lr_access_rules.py](../../../rules/lr_access_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../../pipeline/conversion/conversion_component_factory.md)
- [tests/test_lr_access_analyser.py](../../../tests/test_lr_access_analyser.md)

## Symbol contracts and control points

### `LrAccessAnalyser` - L20-L800

```python
class LrAccessAnalyser()
```

Classify simple inline bounded searches without mutating source text.

Declared class/data-model fields:

```python
_LR_ACCESS_RE = '\\b(?:OBTAIN\\b|FIND\\b|STORE\\s+[A-Z][A-Z0-9-]*|MODIFY\\s+[A-Z][A-Z0-9-]*|ERASE\\s+[A-Z][A-Z0-9-]*|CONNECT\\s+[A-Z][A-Z0-9-]*|DISCONNECT\\s+[A-Z][A-Z0-9-]*)\\b|EXPANDED LRF'
_FIXED = re.compile('^\\d{6}([ */D-])?(.*)$', re.I)
_OBTAIN = re.compile('\\bOBTAIN\\s+(?P<kind>FIRST|NEXT)\\s+(?P<record>[A-Z][A-Z0-9-]*)(?:\\s+WITHIN\\s+(?P<set>[A-Z][A-Z0-9-]*))?(?P<tail>[^.\\n]*)', re.I)
_INLINE_LOOP = re.compile('(?<![A-Z0-9-])PERFORM\\s+UNTIL\\s+(?P<condition>.*?)\\bEND-PERFORM\\b', re.I | re.S)
_LITERAL_EQUALITY = re.compile('\\b(?P<field>[A-Z][A-Z0-9-]*)(?:\\s+(?:OF|IN)\\s+[A-Z][A-Z0-9-]*)?\\s*(?:NOT\\s*=|<=|>=|=|<|>)\\s*(?P<literal>\'[^\']*\'|\\"[^\\"]*\\"|[+-]?\\d+)', re.I)
```

### `LrAccessAnalyser.__init__` - L59-L60

```python
__init__(self) -> None
```

### `LrAccessAnalyser._source_area` - L63-L67

```python
_source_area(line: str) -> tuple[str, str]
```

Return indicator and source area for fixed-format or free text.

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].rstrip`, `line.rstrip`.

Control points:

- L65: `if len(line) >= 7 and line[:6].isdigit()`

### `LrAccessAnalyser._strip_inline_comment` - L70-L94

```python
_strip_inline_comment(body: str) -> str
```

Strip COBOL ``*>`` comments without cutting quoted data literals.

Observed calls (lexical order): `len`, `body[:index].rstrip`, `body.rstrip`.

Control points:

- L80: `while index < len(body)`
- L82: `if quote`
- L83: `if char == quote`
- L85: `if index + 1 < len(body) and body[index + 1] == quote`
- L89: `if char in {"'", '"'}`
- L91: `if char == '*' and index + 1 < len(body) and (body[index + 1] == '>')`

### `LrAccessAnalyser._logical_text` - L97-L116

```python
_logical_text(cls, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `cls._source_area`, `cls._strip_inline_comment`, `cls._strip_inline_comment(body).strip`, `bodies.append`, `'\n'.join`, `'\n'.join(bodies).upper`.

Control points:

- L99: `for raw in str(text or '').splitlines()`
- L101: `if indicator in {'*', '/', 'D', 'd'}`
- L104: `if not body`
- L106: `if indicator == '-' and bodies`

### `LrAccessAnalyser._is_status_term` - L119-L127

```python
_is_status_term(term: str) -> bool
```

Observed calls (lexical order): `re.sub`, `re.sub('\\s+', ' ', term.upper()).strip`, `term.upper`, `any`, `re.search`.

Control points:

- L121: `if any((token in normalized for token in END_OF_SET_STATUS_FIELDS))`
- L123: `if any((token in normalized for token in END_OF_SET_CONDITIONS))`
- L125: `if re.search('\\b[A-Z0-9-]+-EOC\\b', normalized)`

### `LrAccessAnalyser._paragraph_labels` - L130-L171

```python
_paragraph_labels(text: str) -> list[tuple[int, str, str]]
```

Return paragraph labels in physical order, retaining duplicate names.

Observed calls (lexical order): `text.splitlines`, `next`, `enumerate`, `re.search`, `len`, `range`, `re.fullmatch`, `match.group`, `match.group(1).upper`, `match.group(2).strip`, `name.endswith`, `labels.append`.

Control points:

- L160: `for index in range(scan_start, len(lines))`
- L162: `if not match`
- L165: `if name in reserved`
- L168: `if name.endswith('-SECTION') and (not trailing)`

### `LrAccessAnalyser._section_bodies` - L174-L211

```python
_section_bodies(text: str) -> list[tuple[int, str, str]]
```

Return COBOL section bodies in physical order.

Observed calls (lexical order): `text.splitlines`, `next`, `enumerate`, `re.search`, `len`, `range`, `re.fullmatch`, `headers.append`, `match.group`, `match.group(1).upper`, `'\n'.join`, `sections.append`.

Control points:

- L190: `for index in range(scan_start, len(lines))`
- L195: `if match`
- L198: `if re.search('\\b(?:IDENTIFICATION|ENVIRONMENT|DATA|PROCEDURE)\\s+DIVISION\\b', line, re.I)`
- L202: `for (header_index, (line_index, name)) in enumerate(headers)`
- L203: `if name == '__DIVISION_BOUNDARY__'`

### `LrAccessAnalyser._paragraph_bodies` - L214-L233

```python
_paragraph_bodies(text: str) -> dict[str, str]
```

Return paragraph bodies, conservatively unioning duplicate labels.

Observed calls (lexical order): `text.splitlines`, `LrAccessAnalyser._paragraph_labels`, `enumerate`, `len`, `'\n'.join`.

Control points:

- L225: `for (label_index, (line_index, name, trailing)) in enumerate(labels)`
- L229: `if name in paragraphs`

### `LrAccessAnalyser._expand_procedure_copybooks` - L236-L342

```python
_expand_procedure_copybooks(cls, text: str, copybooks: dict[str, str] | None) -> tuple[str, list[str]]
```

Expand supplied procedure COPY books for analysis only.

Observed calls (lexical order): `(copybooks or {}).items`, `key_for`, `str`, `re.compile`, `next`, `enumerate`, `text.splitlines`, `re.search`, `expand_lines`, `'\n'.join`, `dict.fromkeys`, `list`.

Control points:

- L256: `for (key, value) in (copybooks or {}).items()`
- L267: `if procedure_start is None`

### `LrAccessAnalyser._expand_procedure_copybooks.key_for` - L250-L253

```python
key_for(value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().strip`, `str(value or '').strip().strip('"\'').upper`, `re.sub`.

### `LrAccessAnalyser._expand_procedure_copybooks.expand_lines` - L273-L337

```python
expand_lines(source_lines: list[str], active: tuple[str, ...], depth: int) -> list[str]
```

Observed calls (lexical order): `copy_line.fullmatch`, `re.match`, `re.search`, `copy_name_match.group`, `copy_name_match.group(1).upper`, `diagnostics.append`, `output.append`, `key_for`, `match.group`, `match.group(2).strip`, `cls._logical_text`, `copy_text.strip`, `copy_text.splitlines`, `expand_lines`, `output.extend`.

Control points:

- L275: `for line in source_lines`
- L277: `if not match`
- L280: `if re.match('^\\s*COPY\\s+[A-Z0-9][A-Z0-9-]*\\b', line, re.I) and re.search('\\bREPLACING\\b', line, re.I)`
- L292: `if tail`
- L295: `if re.search('\\bREPLACING\\b', tail, re.I)`
- L307: `if name not in normalized`
- L314: `if name in active`
- L321: `if depth >= 16`
- Another 1 conditions/loops exist in this source span.

### `LrAccessAnalyser._has_procedure_copy` - L345-L372

```python
_has_procedure_copy(cls, text: str) -> bool
```

Return whether a COPY statement appears in PROCEDURE DIVISION.

Observed calls (lexical order): `text.splitlines`, `next`, `enumerate`, `re.search`, `re.compile`, `literal.sub`.

Control points:

- L361: `if procedure_start is None`
- L365: `for line in lines[procedure_start + 1:]`
- L370: `if re.search('\\bCOPY\\s+[A-Z0-9][A-Z0-9-]*\\b', code, re.I)`

### `LrAccessAnalyser._unsupported_loop_diagnostics` - L375-L674

```python
_unsupported_loop_diagnostics(text: str) -> list[str]
```

Explain paragraph/THRU LRF loops that are intentionally not rewritten.

Observed calls (lexical order): `bool`, `re.search`, `LrAccessAnalyser._has_procedure_copy`, `LrAccessAnalyser._paragraph_bodies`, `LrAccessAnalyser._section_bodies`, `Counter`, `section_counts.items`, `LrAccessAnalyser._paragraph_labels`, `name_counts.items`, `re.compile`, `mask_literals`, `loop_tokens.finditer`, `token.group`, `token.group(0).upper`, `token.group(0).upper().startswith`, `inline_loop_stack.append`.
Another 24 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L390: `if not has_visible_lr_access and (not has_procedure_copy)`
- L398: `for (_line, name, body) in section_entries`
- L399: `if name in sections`
- L540: `for token in loop_tokens.finditer(scan_text)`
- L541: `if token.group(0).upper().startswith('PERFORM')`
- L543: `if inline_loop_stack`
- L550: `for start in unmatched_inline_starts`
- L553: `if not has_access`
- Another 21 conditions/loops exist in this source span.

### `LrAccessAnalyser._unsupported_loop_diagnostics.mask_literals` - L416-L424

```python
mask_literals(body: str) -> str
```

Mask quoted literals before recognizing executable COBOL verbs.

Observed calls (lexical order): `re.compile`, `literal.sub`, `match.group`, `re.sub`.

### `LrAccessAnalyser._unsupported_loop_diagnostics.paragraph_tree_has_access` - L426-L510

```python
paragraph_tree_has_access(start_names: list[str]) -> bool
```

Observed calls (lexical order): `list`, `set`, `pending.pop`, `pending.pop().upper`, `diagnostics.append`, `visited.add`, `mask_literals`, `access_pattern.search`, `perform_pattern.finditer`, `call.group`, `call.group(1).upper`, `(call.group(2) or '').upper`, `names.index`, `pending.extend`, `pending.append`.

Control points:

- L429: `while pending`
- L431: `if name in visited`
- L438: `if name in duplicate_names`
- L449: `if name in paragraphs and name in sections or name in duplicate_sections`
- L456: `if name in paragraphs`
- L458: `if name in sections`
- L471: `if access_pattern.search(body)`
- L473: `for call in perform_pattern.finditer(body)`
- Another 4 conditions/loops exist in this source span.

### `LrAccessAnalyser.bounded_searches` - L676-L800

```python
bounded_searches(self, cobol_text: str, procedure_copybooks: dict[str, str] | None=None) -> dict[str, str]
```

Return proven bounded searches, optionally analyzing supplied procedure COPY books.

Observed calls (lexical order): `self._logical_text`, `self._expand_procedure_copybooks`, `self.messages.extend`, `self._unsupported_loop_diagnostics`, `list`, `self._INLINE_LOOP.finditer`, `self._OBTAIN.finditer`, `set`, `enumerate`, `loop.group`, `re.search`, `self.messages.append`, `next`, `m.group`, `m.group('kind').upper`, `next_access.start`.
Another 29 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L692: `if 'EXPANDED LRF FIRST' not in text and 'OBTAIN FIRST' not in text`
- L700: `for (loop_index, loop) in enumerate(loops)`
- L705: `if re.search('(?<![A-Z0-9-])PERFORM\\s+UNTIL\\b', loop_text, re.I)`
- L719: `if next_access is None`
- L723: `if trailing_body`
- L730: `if re.search('\\b(?:MOVE|DISPLAY|CALL|COMPUTE|ADD|SUBTRACT|MULTIPLY|DIVIDE|IF|EVALUATE|WRITE|READ|CONTINUE|PERFORM|OBTAIN|STORE|MODIFY|DELETE|EXEC|SQL|GOBACK|STOP|CLOSE|OPEN|EXIT|S...`
- L748: `if not status_terms or len(data_predicates) != 1`
- L765: `if len(first_matches) != 1`
- Another 3 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
