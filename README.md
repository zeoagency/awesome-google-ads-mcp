# Awesome Google Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated developer index and technical comparison of Model Context Protocol (MCP) servers and agentic tooling for **[Google Ads](https://ads.google.com/)**.

Official links: [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/first-call/overview) · [Google Cloud Console](https://console.cloud.google.com/) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Ads API Changelog](https://developers.google.com/google-ads/api/docs/release-notes) · [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)

---

## Contents

- [Developer Comparison Matrix (44)](#developer-comparison-matrix)

1. [Query and report with GAQL (8)](#1-query-and-report-with-gaql)
   - [Official DevRel gateways and gRPC SearchStream pipelines (2)](#official-devrel-gateways-and-grpc-searchstream-pipelines)
   - [Dynamic schema reflection and field discovery (1)](#dynamic-schema-reflection-and-field-discovery)
   - [Zero-SDK lean REST and minimal GAQL execution (3)](#zero-sdk-lean-rest-and-minimal-gaql-execution)
   - [Edge runtimes and compiled native proxies (2)](#edge-runtimes-and-compiled-native-proxies)
2. [Export, snapshot, and cache performance reports locally (5)](#2-export-snapshot-and-cache-performance-reports-locally)
   - [Local performance snapshotting and analytical caches (3)](#local-performance-snapshotting-and-analytical-caches)
   - [Encrypted action audit logging and safety cache proxies (2)](#encrypted-action-audit-logging-and-safety-cache-proxies)
3. [Automate campaign mutations, budgets, and bid strategies (12)](#3-automate-campaign-mutations-budgets-and-bid-strategies)
   - [Direct campaign mutation and bid/budget setters (3)](#direct-campaign-mutation-and-bidbudget-setters)
   - [Validated campaign CRUD with dry-run mutation guards (6)](#validated-campaign-crud-with-dry-run-mutation-guards)
   - [Keyword Planner and RLSA audience targeting suites (3)](#keyword-planner-and-rlsa-audience-targeting-suites)
4. [Enforce mutation safety guardrails, budget caps, and approval workflows (2)](#4-enforce-mutation-safety-guardrails-budget-caps-and-approval-workflows)
   - [Daily spend limit guardrails and budget caps (1)](#daily-spend-limit-guardrails-and-budget-caps)
   - [Client-specific approval workflows and human review prompts (1)](#client-specific-approval-workflows-and-human-review-prompts)
5. [Manage agency access and multi-account MCC hierarchies (9)](#5-manage-agency-access-and-multi-account-mcc-hierarchies)
   - [Dynamic MCC switching via login-customer-id routing (3)](#dynamic-mcc-switching-via-login-customer-id-routing)
   - [Proactive 60-minute OAuth token refresh daemons (3)](#proactive-60-minute-oauth-token-refresh-daemons)
   - [Multi-tenant credential vaults and agency proxies (3)](#multi-tenant-credential-vaults-and-agency-proxies)
6. [Analyze performance with domain playbooks and heuristics (3)](#6-analyze-performance-with-domain-playbooks-and-heuristics)
   - [Expert AdTech reasoning engines and conversion lag discounting (1)](#expert-adtech-reasoning-engines-and-conversion-lag-discounting)
   - [Impression share lost-to-budget and micros currency models (2)](#impression-share-lost-to-budget-and-micros-currency-models)
7. [Integrate agentic workflows and multi-platform marketing stacks (5)](#7-integrate-agentic-workflows-and-multi-platform-marketing-stacks)
   - [Autonomous Claude Code marketing skills and CLI copilots (3)](#autonomous-claude-code-marketing-skills-and-cli-copilots)
   - [Google Ads reporting proxies with ecommerce attribution (2)](#google-ads-reporting-proxies-with-ecommerce-attribution)

- [Resources](#resources)
- [Reference](#reference)

---

## Developer Comparison Matrix

*44 projects. Side-by-side technical capability comparison across runtime, wire transport, API architecture, streaming, and mutation safety. Project names link internally to detailed listings below.*

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
| [nowork-studio/notfair-plugin](#nowork-studio-notfair-plugin) | ⭐ 3,840 | `TS` | `HTTP` | `SDK` | ❌ | ✏️ Live | ✅ Full | ✅ Dynamic | ✅ Auto |
| [googleads/google-ads-mcp](#googleads-google-ads-mcp) | ⭐ 969 | `Py` | `stdio` | `SDK` | ✅ gRPC | 🛡️ Dry-Run | ✅ Full | ✅ Dynamic | ✅ Auto |
| [cohnen/mcp-google-ads](#cohnen-mcp-google-ads) | ⭐ 710 | `Py` | `stdio` | `REST` | ❌ | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [kLOsk/adloop](#klosk-adloop) | ⭐ 266 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ✅ Full | ✅ Dynamic | ✅ Auto |
| [TheMattBerman/google-ads-copilot](#themattberman-google-ads-copilot) | ⭐ 235 | `Shell` | `stdio` | `REST` | ❌ | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [thatrebeccarae/claude-marketing](#thatrebeccarae-claude-marketing) | ⭐ 147 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [gomarble-ai/google-ads-mcp-server](#gomarble-ai-google-ads-mcp-server) | ⭐ 144 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ✅ Full | ✅ Dynamic | ✅ Auto |
| [mathiaschu/google-ads-analyzer](#mathiaschu-google-ads-analyzer) | ⭐ 67 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ✅ Full | ❌ | ❌ |
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | ⭐ 52 | `Rust` | `stdio` | `REST` | ✅ gRPC | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [TrueClicks/google-ads-mcp-js](#trueclicks-google-ads-mcp-js) | ⭐ 50 | `JS` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [grantweston/google-ads-mcp-complete](#grantweston-google-ads-mcp-complete) | ⭐ 25 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ✅ Full | ✅ Dynamic | ❌ |
| [promobase/google-ads-mcp](#promobase-google-ads-mcp) | ⭐ 22 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ✅ Dynamic | ❌ |
| [johnoconnor0/google-ads-mcp](#johnoconnor0-google-ads-mcp) | ⭐ 16 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ✅ Auto |
| [davidmosiah/google-ads-mcp-unofficial](#davidmosiah-google-ads-mcp-unofficial) | ⭐ 4 | `TS` | `stdio` | `REST` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [akelaonline/MCP-Google-Ads](#akelaonline-mcp-google-ads) | ⭐ 4 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [itallstartedwithaidea/google-ads-mcp](#itallstartedwithaidea-google-ads-mcp) | ⭐ 3 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [minholi/google-ads-mcp](#minholi-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `REST` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | ⭐ 1 | `TS` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [LucasSantana-Dev/google-ads-mcp](#lucassantana-dev-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [ameydabhade/google-ads-mcp](#ameydabhade-google-ads-mcp) | ⭐ 1 | `TS` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [konradbachowski/google-ads-mcp](#konradbachowski-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [growmedevelopment/google-ads-mcp](#growmedevelopment-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [ball2jh/google-ads-mcp](#ball2jh-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [monsieurgoodmood/google-ads-mcp-plus](#monsieurgoodmood-google-ads-mcp-plus) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [dhawalshah/google-ads-mcp](#dhawalshah-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ❌ |
| [BrandonMiller18/google-ads-mcp](#brandonmiller18-google-ads-mcp) | ⭐ 1 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [BinarCode/google-ads-mcp-http](#binarcode-google-ads-mcp-http) | ⭐ 0 | `Py` | `HTTP` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ❌ |
| [AfzalAliSolangi/GoogleAds-MCP-Server](#afzalalisolangi-googleads-mcp-server) | ⭐ 0 | `TS` | `stdio` | `REST` | ✅ gRPC | 👁️ Read-Only | ✅ Full | ✅ Dynamic | ❌ |
| [cristiandrei1234/google-ads-mcp](#cristiandrei1234-google-ads-mcp) | ⭐ 0 | `TS` | `stdio` | `REST` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [atlasbarinc/google-ads-mcp](#atlasbarinc-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [rgellis/google-ads-mcp](#rgellis-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [abdulrhmanalhur/google-ads-MCP](#abdulrhmanalhur-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [matheusslg/google-ads-mcp](#matheusslg-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ❌ | ❌ | ❌ |
| [Codyp10/Google-Ads-MCP](#codyp10-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ✅ Full | ❌ | ❌ |
| [locomotive-agency/google-ads-mcp](#locomotive-agency-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ❌ |
| [noordevtech/GoogleAds-mcp](#noordevtech-googleads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | ✏️ Live | ✅ Full | ✅ Dynamic | ✅ Auto |
| [ConnorCallison/google-ads-mcp](#connorcallison-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ❌ |
| [connorstearns/mcp-google-ads](#connorstearns-mcp-google-ads) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ✅ Auto |
| [abhibavishi/google-ads-mcp](#abhibavishi-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ❌ |
| [shivpanks19/mcp-google-ads](#shivpanks19-mcp-google-ads) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ✅ Dynamic | ❌ |
| [alexeykozyavkin/google-ads-mcp](#alexeykozyavkin-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [huzaifa-hb/Google-Ads-MCP](#huzaifa-hb-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |
| [mailmanar/google-ads-mcp](#mailmanar-google-ads-mcp) | ⭐ 0 | `Py` | `stdio` | `SDK` | ❌ | 👁️ Read-Only | ❌ | ❌ | ❌ |

---

## 1. Query and report with GAQL

*8 projects. High-throughput SearchStream pipelines, dynamic schema reflection, and lightweight proxies for executing GAQL queries.*

### Official DevRel gateways and gRPC SearchStream pipelines

*2 projects. Official Google implementations and high-throughput gRPC streaming servers with full protobuf serialization.*

| Project | What it does |
|---|---|
| <a id="googleads-google-ads-mcp"></a>[**googleads/google-ads-mcp**](https://github.com/googleads/google-ads-mcp) | Official Google DevRel reference server featuring high-throughput gRPC SearchStream pipelines, complete protobuf serialization, and validate_only dry-run safety. Ideal for enterprise production gateways requiring direct alignment with upstream Google Ads API releases. |
| <a id="binarcode-google-ads-mcp-http"></a>[**BinarCode/google-ads-mcp-http**](https://github.com/BinarCode/google-ads-mcp-http) | Standalone HTTP and Streamable HTTP transport bridge for Google Ads MCP, built for containerized architectures and remote agents. Eliminates local stdio subprocess deadlocks when orchestrating pipelines in serverless or cloud environments. |

### Dynamic schema reflection and field discovery

*1 project. Minimalist reflection servers querying GoogleAdsFieldService at runtime to eliminate schema drift and token bloat.*

| Project | What it does |
|---|---|
| <a id="davidmosiah-google-ads-mcp-unofficial"></a>[**davidmosiah/google-ads-mcp-unofficial**](https://github.com/davidmosiah/google-ads-mcp-unofficial) | TypeScript reflection wrapper offering dynamic metadata inspection and consolidated reporting across active campaign entities. Designed for Cursor and Claude Desktop developers wanting zero-dependency Node installation. |

### Zero-SDK lean REST and minimal GAQL execution

*3 projects. Lightweight proxies bypassing heavy SDK binaries in favor of direct HTTP calls, raw JSON, and compact GAQL responses.*

| Project | What it does |
|---|---|
| <a id="cohnen-mcp-google-ads"></a>[**cohnen/mcp-google-ads**](https://github.com/cohnen/mcp-google-ads) | Community flagship with 710+ stars that completely bypasses the 500MB Python SDK in favor of direct requests.post REST calls. Serves official GAQL syntax references via gaql:// MCP resources for in-context query synthesis. |
| <a id="afzalalisolangi-googleads-mcp-server"></a>[**AfzalAliSolangi/GoogleAds-MCP-Server**](https://github.com/AfzalAliSolangi/GoogleAds-MCP-Server) | TypeScript MCP server optimized for Cloudflare Workers and edge execution with strict read-only guarantees. Implements streaming response parsing and web-standard OAuth token forwarding for serverless agents. |
| <a id="minholi-google-ads-mcp"></a>[**minholi/google-ads-mcp**](https://github.com/minholi/google-ads-mcp) | Compact Python proxy focusing on campaign-level KPI extraction and automated daily budget reporting. Returns sanitized Markdown summary tables directly formatted for LLM executive summaries. |

### Edge runtimes and compiled native proxies

*2 projects. Compiled Rust and high-performance TypeScript servers designed for serverless, low-memory, and edge execution.*

| Project | What it does |
|---|---|
| <a id="fgribreau-mcp-google-ads"></a>[**FGRibreau/mcp-google-ads**](https://github.com/FGRibreau/mcp-google-ads) | Compiled Rust MCP server delivering sub-millisecond execution times and minimal memory footprint (<15MB RSS). Ideal for high-concurrency enterprise microservices executing continuous GAQL search streams. |
| <a id="cristiandrei1234-google-ads-mcp"></a>[**cristiandrei1234/google-ads-mcp**](https://github.com/cristiandrei1234/google-ads-mcp) | TypeScript server wrapping core reporting services with structured zod validation schemas. Offers reliable reporting for campaigns, ad groups, and keyword performance in Node-based agent stacks. |

---

## 2. Export, snapshot, and cache performance reports locally

*5 projects. Local snapshot caching, CSV/JSON analytical exports, and encrypted audit logging without upstream API rate limit pressure.*

### Local performance snapshotting and analytical caches

*3 projects. Cached snapshot proxies enabling offline analytical queries and historical performance reporting without API rate limits.*

| Project | What it does |
|---|---|
| <a id="atlasbarinc-google-ads-mcp"></a>[**atlasbarinc/google-ads-mcp**](https://github.com/atlasbarinc/google-ads-mcp) | Local analytical cache server designed for financial audit pipelines and historical metric comparison. Stores campaign snapshots on disk to support longitudinal performance reviews without hitting rate limits. |
| <a id="mharnett-mcp-google-ads"></a>[**mharnett/mcp-google-ads**](https://github.com/mharnett/mcp-google-ads) | TypeScript caching server with 167 commits implementing SQLite persistence for ad performance and search query reports. Provides reliable offline query tools for local analysis in Claude Desktop. |
| <a id="lucassantana-dev-google-ads-mcp"></a>[**LucasSantana-Dev/google-ads-mcp**](https://github.com/LucasSantana-Dev/google-ads-mcp) | Python reporting and caching implementation with built-in export utilities for tabular CSV and JSON analytics. Supports offline data exploration for PPC media buyers triaging underperforming keywords. |

### Encrypted action audit logging and safety cache proxies

*2 projects. Servers maintaining local transactional audit trails and safety queues for review before live execution.*

| Project | What it does |
|---|---|
| <a id="klosk-adloop"></a>[**kLOsk/adloop**](https://github.com/kLOsk/adloop) | Cross-platform ad operations client with two-phase commit mutation previews. Provides local action audit logging and unified management tools across Google Ads and paid media channels. |
| <a id="akelaonline-mcp-google-ads"></a>[**akelaonline/MCP-Google-Ads**](https://github.com/akelaonline/MCP-Google-Ads) | Python Google Ads server featuring encrypted local action logging and pending mutation confirmation queues. Provides structured reporting and Google Merchant Center product diagnostics. |

---

## 3. Automate campaign mutations, budgets, and bid strategies

*12 projects. Tools capable of modifying live accounts—adjusting budgets, pausing ad groups, creating campaigns, and syncing keyword lists.*

### Direct campaign mutation and bid/budget setters

*3 projects. Servers providing write endpoints for modifying campaign budgets, pausing ad groups, and adjusting bid amounts.*

| Project | What it does |
|---|---|
| <a id="grantweston-google-ads-mcp-complete"></a>[**grantweston/google-ads-mcp-complete**](https://github.com/grantweston/google-ads-mcp-complete) | Comprehensive multi-service wrapper exposing CampaignService, AdGroupService, and AdGroupCriterionService mutation tools. Built for automated bid adjustments, ad schedule updates, and negative keyword list synchronization. |
| <a id="promobase-google-ads-mcp"></a>[**promobase/google-ads-mcp**](https://github.com/promobase/google-ads-mcp) | Agency-focused mutation proxy allowing agents to update promotional budgets, toggle seasonal ad groups, and pause ad spend. Incorporates account ID validation to prevent cross-client budget pollution. |
| <a id="itallstartedwithaidea-google-ads-mcp"></a>[**itallstartedwithaidea/google-ads-mcp**](https://github.com/itallstartedwithaidea/google-ads-mcp) | Extensive 29-tool Google Ads management server exposing campaign, ad group, keyword, and budget mutation endpoints alongside raw GAQL execution tools. |

### Validated campaign CRUD with dry-run mutation guards

*6 projects. Mutation suites enforcing validate_only dry-run preflights, currency checks, and campaign deployment tools.*

| Project | What it does |
|---|---|
| <a id="epave-google-ads-mcp"></a>[**epave/google-ads-mcp**](https://github.com/epave/google-ads-mcp) | Safety-first campaign CRUD server enforcing validate_only dry-run preflights on all mutate operations. Prevents invalid budget increments and malformed ad structures from throwing unrecoverable API errors. |
| <a id="rgellis-google-ads-mcp"></a>[**rgellis/google-ads-mcp**](https://github.com/rgellis/google-ads-mcp) | Python mutation suite with 166 commits implementing transactional checks and rollback safeguards for campaign bid adjustments. Built to support robust agentic self-healing workflows. |
| <a id="abdulrhmanalhur-google-ads-mcp"></a>[**abdulrhmanalhur/google-ads-MCP**](https://github.com/abdulrhmanalhur/google-ads-MCP) | Validated campaign management server checking currency micros conversions and bid limits before issuing Google Ads API calls. Protects against LLM decimal slips that could overspend budget. |
| <a id="matheusslg-google-ads-mcp"></a>[**matheusslg/google-ads-mcp**](https://github.com/matheusslg/google-ads-mcp) | Python server featuring atomic mutate handlers for updating campaign statuses and target ROAS settings. Includes pre-commit validation to ensure campaign budget IDs match target campaigns. |
| <a id="codyp10-google-ads-mcp"></a>[**Codyp10/Google-Ads-MCP**](https://github.com/Codyp10/Google-Ads-MCP) | Python campaign mutation and creation server providing specialized tools for deploying Performance Max (PMax) campaigns, Responsive Search Ads (RSA), and negative keyword lists. |
| <a id="ameydabhade-google-ads-mcp"></a>[**ameydabhade/google-ads-mcp**](https://github.com/ameydabhade/google-ads-mcp) | TypeScript MCP server with zod schema validation providing campaign performance reporting and status toggling for Node-based agent stacks. |

### Keyword Planner and RLSA audience targeting suites

*3 projects. Specialized keyword generation, negative keyword list management, and audience targeting automation tools.*

| Project | What it does |
|---|---|
| <a id="konradbachowski-google-ads-mcp"></a>[**konradbachowski/google-ads-mcp**](https://github.com/konradbachowski/google-ads-mcp) | Specialized Keyword Planner MCP server exposing fine-grained tools for keyword generation, search volume forecasting, and RLSA audience targeting. Enables agents to discover high-intent keyword targets and forecast monthly spend. |
| <a id="growmedevelopment-google-ads-mcp"></a>[**growmedevelopment/google-ads-mcp**](https://github.com/growmedevelopment/google-ads-mcp) | PPC keyword and ad group management server with 96 commits providing tools to audit keyword match types and negative keyword conflicts. Ideal for automated hygiene audits in Search campaigns. |
| <a id="ball2jh-google-ads-mcp"></a>[**ball2jh/google-ads-mcp**](https://github.com/ball2jh/google-ads-mcp) | Keyword and campaign management toolkit designed to sync negative keyword lists across multiple Search ad groups. Prevents cross-campaign cannibalization through automated list application. |

---

## 4. Enforce mutation safety guardrails, budget caps, and approval workflows

*2 projects. Pre-commit budget thresholds, percentage increase limits, and human approval prompts to prevent accidental overspend.*

### Daily spend limit guardrails and budget caps

*1 project. Safety layers introducing daily budget caps and confirmation prompts to protect against unintended spending spikes.*

| Project | What it does |
|---|---|
| <a id="monsieurgoodmood-google-ads-mcp-plus"></a>[**monsieurgoodmood/google-ads-mcp-plus**](https://github.com/monsieurgoodmood/google-ads-mcp-plus) | Python mutation guardrail server enforcing daily spend confirmation thresholds before executing budget modifications. |

### Client-specific approval workflows and human review prompts

*1 project. Agency guardrail proxies enforcing review checkpoints whenever proposed budget changes exceed predefined limits.*

| Project | What it does |
|---|---|
| <a id="locomotive-agency-google-ads-mcp"></a>[**locomotive-agency/google-ads-mcp**](https://github.com/locomotive-agency/google-ads-mcp) | Agency reporting server with 14 commits enforcing client-specific approval prompts and read-only account performance inspection. |

---

## 5. Manage agency access and multi-account MCC hierarchies

*9 projects. Manager Account (MCC) hierarchies, multi-client routing, 60-minute OAuth token refresh daemons, and credential vaults.*

### Dynamic MCC switching via login-customer-id routing

*3 projects. Servers enabling agency operators to seamlessly switch between hundreds of client accounts by injecting login-customer-id headers.*

| Project | What it does |
|---|---|
| <a id="noordevtech-googleads-mcp"></a>[**noordevtech/GoogleAds-mcp**](https://github.com/noordevtech/GoogleAds-mcp) | High-scoring agency gateway (B+ / 76.8%) offering seamless MCC multi-account switching via dynamic login_customer_id header routing. Enables agents to inspect account hierarchies and execute queries across hundreds of child accounts in a single session. |
| <a id="trueclicks-google-ads-mcp-js"></a>[**TrueClicks/google-ads-mcp-js**](https://github.com/TrueClicks/google-ads-mcp-js) | JavaScript MCP implementation from the TrueClicks PPC audit platform providing MCC account tree discovery and agency-wide quality scoring. Integrates proprietary account audit heuristics with standard Google Ads reporting. |
| <a id="connorcallison-google-ads-mcp"></a>[**ConnorCallison/google-ads-mcp**](https://github.com/ConnorCallison/google-ads-mcp) | Python MCC routing proxy providing account enumeration and automated cross-client performance benchmarking. Formats agency roll-up reports with clear customer ID attribution. |

### Proactive 60-minute OAuth token refresh daemons

*3 projects. Implementations that prevent the standard 3,600s Google OAuth session drop by running proactive background refresh loops.*

| Project | What it does |
|---|---|
| <a id="gomarble-ai-google-ads-mcp-server"></a>[**gomarble-ai/google-ads-mcp-server**](https://github.com/gomarble-ai/google-ads-mcp-server) | Enterprise-grade server (⭐ 144) solving the 60-minute Google OAuth session drop with a proactive background token refresh daemon. Critical for long-running autonomous workflows that span multiple hours of batch reporting. |
| <a id="connorstearns-mcp-google-ads"></a>[**connorstearns/mcp-google-ads**](https://github.com/connorstearns/mcp-google-ads) | Python server featuring 87 commits with persistent OAuth token storage and automated refresh handling across development sessions. Eliminates repeated browser re-authentication during daily agent coding. |
| <a id="johnoconnor0-google-ads-mcp"></a>[**johnoconnor0/google-ads-mcp**](https://github.com/johnoconnor0/google-ads-mcp) | Python implementation with 29 commits wrapping Google OAuth2 token lifecycle management with encrypted credential storage. Ensures secure credential caching for desktop agents. |

### Multi-tenant credential vaults and agency proxies

*3 projects. Secure multi-client credential isolation and agency gateway proxies designed for enterprise PPC operations.*

| Project | What it does |
|---|---|
| <a id="dhawalshah-google-ads-mcp"></a>[**dhawalshah/google-ads-mcp**](https://github.com/dhawalshah/google-ads-mcp) | Multi-tenant credential isolation server supporting distinct customer OAuth configurations stored securely in environment namespaces. Prevents accidental cross-tenant data leakage in agency environments. |
| <a id="abhibavishi-google-ads-mcp"></a>[**abhibavishi/google-ads-mcp**](https://github.com/abhibavishi/google-ads-mcp) | Python agency gateway with 41 commits providing client account isolation and structured metric reporting. Includes safety checks to ensure queries target valid customer IDs. |
| <a id="shivpanks19-mcp-google-ads"></a>[**shivpanks19/mcp-google-ads**](https://github.com/shivpanks19/mcp-google-ads) | Python proxy supporting dynamic credential switching across multiple Google Cloud project client IDs. Suitable for consultancy teams managing disparate client infrastructure. |

---

## 6. Analyze performance with domain playbooks and heuristics

*3 projects. AdTech domain reasoning engines enforcing conversion lag discounting, lost impression share attribution, and currency micros math.*

### Expert AdTech reasoning engines and conversion lag discounting

*1 project. Cognitive analytical engines embedding domain playbooks for 7-day conversion lag discounting and Bid-to-Position heuristics.*

| Project | What it does |
|---|---|
| <a id="mathiaschu-google-ads-analyzer"></a>[**mathiaschu/google-ads-analyzer**](https://github.com/mathiaschu/google-ads-analyzer) | Cognitive reasoning engine embodying 12 expert PPC domain playbooks. Programmatically discounts conversion metrics using 7-day conversion lag curves and applies Bid-to-Position heuristics before recommending budget changes. |

### Impression share lost-to-budget and micros currency models

*2 projects. Specialized math helpers converting between raw micros ($1 = 1,000,000) and auditing Lost IS (budget) versus Lost IS (rank).*

| Project | What it does |
|---|---|
| <a id="brandonmiller18-google-ads-mcp"></a>[**BrandonMiller18/google-ads-mcp**](https://github.com/BrandonMiller18/google-ads-mcp) | Specialized analytics server calculating impression share lost to budget versus rank, converting currency micros to standard units ($1 = 1,000,000 micros). Protects agents from misinterpreting raw AdTech integers. |
| <a id="alexeykozyavkin-google-ads-mcp"></a>[**alexeykozyavkin/google-ads-mcp**](https://github.com/alexeykozyavkin/google-ads-mcp) | Performance audit server providing automated calculation of click-through rate (CTR) anomalies and cost-per-click (CPC) trends across Search campaigns. Delivers clean tabular outputs for agent consumption. |

---

## 7. Integrate agentic workflows and multi-platform marketing stacks

*5 projects. Autonomous Claude Code marketing skills, terminal copilot harnesses, and campaign proxies with ecommerce conversion tracking.*

### Autonomous Claude Code marketing skills and CLI copilots

*3 projects. Ready-to-run Claude Code agent skills and terminal harnesses that execute ad audits and copy generation directly in CLI.*

| Project | What it does |
|---|---|
| <a id="nowork-studio-notfair-plugin"></a>[**nowork-studio/notfair-plugin**](https://github.com/nowork-studio/notfair-plugin) | Benchmark-topping multi-channel agent skills suite (⭐ 3,840) containing 48 terminal skills across SEO, GEO, social media, and Google Ads management. Provides comprehensive CLI automation routines for Claude Code workflows. |
| <a id="thatrebeccarae-claude-marketing"></a>[**thatrebeccarae/claude-marketing**](https://github.com/thatrebeccarae/claude-marketing) | Popular Claude Code skill collection (⭐ 147) integrating Google Ads audit routines directly into terminal-native agent workflows. Features pre-engineered prompts and scripts for analyzing Search campaign performance. |
| <a id="themattberman-google-ads-copilot"></a>[**TheMattBerman/google-ads-copilot**](https://github.com/TheMattBerman/google-ads-copilot) | High-profile copilot repository (⭐ 235) orchestrating Docker containers and agentic scripts to monitor live ad accounts. Generates proactive Telegram and terminal alerts when budget pacing deviates from target thresholds. |

### Google Ads reporting proxies with ecommerce attribution

*2 projects. Campaign reporting proxies connecting Google Ads performance data with store telemetry and daily pacing alerts.*

| Project | What it does |
|---|---|
| <a id="huzaifa-hb-google-ads-mcp"></a>[**huzaifa-hb/Google-Ads-MCP**](https://github.com/huzaifa-hb/Google-Ads-MCP) | Python Google Ads server with 63 commits providing GAQL query execution and campaign telemetry extraction for ecommerce store performance monitoring. |
| <a id="mailmanar-google-ads-mcp"></a>[**mailmanar/google-ads-mcp**](https://github.com/mailmanar/google-ads-mcp) | Python reporting server with 66 commits providing daily pacing alerts and spend monitoring across Google Ads campaign hierarchies. |

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
- **Direct REST vs. SDK Footprint:** Official Google Ads SDKs bundle hundreds of megabytes of generated protobuf stubs and gRPC dependencies. Lean REST servers (`cohnen/mcp-google-ads`, `FGRibreau/mcp-google-ads`) execute lightweight HTTP calls directly against `https://googleads.googleapis.com`, reducing server footprint from >500MB to <30MB.
- **Dry-Run Mutation Safety:** Writing directly to live advertising accounts introduces risk of catastrophic budget overspend. Servers supporting `validate_only=true` preflight transactions against Google Ads API servers to detect validation errors without modifying live ad campaigns.
- **Proactive Token Refresh Daemons:** Google OAuth access tokens expire after 3,600 seconds (1 hour). Unhandled token expiration causes agent sessions to crash mid-workflow. Production implementations (`gomarble-ai`, `googleads`) maintain background refresh daemons that renew tokens proactively.
- **Currency Micros Conversion:** Google Ads represents monetary values as integer micros ($1.00 = 1,000,000 micros). Specialized helpers convert between micros and standard currency to prevent catastrophic budget inflation.
- **Manager Account (MCC) Hierarchy Routing:** Multi-account agency deployments require dynamic routing via the `login-customer-id` HTTP header, allowing an agent to manage hundreds of client accounts under a single authenticated developer token.
