"""Keep the complete Phase 2 unittest evidence under the pytest entry point."""

from __future__ import annotations

from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from test_controller import PackageSecurityTests, SchemaAndLoopTests, TransitionTests
