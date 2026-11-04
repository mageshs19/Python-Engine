# LOCATION: converter/pipeline/conversion/conversion_pipeline_steps.py
# ACTION: REPLACE ENTIRE FILE

"""Helper steps for the CONTENT phase of the IDMS->DB2 conversion.

ConversionPipeline owns pass ORDER. This mixin owns what each step does.
Splitting them keeps the order readable in one screen and lets a step be
tested without constructing the whole pipeline.

CORRECTION 1 - the legacy stand-down could never fire
-----------------------------------------------------
``GATE_LEGACY_RESTART_GENERATOR`` was False, so::

    if GATE_LEGACY_RESTART_GENERATOR and restart_context is not None:

was unreachable and BOTH restart generators ran on every program. The
metadata-driven pass emits 710-/720- handlers; the legacy pass emits
``PERFORM 810-``/``820-``. Measured on VMDZ1567: 710-/720- scored 2 each
(defined and performed), 810-/820- scored 1 each (performed only). A
PERFORM of a paragraph that does not exist is IGYPS2072-S.

CORRECTION 2 - the program kind was read from the INPUT
--------------------------------------------------------
``is_update=self._program_is_update(conversion_input)``. ConversionInput
carries paths and parsed metadata; it has never carried the IDMS write
verbs. Once the workspace was flattened to one Program folder the
input's only kind signal disappeared and EVERY program resolved to
retrieval, so update programs silently lost restart control, their
COMMIT and their business UPDATE.

The kind is now MEASURED from the expanded source, once, and every
consumer is TOLD. Two classifiers eventually disagree, and the
disagreement is invisible until a cleanup pass deletes the COMMIT the
restart pass just injected.

CORRECTION 3 - THE KIND REACHED ONE CONSUMER OUT OF THREE
-----------------------------------------------------------
CORRECTION 2 ends with "every consumer is TOLD". Measured, exactly ONE
consumer was ever offered it - retrieval_commit_cleanup, from
``_apply_commit_cleanup``. The run log says so plainly::

    Program kind: retrieval_commit_cleanup does not accept a program
                  kind; it will classify independently and may disagree.
    Update postprocess: no program kind supplied; the caller must pass
                  the kind the pipeline already resolved.

and IdmsStatementTransformer appears in neither line, because it was
never offered the kind at all.

That was not cosmetic. ``_convert_obtain_calc`` encodes ONE semantic -
"the direct UPDATE carries the composite key, so the positioning read is
redundant" - and applied it to retrieval programs, where an OBTAIN CALC
is the ONLY population of the DCLGEN host group. VMDZ4310 shipped with
twelve MOVEs out of DCLDZBEFFTV and no SELECT; the removal comment was
then consumed by REMOVED_OBTAIN_CALC_PATTERN and the orphaned CONTINUE
by _maybe_skip_redundant_continue, so the deleted read left NO TRACE in
the output and no diagnostic anywhere.

``_publish_lr_retrieval_state`` closes that gap. It delivers two values
to the statement transformer, which lives behind CobolTransformer:

    program_kind        measured here, every program, already correct
    lrf_calc_records    the records LrfPathExpander emitted an
                        OBTAIN CALC for, published as its
                        calc_parent_records

Both are needed. The kind alone would convert a hand-written OBTAIN CALC
in a retrieval program - VMBWCEF in VM4BD302 - which is a real finding
but a DIFFERENT one, to be fixed with its own measurement. The record
set alone would convert the LRF keyed parent in an UPDATE program with
LRF syntax - VMDZ1526 - where removing the read is correct.

KNOWN DUPLICATION - THE KIND CONSTANTS HAVE TWO OWNERS
--------------------------------------------------------
``KIND_UPDATE`` is imported here from ``rules.program_kind_rules``.
``converter.resolvers.program_kind_resolver`` also defines
``KIND_RETRIEVAL`` and ``KIND_UPDATE``. One fact, two modules: the day a
third kind is added, one of them will be missed. The rules module should
own them and the resolver should re-export, as
``rules/cursor_spec/cursor_spec_rules.py`` already does for
CURSOR_OPERATIONS. Not changed here, so this step stays measurable.
"""

from __future__ import annotations

import re

