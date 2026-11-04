# `converter/pipeline/conversion/conversion_message_utils.py`

Source: [converter/pipeline/conversion/conversion_message_utils.py](../../../../../converter/pipeline/conversion/conversion_message_utils.py) | 34 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `5ddc2a70d53ffe2401c17de54bbe6e52e0d57e4c86e43e08ff648d99cd4d99ae`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion_service.py](../conversion_service.md)

## Symbol contracts and control points

### `ConversionMessageUtils` - L4-L34

```python
class ConversionMessageUtils()
```

Message collection helpers shared by the conversion pipeline.

### `ConversionMessageUtils._component_messages` - L7-L23

```python
_component_messages(self, component: object) -> list[str]
```

Return messages from components that optionally expose them.

Observed calls (lexical order): `getattr`, `callable`, `messages`, `str`, `str(message or '').strip`.

Control points:

- L15: `if callable(messages)`
- L17: `if not messages`

### `ConversionMessageUtils._unique_messages` - L25-L34

```python
_unique_messages(self, messages: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `str`, `str(message or '').strip`, `seen.add`, `output.append`.

Control points:

- L28: `for message in messages`
- L30: `if not clean_message or clean_message in seen`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
