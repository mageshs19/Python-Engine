# LOCATION: tests/test_lrf_path_expander.py
# ACTION: REPLACE ENTIRE FILE
"""LRF path expansion tests.

ASSERTION CONTRACT
------------------
The expander KEEPS an audit trail: every expanded statement is preceded by
a '*DB2:' comment quoting the original LRF statement. That comment is a
feature, not residue, so assertions about "no LRF verb remains" must look
at EXECUTABLE lines only. Asserting against the whole output text would
forbid the audit trail.
"""

from converter.parsers.lrf_parser import LrfParser
from converter.repositories.lrf_repository import LrfRepository
from converter.resolvers.lrf_path_resolver import LrfPathResolver
from converter.transformers.lrf_path_expander import LrfPathExpander


SUBSCHEMA = """
     ADD SUBSCHEMA NAME IS VMBTS03 OF SCHEMA NAME IS VMBTSCH
         .
     ADD LOGICAL RECORD VMBTL03-R01
         ELEMENTS ARE
             VMBSIAS
             VMBFAS
         .
     ADD PATH-GROUP OBTAIN VMBTL03-R01
         SELECT FOR KEYWORD SWEEP-VMBFAS
             OBTAIN EACH VMBFAS WITHIN AR-VMBFRM1
                 ON 0307 RETURN VMBFAS-EOA
                 ON 0000 NEXT
         SELECT FOR KEYWORD VMBFAS-BY-VMBSIAS
             FIND FIRST VMBSIAS WITHIN AR-VMBFRM1
                 WHERE CALCKEY EQ KY-SIFORM OF VMBSIAS OF LR
                 ON 0326 RETURN VMBSIAS-NOT-FND
                 ON 0000 NEXT
             OBTAIN EACH VMBFAS WITHIN VMBSIAS-VMBFAS
                 ON 0000 NEXT
                 ON 0307 RETURN NO-MORE-VMBFAS
         .
"""

COMMENT_INDICATORS = ("*", "/")


# ---------------------------------------------------------------- helpers
def _expander():
    records = LrfParser().parse(SUBSCHEMA)
    resolver = LrfPathResolver(
        lrf_repository=LrfRepository(records),
        mapping_repository=None,
    )
    return LrfPathExpander(path_resolver=resolver)


def _is_comment(line: str) -> bool:
    text = str(line or "")
    if len(text) >= 7 and text[:6].strip().isdigit():
        return text[6] in COMMENT_INDICATORS
    return text.lstrip().startswith(COMMENT_INDICATORS)


def _executable(output: str) -> str:
    """Only the executable lines - comments and audit trail removed."""
    return "\n".join(
        line for line in str(output or "").splitlines()
        if line.strip() and not _is_comment(line)
    )


def _comments(output: str) -> str:
    """Only the comment lines."""
    return "\n".join(
        line for line in str(output or "").splitlines()
        if _is_comment(line)
    )


# ------------------------------------------------------------------ parser
def test_parser_reads_logical_record_and_paths():
    records = LrfParser().parse(SUBSCHEMA)
    assert len(records) == 1

    record = records[0]
    assert record.logical_record_name == "VMBTL03-R01"
    assert record.element_records == ["VMBSIAS", "VMBFAS"]
    assert {path.keyword for path in record.paths} == {
        "SWEEP-VMBFAS",
        "VMBFAS-BY-VMBSIAS",
    }


# --------------------------------------------------------------- expansion
def test_obtain_first_is_expanded_to_classic_idms():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBTL03-R01 WHERE SWEEP-VMBFAS.\n"
    )
    out = _expander().expand(source)
    code = _executable(out)

    assert "OBTAIN FIRST VMBFAS WITHIN AR-VMBFRM1." in code
    # No logical-record verb survives as EXECUTABLE code.
    assert "VMBTL03-R01" not in code
    assert "WHERE SWEEP-VMBFAS" not in code


def test_expansion_keeps_an_audit_trail():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBTL03-R01 WHERE SWEEP-VMBFAS.\n"
    )
    out = _expander().expand(source)
    notes = _comments(out)

    assert "*DB2:" in notes
    assert "VMBTL03-R01" in notes
    assert "SWEEP-VMBFAS" in notes


def test_obtain_next_is_expanded_without_parent_access():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN NEXT VMBTL03-R01 WHERE VMBFAS-BY-VMBSIAS.\n"
    )
    code = _executable(_expander().expand(source))

    assert "OBTAIN NEXT VMBFAS WITHIN VMBSIAS-VMBFAS." in code
    assert "FIND FIRST VMBSIAS" not in code


