"""Run directory path helpers."""

from __future__ import annotations

from pathlib import Path

from strix.core.brand import (
    LEGACY_RUNS_DIR_NAME,
    preferred_runs_dir_name,
    runs_search_dir_names,
)

# Public name used by CLI help / docs. New runs write under this name by default
# (or AEGISGUARD_RUNS_DIR / STRIX_RUNS_DIR). Legacy ``strix_runs`` remains
# discoverable for resume/view.
RUNS_DIR_NAME = preferred_runs_dir_name()
RUNTIME_STATE_DIR_NAME = ".state"
RUN_RECORD_FILENAME = "run.json"


def run_dir_for(run_name: str, *, cwd: Path | None = None) -> Path:
    base = cwd or Path.cwd()
    return base / preferred_runs_dir_name() / run_name


def runtime_state_dir(run_dir: Path) -> Path:
    return run_dir / RUNTIME_STATE_DIR_NAME


def run_record_path(run_dir: Path) -> Path:
    return run_dir / RUN_RECORD_FILENAME


def runs_base_dir(*, cwd: Path | None = None) -> Path:
    """Primary runs directory for new output (AegisGuard name by default)."""
    base = cwd or Path.cwd()
    return base / preferred_runs_dir_name()


def existing_runs_dirs(*, cwd: Path | None = None) -> list[Path]:
    """Existing run roots to search (preferred first, then legacy)."""
    base = cwd or Path.cwd()
    dirs: list[Path] = []
    for name in runs_search_dir_names():
        path = base / name
        if path.is_dir() and path not in dirs:
            dirs.append(path)
    # Also surface a legacy directory that exists even if preferred name was overridden
    legacy = base / LEGACY_RUNS_DIR_NAME
    if legacy.is_dir() and legacy not in dirs:
        dirs.append(legacy)
    return dirs


def latest_run_dir(*, cwd: Path | None = None) -> Path | None:
    candidates: list[Path] = []
    for root in existing_runs_dirs(cwd=cwd):
        candidates.extend(
            child for child in root.iterdir() if run_record_path(child).is_file()
        )
    if not candidates:
        # Fall back to empty preferred dir existence check for callers that mkdir later
        return None
    # run.json is rewritten on status/end changes, so its mtime tracks activity
    # more reliably than the directory mtime (a live run sorts to the top).
    return max(candidates, key=lambda child: run_record_path(child).stat().st_mtime)
