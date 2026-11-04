# `converter/composers/update_sql_cleanup/obtain_calc_remover.py`

Source: [converter/composers/update_sql_cleanup/obtain_calc_remover.py](../../../../../converter/composers/update_sql_cleanup/obtain_calc_remover.py) | 174 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `c35d860e4d8be55b9e447a431af0cda1546ff25cda0ed54cbee8ce7da04f8eb7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Removes a generated OBTAIN CALC SELECT block before a direct UPDATE.

## Module-level bindings

`PROGRAM_KIND_ATTRIBUTE` (L63), `STOOD_DOWN_MESSAGE` (L65), `REMOVED_MESSAGE` (L70), `__all__` (L174)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.program_kind_rules import KIND_RETRIEVAL
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/program_kind_rules.py](../../../rules/program_kind_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)

## Symbol contracts and control points

### `ObtainCalcRemover` - L76-L171

```python
class ObtainCalcRemover()
```

### `ObtainCalcRemover.__init__` - L77-L79

```python
__init__(self, owner, scanner) -> None
```

### `ObtainCalcRemover._stands_down` - L81-L93

```python
_stands_down(self) -> bool
```

True when this program is read-only.

Observed calls (lexical order): `str`, `str(getattr(self.owner, PROGRAM_KIND_ATTRIBUTE, '') or '').strip`, `str(getattr(self.owner, PROGRAM_KIND_ATTRIBUTE, '') or '').strip().lower`, `getattr`.

### `ObtainCalcRemover.rewrite` - L95-L171

```python
rewrite(self, text: str) -> str
```

Observed calls (lexical order): `self._stands_down`, `self.owner.CONVERTED_OBTAIN_CALC_PATTERN.search`, `str`, `self.owner.messages.append`, `text.splitlines`, `len`, `self.owner._logical`, `self.owner.CONVERTED_OBTAIN_CALC_PATTERN.match`, `output.append`, `NameNormalizer.normalize`, `match.group`, `NameNormalizer.to_cobol`, `self.owner._leading_spaces`, `self.owner._table_for_record`, `self.scanner.skip_generated_sql_and_sqlcode`, `output.extend`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L96: `if self._stands_down()`
- L97: `if self.owner.CONVERTED_OBTAIN_CALC_PATTERN.search(str(text or ''))`
- L106: `while index < len(lines)`
- L110: `if not match`
- L124: `if not table`
- L143: `if not key_columns`
- L168: `if changed`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
