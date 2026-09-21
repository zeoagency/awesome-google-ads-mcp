# Contributing to Awesome Google Ads MCP

Thank you for contributing to **Awesome Google Ads MCP**! This repository is a strictly curated, developer-focused index and technical comparison of Model Context Protocol (MCP) servers and agent-facing tooling for the **Google Ads API**.

To maintain institutional engineering quality and prevent directory bloat, all submissions must satisfy our **15 Inclusion Criteria**.

---

## Inclusion Criteria Checklist

Before submitting a Pull Request, verify that your project satisfies every applicable requirement:

1. **Protocol Compliance:** Must implement the Model Context Protocol (MCP) specification (JSON-RPC 2.0 over `stdio`, `sse`, or `streamable-http`) OR provide a dedicated, executable agentic tool wrapper for Google Ads.
2. **Current API Surface:** Must interface with the current **Google Ads API** (REST v17+ or gRPC). Tools interfacing exclusively with the sunset AdWords API are quarantined in `docs/EXCLUSIONS.md`.
3. **Strict Domain Boundary:** Scope is exclusively Google Ads (Search, Display, Shopping, Performance Max, Video, App, Demand Gen, Local). Generic paid-media directories or cross-channel ad tools qualify only if they provide cleanly separable, first-class Google Ads API toolsets.
4. **Code Evidence Required:** Must point to a repository with functional, executable code. Repositories containing only a README, boilerplate without logic, or placeholder commits are rejected.
5. **Canonical Repository:** In case of forks or clones, only the canonical upstream repository or actively maintained independent forks are accepted.
6. **Verifiable Write Safety:** Any tool claiming write capabilities (campaign creation, budget updates, bid adjustments, offline conversion uploads) must demonstrate working mutate endpoints with safety guardrails (such as `validate_only` dry-runs).
7. **Explicit Campaign Types:** Must document which campaign types are actually supported (e.g. Search-only vs Performance Max/Shopping).
8. **Auth Model Transparency:** Must document required authentication flows (OAuth2 Desktop/Web, Service Account impersonation, Refresh Token daemon, Developer Token tier).
9. **MCC Multi-Account Support:** Must explicitly declare whether it supports Manager Accounts (MCC) via `login-customer-id` header injection.
10. **Clean Subprocess Handling:** Stdio subprocess wrappers must properly isolate I/O buffers (e.g., handling Windows pipe deadlocks via `stdin=subprocess.DEVNULL`).
11. **Local Caching Protocols:** Meta-MCP tools ingesting data into SQLite must implement clean cache synchronization without unbounded data drift.
12. **MCP Apps Verification:** Tools claiming UI rendering must implement `@modelcontextprotocol/ext-apps` sandboxed view protocols.
13. **Active Maintenance:** Archived or abandoned repositories are labeled as `[Archived]` and included only if they demonstrate historical architectural reference value.
14. **Public Source Access:** Closed-source commercial products qualify only if an open client connector or MCP wrapper repository is publicly accessible.
15. **Plain-English Description:** Submissions must include a concise description ($\le 3$ sentences) highlighting exact technical differentiation, supported API resources, and target developer persona.

---

## Submission Workflow

1. Fork the repository.
2. Add your project to the appropriate subcategory table in `README.md` following the exact format:

   ```markdown
   | <a id="owner-repo"></a>[**owner/repo**](https://github.com/owner/repo) | Concise factual description of what it actually does. |
   ```

3. Update the Developer Comparison Matrix with verified technical capabilities.
4. Ensure all category counts and subcategory counts in `## Contents` and section headers remain mathematically consistent.
5. Run the markdown linter:

   ```bash
   npx markdownlint-cli2 "**/*.md"
   ```

6. Submit your Pull Request. All CI checks must pass.
