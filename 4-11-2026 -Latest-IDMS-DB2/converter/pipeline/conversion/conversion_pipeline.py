# LOCATION: converter/pipeline/conversion/conversion_pipeline.py
# ACTION: REPLACE ENTIRE FILE
from __future__ import annotations

import os

from converter.analyzers.program_flow_analyzer import ProgramFlowAnalyzer
from converter.composers.lrf_key_binding_composer import LrfKeyBindingComposer
from converter.composers.bounded_lrf_singleton_rewriter import (
    BoundedLrfSingletonRewriter,
)
from converter.composers.lrf_group_move_decomposer import LrfGroupMoveDecomposer
from converter.domain.models import ConversionInput
from converter.pipeline.conversion.conversion_layout_pipeline import (
    ConversionLayoutPipeline,
)
from converter.pipeline.conversion.conversion_pipeline_steps import (  # noqa: F401
    GATE_LEGACY_RESTART_GENERATOR,
    LEGACY_RESTART_SKIPPED,
    RESTART_DCLGEN_CLASS,
    RESTART_DCLGEN_MODULE,
    ConversionPipelineSteps,
)
from converter.validators.mapping_scope_filter import MappingScopeFilter
from converter.validators.mapping_validator import MappingValidator

from converter.rules.common_rules import (
    DEFAULT_ENABLE_LRF_SINGLETON_SHORTCUT,
    ENV_ENABLE_LRF_SINGLETON_SHORTCUT,
    LABEL_LR_STATUS,
    LABEL_LRF_READ,
    LABEL_LRF_UPDATE,
    LRF_STAGE_FAILED_TEMPLATE,
    LRF_STAGE_NO_METHOD_TEMPLATE,
    LRF_STAGE_NOT_WIRED_TEMPLATE,
    METHOD_APPLY,
    METHOD_EXPAND,
    TRANSFORMER_LR_STATUS_REPLACER,
    TRANSFORMER_LRF_PATH_EXPANDER,
    TRANSFORMER_LRF_UPDATE_EXPANDER,
    TRUTHY_CONFIG_VALUES,
)

