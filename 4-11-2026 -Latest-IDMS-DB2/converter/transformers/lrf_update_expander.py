# LOCATION: converter/transformers/lrf_update_expander.py
# ACTION: REPLACE ENTIRE FILE
"""Expands the UPDATE-side Logical Record Facility syntax into classic IDMS.

WHY THIS EXISTS
---------------
``LrfPathExpander`` teaches the converter the READ and DELETE logical-record
forms::

    OBTAIN FIRST <logical-record> WHERE <keyword>.  -> OBTAIN FIRST <rec> WITHIN <set>.
    ERASE        <logical-record> WHERE <keyword>.  -> ERASE <rec>.

The WRITE-side forms have the same shape but the converter never learned
them, so an update program written against a logical record kept its LRF
verbs all the way to the residual-IDMS checks::

    MODIFY <logical-record> WHERE <keyword>.   (SQL UPDATE)
    STORE  <logical-record> WHERE <keyword>.   (SQL INSERT)

CORRECTION 1 - THE PRE-CHECK READ RAW LINES
-------------------------------------------
``_contains_lr_update_syntax`` applied the anchored pattern to RAW source
lines. A fixed-format record is::

    000186     STORE VMBTL07-R01 WHERE ST-VMBEVEF.          01860000
    |----|     |------------ body, cols 8-72 -----|         |------|
    cols 1-6                                                cols 73-80

``^\\s*(MODIFY|STORE)`` cannot match ``000186...`` and ``$`` cannot match
with ``01860000`` trailing, so the gate returned False for EVERY mainframe
program and the whole pass silently no-opped. This is the same defect
already recorded against LrfPathExpander._contains_lrf_syntax. The check
now reduces each line to its LOGICAL BODY first, exactly as the main loop
already did.

CORRECTION 2 - "KEEP" DELETED THE STATEMENT
-------------------------------------------
``_keep`` emitted the audit marker as a comment AND the original statement
as a second comment, so a refused MODIFY / STORE was commented out rather
than left alone. A refusal must never remove executable code. The original
line is now re-emitted byte-for-byte beneath the marker.

CORRECTION 3 - COMMENT DETECTION ATE EXECUTABLE LINES
-----------------------------------------------------
The free-format fallback tested ``startswith(("*", "/", "D", "-"))``. The
D and - indicators are meaningful ONLY in column 7 of a fixed-format
record; applied to a stripped line they classify ``DISPLAY ...`` and
``-100`` as comments. Column 7 is now authoritative for fixed format, and
only ``*`` / ``/`` count in free format.

CORRECTION 4 - WHOLE-FILE LINE ENDINGS WERE REWRITTEN
-----------------------------------------------------
The emitter returned ``"\\n".join(output).rstrip() + "\\n"``, converting
CRLF to LF and dropping trailing blank lines across the ENTIRE file - a
diff far wider than the two lines actually touched, and enough to fail a
byte-identical regression gate. The dominant newline is preserved and the
trailing newline is reproduced only when the source had one.

CORRECTION 5 - UNMAPPED DIAGNOSTICS WERE DROPPED
------------------------------------------------
``_log`` looked the key up with ``.get(key, "")`` and returned silently
when the message was absent, so a diagnostic whose template was never
added produced NOTHING. An unmapped key is now reported as an unmapped
key, which is the difference between a visible gap and a lost finding.

CORRECTION 6 - A WRAPPED STATEMENT VANISHED
-------------------------------------------
``MODIFY <lr> WHERE <keyword> AND ...`` continued on the next line does
not match the single-line pattern, so it passed through unchanged and was
not even counted as skipped. It is now recognised as an update-verb line
the pass cannot handle, kept intact, and REPORTED.

NO-LRF CONTRACT
---------------
With no logical record metadata, or with metadata but no LRF update syntax
in the program, ``expand()`` returns the source text byte-for-byte. A
program that never used a logical record behaves exactly as before. The
three early exits return the ORIGINAL object, never a rejoined copy.

MODIFY vs STORE
---------------
MODIFY is the SQL UPDATE case. The element record to modify is the record
the path makes current with its last FIND / OBTAIN navigation command -
the only element the subschema parser captures for a MODIFY path-group -
so MODIFY is expanded whenever that record resolves and is mapped.

STORE is the SQL INSERT case. A STORE path-group usually seeds several
element records the subschema does not pin down, so guessing which one to
write is unsafe. STORE is expanded only for a single-element logical
record; otherwise it is kept, with a ``*DB2-KEEP:`` audit comment, for
manual review.

NAME FORM
---------
Generated names are COBOL form (UPPERCASE, hyphens). NameNormalizer is not
used here: normalize() yields the DB2 column form and would emit
VMBTL07_R01.
"""