from converter.domain.models import ConversionInput
from converter.analyzers.lr_access.lrf_key_binding_planner import LrfKeyBindingPlanner
from converter.analyzers.lr_access.handwritten_obtain_calc_planner import HandwrittenObtainCalcPlanner
from converter.pipeline.run import run_stage
from converter.pipeline.stage import Document
from converter.resolvers.program_kind_resolver import ProgramKindResolver
from converter.services.name_normalizer import NameNormalizer
from rules.program_kind_rules import KIND_UPDATE

# Module path of the resolver that turns DCLGEN columns into a restart
# DclgenRoleInfo. Imported lazily and REPORTED when absent, so a wrong
# path names itself instead of crashing a conversion.
RESTART_DCLGEN_MODULE = "converter.postprocess.update_restart_dclgen_resolver"
RESTART_DCLGEN_CLASS = "UpdateRestartDclgenResolver"

# When a metadata-driven restart context exists, the LEGACY restart
# generator stands down. Two generators writing restart infrastructure
# into one program injected the DZ01RSTV DCLGEN twice, which duplicates
# every data name in the group - a hard compile error.
#
# Set False to run both and compare output. The log states which
# generator owned each program either way.
GATE_LEGACY_RESTART_GENERATOR = True
LEGACY_RESTART_SKIPPED = (
    "Restart: legacy paragraph generator skipped; the metadata-driven "
    "restart pass owns this program."
)

# ---------------------------------------------------------------------
# Program kind delivery
# ---------------------------------------------------------------------
# One classifier, consulted once. Any composer that needs the kind is
# TOLD, never left to work it out again.
PROGRAM_KIND_ATTRIBUTE = "program_kind"
PROGRAM_KIND_HANDOFF_OK = "Program kind: handed '{kind}' to {component}."
PROGRAM_KIND_HANDOFF_REFUSED = (
    "Program kind: {component} does not accept a program kind; it will "
    "classify independently and may disagree."
)

# The statement transformer is not in the transformers map under its own
# key: it is a constructor argument of CobolTransformer, which owns
# per-program publication to it - see _publish_bounded_search_records.
# Declared as names so producer and consumer cannot drift on a literal.
COBOL_TRANSFORMER_KEY = "cobol"
STATEMENT_TRANSFORMER_ATTRIBUTE = "idms_statement_transformer"
STATEMENT_TRANSFORMER_NAME = "idms_statement_transformer"
LRF_EXPANDER_KEY = "lrf_path_expander"
LRF_CALC_RECORDS_ATTRIBUTE = "lrf_calc_records"
LRF_KEY_INPUT_MOVES_ATTRIBUTE = "lrf_key_input_moves"
LRF_KEY_BINDING_ERRORS_ATTRIBUTE = "lrf_key_binding_errors"
LRF_SELECT_COLUMNS_ATTRIBUTE = "lrf_select_columns"
HANDWRITTEN_CALC_PLANS_ATTRIBUTE = "handwritten_calc_plans"
CALC_PARENT_RECORDS_ATTRIBUTE = "calc_parent_records"

STATEMENT_TRANSFORMER_UNREACHABLE = (
    "Program kind: the statement transformer could not be reached "
    "behind the COBOL transformer; it will classify OBTAIN CALC with "
    "UPDATE semantics regardless of the program kind."
)
LRF_CALC_RECORDS_PUBLISHED = (
    "LRF keyed read: published {count} keyed parent record(s) to the "
    "statement transformer ({records})."
)
LRF_CALC_RECORDS_NONE = (
    "LRF keyed read: the expansion produced no keyed parent access; "
    "every OBTAIN CALC keeps its existing treatment."
)

COMMIT_CLEANUP_MISSING = (
    "Retrieval cleanup: composer is not registered; a COMMIT in a "
    "read-only program will not be removed."
)
DATE_COMPARE_MISSING = (
    "DB2 date compare: composer is not registered; DATE host "
    "comparisons will not be realigned."
)


