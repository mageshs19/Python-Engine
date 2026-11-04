# `converter/infrastructure/file_loader.py`

Source: [converter/infrastructure/file_loader.py](../../../../converter/infrastructure/file_loader.py) | 69 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `d43a5ab82bd222f5dff90f0f61a3c91ca1128bfbb1724e039a1d63028f7cf0ee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from io import BytesIO
import pdfplumber
```

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/text_loader.py](../parsers/text_loader.md)
- [converter/ui/input_loader.py](../ui/input_loader.md)
- [runners/batch/program_converter.py](../../runners/batch/program_converter.md)
- [runners/batch/shared_input_loader.py](../../runners/batch/shared_input_loader.md)
- [runners/retrieval/retrieval_input_loader.py](../../runners/retrieval/retrieval_input_loader.md)
- [runners/retrieval/retrieval_program_converter.py](../../runners/retrieval/retrieval_program_converter.md)
- [runners/update/update_input_loader.py](../../runners/update/update_input_loader.md)
- [runners/update/update_program_converter.py](../../runners/update/update_program_converter.md)

## Symbol contracts and control points

### `FileLoader` - L6-L69

```python
class FileLoader()
```

Loads readable text from uploaded-file-like objects.

### `FileLoader.read_uploaded_text` - L19-L35

```python
read_uploaded_text(self, uploaded_file) -> str
```

Observed calls (lexical order): `uploaded_file.getvalue`, `str`, `str(uploaded_file.name or '').lower`, `file_name.endswith`, `self.read_pdf_bytes`, `raw_bytes.decode`.

Control points:

- L23: `if uploaded_file is None`
- L29: `if file_name.endswith('.pdf')`

### `FileLoader.read_pdf_bytes` - L37-L53

```python
read_pdf_bytes(self, raw_bytes: bytes) -> str
```

Observed calls (lexical order): `BytesIO`, `pdfplumber.open`, `page.extract_text`, `page_text.splitlines`, `self._clean_line`, `lines.append`, `'\n'.join`, `'\n'.join(lines).strip`.

Control points:

- L44: `for page in pdf.pages`
- L47: `for raw_line in page_text.splitlines()`
- L50: `if cleaned_line`

### `FileLoader._clean_line` - L55-L69

```python
_clean_line(self, line: str | None) -> str
```

Observed calls (lexical order): `str`, `str(line).rstrip`, `cleaned.replace`, `cleaned.strip`.

Control points:

- L59: `if line is None`
- L66: `while ' ' in cleaned`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