class ConversionPipeline(ConversionPipelineSteps):
    """Runs the CONTENT phase of the IDMS->DB2 conversion.

    Depends on the host class for the component factory methods and message
    helpers (via mixins). Returns (converted_cobol, operations,
    dclgen_repository); validation messages are appended to the passed-in
    list.

    The FINISHING phase - layout, paragraph extraction, counters, restart
    control, indent and resequencing - lives in ConversionLayoutPipeline.
    That split keeps the two concerns testable in isolation: this class
    decides WHAT the program says, that class decides HOW it is laid out.

    WHAT each step does lives in ConversionPipelineSteps. This file owns
    ORDER, and only order.

    Pass-ordering contracts (content phase)
    ---------------------------------------
    0a. LOGICAL RECORD EXPANSION. THREE stages, in this order, all inside
        ``_expand_logical_records``:

        1. ``LrfPathExpander``  - the READ and DELETE side::

               OBTAIN FIRST <LR> WHERE <keyword> -> OBTAIN FIRST <rec> WITHIN <set>
               ERASE <LR> WHERE <keyword>        -> ERASE <rec>
               FIELD OF <rec> OF LR              -> FIELD OF <rec>

        2. ``LrfUpdateExpander`` - the WRITE side::

               MODIFY <LR> WHERE <keyword>       -> MODIFY <rec>
               STORE  <LR> WHERE <keyword>       -> STORE <rec>

        3. ``LrStatusTokenReplacer`` - the status literals both expanders
           may leave behind::

               LR-STATUS = 'X-EOA'               -> DB-END-OF-SET -> SQLCODE = 100

        Stage 3 MUST run last: it consumes tokens the first two emit.

        The group MUST run first in the pipeline, because the PROGRAM KIND
        resolver, MappingScopeFilter, CobolTransformer and
        ProgramFlowAnalyzer all read the source text. Every pass after this
        point sees classic IDMS and needs no logical-record knowledge.

    0b. ``ProgramKindResolver`` measures UPDATE vs RETRIEVAL from the
        EXPANDED source. After 0a, because the update-side LRF forms are
        rewritten in stage 2 above; before statement transformation, which
        removes the write verbs entirely.

    0c. ``MappingScopeFilter`` rescopes the mapping validation report to the
        program being converted. MappingValidator audits the WHOLE Sheet
        Mapping workbook, so a restart-table gap was reported as a blocking
        error against every retrieval program that never touches it. A gap
        stays an error for a table this program references, and becomes a
        workbook note for any other.

    0d. ``_publish_lr_retrieval_state`` DELIVERS what 0a and 0b produced -
        the program kind, and the records for which 0a emitted a keyed
        parent access - to the statement transformer.

        MUST sit after 0b and BEFORE the transform, and nowhere else. The
        statement transformer does not appear in ``transformers`` under
        its own key: it is a constructor argument of CobolTransformer, so
        it was never offered the kind, and ``transform()`` calls
        ``_reset_statement_transformer()`` on entry. Publishing after the
        transform would arrive too late. See ConversionPipelineSteps
        CORRECTION 3.

    1.  ``feedback_cleanup`` (CobolCleanupComposer) runs
        ``OutputWritePlacementCleanup``, which lifts a guarded output WRITE
        out of the child-row paragraph into the PARENT paragraph, after the
        child cursor CLOSE. Left in the child-row paragraph the WRITE fires
        once per fetched child row instead of once per parent row.

    Steps 2 through 8 are owned by ConversionLayoutPipeline and documented
    there.

    CORRECTION 1 - THE WRITE SIDE WAS DOCUMENTED BUT NEVER RUN
    ----------------------------------------------------------
    Contract 0b used to claim the update-side LRF forms "are rewritten
    there", meaning by LrfPathExpander in 0a. That expander carries exactly
    three patterns - OBTAIN, OBTAIN continued, ERASE. It has never held a
    MODIFY or a STORE pattern, so an Update-with-LRF program kept::

        STORE  VMBTL07-R01 WHERE ST-VMBEVEF.
        MODIFY VMBTL07-R01 WHERE MO-VMBEVEF.

    all the way to the output, while the run log reported::

        LRF expansion: expanded 1 statement(s), skipped 0.

    "skipped 0" was not reassurance. A statement is only counted as skipped
    once it has MATCHED an LR pattern and then been refused. MODIFY and
    STORE matched nothing, so they were never seen as logical-record
    statements and never counted at all.

    ``LrfUpdateExpander`` had already been written and unit-tested for
    exactly these two verbs. It had no call site anywhere in the
    composition root - only in its own test module. Stage 2 above is that
    missing call site. The docstring claim is now true.

    CORRECTION 2 - THREE SILENT EXITS
    ---------------------------------
    ``_expand_logical_records`` returned the unmodified source whenever a
    transformer key was absent from the factory dict, and said nothing::

        expander = transformers.get("lrf_path_expander")
        if expander is None:
            return source_text          # no message

    A pass that was never WIRED is not the same thing as a program with no
    logical records, and silence cannot tell those apart. That is the same
    failure mode already recorded against the bare ``except Exception:
    pass`` that hid the LRF populator for three conversion cycles. Every
    stage now reports a missing component, a missing method, and a raised
    exception, and drains the component's own messages in all three cases.

    CORRECTION 3 - STEP 0d DID NOT EXIST
    ------------------------------------
    "The kind is now measured from the source, ONCE, and handed to every
    consumer that needs it", below, was true of the MEASUREMENT and false
    of the HANDOFF. ``_hand_off_program_kind`` had exactly ONE call site -
    ``retrieval_commit_cleanup``, inside ``_apply_commit_cleanup``. The
    statement transformer, which decides whether an OBTAIN CALC is a
    redundant positioning read or the only population of a DCLGEN host
    group, was never offered it.

    Measured on VMDZ4310: twelve MOVEs out of DCLDZBEFFTV and no SELECT,
    because the update rule was applied to a retrieval program. The kind
    was correct for all six programs on every run; only delivery was
    missing. Step 0d is that delivery.

    PROGRAM KIND - MEASURED, NOT CONFIGURED
    ---------------------------------------
    The kind used to come from ``self._program_is_update(conversion_input)``.
    ConversionInput carries paths and parsed metadata; it has never carried
    the IDMS write verbs. Once the workspace was flattened to a single
    Program folder - "One Program folder. No Retrieval / Update split" -
    the input's only kind signal disappeared and EVERY program resolved to
    retrieval. Update programs then silently lost restart control, their
    COMMIT and their business UPDATE, and the run log reported "Retrieval
    DB2 COBOL generation completed." for all of them.

    The kind is now measured from the source, ONCE, and handed to the
    consumers that need it. The input may still PROMOTE a program to
    update; it may not demote one whose source carries a write verb.

    RESTART CONTEXT
    ---------------
    The restart pass is run by the FINISHING phase, but its context can
    only be built HERE: finish() receives text and messages, never the
    conversion input, the DCLGEN columns or the program kind. The context
    is therefore built from the EXPANDED source - the checkpoint record
    is IDMS syntax and must be seen before it is converted away - and
    handed to ConversionLayoutPipeline through its constructor.

    The checkpoint record is written with the CLASSIC form - ``MODIFY
    FFRECAB``, ``STORE FFRECAB`` - which carries no ``WHERE <keyword>``
    clause. LR_MODIFY_WHERE_PATTERN requires that clause, so stage 2
    cannot match a checkpoint operation and restart handling is
    structurally out of its reach.

    TWO RESTART GENERATORS, ONE OWNER
    ---------------------------------
    ``SelectParagraphGenerator`` is the LEGACY restart path. It hardcoded
    the restart table, column and host names because it never read a
    DCLGEN, and it injected its own DZ01RSTV include and working storage.
    The metadata-driven pass (restart_injection, step 5b of the finishing
    phase) resolves every name from Sheet Mapping, DCLGEN and the program
    source, and MEASURES the checkpoint payload from the restart record
    layout - the value the legacy path guessed at 1215.

    Running both duplicated the DZ01RSTV include and left a PERFORM of a
    deleted handler. The legacy generator stands down whenever a restart
    context exists. See GATE_LEGACY_RESTART_GENERATOR.

    REGISTRY MIGRATION
    ------------------
    Passes marked MIGRATED are defined in converter/pipeline/registry.py
    and executed through run_stage(). The composer is constructed by the
    registry, not taken from the factory dict. Call POSITION is still
    owned by this file.

    SINGLE-OWNER PASS CONTRACT
    --------------------------
    Content transformations are each invoked once at their owning boundary.
    Cursor ordering runs only after cursor declarations and flow exist;
    restart-skip normalization runs once after statement transformation, before
    downstream cleanup can consume its markers. Re-running idempotent passes
    is not used as a substitute for a correct pipeline boundary.
    """

    # ------------------------------------------------------------------
    # Entry point
    # ------------------------------------------------------------------
    def _run_pipeline(
        self,
        *,
        conversion_input: ConversionInput,
        validation_messages: list[str],
    ) -> tuple[str, list, object]:
        repositories = self._repositories(conversion_input)
        resolvers = self._resolvers(repositories)
        generators = self._generators(
            repositories=repositories,
            resolvers=resolvers,
        )
        transformers = self._transformers(
            repositories=repositories,
            resolvers=resolvers,
            generators=generators,
        )
        composers = self._composers(
            repositories=repositories,
            resolvers=resolvers,
        )

        # --- 0a. LRF -> classic IDMS expansion ------------------------
        source_text = self._expand_logical_records(
            conversion_input=conversion_input,
            transformers=transformers,
            validation_messages=validation_messages,
        )

        # --- 0b. Program kind, measured once from the source ----------
        program_kind = self._resolve_program_kind(
            conversion_input=conversion_input,
            source_text=source_text,
            validation_messages=validation_messages,
        )

        # --- 0c. Input validation, rescoped to this program -----------
        mapping_validator = MappingValidator(
            mapping_repository=repositories["mapping"],
            dclgen_repository=repositories["dclgen"],
            table_name_resolver=resolvers["table_name"],
        )
        mapping_scope_filter = MappingScopeFilter(
            mapping_repository=repositories["mapping"],
            table_name_resolver=resolvers["table_name"],
        )
        validation_messages.extend(
            mapping_scope_filter.apply(
                messages=mapping_validator.validate(),
                source_text=source_text,
            )
        )
        validation_messages.extend(
            self._component_messages(mapping_scope_filter)
        )

        # --- Restart context, from the EXPANDED source ----------------
        restart_context = self._restart_context(
            conversion_input=conversion_input,
            source_text=source_text,
            program_kind=program_kind,
            validation_messages=validation_messages,
        )

        # --- 0d. Deliver what 0a and 0b produced ----------------------
        #
        # MUST sit between 0b and the transform, and nowhere else.
        #
        # The statement transformer is not in `transformers` under its
        # own key - it is a constructor argument of CobolTransformer -
        # so it was never offered the program kind, and it declared no
        # attribute to receive one. _convert_obtain_calc therefore
        # applied UPDATE semantics to retrieval programs and deleted
        # the single read that populates the DCLGEN host group.
        #
        # ORDER IS LOAD-BEARING. transform() calls
        # _reset_statement_transformer() on entry; reset() clears the
        # transformer's OUTPUTS and deliberately leaves these two
        # INPUTS alone. Publishing after transform() would arrive too
        # late. See ConversionPipelineSteps CORRECTION 3.
        self._publish_lr_retrieval_state(
            transformers=transformers,
            program_kind=program_kind,
            source_text=source_text,
            repositories=repositories,
            resolvers=resolvers,
            validation_messages=validation_messages,
        )

        # --- IDMS -> DB2 statement transformation ---------------------
        converted_cobol, transform_messages, operations = transformers[
            "cobol"
        ].transform(
            cobol_text=source_text,
            target_program_id=conversion_input.target_program_id,
        )
        validation_messages.extend(transform_messages)

        # LRF STORE paths that obtain a CALC parent must validate that parent
        # before inserting the child row. This is independent of the normal
        # UPDATE restart lifecycle and is activated only by an explicit
        # marker emitted for a source-proven STORE path.
        from converter.composers.lrf_store_parent_select_composer import (
            LrfStoreParentSelectComposer,
        )
        store_parent_composer = LrfStoreParentSelectComposer(
            sql_generator=generators["sql"],
        )
        converted_cobol = store_parent_composer.compose(converted_cobol)
        validation_messages.extend(store_parent_composer.messages)

        # Restart-skip markers are normalized once at the statement-conversion
        # boundary, before later cleanup can erase their source evidence.
        converted_cobol = self._stage(
            "update_restart_skip", converted_cobol, validation_messages
        )

        # --- Program flow analysis (diagnostics only) -----------------
        flow_analysis = ProgramFlowAnalyzer(
            mapping_rows=conversion_input.sheet_mapping_rows,
            dclgen_columns=conversion_input.dclgen_columns,
            # Use the same authoritative mapping/DCLGEN-aware resolver as the
            # statement converter. Without this dependency, diagnostics fall
            # back to IDMS record names and derive cursor names that do not
            # match the DB2 infrastructure generated later in this pipeline.
            table_name_resolver=resolvers["table_name"],
        ).analyze(
            cobol_text=source_text,
            operations=operations,
        )
        validation_messages.extend(flow_analysis.diagnostics)

        # --- Field references -> DCLGEN host variables ----------------
        converted_cobol = transformers["field_reference"].rewrite(
            converted_cobol
        )
        validation_messages.extend(
            self._component_messages(transformers["field_reference"])
        )

        # Field rewriting can turn an unqualified mapped DATE into a DCLGEN
        # host only after the first date-comparison pass has run. Re-run the
        # idempotent composer now so fixed-format continuation qualifiers and
        # newly resolved hosts receive the same metadata-driven realignment.
        date_compare = composers.get("date_compare")
        if date_compare is not None:
            converted_cobol = date_compare.compose(converted_cobol)
            validation_messages.extend(
                self._component_messages(date_compare)
            )

        # --- DB2 infrastructure, cursors ------------------------------
        converted_cobol = self._apply_db2_infrastructure(
            converted_cobol=converted_cobol,
            operations=operations,
            generators=generators,
            composers=composers,
            validation_messages=validation_messages,
            lrf_source_text=source_text,
        )

        # --- Timestamp / audit, SQLERROR routine ----------------------
        converted_cobol, timestamp_messages = generators["timestamp"].apply(
            cobol_text=converted_cobol,
            target_program_id=conversion_input.target_program_id,
        )
        validation_messages.extend(timestamp_messages)

        converted_cobol = generators["sql_error"].ensure_sql_error_paragraph(
            converted_cobol
        )

        # --- LEGACY restart paragraphs - gated ------------------------
        converted_cobol = self._apply_legacy_restart_generator(
            converted_cobol=converted_cobol,
            conversion_input=conversion_input,
            operations=operations,
            generators=generators,
            restart_context=restart_context,
            validation_messages=validation_messages,
        )

        # --- Safe cleanup passes --------------------------------------
        #
        # NOT given the program kind. update_program_feedback reaches
        # ObtainCalcRemover, which is update-side and kind-blind, but
        # this change is retrieval-LR only and must not edit a file the
        # update path executes. The LR keyed read avoids that pass by
        # carrying a marker it does not match - see
        # DataStatementConverterMixin CORRECTION 8. Teaching the remover
        # the kind is the right follow-up, with its own measurement.
        converted_cobol = self._apply_cleanup_composers(
            converted_cobol=converted_cobol,
            composers=composers,
            validation_messages=validation_messages,
        )

        converted_cobol = self._apply_commit_cleanup(
            converted_cobol=converted_cobol,
            composers=composers,
            program_kind=program_kind,
            validation_messages=validation_messages,
        )

        # Apply relationship key copies after the child DCLGEN INITIALIZE and
        # before final layout. The composer also removes parent status checks
        # that would otherwise inspect a later child's SQLCODE, and preserves
        # EOC state when SQLCODE is overwritten by CLOSE.
        lrf_key_composer = LrfKeyBindingComposer()
        converted_cobol = lrf_key_composer.compose(converted_cobol)
        validation_messages.extend(lrf_key_composer.messages)

        statement_transformer = self._statement_transformer(transformers)
        parent_records = getattr(statement_transformer, "lrf_calc_records", set()) if statement_transformer else set()
        group_decomposer = LrfGroupMoveDecomposer(
            mapping_repository=repositories["mapping"],
            dclgen_repository=repositories["dclgen"],
            copybook_repository=repositories["copybook"],
            table_name_resolver=resolvers["table_name"],
            host_variable_resolver=resolvers["host_variable"],
        )
        converted_cobol = group_decomposer.apply(converted_cobol, parent_records=parent_records)
        validation_messages[:] = group_decomposer.filter_resolved_field_diagnostics(validation_messages)
        validation_messages.extend(group_decomposer.messages)

        # --- FINISHING phase ------------------------------------------
        #
        # original_idms_text is the EXPANDED source, not the raw upload.
        # The converted text derives from it line by line, so style
        # preservation and unmapped-record discovery must compare against
        # the same baseline.
        converted_cobol = ConversionLayoutPipeline(
            composers=composers,
            resolvers=resolvers,
            component_messages=self._component_messages,
            restart_context=restart_context,
        ).finish(
            converted_cobol=converted_cobol,
            original_idms_text=source_text,
            validation_messages=validation_messages,
        )

        # Preserve the source-driven mainline exactly. The former lifecycle
        # standardizer could wrap recognized programs in a universal
        # 0000/1000/2000/3000 skeleton, which is not valid for every business
        # flow. The COBOL team asked for cursor paragraph numbering only.
        # Numbering is source-aware and runs before cursor-flow validation;
        # it does not insert/reorder business PERFORM statements.
        from converter.composers.cursor_paragraph_numbering_composer import (
            CursorParagraphNumberingComposer,
        )
        cursor_numbering = CursorParagraphNumberingComposer()
        converted_cobol = cursor_numbering.compose(converted_cobol)
        validation_messages.extend(cursor_numbering.messages)
        converted_cobol = self._stage(
            "guarantee_cursor_close", converted_cobol, validation_messages
        )

        # The shared cursor lifecycle owner runs AFTER the content cleanup.
        # Only now can a nested child loop be proven to own its OPEN/FETCH/
        # CLOSE and business paragraph. Reconcile fetch-driven business-control
        # semantics here, using discovered paragraph edges/flag assignments,
        # rather than guessing from any paragraph identifier or program name.
        # This pass deliberately does not rerun the entire cleanup composer.
        from converter.composers.cleanup.child_fetch_early_stop_cleanup import (
            ChildFetchEarlyStopCleanup,
        )
        from converter.composers.cleanup.cleanup_message_collector import (
            CleanupMessageCollector,
        )
        child_loop_messages = CleanupMessageCollector()
        child_loop_cleanup = ChildFetchEarlyStopCleanup(child_loop_messages)
        reconciled = child_loop_cleanup.ensure_child_fetch_early_stop(converted_cobol)
        if reconciled != converted_cobol:
            validation_messages.append(
                "Nested cursor control: reconciled child FETCH-to-business "
                "wiring after cursor lifecycle construction."
            )
            converted_cobol = reconciled
        validation_messages.extend(child_loop_messages.messages)

        # Normalize a proven nested parent cursor to FETCH-driven business
        # execution. This prevents a split driving loop from depending on a
        # business paragraph's tail FETCH and matches the row-success contract:
        # every successful parent FETCH invokes its business paragraph once.
        # Refuse ambiguous graphs; never bind both edges at once.
        from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import (
            NestedParentFetchNormalizer,
        )
        parent_normalizer = NestedParentFetchNormalizer()
        converted_cobol = parent_normalizer.apply(converted_cobol)
        validation_messages.extend(parent_normalizer.messages)

        # A flat source loop can have one FETCH in setup (prime) and another
        # at the tail of a performed business THRU range.  When both edges,
        # SQLCODE branches, and the only EOC driver are proven, make the
        # successful FETCH own the business call and delete the redundant
        # call sites.  No paragraph-name or program-name assumptions.
        from converter.composers.cursor_close_guarantee.flat_fetch_drive_normalizer import (
            FlatFetchDriveNormalizer,
        )
        flat_normalizer = FlatFetchDriveNormalizer()
        converted_cobol = flat_normalizer.apply(converted_cobol)
        validation_messages.extend(flat_normalizer.messages)

        # Source-proven SQL lowering is part of the ordinary IDMS -> DB2 stage,
        # not an alternate LRF conversion path. LRF is normalized above before
        # the standard transformer runs; this final lowering only removes cursor
        # scaffolding when the source and generated predicates prove FIRST-only
        # semantics. Ambiguous or NEXT-driven accesses are left unchanged by the
        # rewriter. Keep the legacy environment variable as a diagnostic override
        # only; correctness must not depend on an opt-in environment setting.
        bounded_rewrite = BoundedLrfSingletonRewriter().rewrite(
            converted_cobol, original_idms_text=source_text
        )
        converted_cobol = bounded_rewrite.text
        if bounded_rewrite.changed:
            validation_messages.append(
                f"Source-proven LRF SQL lowering: {bounded_rewrite.diagnostic}"
            )
        elif bounded_rewrite.diagnostic:
            validation_messages.append(
                f"LRF SQL lowering left cursor unchanged: {bounded_rewrite.diagnostic}"
            )

        # Final generated-comment cleanup and sequence normalization happen
        # only after all enabled code generation is complete.
        from converter.composers.manual_storage_parity_composer import (
            ManualStorageParityComposer,
        )
        converted_cobol = ManualStorageParityComposer().compose(converted_cobol)

        # The DCLGEN and output-copybook repository, not a program-ID, prove
        # which ten-byte DATE hosts require eight-byte record conversion.
        from converter.composers.schema_date_transfer_composer import SchemaDateTransferComposer
        date_transfers = SchemaDateTransferComposer(
            dclgen_columns=conversion_input.dclgen_columns,
            copybook_repository=repositories["copybook"],
        )
        converted_cobol = date_transfers.compose(converted_cobol)
        validation_messages.extend(date_transfers.messages)

        from converter.composers.schema_numeric_key_guard import SchemaNumericKeyGuard
        numeric_guard = SchemaNumericKeyGuard(conversion_input.dclgen_columns)
        converted_cobol = numeric_guard.compose(converted_cobol)
        validation_messages.extend(numeric_guard.messages)

        from converter.composers.unused_copybook_pruner import UnusedCopybookPruner
        unused_copybooks = UnusedCopybookPruner(conversion_input.source_copybook_members)
        converted_cobol = unused_copybooks.apply(converted_cobol)
        validation_messages.extend(unused_copybooks.messages)

        from converter.services.final_generated_output_service import (
            FinalGeneratedOutputService,
        )
        final_output = FinalGeneratedOutputService()
        converted_cobol = final_output.apply(
            converted_cobol, standardize_lifecycle=False
        )
        validation_messages.extend(final_output.messages)

        # The content pipeline can still insert/change FETCH and PERFORM
        # statements AFTER ConversionLayoutPipeline ran its indent pass.
        # Therefore final geometry must be normalized only after every
        # semantic rewrite, then resequenced.  Keep the rewrite out of
        # generated member files and independent of any paragraph name.
        from converter.composers.procedure_indent_normalizer import (
            ProcedureIndentNormalizer,
        )
        from converter.services.final_sequence_resequencer_service import (
            FinalSequenceResequencerService,
        )
        final_indent = ProcedureIndentNormalizer()
        converted_cobol = final_indent.compose(converted_cobol)
        validation_messages.extend(final_indent.messages)
        from converter.composers.sql_body_area_b_normalizer import SqlBodyAreaBNormalizer
        sql_alignment = SqlBodyAreaBNormalizer()
        converted_cobol = sql_alignment.compose(converted_cobol)
        validation_messages.extend(sql_alignment.messages)
        converted_cobol = FinalSequenceResequencerService().resequence(converted_cobol)

        return converted_cobol, operations, repositories["dclgen"]

    # ------------------------------------------------------------------
    # LRF expansion
    # ------------------------------------------------------------------
    def _expand_logical_records(
        self,
        *,
        conversion_input: ConversionInput,
        transformers: dict,
        validation_messages: list[str],
    ) -> str:
        """Rewrite LRF syntax into classic IDMS syntax.

        Returns the source text every later pass must use.

        THREE stages, applied in order, each independent of the others:

            1. read / delete side   LrfPathExpander.expand
            2. write side           LrfUpdateExpander.expand
            3. status literals      LrStatusTokenReplacer.apply

        Never raises. A stage that is missing, malformed or that throws is
        REPORTED and skipped, and the text from the previous stage carries
        on - an unconverted LRF verb is caught downstream by the
        residual-IDMS checks anyway. What must never happen is a stage
        failing in silence, because then a wiring fault is indistinguishable
        from a program that has no logical records.

        SIDE EFFECT READ BY STEP 0d: stage 1 leaves its
        ``calc_parent_records`` populated on the expander instance. Step
        0d reads it from the same ``transformers`` dict, so the producer
        and the consumer share one object and no value has to be
        threaded through this method's return.
        """
        text = str(conversion_input.idms_cobol_text or "")
        if not text.strip():
            return text

        text = self._lrf_stage(
            transformers=transformers,
            key=TRANSFORMER_LRF_PATH_EXPANDER,
            method=METHOD_EXPAND,
            label=LABEL_LRF_READ,
            text=text,
            validation_messages=validation_messages,
        )

        text = self._lrf_stage(
            transformers=transformers,
            key=TRANSFORMER_LRF_UPDATE_EXPANDER,
            method=METHOD_EXPAND,
            label=LABEL_LRF_UPDATE,
            text=text,
            validation_messages=validation_messages,
        )

        text = self._lrf_stage(
            transformers=transformers,
            key=TRANSFORMER_LR_STATUS_REPLACER,
            method=METHOD_APPLY,
            label=LABEL_LR_STATUS,
            text=text,
            validation_messages=validation_messages,
        )

        self._dump_expanded(conversion_input, text)
        return text

    @staticmethod
    def _dump_expanded(conversion_input: ConversionInput, text: str) -> None:
        """Persist the LRF-to-ordinary-IDMS intermediate for every conversion.

        The intermediate is a first-class diagnostic artifact, not temporary
        instrumentation. By default it is written under
        ``mainframe/workspace/Output/LRF`` so reviewers can inspect exactly
        what the ordinary IDMS-to-DB2 pipeline receives. Set
        ``IDMS_DB2_LRF_INTERMEDIATE_DIR`` to override that directory; the
        legacy ``DUMP_EXPANDED`` setting is also honored for compatibility.

        This method deliberately writes the source text without generated
        headers or COBOL comments, so the artifact can be fed back into the
        converter and compared with the original and final output.
        """
        from pathlib import Path
        import re

        configured_folder = (
            os.environ.get("IDMS_DB2_LRF_INTERMEDIATE_DIR", "").strip()
            or os.environ.get("DUMP_EXPANDED", "").strip()
        )
        if configured_folder:
            folder = Path(configured_folder).expanduser()
        else:
            project_root = Path(__file__).resolve().parents[3]
            folder = project_root / "mainframe" / "workspace" / "Output" / "LRF"

        raw_name = str(
            getattr(conversion_input, "target_program_id", "") or "UNKNOWN"
        ).strip()
        name = re.sub(r"[^A-Za-z0-9_.-]+", "_", raw_name) or "UNKNOWN"
        path = folder / f"{name}_lrf_to_idms.cbl"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        except OSError as exc:
            # Losing this artifact would make the two-stage conversion
            # unreviewable, so report the failure instead of silently hiding it.
            raise RuntimeError(
                f"Could not write LRF-to-IDMS intermediate '{path}': {exc}"
            ) from exc

    def _lrf_stage(
        self,
        *,
        transformers: dict,
        key: str,
        method: str,
        label: str,
        text: str,
        validation_messages: list[str],
    ) -> str:
        """Run ONE logical-record stage. Reports every way it can decline.

        Four outcomes, all visible:

          * the factory produced no component under ``key``
          * the component has no ``method``
          * the call raised
          * the call returned

        The component's own messages are drained in the last two cases,
        including the failure case: a transformer that reported two
        findings and then threw on the third must not lose the two.
        """
        component = transformers.get(key)

        if component is None:
            validation_messages.append(
                LRF_STAGE_NOT_WIRED_TEMPLATE.format(label=label, key=key)
            )
            return text

        run = getattr(component, method, None)
        if not callable(run):
            validation_messages.append(
                LRF_STAGE_NO_METHOD_TEMPLATE.format(
                    label=label, key=key, method=method
                )
            )
            return text

        try:
            produced = run(text)
        except Exception as exc:  # noqa: BLE001
            validation_messages.extend(self._component_messages(component))
            validation_messages.append(
                LRF_STAGE_FAILED_TEMPLATE.format(label=label, reason=exc)
            )
            return text

        validation_messages.extend(self._component_messages(component))
        return produced or text


__all__ = ["ConversionPipeline"]