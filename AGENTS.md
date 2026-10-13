# Working on this catalog

This repository lists Google Ads MCP servers, command-line tools, and SDKs in plain English. Use [CONTRIBUTING.md](CONTRIBUTING.md) as the source of truth for scope and inclusion rules.

## Review workflow

1. Read every tracked file and identify catalog claims that need verification.
2. Check each candidate against its canonical repository, setup instructions, and implementation. Use official Google documentation to verify official status and API support.
3. For MCP records, capture the actual offline `tools/list` interface at a pinned commit. Inspect registration and handlers separately; record optional tools, prefixes, client visibility, and write gates. Capture the complete inventory across supported configurations; put non-Ads tools in separate sections on the same provider page.
4. Keep each tool's description, full recursive input schema, and pinned source link in its `docs/mcp/` page. Update `docs/TOOLS.md` and the relevant README task rows together. Distinguish source inspection and offline listing from authenticated live tests.
5. Run `node .github/check-catalog.mjs`, `npx --yes markdownlint-cli2@latest "**/*.md"`, and `git diff --check`; all must pass before committing.

## Catalog format

- Group MCP providers by what their tools and handlers actually do. Cross-list providers where useful; task counts are providers, and inventory totals are unique provider/tool pairs.
- Use Google Ads and shared-helper capabilities for the main task groups. Preserve other-platform and protocol-test tools in clearly labeled detail-page sections and in the full tool index.
- Keep CLI and SDK sections separate with counts and two-column tables. Give projects stable anchors and canonical repository links.
- Keep README entries to one or two factual sentences with direct links to representative tools. Put full descriptions and schemas on provider pages, with parameter blocks collapsed.
- Preserve exact exported names and schemas, including defaults, nullability, nested definitions, and constraints. Record behavior beyond the schema as a separate note; label generic payload objects rather than inventing Google API resource fields.
- Keep every provider/tool pair in the alphabetical tool index. Different providers can share a name with different parameters.
- Preserve upstream license notices for extracted descriptions and schemas.
- Keep general tutorials, discovery dumps, rankings, and exclusion ledgers outside the published catalog.
