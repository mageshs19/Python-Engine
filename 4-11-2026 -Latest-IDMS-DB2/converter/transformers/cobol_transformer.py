# LOCATION: converter/transformers/cobol_transformer.py
# ACTION: REPLACE ENTIRE FILE
"""Converts IDMS COBOL statements to DB2-compatible COBOL.

Responsibilities are delegated to focused helper classes while keeping the
existing public API unchanged.

CORRECTION 1 - the IDMS-ABORT paragraph BODY survived its header
-----------------------------------------------------------------
The source carries

    EINDE-PROGRAMMA-EXIT.
        EXIT.
    /
    IDMS-ABORT.                     <- header
        CLOSE FORM.                 <- body
        COPY IDMS IDMS-STATUS.      <- body

Only the header was removed. CLOSE FORM was left stranded after a
paragraph EXIT, and StructuralSafetyComposer then correctly commented it
as unreachable:

    *DB2-KEEP: statement follows a paragraph EXIT and is unreachable.
    *DB2-KEEP CLOSE FORM.

The safety pass was right; the removal was incomplete. The manual
reference deletes the whole paragraph. Skipping now runs to the next
paragraph header, section header or division boundary, so no business
line can be swallowed, and a blast-radius cap reverts to normal
processing if the boundary is never found.

CORRECTION 2 - PROGRAM-NAME disagreed with PROGRAM-ID
------------------------------------------------------
PROGRAM-ID was rewritten to the derived DB2 id while

    MOVE 'VM7BD200' TO PROGRAM-NAME.

kept the source id, so the job log and every abend message named a
program that no longer exists. The manual reference carries
MOVE 'VMDZ7200' TO PROGRAM-NAME.

ProgramNameSyncService already performs this rewrite safely - it reads
the FINAL PROGRAM-ID out of the converted text and touches only a
MOVE literal TO PROGRAM-NAME. It was simply never called. It runs as the
last pass, AFTER fix_program_id_period, so the id it reads is final.

The same id survived in a SECOND place, measured on VMDZ7200 line 442:

    DISPLAY 'VM7BD200: ** DATE ARCHIVAGE NOT OK **'

A MOVE rewrite cannot reach a DISPLAY literal, so the abend message -
the one line an operator reads when the job fails - still named the
source program. sync() now also derives any VM<site>?BD<tail> token
found INSIDE a quoted literal, delegating the transform to
NameDerivationResolver, the single owner of that rule. The derived name
is always the same length as the source name, so no literal can grow
and no line can overflow column 72.

CORRECTION 3 - a second copy of Converter 4 was pasted into this class
-----------------------------------------------------------------------
A ``_convert_status_abort_perform`` method was added at the end of
CobolTransformer. It referenced six names this module does not own:

    IDMS_STATUS_PERFORM_PATTERN   not imported here
    IDMS_ABORT_PERFORM_PATTERN    not imported here
    text / statement / division   local variables that were never bound
    self._remove                  a method of IdmsStatementTransformer

The real Converter 4 lives in the idms_statement package, alongside the
BIND / READY / CONNECT / DISCONNECT / FIND CURRENT converters and the
``_remove`` and ``_division`` helpers it depends on. CobolTransformer
reaches it the way it reaches every other IDMS converter - through

    self.idms_statement_transformer.transform_line(...)

Two copies of one converter is the same defect class as a constant
declared twice: editing the dead copy changes nothing and reads like a
tooling fault. There is now ONE owner of PERFORM IDMS-STATUS /
IDMS-ABORT / IDMS-STOP removal, and it is not this file.

CORRECTION 4 - two passes ran SILENTLY
----------------------------------------
``IdmsResidualCleanup.removed_field_lines`` and
``ProgramNameSyncService.sync`` were both wired into this method, but
neither collector was reset and neither was drained. Two consequences:

  - a removal, a rename or a refusal was invisible in the run log,
    which is precisely what CHK-29.05 ("LR-STATUS replacement should be
    documented") reports as a failure, and

  - ONE instance of each helper is built in __init__ and reused for
    every program, so in a batch run the second program inherited the
    first program's messages and the log named fields and ids that the
    second program never contained.

``reset()`` is called for both with the other per-transformation state,
and ``messages`` is drained into ``validation_messages`` - the residual
cleanup immediately after the line loop, the name sync immediately
after it runs. That is the same contract every composer in the pipeline
already honours.

CORRECTION 5 - THE STATEMENT TRANSFORMER WAS NEVER RESET OR DRAINED
--------------------------------------------------------------------
``IdmsStatementTransformer.reset()`` carries this instruction::

    MUST be called once per program by CobolTransformer.transform(),
    before the first transform_line(). Without it a batch run carries
    one program's diagnostics and unmapped records into the next.

CORRECTION 4 added exactly that call for ``residual_cleanup`` and
``program_name_sync`` - and not for the statement transformer, which is
the component the instruction names. One instance is built in
ConversionComponentFactory and reused for every program in the folder,
so across a six-program run ``unmapped_records`` and ``messages``
accumulated from the first program to the last. A record that had no
DB2 target in program 1 was still listed as unmapped while program 6
was converting.

Its ``messages`` were never drained either, so every
``_keep_and_comment_unmapped`` refusal - the diagnostic that explains
why an IDMS access was left as a comment instead of becoming SQL - went
nowhere. That is the same defect as CORRECTION 4, in the same method,
on the one collaborator CORRECTION 4 missed.

BLAST RADIUS, STATED PLAINLY: draining ``messages`` only lengthens the
run log and cannot change generated COBOL. Calling ``reset()`` CAN:
programs 2..n no longer inherit earlier unmapped records, so a record
that was being commented purely because an earlier program could not
map it will stop being commented. Diff every program against the frozen
baseline after applying this.

CORRECTION 6 - NO SEAM FOR BLOCK-LEVEL ANALYSIS
------------------------------------------------
``IdmsStatementTransformer`` converts ONE LINE at a time and receives
only (line, division, sql_error_paragraph). It therefore cannot tell an
LR WALK from an LR BOUNDED SEARCH, because that is a property of the
enclosing PERFORM UNTIL, and it mapped every OBTAIN FIRST / NEXT to a
cursor unconditionally.

This method is the only place that holds the whole expanded program AND
the transformer instance, so it is the correct seam. An optional
``lr_access_analyser`` collaborator is read ONCE per program, before the
line loop, and its result is published onto the transformer in the same
shape ``unmapped_records`` already uses.

The collaborator defaults to None, so a build that does not supply one
behaves exactly as before - the transformer sees an empty mapping and
every OBTAIN keeps the cursor path.

DO NOT WIRE AN ANALYSER UNTIL THE LOOP-REMOVAL PASS EXISTS. When a
record is classified as a bounded search the in-loop OBTAIN NEXT becomes
a comment, which leaves the program's own PERFORM UNTIL with an empty
body and an unchanging condition - an infinite loop at run time.
"""

