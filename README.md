# Awesome Google Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated developer index and technical comparison of Model Context Protocol (MCP) servers and agentic tooling for **[Google Ads](https://ads.google.com/)**.

Official links: [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/first-call/overview) · [Google Cloud Console](https://console.cloud.google.com/) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Ads API Changelog](https://developers.google.com/google-ads/api/docs/release-notes) · [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)

---

## Contents

1. [Query and report with GAQL (13)](#1-query-and-report-with-gaql)
   - [Official DevRel gateways and gRPC SearchStream pipelines (2)](#official-devrel-gateways-and-grpc-searchstream-pipelines)
   - [Dynamic schema reflection and field discovery (3)](#dynamic-schema-reflection-and-field-discovery)
   - [Zero-SDK lean REST and minimal GAQL execution (4)](#zero-sdk-lean-rest-and-minimal-gaql-execution)
   - [Edge runtimes and compiled native proxies (4)](#edge-runtimes-and-compiled-native-proxies)
2. [Persist data locally and query with SQL (5)](#2-persist-data-locally-and-query-with-sql)
   - [Embedded SQLite data warehouses with background workers (2)](#embedded-sqlite-data-warehouses-with-background-workers)
   - [Local campaign snapshot and zero-quota analytical caches (3)](#local-campaign-snapshot-and-zero-quota-analytical-caches)
3. [Automate campaign mutations, budgets, and bid strategies (10)](#3-automate-campaign-mutations-budgets-and-bid-strategies)
   - [Direct REST campaign mutation and bid/budget setters (3)](#direct-rest-campaign-mutation-and-bidbudget-setters)
   - [Validated campaign CRUD with dry-run mutation guards (4)](#validated-campaign-crud-with-dry-run-mutation-guards)
   - [Keyword Planner and RLSA audience targeting suites (3)](#keyword-planner-and-rlsa-audience-targeting-suites)
4. [Enforce mutation safety with visual MCP Apps and human approval (4)](#4-enforce-mutation-safety-with-visual-mcp-apps-and-human-approval)
   - [Interactive React widgets with window.postMessage commit bypass (2)](#interactive-react-widgets-with-windowpostmessage-commit-bypass)
   - [Spend protection sliders and physical budget modals (2)](#spend-protection-sliders-and-physical-budget-modals)
5. [Manage agency access and multi-account MCC hierarchies (10)](#5-manage-agency-access-and-multi-account-mcc-hierarchies)
   - [Dynamic MCC switching via login-customer-id routing (3)](#dynamic-mcc-switching-via-login-customer-id-routing)
   - [Proactive 60-minute OAuth token refresh daemons (3)](#proactive-60-minute-oauth-token-refresh-daemons)
   - [Multi-tenant credential vaults and agency proxies (4)](#multi-tenant-credential-vaults-and-agency-proxies)
6. [Analyze performance with domain playbooks and heuristics (4)](#6-analyze-performance-with-domain-playbooks-and-heuristics)
   - [Expert AdTech reasoning engines and conversion lag discounting (1)](#expert-adtech-reasoning-engines-and-conversion-lag-discounting)
   - [Impression share lost-to-budget and micros currency models (3)](#impression-share-lost-to-budget-and-micros-currency-models)
7. [Integrate agentic workflows and multi-platform marketing stacks (9)](#7-integrate-agentic-workflows-and-multi-platform-marketing-stacks)
   - [Autonomous Claude Code marketing skills and CLI copilots (3)](#autonomous-claude-code-marketing-skills-and-cli-copilots)
   - [Unified Google Ads, Meta Ads, and GA4 analytics bridges (6)](#unified-google-ads-meta-ads-and-ga4-analytics-bridges)
8. [Developer comparison matrix (55)](#developer-comparison-matrix)
9. [Resources](#resources)
10. [Reference](#reference)

---

## Developer Comparison Matrix

*55 projects. Side-by-side technical capability comparison across runtime, authentication, persistence, token formatting, and API coverage. Project names link internally to detailed listings below.*

| Project | Role | Runtime | Transport | SearchStream | Dry-Run | Mutations | Search | PMax/Shop | Video/Disp | Offline Conv | GAQL Refl | SQLite Cache | Latency | MCP Apps | HITL Appr | MCC Multi | Refresh Daemon | Footprint | Stars / Cadence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [nowork-studio/notfair-plugin](#nowork-studio-notfair-plugin) | `MCP App Platform` | `TypeScript` | `Streamable HTTP` | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | WAL | Sub-5ms | React | Modal | Dynamic | Auto | Ultra-Low | 3840★ (Active) |
| [irinabuht12-oss/google-meta-ads-ga4-mcp](#irinabuht12-oss-google-meta-ads-ga4-mcp) | `Multi-Platform Suite` | `Polyglot` | `stdio` | No | No | Read-Only | Yes | Yes | Yes | Yes | Yes | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 2033★ (Active) |
| [googleads/google-ads-mcp](#googleads-google-ads-mcp) | `DevRel Gateway` | `Python` | `stdio` | Full | Yes | Read-Only | Yes | Yes | Yes | No | Yes | WAL | Sub-5ms | No | No | Dynamic | Auto | Low | 969★ (Active) |
| [irinabuht12-oss/marketing-skills](#irinabuht12-oss-marketing-skills) | `Agent Skill Suite` | `Markdown` | `stdio` | No | No | Read-Only | Yes | Yes | Yes | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 1638★ (Active) |
| [cohnen/mcp-google-ads](#cohnen-mcp-google-ads) | `Lean REST Gateway` | `Python` | `stdio` | No | No | Read-Only | Yes | Yes | Yes | No | Yes | No | 800ms–2500ms | No | No | Dynamic | Manual | Ultra-Low | 710★ (Active) |
| [kLOsk/adloop](#klosk-adloop) | `Meta-MCP Engine` | `Python` | `stdio` | No | No | Read-Only | Yes | Yes | Yes | No | Yes | WAL | Sub-5ms | No | No | Dynamic | Auto | Ultra-Low | 266★ (Active) |
| [TheMattBerman/google-ads-copilot](#themattberman-google-ads-copilot) | `Agentic Copilot` | `Shell` | `stdio` | No | No | Read-Only | Yes | Yes | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 235★ (Active) |
| [thatrebeccarae/claude-marketing](#thatrebeccarae-claude-marketing) | `Claude Skill Pack` | `Python` | `stdio` | No | No | Read-Only | Yes | Yes | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 147★ (Active) |
| [gomarble-ai/google-ads-mcp-server](#gomarble-ai-google-ads-mcp-server) | `Enterprise Daemon` | `Python` | `stdio` | No | Yes | Yes | Yes | Yes | Yes | No | Yes | WAL | Sub-5ms | No | No | Dynamic | Auto | Low | 144★ (Active) |
| [mathiaschu/google-ads-analyzer](#mathiaschu-google-ads-analyzer) | `Cognitive Brain` | `Python` | `stdio` | No | No | Read-Only | Yes | Yes | Yes | No | Yes | No | 800ms–2500ms | No | No | Single | Manual | Low | 67★ (Active) |
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | `Native Rust Gateway` | `Rust` | `stdio` | Full | No | Read-Only | Yes | Yes | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Ultra-Low | 52★ (Active) |
| [TrueClicks/google-ads-mcp-js](#trueclicks-google-ads-mcp-js) | `Audit & MCC Proxy` | `JavaScript` | `stdio` | No | No | Read-Only | Yes | Yes | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 50★ (Active) |
| [grantweston/google-ads-mcp-complete](#grantweston-google-ads-mcp-complete) | `Campaign Mutator` | `Python` | `stdio` | No | No | Yes | Yes | Yes | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 25★ (Active) |
| [promobase/google-ads-mcp](#promobase-google-ads-mcp) | `Budget Mutator` | `Python` | `stdio` | No | No | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 22★ (Active) |
| [johnoconnor0/google-ads-mcp](#johnoconnor0-google-ads-mcp) | `Auth Daemon` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Auto | Low | 16★ (Active) |
| [davidmosiah/google-ads-mcp-unofficial](#davidmosiah-google-ads-mcp-unofficial) | `Reporting Proxy` | `TypeScript` | `stdio` | No | No | Read-Only | Yes | No | No | No | Yes | No | 800ms–2500ms | No | No | Single | Manual | Low | 4★ (Active) |
| [akelaonline/MCP-Google-Ads](#akelaonline-mcp-google-ads) | `Local SQLite Engine` | `Python` | `stdio` | No | No | Read-Only | Yes | Yes | No | No | No | WAL | Sub-5ms | No | No | Dynamic | Manual | Low | 4★ (Active) |
| [itallstartedwithaidea/google-ads-mcp](#itallstartedwithaidea-google-ads-mcp) | `Marketing Bridge` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 3★ (Active) |
| [VidenGrowth/public-google-ads-mcp](#videngrowth-public-google-ads-mcp) | `Agency Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 2★ (Active) |
| [x777/mcp-google-ads](#x777-mcp-google-ads) | `FastMCP REST Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 1★ (Active) |
| [minholi/google-ads-mcp](#minholi-google-ads-mcp) | `Reporting Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 1★ (Active) |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | `Local Cache Proxy` | `TypeScript` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | WAL | Sub-5ms | No | No | Single | Manual | Low | 1★ (Active) |
| [LucasSantana-Dev/google-ads-mcp](#lucassantana-dev-google-ads-mcp) | `Analytical Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | WAL | Sub-5ms | No | No | Single | Manual | Low | 1★ (Active) |
| [saifshabsug/google-ads-mcp-pro](#saifshabsug-google-ads-mcp-pro) | `Campaign Mutator` | `Python` | `stdio` | No | No | Yes | Yes | Yes | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 1★ (Active) |
| [konradbachowski/google-ads-mcp](#konradbachowski-google-ads-mcp) | `Keyword Specialist` | `Python` | `stdio` | No | No | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | High | 1★ (Active) |
| [growmedevelopment/google-ads-mcp](#growmedevelopment-google-ads-mcp) | `Keyword Specialist` | `Python` | `stdio` | No | No | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 1★ (Active) |
| [ball2jh/google-ads-mcp](#ball2jh-google-ads-mcp) | `Keyword Specialist` | `Python` | `stdio` | No | No | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 1★ (Active) |
| [ameydabhade/google-ads-mcp](#ameydabhade-google-ads-mcp) | `MCP App UI` | `TypeScript` | `stdio` | No | No | Yes | Yes | No | No | No | No | No | 800ms–2500ms | React | Modal | Single | Manual | Low | 1★ (Active) |
| [monsieurgoodmood/google-ads-mcp-plus](#monsieurgoodmood-google-ads-mcp-plus) | `Spend Protector` | `Python` | `stdio` | No | Yes | Yes | Yes | No | No | No | No | No | 800ms–2500ms | React | Modal | Single | Manual | Low | 1★ (Active) |
| [dhawalshah/google-ads-mcp](#dhawalshah-google-ads-mcp) | `Multi-Tenant Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 1★ (Active) |
| [BrandonMiller18/google-ads-mcp](#brandonmiller18-google-ads-mcp) | `Analytics Helper` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 1★ (Active) |
| [BinarCode/google-ads-mcp-http](#binarcode-google-ads-mcp-http) | `Cloud Gateway` | `TypeScript` | `Streamable HTTP` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 0★ (Active) |
| [ThainaJardim/google-ads-mcp](#thainajardim-google-ads-mcp) | `Schema Reflector` | `Python` | `stdio` | No | No | Read-Only | Yes | Yes | Yes | No | Yes | No | 800ms–2500ms | No | No | Single | Manual | Ultra-Low | 0★ (Active) |
| [yeswanthreddyk/Google-ads-MCP](#yeswanthreddyk-google-ads-mcp) | `FastMCP Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | Yes | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [AfzalAliSolangi/GoogleAds-MCP-Server](#afzalalisolangi-googleads-mcp-server) | `Edge Gateway` | `TypeScript` | `stdio` | Full | No | Read-Only | Yes | Yes | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Ultra-Low | 0★ (Active) |
| [Lazare-42/google-ads-mcp](#lazare-42-google-ads-mcp) | `Native Rust Proxy` | `Rust` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Auto | Ultra-Low | 0★ (Active) |
| [kiarashedraki/google-ads-mcp](#kiarashedraki-google-ads-mcp) | `TypeScript Proxy` | `TypeScript` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [cristiandrei1234/google-ads-mcp](#cristiandrei1234-google-ads-mcp) | `TypeScript Proxy` | `TypeScript` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [atlasbarinc/google-ads-mcp](#atlasbarinc-google-ads-mcp) | `Analytical Cache` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | WAL | Sub-5ms | No | No | Single | Manual | Low | 0★ (Active) |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | `Guarded Mutator` | `Python` | `stdio` | No | Yes | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [rgellis/google-ads-mcp](#rgellis-google-ads-mcp) | `Guarded Mutator` | `Python` | `stdio` | No | Yes | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [abdulrhmanalhur/google-ads-MCP](#abdulrhmanalhur-google-ads-mcp) | `Guarded Mutator` | `Python` | `stdio` | No | Yes | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [matheusslg/google-ads-mcp](#matheusslg-google-ads-mcp) | `Guarded Mutator` | `Python` | `stdio` | No | Yes | Yes | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [locomotive-agency/google-ads-mcp](#locomotive-agency-google-ads-mcp) | `Spend Protector` | `Python` | `stdio` | No | Yes | Yes | Yes | No | No | No | No | No | 800ms–2500ms | React | Modal | Dynamic | Manual | Low | 0★ (Active) |
| [noordevtech/GoogleAds-mcp](#noordevtech-googleads-mcp) | `MCC Agency Gateway` | `Python` | `stdio` | No | Yes | Yes | Yes | Yes | Yes | No | Yes | WAL | Sub-5ms | No | No | Dynamic | Auto | Low | 0★ (Active) |
| [ConnorCallison/google-ads-mcp](#connorcallison-google-ads-mcp) | `MCC Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 0★ (Active) |
| [connorstearns/mcp-google-ads](#connorstearns-mcp-google-ads) | `Auth Daemon` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Auto | Low | 0★ (Active) |
| [abhibavishi/google-ads-mcp](#abhibavishi-google-ads-mcp) | `Agency Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 0★ (Active) |
| [shivpanks19/mcp-google-ads](#shivpanks19-mcp-google-ads) | `Agency Proxy` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Dynamic | Manual | Low | 0★ (Active) |
| [alexeykozyavkin/google-ads-mcp](#alexeykozyavkin-google-ads-mcp) | `Analytics Helper` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [Codyp10/Google-Ads-MCP](#codyp10-google-ads-mcp) | `Analytics Helper` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [iflow-mcp/itallstartedwithaidea-google-ads-mcp](#iflow-mcp-itallstartedwithaidea-google-ads-mcp) | `Marketing Bridge` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [zelentsov-dev/google-ads-mcp](#zelentsov-dev-google-ads-mcp) | `Analytics Bridge` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [huzaifa-hb/Google-Ads-MCP](#huzaifa-hb-google-ads-mcp) | `Analytics Bridge` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |
| [mailmanar/google-ads-mcp](#mailmanar-google-ads-mcp) | `Analytics Bridge` | `Python` | `stdio` | No | No | Read-Only | Yes | No | No | No | No | No | 800ms–2500ms | No | No | Single | Manual | Low | 0★ (Active) |

---

## 1. Query and report with GAQL

*13 projects. High-throughput SearchStream pipelines, dynamic schema reflection, and lightweight proxies for executing GAQL queries.*

### Official DevRel gateways and gRPC SearchStream pipelines

*2 projects. Official Google implementations and high-throughput gRPC streaming servers with full protobuf serialization.*

| Project | What it does |
|---|---|
| <a id="googleads-google-ads-mcp"></a>[**googleads/google-ads-mcp**](https://github.com/googleads/google-ads-mcp) | Official Google DevRel reference server featuring high-throughput gRPC SearchStream pipelines, complete protobuf serialization, and validate_only dry-run safety. Ideal for enterprise production gateways requiring direct alignment with upstream Google Ads API releases. |
| <a id="binarcode-google-ads-mcp-http"></a>[**BinarCode/google-ads-mcp-http**](https://github.com/BinarCode/google-ads-mcp-http) | Standalone HTTP and Streamable HTTP transport bridge for Google Ads MCP, built for containerized architectures and remote agents. Eliminates local stdio subprocess deadlocks when orchestrating pipelines in serverless or cloud environments. |

### Dynamic schema reflection and field discovery

*3 projects. Minimalist reflection servers querying GoogleAdsFieldService at runtime to eliminate schema drift and token bloat.*

| Project | What it does |
|---|---|
| <a id="thainajardim-google-ads-mcp"></a>[**ThainaJardim/google-ads-mcp**](https://github.com/ThainaJardim/google-ads-mcp) | Minimalist 3-tool reflection server that queries GoogleAdsFieldService dynamically at runtime, consuming only ~350 tokens per turn. Eliminates schema bloat by letting LLMs inspect available GAQL fields before constructing queries. |
| <a id="davidmosiah-google-ads-mcp-unofficial"></a>[**davidmosiah/google-ads-mcp-unofficial**](https://github.com/davidmosiah/google-ads-mcp-unofficial) | TypeScript reflection wrapper offering dynamic metadata inspection and consolidated reporting across active campaign entities. Designed for Cursor and Claude Desktop developers wanting zero-dependency Node installation. |
| <a id="yeswanthreddyk-google-ads-mcp"></a>[**yeswanthreddyk/Google-ads-MCP**](https://github.com/yeswanthreddyk/Google-ads-MCP) | FastMCP Python server with 10 consolidated tools and Pydantic v2 schemas providing explicit type hints for LLM tool calling. Balances schema clarity with moderate token consumption across standard reporting endpoints. |

### Zero-SDK lean REST and minimal GAQL execution

*4 projects. Lightweight proxies bypassing heavy SDK binaries in favor of direct HTTP calls, raw JSON, and compact GAQL responses.*

| Project | What it does |
|---|---|
| <a id="cohnen-mcp-google-ads"></a>[**cohnen/mcp-google-ads**](https://github.com/cohnen/mcp-google-ads) | Community flagship with 710+ stars that completely bypasses the 500MB Python SDK in favor of direct requests.post REST calls. Serves official GAQL syntax references via gaql:// MCP resources for in-context query synthesis. |
| <a id="x777-mcp-google-ads"></a>[**x777/mcp-google-ads**](https://github.com/x777/mcp-google-ads) | Python FastMCP server executing direct REST calls against Google Ads API v23 with 28 targeted tools. Uses Pydantic data modeling to serialize campaign and ad group metrics without SDK overhead. |
| <a id="afzalalisolangi-googleads-mcp-server"></a>[**AfzalAliSolangi/GoogleAds-MCP-Server**](https://github.com/AfzalAliSolangi/GoogleAds-MCP-Server) | TypeScript MCP server optimized for Cloudflare Workers and edge execution with strict read-only guarantees. Implements streaming response parsing and web-standard OAuth token forwarding for serverless agents. |
| <a id="minholi-google-ads-mcp"></a>[**minholi/google-ads-mcp**](https://github.com/minholi/google-ads-mcp) | Compact Python proxy focusing on campaign-level KPI extraction and automated daily budget reporting. Returns sanitized Markdown summary tables directly formatted for LLM executive summaries. |

### Edge runtimes and compiled native proxies

*4 projects. Compiled Rust and high-performance TypeScript servers designed for serverless, low-memory, and edge execution.*

| Project | What it does |
|---|---|
| <a id="fgribreau-mcp-google-ads"></a>[**FGRibreau/mcp-google-ads**](https://github.com/FGRibreau/mcp-google-ads) | Compiled Rust MCP server delivering sub-millisecond execution times and minimal memory footprint (<15MB RSS). Ideal for high-concurrency enterprise microservices executing continuous GAQL search streams. |
| <a id="lazare-42-google-ads-mcp"></a>[**Lazare-42/google-ads-mcp**](https://github.com/Lazare-42/google-ads-mcp) | High-performance Rust implementation with native Service Account authentication and automated Google OAuth token caching. Built for headless Docker agent containers requiring zero user interaction during execution. |
| <a id="kiarashedraki-google-ads-mcp"></a>[**kiarashedraki/google-ads-mcp**](https://github.com/kiarashedraki/google-ads-mcp) | TypeScript MCP implementation using environment refresh tokens and pre-compiled GAQL query templates. Targets modern JavaScript agent runtimes with minimal configuration overhead. |
| <a id="cristiandrei1234-google-ads-mcp"></a>[**cristiandrei1234/google-ads-mcp**](https://github.com/cristiandrei1234/google-ads-mcp) | TypeScript server wrapping core reporting services with structured zod validation schemas. Offers reliable reporting for campaigns, ad groups, and keyword performance in Node-based agent stacks. |

---

## 2. Persist data locally and query with SQL

*5 projects. Embedded SQLite databases and background ingestion workers enabling sub-5ms SQL analytics with zero API quota consumption.*

### Embedded SQLite data warehouses with background workers

*2 projects. Meta-MCP architectures running local SQLite WAL engines that synchronize account telemetry and execute multi-table joins.*

| Project | What it does |
|---|---|
| <a id="klosk-adloop"></a>[**kLOsk/adloop**](https://github.com/kLOsk/adloop) | Pioneering Meta-MCP analytical engine running an embedded SQLite database in WAL mode with background worker synchronization. Executes complex multi-table SQL queries in 1.8ms–4.2ms with zero daily Google Ads API quota burn. |
| <a id="akelaonline-mcp-google-ads"></a>[**akelaonline/MCP-Google-Ads**](https://github.com/akelaonline/MCP-Google-Ads) | Python local data warehouse server that synchronizes account structures into local SQLite tables upon initialization. Enables agents to run arbitrary SQL joins across campaigns, metrics, and bid strategies without latency. |

### Local campaign snapshot and zero-quota analytical caches

*3 projects. Cached snapshot proxies enabling offline analytical queries and historical performance reporting without API rate limits.*

| Project | What it does |
|---|---|
| <a id="atlasbarinc-google-ads-mcp"></a>[**atlasbarinc/google-ads-mcp**](https://github.com/atlasbarinc/google-ads-mcp) | Local analytical cache server designed for financial audit pipelines and historical metric comparison. Stores campaign snapshots on disk to support longitudinal performance reviews without hitting rate limits. |
| <a id="mharnett-mcp-google-ads"></a>[**mharnett/mcp-google-ads**](https://github.com/mharnett/mcp-google-ads) | TypeScript caching server with 167 commits implementing SQLite persistence for ad performance and search query reports. Provides reliable offline query tools for local analysis in Claude Desktop. |
| <a id="lucassantana-dev-google-ads-mcp"></a>[**LucasSantana-Dev/google-ads-mcp**](https://github.com/LucasSantana-Dev/google-ads-mcp) | Python reporting and caching implementation with built-in export utilities for tabular CSV and JSON analytics. Supports offline data exploration for PPC media buyers triaging underperforming keywords. |

---

## 3. Automate campaign mutations, budgets, and bid strategies

*10 projects. Tools capable of modifying live accounts—adjusting budgets, pausing ad groups, applying recommendations, and managing keyword lists.*

### Direct REST campaign mutation and bid/budget setters

*3 projects. Servers providing direct write endpoints for modifying campaign budgets, pausing ad groups, and adjusting bid amounts.*

| Project | What it does |
|---|---|
| <a id="saifshabsug-google-ads-mcp-pro"></a>[**saifshabsug/google-ads-mcp-pro**](https://github.com/saifshabsug/google-ads-mcp-pro) | Dedicated mutation server offering 43 write endpoints to pause campaigns, adjust daily budgets, and change keyword bids directly. Eliminates read-only passivity for agents acting as automated PPC bid managers. |
| <a id="grantweston-google-ads-mcp-complete"></a>[**grantweston/google-ads-mcp-complete**](https://github.com/grantweston/google-ads-mcp-complete) | Comprehensive multi-service wrapper exposing CampaignService, AdGroupService, and AdGroupCriterionService mutation tools. Built for automated bid adjustments, ad schedule updates, and negative keyword list synchronization. |
| <a id="promobase-google-ads-mcp"></a>[**promobase/google-ads-mcp**](https://github.com/promobase/google-ads-mcp) | Agency-focused mutation proxy allowing agents to update promotional budgets, toggle seasonal ad groups, and pause ad spend. Incorporates account ID validation to prevent cross-client budget pollution. |

### Validated campaign CRUD with dry-run mutation guards

*4 projects. Mutation suites enforcing validate_only dry-run preflights and parameter checks before committing live changes.*

| Project | What it does |
|---|---|
| <a id="epave-google-ads-mcp"></a>[**epave/google-ads-mcp**](https://github.com/epave/google-ads-mcp) | Safety-first campaign CRUD server enforcing validate_only dry-run preflights on all mutate operations. Prevents invalid budget increments and malformed ad structures from throwing unrecoverable API errors. |
| <a id="rgellis-google-ads-mcp"></a>[**rgellis/google-ads-mcp**](https://github.com/rgellis/google-ads-mcp) | Python mutation suite with 166 commits implementing transactional checks and rollback safeguards for campaign bid adjustments. Built to support robust agentic self-healing workflows. |
| <a id="abdulrhmanalhur-google-ads-mcp"></a>[**abdulrhmanalhur/google-ads-MCP**](https://github.com/abdulrhmanalhur/google-ads-MCP) | Validated campaign management server checking currency micros conversions and bid limits before issuing Google Ads API calls. Protects against LLM decimal slips that could overspend budget. |
| <a id="matheusslg-google-ads-mcp"></a>[**matheusslg/google-ads-mcp**](https://github.com/matheusslg/google-ads-mcp) | Python server featuring atomic mutate handlers for updating campaign statuses and target ROAS settings. Includes pre-commit validation to ensure campaign budget IDs match target campaigns. |

### Keyword Planner and RLSA audience targeting suites

*3 projects. Specialized keyword generation, negative keyword list management, and audience targeting automation tools.*

| Project | What it does |
|---|---|
| <a id="konradbachowski-google-ads-mcp"></a>[**konradbachowski/google-ads-mcp**](https://github.com/konradbachowski/google-ads-mcp) | Specialized Keyword Planner MCP server exposing fine-grained tools for keyword generation, search volume forecasting, and RLSA audience targeting. Enables agents to discover high-intent keyword targets and forecast monthly spend. |
| <a id="growmedevelopment-google-ads-mcp"></a>[**growmedevelopment/google-ads-mcp**](https://github.com/growmedevelopment/google-ads-mcp) | PPC keyword and ad group management server with 96 commits providing tools to audit keyword match types and negative keyword conflicts. Ideal for automated hygiene audits in Search campaigns. |
| <a id="ball2jh-google-ads-mcp"></a>[**ball2jh/google-ads-mcp**](https://github.com/ball2jh/google-ads-mcp) | Keyword and campaign management toolkit designed to sync negative keyword lists across multiple Search ad groups. Prevents cross-campaign cannibalization through automated list application. |

---

## 4. Enforce mutation safety with visual MCP Apps and human approval

*4 projects. Interactive React widgets, spend sliders, and window.postMessage protocols that physically bypass the LLM on financial commit.*

### Interactive React widgets with window.postMessage commit bypass

*2 projects. Implementations of @modelcontextprotocol/ext-apps rendering sandboxed webviews for human approval before spend execution.*

| Project | What it does |
|---|---|
| <a id="nowork-studio-notfair-plugin"></a>[**nowork-studio/notfair-plugin**](https://github.com/nowork-studio/notfair-plugin) | Benchmark-topping autonomous growth platform (⭐ 3,840) implementing @modelcontextprotocol/ext-apps with sandboxed React widgets. Physical Approve & Execute buttons trigger JSON-RPC commits via window.postMessage, completely bypassing LLM hallucinations during live spend commits. |
| <a id="ameydabhade-google-ads-mcp"></a>[**ameydabhade/google-ads-mcp**](https://github.com/ameydabhade/google-ads-mcp) | TypeScript MCP server pioneering interactive chat components for Google Ads performance monitoring. Renders visual ROAS charts and campaign status toggle buttons directly within Claude Desktop and Cursor chat interfaces. |

### Spend protection sliders and physical budget modals

*2 projects. UI components featuring spend-cap sliders and visual guardrails to protect against accidental prompt-injection mutations.*

| Project | What it does |
|---|---|
| <a id="monsieurgoodmood-google-ads-mcp-plus"></a>[**monsieurgoodmood/google-ads-mcp-plus**](https://github.com/monsieurgoodmood/google-ads-mcp-plus) | Mutation protection layer introducing visual spend sliders and daily budget confirmation dialogs. Prevents autonomous agents from modifying budgets beyond predefined safety thresholds without explicit human review. |
| <a id="locomotive-agency-google-ads-mcp"></a>[**locomotive-agency/google-ads-mcp**](https://github.com/locomotive-agency/google-ads-mcp) | Agency spend guardrail server enforcing maximum daily spend limits and client-specific approval workflows. Emits human-in-the-loop review prompts whenever proposed budget increases exceed 20%. |

---

## 5. Manage agency access and multi-account MCC hierarchies

*10 projects. Manager Account (MCC) hierarchies, multi-client routing, 60-minute OAuth token refresh daemons, and credential vaults.*

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

*4 projects. Secure multi-client credential isolation and agency gateway proxies designed for enterprise PPC operations.*

| Project | What it does |
|---|---|
| <a id="dhawalshah-google-ads-mcp"></a>[**dhawalshah/google-ads-mcp**](https://github.com/dhawalshah/google-ads-mcp) | Multi-tenant credential isolation server supporting distinct customer OAuth configurations stored securely in environment namespaces. Prevents accidental cross-tenant data leakage in agency environments. |
| <a id="abhibavishi-google-ads-mcp"></a>[**abhibavishi/google-ads-mcp**](https://github.com/abhibavishi/google-ads-mcp) | Python agency gateway with 41 commits providing client account isolation and structured metric reporting. Includes safety checks to ensure queries target valid customer IDs. |
| <a id="shivpanks19-mcp-google-ads"></a>[**shivpanks19/mcp-google-ads**](https://github.com/shivpanks19/mcp-google-ads) | Python proxy supporting dynamic credential switching across multiple Google Cloud project client IDs. Suitable for consultancy teams managing disparate client infrastructure. |
| <a id="videngrowth-public-google-ads-mcp"></a>[**VidenGrowth/public-google-ads-mcp**](https://github.com/VidenGrowth/public-google-ads-mcp) | Open agency connector from Viden Growth facilitating multi-account performance aggregation and automated client reporting. Tailored for agency media planners reviewing cross-client spend. |

---

## 6. Analyze performance with domain playbooks and heuristics

*4 projects. AdTech domain reasoning engines enforcing conversion lag discounting, lost impression share attribution, and currency micros math.*

### Expert AdTech reasoning engines and conversion lag discounting

*1 project. Cognitive analytical engines embedding domain playbooks for 7-day conversion lag discounting and Bid-to-Position heuristics.*

| Project | What it does |
|---|---|
| <a id="mathiaschu-google-ads-analyzer"></a>[**mathiaschu/google-ads-analyzer**](https://github.com/mathiaschu/google-ads-analyzer) | Cognitive reasoning engine embodying 12 expert PPC domain playbooks. Programmatically discounts conversion metrics using 7-day conversion lag curves and applies Bid-to-Position heuristics before recommending budget changes. |

### Impression share lost-to-budget and micros currency models

*3 projects. Specialized math helpers converting between raw micros ($1 = 1,000,000) and auditing Lost IS (budget) versus Lost IS (rank).*

| Project | What it does |
|---|---|
| <a id="brandonmiller18-google-ads-mcp"></a>[**BrandonMiller18/google-ads-mcp**](https://github.com/BrandonMiller18/google-ads-mcp) | Specialized analytics server calculating impression share lost to budget versus rank, converting currency micros to standard units ($1 = 1,000,000 micros). Protects agents from misinterpreting raw AdTech integers. |
| <a id="alexeykozyavkin-google-ads-mcp"></a>[**alexeykozyavkin/google-ads-mcp**](https://github.com/alexeykozyavkin/google-ads-mcp) | Performance audit server providing automated calculation of click-through rate (CTR) anomalies and cost-per-click (CPC) trends across Search campaigns. Delivers clean tabular outputs for agent consumption. |
| <a id="codyp10-google-ads-mcp"></a>[**Codyp10/Google-Ads-MCP**](https://github.com/Codyp10/Google-Ads-MCP) | Python analytics proxy formatting campaign metrics into concise executive summaries with automated currency conversions. Reduces token overhead by stripping raw nested API structures. |

---

## 7. Integrate agentic workflows and multi-platform marketing stacks

*9 projects. Autonomous Claude Code marketing skills, CLI copilot environments, and unified Google Ads + Meta Ads + GA4 growth platforms.*

### Autonomous Claude Code marketing skills and CLI copilots

*3 projects. Ready-to-run Claude Code agent skills and terminal harnesses that execute ad audits and copy generation directly in CLI.*

| Project | What it does |
|---|---|
| <a id="thatrebeccarae-claude-marketing"></a>[**thatrebeccarae/claude-marketing**](https://github.com/thatrebeccarae/claude-marketing) | Popular Claude Code skill collection (⭐ 147) integrating Google Ads audit routines directly into terminal-native agent workflows. Features pre-engineered prompts and scripts for analyzing Search campaign performance. |
| <a id="themattberman-google-ads-copilot"></a>[**TheMattBerman/google-ads-copilot**](https://github.com/TheMattBerman/google-ads-copilot) | High-profile copilot repository (⭐ 235) orchestrating Docker containers and agentic scripts to monitor live ad accounts. Generates proactive Telegram and terminal alerts when budget pacing deviates from target thresholds. |
| <a id="irinabuht12-oss-marketing-skills"></a>[**irinabuht12-oss/marketing-skills**](https://github.com/irinabuht12-oss/marketing-skills) | Comprehensive marketing skill repository (⭐ 1,638) containing ready-to-run markdown skill instructions for Google Ads and paid media optimization. Teaches agents how to diagnose Quality Score drops and structure RSA copy. |

### Unified Google Ads, Meta Ads, and GA4 analytics bridges

*6 projects. Multi-channel marketing suites bridging Google Ads performance data with Meta Ads and Google Analytics 4 telemetry.*

| Project | What it does |
|---|---|
| <a id="irinabuht12-oss-google-meta-ads-ga4-mcp"></a>[**irinabuht12-oss/google-meta-ads-ga4-mcp**](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | Massive multi-platform suite (⭐ 2,033) uniting Google Ads, Meta Ads, and Google Analytics 4 under a single MCP server. Enables cross-channel attribution queries and blended ROAS calculations within a unified agent context. |
| <a id="itallstartedwithaidea-google-ads-mcp"></a>[**itallstartedwithaidea/google-ads-mcp**](https://github.com/itallstartedwithaidea/google-ads-mcp) | Multi-channel marketing server bridging Google Ads performance data with Meta Ads and GA4 reporting pipelines. Built for performance marketers analyzing blended return on ad spend across paid media channels. |
| <a id="iflow-mcp-itallstartedwithaidea-google-ads-mcp"></a>[**iflow-mcp/itallstartedwithaidea-google-ads-mcp**](https://github.com/iflow-mcp/itallstartedwithaidea-google-ads-mcp) | Active downstream fork maintaining cross-platform marketing tools with updated dependency pins and MCP specification compliance. Supports cross-channel reporting for Search and Social campaigns. |
| <a id="zelentsov-dev-google-ads-mcp"></a>[**zelentsov-dev/google-ads-mcp**](https://github.com/zelentsov-dev/google-ads-mcp) | Marketing analytics server providing unified data extraction for Google Ads campaigns and Google Analytics 4 conversion events. Simplifies attribution reporting in agent workflows. |
| <a id="huzaifa-hb-google-ads-mcp"></a>[**huzaifa-hb/Google-Ads-MCP**](https://github.com/huzaifa-hb/Google-Ads-MCP) | Python marketing proxy with 63 commits connecting Google Ads campaign telemetry with ecommerce store conversion tracking. Formats ROAS summaries for automated client updates. |
| <a id="mailmanar-google-ads-mcp"></a>[**mailmanar/google-ads-mcp**](https://github.com/mailmanar/google-ads-mcp) | Cross-channel reporting server with 66 commits providing consolidated spend tracking across Google Ads and supplementary advertising channels. Focuses on daily pacing alerts and budget anomaly detection. |

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
- **Meta-MCP SQLite Ingestion Pattern:** Servers that initialize an embedded SQLite database in WAL mode and spin up a background worker thread (`kLOsk/adloop`, `akelaonline/MCP-Google-Ads`) execute local analytical queries in 1.8ms–4.2ms (over 300x faster than live GAQL) while consuming zero daily API quota.
- **MCP Apps Spend Approvals:** Direct text-based mutation tools expose ad accounts to prompt injection and accidental micro-unit decimal errors. MCP Apps (`nowork-studio/notfair-plugin`, `ameydabhade/google-ads-mcp`) render sandboxed React widgets directly within chat; clicking an approval slider fires JSON-RPC commits via `window.postMessage`, completely bypassing the LLM on financial commit.
- **Proactive Token Refresh Daemons:** Google OAuth access tokens expire after 3,600 seconds (1 hour). Unhandled token expiration causes agent sessions to crash mid-workflow. Production implementations (`gomarble-ai`, `googleads`) maintain background refresh daemons that renew tokens proactively.
- **Currency Micros Conversion:** Google Ads represents monetary values as integer micros ($1.00 = 1,000,000 micros). Specialized helpers convert between micros and standard currency to prevent catastrophic budget inflation.
- **Manager Account (MCC) Hierarchy Routing:** Multi-account agency deployments require dynamic routing via the `login-customer-id` HTTP header, allowing an agent to manage hundreds of client accounts under a single authenticated developer token.
