"""Compatibility export for the reusable L6 ZIP inspection helper."""

from governance.framework_runtime import l6_module
globals().update(vars(l6_module("safe_zip")))