class ConversionPipelineSteps:
    """What each content-phase step does. Order lives in the pipeline."""

    # ------------------------------------------------------------------
    # Registry helper
    # ------------------------------------------------------------------
    @staticmethod
    def _stage(
        name: str,
        converted_cobol: str,
        validation_messages: list[str],
    ) -> str:
        """Run one registered stage and drain its diagnostics.

        A disabled stage is a no-op. An unknown name is reported as an
        [error] message rather than silently dropping the pass.
        """
        doc = run_stage(name, Document(cobol=converted_cobol))
        validation_messages.extend(doc.messages)
        return doc.cobol

    # ------------------------------------------------------------------
    # Program kind
    # ------------------------------------------------------------------
    def _resolve_program_kind(
        self,
        *,
        conversion_input: ConversionInput,
        source_text: str,
        validation_messages: list[str],
    ) -> str:
        """Measure UPDATE vs RETRIEVAL from the EXPANDED source."""
        declared = getattr(conversion_input, "is_update", None)
        if declared is None:
            declared = self._input_declares_update(conversion_input)

        kind, messages = ProgramKindResolver().resolve(
            source_text=source_text,
            input_says_update=declared,
        )
        validation_messages.extend(messages)
        return kind

    def _input_declares_update(
        self,
        conversion_input: ConversionInput,
    ) -> bool | None:
        """What the input believes, or None when it is silent.

        Kept so an input that genuinely knows can still PROMOTE a
        program. It can no longer demote one.
        """
        probe = getattr(self, "_program_is_update", None)
        if not callable(probe):
            return None
        try:
            return bool(probe(conversion_input))
        except Exception:  # noqa: BLE001
            return None

    def _hand_off_program_kind(
        self,
        *,
        component,
        component_name: str,
        program_kind: str,
        validation_messages: list[str],
    ) -> None:
        """Tell a composer the kind, or report that it will guess."""
        if component is None:
            return

        if not hasattr(component, PROGRAM_KIND_ATTRIBUTE):
            validation_messages.append(
                PROGRAM_KIND_HANDOFF_REFUSED.format(component=component_name)
            )
            return

        try:
            setattr(component, PROGRAM_KIND_ATTRIBUTE, program_kind)
        except Exception:  # noqa: BLE001
            validation_messages.append(
                PROGRAM_KIND_HANDOFF_REFUSED.format(component=component_name)
            )
            return

        validation_messages.append(
            PROGRAM_KIND_HANDOFF_OK.format(
                kind=program_kind, component=component_name
            )
        )

    # ------------------------------------------------------------------
    # LR retrieval state - see CORRECTION 3
    # ------------------------------------------------------------------
    def _statement_transformer(self, transformers: dict):
        """The IdmsStatementTransformer behind the COBOL transformer.

        None when it cannot be reached, so the caller reports rather
        than raising. A conversion that loses one keyed read is a
        finding; a conversion that aborts on an attribute lookup is an
        outage.
        """
        cobol_transformer = (transformers or {}).get(COBOL_TRANSFORMER_KEY)
        if cobol_transformer is None:
            return None
        return getattr(
            cobol_transformer, STATEMENT_TRANSFORMER_ATTRIBUTE, None
        )

    @staticmethod
    def _source_proven_lrf_select_columns(source_text: str, mapping_repository, record_name: str) -> list[str]:
        """Return mapped columns referenced after an LRF keyed parent read.

        This is intentionally source-driven: Sheet Mapping is the allow-list,
        while qualified COBOL references after OBTAIN CALC are the evidence
        that a field is needed. If no fields can be proven, return [] so the
        SQL generator refuses to replace the source access with a guessed
        SELECT. Comments and fixed-format sequence/identification columns are
        excluded before scanning.
        """
        record = NameNormalizer.normalize(record_name)
        record_display = NameNormalizer.to_cobol(record_name)
        if not record or not record_display:
            return []

        logical_lines: list[str] = []
        for raw in str(source_text or "").splitlines():
            line = raw.rstrip("\r\n")
            if len(line) > 6 and line[:6].strip().isdigit():
                if line[6] in "*/":
                    continue
                line = line[7:72]
            elif line.lstrip().startswith(("*", "/*")):
                continue
            logical_lines.append(line.upper())
        logical = "\n".join(logical_lines)
        access = re.search(rf"\bOBTAIN\s+CALC\s+{re.escape(record_display)}\b", logical)
        if not access:
            return []
        downstream = logical[access.end():]

        required: list[str] = []
        seen: set[str] = set()
        try:
            rows = mapping_repository.rows_for_record(record) or []
        except Exception:  # noqa: BLE001
            return []

        # Keep the hierarchy from Sheet Mapping. A referenced group field may
        # contain mapped descendants even when the group itself has no DB2
        # column (for example a source MOVE of a group into a working field).
        entries: list[tuple[int, str, str, str, object]] = []
        for row in rows:
            zone = str(getattr(row, "cobol_zone", "") or "").strip().upper()
            parts = zone.split()
            level = 0
            if parts and parts[0].isdigit():
                level = int(parts.pop(0))
            field = parts[0] if parts else ""
            if not field or field == "FILLER" or field == "REDEFINES":
                continue
            column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            pic_clause = str(getattr(row, "idms_pic_clause", "") or "").upper()
            entries.append((level, field, column, pic_clause, row))

        # Analyze physical source statements after removing fixed-format
        # sequence areas. A DISPLAY of a whole group is commonly diagnostic;
        # it must not make every descendant a SELECT column merely because a
        # later COBOL statement shares the same sentence before a period.
        statements = [part.strip() for part in downstream.splitlines() if part.strip()]
        referenced: set[str] = set()
        operational_group_refs: set[str] = set()
        operation_re = re.compile(
            r"^(?:[A-Z0-9-]+\.\s*)?(?:MOVE|IF|ELSE|COMPUTE|ADD|SUBTRACT|MULTIPLY|DIVIDE|EVALUATE|SET)\b"
        )
        for _level, field, _column, _pic_clause, _row in entries:
            pattern = re.compile(
                rf"\b{re.escape(field)}\s+(?:OF|IN)\s+{re.escape(record_display)}\b"
            )
            for statement in statements:
                if not pattern.search(statement):
                    continue
                referenced.add(field)
                if operation_re.search(statement.upper()):
                    operational_group_refs.add(field)

        selected_names = set(referenced)
        # If a referenced non-column group participates in business data
        # movement/logic, include its mapped descendants in hierarchy order.
        for index, (level, field, column, _pic_clause, _row) in enumerate(entries):
            if field not in operational_group_refs or column or level <= 0:
                continue
            descendants: list[tuple[int, str, str, str, object]] = []
            for child in entries[index + 1:]:
                child_level, _child_field, _child_column, _child_pic_clause, _child_row = child
                if child_level <= level:
                    break
                if _child_column:
                    descendants.append(child)
            # Some mappings represent a COBOL subgroup as a single DB2
            # column (PIC GROUP). Prefer that explicit mapped representation
            # over selecting its scalar CALC-key components as duplicate
            # output fields. If no mapped subgroup exists, select mapped leaf
            # descendants so a genuine group MOVE remains fully populated.
            group_columns = [item for item in descendants if "GROUP" in item[3]]
            chosen_descendants = group_columns or descendants
            selected_names.update(item[1] for item in chosen_descendants)

        for _level, field, column, _pic_clause, _row in entries:
            if field not in selected_names or not column or column in seen:
                continue
            seen.add(column)
            required.append(column)
        return required

    def _publish_lr_retrieval_state(
        self,
        *,
        transformers: dict,
        program_kind: str,
        source_text: str,
        repositories: dict,
        resolvers: dict,
        validation_messages: list[str],
    ) -> None:
        """Deliver the kind and the LRF keyed-parent records.

        CALL THIS IMMEDIATELY BEFORE transformers["cobol"].transform().

        ORDER IS LOAD-BEARING. transform() calls
        _reset_statement_transformer() on entry, which calls reset().
        reset() clears the transformer's OUTPUTS - messages,
        unmapped_records - and deliberately does NOT clear these two
        INPUTS. Publishing after transform() would arrive too late;
        clearing them in reset() would erase the handoff between the
        moment it is made and the moment it is read.

        The record set is ALWAYS set, never merged and never left
        absent, so the reading end can never confuse "no expander" with
        "expander found nothing" - the same contract
        CobolTransformer._publish_bounded_search_records established.
        """
        statement_transformer = self._statement_transformer(transformers)

        if statement_transformer is None:
            validation_messages.append(STATEMENT_TRANSFORMER_UNREACHABLE)
            return

        self._hand_off_program_kind(
            component=statement_transformer,
            component_name=STATEMENT_TRANSFORMER_NAME,
            program_kind=program_kind,
            validation_messages=validation_messages,
        )

        expander = (transformers or {}).get(LRF_EXPANDER_KEY)
        records = set(
            getattr(expander, CALC_PARENT_RECORDS_ATTRIBUTE, None) or set()
        )

        try:
            setattr(
                statement_transformer, LRF_CALC_RECORDS_ATTRIBUTE, records
            )
        except Exception:  # noqa: BLE001
            validation_messages.append(STATEMENT_TRANSFORMER_UNREACHABLE)
            return

        if records:
            validation_messages.append(
                LRF_CALC_RECORDS_PUBLISHED.format(
                    count=len(records),
                    records=", ".join(sorted(records)),
                )
            )
        else:
            validation_messages.append(LRF_CALC_RECORDS_NONE)

        # Publish a program-specific SELECT projection, based on actual
        # qualified field references after each generated keyed parent read.
        # The SQL builder still validates every selected column against DCLGEN
        # and resolves the corresponding host variable before emitting SQL.
        select_columns: dict[str, list[str]] = {}
        mapping_repository = repositories["mapping"]
        for parent in sorted(records):
            required_columns = self._source_proven_lrf_select_columns(
                source_text, mapping_repository, parent
            )
            select_columns[NameNormalizer.normalize(parent)] = required_columns
            select_columns[NameNormalizer.to_cobol(parent)] = required_columns
            if not required_columns:
                validation_messages.append(
                    f"LRF keyed read: no source-proven downstream mapped fields for {parent}; "
                    "the executable keyed SELECT will be refused and the source access retained."
                )
            else:
                validation_messages.append(
                    f"LRF keyed read: SELECT projection for {parent} restricted to "
                    f"{len(required_columns)} source-used mapped column(s)."
                )
        setattr(statement_transformer, LRF_SELECT_COLUMNS_ATTRIBUTE, select_columns)

        # The LRF parent input split is derived from mapping metadata and the
        # actual source MOVE before the generated OBTAIN CALC. Relationship
        # cursor predicates are already bound to the parent DCLGEN hosts by
        # the LRF host-variable populator; copying those values to the child
        # DCLGEN group would be redundant and can be wrong after INITIALIZE.
        planner = LrfKeyBindingPlanner(
            mapping_repository=repositories["mapping"],
            dclgen_repository=repositories["dclgen"],
            table_name_resolver=resolvers["table_name"],
            host_variable_resolver=resolvers["host_variable"],
            copybook_repository=repositories.get("copybook"),
        )
        key_input_moves: dict[str, list[str]] = {}
        key_binding_errors: dict[str, list[str]] = {}
        for parent in sorted(records):
            moves, diagnostics, required = planner.plan_parent_input(source_text, parent)
            if diagnostics:
                validation_messages.extend(diagnostics)
                if required:
                    key_binding_errors[parent] = list(diagnostics)
            elif moves:
                key_input_moves[parent] = moves

        setattr(statement_transformer, LRF_KEY_INPUT_MOVES_ATTRIBUTE, key_input_moves)
        setattr(statement_transformer, LRF_KEY_BINDING_ERRORS_ATTRIBUTE, key_binding_errors)
        if key_input_moves:
            validation_messages.append(
                "LRF key binding: generated metadata-proven input split(s) for "
                + ", ".join(sorted(key_input_moves)) + "."
            )
        if key_binding_errors:
            validation_messages.append(
                "LRF key binding: one or more LRF keyed reads were marked unsafe; "
                "the original access will be retained rather than emitting incomplete SQL."
            )

        # Hand-written retrieval OBTAIN CALC is distinct from update positioning
        # reads and LRF-generated parent reads. Enable it only when metadata,
        # source assignments and following status guards are all provable.
        handwritten_plans: dict[str, dict[str, str]] = {}
        if str(program_kind or "").strip().lower() == "retrieval":
            try:
                planner = HandwrittenObtainCalcPlanner(
                    mapping_repository=mapping_repository,
                    table_name_resolver=resolvers["table_name"],
                    host_variable_resolver=resolvers["host_variable"],
                )
                handwritten_plans, plan_messages = planner.plan(
                    source_text, excluded_records=records
                )
                validation_messages.extend(plan_messages)
            except Exception as exc:  # noqa: BLE001 - fail closed
                validation_messages.append(
                    "Hand-written OBTAIN CALC planner failed safely "
                    f"({type(exc).__name__}); unplanned accesses remain review-only."
                )
        setattr(statement_transformer, HANDWRITTEN_CALC_PLANS_ATTRIBUTE, handwritten_plans)

    # ------------------------------------------------------------------
    # Restart context
    # ------------------------------------------------------------------
    def _restart_dclgen_resolver(self, validation_messages: list[str]):
        """The resolver that turns DCLGEN columns into a restart role.

        Imported lazily and by NAME. A wrong path is reported with the
        path it tried and the conversion continues without restart,
        instead of aborting every program in the batch.
        """
        try:
            module = __import__(
                RESTART_DCLGEN_MODULE, fromlist=[RESTART_DCLGEN_CLASS]
            )
            return getattr(module, RESTART_DCLGEN_CLASS)()
        except Exception as exc:  # noqa: BLE001
            validation_messages.append(
                "Restart context: the restart DCLGEN resolver was not "
                f"available at {RESTART_DCLGEN_MODULE}."
                f"{RESTART_DCLGEN_CLASS} ({type(exc).__name__}: {exc}); "
                "no restart control will be injected."
            )
            return None

    def _restart_context(
        self,
        *,
        conversion_input: ConversionInput,
        source_text: str,
        program_kind: str,
        validation_messages: list[str],
    ):
        """Build the run-scoped restart context, or None with a reason.

        WHY TOTALS ARE RESOLVED HERE

        RestartMainFlowBuilder renders the totals block from whatever it
        is handed and never authors a DISPLAY itself, deliberately: two
        authors mean two sets of totals that disagree.
        RestartTotalsResolver is the author. Nothing connected the two,
        so every update program with restart control terminated without
        reporting how many records it read or wrote.

        WHY `guaranteed` IS SUPPLIED

        The resolver is reference-driven: it displays a counter only when
        something adds to it. The business-UPDATE row counter does not
        exist yet at this point in the run - the pass that declares and
        increments it has not executed. `guaranteed` is the resolver's own
        hook for exactly that case: names the CALLER can prove a later pass
        will increment. They come from the restart working-storage rules,
        which already own those two names, so none is hardcoded here.
        """
        from converter.resolvers.restart_context_builder import (
            RestartContextBuilder,
        )
        from converter.generators.restart.restart_totals_resolver import (
            RestartTotalsResolver,
        )
        from rules.update_restart_rules import UPDATE_RESTART_WS_NAMES

        is_update = program_kind == KIND_UPDATE

        totals: tuple[str, ...] = ()
        if is_update:
            resolver = RestartTotalsResolver()
            guaranteed = tuple(
                str(UPDATE_RESTART_WS_NAMES.get(key, "") or "").strip()
                for key in ("input_counter", "update_counter")
            )
            totals = tuple(
                resolver.resolve(
                    str(source_text or "").splitlines(),
                    guaranteed=guaranteed,
                )
                or ()
            )
            validation_messages.extend(resolver.messages)

        builder = RestartContextBuilder(
            dclgen_resolver=self._restart_dclgen_resolver(validation_messages),
        )
        context, messages = builder.build(
            source_text=source_text,
            dclgen_columns=conversion_input.dclgen_columns,
            is_update=is_update,
            totals=totals,
        )
        validation_messages.extend(messages)
        return context

    def _apply_legacy_restart_generator(
        self,
        *,
        converted_cobol: str,
        conversion_input: ConversionInput,
        operations: list,
        generators: dict,
        restart_context,
        validation_messages: list[str],
    ) -> str:
        """The LEGACY restart path, run only when nothing better can.

        A retrieval program still yields a context - one whose kind is
        'retrieval' - so this guard skips the legacy generator for
        read-only programs too. That matches the previous behaviour,
        where it ran but did nothing.
        """
        if GATE_LEGACY_RESTART_GENERATOR and restart_context is not None:
            validation_messages.append(LEGACY_RESTART_SKIPPED)
            return converted_cobol

        converted_cobol, select_messages = generators["select_paragraph"].apply(
            cobol_text=converted_cobol,
            program_id=conversion_input.target_program_id,
            operations=operations,
        )
        validation_messages.extend(select_messages)
        return converted_cobol

    # ------------------------------------------------------------------
    # DB2 infrastructure and cursor passes
    # ------------------------------------------------------------------
    def _apply_db2_infrastructure(
        self,
        *,
        converted_cobol: str,
        operations: list,
        generators: dict,
        composers: dict,
        validation_messages: list[str],
        lrf_source_text: str | None = None,
    ) -> str:
        converted_cobol, infrastructure_messages = generators[
            "db2_infrastructure"
        ].apply(
            cobol_text=converted_cobol,
            operations=operations,
            lrf_source_text=lrf_source_text,
        )
        validation_messages.extend(infrastructure_messages)

        # Cursor ordering is normalized exactly once, after cursor declarations
        # and the cursor control-flow plan are present. Running it before cursor
        # generation cannot inspect the final declaration and created a second,
        # redundant mutation point.

        converted_cobol, cursor_messages = generators[
            "cursor_paragraph"
        ].apply(cobol_text=converted_cobol, operations=operations)
        validation_messages.extend(cursor_messages)

        # LRF host variable population
        if hasattr(
            generators["cursor_paragraph"], "augment_lrf_procedure_division"
        ):
            converted_cobol, lrf_messages = generators[
                "cursor_paragraph"
            ].augment_lrf_procedure_division(converted_cobol)
            validation_messages.extend(lrf_messages)

        # ------------------------------------------------------------------
        # Flow-Bucket Orchestration - REMOVED 10-10-2026
        #
        # The pass never executed: it read raw lines without stripping the
        # 6-digit COBOL sequence area, so _parse_program_sections() could
        # not find WORKING-STORAGE and it logged "No WORKING-STORAGE
        # SECTION found - skipping orchestration" on every program. All
        # five of its stated goals are already delivered by fixed-format
        # aware passes, verified on VMDZ7200:
        #     cursor flags + 88 levels -> db2_infrastructure_generator
        #     NNNN / TS-TIMESTAMP      -> timestamp_generator
        #     WS section markers       -> infrastructure block builder
        # ------------------------------------------------------------------

        # CursorLifecycle is the single mutating owner of OPEN/FETCH/business/
        # CLOSE wiring. Do not run CursorFlowComposer first: it rewrites FETCH
        # success branches and loop ownership, after which the close-guarantee
        # stage can discover a second business-call edge and mutate the same
        # cursor again. The lifecycle stage below classifies each cursor and
        # either preserves a proven existing loop or synthesizes only what is
        # missing.

        # ------------------------------------------------------------------
        # Cursor close guarantee: the FETCH paragraph is driven UNTIL
        # <cursor>-EOC, the CLOSE paragraph is performed, and the fetched
        # row reaches the business paragraph.
        # ------------------------------------------------------------------
        # Cursor lifecycle validation/rewriting is intentionally deferred until
        # the outer lifecycle structure is standardized. This prevents an early
        # cursor rewrite from being followed by a second mainline rewrite.

        converted_cobol = composers["sqlcode_cleanup"].compose(converted_cobol)
        validation_messages.extend(
            self._component_messages(composers["sqlcode_cleanup"])
        )

        # Single owner for cursor ORDER BY normalization. This is deliberately
        # after cursor declarations and flow generation, never before them.
        converted_cobol = self._stage(
            "cursor_order_cleanup", converted_cobol, validation_messages
        )

        # ------------------------------------------------------------------
        # DB2 DATE comparison realignment.
        #
        # A DB2 DATE host is DD.MM.CCYY, 10 bytes. A COBOL date field is
        # CCYYMMDD, PIC 9(8). Comparing them directly compares '0' against
        # '2' and selects the wrong rows, so this pass must be visible in
        # the log whether it fires or not.
        # ------------------------------------------------------------------
        date_compare = composers.get("date_compare")

        if date_compare is None:
            validation_messages.append(DATE_COMPARE_MISSING)
        else:
            converted_cobol = date_compare.compose(converted_cobol)
            validation_messages.extend(
                self._component_messages(date_compare)
            )

        return converted_cobol

    # ------------------------------------------------------------------
    # Cleanup passes
    # ------------------------------------------------------------------
