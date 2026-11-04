from converter.composers.lrf_key_binding_composer import LrfKeyBindingComposer


def test_key_moves_are_inserted_after_initialize_and_before_open():
    text = """SEARCH-MUTATIES.
    INITIALIZE DCLDZEVEFTV.
    PERFORM 710-OPEN-DZEVEFC1.
    PERFORM 720-FETCH-DZEVEFC1.
"""
    moves = {"DCLDZEVEFTV": ["MOVE KEY-FIELD OF DCLDZBEFFTV TO KEY-FIELD OF DCLDZEVEFTV."]}
    composer = LrfKeyBindingComposer()
    result = composer.compose(text, moves)
    assert result.index("INITIALIZE DCLDZEVEFTV") < result.index("MOVE KEY-FIELD") < result.index("PERFORM 710-OPEN-DZEVEFC1")
    assert not composer.messages or "LRF key propagation" in " ".join(composer.messages)


def test_parent_status_block_is_removed_and_post_close_uses_eoc_flag():
    text = """SEARCH-MUTATIES.
    IF DB-LRF-PARENT-NOT-FOUND
       DISPLAY 'PARENT NOT FOUND'
       CALL USERABEN
    END-IF.
    PERFORM 730-CLOSE-DZEVEFC1.
    IF SQLCODE = 100
       DISPLAY 'NO MORE CHILD'
    END-IF.
"""
    composer = LrfKeyBindingComposer()
    result = composer.compose(text)
    assert "DB-LRF-PARENT-NOT-FOUND" not in result
    assert "PARENT NOT FOUND" not in result
    assert "IF DZEVEFC1-EOC" in result


def test_loop_uses_cursor_eoc_flag_when_fetch_in_same_perform_block():
    text = """SEARCH-MUTATIES.
    PERFORM UNTIL SQLCODE = 100
       OR CT-EVENT = '0092'
       PERFORM 720-FETCH-DZEVEFC1
    END-PERFORM.
"""
    composer = LrfKeyBindingComposer()
    result = composer.compose(text)
    assert "PERFORM UNTIL DZEVEFC1-EOC" in result
    assert "SQLCODE = 100" not in result
