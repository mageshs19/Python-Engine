from pathlib import Path

from converter.composers.bounded_lrf_singleton_rewriter import (
    BoundedLrfSingletonRewriter,
)

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "tests" / "fixtures" / "legacy_generated" / "VMDZ4310_21-10-2026_164736.cbl"


def test_bounded_inline_lrf_cursor_becomes_singleton_select():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    result = BoundedLrfSingletonRewriter().rewrite(source)

    assert result.changed is True
    assert "FETCH FIRST 1 ROW ONLY" in result.text
    assert "CT_RKTEVPR_479EVEF = '0092'" in result.text
    assert "DECLARE DZEVEFC1 CURSOR" not in result.text
    assert "PERFORM UNTIL DZEVEFC1-EOC" not in result.text
    assert "DZEVEFC1-EOC" not in result.text
    # Rewriting must preserve the source's no-child-match business behavior.
    assert "IF SQLCODE = 100" in result.text
    assert "CALL USERABEN" in result.text
    assert "NO MORE VMBEVEF" in result.text
    assert "710-OPEN-DZEVEFC1." not in result.text
    assert "720-FETCH-DZEVEFC1." not in result.text
    assert "730-CLOSE-DZEVEFC1." not in result.text
    assert "NR_CI1POS_479EVEF" in result.text
    assert "NR_CI26POS_479EVEF" in result.text
    assert max(map(len, result.text.splitlines())) <= 80


def test_rewriter_fails_closed_without_expanded_lrf_marker():
    source = "000010 IDENTIFICATION DIVISION."
    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is False
    assert result.text == source


def test_rewriter_can_process_safe_cursor_when_unrelated_cursor_exists():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    start = next(i for i, line in enumerate(lines) if "DECLARE DZEVEFC1 CURSOR WITH HOLD FOR" in line)
    end = next(i for i in range(start, len(lines)) if "END-EXEC" in lines[i])
    extra = [line.replace("DZEVEFC1", "DZEVEFC2") for line in lines[start:end + 1]]
    # An unrelated cursor declaration without a bounded loop must not block
    # a different cursor whose complete bounded pattern can be proven.
    lines[end + 1:end + 1] = extra
    source = "\n".join(lines) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is True
    assert "DECLARE DZEVEFC1 CURSOR" not in result.text
    assert "DECLARE DZEVEFC2 CURSOR" in result.text
    assert "FETCH FIRST 1 ROW ONLY" in result.text


def test_rewriter_fails_closed_on_select_fetch_projection_mismatch():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    start = next(i for i, line in enumerate(lines) if line[7:72].strip() == "720-FETCH-DZEVEFC1.")
    end = next(i for i in range(start + 1, len(lines)) if "END-EXEC" in lines[i])
    host_line = next(i for i in range(start + 1, end) if "NR-ID-479EVEF" in lines[i] and ":DCLDZEVEFTV." in lines[i])
    del lines[host_line]
    source = "\n".join(lines) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is False
    assert "SELECT/FETCH projection mismatch" in result.diagnostic
    assert result.text == source


def test_multiline_equality_predicate_is_joined_before_classification():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    index = next(i for i, line in enumerate(lines) if "OR CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0092'" in line)
    original_line = lines[index]
    source_body = original_line[7:72].replace(" = '0092'", "")
    lines[index] = original_line[:7] + f"{source_body:<65}" + original_line[72:]
    predicate_continuation = "= '0092'"
    lines.insert(index + 1, f"{3265:06d} {predicate_continuation:<65}{3265000:08d}")
    source = "\n".join(lines) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is True
    assert "CT_RKTEVPR_479EVEF = '0092'" in result.text
    assert "DECLARE DZEVEFC1 CURSOR" not in result.text


def test_rewriter_refuses_to_remove_loop_that_contains_business_work():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    end = next(i for i, line in enumerate(lines) if "END-PERFORM." in line and i > 250)
    lines.insert(end, "003285        DISPLAY 'BUSINESS WORK MUST BE PRESERVED'                    00328500")
    source = "\n".join(lines) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is False
    assert result.text == source


