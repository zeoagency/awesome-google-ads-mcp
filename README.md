# Awesome Google Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Find Google Ads MCP tools by the work they perform, with full tool descriptions and parameters.

**7 MCP servers · 354 tool registrations · 323 unique tool names.**

290 registrations serve Google Ads or shared helpers; 64 other-platform or protocol-test tools appear separately on their provider pages. Also includes 4 CLIs and 7 SDKs.

[Search every tool](docs/TOOLS.md) · [Google Ads API](https://developers.google.com/google-ads/api/docs/start) · [Contribute](CONTRIBUTING.md)

## Contents

- [Explore accounts and explain performance (7)](#explore-accounts-and-explain-performance)
- [Research keywords and control search terms (5)](#research-keywords-and-control-search-terms)
- [Build campaigns and manage budgets (5)](#build-campaigns-and-manage-budgets)
- [Manage creatives, assets, and audiences (5)](#manage-creatives-assets-and-audiences)
- [Track conversions, experiments, and recommendations (4)](#track-conversions-experiments-and-recommendations)
- [Preview, validate, and audit changes (5)](#preview-validate-and-audit-changes)
- [Full MCP tool catalogs (7)](#full-mcp-tool-catalogs)
- [Command-line tools (4)](#command-line-tools)
- [SDKs and client libraries (7)](#sdks-and-client-libraries)

Groups follow registered tools and their implementations. Servers appear in every task they support; counts in task headings are providers, not a ranking. Snapshots were checked on 2026-10-13 using offline MCP listings and source review; no live account operations were tested.

## Explore accounts and explain performance

7 providers.

| MCP | What its tools do |
|---|---|
| [googleads/google-ads-mcp](#googleads-google-ads-mcp) | Discover accounts, inspect fields, and build structured GAQL reports. [`customers_list_accessible_customers`](docs/mcp/googleads-google-ads-mcp.md#tool-customers-list-accessible-customers) · [`search_search`](docs/mcp/googleads-google-ads-mcp.md#tool-search-search) |
| [growmedevelopment/google-ads-mcp](#growmedevelopment-google-ads-mcp) | List enabled manager-account clients and query their performance. [`list_customer_clients`](docs/mcp/growmedevelopment-google-ads-mcp.md#tool-list-customer-clients) · [`search`](docs/mcp/growmedevelopment-google-ads-mcp.md#tool-search) |
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | Run arbitrary GAQL and inspect policy issues. [`run_gaql`](docs/mcp/fgribreau-mcp-google-ads.md#tool-run-gaql) · [`get_policy_issues`](docs/mcp/fgribreau-mcp-google-ads.md#tool-get-policy-issues) |
| [kLOsk/adloop](#klosk-adloop) | Inspect Performance Max results, detailed asset performance, and account changes. [`get_pmax_performance`](docs/mcp/klosk-adloop.md#tool-get-pmax-performance) · [`get_change_history`](docs/mcp/klosk-adloop.md#tool-get-change-history) |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | Diagnose campaign delivery and split performance by conversion action. [`google_ads_get_campaign_diagnostics`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-get-campaign-diagnostics) · [`google_ads_ad_performance_by_conversion`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-ad-performance-by-conversion) |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | Combine campaign diagnostics, impression share, and locally computed hints. [`get_campaign_dashboard`](docs/mcp/epave-google-ads-mcp.md#tool-get-campaign-dashboard) · [`get_impression_share_summary`](docs/mcp/epave-google-ads-mcp.md#tool-get-impression-share-summary) |
| [cesteral/mcp-open-advertising](#cesteral-mcp-open-advertising) | Query GAQL, paginate entities, and read performance insights. [`gads_gaql_search`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-gaql-search) · [`gads_get_insights`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-get-insights) |

## Research keywords and control search terms

5 providers.

| MCP | What its tools do |
|---|---|
| [growmedevelopment/google-ads-mcp](#growmedevelopment-google-ads-mcp) | Expand seed keywords with volume, competition, and bid-range metrics. [`generate_keyword_ideas`](docs/mcp/growmedevelopment-google-ads-mcp.md#tool-generate-keyword-ideas) |
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | Research keyword ideas and draft shared negative keyword lists. [`discover_keywords`](docs/mcp/fgribreau-mcp-google-ads.md#tool-discover-keywords) · [`create_negative_keyword_list`](docs/mcp/fgribreau-mcp-google-ads.md#tool-create-negative-keyword-list) |
| [kLOsk/adloop](#klosk-adloop) | Forecast keyword budgets through KeywordPlanIdeaService and manage brand exclusions. [`estimate_budget`](docs/mcp/klosk-adloop.md#tool-estimate-budget) · [`draft_prepare_brand_exclusions`](docs/mcp/klosk-adloop.md#tool-draft-prepare-brand-exclusions) |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | Fetch keyword volume and identify search terms by conversion action. [`google_ads_keyword_volume`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-keyword-volume) · [`google_ads_search_term_report_by_conversion`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-search-term-report-by-conversion) |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | Inspect search-term categories and preview keyword additions. [`get_search_term_insights`](docs/mcp/epave-google-ads-mcp.md#tool-get-search-term-insights) · [`add_keywords`](docs/mcp/epave-google-ads-mcp.md#tool-add-keywords) |

## Build campaigns and manage budgets

5 providers.

| MCP | What its tools do |
|---|---|
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | Draft Performance Max campaigns, schedules, budgets, and bidding changes. [`create_pmax_campaign`](docs/mcp/fgribreau-mcp-google-ads.md#tool-create-pmax-campaign) · [`set_campaign_schedule`](docs/mcp/fgribreau-mcp-google-ads.md#tool-set-campaign-schedule) |
| [kLOsk/adloop](#klosk-adloop) | Draft campaigns and AI Max settings with preview/apply workflows. [`draft_campaign`](docs/mcp/klosk-adloop.md#tool-draft-campaign) · [`draft_ai_max_settings`](docs/mcp/klosk-adloop.md#tool-draft-ai-max-settings) |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | Change bidding with explicit portfolio-strategy controls. [`google_ads_update_campaign_bidding`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-update-campaign-bidding) · [`google_ads_detach_portfolio_bid_strategy`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-detach-portfolio-bid-strategy) |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | Preview Search, Display, Performance Max, and Demand Gen campaign changes. [`create_demand_gen_campaign`](docs/mcp/epave-google-ads-mcp.md#tool-create-demand-gen-campaign) · [`update_campaign_budget`](docs/mcp/epave-google-ads-mcp.md#tool-update-campaign-budget) |
| [cesteral/mcp-open-advertising](#cesteral-mcp-open-advertising) | Duplicate campaigns and perform bulk resource or status mutations. [`gads_duplicate_entity`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-duplicate-entity) · [`gads_bulk_update_status`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-bulk-update-status) |

## Manage creatives, assets, and audiences

5 providers.

| MCP | What its tools do |
|---|---|
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | Draft search ads, extensions, and Performance Max audience signals. [`draft_responsive_search_ad`](docs/mcp/fgribreau-mcp-google-ads.md#tool-draft-responsive-search-ad) · [`add_asset_group_signal`](docs/mcp/fgribreau-mcp-google-ads.md#tool-add-asset-group-signal) |
| [kLOsk/adloop](#klosk-adloop) | Inspect asset results and draft demographic or creative changes. [`get_detailed_asset_performance`](docs/mcp/klosk-adloop.md#tool-get-detailed-asset-performance) · [`draft_demographic_targeting`](docs/mcp/klosk-adloop.md#tool-draft-demographic-targeting) |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | Update video references and build Demand Gen multi-asset ads. [`google_ads_update_video_ad_videos`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-update-video-ad-videos) · [`google_ads_create_demand_gen_multi_asset_ad`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-create-demand-gen-multi-asset-ad) |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | Add Performance Max text assets; opt-in tools inspect audience overlap and creator insights. [`generate_audience_overlap_insights`](docs/mcp/epave-google-ads-mcp.md#tool-generate-audience-overlap-insights) · [`add_asset_group_text`](docs/mcp/epave-google-ads-mcp.md#tool-add-asset-group-text) |
| [cesteral/mcp-open-advertising](#cesteral-mcp-open-advertising) | Create image assets or assets referencing existing YouTube videos. [`gads_upload_image`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-upload-image) · [`gads_upload_video`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-upload-video) |

## Track conversions, experiments, and recommendations

4 providers.

| MCP | What its tools do |
|---|---|
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | Draft conversion actions and recommendation apply/dismiss operations. [`create_conversion_action`](docs/mcp/fgribreau-mcp-google-ads.md#tool-create-conversion-action) · [`apply_recommendation`](docs/mcp/fgribreau-mcp-google-ads.md#tool-apply-recommendation) |
| [kLOsk/adloop](#klosk-adloop) | Preview enhanced conversion uploads and manage custom conversion goals. [`draft_upload_enhanced_conversions_for_leads`](docs/mcp/klosk-adloop.md#tool-draft-upload-enhanced-conversions-for-leads) · [`draft_custom_conversion_goal`](docs/mcp/klosk-adloop.md#tool-draft-custom-conversion-goal) |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | Create, schedule, end, and promote campaign experiments. [`google_ads_create_experiment`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-create-experiment) · [`google_ads_promote_experiment`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-promote-experiment) |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | Select campaign conversion actions and read Google recommendations. [`set_campaign_conversion_actions`](docs/mcp/epave-google-ads-mcp.md#tool-set-campaign-conversion-actions) · [`get_recommendations`](docs/mcp/epave-google-ads-mcp.md#tool-get-recommendations) |

## Preview, validate, and audit changes

5 providers.

| MCP | What its tools do |
|---|---|
| [FGRibreau/mcp-google-ads](#fgribreau-mcp-google-ads) | Apply stored plans; the default dry run is a local preview, not API validation. [`confirm_and_apply`](docs/mcp/fgribreau-mcp-google-ads.md#tool-confirm-and-apply) |
| [kLOsk/adloop](#klosk-adloop) | Validate eligible Google Ads plan steps and support approval-card apply. [`confirm_and_apply`](docs/mcp/klosk-adloop.md#tool-confirm-and-apply) · [`approve_change`](docs/mcp/klosk-adloop.md#tool-approve-change) |
| [mharnett/mcp-google-ads](#mharnett-mcp-google-ads) | Check RSA assets locally and preview removals before confirmation. [`google_ads_validate_ad`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-validate-ad) · [`google_ads_remove_items`](docs/mcp/mharnett-mcp-google-ads.md#tool-google-ads-remove-items) |
| [epave/google-ads-mcp](#epave-google-ads-mcp) | Refresh confirmation previews and inspect the local DuckDB audit. [`refresh_preview`](docs/mcp/epave-google-ads-mcp.md#tool-refresh-preview) · [`get_local_audit`](docs/mcp/epave-google-ads-mcp.md#tool-get-local-audit) |
| [cesteral/mcp-open-advertising](#cesteral-mcp-open-advertising) | Validate create/update payloads with Google; calculate pacing locally from supplied figures. [`gads_validate_entity`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-validate-entity) · [`gads_get_pacing_status`](docs/mcp/cesteral-mcp-open-advertising.md#tool-gads-get-pacing-status) |

## Full MCP tool catalogs

7 servers. Full counts include optional tools and other-platform sections; each page explains what a default client actually sees.

| MCP | Complete catalog |
|---|---|
| <a id="googleads-google-ads-mcp"></a>[**googleads/google-ads-mcp**](https://github.com/googleads/google-ads-mcp) | [3 tools](docs/mcp/googleads-google-ads-mcp.md) |
| <a id="growmedevelopment-google-ads-mcp"></a>[**growmedevelopment/google-ads-mcp**](https://github.com/growmedevelopment/google-ads-mcp) | [5 tools](docs/mcp/growmedevelopment-google-ads-mcp.md) |
| <a id="fgribreau-mcp-google-ads"></a>[**FGRibreau/mcp-google-ads**](https://github.com/FGRibreau/mcp-google-ads) | [63 tools](docs/mcp/fgribreau-mcp-google-ads.md) |
| <a id="klosk-adloop"></a>[**kLOsk/adloop**](https://github.com/kLOsk/adloop) | [124 tools](docs/mcp/klosk-adloop.md) · 66 Ads/helpers + 58 other-platform |
| <a id="mharnett-mcp-google-ads"></a>[**mharnett/mcp-google-ads**](https://github.com/mharnett/mcp-google-ads) | [76 tools](docs/mcp/mharnett-mcp-google-ads.md) · write opt-in tools included |
| <a id="epave-google-ads-mcp"></a>[**epave/google-ads-mcp**](https://github.com/epave/google-ads-mcp) | [59 tools](docs/mcp/epave-google-ads-mcp.md) · optional audience tools included |
| <a id="cesteral-mcp-open-advertising"></a>[**cesteral/mcp-open-advertising**](https://github.com/cesteral/mcp-open-advertising) | [24 tools](docs/mcp/cesteral-mcp-open-advertising.md) · 18 Ads + 6 optional protocol tests |

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
