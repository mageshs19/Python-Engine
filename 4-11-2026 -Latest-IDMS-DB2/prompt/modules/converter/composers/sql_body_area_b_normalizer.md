# `converter/composers/sql_body_area_b_normalizer.py`

Source: [converter/composers/sql_body_area_b_normalizer.py](../../../../converter/composers/sql_body_area_b_normalizer.py) | 45 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `335e6061ca0fbd7732165c337b2c9a5286b1b0d2d67b77b1d63ecb541262ef7a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Normalize SQL body geometry after late SQL generation, without editing tokens.

## Module-level bindings

`__all__` (L45)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_schema_driven_4310_generic_rules.py](../../tests/test_schema_driven_4310_generic_rules.md)

## Symbol contracts and control points

### `SqlBodyAreaBNormalizer` - L10-L43

```python
class SqlBodyAreaBNormalizer()
```

### `SqlBodyAreaBNormalizer.__init__` - L11-L13

```python
__init__(self, min_indent=4)
```

### `SqlBodyAreaBNormalizer.compose` - L15-L43

```python
compose(self, text)
```

Observed calls (lexical order): `self.messages.clear`, `text.splitlines`, `len`, `line[72:80].isdigit`, `line[:6].isdigit`, `output.append`, `body.strip`, `body.strip().upper`, `re.match`, `body.lstrip`, `newbody.ljust`, `re.search`, `self.messages.append`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L17: `if not text`
- L19: `for line in text.splitlines()`
- L21: `if not is_fixed or line[6] in ('*', '/', 'D', 'd')`
- L25: `if re.match('^PROCEDURE\\s+DIVISION\\b', upper)`
- L27: `if in_procedure and re.match('^EXEC\\s+SQL\\b', upper)`
- L29: `if in_sql and upper and (not re.match('^END-EXEC\\b', upper))`
- L31: `if leading < self.min_indent`
- L33: `if len(newbody) <= 65`
- Another 3 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
