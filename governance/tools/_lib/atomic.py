"""Compatibility export for the reusable L6 atomic-write helper."""

from governance.framework_runtime import l6_module
globals().update(vars(l6_module("atomic")))
