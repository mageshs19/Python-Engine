# `converter/composers/manual_style_preserver.py`

Source: [converter/composers/manual_style_preserver.py](../../../../converter/composers/manual_style_preserver.py) | 42 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `041f4c936f7cb24aa3f04d0c24de887fa53c74a636b6141e0a929aae1ad262fb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `ManualStylePreserver` - L1-L42

```python
class ManualStylePreserver()
```

Preserves manual COBOL style by avoiding broad formatting changes.

### `ManualStylePreserver.preserve` - L11-L22

```python
preserve(self, original_text: str, converted_text: str) -> str
```

Observed calls (lexical order): `self._preserve_comment_density`, `self._normalize_excess_blank_lines`, `text.rstrip`.

Control points:

- L16: `if not converted_text`

### `ManualStylePreserver._preserve_comment_density` - L24-L33

```python
_preserve_comment_density(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `line.rstrip`, `output_lines.append`, `'\n'.join`.

Control points:

- L30: `for line in str(text or '').splitlines()`

### `ManualStylePreserver._normalize_excess_blank_lines` - L35-L42

```python
_normalize_excess_blank_lines(self, text: str) -> str
```

Observed calls (lexical order): `text.replace`.

Control points:

- L39: `while '\n\n\n\n' in text`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
