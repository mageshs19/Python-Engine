"""Final cleanup after every source-to-source generator has completed.

The bounded LRF singleton rewriter runs after the layout pipeline and emits
fixed-format records with placeholder sequence values plus explanatory
comments. This service removes only generated narration, preserves LRF trace
markers/business comments, and resequences the final records.
"""
from __future__ import annotations

import re

from converter.composers.paragraph_entry_display_composer import _is_paragraph as _is_cobol_paragraph
from converter.composers.unnecessary_comments_cleanup_composer import (
    UnnecessaryCommentsCleanupComposer,
)
from converter.services.final_sequence_resequencer_service import (
    FinalSequenceResequencerService,
)
from converter.services.program_constant_normalizer import ProgramConstantNormalizer


def _logical(line: str) -> str:
    text = str(line or "").rstrip()
    if len(text) >= 7 and text[:6].isdigit():
        return text[7:72].strip()
    return text.strip()


def _is_fixed_comment(line: str) -> bool:
    text = str(line or "")
    return len(text) >= 7 and text[:6].isdigit() and text[6] in ("*", "/")


def _is_comment(line: str) -> bool:
    text = str(line or "")
    if _is_fixed_comment(text):
        return True
    return text.lstrip().startswith(("*", "/"))


class FinalGeneratedOutputService:
    def __init__(self) -> None:
        self.messages: list[str] = []

    @classmethod
    def _ensure_sql_location_before_runtime_sql(cls, text: str) -> str:
        """Set SQL-LOCATION before runtime SQL blocks that lack a local value.

        This is a final safety net for legacy/reused restart paragraphs that
        bypass the current restart SQL builder. It scopes the check to the
        current COBOL paragraph and the preceding runtime SQL statement, so a
        location used for one SQL statement is not accidentally reused for the
        next one. INCLUDE and DECLARE CURSOR blocks are not runtime statements.
        """
        lines = str(text or "").splitlines()
        output: list[str] = []
        scope_start = 0
        last_runtime_end = -1
        index = 0
        while index < len(lines):
            line = lines[index]
            body = _logical(line)
            if cls._is_area_a_paragraph(line):
                scope_start = index
                last_runtime_end = -1

            if not re.search(r"\bEXEC\s+SQL\b", body, re.I):
                output.append(line)
                index += 1
                continue

            end = next(
                (pos for pos in range(index + 1, len(lines)) if re.search(r"\bEND-EXEC\b", _logical(lines[pos]), re.I)),
                None,
            )
            if end is None:
                output.append(line)
                index += 1
                continue

            block_lines = [body] + [_logical(item) for item in lines[index + 1:end]]
            block_text = " ".join(block_lines).upper()
            runtime = bool(re.search(r"\b(?:SELECT|INSERT|UPDATE|DELETE|COMMIT|ROLLBACK|OPEN|FETCH|CLOSE)\b", block_text))
            non_runtime = bool(re.search(r"\b(?:INCLUDE|DECLARE)\b", block_text))
            if runtime and not non_runtime:
                # Older keyed-read builders emitted a symbolic label into
                # SQL-LOCATION even when SQLERRWS expects a numeric location.
                # A QUERYNO in this very SQL block is source-proven numeric
                # metadata; normalize only an *immediately preceding* marker,
                # never an arbitrary business literal elsewhere in the code.
                queryno = re.search(r"\bQUERYNO\s+(\d+)\b", block_text, re.I)
                if queryno:
                    preceding = next((n for n in range(len(output) - 1, -1, -1)
                                      if _logical(output[n]) and not _is_comment(output[n])), -1)
                    if preceding >= 0:
                        previous = _logical(output[preceding])
                        if re.fullmatch(r"MOVE\s+'[A-Z][A-Z0-9_-]*'\s+TO\s+SQL-LOCATION\.", previous, re.I):
                            raw = output[preceding]
                            replacement = f"    MOVE {queryno.group(1)} TO SQL-LOCATION."
                            output[preceding] = (
                                raw[:7] + replacement.ljust(65) + raw[72:]
                                if len(raw) >= 7 and raw[:6].isdigit()
                                else replacement
                            )
                segment_start = (last_runtime_end + 1) if last_runtime_end >= scope_start else scope_start
                prior_bodies = [_logical(item).upper() for item in lines[segment_start:index]]
                has_local_location = any(
                    re.search(r"\bTO\s+SQL-LOCATION\b", prior, re.I)
                    for prior in prior_bodies
                )
                if not has_local_location:
                    paragraph_body = _logical(lines[scope_start]) if scope_start < len(lines) else ""
                    number = re.match(r"^(\d{3,6})-[A-Z0-9-]+\.$", paragraph_body, re.I)
                    # Prefer the paragraph's numeric identity. A symbolic
                    # fallback such as SQL-STATEMENT is an undeclared COBOL
                    # data-name, not a valid diagnostic location. For an
                    # unnumbered paragraph, QUERYNO is a source-proven numeric
                    # identifier associated with this SQL operation.
                    queryno = re.search(r"\bQUERYNO\s+(\d+)\b", block_text, re.I)
                    location = number.group(1) if number else (
                        queryno.group(1) if queryno else ""
                    )
                    if location:
                        # No period: a period inside IF/EVALUATE would close
                        # the enclosing COBOL sentence.
                        indent = "            "
                        output.append(f"{indent}MOVE {location} TO SQL-LOCATION")
                    else:
                        # No invented identifier. The semantic preflight must
                        # flag missing diagnostics if no numeric location exists.
                        pass
                last_runtime_end = end

            output.extend(lines[index:end + 1])
            index = end + 1

        result = "\n".join(output)
        if str(text or "").endswith(("\n", "\r")):
            result += "\n"
        return result

    @staticmethod
    def _remove_obsolete_lrf_comments(text: str) -> str:
        """Remove only stale LRF breadcrumbs whose executable SQL now exists.

        The subschema expander can carry commented path-group statements
        (fixed-format ``*=`` lines) into the generated member. They are not
        COBOL logic. Likewise, a prior KEEP note for an LRF MODIFY is stale
        when the final member contains the corresponding generated UPDATE.
        Unresolved mapping KEEP notes are retained.
        """
        lines = str(text or "").splitlines()
        has_business_update = any(
            re.search(r"\bUPDATE\s+[A-Z][A-Z0-9_]*\b", _logical(line), re.I)
            for line in lines if not _is_comment(line)
        )
        output: list[str] = []
        index = 0
        while index < len(lines):
            line = lines[index]
            body = _logical(line)
            if _is_fixed_comment(line) and body.startswith("="):
                index += 1
                continue

            if _is_comment(line):
                end = index + 1
                while end < len(lines) and _is_comment(lines[end]):
                    end += 1
                block = lines[index:end]
                # Generated breadcrumbs are consumed by this comment-block
                # branch, so a later executable-line check can never see them.
                # Remove only the obsolete generated line and keep neighboring
                # business/review comments intact.
                block = [
                    item for item in block
                    if "deleted by the idms conversion. original:" not in _logical(item).lower()
                ]
                if not block:
                    index = end
                    continue
                joined = " ".join(_logical(item).upper() for item in block)
                stale_lrf_modify = (
                    has_business_update
                    and "DB2-KEEP" in joined
                    and "EXPANDED LRF MODIFY" in joined
                )
                next_index = end
                while next_index < len(lines) and not _logical(lines[next_index]):
                    next_index += 1
                next_body = _logical(lines[next_index]) if next_index < len(lines) else ""
                orphaned_record_label = (
                    len(block) == 1
                    and bool(re.fullmatch(r"[A-Z][A-Z0-9-]*\.", _logical(block[0]), re.I))
                    and bool(
                        re.match(r"^(?:MOVE\b.*SQL-LOCATION|EXEC\s+SQL|UPDATE\b|INSERT\b|SELECT\b)", next_body, re.I)
                    )
                )
                if not stale_lrf_modify and not orphaned_record_label:
                    output.extend(block)
                index = end
                continue

            output.append(line)
            index += 1

        newline = "\n"
        result = newline.join(output)
        if str(text or "").endswith(("\n", "\r")):
            result += newline
        return result

    @staticmethod
    def _remove_consumed_extra_filter_comments(text: str) -> str:
        """Drop generated cursor-WHERE notes only after SQL consumed the filter.

        If the field and every literal from the note occur in the same generated
        EXEC SQL block, the note is obsolete. Otherwise preserve it as a review
        warning rather than silently losing an unconverted business predicate.
        """
        source = str(text or "")
        sql_blocks = [
            match.group(1)
            for match in re.finditer(r"EXEC\s+SQL\b(.*?)END-EXEC", source, re.I | re.S)
        ]
        normalized_blocks = [re.sub(r"[^A-Z0-9]", "", block.upper()) for block in sql_blocks]
        output: list[str] = []
        for line in source.splitlines():
            body = _logical(line)
            if not _is_comment(line) or not re.search(r"add to the generated cursor WHERE", body, re.I):
                output.append(line)
                continue

            condition = re.split(r"-\s*add to the generated cursor WHERE", body, maxsplit=1, flags=re.I)[0]
            identifiers = [
                token for token in re.findall(r"[A-Z][A-Z0-9-]*", condition.upper())
                if token not in {"DB2", "LRF", "EXTRA", "FILTER", "AND", "OR", "NOT", "IS", "NULL"}
            ]
            literals = re.findall(r"'((?:''|[^'])*)'|\b(\d+)\b", condition)
            literal_values = [single or numeric for single, numeric in literals]
            consumed = False
            for block in normalized_blocks:
                normalized_identifiers = [re.sub(r"[^A-Z0-9]", "", token) for token in identifiers]
                if all(token and token in block for token in normalized_identifiers) and all(
                    re.sub(r"[^A-Z0-9]", "", value.upper()) in block for value in literal_values
                ):
                    consumed = True
                    break
            if not consumed:
                output.append(line)

        result = "\n".join(output)
        if source.endswith(("\n", "\r")):
            result += "\n"
        return result

    @staticmethod
    def _normalize_lrf_error_conditions(text: str) -> str:
        """Normalize the converted form of `IF ... OR 'LR-ERROR'`.

        After DB-REC-NOT-FOUND becomes SQLCODE = 100, the source's abbreviated
        LR-ERROR alternative must become a full COBOL condition. A non-zero
        SQLCODE covers both not-found and SQL errors. Preserve fixed-format
        sequence and identification areas when replacing the logical body.
        """
        output: list[str] = []
        condition = re.compile(
            r"^IF\s+SQLCODE\s*=\s*100\s+OR\s+'LR-ERROR'\.?$", re.I
        )
        for line in str(text or "").splitlines():
            if len(line) >= 7 and line[:6].isdigit():
                body = line[7:72].strip()
                if condition.match(body):
                    # Do not terminate the COBOL sentence here. The source
                    # condition governs the following PERFORM IDMS-STOP, whose
                    # period closes the IF statement. A period on this IF would
                    # make the rollback/abend call unconditional.
                    line = line[:7] + "IF SQLCODE NOT = 0".ljust(65) + line[72:]
            else:
                body = line.strip()
                if condition.match(body):
                    line = "IF SQLCODE NOT = 0"
            output.append(line)
        result = "\n".join(output)
        if str(text or "").endswith(("\n", "\r")):
            result += "\n"
        return result

    @staticmethod
    def _remove_empty_sqlcode_guards(text: str) -> str:
        """Remove a generated SQLCODE IF only when it has no executable body.

        The converted IDMS `IF DB-REC-NOT-FOUND OR 'LR-ERROR'` can lose its
        obsolete `PERFORM IDMS-STOP` target after SQLERROR handling has been
        emitted. The resulting `IF SQLCODE NOT = 0.` immediately before the next
        paragraph is invalid COBOL and performs no work. Remove only that exact
        empty shape; guards with a body or END-IF are left untouched.
        """
        lines = str(text or "").splitlines()
        output: list[str] = []
        for index, line in enumerate(lines):
            body = _logical(line)
            if not re.fullmatch(r"IF\s+SQLCODE\s+NOT\s*=\s*0\.?", body, re.I):
                output.append(line)
                continue
            next_index = index + 1
            while next_index < len(lines) and (not _logical(lines[next_index]) or _is_comment(lines[next_index])):
                next_index += 1
            if next_index < len(lines) and FinalGeneratedOutputService._is_area_a_paragraph(lines[next_index]):
                continue
            output.append(line)
        result = "\n".join(output)
        if str(text or "").endswith(("\n", "\r")):
            result += "\n"
        return result

    @staticmethod
    def _is_area_a_paragraph(line: str) -> bool:
        # Share one lexical rule with paragraph tracing; an Area A END-IF.
        # is a scope terminator and must never start a new paragraph.
        return _is_cobol_paragraph(line)

    @staticmethod
    def _remove_resolved_status_warning(text: str) -> str:
        lines = text.splitlines()
        active = "\n".join(_logical(line) for line in lines if not _is_comment(line))
        active = re.sub(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"|\*>[^\n]*", " ", active)
        if re.search(r"(?<![A-Z0-9-])ERROR-STATUS(?![A-Z0-9-])", active, re.I):
            return text
        output = []
        index = 0
        while index < len(lines):
            if (_is_comment(lines[index]) and _logical(lines[index]).upper().startswith(
                    "DB2 WARNING: ERROR-STATUS IS UNDEFINED AFTER COPYBOOK REMOVAL")):
                index += 1
                if index < len(lines) and _is_comment(lines[index]) and _logical(lines[index]).upper().startswith(
                        "SHARES A LINE WITH LIVE OPERANDS; LEFT FOR MANUAL REVIEW."):
                    index += 1
                continue
            output.append(lines[index])
            index += 1
        return "\n".join(output) + ("\n" if text.endswith("\n") else "")

    def apply(self, text: str, *, standardize_lifecycle: bool = False) -> str:
        self.messages = []
        source = str(text or "")
        if not source:
            return ""

        source = self._ensure_sql_location_before_runtime_sql(source)
        source = self._remove_obsolete_lrf_comments(source)
        source = self._remove_consumed_extra_filter_comments(source)
        source = self._normalize_lrf_error_conditions(source)
        source = self._remove_empty_sqlcode_guards(source)
        source = self._remove_resolved_status_warning(source)
        cleanup = UnnecessaryCommentsCleanupComposer()
        source = cleanup.cleanup_generated_narration(source)
        self.messages.extend(cleanup.messages)
        # Generic final guard: later generation stages must not leave a second
        # program-specific CS-* constant when CS-PROGRAM already exists.
        source = ProgramConstantNormalizer.normalize(source)
        from converter.composers.program_identity_initializer import ProgramIdentityInitializer
        identity = ProgramIdentityInitializer()
        source = identity.compose(source)
        self.messages.extend(identity.messages)
        # Mainline restructuring is opt-in only. Production defaults to False
        # because lifecycle wrappers are not valid for every business program;
        # callers that explicitly need the legacy transformation must opt in.
        if standardize_lifecycle:
            from converter.composers.lifecycle_standardization_composer import (
                LifecycleStandardizationComposer,
            )
            lifecycle = LifecycleStandardizationComposer()
            source = lifecycle.compose(source)
            self.messages.extend(lifecycle.messages)
        # Mandatory, concept-level paragraph entry tracing. This applies to all
        # generated COBOL paragraphs, not to a program-name allowlist.
        from converter.composers.paragraph_entry_display_composer import (
            ParagraphEntryDisplayComposer,
        )
        paragraph_display = ParagraphEntryDisplayComposer()
        source = paragraph_display.compose(source)
        self.messages.extend(paragraph_display.messages)
        return FinalSequenceResequencerService().resequence(source)


__all__ = ["FinalGeneratedOutputService"]
