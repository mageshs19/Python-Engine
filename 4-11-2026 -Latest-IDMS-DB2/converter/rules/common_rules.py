"""Canonical identifiers and policy constants shared by conversion stages.

This module contains values that identify a conversion rule or stage. It does
not contain program-specific business values, which must come from source,
subschema, copybook, DCLGEN, or sheet mapping data.
"""

# LRF normalization component registry keys.
TRANSFORMER_LRF_PATH_EXPANDER = "lrf_path_expander"
TRANSFORMER_LRF_UPDATE_EXPANDER = "lrf_update_expander"
TRANSFORMER_LR_STATUS_REPLACER = "lr_status_token_replacer"
TRANSFORMER_COBOL = "cobol"
TRANSFORMER_FIELD_REFERENCE = "field_reference"

# Human-readable stage labels.
LABEL_LRF_READ = "LRF expansion"
LABEL_LRF_UPDATE = "LRF update expansion"
LABEL_LR_STATUS = "LR-STATUS tokens"

# Component protocol method names.
METHOD_EXPAND = "expand"
METHOD_APPLY = "apply"

# Diagnostic templates. Keep wording in one place for consistent reports.
LRF_STAGE_NOT_WIRED_TEMPLATE = (
    "{label}: no component was wired under '{key}'; the logical-record "
    "syntax it owns will reach the output unconverted."
)
LRF_STAGE_NO_METHOD_TEMPLATE = (
    "{label}: the component wired under '{key}' has no {method}() method; "
    "the stage was skipped."
)
LRF_STAGE_FAILED_TEMPLATE = (
    "{label}: skipped, the text from the previous stage will be used. "
    "Reason: {reason}"
)

# Opt-in compatibility behavior. Off by default to preserve the required
# LRF -> ordinary IDMS -> DB2 conversion architecture.
ENV_ENABLE_LRF_SINGLETON_SHORTCUT = "IDMS_DB2_ENABLE_LRF_SINGLETON_SHORTCUT"
DEFAULT_ENABLE_LRF_SINGLETON_SHORTCUT = "0"
TRUTHY_CONFIG_VALUES = frozenset({"1", "true", "yes"})

# Common diagnostic/status markers.
DB2_KEEP_MARKER = "DB2-KEEP"
