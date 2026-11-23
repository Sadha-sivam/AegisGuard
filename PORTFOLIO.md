# AegisGuard: Portfolio Materials

Maintainer: Sadhasivam (https://github.com/Sadha-sivam). Fill in the bracketed items with what you actually did before publishing. Do not claim
authorship of the upstream Strix implementation.

## A. GitHub repository description (≤350 chars)

> AegisGuard: multi-agent AI penetration-testing CLI that validates findings with real exploit
> attempts in a Docker sandbox. A customized, rebranded build of the open-source Strix project (Apache-2.0).

Suggested topics: `cybersecurity`, `penetration-testing`, `application-security`, `ai-agents`, `llm`, `security-automation`, `devsecops`, `docker`, `python`, `golang`, `react`, `sarif`, `strix`, `apache-2-0`

Suggested website field: leave empty, or your portfolio URL.

## B. Project summary

AegisGuard is a command-line application security tool in which cooperating LLM agents test a web
app, API or codebase. Agents map the target, drive a browser and an intercepting HTTP proxy, run
security tools in an isolated Docker container, and report only issues they can reproduce with a
proof of concept. Reports are written locally (including SARIF and PDF output) and can be browsed
in a local web viewer. It targets the problem of noisy static-analysis results and slow manual
testing. Stack: Python 3.12, Go (terminal UI), TypeScript/React (viewer), Docker, LiteLLM/OpenAI
Agents SDK. AegisGuard is a customized build of Strix 1.7.1 by its original authors.

## C. Technical highlights (present in the source)

- Root/child multi-agent orchestration with an agent graph and shared notes, to-do and coverage tools.
- Tool suite: Playwright browser, Caido HTTP proxy, shell, patch application, threat modeling, web search (Exa/Perplexity), MCP client.
- Docker sandbox runtime with a Kali-based image definition and bundled opengrep rules.
- Knowledge "skills" in Markdown for ~30 vulnerability classes plus recon, frameworks and protocols.
- Scan modes (quick/standard/deep), PR diff-scope, `--fail-on` severity gating, budget limits, resumable runs.
- Provider-agnostic LLM routing, context compaction and cost tracking.
- SARIF/PDF reporting, CVSS scoring, finding de-duplication.
- Local web viewer (React SPA) and Go Bubble Tea terminal UI.
- Extensive pytest suite (116 test modules) and Go TUI tests.

## D. My contributions

- Rebranded the CLI, terminal-UI strings, viewer, PDF report text and documentation; designed the logo and favicon.
- Added the `aegisguard` command alias and updated package metadata.
- Wrote a new README, NOTICE, change log (`MODIFICATIONS.md`) and `.env.example`.
- Replaced install instructions that pointed at upstream installers; documented upstream telemetry, update-check and cloud coupling and how to disable it.
- Audited the repository for committed secrets and tightened `.gitignore`.
- [Add: test runs you performed, configuration you changed, bugs you fixed, scans you ran.]

I did not write the original agent, runtime, tooling or reporting implementation; that is Strix.

## E. Resume description

**AegisGuard: AI-Driven Penetration Testing CLI (customized fork of Strix, Apache-2.0)**
- Customized and rebranded an open-source multi-agent pentesting framework (Python, Go, React, Docker); added a CLI alias, new branding assets and complete documentation.
- Audited the fork for secrets and for telemetry/update/cloud calls to upstream services, and documented opt-outs and secure configuration.
- Maintained license compliance (Apache-2.0 NOTICE, attribution, change log).
- [Add measurable results from scans or tests you ran.]

## F. LinkedIn project description

AegisGuard is my customized build of Strix, an open-source framework where teams of LLM agents
test applications the way a penetration tester would: mapping the target, running tools in a
Docker sandbox, and validating each finding with a working proof of concept before reporting it.
I rebranded the CLI, terminal UI, viewer and reports, wrote the documentation, reviewed the
project's data flows (telemetry, update checks, cloud features) and kept it compliant with the
original Apache-2.0 license. The core engine was created by the Strix authors; my work is the
customization, packaging, documentation and security review. Skills: Python, Docker, application
security, LLM agents, secure configuration, open-source licensing.