# LOCATION: converter/pipeline/conversion/conversion_pipeline_steps.py
# ACTION: REPLACE THE _apply_cleanup_composers METHOD
# LOCATION: converter/pipeline/conversion/conversion_pipeline_steps.py
# ACTION: REPLACE THE _apply_cleanup_composers METHOD

    def _apply_cleanup_composers(
        self,
        *,
        converted_cobol: str,
        composers: dict,
        validation_messages: list[str],
    ) -> str:
        """Content-level cleanup, before any layout decision is taken.

        feedback_cleanup == CobolCleanupComposer. It runs
        OutputWritePlacementCleanup, which moves the guarded output WRITE
        out of the child-row paragraph into the parent paragraph. The
        paragraph EXTRACTION in the finishing phase depends on that
        relocation having already happened.

        DELIBERATELY NOT GIVEN THE PROGRAM KIND
        ----------------------------------------
        update_program_feedback reaches UpdateSqlCleanupComposer and
        through it ObtainCalcRemover, which strips a generated
        OBTAIN CALC SELECT block because "the direct UPDATE will use the
        composite key". That pass is kind-blind and runs on retrieval
        programs too, where there is no direct UPDATE and the SELECT it
        would delete is the only population of the DCLGEN host group.

        Teaching it the kind is the correct fix and is NOT made here:
        this change is retrieval-LR only and must not edit a file the
        update path executes. The LR keyed read avoids the pass instead,
        by carrying a marker ObtainCalcRemover does not match - see
        DataStatementConverterMixin CORRECTION 8.

        A follow-up should hand the kind to this loop and make
        ObtainCalcRemover stand down on retrieval, with its own
        measurement. Until then the omission is a decision, not an
        oversight, and is recorded as one.
        """
        for name in (
            "feedback_cleanup",
            "unnecessary_comments_cleanup",
            "update_program_feedback",
        ):
            converted_cobol = composers[name].compose(converted_cobol)
            validation_messages.extend(
                self._component_messages(composers[name])
            )

        return converted_cobol
        
    def _apply_commit_cleanup(
        self,
        *,
        converted_cobol: str,
        composers: dict,
        program_kind: str,
        validation_messages: list[str],
    ) -> str:
        """Remove a COMMIT from a read-only program - and only then.

        The restart pass injects a COMMIT into an update program. If this
        composer classifies independently it will delete that COMMIT and
        the checkpoint will never be committed, so it is told the kind.
        """
        commit_cleanup = composers.get("retrieval_commit_cleanup")

        if commit_cleanup is None:
            validation_messages.append(COMMIT_CLEANUP_MISSING)
            return converted_cobol

        self._hand_off_program_kind(
            component=commit_cleanup,
            component_name="retrieval_commit_cleanup",
            program_kind=program_kind,
            validation_messages=validation_messages,
        )
        converted_cobol = commit_cleanup.compose(converted_cobol)
        validation_messages.extend(
            self._component_messages(commit_cleanup)
        )
        return converted_cobol


__all__ = [
    "ConversionPipelineSteps",
    "RESTART_DCLGEN_MODULE",
    "RESTART_DCLGEN_CLASS",
    "GATE_LEGACY_RESTART_GENERATOR",
    "LEGACY_RESTART_SKIPPED",
    "PROGRAM_KIND_ATTRIBUTE",
    "PROGRAM_KIND_HANDOFF_OK",
    "PROGRAM_KIND_HANDOFF_REFUSED",
    "COBOL_TRANSFORMER_KEY",
    "STATEMENT_TRANSFORMER_ATTRIBUTE",
    "STATEMENT_TRANSFORMER_NAME",
    "STATEMENT_TRANSFORMER_UNREACHABLE",
    "LRF_EXPANDER_KEY",
    "LRF_CALC_RECORDS_ATTRIBUTE",
    "CALC_PARENT_RECORDS_ATTRIBUTE",
    "LRF_CALC_RECORDS_PUBLISHED",
    "LRF_CALC_RECORDS_NONE",
    "COMMIT_CLEANUP_MISSING",
    "DATE_COMPARE_MISSING",
]