from __future__ import annotations

import re

from converter.domain.models import IdmsOperation
from converter.parsers.cobol_parser import CobolParser
from converter.services.program_name_sync_service import (
    ProgramNameSyncService,
)
from converter.transformers.cobol_identification_transformer import (
    CobolIdentificationTransformer,
)
from converter.transformers.cobol_program_id_transformer import (
    CobolProgramIdTransformer,
)
from converter.transformers.cobol_transformed_line_merger import (
    CobolTransformedLineMerger,
)
from converter.transformers.cobol_transformer_line_utils import (
    CobolTransformerLineUtils,
)
from converter.transformers.idms_residual_cleanup import IdmsResidualCleanup
from converter.transformers.idms_statement_transformer import (
    IdmsStatementTransformer,
)

# DIVISION_PATTERN is imported from cobol_patterns, NOT from
# final_feedback_fix_patterns. Both modules declare a name spelled that
# way; only the cobol_patterns form carries the capture group that
# `division_match.group(1)` below depends on. Do not "tidy" this import.
from patterns.cobol_patterns import DIVISION_PATTERN
from patterns.db2_patterns import SQL_ERROR_PARAGRAPH_PATTERN
from patterns.final_feedback_fix_patterns import (
    DIVISION_SECTION_HEADER_PATTERN,
    PARAGRAPH_HEADER_PATTERN,
)
from patterns.cobol_transformer_patterns import (
    EXIT_LINE_PATTERN,
    IDMS_ABORT_PARAGRAPH_PATTERN,
)
from rules.cobol_statement_rules import NON_PARAGRAPH_SINGLE_WORDS
from rules.cobol_transformer_rules import (
    DB2_COMPILER_OPTION_LINE,
    DEFAULT_SQL_ERROR_PARAGRAPH,
)

