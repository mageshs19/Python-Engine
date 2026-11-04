from types import SimpleNamespace

from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter
from converter.resolvers.lrf_cursor_where_resolver import LrfCursorWhereResolver


def fixed(body, indicator=" "):
    return f"000100{indicator}{body:<65}00010000"


def test_wrapped_lrf_marker_preserves_path_filters_and_maps_them_to_db2_columns():
    source = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("DB2: LRF ALL-CHILD-BY-PARENT extra filter: SRC-TYPE = 'A1'", "*"),
        fixed("AND SRC-STATUS = '02' - add to the generated cursor WHERE.", "*"),
    ])
    rows = [
        SimpleNamespace(cobol_zone="SRC-TYPE", reference_field_name_copybook="", new_db2_field_name="DB2_TYPE", cross_application_db2_field_name=""),
        SimpleNamespace(cobol_zone="SRC-STATUS", reference_field_name_copybook="", new_db2_field_name="DB2_STATUS", cross_application_db2_field_name=""),
    ]

    class Mapping:
        def rows_for_record(self, record):
            assert record == "CHILD"
            return rows

    resolver = LrfCursorWhereResolver(mapping_repository=Mapping())
    info = resolver.extract_lrf_cursors_from_cobol(source)
    assert info["CHILD"]["extra_filters"] == "SRC-TYPE = 'A1' AND SRC-STATUS = '02'"
    assert resolver.extra_filter_conditions_for_lrf_cursor("CHILD", info["CHILD"]) == [
        "DB2_TYPE = 'A1'",
        "DB2_STATUS = '02'",
    ]


def test_source_proven_first_only_cursor_is_rewritten_to_singleton_select():
    source_idms = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("DB2: LRF ALL-CHILD-BY-PARENT extra filter: DB2_TYPE = 'A1'", "*"),
        fixed("- add to the generated cursor WHERE.", "*"),
        # The expanded LRF marker is the surviving provenance here; the
        # original OBTAIN statement has already been consumed by expansion.
        fixed("MODIFY LR-EVENT WHERE MOD-CHILD."),
    ])
    output = "\n".join([
        fixed("WORKING-STORAGE SECTION."),
        fixed("EXEC SQL DECLARE C1 CURSOR FOR"),
        fixed(" SELECT DB2_ID, DB2_VALUE"),
        fixed(" FROM DB2_CHILD"),
        fixed(" WHERE DB2_PARENT_ID = :DCLPARENT.PARENT_ID"),
        fixed(" AND DB2_TYPE = 'A1'"),
        fixed(" ORDER BY DB2_ID DESC"),
        fixed(" QUERYNO 123"),
        fixed("END-EXEC"),
        fixed("01 WS-C1-FLAG PIC X."),
        fixed(" 88 C1-EOC VALUE 'Y'."),
        fixed("PROCEDURE DIVISION."),
        fixed(" PERFORM 710-OPEN-C1."),
        fixed(" PERFORM 720-FETCH-C1 UNTIL C1-EOC."),
        fixed(" PERFORM 730-CLOSE-C1."),
        fixed(" IF NOT SQLCODE = 0"),
        fixed("   CALL USERABEN"),
        fixed(" END-IF."),
        fixed(" MOVE DCLCHILD.DB2-VALUE TO WS-VALUE."),
        fixed(" MOVE 710 TO SQL-LOCATION."),
        fixed(" EXEC SQL"),
        fixed(" UPDATE DB2_CHILD"),
        fixed(" SET DB2_VALUE = :DCLCHILD.DB2-VALUE"),
        fixed(" WHERE DB2_ID = :DCLCHILD.DB2-ID"),
        fixed(" END-EXEC."),
        fixed("710-OPEN-C1."),
        fixed(" EXEC SQL OPEN C1 END-EXEC."),
        fixed("720-FETCH-C1."),
        fixed(" EXEC SQL FETCH C1 INTO :DCLCHILD.DB2-ID, :DCLCHILD.DB2-VALUE END-EXEC."),
        fixed("730-CLOSE-C1."),
        fixed(" EXEC SQL CLOSE C1 END-EXEC."),
    ]) + "\n"

    stale_output = "\n".join(
        line for line in output.splitlines() if "AND DB2_TYPE = 'A1'" not in line
    ) + "\n"
    stale_result = BoundedLrfSingletonRewriter().rewrite(
        stale_output, original_idms_text=source_idms
    )
    assert not stale_result.changed
    assert "source LRF path filters are absent" in stale_result.diagnostic

    result = BoundedLrfSingletonRewriter().rewrite(output, original_idms_text=source_idms)
    assert result.changed, result.diagnostic
    assert "DECLARE C1 CURSOR" not in result.text
    assert "FETCH FIRST 1 ROW ONLY" in result.text
    assert "AND DB2_TYPE = 'A1'" in result.text
    assert "PERFORM 720-FETCH-C1 UNTIL C1-EOC" not in result.text
    assert "UPDATE DB2_CHILD" in result.text




