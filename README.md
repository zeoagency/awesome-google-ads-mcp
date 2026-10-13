# Awesome Google Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of Google Ads MCP servers, command-line tools, and SDKs.

Official references: [Google Ads API](https://developers.google.com/google-ads/api/docs/start) · [Client libraries](https://developers.google.com/google-ads/api/docs/client-libs) · [API sunset schedule](https://developers.google.com/google-ads/api/docs/sunset-dates)

## Contents

18 projects, grouped by interface.

- [MCP comparison (7)](#mcp-comparison)
- [MCP servers (7)](#mcp-servers)
- [Command-line tools (4)](#command-line-tools)
- [SDKs and client libraries (7)](#sdks-and-client-libraries)
  - [Official libraries (6)](#official-libraries)
  - [Community libraries (1)](#community-libraries)
- [Contributing](CONTRIBUTING.md)

## MCP comparison

7 servers. Compare the shipped MCP transport and implemented Google Ads read/write operations.

| Project | Runtime | MCP transport | Google Ads access | API client |
|---|---|---|---|---|
| [googleads/google-ads-mcp](#googleads-google-ads-mcp) | Python | stdio, Streamable HTTP | Read | Official Python client |
| [growmedevelopment/google-ads-mcp](#growmedevelopment-google-ads-mcp) | Python | stdio, Streamable HTTP | Read | Official Python client |
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | Rust | stdio | Read and write | Direct REST |
| [kLOsk/adloop](#klosk-adloop) | Python | stdio | Read and write | Official Python client |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | TypeScript / Node.js | stdio | Read; writes opt-in | Community Node.js client |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | Python | stdio | Read; writes opt-in | Official Python client |
| [cesteral/mcp-open-advertising](#cesteral-mcp-open-advertising) | TypeScript / Node.js | stdio, Streamable HTTP | Read and write | Direct REST |

Source and setup documentation checked on 2026-10-13; authenticated Google Ads operations were not tested. Read/write describes implemented operations, not complete coverage of every campaign type.

## MCP servers

7 projects. Expose Google Ads queries or account operations to MCP clients.

| Project | What it does |
|---|---|
| <a id="googleads-google-ads-mcp"></a>[**googleads/google-ads-mcp**](https://github.com/googleads/google-ads-mcp) | Queries Google Ads accounts with Google's official read-only MCP server, using GAQL, resource metadata, and account discovery. Uses the Python client library's SearchStream method for reporting. |
| <a id="growmedevelopment-google-ads-mcp"></a>[**growmedevelopment/google-ads-mcp**](https://github.com/growmedevelopment/google-ads-mcp) | Extends Google's read-only MCP server with manager-account client discovery and Keyword Planner keyword ideas. Adds batching and retries to keyword planning requests. |
| <a id="fgribreau-mcp-google-ads"></a>[**FGRibreau/mcp-google-ads**](https://github.com/FGRibreau/mcp-google-ads) | Queries and modifies Google Ads resources through a Rust MCP server using REST. Provides local mutation previews, confirmation, budget guards, and audit logs; previews do not perform Google Ads API validation. |
| <a id="klosk-adloop"></a>[**kLOsk/adloop**](https://github.com/kLOsk/adloop) | Queries and manages Google Ads campaigns, keywords, and assets within a multi-platform MCP server. Provides draft-and-confirm workflows, Google Ads `validate_only` preflight, and local JSONL audit logs. |
| <a id="mharnett-mcp-google-ads"></a>[**mharnett/mcp-google-ads**](https://github.com/mharnett/mcp-google-ads) | Queries Google Ads performance and exposes campaign, keyword, asset, and experiment operations through a TypeScript MCP server. Enables mutating tools only when `GOOGLE_ADS_MCP_WRITE=true`. |
| <a id="epave-google-ads-mcp"></a>[**epave/google-ads-mcp**](https://github.com/epave/google-ads-mcp) | Queries and manages Google Ads campaigns, keywords, and assets through a Python MCP server. Keeps writes disabled by default and provides confirmation-token previews and a local DuckDB audit store. |
| <a id="cesteral-mcp-open-advertising"></a>[**cesteral/mcp-open-advertising**](https://github.com/cesteral/mcp-open-advertising/tree/main/packages/gads-mcp) | Exposes Google Ads GAQL queries and resource mutations through the repository's separate `gads-mcp` package. Calls the Google Ads REST API and supports local stdio and remote Streamable HTTP. |

## Command-line tools

4 projects. Run Google Ads queries, exports, or account operations from a terminal.

| Project | What it does |
|---|---|
| <a id="google-ads-api-report-fetcher"></a>[**google/ads-api-report-fetcher**](https://github.com/google/ads-api-report-fetcher) | Executes GAQL report files across Google Ads accounts and exports results to CSV, JSON, BigQuery, or Sheets using Python and Node.js CLIs. Lives in Google's GitHub organization but is not an officially supported Google product. |
| <a id="getyourguide-gaql-cli"></a>[**getyourguide/gaql-cli**](https://github.com/getyourguide/gaql-cli) | Runs Google Ads queries from a terminal command or interactive REPL with field completion. Exports CSV, JSON, JSONL, and protobuf results and supports manager-account discovery. |
| <a id="bin-huang-google-ads-open-cli"></a>[**Bin-Huang/google-ads-open-cli**](https://github.com/Bin-Huang/google-ads-open-cli) | Runs read-only GAQL queries and inspects Google Ads campaign, keyword, conversion, and manager-account data from the terminal. Uses direct REST requests. |
| <a id="icoolqin-google-ads-cli"></a>[**icoolqin/google-ads-cli**](https://github.com/icoolqin/google-ads-cli) | Queries Google Ads accounts and manages campaigns, budgets, and assets through a Python CLI. Defaults mutations to local plans and offers separate API validation and execution modes. |

## SDKs and client libraries

7 projects. Integrate the Google Ads API into applications using supported or community client libraries.

### Official libraries

6 projects. Google supports these libraries in its [client library directory](https://developers.google.com/google-ads/api/docs/client-libs).

| Project | What it does |
|---|---|
| <a id="googleads-google-ads-python"></a>[**googleads/google-ads-python**](https://github.com/googleads/google-ads-python) | Calls the Google Ads API from Python with authentication helpers, protobuf requests, reporting, and mutation services. Includes runnable examples. |
| <a id="googleads-google-ads-java"></a>[**googleads/google-ads-java**](https://github.com/googleads/google-ads-java) | Calls the Google Ads API from Java through typed service clients for reporting and mutations. Includes configuration helpers and examples. |
| <a id="googleads-google-ads-dotnet"></a>[**googleads/google-ads-dotnet**](https://github.com/googleads/google-ads-dotnet) | Calls the Google Ads API from .NET through typed service clients for reporting and mutations. Includes configuration helpers and examples. |
| <a id="googleads-google-ads-php"></a>[**googleads/google-ads-php**](https://github.com/googleads/google-ads-php) | Calls the Google Ads API from PHP through service clients for reporting and mutations. Includes authentication and configuration helpers and examples. |
| <a id="googleads-google-ads-ruby"></a>[**googleads/google-ads-ruby**](https://github.com/googleads/google-ads-ruby) | Calls the Google Ads API from Ruby through service clients for reporting and mutations. Includes configuration helpers and examples. |
| <a id="googleads-google-ads-perl"></a>[**googleads/google-ads-perl**](https://github.com/googleads/google-ads-perl) | Calls the Google Ads API from Perl through service clients for reporting and mutations. Includes authentication and configuration helpers and examples. |

### Community libraries

1 project. Provides a community-maintained Node.js client, listed separately from Google's supported libraries.

| Project | What it does |
|---|---|
| <a id="opteo-google-ads-api"></a>[**Opteo/google-ads-api**](https://github.com/Opteo/google-ads-api) | Queries and mutates Google Ads accounts from Node.js with TypeScript resource and service definitions. Provides GAQL helpers and streaming through a community-maintained client listed in Google's documentation. |
