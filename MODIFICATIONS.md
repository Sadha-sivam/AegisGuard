# Modifications to Strix

AegisGuard is a derivative of **Strix 1.7.1** (<https://github.com/usestrix/strix>, Apache-2.0,
Copyright 2025 OmniSecure Inc.). This file states what was changed (Apache-2.0 section 4(b)).
The upstream `LICENSE` is byte-identical to the supplied Strix archive, and all upstream
copyright notices are retained. Changed code files also carry a short in-file modification notice.

The comparison baseline is the Strix archive supplied by the maintainer; it was not compared
against the live GitHub repository (no network) and no Git history was available.

## Design rule

Only product identity, packaging and documentation were changed. Functional code, dependencies,
tests (apart from one string assertion), the Python package name (`strix`), the `strix` command,
`STRIX_*` environment variables, `~/.strix`, the sandbox image name and upstream API headers are
untouched, because renaming them would break behavior or compatibility.

## Summary of provenance (552 upstream files)

| Category | Files |
|----------|-------|
| Unchanged from the supplied Strix archive | 491 |
| Modified | 59 (about 40 are documentation; code changes total roughly 60 added lines of branding text) |
| New | 5 (`NOTICE`, `MODIFICATIONS.md`, `PORTFOLIO.md`, `.env.example`, `docs/logo/aegisguard.png`) plus `AUDIT_REPORT.md` |
| Removed | 2 (`docs/logo/strix.png`; `.github/screenshot.png`, relocated to `docs/images/screenshot.png`) |

## Changes

| Area | Change |
|------|--------|
| CLI | Panel titles `STRIX` to `AEGISGUARD`; `--help` description; headless hint; post-scan footer replaced by an attribution line. New `aegisguard` console script (`pyproject.toml`) next to `strix`. |
| OAuth callback page | Brand text and links (`auth_cli.py`) now point to AegisGuard and credit Strix. |
| Terminal UI (Go) | Splash, "Connecting..." and "Welcome to..." strings (`view.go`, `model.go`). Not compiled or tested. |
| Local viewer | Page title, header and sidebar brand text, privacy sentence in `frontend/src` and in the prebuilt bundle `static/assets/index-B1JzV4Vu.js` (patched in place; regenerate with `make viewer`). |
| PDF report | Wordmark, logo letter and document metadata. |
| Assets | New shield logo and favicon (original artwork by the maintainer's session): `.github/logo.png`, viewer `logo.png` x2, `docs/images/logo.png`, `docs/logo/aegisguard.png`, `docs/images/favicon-48.ico`. |
| Packaging | `pyproject.toml`: description, `maintainers`, project URLs, `aegisguard` script. Distribution name stays `strix-agent` because code reads that metadata. |
| Documentation | New README, NOTICE, `.env.example`, MODIFICATIONS, PORTFOLIO, AUDIT_REPORT. Prose "Strix" to "AegisGuard" in `docs/` (not `docs/cloud/`, which documents the upstream commercial service), `AGENTS.md`, `CONTRIBUTING.md`. Upstream installer commands replaced with source installs. `strix/telemetry/README.md` keeps original text plus an attribution note. |
| Repo hygiene | `.gitignore` additions; screenshot caption clarifying it is upstream's. |
| Tests | `tests/test_main_launch.py`: expected headless-hint wording updated. |

## Known upstream coupling (unchanged)

Telemetry (PostHog/Scarf), update checks and `--update`, `strix cloud`, the viewer's email and
feedback relay, ChatGPT OAuth using Codex CLI identifiers, and the default sandbox image all
use upstream services or registries.

## Validation performed

Environment: offline sandbox, Python 3.12.3, no Docker, no Go, no network.

| Check | Result |
|-------|--------|
| `python -m compileall strix tests scripts` | Passed |
| `node --check` on the patched viewer bundle | Passed |
| TOML / JSON / workflow YAML parsing | Passed |
| Secret and personal-data scan | No credentials found (details in AUDIT_REPORT.md) |
| File-set comparison with the supplied archive | Matches this document |
| `pytest`, `ruff`, `mypy`, `uv lock --check`, app start-up, viewer, Docker sandbox, agent run, Go build and tests | **Not run** (dependencies could not be installed) |

## Modified files: code, packaging, assets

- `pyproject.toml`
- `strix/interface/auth_cli.py`
- `strix/interface/cli_args.py`
- `strix/interface/main.py`
- `strix/interface/tui/internal/app/model.go`
- `strix/interface/tui/internal/app/view.go`
- `strix/interface/viewer/cli.py`
- `strix/interface/viewer/frontend/index.html`
- `strix/interface/viewer/frontend/src/App.tsx`
- `strix/interface/viewer/frontend/src/components/Sidebar.tsx`
- `strix/interface/viewer/report_pdf.py`
- `strix/interface/viewer/static/assets/index-B1JzV4Vu.js`
- `strix/interface/viewer/static/index.html`
- `tests/test_main_launch.py`

## Modified files: documentation and images

- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/logo.png`
- `.gitignore`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `README.md`
- `benchmarks/README.md`
- `docs/README.md`
- `docs/advanced/configuration.mdx`
- `docs/advanced/skills.mdx`
- `docs/contributing.mdx`
- `docs/docs.json`
- `docs/images/favicon-48.ico`
- `docs/images/logo.png`
- `docs/index.mdx`
- `docs/integrations/ci-cd.mdx`
- `docs/integrations/coding-agents.mdx`
- `docs/integrations/github-actions.mdx`
- `docs/integrations/mcp.mdx`
- `docs/llm-providers/anthropic.mdx`
- `docs/llm-providers/azure.mdx`
- `docs/llm-providers/bedrock.mdx`
- `docs/llm-providers/local.mdx`
- `docs/llm-providers/novita.mdx`
- `docs/llm-providers/openai.mdx`
- `docs/llm-providers/openrouter.mdx`
- `docs/llm-providers/overview.mdx`
- `docs/llm-providers/vercel-ai-gateway.mdx`
- `docs/llm-providers/vertex.mdx`
- `docs/quickstart.mdx`
- `docs/tools/browser.mdx`
- `docs/tools/overview.mdx`
- `docs/tools/proxy.mdx`
- `docs/tools/sandbox.mdx`
- `docs/tools/terminal.mdx`
- `docs/usage/cli.mdx`
- `docs/usage/instructions.mdx`
- `docs/usage/scan-modes.mdx`
- `docs/usage/viewer.mdx`
- `strix/interface/viewer/frontend/public/logo.png`
- `strix/interface/viewer/static/logo.png`
- `strix/skills/README.md`
- `strix/telemetry/README.md`
- `strix/tools/agent_browser/README.md`
- `strix/tools/view_image/README.md`
