"""Compatibility export for reusable L6 diagnostics helpers."""

from governance.framework_runtime import l6_module
globals().update(vars(l6_module("diagnostics")))
