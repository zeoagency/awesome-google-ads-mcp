# Awesome Google Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated developer index and technical comparison of Model Context Protocol (MCP) servers and agentic tooling for **[Google Ads](https://ads.google.com/)**.

Official links: [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/first-call/overview) · [Google Cloud Console](https://console.cloud.google.com/) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Ads API Changelog](https://developers.google.com/google-ads/api/docs/release-notes) · [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)

---

## Contents

- [Developer Comparison Matrix (5)](#developer-comparison-matrix)

1. [Query and report with GAQL (2)](#1-query-and-report-with-gaql)
   - [Official DevRel gateways and gRPC SearchStream pipelines (1)](#official-devrel-gateways-and-grpc-searchstream-pipelines)
   - [Edge runtimes and compiled native proxies (1)](#edge-runtimes-and-compiled-native-proxies)
2. [Export, snapshot, and cache performance reports locally (2)](#2-export-snapshot-and-cache-performance-reports-locally)
   - [Local performance snapshotting and analytical caches (1)](#local-performance-snapshotting-and-analytical-caches)
   - [Encrypted action audit logging and safety cache proxies (1)](#encrypted-action-audit-logging-and-safety-cache-proxies)
3. [Automate campaign mutations, budgets, and bid strategies (1)](#3-automate-campaign-mutations-budgets-and-bid-strategies)
   - [Keyword Planner and RLSA audience targeting suites (1)](#keyword-planner-and-rlsa-audience-targeting-suites)

- [Resources](#resources)
- [Reference](#reference)

---

## Developer Comparison Matrix

*5 projects. Side-by-side technical capability comparison across runtime, wire transport, API architecture, streaming, and mutation safety. Project names link internally to detailed listings below.*

Indicator Legend:

- **Transport:** `stdio` (local subprocess) vs `HTTP` (Streamable HTTP / remote microservice)
- **Client Type:** `REST` (lightweight direct HTTP calls) vs `SDK` (official Google Ads SDK with protobuf stubs)
- **SearchStream:** `✅ gRPC` (high-throughput gRPC streaming) vs `❌` (paged search)
- **Mutations:** `✏️ Live` (direct account modification) · `🛡️ Dry-Run` (`validate_only` dry-run preflight) · `👁️ Read-Only` (reporting queries only)
- **PMax / Shop:** `✅ Full` (Performance Max and Shopping supported) vs `❌` (Search-only)
- **MCC Multi:** `✅ Dynamic` (dynamic `login-customer-id` header switching) vs `❌` (single customer account)
- **Auth Daemon:** `✅ Auto` (proactive 60-min token refresh loop) vs `❌` (manual refresh)

| Project | Stars | Runtime | Transport | Client Type | SearchStream | Mutations | PMax / Shop | MCC Multi | Auth Daemon |
|---|---|---|---|---|---|---|---|---|---|
| [googleads/google-ads-mcp](#googleads-google-ads-mcp) | ⭐ 969 | `Py` | `stdio` | `SDK` | ✅ gRPC | 🛡️ Dry-Run | ✅ Full | ✅ Dynamic | ✅ Auto |
| [kLOsk/adloop](#klosk-adloop) | ⭐ 266 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ✅ Full | ✅ Dynamic | ✅ Auto |
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | ⭐ 52 | `Rust` | `stdio` | `REST` | ✅ gRPC | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | ⭐ 1 | `TS` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [growmedevelopment/google-ads-mcp](#growmedevelopment-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |

---

## 1. Query and report with GAQL

*2 projects. High-throughput SearchStream pipelines and compiled proxies for executing GAQL queries.*

### Official DevRel gateways and gRPC SearchStream pipelines

*1 project. Official Google implementations and high-throughput gRPC streaming servers with full protobuf serialization.*

| Project | What it does |
|---|---|
| <a id="googleads-google-ads-mcp"></a>[**googleads/google-ads-mcp**](https://github.com/googleads/google-ads-mcp) | Official Google DevRel reference server featuring high-throughput gRPC SearchStream pipelines, complete protobuf serialization, and validate_only dry-run safety. Ideal for enterprise production gateways requiring direct alignment with upstream Google Ads API releases. |

### Edge runtimes and compiled native proxies

*1 project. Compiled Rust server designed for low-memory, high-concurrency execution.*

| Project | What it does |
|---|---|
| <a id="fgribreau-mcp-google-ads"></a>[**FGRibreau/mcp-google-ads**](https://github.com/FGRibreau/mcp-google-ads) | Compiled Rust MCP server delivering sub-millisecond execution times and minimal memory footprint (<15MB RSS). Ideal for high-concurrency enterprise microservices executing continuous GAQL search streams. |

---

## 2. Export, snapshot, and cache performance reports locally

*2 projects. Local snapshot caching, offline analytical queries, and two-phase commit mutation safety.*

### Local performance snapshotting and analytical caches

*1 project. TypeScript caching server implementing SQLite persistence for ad performance and search query reports.*

| Project | What it does |
|---|---|
| <a id="mharnett-mcp-google-ads"></a>[**mharnett/mcp-google-ads**](https://github.com/mharnett/mcp-google-ads) | TypeScript caching server with 167 commits implementing SQLite persistence for ad performance and search query reports. Provides reliable offline query tools for local analysis in Claude Desktop. |

### Encrypted action audit logging and safety cache proxies

*1 project. Unified ad operations client with two-phase commit mutation previews and local audit logging.*

| Project | What it does |
|---|---|
| <a id="klosk-adloop"></a>[**kLOsk/adloop**](https://github.com/kLOsk/adloop) | Cross-platform ad operations client with two-phase commit mutation previews. Provides local action audit logging and unified management tools across Google Ads and paid media channels. |

---

## 3. Automate campaign mutations, budgets, and bid strategies

*1 project. PPC keyword and ad group management server.*

### Keyword Planner and RLSA audience targeting suites

*1 project. Specialized tools to audit keyword match types and negative keyword conflicts.*

| Project | What it does |
|---|---|
| <a id="growmedevelopment-google-ads-mcp"></a>[**growmedevelopment/google-ads-mcp**](https://github.com/growmedevelopment/google-ads-mcp) | PPC keyword and ad group management server with 96 commits providing tools to audit keyword match types and negative keyword conflicts. Ideal for automated hygiene audits in Search campaigns. |

---

## Resources

- **[Google Ads API Developer Documentation](https://developers.google.com/google-ads/api/docs/first-call/overview)**: The official manual for REST and gRPC API integration, resource schemas, and service definitions.
- **[Google Ads Query Language (GAQL) Reference](https://developers.google.com/google-ads/api/docs/query/overview)**: The definitive syntax reference for constructing GAQL query strings across resources and metrics.
- **[Model Context Protocol Specification](https://modelcontextprotocol.io/)**: Protocol documentation for JSON-RPC 2.0 messages over stdio, SSE, and Streamable HTTP.
- **[Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials)**: Developer portal for configuring OAuth 2.0 Client IDs, redirect URIs, and Google Ads API scopes.
- **[Google Ads Python SDK GitHub](https://github.com/googleads/google-ads-python)**: Official Google-supported client library featuring gRPC bindings and protobuf stubs.
- **[Google Ads Node.js Client GitHub](https://github.com/googleads/google-ads-nodejs)**: Official TypeScript/Node client library for executing searchStream and mutate queries.

---

## Reference

- **gRPC SearchStream vs. Paged Search:** The Google Ads API provides two distinct query endpoints: `GoogleAdsService.Search` (paged, subject to page-token boundaries and higher round-trip latency) and `GoogleAdsService.SearchStream` (HTTP/2 gRPC streaming, yielding continuous chunks for lower latency and memory overhead). Production gateways should prefer `SearchStream`.
- **Direct REST vs. SDK Footprint:** Official Google Ads SDKs bundle hundreds of megabytes of generated protobuf stubs and gRPC dependencies. Lean REST servers (`FGRibreau/mcp-google-ads`) execute lightweight HTTP calls directly against `https://googleads.googleapis.com`, reducing server footprint from >500MB to <30MB.
- **Dry-Run Mutation Safety:** Writing directly to live advertising accounts introduces risk of catastrophic budget overspend. Servers supporting `validate_only=true` preflight transactions against Google Ads API servers to detect validation errors without modifying live ad campaigns.
- **Proactive Token Refresh Daemons:** Google OAuth access tokens expire after 3,600 seconds (1 hour). Unhandled token expiration causes agent sessions to crash mid-workflow. Production implementations (`googleads`) maintain background refresh daemons that renew tokens proactively.
- **Currency Micros Conversion:** Google Ads represents monetary values as integer micros ($1.00 = 1,000,000 micros). Specialized helpers convert between micros and standard currency to prevent catastrophic budget inflation.
- **Manager Account (MCC) Hierarchy Routing:** Multi-account agency deployments require dynamic routing via the `login-customer-id` HTTP header, allowing an agent to manage hundreds of client accounts under a single authenticated developer token.
