"""AegisGuard product identity and config-path helpers.

The Python import package remains ``strix`` for compatibility with the upstream
codebase. User-facing product identity is AegisGuard. Config/run directories
prefer AegisGuard names and fall back to legacy Strix paths when present.
"""

from __future__ import annotations

import os
from pathlib import Path


PRODUCT_NAME = "AegisGuard"
PRODUCT_NAME_UPPER = "AEGISGUARD"
PRODUCT_TAGLINE = "AI-Powered Autonomous Security Testing Platform"
PRODUCT_REPO_URL = "https://github.com/Sadha-sivam/AegisGuard"
UPSTREAM_NAME = "Strix"
UPSTREAM_REPO_URL = "https://github.com/usestrix/strix"
DISTRIBUTION_NAME = "strix-agent"  # PyPI/importlib metadata name (unchanged)

LEGACY_CONFIG_DIRNAME = ".strix"
CONFIG_DIRNAME = ".aegisguard"
LEGACY_RUNS_DIR_NAME = "strix_runs"
RUNS_DIR_NAME = "aegisguard_runs"


def config_dir() -> Path:
    """Return the active config directory.

    Prefers ``~/.aegisguard``. If it does not exist but the legacy ``~/.strix``
    directory does, that path is used so existing installs keep working.
    New writes should call ``ensure_config_dir()``.
    """
    preferred = Path.home() / CONFIG_DIRNAME
    legacy = Path.home() / LEGACY_CONFIG_DIRNAME
    if preferred.exists() or not legacy.exists():
        return preferred
    return legacy


def ensure_config_dir() -> Path:
    """Create and return the preferred AegisGuard config directory."""
    path = Path.home() / CONFIG_DIRNAME
    path.mkdir(parents=True, exist_ok=True)
    return path


def config_file(name: str) -> Path:
    """Resolve a named file under the active config directory."""
    return config_dir() / name


def preferred_runs_dir_name() -> str:
    """Directory name for new scan runs (overridable via env)."""
    override = os.environ.get("AEGISGUARD_RUNS_DIR") or os.environ.get("STRIX_RUNS_DIR")
    if override:
        return override
    return RUNS_DIR_NAME


def runs_search_dir_names() -> tuple[str, ...]:
    """Directory names to search when locating existing runs."""
    preferred = preferred_runs_dir_name()
    names = [preferred]
    if LEGACY_RUNS_DIR_NAME not in names:
        names.append(LEGACY_RUNS_DIR_NAME)
    return tuple(names)
