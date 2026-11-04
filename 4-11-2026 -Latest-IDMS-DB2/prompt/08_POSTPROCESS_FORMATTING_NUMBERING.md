# Finishing passes, fixed format and paragraph numbering

## Layout subphase versus final output

`ConversionLayoutPipeline.finish` runs layout/style/fixed-format work, output
write extraction, late date conversion, record materialization, counter
creation, restart injection, unmapped-block handling, structural safety,
indentation, MOVE alignment, paragraph separation, resequencing, comment cleanup
and the enhancement pipeline. Its enhancement exception is recorded and that
pass is skipped; it is not guaranteed success.

The shared content pipeline then performs more cursor/flow/schema work. Final
procedure indentation, SQL Area B alignment and sequence generation run after
those content changes. A correct earlier indent pass cannot align statements
that did not yet exist. Update/retrieval runners can also apply route-specific
processing after service return; inspect their writers when changing final output.

## Fixed-format contract

Treat sequence area, indicator, source body and identification area separately.
Keep comments and literals intact. Reflow logical statements using valid
continuations rather than dropping text at a width boundary. Final 80-character
records are a formatting check, not proof of valid COBOL syntax or valid data.
Reference-modification qualification, periods, END-IF/END-PERFORM and embedded SQL
boundaries remain compiler-sensitive.

## Numbering and procedure control

Source business paragraph names and physical order are preserved unless a
source-proven flow transformation requires otherwise. Numeric prefixes are part
of names; they do not themselves schedule execution. Every changed definition
requires coordinated reference updates, and PERFORM THRU depends on the physical
span between labels. An external INCLUDE target remains unproved without its body.

`CursorParagraphNumberingComposer` owns generated cursor labels. The active
`rules/cursor_rules.py` convention starts OPEN/FETCH/CLOSE at 2100/2200/2300,
then advances the next cursor by a 1000-slot stride. The timestamp helper may be
`600-GET-TIMESTAMP`. These are actual configuration conventions, not mandates to
rename all business paragraphs to a universal 0000/1000/2000/3000 skeleton.

`FinalGeneratedOutputService` is called with `standardize_lifecycle=False` in the
main pipeline. A legacy lifecycle standardizer existing in a module is not proof
that it runs in this path. Do not resurrect the old 300-slot or 6000-timestamp
claims from deleted historical documentation.

## Source map

- [Layout phase](modules/converter/pipeline/conversion/conversion_layout_pipeline.md)
- [Layout steps](modules/converter/pipeline/conversion/conversion_layout_steps.md)
- [Final output](modules/converter/services/final_generated_output_service.md)
- [Cursor numbering](modules/converter/composers/cursor_paragraph_numbering_composer.md)
- [Cursor conventions](modules/rules/cursor_rules.md)
- [Procedure indentation](modules/converter/composers/procedure_indent_normalizer.md)
- [SQL alignment](modules/converter/composers/sql_body_area_b_normalizer.md)
- [Final resequencing](modules/converter/services/final_sequence_resequencer_service.md)

## V129 resolved diagnostic cleanup
FinalGeneratedOutputService removes only its exact generated undefined-ERROR-STATUS warning and its known continuation after no executable ERROR-STATUS identifier remains. Quoted literals and comments do not count as executable references. Other warning types are retained. This runs after status transformations and before resequencing.
