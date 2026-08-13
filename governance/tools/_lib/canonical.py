"""Compatibility export for reusable L6 canonicalization helpers."""

from governance.framework_runtime import l6_module
globals().update(vars(l6_module("canonical")))
