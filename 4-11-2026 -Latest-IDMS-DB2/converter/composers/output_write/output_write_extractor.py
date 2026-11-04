# LOCATION: converter/composers/output_write/output_write_extractor.py
# ACTION: CREATE NEW FILE
"""Performs one accepted extraction.

Lines are MOVED and re-indented, never edited: no condition, MOVE or
WRITE is ever rewritten. Two splices happen, in this order:

    1 the guarded body is replaced by the call site,
    2 the new paragraph is inserted after the host paragraph ends.

The second index must be corrected for the size change the first splice
caused, which is the whole reason this lives in its own class.
"""

from __future__ import annotations

import re
from converter.services.perform_thru_scope import perform_spans, paragraph_indices

from converter.composers.output_write.output_write_eligibility import (
    ExtractionPlan,
)
from converter.composers.output_write.output_write_line_utils import (
    OutputWriteLineUtils,
)
from converter.composers.output_write.output_write_renderer import (
    OutputWriteRenderer,
)
from converter.composers.output_write.output_write_scanner import (
    OutputWriteScanner,
)


class OutputWriteExtractor:
    """Splices the call site in and the new paragraph after."""

    def __init__(
        self,
        line_utils: OutputWriteLineUtils | None = None,
        renderer: OutputWriteRenderer | None = None,
        scanner: OutputWriteScanner | None = None,
    ) -> None:
        self.lines = line_utils or OutputWriteLineUtils()
        self.renderer = renderer or OutputWriteRenderer(self.lines)
        self.scanner = scanner or OutputWriteScanner(self.lines)

    # ----------------------------------------------------------- public
    def apply(self, lines: list[str], plan: ExtractionPlan) -> None:
        """Rewrite `lines` in place for one accepted plan."""
        block = plan.block
        template = self.lines.template_line(lines, block.if_index)

        call_site = self.renderer.call_site_lines(
            template=template,
            indent=self.lines.call_indent(lines, block.body_start),
            paragraph=plan.paragraph,
        )
        paragraph_block = self.renderer.paragraph_lines(
            template=template,
            paragraph=plan.paragraph,
            body=plan.body,
        )

        # A fixed-record output group that was cleared only at program start
        # must be reset for every record we materialise. Preserve the original
        # clear verb (MOVE SPACES), not an invented INITIALIZE variant.
        reset = self._per_write_reset(lines, plan)
        if reset:
            heading_index = next(
                (i for i, line in enumerate(paragraph_block)
                 if self.lines.paragraph_name(line) == plan.paragraph),
                None,
            )
            if heading_index is not None:
                paragraph_block.insert(heading_index + 1, reset)

        # 1. Replace the guarded body with the PERFORM call site.
        lines[block.body_start:block.end_index] = call_site

        # 2. Insert the new paragraph after the host paragraph ends,
        #    correcting for the size change step 1 just made.
        insert_at = self._insert_index(
            lines=lines,
            end_index=block.end_index,
            shift=len(call_site) - len(plan.body),
        )
        lines[insert_at:insert_at] = paragraph_block

    # ---------------------------------------------------------- helpers
    def _insert_index(
        self,
        *,
        lines: list[str],
        end_index: int,
        shift: int,
    ) -> int:
        """Index just past the paragraph that held the extracted block."""
        insertion = self.scanner.paragraph_end_index(lines, end_index + shift)
        # A PERFORM paragraph THRU exit-paragraph executes *every paragraph*
        # in the physical range. Never insert a generated helper inside it;
        # doing so can WRITE a second time or bypass the original IF guard.
        labels = paragraph_indices(lines)
        containing = [
            span for span in perform_spans(lines)
            if span.start_index <= end_index + shift <= span.end_index
        ]
        for span in containing:
            insertion = max(
                insertion,
                self.scanner.paragraph_end_index(lines, labels[span.end]),
            )
        return insertion

    def _per_write_reset(self, lines: list[str], plan: ExtractionPlan) -> str:
        """Preserve a source-proven fixed output-buffer clear per WRITE.

        Only move the reset into the extracted helper when the source already
        clears this exact FROM group outside the extracted body. Never assume
        a group name, initialization verb, or record encoding.
        """
        body = " ".join(self.lines.logical(line) for line in plan.body)
        write = re.search(
            r"\bWRITE\s+[A-Z0-9-]+\s+FROM\s+([A-Z0-9-]+)\b", body
        )
        if not write:
            return ""
        group = write.group(1)
        if re.search(rf"\bMOVE\s+SPACES?\s+TO\s+{re.escape(group)}\b", body):
            return ""
        earlier = lines[:plan.block.if_index]
        original = next((
            line for line in earlier
            if re.search(
                rf"\bMOVE\s+SPACES?\s+TO\s+{re.escape(group)}\b",
                self.lines.logical(line), re.I,
            )
        ), None)
        if original is None:
            return ""
        return self.lines.clone(original, f"    MOVE SPACES TO {group}")


__all__ = ["OutputWriteExtractor"]