def test_rewriter_refuses_nested_inline_perform_even_when_end_perform_is_same_line():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    end = next(i for i, line in enumerate(lines) if "END-PERFORM." in line and i > 250)
    # A same-line nested loop used to make the first END-PERFORM look like the
    # outer loop terminator. The renderer must preserve the entire cursor loop.
    lines.insert(end, "003285     PERFORM UNTIL INNER-DONE = 'Y' END-PERFORM           03285000")
    source = "\n".join(lines) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is False
    assert result.text == source


def test_rewriter_refuses_nested_cursor_eoc_reference_after_inner_end_if():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    eoc_if = next(i for i, line in enumerate(lines) if "IF DZEVEFC1-EOC" in line)
    end_if = next(i for i in range(eoc_if + 1, len(lines)) if "END-IF" in lines[i])
    lines.insert(end_if, "003395        IF WS-ANOTHER-CONDITION = 'Y'                     03395000")
    lines.insert(end_if + 1, "003396           DISPLAY 'INNER BRANCH'                         03396000")
    lines.insert(end_if + 2, "003397        END-IF                                              03397000")
    # This reference is nested under the outer EOC branch but occurs after
    # the first (inner) END-IF. The whole rewrite must refuse, not leave a
    # dangling reference after deleting the cursor's generated flag.
    lines.insert(end_if + 3, "003398        IF DZEVEFC1-EOC                                      03398000")
    lines.insert(end_if + 4, "003399           DISPLAY 'NESTED EOC'                             03399000")
    lines.insert(end_if + 5, "003400        END-IF                                              03400000")
    source = "\n".join(lines) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is False
    assert "Nested cursor EOC reference in not-found branch" in result.diagnostic
    assert result.text == source


def test_matching_eoc_branch_ignores_end_if_text_inside_literal():
    source = GENERATED.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    eoc_if = next(i for i, line in enumerate(lines) if "IF DZEVEFC1-EOC" in line)
    lines.insert(eoc_if + 1, "003335        DISPLAY 'TEXT END-IF IS NOT A TERMINATOR'           03335000")
    source = "\n".join(lines) + "\n"

    result = BoundedLrfSingletonRewriter().rewrite(source)
    assert result.changed is True
    assert "IF SQLCODE = 100" in result.text
    assert "TEXT END-IF IS NOT A TERMINATOR" in result.text


def test_find_end_exec_supports_long_sql_declarations_beyond_80_lines():
    bodies = ["DECLARE CURSOR-A CURSOR"] + [f"COLUMN-{index} = :HOST-{index}" for index in range(1, 90)] + ["END-EXEC."]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) == len(bodies) - 1


def test_find_end_exec_fails_closed_at_new_sql_block_before_terminator():
    bodies = [
        "DECLARE CURSOR-A CURSOR",
        "SELECT COL-A FROM TABLE-A",
        "EXEC SQL",
        "DECLARE CURSOR-B CURSOR",
        "END-EXEC.",
    ]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) is None


def test_find_end_exec_fails_closed_at_numeric_paragraph_before_terminator():
    bodies = [
        "DECLARE CURSOR-A CURSOR",
        "SELECT COL-A FROM TABLE-A",
        "100-PROCESS-ROW.",
        "PERFORM 200-NEXT-ROW.",
        "END-EXEC.",
    ]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) is None




def test_find_end_exec_fails_closed_at_named_area_a_paragraph_before_terminator():
    bodies = [
        "DECLARE CURSOR-A CURSOR",
        "SELECT COL-A FROM TABLE-A",
        "MAIN-PROCESS-PARA.",
        "DISPLAY 'OTHER PROCEDURE CODE'",
        "END-EXEC.",
    ]
    source_lines = [
        f"{index * 10:06d} {body:<65}{index * 10000:08d}"
        for index, body in enumerate(bodies, start=1)
    ]

    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0, source_lines) is None