# Attribute the bounded-search mapping is published under. The reading
# end declares the same name; keeping it in one place is what stops the
# producer and the consumer drifting apart.
BOUNDED_SEARCH_ATTRIBUTE = "bounded_search_records"

ANALYSER_FAILED_TEMPLATE = (
    "LR access analysis: skipped, every OBTAIN keeps the cursor path. "
    "Reason: {reason}"
)
ANALYSER_RESULT_TEMPLATE = (
    "LR access analysis: {count} record(s) classified as a bounded "
    "search ({records})."
)


class CobolTransformer:
    """Converts IDMS COBOL statements to DB2-compatible COBOL."""

    def __init__(
        self,
        idms_statement_transformer: IdmsStatementTransformer,
        lr_access_analyser=None,
    ) -> None:
        self.idms_statement_transformer = idms_statement_transformer

        # Optional. None -> no bounded-search classification is made and
        # the statement transformer behaves exactly as before.
        # See CORRECTION 6.
        self.lr_access_analyser = lr_access_analyser

        self.parser = CobolParser()

        self.line_utils = CobolTransformerLineUtils()
        self.program_id_transformer = CobolProgramIdTransformer(
            line_utils=self.line_utils,
        )
        self.identification_transformer = CobolIdentificationTransformer(
            line_utils=self.line_utils,
        )
        self.program_name_sync = ProgramNameSyncService()
        self.residual_cleanup = IdmsResidualCleanup()
        self.line_merger = CobolTransformedLineMerger(
            line_utils=self.line_utils,
        )
        self._in_working_storage = False

    # =================================================================
    # Public entry point
    # =================================================================
    def transform(
        self,
        cobol_text: str,
        target_program_id: str = "",
    ) -> tuple[str, list[str], list[IdmsOperation]]:
        operations = self.parser.analyze(cobol_text)

        validation_messages: list[str] = []
        output_lines: list[str] = []
        compiler_option_seen = False
        current_division = ""
        sql_error_paragraph = self._detect_sql_error_paragraph(cobol_text)

        # ---- Per-transformation state.
        #
        # residual_cleanup, program_name_sync and the statement
        # transformer are built ONCE and reused for every program, so
        # their collectors must be emptied here. Without this a batch run
        # reports program 1's removals, renames and unmapped records
        # against program 2. See CORRECTION 4 and CORRECTION 5.
        self._in_working_storage = False
        self.residual_cleanup.reset()
        self.program_name_sync.reset()
        self._reset_statement_transformer()

        # ---- Block-level classification, once, before the line loop.
        self._publish_bounded_search_records(
            cobol_text=cobol_text,
            validation_messages=validation_messages,
        )

        for raw_line in str(cobol_text or "").splitlines():
            line = raw_line.rstrip()
            # Preserve fixed-format comment/debug records before stripping
            # sequence/indicator columns. Otherwise a line such as
            # "019000*= STORE VMBEVEF" becomes logical text containing a
            # STORE token and is incorrectly converted into a second INSERT.
            if self._is_source_comment_record(line):
                output_lines.append(line)
                continue

            logical = self.line_utils.logical_line(line)
            logical_stripped = logical.strip()

            if not logical_stripped:
                output_lines.append(line)
                continue

            if self._is_cbl_line(logical_stripped):
                compiler_option_seen = True
                validation_messages.append(
                    f"Compiler option: replaced '{logical_stripped}' with "
                    f"{DB2_COMPILER_OPTION_LINE}."
                )
                output_lines.append(
                    self.line_utils.replace_logical_body(
                        original_line=line,
                        replacement_body=DB2_COMPILER_OPTION_LINE,
                    )
                )
                continue

            # Preserve the IDMS-ABORT paragraph label and let the ordinary
            # statement pipeline convert/remove only IDMS-specific statements
            # inside it. Some source programs place valid COBOL cleanup there
            # (for example CLOSE FORM); deleting the whole block changes cleanup
            # behavior and breaks original paragraph-order parity.

            program_id_line = self.program_id_transformer.program_id_replacement(
                original_line=line,
                logical_line=logical_stripped,
                target_program_id=target_program_id,
            )

            if program_id_line is not None:
                output_lines.append(program_id_line)
                continue

            author_line = self.identification_transformer.author_replacement(
                original_line=line,
                logical_line=logical_stripped,
            )

            if author_line is not None:
                output_lines.append(author_line)
                continue

            date_written_line = self.identification_transformer.date_written_replacement(
                original_line=line,
                logical_line=logical_stripped,
            )

            if date_written_line is not None:
                output_lines.append(date_written_line)
                continue

            division_match = DIVISION_PATTERN.match(logical_stripped)

            if division_match:
                current_division = division_match.group(1).upper()
                self._in_working_storage = False
                output_lines.append(line)
                continue

            # Track WORKING-STORAGE section entry. IDMS declarative lines
            # such as "IDMS-RECORDS WITHIN WORKING-STORAGE SECTION." must not
            # be captured here; they fall through to the residual cleanup.
            if (
                "WORKING-STORAGE" in logical_stripped.upper()
                and "SECTION" in logical_stripped.upper()
                and not self.residual_cleanup.is_idms_declarative_or_control(
                    logical_stripped
                )
            ):
                self._in_working_storage = True
                output_lines.append(line)
                continue

            # Track section changes within a division. IDMS control/schema
            # sections are left for the residual cleanup below to remove.
            if (
                "SECTION" in logical_stripped.upper()
                and "WORKING-STORAGE" not in logical_stripped.upper()
                and not self.residual_cleanup.is_idms_declarative_or_control(
                    logical_stripped
                )
            ):
                self._in_working_storage = False
                output_lines.append(line)
                continue

            # Apply COMP-3 and FILLER cleaning to WORKING-STORAGE data
            # declarations.
            if self._in_working_storage and "PIC" in logical_stripped and any(
                marker in logical_stripped
                for marker in [
                    "COMP-3",
                    "COMP-2",
                    "COMP-1",
                    "COMPUTATIONAL",
                    "FILLER",
                    "PACKED",
                ]
            ):
                cleaned_line = self._clean_data_declaration_line(line)
                if cleaned_line is not None:  # Only append if not removed
                    output_lines.append(cleaned_line)
                continue

            if self.residual_cleanup.is_idms_declarative_or_control(
                logical_stripped
            ):
                output_lines.extend(
                    self.residual_cleanup.removed_declarative_lines(
                        logical_stripped
                    )
                )
                continue

            if self.residual_cleanup.is_idms_executable_cleanup(
                logical_stripped
            ):
                output_lines.extend(
                    self.residual_cleanup.removed_executable_lines(
                        logical_line=logical_stripped,
                        current_division=current_division,
                    )
                )
                continue

            # A source-proven hand-written retrieval OBTAIN CALC owns the
            # immediately following ERROR-STATUS guards. Give that narrow
            # scope to the statement transformer before generic orphan-field
            # cleanup comments those lines out. All other residual IDMS status
            # references continue through the existing cleanup path.
            if (
                getattr(self.idms_statement_transformer, "_active_handwritten_calc_record", "")
                and "ERROR-STATUS" in logical_stripped.upper()
            ):
                scoped_lines, _scoped_set = self.idms_statement_transformer.transform_line(
                    line=logical_stripped,
                    current_division=current_division,
                    sql_error_paragraph=sql_error_paragraph,
                )
                if self.line_merger.transformer_changed_line(
                    original_logical=logical_stripped,
                    transformed_lines=scoped_lines,
                ):
                    output_lines.extend(
                        self.line_merger.merge_transformed_lines_with_original_style(
                            original_line=line,
                            original_logical=logical_stripped,
                            transformed_lines=scoped_lines,
                        )
                    )
                    continue

            # Orphaned copybook-field references. COPY_IDMS_PATTERN
            # removed the member that declared LR-STATUS / ERROR-STATUS
            # / DML-SEQUENCE; this catches what that deletion orphans.
            # Its diagnostics are drained after the loop - CORRECTION 4.
            if self.residual_cleanup.references_removed_field(
                logical_stripped
            ):
                output_lines.extend(
                    self.residual_cleanup.removed_field_lines(
                        logical_stripped
                    )
                )
                continue

            # Every IDMS statement converter - including Converter 4,
            # which removes PERFORM IDMS-STATUS / IDMS-ABORT / IDMS-STOP -
            # is reached through this one call. See CORRECTION 3.
            transformed_lines, _opened_set = (
                self.idms_statement_transformer.transform_line(
                    line=logical_stripped,
                    current_division=current_division,
                    sql_error_paragraph=sql_error_paragraph,
                )
            )

            if self.line_merger.transformer_changed_line(
                original_logical=logical_stripped,
                transformed_lines=transformed_lines,
            ):
                output_lines.extend(
                    self.line_merger.merge_transformed_lines_with_original_style(
                        original_line=line,
                        original_logical=logical_stripped,
                        transformed_lines=transformed_lines,
                    )
                )
            else:
                output_lines.append(line)

        # ---- Drain the cleanup diagnostics.
        #
        # Drained here, AFTER the loop, because every removal and every
        # refusal must reach the run log. A pass that silently deletes
        # generated output cannot be reviewed. See CORRECTION 4 and
        # CORRECTION 5.
        validation_messages.extend(self.residual_cleanup.messages)
        validation_messages.extend(
            list(getattr(self.idms_statement_transformer, "messages", []) or [])
        )

        if not compiler_option_seen:
            self._ensure_compiler_option(output_lines, validation_messages)

        converted_text = "\n".join(output_lines).rstrip() + "\n"

        # IDMS-ABORT is not a DB2 runtime hook. Once IDMS statements have
        # been converted, remove only an empty/EXIT-only IDMS-ABORT paragraph.
        # Keep it when it still contains real COBOL cleanup (for example
        # CLOSE FORM), or when another paragraph explicitly branches to it.
        converted_text = self._remove_empty_idms_abort_paragraph(converted_text)

        converted_text = self.program_id_transformer.fix_program_id_period(
            text=converted_text,
            target_program_id=target_program_id,
        )

        # PROGRAM-NAME must agree with the FINAL PROGRAM-ID, so this runs
        # last. Safe by construction: ProgramNameSyncService reads the id
        # out of the converted text, rewrites only a
        # MOVE literal TO PROGRAM-NAME, and derives any VM..BD.. id found
        # INSIDE a quoted literal. The derived name is the same length as
        # the source name, so the fixed-format geometry is untouched and
        # no resequencing is needed. See CORRECTION 2.
        converted_text = self.program_name_sync.sync(converted_text)
        validation_messages.extend(self.program_name_sync.messages)

        return converted_text, validation_messages, operations

    # =================================================================
    # Per-program collaborator state
    # =================================================================
    def _remove_empty_idms_abort_paragraph(self, text: str) -> str:
        """Remove or neutralize residual IDMS-ABORT paragraph labels.

        IDMS-ABORT is a legacy runtime hook, not a DB2 paragraph name. The
        source estate contains blank/EXIT-only instances and instances with
        real cleanup statements. Empty unreferenced blocks are removed;
        blocks with executable cleanup are retained under a neutral COBOL
        label. Any surviving explicit branch to the old label is redirected
        to the neutral label. No program names or paragraph numbers are
        hardcoded, and valid cleanup statements are never deleted here.
        """
        original = str(text or "")
        lines = original.splitlines()
        if not lines:
            return original

        def logical(raw: str) -> str:
            return self.line_utils.logical_line(raw).strip()

        # Conservative paragraph-header recognizer. Exclude common COBOL
        # verbs so EXIT. or CONTINUE. cannot be mistaken for a paragraph.
        statement_verbs = {
            "ACCEPT", "ADD", "CALL", "CLOSE", "COMPUTE", "CONTINUE",
            "DELETE", "DISPLAY", "DIVIDE", "ELSE", "END-CALL", "END-IF",
            "END-PERFORM", "END-READ", "END-SEARCH", "END-WRITE", "ENTRY",
            "EVALUATE", "EXIT", "EXEC", "GOBACK", "IF", "INITIALIZE",
            "INSPECT", "MERGE", "MOVE", "MULTIPLY", "OPEN", "PERFORM",
            "READ", "REWRITE", "SEARCH", "SET", "SORT", "START",
            "STOP", "STRING", "SUBTRACT", "UNSTRING", "WHEN", "WRITE",
        }

        def is_paragraph_header(index: int) -> bool:
            value = logical(lines[index])
            if not value or value.startswith(("*", "/")):
                return False
            if not re.fullmatch(r"[A-Z0-9][A-Z0-9-]*\.", value, re.IGNORECASE):
                return False
            return value[:-1].upper() not in statement_verbs

        abort_indexes = [
            i for i, line in enumerate(lines)
            if IDMS_ABORT_PARAGRAPH_PATTERN.match(logical(line))
        ]
        if not abort_indexes:
            return original

        # Pick a neutral name that does not collide with an existing
        # paragraph. A neutral label preserves ordinary COBOL cleanup while
        # removing the legacy IDMS hook name from generated DB2 source.
        used_names = {logical(line).upper().rstrip(".") for line in lines}
        neutral_name = "ABORT-CLEANUP"
        suffix = 2
        while neutral_name.upper() in used_names:
            neutral_name = f"ABORT-CLEANUP-{suffix}"
            suffix += 1

        remove_indexes: set[int] = set()
        rename_indexes: set[int] = set()
        for index in abort_indexes:
            end = index + 1
            while end < len(lines) and not is_paragraph_header(end):
                end += 1

            substantive = []
            exit_indexes = []
            for body_index in range(index + 1, end):
                value = logical(lines[body_index])
                if not value or value.startswith(("*", "/")):
                    continue
                if EXIT_LINE_PATTERN.match(value):
                    exit_indexes.append(body_index)
                    continue
                substantive.append(value)

            # Check references outside the declaration itself. Comments are
            # excluded so a documentation mention cannot keep a dead label.
            reference_pattern = re.compile(
                r"\b(?:PERFORM|GO\s+TO|THRU|THROUGH)\s+IDMS-ABORT\b",
                flags=re.IGNORECASE,
            )
            has_reference = any(
                i != index
                and not self._is_source_comment_record(line)
                and reference_pattern.search(logical(line))
                for i, line in enumerate(lines)
            )

            if not substantive and not has_reference:
                remove_indexes.add(index)
                remove_indexes.update(exit_indexes)
            else:
                rename_indexes.add(index)

        if not remove_indexes and not rename_indexes:
            return original

        result: list[str] = []
        for i, line in enumerate(lines):
            if i in remove_indexes:
                continue
            if i in rename_indexes:
                result.append(
                    self.line_utils.replace_logical_body(
                        original_line=line,
                        replacement_body=f"{neutral_name}.",
                    )
                )
                continue
            if not self._is_source_comment_record(line):
                logical_line = logical(line)
                if re.search(r"\b(?:PERFORM|GO\s+TO|THRU|THROUGH)\s+IDMS-ABORT\b", logical_line, re.IGNORECASE):
                    logical_line = re.sub(
                        r"\b(IDMS-ABORT)\b",
                        neutral_name,
                        logical_line,
                        flags=re.IGNORECASE,
                    )
                    result.append(
                        self.line_utils.replace_logical_body(
                            original_line=line,
                            replacement_body=logical_line,
                        )
                    )
                    continue
            result.append(line)

        return "\n".join(result) + ("\n" if original.endswith("\n") else "")

    def _reset_statement_transformer(self) -> None:
        """Clear the statement transformer's per-program state.

        Tolerates a transformer without reset() so a stub or an older
        build still runs; the attributes it owns are cleared directly in
        that case rather than left to accumulate. See CORRECTION 5.
        """
        transformer = self.idms_statement_transformer

        reset = getattr(transformer, "reset", None)
        if callable(reset):
            reset()
            return

        if hasattr(transformer, "messages"):
            transformer.messages = []
        if hasattr(transformer, "unmapped_records"):
            transformer.unmapped_records = set()

    def _publish_bounded_search_records(
        self,
        *,
        cobol_text: str,
        validation_messages: list[str],
    ) -> None:
        """Classify LR accesses once, then hand the result to the line pass.

        Always leaves the attribute DEFINED, so the reading end never has
        to distinguish "no analyser" from "analyser found nothing" by the
        absence of an attribute. Never raises: a failed classification
        falls back to the cursor path for every record and says so.
        See CORRECTION 6.
        """
        transformer = self.idms_statement_transformer
        setattr(transformer, BOUNDED_SEARCH_ATTRIBUTE, {})

        if self.lr_access_analyser is None:
            # Cursor conversion is the conservative fallback. Make the
            # missing block-level classifier visible whenever this program
            # actually contains expanded LRF access markers; otherwise a
            # reviewer can mistake a fallback cursor for a deliberate LR
            # access plan. Do not enable singleton/bounded-search rendering
            # until executable SELECT generation and safe loop removal exist.
            if "*DB2: EXPANDED LRF" in str(cobol_text or "").upper():
                validation_messages.append(
                    "LR access analysis: no source-level analyser is wired; "
                    "the post-layout bounded-search pass will rewrite only a "
                    "fully proven inline cursor loop, otherwise it retains the cursor."
                )
            return

        try:
            found = self.lr_access_analyser.bounded_searches(cobol_text)
        except Exception as exc:  # noqa: BLE001
            validation_messages.append(
                ANALYSER_FAILED_TEMPLATE.format(reason=exc)
            )
            return

        records = dict(found or {})
        validation_messages.extend(
            list(getattr(self.lr_access_analyser, "messages", []) or [])
        )

        # Analysis is wired, but source-line rendering is not enabled until
        # its loop-removal owner can prove all business work is preserved.
        # Publishing records while either gate is off would let the line-level
        # converter replace OBTAIN NEXT but leave its PERFORM loop in place.
        from rules.lr_access_rules import (
            ENABLE_BOUNDED_SEARCH_RENDERING,
            ENABLE_LOOP_REMOVAL,
        )
        if ENABLE_BOUNDED_SEARCH_RENDERING and ENABLE_LOOP_REMOVAL:
            setattr(transformer, BOUNDED_SEARCH_ATTRIBUTE, records)
        else:
            setattr(transformer, BOUNDED_SEARCH_ATTRIBUTE, {})
            if records:
                validation_messages.append(
                    "LR access analysis found bounded-search candidate(s) "
                    f"({', '.join(sorted(records))}), but source-level rendering "
                    "is disabled; the post-layout safety rewriter owns any "
                    "proven singleton conversion."
                )

        if records:
            validation_messages.append(
                ANALYSER_RESULT_TEMPLATE.format(
                    count=len(records),
                    records=", ".join(sorted(records)),
                )
            )

    # =================================================================
    # Helpers
    # =================================================================
    @staticmethod
    def _is_source_comment_record(line: str) -> bool:
        """Recognize comments before fixed-format columns are stripped."""
        text = str(line or "")
        if len(text) >= 7 and text[:6].isdigit():
            return text[6] in ("*", "/", "D", "d")
        stripped = text.lstrip()
        return stripped.startswith(("*", "/"))

    def _is_cbl_line(
        self,
        logical_line: str,
    ) -> bool:
        return str(logical_line or "").strip().upper().startswith("CBL ")

    def _ensure_compiler_option(
        self,
        output_lines: list[str],
        validation_messages: list[str],
    ) -> None:
        """Insert the DB2 compiler option when the source carried none.

        CBL is a compiler directive and must precede IDENTIFICATION
        DIVISION, so the line is inserted immediately above it.

        The inserted line clones the sequence-area geometry of the
        IDENTIFICATION DIVISION line it sits above, exactly as every
        other insertion pass does. FinalSequenceResequencerService
        renumbers columns 1-6 and 73-80 afterwards, so the clone only
        has to be well-formed, not finally numbered.

        Never raises: a program with no IDENTIFICATION DIVISION is
        already broken for other reasons, and is reported rather than
        silently patched.
        """
        for index, line in enumerate(output_lines):
            logical = self.line_utils.logical_line(line).strip().upper()

            if not logical.startswith("IDENTIFICATION DIVISION"):
                continue

            output_lines.insert(
                index,
                self.line_utils.replace_logical_body(
                    original_line=line,
                    replacement_body=DB2_COMPILER_OPTION_LINE,
                ),
            )
            validation_messages.append(
                "Compiler option: source carried no CBL line; inserted "
                f"{DB2_COMPILER_OPTION_LINE} before IDENTIFICATION DIVISION."
            )
            return

        validation_messages.append(
            "Compiler option: no IDENTIFICATION DIVISION found, so "
            f"{DB2_COMPILER_OPTION_LINE} was not inserted."
        )

    def _detect_sql_error_paragraph(
        self,
        cobol_text: str,
    ) -> str:
        match = SQL_ERROR_PARAGRAPH_PATTERN.search(str(cobol_text or ""))

        if not match:
            return DEFAULT_SQL_ERROR_PARAGRAPH

        return match.group(1).upper()

    def _clean_data_declaration_line(
        self,
        line: str,
    ) -> str:
        """Preserve a COBOL data declaration exactly as authored.

        COMP-3/COMP-2/COMP-1 are valid COBOL USAGE clauses, not IDMS-only
        syntax. Removing them changes storage representation. Removing a
        FILLER changes offsets in a group, and adding VALUE ZEROES can alter
        initialization or make a REDEFINES declaration invalid.

        This generic cleanup hook is therefore intentionally a no-op. If a
        specific generated work field needs a different representation, its
        owning generator must define that representation explicitly.
        """
        return line


__all__ = [
    "CobolTransformer",
]