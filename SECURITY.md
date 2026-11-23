# Security Policy

## Supported versions

Security fixes are accepted for the current AegisGuard source on the default
branch of this repository.

## Reporting a vulnerability

Please report security issues privately:

- Email: [sadhasivam7172@gmail.com](mailto:sadhasivam7172@gmail.com)
- Or use GitHub Security Advisories on
  [`Sadha-sivam/AegisGuard`](https://github.com/Sadha-sivam/AegisGuard)

Include steps to reproduce, impact, and affected versions when possible. Do not
open a public issue for an unfixed vulnerability.

We aim to acknowledge reports within 7 days and to share a remediation plan
when confirmed.

## Authorized use only

AegisGuard is a penetration-testing tool. Use it only against systems you own or
have explicit written authorization to test. Unauthorized scanning or
exploitation is illegal and outside the intended use of this software.

## Scope

In scope:

- This repository and published packages derived from it
- The local CLI, viewer, and report generation code in this fork

Out of scope / third-party:

- Upstream Strix Cloud (`app.strix.ai`) and related managed services
- The default sandbox image hosted at `ghcr.io/usestrix/strix-sandbox` (unless
  you build and run your own image from `containers/Dockerfile`)
- Third-party LLM providers and MCP servers you configure

## Provenance

AegisGuard is a derivative of the open-source [Strix](https://github.com/usestrix/strix)
project (Apache License 2.0, Copyright 2025 OmniSecure Inc.). See `NOTICE` and
`MODIFICATIONS.md`.
