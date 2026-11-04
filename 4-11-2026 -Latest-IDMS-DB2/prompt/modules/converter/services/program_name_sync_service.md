# `converter/services/program_name_sync_service.py`

Source: [converter/services/program_name_sync_service.py](../../../../converter/services/program_name_sync_service.py) | 144 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `04c8af4821b62d44c65bade6f5d7641fc032342340355b074504b5e663c9b77b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Program name synchronization service.

## Module-level bindings

`__all__` (L142)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_derivation_resolver import NameDerivationResolver
from patterns.final_feedback_fix_patterns import COBOL_LITERAL_PATTERN, MOVE_TO_PROGRAM_NAME_PATTERN, PROGRAM_ID_PATTERN, VM_BD_TOKEN_PATTERN
```

## Local dependency notes

- [converter/services/name_derivation_resolver.py](name_derivation_resolver.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)
- [converter/transformers/cobol_transformer.py](../transformers/cobol_transformer.md)

## Symbol contracts and control points

### `ProgramNameSyncService` - L55-L139

```python
class ProgramNameSyncService()
```

Synchronizes PROGRAM-NAME and embedded ids from final PROGRAM-ID.

### `ProgramNameSyncService.__init__` - L58-L65

```python
__init__(self, name_derivation_resolver: NameDerivationResolver | None=None) -> None
```

Observed calls (lexical order): `NameDerivationResolver`.

### `ProgramNameSyncService.reset` - L67-L69

```python
reset(self) -> None
```

Drop diagnostics from the previous program.

### `ProgramNameSyncService.sync` - L74-L104

```python
sync(self, text: str) -> str
```

Rewrite MOVE literal TO PROGRAM-NAME, then embedded ids.

Observed calls (lexical order): `str`, `PROGRAM_ID_PATTERN.search`, `self.messages.append`, `program_match.group`, `program_match.group('program').upper`, `MOVE_TO_PROGRAM_NAME_PATTERN.subn`, `self.sync_literals`.

Control points:

- L79: `if not program_match`
- L98: `if moves`

### `ProgramNameSyncService.sync.replace_program_name` - L87-L92

```python
replace_program_name(match) -> str
```

Observed calls (lexical order): `match.group`.

### `ProgramNameSyncService.sync_literals` - L106-L139

```python
sync_literals(self, text: str) -> str
```

Derive any VM..BD.. program id embedded in a COBOL literal.

Observed calls (lexical order): `str`, `COBOL_LITERAL_PATTERN.sub`, `self.messages.append`, `len`, `'; '.join`, `set`, `sorted`.

Control points:

- L113: `if "'" not in source`
- L132: `if rewritten`

### `ProgramNameSyncService.sync_literals._derive_inside` - L118-L128

```python
_derive_inside(literal_match) -> str
```

Observed calls (lexical order): `VM_BD_TOKEN_PATTERN.sub`, `literal_match.group`.

### `ProgramNameSyncService.sync_literals._derive_inside._derive_token` - L119-L124

```python
_derive_token(token_match) -> str
```

Observed calls (lexical order): `token_match.group`, `self._resolver.derive`, `derived.upper`, `token.upper`, `rewritten.append`.

Control points:

- L122: `if derived.upper() != token.upper()`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
