# Working on this catalog

This repository lists Google Ads MCP servers, command-line tools, and SDKs in plain English. Use [CONTRIBUTING.md](CONTRIBUTING.md) as the source of truth for scope and inclusion rules.

## Review workflow

1. Read every tracked file and identify catalog claims that need verification.
2. Check each candidate against its canonical repository, setup instructions, and implementation. Use official Google documentation to verify official status and API support.
3. Keep evidence links for every added or changed capability in the commit or pull request description. Distinguish source inspection from an authenticated live test.
4. Update the relevant README table and comparison row together. Recount each section and check internal anchors and external links.
5. Run `npx --yes markdownlint-cli2@latest "**/*.md"` and `git diff --check`; both must pass before committing.

## Catalog format

- Keep separate MCP, CLI, and SDK sections with counts and two-column project tables.
- Give each project a stable `<a id="owner-repo"></a>` anchor and a canonical repository link.
- Describe each project in one or two factual sentences, focusing on its Google Ads interface.
- Keep the comparison matrix compact. Link project names to their table entries and record only verified capabilities.
- Keep general tutorials, discovery dumps, rankings, and exclusion ledgers outside the published catalog.
