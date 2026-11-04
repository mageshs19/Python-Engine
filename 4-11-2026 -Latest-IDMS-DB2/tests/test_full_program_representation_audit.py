from pathlib import Path
from dataclasses import replace
import re
import pytest

from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.composers.program_identity_initializer import ProgramIdentityInitializer
from mainframe.verification.group_representation_contract import (
    audit_character_group_moves, audit_target_character_widths,
)
from review.engine.context import ReviewContext
from review.engine.reviewer import Reviewer, is_accepted, blockers
from review.engine.check_base import Check, CRITICAL
from review.checks.chk_35_group_representation import GroupRepresentationCheck
from review.checks.chk_36_production_evidence import ProductionEvidenceCheck
from review.checks.chk_04_program_header import CSPG
from review.checks.chk_24_picture_and_length import picture_category,picture_length
from review.runner.workspace_inputs import WorkspaceReviewInputs
from review.runner.review_file import build_context

ROOT=Path(__file__).resolve().parents[1]
COL=DclgenColumn(table_name='DZTESTTV',column_name='ID_SERIAL',cobol_host_name='ID-SERIAL',
                 db2_type='CHAR(28) NOT NULL',cobol_picture='X(28)')
PACKED='''IDENTIFICATION DIVISION.
PROGRAM-ID. SAMPLE.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 DEST-KEY.
 05 PART-A PIC 9(8) COMP-3.
 05 PART-B PIC 9(8) COMP-3.
 05 PART-C PIC 9(6) COMP-3.
 05 PART-D PIC 9(3) COMP-3.
 05 PART-E PIC 9(3) COMP-3.
 05 FILLER PIC XX VALUE SPACES.
PROCEDURE DIVISION.
MAIN.
 MOVE ID-SERIAL OF DCLDZTESTTV TO DEST-KEY.
 STOP RUN.
'''

def fixed(text):
    return '\n'.join(f'{i*10:06d} '+s.ljust(65)+f'{i*1000:08d}'
                     for i,s in enumerate(text.splitlines(),1))+'\n'

@pytest.mark.parametrize('formatter',[str,fixed])
def test_character_group_to_packed_is_blocked(formatter):
    findings=audit_character_group_moves(formatter(PACKED),[COL])
    assert len(findings)==1
    assert findings[0].code=='UNCONVERTED-CHARACTER-GROUP'
    assert '20-byte group' in findings[0].message

@pytest.mark.parametrize('width',[20,28,30])
def test_same_length_does_not_prove_binary_encoding(width):
    assert audit_character_group_moves(PACKED,[replace(COL,db2_type=f'CHAR({width})')])

@pytest.mark.parametrize('name',['CUSTOM-KEY','RENAMED-PAYLOAD','GROUP-987'])
def test_rule_is_not_driven_by_names(name):
    text=PACKED.replace('DEST-KEY',name).replace('PART-A','OTHER-ONE')
    assert audit_character_group_moves(text,[COL])[0].target==name


def test_display_group_and_elementary_numeric_move_not_misclassified():
    assert not audit_character_group_moves(PACKED.replace(' COMP-3',''),[COL])
    text=PACKED.replace('TO DEST-KEY.','TO PART-A.')
    assert not audit_character_group_moves(text,[COL])


def test_comments_literals_and_storage_values_do_not_become_moves():
    text=PACKED.replace(' MOVE ID-SERIAL OF DCLDZTESTTV TO DEST-KEY.',
                       " DISPLAY 'MOVE ID-SERIAL OF DCLDZTESTTV TO DEST-KEY.'.\n"
                       '* MOVE ID-SERIAL OF DCLDZTESTTV TO DEST-KEY.')
    assert not audit_character_group_moves(text,[COL])


def test_nested_receiving_group_and_wrapped_transfer():
    text=PACKED.replace('01 DEST-KEY.','01 OUTER.\n 02 DEST-KEY.').replace(
        'MOVE ID-SERIAL OF DCLDZTESTTV TO DEST-KEY.',
        'MOVE ID-SERIAL OF DCLDZTESTTV\n TO DEST-KEY OF OUTER.')
    assert audit_character_group_moves(text,[COL])


def test_character_contract_conflict_only_for_used_host():
    row=SheetMappingRow(new_db2_record='DZTESTTV',new_db2_field_name='ID_SERIAL',new_db2_data_type='CHAR (20)')
    assert len(audit_target_character_widths(PACKED,[row],[COL]))==1
    assert not audit_target_character_widths('DISPLAY "ID-SERIAL".',[row],[COL])
    assert not audit_target_character_widths(PACKED,[replace(row,new_db2_data_type='CHAR(28)')],[COL])


IDENTITY='''IDENTIFICATION DIVISION.
PROGRAM-ID. SAMPLE.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 CS-PROGRAM PIC X(8) VALUE 'SAMPLE'.
EXEC SQL INCLUDE SQLERRWS END-EXEC.
PROCEDURE DIVISION.
MAIN.
    PERFORM STARTUP.
    STOP RUN.
STARTUP.
    CONTINUE.
'''

