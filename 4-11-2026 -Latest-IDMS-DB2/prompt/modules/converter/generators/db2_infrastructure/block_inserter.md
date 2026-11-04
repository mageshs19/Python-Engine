# `converter/generators/db2_infrastructure/block_inserter.py`

Source: [converter/generators/db2_infrastructure/block_inserter.py](../../../../../converter/generators/db2_infrastructure/block_inserter.py) | 107 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `51a514446dff70c366f0e14ba2de8e04134927d7eba120b215123a849ff7e42a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Inserts the generated block into DATA DIVISION and adds DCLGEN INITIALIZE.

## Import declarations

```python
from __future__ import annotations
import re
from converter.generators.db2_infrastructure.infrastructure_patterns import DATA_DIVISION_PATTERN, LINKAGE_SECTION_PATTERN, PROCEDURE_DIVISION_PATTERN, WORKING_STORAGE_PATTERN
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/generators/db2_infrastructure/infrastructure_patterns.py](infrastructure_patterns.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure_generator.py](../db2_infrastructure_generator.md)

## Symbol contracts and control points

### `BlockInserter` - L19-L107

```python
class BlockInserter()
```

### `BlockInserter.__init__` - L20-L21

```python
__init__(self, line_utils) -> None
```

### `BlockInserter.insert_in_data_division` - L23-L57

```python
insert_in_data_division(self, text: str, block: str) -> str
```

Observed calls (lexical order): `pattern.search`, `(text[:match.start()].rstrip() + '\n\n' + block.rstrip() + '\n\n' + text[match.start():].lstrip()).rstrip`, `match.start`, `text[:match.start()].rstrip`, `block.rstrip`, `text[match.start():].lstrip`, `WORKING_STORAGE_PATTERN.search`, `(text[:working_storage_match.end()].rstrip() + '\n\n' + block.rstrip() + '\n\n' + text[working_storage_matc...`, `text[:working_storage_match.end()].rstrip`, `working_storage_match.end`, `text[working_storage_match.end():].lstrip`, `DATA_DIVISION_PATTERN.search`, `(text[:data_division_match.end()].rstrip() + '\n\n' + 'WORKING-STORAGE SECTION.' + '\n\n' + block.rstrip() ...`, `data_division_match.end`, `text[:data_division_match.end()].rstrip`, `text[data_division_match.end():].lstrip`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L24: `for pattern in [LINKAGE_SECTION_PATTERN, PROCEDURE_DIVISION_PATTERN]`
- L26: `if match`
- L36: `if working_storage_match`
- L46: `if data_division_match`

### `BlockInserter.ensure_dclgen_initialization` - L59-L88

```python
ensure_dclgen_initialization(self, text: str, include_names: list[str]) -> str
```

Observed calls (lexical order): `self.line_utils.normalize_include_name`, `NameNormalizer.to_cobol`, `re.search`, `re.escape`, `missing_initializes.append`.

Control points:

- L69: `if not clean_include_names`
- L73: `for include_name in clean_include_names`
- L75: `if re.search(f'\\bINITIALIZE\\s+{re.escape(group_name)}\\b', text, flags=re.IGNORECASE)`
- L83: `if not missing_initializes`

### `BlockInserter._insert_after_procedure_division` - L90-L107

```python
_insert_after_procedure_division(self, text: str, block: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `output.append`, `self.line_utils.logical_line`, `PROCEDURE_DIVISION_PATTERN.match`, `'\n'.join`, `'\n'.join(output).rstrip`, `str(text or '').rstrip`.

Control points:

- L95: `for line in lines`
- L97: `if inserted`
- L100: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L104: `if inserted`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
