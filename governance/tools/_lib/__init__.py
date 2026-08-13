"""Compatibility exports for the reusable L6 helper sublayer."""

import sys
from pathlib import Path


repository_root = Path(__file__).resolve().parents[3]
if str(repository_root) not in sys.path:
    sys.path.insert(0, str(repository_root))

from governance.framework_runtime import l6_module

__version__ = l6_module("__init__").__version__

__all__ = ["__version__"]
