# `converter/resolvers/cursor_name_resolver.py`

Source: [converter/resolvers/cursor_name_resolver.py](../../../../converter/resolvers/cursor_name_resolver.py) | 88 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `d648f316852c8f3e9a66fccd7bb8b3f5d1768591df30c78b17024eb53ab271d4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from catalogs.db2_naming_catalog import DB2_CURSOR_SUFFIX, DB2_DEFAULT_CURSOR_NAME
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_rules import cursor_paragraph_number
```

## Local dependency notes

- [catalogs/db2_naming_catalog.py](../../catalogs/db2_naming_catalog.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/cursor_rules.py](../../rules/cursor_rules.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](../analyzers/program_flow/flow_cursor_loop_scanner.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](../analyzers/program_flow/program_flow_analyzer.md)
- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/services/program_cursor_loop_analyzer.py](../services/program_cursor_loop_analyzer.md)
- [converter/services/program_flow_analyzer.py](../services/program_flow_analyzer.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../tests/test_generic_cursor_numbering_and_perform_integrity.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `CursorNameResolver` - L6-L88

```python
class CursorNameResolver()
```

Resolves cursor names and cursor paragraph names.

### `CursorNameResolver.cursor_name_from_table` - L15-L29

```python
cursor_name_from_table(self, table_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self._remove_table_suffix`, `NameNormalizer.to_cobol`.

Control points:

- L21: `if not table`
- L26: `if not base`

### `CursorNameResolver.paragraph_names` - L31-L42

```python
paragraph_names(self, cursor_order: int, cursor_name: str) -> dict[str, str]
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `cursor_paragraph_number`.

### `CursorNameResolver.paragraph_numbers` - L44-L52

```python
paragraph_numbers(self, cursor_order: int) -> dict[str, int]
```

Observed calls (lexical order): `cursor_paragraph_number`.

### `CursorNameResolver.cursor_spec` - L54-L74

```python
cursor_spec(self, cursor_order: int, table_name: str) -> dict[str, str | int]
```

Observed calls (lexical order): `self.cursor_name_from_table`, `self.paragraph_names`, `self.paragraph_numbers`.

### `CursorNameResolver._remove_table_suffix` - L76-L88

```python
_remove_table_suffix(self, table_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `table.endswith`.

Control points:

- L82: `if table.endswith('_TV') or table.endswith('_TB')`
- L85: `if table.endswith('TV') or table.endswith('TB')`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