def test_lrf_extra_filter_resolution_fails_closed_when_mapping_is_ambiguous():
    source = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("DB2: LRF ALL-CHILD-BY-PARENT extra filter: SRC-TYPE = 'A1'", "*"),
        fixed("- add to the generated cursor WHERE.", "*"),
    ])
    duplicate_rows = [
        SimpleNamespace(cobol_zone="SRC-TYPE", reference_field_name_copybook="", new_db2_field_name="DB2_TYPE_A", cross_application_db2_field_name=""),
        SimpleNamespace(cobol_zone="SRC-TYPE", reference_field_name_copybook="", new_db2_field_name="DB2_TYPE_B", cross_application_db2_field_name=""),
    ]

    class Mapping:
        def rows_for_record(self, record):
            return duplicate_rows

    resolver = LrfCursorWhereResolver(mapping_repository=Mapping())
    info = resolver.extract_lrf_cursors_from_cobol(source)
    assert resolver.extra_filter_conditions_for_lrf_cursor("CHILD", info["CHILD"]) is None
    assert any("could not be mapped" in message for message in resolver.messages)


def test_ordinary_program_without_lrf_source_is_unchanged():
    output = fixed("EXEC SQL DECLARE C1 CURSOR FOR") + "\n"
    result = BoundedLrfSingletonRewriter().rewrite(output)
    assert not result.changed
    assert result.text == output



def test_legacy_add_to_cursor_where_directive_becomes_mapped_lrf_filter():
    source = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("AND SRC-STATUS = '02' - add to the generated cursor WHERE.", "*"),
    ])
    rows = [
        SimpleNamespace(
            cobol_zone="SRC-STATUS-CHILD",
            reference_field_name_copybook="",
            new_db2_field_name="DB2_STATUS",
            cross_application_db2_field_name="",
        ),
    ]

    class Mapping:
        def rows_for_record(self, record):
            assert record == "CHILD"
            return rows

    resolver = LrfCursorWhereResolver(mapping_repository=Mapping())
    info = resolver.extract_lrf_cursors_from_cobol(source)
    assert info["CHILD"]["extra_filters"] == "SRC-STATUS = '02'"
    assert resolver.extra_filter_conditions_for_lrf_cursor("CHILD", info["CHILD"]) == [
        "DB2_STATUS = '02'",
    ]


def test_marker_first_fallback_does_not_rewrite_when_matching_next_exists():
    source_idms = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("FIND NEXT CHILD WITHIN PARENT-CHILD."),
    ])
    output = "\n".join([
        fixed("EXEC SQL DECLARE C1 CURSOR FOR"),
        fixed(" SELECT DB2_ID, DB2_VALUE"),
        fixed(" FROM DB2_CHILD"),
        fixed(" WHERE DB2_PARENT_ID = :DCLPARENT.PARENT_ID"),
        fixed(" AND DB2_TYPE = 'A1'"),
        fixed(" ORDER BY DB2_ID DESC"),
        fixed(" QUERYNO 123"),
        fixed("END-EXEC"),
        fixed("PROCEDURE DIVISION."),
        fixed(" PERFORM 710-OPEN-C1."),
        fixed(" PERFORM 720-FETCH-C1 UNTIL C1-EOC."),
        fixed(" PERFORM 730-CLOSE-C1."),
        fixed(" MOVE DCLCHILD.DB2-VALUE TO WS-VALUE."),
        fixed("710-OPEN-C1."),
        fixed(" EXEC SQL OPEN C1 END-EXEC."),
        fixed("720-FETCH-C1."),
        fixed(" EXEC SQL FETCH C1 INTO :DCLCHILD.DB2-ID, :DCLCHILD.DB2-VALUE END-EXEC."),
        fixed("730-CLOSE-C1."),
        fixed(" EXEC SQL CLOSE C1 END-EXEC."),
    ]) + "\n"
    result = BoundedLrfSingletonRewriter().rewrite(output, original_idms_text=source_idms)
    assert not result.changed
    assert "DECLARE C1 CURSOR" in result.text


def test_first_only_rewrite_refuses_when_legacy_cursor_where_filter_is_missing():
    source_idms = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("AND SRC-STATUS = '02' - add to the generated cursor WHERE.", "*"),
    ])
    output = "\n".join([
        fixed("EXEC SQL DECLARE C1 CURSOR FOR"),
        fixed(" SELECT DB2_ID, DB2_VALUE"),
        fixed(" FROM DB2_CHILD"),
        fixed(" WHERE DB2_PARENT_ID = :DCLPARENT.PARENT_ID"),
        fixed(" ORDER BY DB2_ID DESC"),
        fixed(" QUERYNO 123"),
        fixed("END-EXEC"),
        fixed("PROCEDURE DIVISION."),
        fixed(" PERFORM 710-OPEN-C1."),
        fixed(" PERFORM 720-FETCH-C1 UNTIL C1-EOC."),
        fixed(" PERFORM 730-CLOSE-C1."),
        fixed(" MOVE DCLCHILD.DB2-VALUE TO WS-VALUE."),
        fixed("710-OPEN-C1."),
        fixed(" EXEC SQL OPEN C1 END-EXEC."),
        fixed("720-FETCH-C1."),
        fixed(" EXEC SQL FETCH C1 INTO :DCLCHILD.DB2-ID, :DCLCHILD.DB2-VALUE END-EXEC."),
        fixed("730-CLOSE-C1."),
        fixed(" EXEC SQL CLOSE C1 END-EXEC."),
    ]) + "\n"
    result = BoundedLrfSingletonRewriter().rewrite(output, original_idms_text=source_idms)
    assert not result.changed
    assert "source LRF path filters are absent" in result.diagnostic
    assert "DECLARE C1 CURSOR" in result.text