from __future__ import annotations

import re

from converter.services.fixed_format_line_service import (
    FixedFormatLineService,
)
from patterns.lrf_program_patterns import LR_MODIFY_WHERE_PATTERN
from rules.lrf_conversion_rules import (
    ENABLE_LRF_PATH_EXPANSION,
    EXPANDED_UPDATE_TEMPLATE,
    LRF_UPDATE_MESSAGES,
    MODIFY_TEMPLATE,
    REQUIRE_MAPPED_DRIVING_RECORD,
    SKIPPED_NO_PATH_TEMPLATE,
    SKIPPED_NO_RECORD_TEMPLATE,
    SKIPPED_STORE_AMBIGUOUS_TEMPLATE,
    SKIPPED_UNMAPPED_TEMPLATE,
    STATEMENT_TERMINATOR,
    STORE_TEMPLATE,
)

# Independent kill switch for bisection. Falls back to the shared LRF
# switch so this module imports cleanly before the constant is added.
try:  # pragma: no cover - import-time fallback
    from rules.lrf_conversion_rules import ENABLE_LRF_UPDATE_EXPANSION
except ImportError:  # pragma: no cover
    ENABLE_LRF_UPDATE_EXPANSION = ENABLE_LRF_PATH_EXPANSION

PROCEDURE_DIVISION_TOKEN = "PROCEDURE DIVISION"

# Valid column-7 indicators in a fixed-format record.
COMMENT_INDICATORS = ("*", "/", "D", "-")

# Indicators that mean "comment" in FREE format, where there is no
# column 7. D and - are deliberately absent: see CORRECTION 3.
FREE_FORMAT_COMMENT_PREFIXES = ("*", "/")

COMMENT_PREFIX_COLUMNS = "      "
DEFAULT_INDENT = "    "
SEQUENCE_AREA_WIDTH = 6
INDICATOR_COLUMN = 6  # zero-based index of column 7

VERB_MODIFY = "MODIFY"
VERB_STORE = "STORE"
UPDATE_VERBS = (VERB_MODIFY, VERB_STORE)
NAVIGATION_VERBS = ("FIND", "OBTAIN")
WHERE_TOKEN = "WHERE"

UNMAPPED_DIAGNOSTIC_TEMPLATE = (
    "LRF update expansion: unmapped diagnostic '{key}' {values}"
)
UNRENDERABLE_DIAGNOSTIC_TEMPLATE = (
    "LRF update expansion: diagnostic '{key}' could not be rendered ({error})."
)
UNTERMINATED_KEEP_TEMPLATE = (
    "DB2-KEEP: {verb} on a logical record continues past this line; "
    "the single-line form is the only one this pass expands."
)


def cobol_name(value: str) -> str:
    """UPPERCASE COBOL/IDMS form: hyphens, never underscores."""
    return str(value or "").strip().upper().replace("_", "-")


