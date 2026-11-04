# `converter/composers/cobol_formatter.py`

Source: [converter/composers/cobol_formatter.py](../../../../converter/composers/cobol_formatter.py) | 67 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `965d26a30f81810da1b59e8c6bac25f4004da9b1eebe2e34a5349a6e550d488a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_imports.py](../../tests/test_imports.md)

## Symbol contracts and control points

### `CobolFormatter` - L1-L67

```python
class CobolFormatter()
```

Preserve-first COBOL formatter.

### `CobolFormatter.format` - L30-L41

```python
format(self, text: str) -> str
```

Observed calls (lexical order): `self._normalize_line_endings`, `self._rstrip_lines`, `self._normalize_excess_blank_lines`, `normalized.rstrip`.

Control points:

- L34: `if not text`

### `CobolFormatter._normalize_line_endings` - L43-L47

```python
_normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `CobolFormatter._rstrip_lines` - L49-L56

```python
_rstrip_lines(self, text: str) -> str
```

Observed calls (lexical order): `'\n'.join`, `line.rstrip`, `str`, `str(text or '').splitlines`.

### `CobolFormatter._normalize_excess_blank_lines` - L58-L67

```python
_normalize_excess_blank_lines(self, text: str) -> str
```

Observed calls (lexical order): `str`, `output.replace`.

Control points:

- L64: `while '\n\n\n\n' in output`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