def test_first_only_update_selects_only_update_key_not_set_payload():
    source_idms = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("DB2: LRF ALL-CHILD-BY-PARENT extra filter: DB2_TYPE = 'A1'", "*"),
        fixed("- add to the generated cursor WHERE.", "*"),
        fixed("MODIFY LR-EVENT WHERE MOD-CHILD."),
    ])
    output = "\n".join([
        fixed("EXEC SQL DECLARE C1 CURSOR FOR"),
        fixed(" SELECT DB2_ID, DB2_VALUE"),
        fixed(" FROM DB2_CHILD"),
        fixed(" WHERE DB2_PARENT_ID = :DCLPARENT.PARENT_ID"),
        fixed(" AND DB2_TYPE = 'A1'"),
        fixed(" ORDER BY DB2_ID DESC"),
        fixed(" QUERYNO 123"),
        fixed("END-EXEC"),
        fixed("PROCEDURE DIVISION."),
        fixed(" PERFORM 710-OPEN-C1."),
        fixed(" PERFORM 720-FETCH-C1 UNTIL C1-EOC."),
        fixed(" PERFORM 730-CLOSE-C1."),
        fixed(" MOVE WS-NEW-VALUE TO DCLCHILD.DB2-VALUE."),
        fixed(" EXEC SQL"),
        fixed(" UPDATE DB2_CHILD"),
        fixed(" SET DB2_VALUE = :DCLCHILD.DB2-VALUE"),
        fixed(" WHERE DB2_ID = :DCLCHILD.DB2-ID"),
        fixed(" END-EXEC."),
        fixed("710-OPEN-C1."),
        fixed(" EXEC SQL OPEN C1 END-EXEC."),
        fixed("720-FETCH-C1."),
        fixed(" EXEC SQL FETCH C1 INTO :DCLCHILD.DB2-ID, :DCLCHILD.DB2-VALUE END-EXEC."),
        fixed("730-CLOSE-C1."),
        fixed(" EXEC SQL CLOSE C1 END-EXEC."),
    ]) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(output, original_idms_text=source_idms)
    assert result.changed, result.diagnostic
    sql_start = result.text.index("SELECT DB2_ID")
    sql_end = result.text.index("END-EXEC", sql_start)
    singleton_sql = result.text[sql_start:sql_end]
    assert "SELECT DB2_ID" in singleton_sql
    assert "DB2_VALUE" not in singleton_sql
    assert "FETCH FIRST 1 ROW ONLY" in singleton_sql
    # The UPDATE still uses the new business value; the lookup must not fetch
    # the old DB2_VALUE into that same DCLGEN host variable.
    assert "SET DB2_VALUE = :DCLCHILD.DB2-VALUE" in result.text


def test_lrf_filter_mapping_ignores_cobol_level_prefix_in_mapping_sheet():
    source = "\n".join([
        fixed("DB2: Expanded LRF FIRST LR-EVENT WHERE ALL-CHILD-BY-PARENT", "*"),
        fixed("-> CHILD WITHIN PARENT-CHILD.", "*"),
        fixed("DB2: LRF ALL-CHILD-BY-PARENT extra filter: CT-RK-TEVPR = '0168'", "*"),
        fixed("AND CT-RK-TGDSV = '0219' - add to the generated cursor WHERE.", "*"),
    ])
    rows = [
        SimpleNamespace(cobol_zone="03 CT-RK-TEVPR", reference_field_name_copybook="", new_db2_field_name="CT_RKTEVPR_479EVEF", cross_application_db2_field_name=""),
        SimpleNamespace(cobol_zone="04 CT-RK-TGDSV", reference_field_name_copybook="", new_db2_field_name="CT_RKTGDSV_479EVEF", cross_application_db2_field_name=""),
    ]

    class Mapping:
        def rows_for_record(self, record):
            assert record == "CHILD"
            return rows

    resolver = LrfCursorWhereResolver(mapping_repository=Mapping())
    info = resolver.extract_lrf_cursors_from_cobol(source)
    assert resolver.extra_filter_conditions_for_lrf_cursor("CHILD", info["CHILD"]) == [
        "CT_RKTEVPR_479EVEF = '0168'",
        "CT_RKTGDSV_479EVEF = '0219'",
    ]
