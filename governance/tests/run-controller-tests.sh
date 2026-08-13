#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"
export PYTHONDONTWRITEBYTECODE=1
python3 -m pytest governance/tests/controller "$@"
