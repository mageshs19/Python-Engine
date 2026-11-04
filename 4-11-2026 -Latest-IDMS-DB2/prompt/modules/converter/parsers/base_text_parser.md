# `converter/parsers/base_text_parser.py`

Source: [converter/parsers/base_text_parser.py](../../../../converter/parsers/base_text_parser.py) | 69 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `51752632b5f7e418ff3345a16ff661488734f71888c71d0bff7ca507f92e33b3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/cobol_parser.py](cobol_parser.md)
- [converter/parsers/copybook_parser.py](copybook_parser.md)
- [converter/parsers/dclgen_parser.py](dclgen_parser.md)

## Symbol contracts and control points

### `BaseTextParser` - L1-L69

```python
class BaseTextParser()
```

Shared parser helper methods.

### `BaseTextParser.normalize_line_endings` - L9-L13

```python
normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `BaseTextParser.normalize_spaces` - L15-L25

```python
normalize_spaces(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `output.replace`.

Control points:

- L22: `while ' ' in output`

### `BaseTextParser.clean_text` - L27-L36

```python
clean_text(self, text: str) -> str
```

Observed calls (lexical order): `self.normalize_line_endings`, `self.normalize_spaces`, `output.replace`, `output.replace('“', '"').replace`, `output.replace('‘', "'").replace`.

### `BaseTextParser.clean_cell` - L38-L52

```python
clean_cell(self, value) -> str
```

Observed calls (lexical order): `str`, `text.replace`, `self.normalize_spaces`, `text.strip`.

Control points:

- L42: `if value is None`

### `BaseTextParser.strip_sequence_area` - L54-L69

```python
strip_sequence_area(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L60: `if len(text) > 6`
- L63: `if indicator in ('*', '/')`
- L66: `if text[:6].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
