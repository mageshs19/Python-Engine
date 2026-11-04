# `converter/pipeline/lrf_host_variable_population.py`

Source: [converter/pipeline/lrf_host_variable_population.py](../../../../converter/pipeline/lrf_host_variable_population.py) | 169 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `c12bc3059381e24b56eb79ba4327bb6f23dc3c5c11842631cdbeaf8042419f25`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Orchestrates LRF host variable population integration into the pipeline.

## Import declarations

```python
from __future__ import annotations
from typing import Optional
from converter.generators.lrf_host_variable_populator import LrfHostVariablePopulator
```

## Local dependency notes

- [converter/generators/lrf_host_variable_populator.py](../generators/lrf_host_variable_populator.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `setup_lrf_host_variable_population` - L47-L101

```python
setup_lrf_host_variable_population(cursor_paragraph_generator, host_variable_resolver=None, table_name_resolver=None, cursor_name_resolver=None, relationship_resolver=None, name_normalizer=None, lrf_path_resolver=None, lrf_repository=None) -> bool
```

Configure LRF host variable population in the cursor generator.

Observed calls (lexical order): `LrfHostVariablePopulator`.

Control points:

- L76: `if not cursor_paragraph_generator`

### `augment_with_lrf_population` - L104-L137

```python
augment_with_lrf_population(cursor_paragraph_generator, cobol_text: str) -> tuple[str, list[str]]
```

Apply LRF host variable population to generated COBOL.

Observed calls (lexical order): `getattr`, `populator.augment_procedure_division`.

Control points:

- L115: `if not cursor_paragraph_generator`
- L123: `if not populator`

### `LrfHostVariablePopulationMixin` - L140-L169

```python
class LrfHostVariablePopulationMixin()
```

Mixin to add LRF host variable population to CursorParagraphGenerator.

Declared class/data-model fields:

```python
_lrf_host_variable_populator: Optional[LrfHostVariablePopulator] = None
_table_name_resolver = None
_cursor_name_resolver = None
```

### `LrfHostVariablePopulationMixin.augment_lrf_procedure_division` - L153-L169

```python
augment_lrf_procedure_division(self, cobol_text: str) -> tuple[str, list[str]]
```

Apply LRF host variable population after main generation.

Observed calls (lexical order): `self._lrf_host_variable_populator.augment_procedure_division`.

Control points:

- L164: `if not self._lrf_host_variable_populator`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
