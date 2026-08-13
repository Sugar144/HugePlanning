"""Resolve GOV-GEN helpers only from the externally acquired locked framework."""
from __future__ import annotations

from functools import lru_cache
import importlib
import importlib.util
import os
from pathlib import Path
import sys
from types import ModuleType


ENVIRONMENT_VARIABLE = "GOV_GEN_FRAMEWORK_ROOT"


@lru_cache(maxsize=1)
def framework_root() -> Path:
    value = os.environ.get(ENVIRONMENT_VARIABLE)
    if not value:
        raise RuntimeError(f"{ENVIRONMENT_VARIABLE} is required; run scripts/acquire-framework.py first")
    root = Path(value).resolve()
    if not (root / "framework/core/project-operating-contract.md").is_file():
        raise RuntimeError("configured GOV-GEN framework root is incomplete")
    return root


@lru_cache(maxsize=None)
def l6_module(name: str) -> ModuleType:
    package_name = "_hugeplanning_locked_gov_gen_l6"
    package = sys.modules.get(package_name)
    if package is None:
        init = framework_root() / "framework/core/l6/__init__.py"
        spec = importlib.util.spec_from_file_location(package_name, init, submodule_search_locations=[str(init.parent)])
        if spec is None or spec.loader is None:
            raise RuntimeError("locked GOV-GEN L6 package cannot be loaded")
        package = importlib.util.module_from_spec(spec)
        sys.modules[package_name] = package
        spec.loader.exec_module(package)
    return importlib.import_module(f"{package_name}.{name}")


def framework_path(relative: str) -> Path:
    path = framework_root() / relative
    if not path.is_file():
        raise RuntimeError(f"locked GOV-GEN framework surface is missing: {relative}")
    return path
