# AegisGuard Pre-Publication Audit Report

Maintainer: Sadhasivam (<https://github.com/Sadha-sivam>) · Audit date: 2026-11-23
Scope: the AegisGuard working tree compared with the Strix 1.7.1 archive supplied by the maintainer.

> This is a technical audit, not legal advice. Items marked **UNVERIFIED** could not be confirmed
> in an offline sandbox (no network, no Git history, no package installs). A similarity or
> provenance comparison shows what differs from the supplied archive; it does not prove ownership.

## A. Copyright and license findings

| Finding | Evidence | Status |
|---------|----------|--------|
| Governing license is **Apache License 2.0** | `LICENSE` is the Apache 2.0 text; `pyproject.toml` declares `Apache-2.0`; the nine `skills/*/SKILL.md` front matters declare `license: Apache-2.0` | Verified in the supplied archive |
| Copyright holder named: **OmniSecure Inc., 2025** | Appendix boilerplate at the end of `LICENSE` (line 189). Source files carry no per-file copyright headers | Verified in file; **UNVERIFIED** against the live GitHub repo |
| `LICENSE` unmodified | SHA-256 identical to the supplied archive (`7db96971...e7b9e3`) | Verified |
| No conflicting license files | Only one `LICENSE`; no `COPYING`, no vendored third-party license files | Verified |
| Upstream has no `NOTICE` file | Nothing to carry forward under Apache-2.0 §4(d) | Verified |
| Redistribution and modification permitted | Apache-2.0 §2 and §4 grant copyright and patent licenses to reproduce, modify, distribute and sublicense, including commercially | Per license text |
| Rebranding permitted | Apache-2.0 §6 gives no trademark rights, so the name "Strix" and its logo cannot be used as your product identity. Renaming to AegisGuard is the compliant choice; stating "based on Strix" is factual attribution | Compliant |
| Publishing on your own GitHub permitted | Conditions in §4: (a) include the license, (b) mark modified files, (c) keep existing notices, (d) carry a NOTICE if one exists. All four are addressed (see E) | Compliant, subject to E |

Changing the product name does not transfer ownership of Strix code. The Strix authors keep
copyright in their code; you hold copyright only in your own modifications and new files.

## B. Original Strix code and attribution

Baseline: the supplied `strix-main.zip` (version 1.7.1 in `pyproject.toml`; the second upload was byte-identical).

| Category | Count |
|----------|-------|
| Files in the supplied Strix archive | 552 |
| Unchanged in AegisGuard | 491 |
| Modified | 59 (about 40 documentation, the rest branding strings, logos and packaging) |
| New | 6 (`NOTICE`, `MODIFICATIONS.md`, `PORTFOLIO.md`, `AUDIT_REPORT.md`, `.env.example`, `docs/logo/aegisguard.png`) |
| Removed | 2 (old Strix logo copy; screenshot relocated) |

Roughly 105,700 lines of upstream Python, Go and TypeScript exist; fewer than about 60 lines of
code were changed, all branding text or packaging metadata. Everything functional in AegisGuard is
Strix's work.

Attribution now appears in: `README.md` (banner, section 16), `NOTICE`, `MODIFICATIONS.md`,
`pyproject.toml` (original `authors` entry kept, you added under `maintainers`), the CLI footer,
the OAuth callback page, and a notice at the top of every changed code file.
Your name appears only in maintainer, contribution and notice sections, never in original headers.

## C. AegisGuard modifications

See `MODIFICATIONS.md` for the full list. In short: CLI/TUI/viewer/PDF/OAuth-page branding
strings, an `aegisguard` command alias, new logo and favicon, `pyproject.toml` metadata, rewritten
README and new compliance/portfolio documents, install instructions repointed from upstream
installers to your repository, one edited test assertion.

## D. Your actual contributions (accurate wording)

- Branding of user-facing surfaces and design of the logo/favicon.
- Packaging metadata and the `aegisguard` alias.
- Documentation: README, NOTICE, MODIFICATIONS, AUDIT_REPORT, PORTFOLIO, `.env.example`, `.gitignore`, CONTRIBUTING maintainer section.
- License/attribution compliance work and a secret/privacy review.

Do **not** claim: authorship of the agent engine, tools, runtime, reporting, TUI or viewer; passing
tests; working builds; scans performed. None of these have been demonstrated yet.

## E. Missing attribution or licensing issues

| # | Issue | Severity | Action |
|---|-------|----------|--------|
| 1 | Apache-2.0 §4(b) asks modified files to carry prominent change notices | Medium | **Fixed** for code files (in-file notice). About 40 documentation files rely on `MODIFICATIONS.md` as the notice; this is a common practice but whether it fully satisfies §4(b) is **UNVERIFIED** |
| 2 | Trademark: "Strix" name and logo | Low | Logo replaced everywhere; leftover "S" mark in PDF reports changed to "A"; remaining "Strix" strings are functional identifiers or factual attribution |
| 3 | Remaining Strix-branded image: `docs/images/screenshot.png` (window title "Strix") | Low | Kept, captioned as upstream's. Replace with your own capture |
| 4 | CC-BY-4.0 icon: `react-icons/vsc` (VS Code codicons) is compiled into the viewer bundle | Low | Attribution added to `NOTICE`. **UNVERIFIED**: license of that icon set is from lockfile/package knowledge, not checked offline |
| 5 | MIT/ISC/BSD notices for bundled JS and Go libraries | Low | The bundle keeps React and Lucide license comments only. Generate a full third-party notice list on your machine (e.g. with a license checker) before shipping binaries |
| 6 | Python dependency licenses are not recorded in `uv.lock` | Medium | **UNVERIFIED.** From general knowledge (not confirmed offline): `cvss` is LGPL-3.0, `certifi` and `tqdm` carry MPL-2.0, PyInstaller (dev only) is GPL-2.0 with a bootloader exception. Importing LGPL/MPL packages unmodified is normally fine; shipping a frozen PyInstaller binary adds obligations. Run a license report (`uv run pip-licenses` or similar) before releasing binaries. `caido-sdk-client` license is unknown |
| 7 | npm: 284 packages: MIT 247, ISC 16, MPL-2.0 12, BSD-3 4, Apache-2.0 3, 0BSD 1, CC-BY-4.0 1 | Info | MPL-2.0 entries are `lightningcss` and CC-BY-4.0 is `caniuse-lite`; both appear to be build-time tools (dev dependencies), not shipped code. Inference, **UNVERIFIED** |
| 8 | Go modules (Bubble Tea, Lip Gloss, Bubbles, chroma, x/sys etc.) | Info | Believed MIT/BSD; **UNVERIFIED** (no module cache offline) |
| 9 | Sandbox image `ghcr.io/usestrix/strix-sandbox` is hosted by upstream; its contents and tool licenses are outside this repo | Medium | Documented in README limitations. You may build your own from `containers/Dockerfile` |
| 10 | `containers/Dockerfile` downloads many third-party tools and the community Opengrep ruleset at build time | Info | Not redistributed in the repo. Only one rule file (upstream-authored) is stored. The downloaded ruleset's license is **UNVERIFIED** |
| 11 | ChatGPT sign-in uses OpenAI Codex CLI client ID and `originator` values (`strix/config/codex.py`) | Medium | Third-party terms risk, not a copyright issue. **UNVERIFIED** whether OpenAI permits it. Documented in README; consider not promoting or disabling this feature |
| 12 | No Git history in the archive | Info | Contributor list and exact authorship cannot be verified. See H for the transparent commit plan |

No evidence of copied third-party prose in skills/docs was found by keyword search (only links to
PortSwigger research and SecLists). A true text-similarity scan was not possible offline: **UNVERIFIED**.

## F. Secret scan results

Scanned all text files except lockfiles and the minified bundle (which was grepped separately).

| Check | Result |
|-------|--------|
| Vendor key patterns (OpenAI, Anthropic, AWS, GitHub, Slack, Google, Stripe, JWT, private keys) | None found. One false positive in minified CSS |
| Hardcoded credential assignments | Only a placeholder string `strix-codex-oauth` in `codex.py` (not a secret) |
| High-entropy literals | One PostHog project key `phc_...` in `strix/telemetry/posthog.py`. It is upstream's write-only analytics key, not yours; it is left unchanged because removing it would break telemetry code |
| Personal data | No personal data from you was present; the only emails are test fixtures and the upstream contact `hi@usestrix.com` in `pyproject.toml` `authors`. Your public email was added deliberately to README, CONTRIBUTING and `pyproject.toml` |
| Local paths, private IPs | Only fake values in tests and help text |
| Stray files (`.env`, logs, databases, keys, `run.json`) | None. `.env.example` contains placeholders only |

Nothing needed removal. `.gitignore` now also ignores `.env.*` (except the example), `.strix/`, `cli-config.json`, `*.pem`, `*.key`; `strix_runs/` was already ignored.

## G. Files changed during the audit

Code: `strix/interface/auth_cli.py` (branding), `strix/interface/viewer/report_pdf.py` (logo letter), in-file modification notices on all changed code files, `pyproject.toml` (maintainers, URLs, notice).
Docs: `README.md` (maintainer, contributions, caveats), `CONTRIBUTING.md`, `NOTICE`, `PORTFOLIO.md`, `MODIFICATIONS.md` (regenerated), `AUDIT_REPORT.md` (new). Placeholders `YOUR-USERNAME` and `YOUR NAME` replaced with your details across README, NOTICE and docs.

## H. GitHub publication readiness

Suggested description (≤350 chars):
> AegisGuard: multi-agent AI penetration-testing CLI that validates findings with real exploit attempts in a Docker sandbox. A customized, maintained build of the open-source Strix project (Apache-2.0).

Topics: `cybersecurity`, `penetration-testing`, `application-security`, `ai-agents`, `llm`, `security-automation`, `devsecops`, `docker`, `python`, `golang`, `react`, `sarif`, `strix`, `apache-2-0`.

Recommended commit plan (transparent history):
1. `git init`, add the original Strix files unchanged, and commit as "Import Strix 1.7.1 upstream snapshot".
2. Apply AegisGuard's changes and commit as "Rebrand as AegisGuard; add maintainer docs and notices".
Do not squash into one commit that hides the upstream origin.

Checklist before pushing:
- [ ] Compare `LICENSE` with <https://github.com/usestrix/strix/blob/main/LICENSE>.
- [ ] Run `uv sync && uv run pytest`, `make check-all`, `make tui-test`; record real results in README section 13.
- [ ] Decide on telemetry default (see I) and recapture a screenshot from your own run.
- [ ] Review `.github/workflows` (upstream release workflows); disable `build-release.yml` unless you set up releases.
- [ ] Nothing was published or uploaded by this audit.

## I. Remaining legal or technical concerns

1. Nothing was executed: tests, app start-up, Docker sandbox, agent runs, Go build and `uv lock --check` are all **not run**. The patched viewer bundle and Go strings are untested.
2. Telemetry is on by default and sends data to upstream's PostHog/Scarf accounts. The README discloses this, but as maintainer you should consider making it opt-in by default (a small code change I did not make, to preserve behavior).
3. Update checks and `--update` point at upstream and would replace your fork.
4. The ChatGPT/Codex OAuth identity use (E-11) and upstream Cloud/Enterprise prompts in the viewer UI remain.
5. Dependency and sandbox-image licenses are only partly verified (E-4 to E-10).
6. The upstream authors' copyright holder and contributor list are unverified without Git history or network access.

## J. Final deliverable

`AegisGuard.zip` contains the complete project folder `AegisGuard/`.
