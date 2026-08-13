"""Shared bounded configuration for the pytest Controller suite."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

from hypothesis import HealthCheck, settings


REPO = Path(__file__).resolve().parents[3]
GOV = REPO / "governance"
TOOLS = GOV / "tools"
LOOP = GOV / "methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml"
TRANSITION_FIXTURES = GOV / "tests/fixtures/transitions"
PACKAGE_GENERATOR = GOV / "tests/fixtures/packages/generate_cases.py"

sys.path.insert(0, str(TOOLS))

spec = importlib.util.spec_from_file_location("controller_package_cases", PACKAGE_GENERATOR)
PACKAGE_CASES = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(PACKAGE_CASES)

PROPERTY_EXAMPLES = 50
STATE_MACHINE_EXAMPLES = 30
STATE_MACHINE_STEPS = 12

settings.register_profile(
    "controller",
    max_examples=PROPERTY_EXAMPLES,
    deadline=None,
    database=None,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
settings.load_profile("controller")
