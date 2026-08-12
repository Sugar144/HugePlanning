"""Bounded deterministic helpers for governance tooling."""

__version__ = "0.1.0"

from .identity import Allocation, Allocator, IdentityError, parse, resolve_historical

__all__ = ["Allocation", "Allocator", "IdentityError", "parse", "resolve_historical"]
