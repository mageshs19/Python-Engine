# `converter/generators/timestamp/program_id_resolver.py`

Source: [converter/generators/timestamp/program_id_resolver.py](../../../../../converter/generators/timestamp/program_id_resolver.py) | 45 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `6edf2503cbbf26b6bc444a70ed0df48b9a28b7b1bd541ada1150dfa40a667adf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`PROGRAM_ID_PATTERN` (L10), `__all__` (L45)

## Import declarations

```python
from __future__ import annotations
import re
from rules.timestamp_audit_rules import TIMESTAMP_DEFAULT_PROGRAM_ID, TIMESTAMP_PROGRAM_ID_LENGTH
```

## Local dependency notes

- [rules/timestamp_audit_rules.py](../../../rules/timestamp_audit_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/__init__.py](__init__.md)
- [converter/generators/timestamp/cs_program_declarator.py](cs_program_declarator.md)
- [converter/generators/timestamp_generator.py](../timestamp_generator.md)

## Symbol contracts and control points

### `ProgramIdResolver` - L16-L42

```python
class ProgramIdResolver()
```

### `ProgramIdResolver.resolve` - L18-L22

```python
resolve(self, target_program_id: str) -> str
```

Observed calls (lexical order): `str`, `str(target_program_id or '').strip`, `str(target_program_id or '').strip().upper`.

Control points:

- L20: `if not program_id`

### `ProgramIdResolver.from_source` - L24-L29

```python
from_source(self, bodies: list[str]) -> str
```

Observed calls (lexical order): `PROGRAM_ID_PATTERN.match`, `str`, `str(body or '').strip`, `match.group`, `match.group('name').upper`.

Control points:

- L25: `for body in bodies or []`
- L27: `if match`

### `ProgramIdResolver.resolve_with_fallback` - L31-L39

```python
resolve_with_fallback(self, target_program_id: str, bodies: list[str]) -> str
```

Observed calls (lexical order): `str`, `str(target_program_id or '').strip`, `self.resolve`, `self.from_source`.

Control points:

- L37: `if explicit`

### `ProgramIdResolver.padded` - L41-L42

```python
padded(self, program_id: str) -> str
```

Observed calls (lexical order): `self.resolve`, `self.resolve(program_id).ljust`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
