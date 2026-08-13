"""Compatibility export for the reusable L6 strict-YAML helper."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from governance.framework_runtime import l6_module
globals().update(vars(l6_module("strict_yaml")))
