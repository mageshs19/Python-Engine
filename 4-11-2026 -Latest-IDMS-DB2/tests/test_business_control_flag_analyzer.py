from converter.composers.cleanup.business_control_flag_analyzer import (
    BusinessControlFlagAnalyzer,
)


def test_discovers_flag_declaration_and_trigger_condition_without_name_rule():
    source = """WORKING-STORAGE SECTION.
01 SW-CHILD-STOP PIC X VALUE 'N'.
PROCEDURE DIVISION.
PROCESS-CHILD.
    IF EVENT-CODE = '0168' AND EVENT-STATUS NOT = '1'
        MOVE 'Y' TO SW-CHILD-STOP
    END-IF.
"""
    evidence = BusinessControlFlagAnalyzer().analyze(source)

    assert "SW-CHILD-STOP" in evidence
    flag = evidence["SW-CHILD-STOP"]
    assert flag.declared is True
    assert flag.assignments[0]["paragraph"] == "PROCESS-CHILD"
    assert "EVENT-CODE = '0168'" in flag.trigger_conditions[0]
    assert "EVENT-STATUS NOT = '1'" in flag.trigger_conditions[0]


def test_discovery_returns_none_when_multiple_flags_have_equal_evidence():
    source = """PROCEDURE DIVISION.
PROCESS-CHILD.
    IF CONDITION-A
        MOVE 'Y' TO STOP-A
    END-IF
    IF CONDITION-B
        MOVE 'Y' TO STOP-B
    END-IF.
"""
    analyzer = BusinessControlFlagAnalyzer()
    assert analyzer.discover_unique_yes_flag(
        source.splitlines(), {"PROCESS-CHILD"}
    ) is None


def test_discovery_ignores_flags_not_assigned_in_the_requested_scope():
    source = """PROCEDURE DIVISION.
PARENT-ROW.
    MOVE 'Y' TO PARENT-FLAG.
CHILD-ROW.
    IF EVENT-CODE = 'X'
        MOVE 'Y' TO CHILD-FLAG
    END-IF.
"""
    analyzer = BusinessControlFlagAnalyzer()
    assert analyzer.discover_unique_yes_flag(
        source.splitlines(), {"CHILD-ROW"}
    ) == "CHILD-FLAG"


def test_flag_name_does_not_need_sw_status_prefix():
    source = """PROCEDURE DIVISION.
PROCESS-CHILD.
    IF EVENT-TYPE = 'STOP'
        MOVE 'Y' TO STOP-NEXT-CHILD
    END-IF.
"""
    analyzer = BusinessControlFlagAnalyzer()
    assert analyzer.discover_unique_yes_flag(
        source.splitlines(), {"PROCESS-CHILD"}
    ) == "STOP-NEXT-CHILD"
