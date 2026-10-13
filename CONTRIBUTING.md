# Contributing

Suggest a Google Ads MCP server, command-line tool, or SDK with a link to its canonical public repository and evidence for the description.

## Inclusion rules

- Provide an implemented MCP interface, executable CLI, or reusable client library that calls the Google Ads API.
- Document installation, authentication, and at least one Google Ads usage example. Source inspection must confirm the advertised interface and API calls.
- Support a Google Ads API version that Google still supports. Check the [official sunset schedule](https://developers.google.com/google-ads/api/docs/sunset-dates); an old version number alone does not establish that an API is retired.
- Include multi-platform tools only when their Google Ads implementation is distinct and verifiable. Describe only that implementation here.
- Link to the canonical upstream project. Include an independent fork only if its Google Ads functionality materially differs and is maintained separately.
- Label libraries maintained by Google as official only when supported by [Google's client library documentation](https://developers.google.com/google-ads/api/docs/client-libs).

Exclude archived repositories, empty scaffolds, README-only connectors, prompt or skill collections, standalone tutorials, and legacy AdWords API tools. AdSense, Google Ad Manager, Analytics-only tools, and generic MCP or cloud utilities are outside this catalog's scope.

Stars, commit counts, repository age, and time since the last commit do not establish functionality or quality. Inspect the implementation rather than treating these figures as acceptance gates.

## Descriptions and evidence

Write one or two concise English sentences explaining the Google Ads functionality. Verify read and write operations, transports, caching, and safety features separately. A generic query endpoint does not establish full campaign management; previews and confirmation prompts do not establish API `validate_only` support.

Use repository documentation and source files to support claims. Include the evidence links in the pull request description, with the date checked. State whether verification used source inspection, local execution, or an authenticated Google Ads account. Avoid unmeasured performance claims, rankings, and guarantees of production readiness.

## Submit a change

1. For an MCP, add or refresh its page in `docs/mcp/` using actual offline `tools/list` output and a pinned source commit. Include every registered tool: exact exported name, complete description, full recursive input JSON Schema, and a source permalink. Capture optional configurations as well as the default tool list; explain prefixes, visibility, and invocation gates.
2. Compare the returned names with source registration and inspect each handler. Separate API reads, local calculations, staged previews, API validation, and real writes. Put other-platform tools and generic protocol fixtures in separate provider-page sections, with their platform or test purpose clearly labeled. Use only Google Ads and its shared helpers for the main task groups.
3. Add every provider/tool pair to `docs/TOOLS.md`, sorted by exact tool name. Update README task groups from implemented capabilities, linking to representative tools. A provider can appear in several groups; do not rank by tool count. Keep full catalog counts distinct from default-client counts and retain upstream licenses.
4. For a CLI or SDK, update its existing two-column README table and category counts. Check repository links, local page links, and anchors.
5. Run the checks used before committing:

   ```bash
   node .github/check-catalog.mjs
   npx --yes markdownlint-cli2@latest "**/*.md"
   git diff --check
   ```

6. Open a pull request explaining the change, linking to evidence, and stating the extraction method and configurations checked.