def test_find_end_exec_does_not_treat_indented_sql_clause_as_paragraph():
    bodies = [
        "DECLARE CURSOR-A CURSOR",
        "SELECT COL-A FROM TABLE-A",
        "ORDER BY COL-A",
        "END-EXEC.",
    ]
    source_lines = [
        f"{index * 10:06d} {'    ' + body if index in (2, 3) else body:<65}{index * 10000:08d}"
        for index, body in enumerate(bodies, start=1)
    ]

    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0, source_lines) == 3


def test_update_where_projection_supports_sql_statement_beyond_100_lines():
    bodies = [
        "EXEC SQL",
        "UPDATE TARGET_TABLE SET VALUE_COL = :INPUT-VALUE WHERE KEY_COL = :KEY-HOST",
    ]
    bodies.extend(f"AND EXTRA_COL_{index} IS NOT NULL" for index in range(1, 105))
    bodies.append("END-EXEC.")
    source_lines = [
        f"{index * 10:06d} {body:<65}{index * 10000:08d}"
        for index, body in enumerate(bodies, start=1)
    ]

    projection = BoundedLrfSingletonRewriter._update_where_projection(
        ["KEY_COL", "VALUE_COL"],
        ["KEY-HOST", "INPUT-VALUE"],
        bodies,
        after=-1,
        excluded_spans=(),
        source_lines=source_lines,
    )

    assert projection == (["KEY_COL"], ["KEY-HOST"])


def test_update_where_projection_ignores_end_exec_in_fixed_format_comment():
    bodies = [
        "EXEC SQL",
        "UPDATE TARGET_TABLE SET VALUE_COL = :INPUT-VALUE WHERE KEY_COL = :KEY-HOST",
        "* END-EXEC. THIS IS ONLY A COMMENT",
        "AND EXTRA_COL IS NOT NULL",
        "END-EXEC.",
    ]
    source_lines = []
    for index, body in enumerate(bodies, start=1):
        indicator = "*" if body.startswith("* ") else " "
        content = body[2:] if indicator == "*" else body
        source_lines.append(f"{index * 10:06d}{indicator}{content:<65}{index * 10000:08d}")

    projection = BoundedLrfSingletonRewriter._update_where_projection(
        ["KEY_COL", "VALUE_COL"],
        ["KEY-HOST", "INPUT-VALUE"],
        bodies,
        after=-1,
        excluded_spans=(),
        source_lines=source_lines,
    )

    assert projection == (["KEY_COL"], ["KEY-HOST"])


def test_find_end_exec_ignores_terminator_text_in_sql_literal():
    bodies = [
        "EXEC SQL",
        "SELECT 'END-EXEC' AS LABEL FROM TABLE_A",
        "WHERE KEY_COL = :KEY-HOST",
        "END-EXEC.",
    ]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) == 3


def test_find_end_exec_ignores_terminator_text_in_sql_line_comment():
    bodies = [
        "EXEC SQL",
        "SELECT COL_A FROM TABLE_A -- END-EXEC is only a comment",
        "WHERE KEY_COL = :KEY-HOST",
        "END-EXEC.",
    ]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) == 3


def test_find_end_exec_ignores_terminator_text_in_multiline_sql_block_comment():
    bodies = [
        "EXEC SQL",
        "SELECT COL_A FROM TABLE_A",
        "/* documentation mentions END-EXEC here",
        "and continues on another line */",
        "WHERE KEY_COL = :KEY-HOST",
        "END-EXEC.",
    ]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) == 5


def test_find_end_exec_ignores_terminator_text_after_cobol_inline_comment_marker():
    bodies = [
        "EXEC SQL",
        "SELECT COL_A FROM TABLE_A *> END-EXEC is not executable",
        "WHERE KEY_COL = :KEY-HOST",
        "END-EXEC.",
    ]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) == 3


def test_find_end_exec_keeps_quote_state_across_physical_lines():
    bodies = [
        "EXEC SQL",
        "SELECT 'literal begins here",
        "END-EXEC is still literal data', COL_A FROM TABLE_A",
        "END-EXEC.",
    ]
    assert BoundedLrfSingletonRewriter._find_end_exec(bodies, 0) == 3