class LrfUpdateExpander:
    """Rewrites LRF MODIFY / STORE program syntax into classic IDMS syntax."""

    def __init__(
        self,
        *,
        path_resolver=None,
        fixed_format: FixedFormatLineService | None = None,
    ) -> None:
        self.path_resolver = path_resolver
        self.fixed_format = fixed_format or FixedFormatLineService()
        self.messages: list[str] = []

    # ---------------------------------------------------------- public
    def expand(self, cobol_text: str) -> str:
        """Rewrite update-side LRF syntax. Byte-identical when nothing matches."""
        self.messages = []

        text = str(cobol_text or "")

        if not text.strip():
            return text

        if not (ENABLE_LRF_PATH_EXPANSION and ENABLE_LRF_UPDATE_EXPANSION):
            if self._contains_lr_update_syntax(text):
                self._log("disabled")
            return text

        if self.path_resolver is None or self._resolver_is_empty():
            if self._contains_lr_update_syntax(text):
                self._log("no_logical_records")
            return text

        if not self._contains_lr_update_syntax(text):
            return text

        newline = "\r\n" if "\r\n" in text else "\n"
        had_trailing_newline = text.endswith(("\n", "\r"))
        lines = text.splitlines()

        output: list[str] = []
        in_procedure = False
        expanded = 0
        skipped = 0
        resolved_lrs: set[str] = set()
        resolved_keywords: set[str] = set()
        index = 0

        while index < len(lines):
            line = lines[index]
            logical = self._logical(line)

            if not in_procedure:
                output.append(line)
                if PROCEDURE_DIVISION_TOKEN in logical.upper():
                    in_procedure = True
                index += 1
                continue

            if self._is_comment(line) or not logical:
                output.append(line)
                index += 1
                continue

            match = LR_MODIFY_WHERE_PATTERN.match(logical)
            source_lines = [line]
            consumed = 1

            # LRF MODIFY / STORE statements may be wrapped across physical
            # records. Join only a bounded, unambiguous statement span. The
            # original physical lines are retained for audit/refusal paths.
            if not match and self._starts_update_verb(logical):
                consumed, joined, joined_match, has_where = self._collect_update_statement(
                    lines, index
                )
                source_lines = lines[index:index + consumed]
                if joined_match is not None:
                    logical = joined
                    match = joined_match
                elif has_where:
                    verb = self._unhandled_update_verb(joined) or self._starts_update_verb(logical)
                    self._log("multiline_unsupported", verb=verb)
                    output.extend(self._keep_lines(
                        source_lines,
                        f"DB2-KEEP: multiline {verb} logical-record statement could not be "
                        "resolved as one complete MODIFY/STORE ... WHERE keyword; retained unchanged.",
                    ))
                    skipped += 1
                    index += consumed
                    continue

            if match:
                rendered, ok = self._expand_update(line, match, source_lines=source_lines)
                output.extend(rendered)
                expanded += 1 if ok else 0
                skipped += 0 if ok else 1
                if ok:
                    resolved_lrs.add(cobol_name(match.group("lr")))
                    resolved_keywords.add(cobol_name(match.group("keyword")))
                index += consumed
                continue

            verb = self._unhandled_update_verb(logical)
            if verb:
                self._log("statement_unterminated", verb=verb)
                output.extend(
                    self._keep(
                        line, UNTERMINATED_KEEP_TEMPLATE.format(verb=verb)
                    )
                )
                skipped += 1
                index += 1
                continue

            output.append(line)
            index += 1

        if expanded or skipped:
            self._log("summary", expanded=expanded, skipped=skipped)
        else:
            # Nothing was touched: hand back the ORIGINAL object so no
            # newline or trailing-blank normalisation can leak into the diff.
            return text

        result = newline.join(output)
        if had_trailing_newline:
            result += newline
        if resolved_lrs:
            result = self._remove_stale_keep_blocks(
                result,
                resolved_lrs=resolved_lrs,
                resolved_keywords=resolved_keywords,
            )
        return result

    # ------------------------------------------------------- expansion
    def _expand_update(
        self, line: str, match, *, source_lines: list[str] | None = None
    ) -> tuple[list[str], bool]:
        source_lines = list(source_lines or [line])

        def keep(marker: str) -> list[str]:
            return self._keep_lines(source_lines, marker)

        verb = str(match.group("verb") or "").upper()
        lr_name = cobol_name(match.group("lr"))
        keyword = cobol_name(match.group("keyword"))

        path = self._lookup_path(keyword)
        if path is None:
            self._log("keyword_not_found", keyword=keyword)
            return (
                keep(SKIPPED_NO_PATH_TEMPLATE.format(keyword=keyword)),
                False,
            )

        # Never trust a keyword alone: a typo can otherwise resolve to a path
        # belonging to a different logical record and silently rewrite the
        # wrong IDMS access. Refuse closed and preserve the executable source.
        expected_lr = cobol_name(getattr(path, "logical_record", ""))
        if expected_lr and expected_lr != lr_name:
            self._log(
                "logical_record_mismatch", keyword=keyword,
                expected_lr=expected_lr, source_lr=lr_name,
            )
            return keep(
                f"DB2-KEEP: keyword {keyword} belongs to {expected_lr}, "
                f"not source logical record {lr_name}; retained unchanged."
            ), False

        path_verb = str(getattr(path, "path_group_verb", "") or "").upper()
        if path_verb and path_verb != verb:
            self._log(
                "verb_mismatch", source_verb=verb, path_verb=path_verb,
                keyword=keyword,
            )
            return keep(
                f"DB2-KEEP: {verb} does not match {path_verb} path for "
                f"keyword {keyword}; retained unchanged."
            ), False

        # STORE paths can seed several records, but a keyword such as
        # ST-VMBEVEF names the exact element being stored. The subschema
        # parser records navigation commands, not STORE commands, so the
        # generic "last navigation record" is the parent (VMBEFF) here.
        # Prefer an exact ST-<element-record> keyword match; only retain the
        # conservative ambiguity refusal for compound keywords such as
        # ST-VMBWCEF-TO-VMBEVEF.
        store_target = (
            self._store_target_record(keyword, path)
            if verb == VERB_STORE else ""
        )
        if verb == VERB_STORE and self._store_is_ambiguous(path) and not store_target:
            self._log("store_ambiguous", keyword=keyword)
            return (
                keep(SKIPPED_STORE_AMBIGUOUS_TEMPLATE.format(keyword=keyword)),
                False,
            )

        record = store_target or self._driving_record(path)
        if not record:
            self._log("no_record", keyword=keyword)
            return (
                keep(SKIPPED_NO_RECORD_TEMPLATE.format(keyword=keyword)),
                False,
            )

        element_records = {
            cobol_name(name)
            for name in self._element_records(expected_lr or lr_name)
            if str(name or "").strip()
        }
        if element_records and record not in element_records:
            logical_record = expected_lr or lr_name
            self._log(
                "driving_record_not_element", record=record,
                logical_record=logical_record,
            )
            return keep(
                f"DB2-KEEP: driving record {record} is not an element of "
                f"{logical_record}; retained unchanged."
            ), False

        if REQUIRE_MAPPED_DRIVING_RECORD and not self._record_is_mapped(record):
            self._log("record_unmapped", record=record, keyword=keyword)
            return (
                keep(SKIPPED_UNMAPPED_TEMPLATE.format(record=record)),
                False,
            )

        rendered = self._comment(
            line,
            EXPANDED_UPDATE_TEMPLATE.format(
                verb=verb, lr=lr_name, keyword=keyword, record=record
            ),
        )
        # Preserve every physical source record in the audit trail when the
        # LRF statement was continued. These are comments only; the generated
        # classic-IDMS statement below is the sole executable replacement.
        for continuation in source_lines[1:]:
            rendered.extend(self._comment(
                continuation,
                f"DB2-LRF-SOURCE: {self._logical(continuation)}",
            ))
        template = STORE_TEMPLATE if verb == VERB_STORE else MODIFY_TEMPLATE
        # A STORE path may first position a CALC parent (for example
        # ST-VMBEVEF obtains VMBEFF by CALCKEY, then stores VMBEVEF).
        # Preserve that semantic requirement as a pipeline marker so the
        # DB2 stage can generate a keyed parent SELECT before INSERT.
        if verb == VERB_STORE and store_target:
            parent_record = self._driving_record(path)
            has_calc_parent = any(
                str(getattr(command, "verb", "") or "").upper() in NAVIGATION_VERBS
                and "CALCKEY" in str(getattr(command, "where_clause", "") or "").upper()
                for command in (getattr(path, "commands", None) or [])
            )
            if parent_record and parent_record != store_target and has_calc_parent:
                rendered.append(
                    self._comment(
                        line,
                        f"DB2-LRF-STORE-PARENT: {parent_record}",
                    )[0]
                )

        rendered.extend(
            self._statement(
                line,
                template.format(record=record),
                # match.string IS the logical line the pattern matched,
                # so the source terminator is available here.
                terminate=self._is_terminated(match.string),
            )
        )

        self._log(
            "expanded", verb=verb, lr=lr_name, keyword=keyword, record=record
        )
        return rendered, True

    # --------------------------------------------------- path analysis
    def _driving_record(self, path) -> str:
        """The element record the path makes current, in COBOL form.

        For a MODIFY / STORE path-group the record to write is the one the
        last FIND / OBTAIN navigation command establishes as current. The
        subschema parser does not retain the MODIFY / STORE verb line
        itself, so the navigation record is the reliable driving record.
        """
        record = ""
        for command in getattr(path, "commands", None) or []:
            verb = str(getattr(command, "verb", "") or "").upper()
            if verb in NAVIGATION_VERBS:
                name = cobol_name(getattr(command, "record_name", ""))
                if name:
                    record = name
        return record

    def _store_is_ambiguous(self, path) -> bool:
        """True when a STORE path seeds more than one element record."""
        elements = [
            name
            for name in self._element_records(
                getattr(path, "logical_record", "")
            )
            if str(name or "").strip()
        ]
        return len(elements) > 1

    def _store_target_record(self, keyword: str, path) -> str:
        """Resolve only an exact ST-<element> keyword to its target record.

        This is deliberately narrower than guessing from the last OBTAIN:
        ST-VMBEVEF can safely select VMBEVEF even though its path first
        obtains VMBEFF. A compound keyword is not an exact record name and
        remains subject to the multi-element safety refusal.
        """
        normalized_keyword = cobol_name(keyword)
        if not normalized_keyword.startswith("ST-"):
            return ""
        target = normalized_keyword[3:]
        if not target or "-TO-" in target:
            return ""
        elements = {
            cobol_name(name)
            for name in self._element_records(
                getattr(path, "logical_record", "")
            )
            if str(name or "").strip()
        }
        return target if target in elements else ""

    def _remove_stale_keep_blocks(
        self,
        text: str,
        *,
        resolved_lrs: set[str],
        resolved_keywords: set[str],
    ) -> str:
        """Drop stale DB2-KEEP blocks superseded by a successful LRF rewrite.

        Earlier conversion passes can leave a KEEP marker beside the source
        LRF statement, before this write-side pass gets a chance to expand it.
        Once the exact LR update has been resolved, that refusal is obsolete.
        Only comment-only blocks carrying a DB2-KEEP marker tied to one of
        those resolved LR/keywords are removed; unresolved KEEP records remain.
        """
        lines = text.splitlines()
        result: list[str] = []
        index = 0
        while index < len(lines):
            if not self._is_comment(lines[index]):
                result.append(lines[index])
                index += 1
                continue
            end = index + 1
            while end < len(lines) and self._is_comment(lines[end]):
                end += 1
            block = lines[index:end]
            joined = " ".join(self._logical(line).upper() for line in block)
            has_keep = "DB2-KEEP" in joined
            tied_to_resolved_access = any(name in joined for name in resolved_lrs) or any(
                keyword in joined for keyword in resolved_keywords
            )
            if not (has_keep and tied_to_resolved_access):
                result.extend(block)
            else:
                # The parent-SELECT marker is generated by this pass and
                # must survive even when it shares a contiguous comment block
                # with stale pre-expansion DB2-KEEP notes.
                result.extend(
                    line for line in block
                    if "DB2-LRF-STORE-PARENT:" in self._logical(line).upper()
                )
            index = end
        newline = "\r\n" if "\r\n" in text else "\n"
        output = newline.join(result)
        if text.endswith(("\n", "\r")):
            output += newline
        return output

    def _resolver_is_empty(self) -> bool:
        try:
            return bool(self.path_resolver.is_empty())
        except Exception:  # noqa: BLE001
            return True

    def _lookup_path(self, keyword: str):
        repository = getattr(self.path_resolver, "lrf_repository", None)
        if repository is None:
            return None
        try:
            return repository.path_for_keyword(keyword)
        except Exception:  # noqa: BLE001
            return None

    def _element_records(self, logical_record_name: str) -> list:
        repository = getattr(self.path_resolver, "lrf_repository", None)
        if repository is None:
            return []
        try:
            return repository.element_records(logical_record_name) or []
        except Exception:  # noqa: BLE001
            return []

    def _record_is_mapped(self, record_name: str) -> bool:
        try:
            return bool(self.path_resolver.record_is_mapped(record_name))
        except Exception:  # noqa: BLE001
            return True

    # ---------------------------------------------------------- render
    def _statement(
        self,
        template_line: str,
        body: str,
        terminate: bool = True,
    ) -> list[str]:
        """Render one generated statement.

        ``terminate`` MIRRORS the source statement, for the same reason
        recorded in LrfPathExpander: a period closes the COBOL SENTENCE,
        so adding one to a statement that sits inside an inline block
        orphans the block's END- keyword and the program will not
        compile. Both current MODIFY / STORE forms are standalone and
        terminated, so this is a latent guard rather than a live fix.

        Defaults to True so any caller added later behaves as this method
        always did unless it opts in.
        """
        text = body.rstrip()
        if terminate and not text.endswith(STATEMENT_TERMINATOR):
            text = f"{text}{STATEMENT_TERMINATOR}"
        indent = self._body_indent(template_line)
        return self._emit(template_line, f"{indent}{text}", indicator=" ")
    
    def _comment(self, template_line: str, body: str) -> list[str]:
        """Comment body starts at column 8 - no indent, no leading star."""
        text = str(body or "").lstrip("*").strip()
        return self._emit(template_line, text, indicator="*")

    def _keep(self, line: str, marker: str) -> list[str]:
        """Audit marker, then the ORIGINAL statement, untouched.

        A refusal must never remove executable code. See CORRECTION 2.
        """
        rendered = self._comment(line, marker)
        rendered.append(line)
        return rendered

    def _emit(self, template_line: str, body: str, indicator: str) -> list[str]:
        if not self._is_fixed(template_line):
            if indicator == "*":
                return [f"{COMMENT_PREFIX_COLUMNS}*{body}"]
            return [body]

        try:
            left, _ind, _old, right = self.fixed_format.split(template_line)
            return self.fixed_format.emit(left, indicator, body, right)
        except Exception:  # noqa: BLE001
            return [template_line]

    @staticmethod
    def _is_terminated(text: str) -> bool:
        """True when the SOURCE statement ended in a period."""
        return str(text or "").rstrip().endswith(STATEMENT_TERMINATOR)
    # --------------------------------------------------------- helpers
    def _logical(self, line: str) -> str:
        """Columns 8-72 of a fixed record, or the stripped line."""
        try:
            return str(self.fixed_format.logical(line) or "").strip()
        except Exception:  # noqa: BLE001
            return str(line or "").strip()

    def _is_fixed(self, line: str) -> bool:
        try:
            return bool(self.fixed_format.is_fixed_line(line))
        except Exception:  # noqa: BLE001
            return False

    def _body_indent(self, line: str) -> str:
        if not self._is_fixed(line):
            text = str(line or "")
            return " " * (len(text) - len(text.lstrip(" ")))
        try:
            _l, _i, body, _r = self.fixed_format.split(line)
            return " " * (len(body) - len(body.lstrip(" ")))
        except Exception:  # noqa: BLE001
            return DEFAULT_INDENT

    def _is_comment(self, line: str) -> bool:
        """Column 7 decides in fixed format; only * and / in free format."""
        text = str(line or "")

        if self._is_fixed(text):
            return (
                len(text) > INDICATOR_COLUMN
                and text[INDICATOR_COLUMN] in COMMENT_INDICATORS
            )

        # Secondary guard: a record whose sequence area is blank or numeric
        # is still fixed format even when the service does not say so.
        if len(text) > INDICATOR_COLUMN:
            sequence = text[:SEQUENCE_AREA_WIDTH].strip()
            if (not sequence) or sequence.isdigit():
                if text[INDICATOR_COLUMN] in COMMENT_INDICATORS:
                    return True

        return text.lstrip().startswith(FREE_FORMAT_COMMENT_PREFIXES)

    @staticmethod
    def _starts_update_verb(logical: str) -> str:
        tokens = str(logical or "").upper().split()
        return tokens[0] if tokens and tokens[0] in UPDATE_VERBS else ""

    def _collect_update_statement(
        self, lines: list[str], start: int
    ) -> tuple[int, str, object | None, bool]:
        """Collect a bounded physical span for a wrapped MODIFY/STORE.

        The span is considered convertible only when the joined logical text
        exactly matches the supported LRF grammar. If WHERE is present but the
        statement remains unsupported, the caller preserves every source line
        and emits a visible refusal. This routine never crosses a blank,
        comment, paragraph header, or another obvious COBOL statement.
        """
        first = self._logical(lines[start])
        joined_parts = [first]
        last_count = 1
        match = LR_MODIFY_WHERE_PATTERN.match(first)
        if match:
            return 1, first, match, True

        max_lines = 8
        for offset in range(1, max_lines):
            position = start + offset
            if position >= len(lines):
                break
            raw = lines[position]
            logical = self._logical(raw)
            if not logical or self._is_comment(raw):
                break
            # A paragraph/section header is a hard boundary, not a
            # continuation of the current LRF statement.
            if (
                re.match(r"^[A-Z0-9-]+(?:\s+SECTION)?\.$", logical, re.I)
                and not re.search(r"\bWHERE\s*$", joined_parts[-1], re.I)
            ):
                break
            if re.match(
                r"^(?:MOVE|IF|ELSE|END-IF|EVALUATE|WHEN|PERFORM|CALL|DISPLAY|"
                r"ADD|SUBTRACT|COMPUTE|WRITE|READ|OPEN|CLOSE|OBTAIN|FIND|STORE|MODIFY)\b",
                logical,
                re.I,
            ) and not re.match(r"^WHERE\b", logical, re.I):
                break

            joined_parts.append(logical)
            last_count = offset + 1
            joined = " ".join(part.strip() for part in joined_parts if part.strip())
            match = LR_MODIFY_WHERE_PATTERN.match(joined)
            if match:
                return last_count, joined, match, True
            # A period closes this sentence. Do not absorb a later statement
            # merely because the first one did not fit the supported grammar.
            if logical.rstrip().endswith("."):
                return last_count, joined, None, bool(re.search(r"\bWHERE\b", joined, re.I))

        joined = " ".join(part.strip() for part in joined_parts if part.strip())
        has_where = bool(re.search(r"\bWHERE\b", joined, re.I))
        return last_count, joined, None, has_where

    def _keep_lines(self, source_lines: list[str], marker: str) -> list[str]:
        """Emit one audit marker and retain all physical source lines intact."""
        if not source_lines:
            return []
        return self._keep(source_lines[0], marker)[:1] + list(source_lines)

    def _contains_lr_update_syntax(self, text: str) -> bool:
        """True when any LOGICAL line carries update-side LRF syntax.

        Reads the logical body, never the raw record. See CORRECTION 1.
        """
        lines = str(text or "").splitlines()
        for index, raw_line in enumerate(lines):
            if self._is_comment(raw_line):
                continue
            logical = self._logical(raw_line)
            if not logical:
                continue
            if LR_MODIFY_WHERE_PATTERN.match(logical):
                return True
            if self._unhandled_update_verb(logical):
                return True
            if self._starts_update_verb(logical):
                _count, _joined, match, has_where = self._collect_update_statement(lines, index)
                if match is not None or has_where:
                    return True
        return False

    @staticmethod
    def _unhandled_update_verb(logical: str) -> str:
        """The verb of an update-side LR line the single-line pattern missed.

        Returns "" for anything that is not ``MODIFY``/``STORE`` followed by
        a ``WHERE``. No regex: the authoritative pattern lives in patterns/.
        """
        tokens = str(logical or "").upper().split()
        if len(tokens) < 3:
            return ""
        if tokens[0] not in UPDATE_VERBS:
            return ""
        if WHERE_TOKEN not in tokens[1:]:
            return ""
        return tokens[0]

    def _log(self, key: str, **values) -> None:
        """Record one diagnostic. An unmapped key is REPORTED, not dropped."""
        template = LRF_UPDATE_MESSAGES.get(key, "")

        if not template:
            rendered = " ".join(
                f"{name}={value}" for name, value in sorted(values.items())
            )
            self.messages.append(
                UNMAPPED_DIAGNOSTIC_TEMPLATE.format(key=key, values=rendered)
            )
            return

        try:
            self.messages.append(template.format(**values))
        except (KeyError, IndexError, ValueError) as error:
            self.messages.append(
                UNRENDERABLE_DIAGNOSTIC_TEMPLATE.format(key=key, error=error)
            )


__all__ = ["LrfUpdateExpander", "cobol_name"]