def test_obtain_first_emits_parent_access_for_join_path():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBTL03-R01 WHERE VMBFAS-BY-VMBSIAS.\n"
    )
    code = _executable(_expander().expand(source))

    assert "FIND FIRST VMBSIAS WITHIN AR-VMBFRM1." in code
    assert "OBTAIN FIRST VMBFAS WITHIN VMBSIAS-VMBFAS." in code

    # Parent must precede the child access.
    assert code.index("FIND FIRST VMBSIAS") < code.index("OBTAIN FIRST VMBFAS")


def test_expanded_names_use_cobol_hyphens_never_underscores():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBTL03-R01 WHERE SWEEP-VMBFAS.\n"
    )
    out = _expander().expand(source)

    assert "_" not in out
    assert "AR-VMBFRM1" in out


# ------------------------------------------------------------- LR-STATUS
def test_lr_status_condition_becomes_end_of_set_token():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           PERFORM BEHANDELING UNTIL LR-STATUS = 'VMBFAS-EOA'.\n"
    )
    code = _executable(_expander().expand(source))

    assert "DB-END-OF-SET" in code
    assert "LR-STATUS" not in code


def test_not_found_literal_becomes_record_not_found_token():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           IF LR-STATUS = 'VMBSIAS-NOT-FND'\n"
    )
    code = _executable(_expander().expand(source))

    assert "DB-REC-NOT-FOUND" in code
    assert "LR-STATUS" not in code


# ----------------------------------------------------------- OF LR suffix
def test_of_lr_qualifier_is_stripped():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           MOVE KY-SIFORM OF VMBSIAS OF LR TO WS-KEY.\n"
    )
    code = _executable(_expander().expand(source))

    assert "KY-SIFORM OF VMBSIAS TO WS-KEY" in code
    assert "OF LR" not in code


# ----------------------------------------------------------- safe refusal
def test_unknown_keyword_is_kept_and_commented():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBTL03-R01 WHERE UNKNOWN-KEYWORD.\n"
    )
    out = _expander().expand(source)
    notes = _comments(out)
    code = _executable(out)

    assert "*DB2-KEEP:" in notes
    assert "UNKNOWN-KEYWORD" in notes
    # Nothing was guessed: no expanded statement was emitted.
    assert "OBTAIN FIRST" not in code


# ------------------------------------------------------- no-LRF contract
def test_without_lrf_metadata_source_is_unchanged():
    resolver = LrfPathResolver(
        lrf_repository=LrfRepository([]),
        mapping_repository=None,
    )
    expander = LrfPathExpander(path_resolver=resolver)
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBTL03-R01 WHERE SWEEP-VMBFAS.\n"
    )
    assert expander.expand(source) == source


def test_program_without_lrf_syntax_is_unchanged():
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBFAS WITHIN AR-VMBFRM1.\n"
        "           MOVE NR-IS-FORM-AS OF VMBFAS TO W-NR.\n"
    )
    assert _expander().expand(source) == source


def test_no_path_resolver_returns_source_unchanged():
    expander = LrfPathExpander(path_resolver=None)
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST VMBTL03-R01 WHERE SWEEP-VMBFAS.\n"
    )
    assert expander.expand(source) == source


# ----------------------------------------------------------- safe scope
def test_data_division_lines_are_never_touched():
    source = (
        "       DATA DIVISION.\n"
        "       01 LR-STATUS PIC X(16).\n"
    )
    out = _expander().expand(source)
    assert "01 LR-STATUS PIC X(16)." in out


def test_comment_lines_are_never_expanded():
    source = (
        "       PROCEDURE DIVISION.\n"
        "      *    OBTAIN FIRST VMBTL03-R01 WHERE SWEEP-VMBFAS.\n"
    )
    out = _expander().expand(source)
    assert "OBTAIN FIRST VMBFAS" not in _executable(out)

def _fixed_line(seq: int, body: str) -> str:
    return f"{seq:06d} {body:<65}{seq:08d}"


def test_fixed_format_lrf_is_detected_without_status_or_of_lr():
    source = "\n".join([
        _fixed_line(100, "PROCEDURE DIVISION."),
        _fixed_line(110, "OBTAIN FIRST VMBTL03-R01 WHERE SWEEP-VMBFAS."),
    ]) + "\n"

    out = _expander().expand(source)
    code = _executable(out)

    assert "OBTAIN FIRST VMBFAS WITHIN AR-VMBFRM1." in code
    assert "WHERE SWEEP-VMBFAS" not in code