@pytest.mark.parametrize('formatter',[str,fixed])
def test_generic_diagnostic_identity_is_first_executable_statement(formatter):
    source=formatter(IDENTITY)
    result=ProgramIdentityInitializer().compose(source)
    assert result.index('MOVE CS-PROGRAM TO PROGRAM-NAME')<result.index('PERFORM STARTUP')
    assert result.count('MOVE CS-PROGRAM TO PROGRAM-NAME')==1
    assert ProgramIdentityInitializer().compose(result)==result

@pytest.mark.parametrize('source',[
    IDENTITY.replace("VALUE 'SAMPLE'","VALUE 'DIFFERENT'"),
    IDENTITY.replace('EXEC SQL INCLUDE SQLERRWS END-EXEC.',''),
    IDENTITY.replace('MAIN.','DECLARATIVES.\nMAIN.'),
    IDENTITY.replace('CONTINUE.','MOVE CS-PROGRAM TO PROGRAM-NAME.'),
])
def test_identity_does_not_guess_or_override_author_defined_assignment(source):
    assert ProgramIdentityInitializer().compose(source)==source

@pytest.mark.parametrize('pic,category,length',[
 ('S9(1)V USAGE COMP-3.','NUMERIC',1),
 ('S9(13)V99 USAGE COMP-3.','NUMERIC',15),
 ('PIC 9(4 ) COMP-3','NUMERIC',4),
 ('X(10) VALUE SPACES.','ALPHANUMERIC',10),
 ('PICTURE IS X(28).','ALPHANUMERIC',28),
])
def test_picture_parser_ignores_usage_and_value_tokens(pic,category,length):
    assert picture_category(pic)==category
    assert picture_length(pic)==length


def test_cs_program_parentheses_are_not_regex_end_anchors():
    assert CSPG.fullmatch("10 CS-PROGRAM PIC X(8) VALUE 'SAMPLE'.")


def test_exception_in_critical_check_cannot_pass_review():
    class Broken(Check):
        CHECK_ID='CHK-X'
        SEVERITY=CRITICAL
        def review(self,ctx,view,record):
            raise ValueError('missing evidence')
    result=Reviewer([Broken()]).review(ReviewContext(converted_cobol=PACKED))
    assert result.blocked==1
    assert not is_accepted(result)
    assert blockers(result)[0].check_id=='CHK-X'


def test_missing_metadata_blocks_requested_production_review():
    ctx=ReviewContext(converted_cobol=IDENTITY,require_metadata=True)
    assert not is_accepted(Reviewer([ProductionEvidenceCheck()]).review(ctx))


def test_real_current_member_fails_representation_not_paragraph_numbering():
    inputs=WorkspaceReviewInputs(ROOT/'mainframe/workspace')
    # Validate the immutable pre-audit source fixture supplied for this audit,
    # not an old historical "Validated Output" member.
    generated=ROOT/'tests/fixtures/representation_v122/VMDZ4310.cbl'
    ctx=build_context(generated,'UNKNOWN','',workspace_inputs=inputs)
    assert not ctx.metadata_diagnostics
    assert ctx.source_cobol
    assert len(ctx.dclgen_columns)==38
    result=Reviewer([GroupRepresentationCheck(),ProductionEvidenceCheck()]).review(ctx)
    assert not is_accepted(result)
    assert result.checks[0].failed==2
    assert result.checks[1].failed==0


def test_manual_numbering_does_not_change_the_nine_local_business_edges():
    from converter.analyzers.program_flow.procedure_control_flow_graph import ProcedureControlFlowGraphBuilder
    original=(ROOT/'tests/fixtures/representation_v122/VMDZ4310.cbl').read_text(encoding='latin1')
    manual=(ROOT/'mainframe/workspace/Manual Output/VMDZ4310.txt').read_text(encoding='latin1')
    def edges(text):
        graph=ProcedureControlFlowGraphBuilder().build(text)
        assert not graph.diagnostics
        assert not [edge for edge in graph.edges if edge.resolution in {'missing','ambiguous'}]
        local=[edge for edge in graph.edges if edge.resolution=='local']
        assert len(local)==9
        normalize=lambda label: re.sub(r'^\d+-','',label)
        return {(normalize(edge.source),normalize(edge.target)) for edge in local}
    assert edges(original)==edges(manual)
    assert edges(ProgramIdentityInitializer().compose(original))==edges(original)


def test_workspace_metadata_failure_is_reported_not_success(tmp_path):
    adapter=WorkspaceReviewInputs(tmp_path)
    result=adapter.for_program(IDENTITY)
    assert any('mapping' in note for note in result.diagnostics)
    assert any('DCLGEN' in note for note in result.diagnostics)
    assert any('original source' in note for note in result.diagnostics)
