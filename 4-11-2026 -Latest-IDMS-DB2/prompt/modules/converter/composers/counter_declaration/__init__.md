# `converter/composers/counter_declaration/__init__.py`

Source: [converter/composers/counter_declaration/__init__.py](../../../../../converter/composers/counter_declaration/__init__.py) | 29 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `6fc7d11fe44af6f7796af43f7b4a0536860da683c50129e1fdeb58ef7d712fcf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Placement and rendering helpers for generated row counters.

## Module-level bindings

`__all__` (L23)

## Import declarations

```python
from converter.composers.counter_declaration.counter_anchor import CounterAnchor, CounterAnchorFinder
from converter.composers.counter_declaration.counter_anchor_resolver import CounterAnchorResolver
from converter.composers.counter_declaration.counter_line_factory import CounterLineFactory
from converter.composers.counter_declaration.counter_totals_writer import CounterTotalsWriter
```

## Local dependency notes

- [converter/composers/counter_declaration/counter_anchor.py](counter_anchor.md)
- [converter/composers/counter_declaration/counter_anchor_resolver.py](counter_anchor_resolver.md)
- [converter/composers/counter_declaration/counter_line_factory.py](counter_line_factory.md)
- [converter/composers/counter_declaration/counter_totals_writer.py](counter_totals_writer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration_writer.py](../counter_declaration_writer.md)

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
