# `converter/transformers/qualified_reference_transformer.py`

Source: [converter/transformers/qualified_reference_transformer.py](../../../../converter/transformers/qualified_reference_transformer.py) | 65 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `d2663647e6ca31b1b7991a023905ec39db2946faaa4d832f9f696e9121704bed`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Qualified IDMS field reference transformer.

## Import declarations

```python
from patterns.field_usage_patterns import QUALIFIED_REFERENCE_PATTERN
from rules.field_mapping_rules import QUALIFIED_REFERENCE_REWRITE_RULES
```

## Local dependency notes

- [patterns/field_usage_patterns.py](../../patterns/field_usage_patterns.md)
- [rules/field_mapping_rules.py](../../rules/field_mapping_rules.md)

## Symbol contracts and control points

### `QualifiedReferenceTransformer` - L16-L65

```python
class QualifiedReferenceTransformer()
```

Rewrites qualified IDMS field references to DB2 DCLGEN host references when mapping metadata exists.

### `QualifiedReferenceTransformer.__init__` - L22-L28

```python
__init__(self, mapping_repository, dclgen_repository) -> None
```

### `QualifiedReferenceTransformer.transform_line` - L30-L40

```python
transform_line(self, line: str) -> str
```

Observed calls (lexical order): `QUALIFIED_REFERENCE_PATTERN.sub`.

Control points:

- L34: `if not line`

### `QualifiedReferenceTransformer._replace_reference` - L42-L65

```python
_replace_reference(self, match) -> str
```

Observed calls (lexical order): `match.group`, `self.mapping_repository.find_column_mapping`, `self.dclgen_repository.find_host_reference`.

Control points:

- L54: `if not mapped_column`
- L62: `if not host_reference`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
