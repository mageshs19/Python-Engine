# `converter/parsers/dclgen_parser.py`

Source: [converter/parsers/dclgen_parser.py](../../../../converter/parsers/dclgen_parser.py) | 135 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `d0bf13fc5ef1cf855dedc78deded3a9451e3b70729d837d4c8dc32ad5c0e5f6f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Parses DB2 DCLGEN text files.

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import DclgenColumn
from converter.parsers.base_text_parser import BaseTextParser
from converter.parsers.dclgen.cobol_host_field_parser import CobolHostFieldParser
from converter.parsers.dclgen.dclgen_column_merger import DclgenColumnMerger
from converter.parsers.dclgen.sql_declare_parser import SqlDeclareParser
from converter.parsers.dclgen.sql_name_normalizer import DclgenNameNormalizer
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/parsers/base_text_parser.py](base_text_parser.md)
- [converter/parsers/dclgen/cobol_host_field_parser.py](dclgen/cobol_host_field_parser.md)
- [converter/parsers/dclgen/dclgen_column_merger.py](dclgen/dclgen_column_merger.md)
- [converter/parsers/dclgen/sql_declare_parser.py](dclgen/sql_declare_parser.md)
- [converter/parsers/dclgen/sql_name_normalizer.py](dclgen/sql_name_normalizer.md)

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/input_loader.py](../ui/input_loader.md)
- [review/runner/workspace_inputs.py](../../review/runner/workspace_inputs.md)
- [runners/batch/shared_input_loader.py](../../runners/batch/shared_input_loader.md)
- [runners/retrieval/retrieval_input_loader.py](../../runners/retrieval/retrieval_input_loader.md)
- [runners/update/update_input_loader.py](../../runners/update/update_input_loader.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_parsers.py](../../tests/test_parsers.md)

## Symbol contracts and control points

### `DclgenParser` - L34-L135

```python
class DclgenParser(BaseTextParser)
```

### `DclgenParser.__init__` - L35-L38

```python
__init__(self) -> None
```

Observed calls (lexical order): `DclgenNameNormalizer`, `DclgenColumnMerger`.

### `DclgenParser.parse_many_texts` - L40-L63

```python
parse_many_texts(self, texts: list[str]) -> list[DclgenColumn]
```

Observed calls (lexical order): `len`, `self.diagnostics.append`, `enumerate`, `self.parse`, `output.extend`.

Control points:

- L49: `for (index, text) in enumerate(texts, start=1)`

### `DclgenParser.parse` - L65-L135

```python
parse(self, text: str, source_label: str='DCLGEN') -> list[DclgenColumn]
```

Observed calls (lexical order): `text.strip`, `self.diagnostics.append`, `self.clean_text`, `SqlDeclareParser`, `CobolHostFieldParser`, `sql_declare_parser.find_table_name`, `sql_declare_parser.parse_columns`, `cobol_field_parser.parse`, `self._merger.merge_sql_columns_with_cobol_hosts`, `len`, `self._merger.fallback_columns_from_cobol_fields`.

Control points:

- L70: `if not text or not text.strip()`
- L85: `if table_name`
- L104: `if sql_columns`
- L122: `if cobol_fields`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
