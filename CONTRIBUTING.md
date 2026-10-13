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

1. Add or update the appropriate table in `README.md`:

   ```markdown
   | <a id="owner-repo"></a>[**owner/repo**](https://github.com/owner/repo) | Executes documented Google Ads operations through its verified interface. |
   ```

2. Update the comparison matrix for MCP servers, section counts, and navigation links as applicable.
3. Check the repository links and the internal anchors.
4. Run the checks used before committing:

   ```bash
   npx --yes markdownlint-cli2@latest "**/*.md"
   git diff --check
   ```

5. Open a pull request explaining the change and linking to the evidence.
