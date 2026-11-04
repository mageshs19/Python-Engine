# `converter/composers/update_program_feedback_composer.py`

Source: [converter/composers/update_program_feedback_composer.py](../../../../converter/composers/update_program_feedback_composer.py) | 60 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `5ddea4af80a991687be8bae1c84ffe7c9b92947a474d7eb7b6d6cf798ee2ee0b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.composers.update_sql_cleanup_composer import UpdateSqlCleanupComposer
from converter.composers.update_program_structure_feedback_composer import UpdateProgramStructureFeedbackComposer
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
```

## Local dependency notes

- [converter/composers/update_program_structure_feedback_composer.py](update_program_structure_feedback_composer.md)
- [converter/composers/update_sql_cleanup_composer.py](update_sql_cleanup_composer.md)
- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `UpdateProgramFeedbackComposer` - L16-L60

```python
class UpdateProgramFeedbackComposer()
```

Public update-program feedback composer.

### `UpdateProgramFeedbackComposer.__init__` - L23-L42

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository, table_name_resolver: TableNameResolver, host_variable_resolver: HostVariableResolver) -> None
```

Observed calls (lexical order): `UpdateSqlCleanupComposer`, `UpdateProgramStructureFeedbackComposer`.

### `UpdateProgramFeedbackComposer.compose` - L44-L60

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `output.strip`, `self.sql_feedback.compose`, `self.messages.extend`, `self.structure_feedback.compose`, `output.rstrip`.

Control points:

- L51: `if not output.strip()`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