def test_lrf_where_can_start_on_next_fixed_format_line():
    source = "\n".join([
        _fixed_line(100, "PROCEDURE DIVISION."),
        _fixed_line(110, "OBTAIN FIRST VMBTL03-R01"),
        _fixed_line(120, "WHERE SWEEP-VMBFAS."),
    ]) + "\n"

    out = _expander().expand(source)
    code = _executable(out)

    assert "OBTAIN FIRST VMBFAS WITHIN AR-VMBFRM1." in code
    assert "OBTAIN FIRST VMBTL03-R01" not in code


def test_incomplete_obtain_does_not_consume_following_perform():
    source = "\n".join([
        _fixed_line(100, "PROCEDURE DIVISION."),
        _fixed_line(110, "OBTAIN FIRST VMBTL03-R01"),
        _fixed_line(120, "PERFORM NEXT-PARAGRAPH."),
    ]) + "\n"

    # No WHERE was found before a statement boundary, so this is not
    # classified as LRF and the source remains byte-for-byte unchanged.
    assert _expander().expand(source) == source


def test_unterminated_wrapped_lrf_does_not_swallow_next_statement():
    source = "\n".join([
        _fixed_line(100, "PROCEDURE DIVISION."),
        _fixed_line(110, "OBTAIN FIRST VMBTL03-R01"),
        _fixed_line(120, "WHERE SWEEP-VMBFAS"),
        _fixed_line(130, "PERFORM NEXT-PARAGRAPH."),
    ]) + "\n"

    out = _expander().expand(source)

    # The incomplete access is explicitly refused, while the next sentence
    # remains present and independently visible. No physical line is eaten.
    assert "*DB2-KEEP:" in out
    assert "PERFORM NEXT-PARAGRAPH." in out
    assert "OBTAIN FIRST VMBTL03-R01" in out


def test_lrf_parent_not_found_status_is_distinct_from_child_not_found():
    from rules.lrf_conversion_rules import (
        LRF_PARENT_NOT_FOUND_TOKEN,
        RECORD_NOT_FOUND_TOKEN,
    )

    expander = _expander()
    assert expander._status_token("VMBEFF-NOT-FND", parent_records={"VMBEFF"}) == LRF_PARENT_NOT_FOUND_TOKEN
    assert expander._status_token("NO-VMBEVEF-FND", parent_records={"VMBEFF"}) == RECORD_NOT_FOUND_TOKEN


def test_subschema_status_metadata_overrides_literal_name_heuristics():
    """The ON-status RETURN meaning wins over suffix-based guessing."""
    from converter.parsers.lrf_parser import LrfParser
    from converter.repositories.lrf_repository import LrfRepository
    from converter.resolvers.lrf_path_resolver import LrfPathResolver
    from converter.transformers.lrf_path_expander import LrfPathExpander

    # This deliberately gives an EOA-looking literal the NOT FOUND status.
    # The parsed subschema semantics must win over the literal's spelling.
    subschema = SUBSCHEMA.replace(
        "ON 0307 RETURN VMBFAS-EOA",
        "ON 0326 RETURN VMBFAS-EOA",
        1,
    )
    resolver = LrfPathResolver(lrf_repository=LrfRepository(LrfParser().parse(subschema)))
    expander = LrfPathExpander(path_resolver=resolver)
    output = expander.expand(
        "PROCEDURE DIVISION.\n"
        "IF LR-STATUS = 'VMBFAS-EOA'\n"
        "    DISPLAY 'NOT FOUND'\n"
        "END-IF.\n"
    )

    assert "IF DB-REC-NOT-FOUND" in output
    assert "IF DB-END-OF-SET" not in output


def test_conflicting_subschema_status_meanings_are_refused():
    """A literal with conflicting ON-status meanings must not be guessed."""
    from converter.parsers.lrf_parser import LrfParser
    from converter.repositories.lrf_repository import LrfRepository
    from converter.resolvers.lrf_path_resolver import LrfPathResolver
    from converter.transformers.lrf_path_expander import LrfPathExpander

    subschema = SUBSCHEMA.replace(
        "ON 0326 RETURN VMBSIAS-NOT-FND",
        "ON 0326 RETURN VMBFAS-EOA",
        1,
    )
    resolver = LrfPathResolver(lrf_repository=LrfRepository(LrfParser().parse(subschema)))
    expander = LrfPathExpander(path_resolver=resolver)
    source = (
        "PROCEDURE DIVISION.\n"
        "IF LR-STATUS = 'VMBFAS-EOA'\n"
        "    DISPLAY 'REVIEW STATUS'\n"
        "END-IF.\n"
    )
    output = expander.expand(source)

    assert "IF LR-STATUS = 'VMBFAS-EOA'" in output
    assert "IF DB-END-OF-SET" not in output
    assert "IF DB-REC-NOT-FOUND" not in output
    assert any("no unique meaning" in message for message in expander.messages)
