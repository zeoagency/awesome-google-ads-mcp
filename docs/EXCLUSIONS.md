# Quarantined & Excluded Entities Ledger: Google Ads MCP Ecosystem Benchmark

**Audit Version:** 1.0.0  
**Evaluation Scope:** Google Ads MCP Ecosystem Candidate Discovery  
**Total Discovered Candidate Pool:** 436  
**Evaluated Core Cohort:** 45  
**Total Quarantined Exclusions:** 391  

---

## 1. Exclusion Governance & Rationale

To preserve the statistical rigor, evidentiary integrity, and actionable utility of the benchmark, candidate repositories identified during wide discovery were systematically quarantined if they failed foundational quality gates.

Exclusion Criteria:

1. **EMPTY_OR_UNMODIFIED_FORK:** Zero-commit downstream forks of upstream repositories without independent modifications or novel tooling.
2. **DORMANT_INACTIVE:** Repositories with no commit activity for >6 months, abandoned prototypes, or unmaintained stubs lacking MCP protocol compliance.
3. **NON_MCP_STANDALONE_SCRIPT:** AdTech scripts, Google Ads API tutorials, or Python ETL tools that lack a Model Context Protocol server interface (`stdio`, `SSE`, Streamable HTTP).
4. **SHALLOW_MARKETING_STUB:** Agency lead-generation repositories, prompt-only Markdown stubs, or multi-platform bundles where Google Ads support is merely aspirational or stubbed.

---

## 2. Quarantined Entities Breakdown

- **DORMANT_INACTIVE:** 314 repositories
- **EMPTY_OR_UNMODIFIED_FORK:** 1 repository
- **NON_MCP_STANDALONE_SCRIPT:** 30 repositories
- **SHALLOW_MARKETING_STUB:** 46 repositories

---

## 3. Quarantined Repositories Directory

### Category: `DORMANT_INACTIVE` (314 repositories)

| # | Repository | Stars | Forks | Language | Last Push | Exclusion Reason |
|---|---|---|---|---|---|---|
| 1 | [`jradcliff/google_ads_mcp`](https://github.com/jradcliff/google_ads_mcp) | 1 | 71 | None | 2025-08-22 | The Google Ads MCP Server is an implementation of the Model  |
| 2 | [`bjorndavidhansen/google-ads-mcp-server`](https://github.com/bjorndavidhansen/google-ads-mcp-server) | 19 | 8 | Python | 2025-04-17 | No description provided |
| 3 | [`DigitalRocket-biz/google-ads-mcp-v20`](https://github.com/DigitalRocket-biz/google-ads-mcp-v20) | 11 | 10 | Python | 2025-06-29 | Google Ads API v20 MCP Server - Complete implementation with |
| 4 | [`gabogabucho/google-ads-mcp`](https://github.com/gabogabucho/google-ads-mcp) | 15 | 3 | Python | 2026-03-10 | MCP para Claude, Claude Code  de Google Ads y GA4 |
| 5 | [`block-town/google-ads-transparency-mcp`](https://github.com/block-town/google-ads-transparency-mcp) | 7 | 4 | Python | 2026-09-09 | MCP server for the Google Ads Transparency Center — look up  |
| 6 | [`AppsYogi-com/adsense-mcp-server`](https://github.com/AppsYogi-com/adsense-mcp-server) | 5 | 3 | TypeScript | 2026-01-20 | A CLI-installable MCP (Model Context Protocol) server that e |
| 7 | [`jgdeutsch/google-ads-mcp`](https://github.com/jgdeutsch/google-ads-mcp) | 2 | 2 | TypeScript | 2026-02-16 | Remote MCP server for Google Ads API analytics |
| 8 | [`samihalawa/google-ads-mcp-server`](https://github.com/samihalawa/google-ads-mcp-server) | 2 | 3 | JavaScript | 2025-11-24 | Model Context Protocol server for Google Ads management |
| 9 | [`mikdeangelis/mcp-google-ads`](https://github.com/mikdeangelis/mcp-google-ads) | 4 | 2 | Python | 2026-02-24 | MCP server for Google Ads API integration |
| 10 | [`TrueClicks/google-ads-mcp-dotnet`](https://github.com/TrueClicks/google-ads-mcp-dotnet) | 9 | 1 | C# | 2026-01-07 | Unofficial Google Ads MCP |
| 11 | [`gokhunyayla/google-ads-mcp-server`](https://github.com/gokhunyayla/google-ads-mcp-server) | 2 | 2 | TypeScript | 2025-07-31 | This is an MCP server for Google Ads API. |
| 12 | [`CAPTAINCODERCOOL/AI-powered-SEO-automation-platform-integrating-Google-Ads-Keyword-Planner`](https://github.com/CAPTAINCODERCOOL/AI-powered-SEO-automation-platform-integrating-Google-Ads-Keyword-Planner) | 8 | 2 | None | 2025-05-13 | AI-powered SEO automation platform integrating Google Ads Ke |
| 13 | [`kiri2sama/google_ads_mcp_server`](https://github.com/kiri2sama/google_ads_mcp_server) | 0 | 2 | None | 2025-10-10 | This repo has been archived in favor of upstream repository |
| 14 | [`GoAnyAPI/goanyapi-mcp`](https://github.com/GoAnyAPI/goanyapi-mcp) | 3 | 2 | TypeScript | 2026-08-31 | Official GoAnyAPI MCP server — connect AI agents to web data |
| 15 | [`nowork-studio/google-ads-mcp`](https://github.com/nowork-studio/google-ads-mcp) | 3 | 1 | None | 2026-08-24 | Hosted Google Ads MCP setup guide for AI agents, powered by  |
| 16 | [`bertramdev/GoogleAdsMCP`](https://github.com/bertramdev/GoogleAdsMCP) | 2 | 1 | Python | 2026-03-23 | Google Ads MCP server — 47 tools for full read/write access  |
| 17 | [`guozheng/mcp-server-google-ads`](https://github.com/guozheng/mcp-server-google-ads) | 2 | 1 | Python | 2025-10-08 | An MCP server for Google Ads |
| 18 | [`freema/mcp-google-marketing`](https://github.com/freema/mcp-google-marketing) | 3 | 0 | TypeScript | 2026-09-19 | MCP server for Google Marketing Platform - manage Google Ana |
| 19 | [`channel47/google-ads-mcp-server`](https://github.com/channel47/google-ads-mcp-server) | 2 | 0 | JavaScript | 2026-01-13 | No description provided |
| 20 | [`MaxGhenis/google-ads-mcp-rw`](https://github.com/MaxGhenis/google-ads-mcp-rw) | 2 | 0 | Python | 2026-02-10 | Google Ads MCP server with read AND write capabilities - cre |
| 21 | [`davidmosiah/google-ads-intent-mcp`](https://github.com/davidmosiah/google-ads-intent-mcp) | 2 | 0 | Python | 2026-08-29 | Dry-run-first Google Ads search-term intent analyzer and neg |
| 22 | [`RyleyReid/google-ads-claude`](https://github.com/RyleyReid/google-ads-claude) | 2 | 0 | Python | 2026-03-28 | Google Ads MCP server for Claude Desktop and AWS Lambda |
| 23 | [`OwlPharaoh20/Marv-Google-ads-AI-agent`](https://github.com/OwlPharaoh20/Marv-Google-ads-AI-agent) | 3 | 0 | Python | 2025-07-19 | 🤖 Marv is a CLI-based AI agent that helps you create, manage |
| 24 | [`diogo622/google-marketing-solutions-google_ads_mcp`](https://github.com/diogo622/google-marketing-solutions-google_ads_mcp) | 0 | 0 | None | 2026-07-06 | MCP Google Ads |
| 25 | [`Djancyp/oido-google-ads`](https://github.com/Djancyp/oido-google-ads) | 0 | 0 | Go | 2026-07-31 | google ads mcp |
| 26 | [`MMM-tl/GoogleADs-MCP`](https://github.com/MMM-tl/GoogleADs-MCP) | 0 | 0 | Python | 2026-09-16 | No description provided |
| 27 | [`electricsymphonymedia/GoogleAds-MCP`](https://github.com/electricsymphonymedia/GoogleAds-MCP) | 0 | 1 | Python | 2025-08-10 | No description provided |
| 28 | [`pipeworx-io/mcp-google_ads`](https://github.com/pipeworx-io/mcp-google_ads) | 0 | 0 | TypeScript | 2026-09-18 | Google Ads MCP Pack |
| 29 | [`AI-CRO/google-ads-mcp`](https://github.com/AI-CRO/google-ads-mcp) | 0 | 0 | Python | 2026-01-29 | Google Ads MCP Server |
| 30 | [`mngocloi/google-ads-mcp`](https://github.com/mngocloi/google-ads-mcp) | 0 | 0 | Python | 2026-09-03 | MCP server for Google Ads API (forked from googleads/google- |
| 31 | [`sivavamana/poorvika-google-ads-mcp`](https://github.com/sivavamana/poorvika-google-ads-mcp) | 0 | 0 | Python | 2026-04-09 | Ads Automation - Google |
| 32 | [`lkalajzic/google-ads-mcp-private`](https://github.com/lkalajzic/google-ads-mcp-private) | 0 | 0 | TypeScript | 2025-08-04 | Google Ads MCP Server - Control Google Ads through Claude De |
| 33 | [`Ponti-Digital/google-ads-mcp-bridge`](https://github.com/Ponti-Digital/google-ads-mcp-bridge) | 0 | 0 | Python | 2026-03-15 | MCP Google Ads (Bridges) |
| 34 | [`isteamhq/mcp-servers`](https://github.com/isteamhq/mcp-servers) | 3 | 0 | None | 2026-04-10 | Open-source MCP servers for Twitter, Bluesky, LinkedIn, Goog |
| 35 | [`mhamoudacom/GAdConductor`](https://github.com/mhamoudacom/GAdConductor) | 3 | 0 | None | 2026-07-24 | Google Ads + Claude — let Claude Code or Codex CLI conduct y |
| 36 | [`dirkschmid1/google-ads-mcp`](https://github.com/dirkschmid1/google-ads-mcp) | 1 | 0 | TypeScript | 2026-02-23 | Google Ads MCP Server - Vercel |
| 37 | [`kakafalconi/google-ads-mcp`](https://github.com/kakafalconi/google-ads-mcp) | 0 | 1 | None | 2026-02-28 | Google Ads MCP Server with 6 write tools. Fork of googleads/ |
| 38 | [`baremetallabs-ai/google-ads-mcp`](https://github.com/baremetallabs-ai/google-ads-mcp) | 0 | 0 | TypeScript | 2026-09-18 | MCP server for inspecting and managing Google Ads accounts v |
| 39 | [`kevinkiplimo/Google-ads_Belva_MCP`](https://github.com/kevinkiplimo/Google-ads_Belva_MCP) | 0 | 0 | None | 2026-07-08 | MCP Connection |
| 40 | [`isteamhq/google-ads-mcp`](https://github.com/isteamhq/google-ads-mcp) | 1 | 0 | TypeScript | 2026-09-14 | MCP server for Google Ads — manage campaigns, keywords, ads, |
| 41 | [`smarjorie/google-ads-api`](https://github.com/smarjorie/google-ads-api) | 0 | 0 | TypeScript | 2026-09-16 | mcp-custom-google-api |
| 42 | [`yusofansari/google-ads-mcp`](https://github.com/yusofansari/google-ads-mcp) | 0 | 0 | Python | 2026-07-02 | Free, open-source MCP server (57 tools) connecting Google Ad |
| 43 | [`Edafeoghene-Egona/google-ads-mcp`](https://github.com/Edafeoghene-Egona/google-ads-mcp) | 0 | 0 | Python | 2026-04-01 | No description provided |
| 44 | [`Asrar-M/google-ads-mcp`](https://github.com/Asrar-M/google-ads-mcp) | 0 | 0 | TypeScript | 2026-03-15 | No description provided |
| 45 | [`v-p3truk/mcp-google-ads`](https://github.com/v-p3truk/mcp-google-ads) | 0 | 0 | Python | 2026-07-13 | Google Ads MCP server with write operations (fork of cohnen/ |
| 46 | [`ab-solution-dev/google-ads-mcp`](https://github.com/ab-solution-dev/google-ads-mcp) | 0 | 0 | Python | 2026-05-19 | Connect Claude AI to Google Ads via MCP — analyze campaigns, |
| 47 | [`aisandler/google-ads-mcp`](https://github.com/aisandler/google-ads-mcp) | 0 | 0 | TypeScript | 2026-03-09 | MCP server for Google Ads campaign reporting and management  |
| 48 | [`at-dan/google-ads-mcp`](https://github.com/at-dan/google-ads-mcp) | 0 | 0 | TypeScript | 2026-04-16 | MCP server for Google Ads API and YouTube video analytics wi |
| 49 | [`EmongMarcc/google-ads-mcp`](https://github.com/EmongMarcc/google-ads-mcp) | 0 | 0 | JavaScript | 2026-03-08 | Google Ads MCP Server for Claude.ai - 18 tools for campaign  |
| 50 | [`Pinlyx/google-ads-mcp`](https://github.com/Pinlyx/google-ads-mcp) | 0 | 0 | None | 2026-09-17 | Google Ads MCP server guide: run your ad account from Claude |
| 51 | [`quvoid/Google-ads-mcp-`](https://github.com/quvoid/Google-ads-mcp-) | 0 | 0 | None | 2026-07-15 | No description provided |
| 52 | [`lkalajzic/google-ads-mcp`](https://github.com/lkalajzic/google-ads-mcp) | 1 | 0 | TypeScript | 2025-08-13 | No description provided |
| 53 | [`midia-simples/google-ads-mcp`](https://github.com/midia-simples/google-ads-mcp) | 0 | 0 | Python | 2026-03-17 | No description provided |
| 54 | [`danielpopamd/google-ads-mcp`](https://github.com/danielpopamd/google-ads-mcp) | 0 | 0 | None | 2026-06-21 | Google Ads MCP server, remote and hosted by AdPlug. Connect  |
| 55 | [`edgarcgpb-dot/mcp-google-ads`](https://github.com/edgarcgpb-dot/mcp-google-ads) | 0 | 0 | Python | 2026-08-26 | MCP para consultar anúncios no Google Ads |
| 56 | [`ashathyapriyan/google-ads-mcp`](https://github.com/ashathyapriyan/google-ads-mcp) | 0 | 0 | TypeScript | 2026-05-07 | Google Ads MCP Server for Claude |
| 57 | [`qmedia-by/google-ads-mcp`](https://github.com/qmedia-by/google-ads-mcp) | 0 | 0 | Python | 2026-08-24 | No description provided |
| 58 | [`mcp-dir/google_ads-mcp`](https://github.com/mcp-dir/google_ads-mcp) | 0 | 0 | None | 2026-08-30 | Full Google Ads management: read (campaigns, performance, RO |
| 59 | [`Mostafa-Ghanem/google-ads-mcp`](https://github.com/Mostafa-Ghanem/google-ads-mcp) | 0 | 0 | TypeScript | 2026-08-02 | No description provided |
| 60 | [`seovimalraj/google-ads-mcp`](https://github.com/seovimalraj/google-ads-mcp) | 1 | 1 | TypeScript | 2025-12-23 | Google ads mcp server to connect any mcp server and run keyw |
| 61 | [`naddot/google-ads-mcp`](https://github.com/naddot/google-ads-mcp) | 0 | 0 | Python | 2026-05-18 | No description provided |
| 62 | [`GoogleAdsMcpOrg/google-ads-mcp`](https://github.com/GoogleAdsMcpOrg/google-ads-mcp) | 1 | 0 | TypeScript | 2026-09-14 | No description provided |
| 63 | [`WEYERSK/Google-Ads-MCP`](https://github.com/WEYERSK/Google-Ads-MCP) | 0 | 0 | Python | 2026-07-22 | Local stdio MCP server for full Google Ads campaign manageme |
| 64 | [`samtactical/Google-ads-mcp`](https://github.com/samtactical/Google-ads-mcp) | 0 | 0 | Python | 2026-08-24 | No description provided |
| 65 | [`valentimtiago07-ship-it/google-ads-mcp`](https://github.com/valentimtiago07-ship-it/google-ads-mcp) | 0 | 0 | Python | 2026-05-15 | No description provided |
| 66 | [`phwtsp/mcp-google-ads`](https://github.com/phwtsp/mcp-google-ads) | 0 | 0 | Python | 2026-03-10 | No description provided |
| 67 | [`Elnura-mxn/google-ads-mcp`](https://github.com/Elnura-mxn/google-ads-mcp) | 0 | 0 | Python | 2026-07-28 | No description provided |
| 68 | [`AmineZhioua/mcp-google-ads`](https://github.com/AmineZhioua/mcp-google-ads) | 0 | 0 | TypeScript | 2026-05-22 | Intelligence layer between your AI agents and Google Ads API |
| 69 | [`Ro-wdy/mcp-google-ads`](https://github.com/Ro-wdy/mcp-google-ads) | 0 | 0 | None | 2026-08-11 | No description provided |
| 70 | [`noviq-ai/google-ads-mcp`](https://github.com/noviq-ai/google-ads-mcp) | 0 | 0 | Python | 2026-03-21 | MCP server for Google Ads - search ad account data and list  |
| 71 | [`JNServiceHVACandPlumbing/Google-Ads-MCP`](https://github.com/JNServiceHVACandPlumbing/Google-Ads-MCP) | 0 | 0 | None | 2026-09-19 | No description provided |
| 72 | [`ppcmarketing-sudo/google-ads-mcp`](https://github.com/ppcmarketing-sudo/google-ads-mcp) | 0 | 0 | Python | 2026-07-18 | No description provided |
| 73 | [`Reuben1987AI/google-ads-mcp`](https://github.com/Reuben1987AI/google-ads-mcp) | 0 | 0 | Python | 2026-06-18 | No description provided |
| 74 | [`ThomasPepperz/google-ads-mcp`](https://github.com/ThomasPepperz/google-ads-mcp) | 0 | 0 | Python | 2026-05-24 | Google Ads Reporting MCP Server for Claude |
| 75 | [`lbiteam/google-ads-mcp`](https://github.com/lbiteam/google-ads-mcp) | 0 | 0 | None | 2026-05-19 | No description provided |
| 76 | [`coupler-io/google-ads-mcp`](https://github.com/coupler-io/google-ads-mcp) | 1 | 0 | None | 2026-09-16 | Google Ads MCP server by Coupler.io for analyzing campaigns, |
| 77 | [`yigitkonur/mcp-ads-google`](https://github.com/yigitkonur/mcp-ads-google) | 0 | 0 | TypeScript | 2026-05-07 | MCP server exposing 98 Google Ads tools, 5 resources, and 10 |
| 78 | [`uLytics/google-ads-mcp`](https://github.com/uLytics/google-ads-mcp) | 0 | 0 | TypeScript | 2025-10-19 | No description provided |
| 79 | [`gnoah241201/mcp-google-ads`](https://github.com/gnoah241201/mcp-google-ads) | 0 | 0 | Python | 2026-05-27 | No description provided |
| 80 | [`jarrah-agency/google-ads-mcp`](https://github.com/jarrah-agency/google-ads-mcp) | 0 | 0 | Python | 2026-09-01 | No description provided |
| 81 | [`vertexdevs-hq/google-ads-mcp`](https://github.com/vertexdevs-hq/google-ads-mcp) | 0 | 0 | TypeScript | 2026-08-22 | No description provided |
| 82 | [`Asaya-01/Google-Ads-MCP`](https://github.com/Asaya-01/Google-Ads-MCP) | 0 | 0 | Python | 2026-09-11 | No description provided |
| 83 | [`dotsoftsolutions1/google-ads-mcp`](https://github.com/dotsoftsolutions1/google-ads-mcp) | 0 | 0 | None | 2026-07-10 | No description provided |
| 84 | [`EkaanshIM/google-ads-mcp`](https://github.com/EkaanshIM/google-ads-mcp) | 0 | 0 | Python | 2026-05-29 | No description provided |
| 85 | [`soriagaldona/google-ads-mcp`](https://github.com/soriagaldona/google-ads-mcp) | 0 | 0 | TypeScript | 2026-02-17 | MCP Server for Google Ads/Advertising documentation - Search |
| 86 | [`apexradius/mcp-google-ads`](https://github.com/apexradius/mcp-google-ads) | 0 | 0 | Python | 2026-09-16 | Multi-account Google Ads MCP server — campaign performance,  |
| 87 | [`juniormilani/google-ads-mcp`](https://github.com/juniormilani/google-ads-mcp) | 0 | 0 | Python | 2026-03-13 | No description provided |
| 88 | [`nishiura-procmo/google-ads-mcp`](https://github.com/nishiura-procmo/google-ads-mcp) | 0 | 0 | Python | 2026-04-06 | Google Ads MCP Server (Read-Only) - AIと会話するだけでGoogle広告データを分析 |
| 89 | [`twominutereports/google-ads-mcp`](https://github.com/twominutereports/google-ads-mcp) | 0 | 0 | None | 2026-04-10 | MCP server to connect AI with Google Ads |
| 90 | [`PradeepGontupuli/Google-Ads-MCP`](https://github.com/PradeepGontupuli/Google-Ads-MCP) | 0 | 0 | Python | 2026-09-11 | No description provided |
| 91 | [`muradiants/google-ads-mcp`](https://github.com/muradiants/google-ads-mcp) | 0 | 0 | Python | 2026-02-11 | MCP server for managing Google Ads campaigns via Claude |
| 92 | [`elvis-velez/google-ads-mcp`](https://github.com/elvis-velez/google-ads-mcp) | 1 | 0 | Python | 2026-09-20 | Manage Google Ads accounts via MCP. Execute GAQL reads and s |
| 93 | [`PaidSync/google-ads-mcp`](https://github.com/PaidSync/google-ads-mcp) | 0 | 0 | None | 2026-08-24 | Google Ads MCP server with full write access, 133 tools, MCC |
| 94 | [`nikhilarokkam/mcp-google-ads`](https://github.com/nikhilarokkam/mcp-google-ads) | 0 | 0 | Python | 2025-06-09 | No description provided |
| 95 | [`boheastill/google-ads-mcp`](https://github.com/boheastill/google-ads-mcp) | 0 | 0 | Python | 2026-07-12 | MCP server connecting Claude Desktop to Google Ads — manage  |
| 96 | [`aminezindine/GOOGLE-ADS-MCP`](https://github.com/aminezindine/GOOGLE-ADS-MCP) | 0 | 0 | None | 2026-04-11 | No description provided |
| 97 | [`scalably-io/google-ads-mcp`](https://github.com/scalably-io/google-ads-mcp) | 0 | 0 | Python | 2026-09-16 | Google Ads MCP server: GAQL queries, resources, recommendati |
| 98 | [`RaphizSanders/google-ads-mcp`](https://github.com/RaphizSanders/google-ads-mcp) | 0 | 0 | TypeScript | 2026-09-19 | MCP server para gerenciar Google Ads. Local (stdio) e remoto |
| 99 | [`jonkinesis/google-ads-mcp`](https://github.com/jonkinesis/google-ads-mcp) | 0 | 0 | Python | 2026-09-20 | Remote MCP server for Google Ads API (Railway, service accou |
| 100 | [`Oskelias/google-ads-mcp`](https://github.com/Oskelias/google-ads-mcp) | 0 | 0 | None | 2026-07-21 | No description provided |
| 101 | [`SamPlayz6/google-ads-mcp`](https://github.com/SamPlayz6/google-ads-mcp) | 0 | 0 | Python | 2026-04-03 | MCP server for managing Google Ads campaigns from Claude Cod |
| 102 | [`AISATURN/google-ads-mcp`](https://github.com/AISATURN/google-ads-mcp) | 0 | 0 | TypeScript | 2026-09-01 | No description provided |
| 103 | [`remoas/google-ads-mcp`](https://github.com/remoas/google-ads-mcp) | 1 | 0 | JavaScript | 2026-03-25 | Google Ads MCP server for Claude Code — search term mining,  |
| 104 | [`kazuhitoNaotsuka/google-ads-mcp`](https://github.com/kazuhitoNaotsuka/google-ads-mcp) | 0 | 0 | JavaScript | 2026-04-09 | Google Ads API MCP Server for Claude Desktop / Claude Code |
| 105 | [`jagmohan0908/google-ads-mcp`](https://github.com/jagmohan0908/google-ads-mcp) | 0 | 0 | Python | 2026-04-16 | No description provided |
| 106 | [`xjodoin/google-ads-mcp`](https://github.com/xjodoin/google-ads-mcp) | 0 | 0 | None | 2025-12-02 | No description provided |
| 107 | [`isaganiesteron/google-ads-mcp`](https://github.com/isaganiesteron/google-ads-mcp) | 0 | 0 | Python | 2025-12-17 | No description provided |
| 108 | [`raphavianna/mcp-google-ads`](https://github.com/raphavianna/mcp-google-ads) | 0 | 0 | None | 2026-08-07 | No description provided |
| 109 | [`gotrellis/google-ads-mcp-server`](https://github.com/gotrellis/google-ads-mcp-server) | 0 | 0 | Python | 2026-09-15 | MCP server for Google Ads API. Paired with clio-idx feat/goo |
| 110 | [`BryanMartinez1014/PruebaQA`](https://github.com/BryanMartinez1014/PruebaQA) | 0 | 0 | HTML | 2025-11-28 | MCP Google ADS test |
| 111 | [`vengadesh66/googleAds-MultiAgent-KPI-research-campaign-planner`](https://github.com/vengadesh66/googleAds-MultiAgent-KPI-research-campaign-planner) | 2 | 1 | Jupyter Notebook | 2025-11-26 | This aims to create a multi agents orchestrate together to p |
| 112 | [`webvibe-io/google-ads-api-mcp`](https://github.com/webvibe-io/google-ads-api-mcp) | 0 | 0 | TypeScript | 2026-05-08 | MCP server for Google Ads API |
| 113 | [`ramosfernando2/mcp-google-ads-remote`](https://github.com/ramosfernando2/mcp-google-ads-remote) | 0 | 0 | Python | 2026-09-10 | Remote Google Ads MCP server (HTTP) |
| 114 | [`pipeworx-io/mcp-seo-keywords-ads`](https://github.com/pipeworx-io/mcp-seo-keywords-ads) | 0 | 0 | TypeScript | 2026-09-18 | SEO Keywords (Google Ads volume) MCP — exact Google Ads sear |
| 115 | [`marcosvb1/google-ads-mcp-worker`](https://github.com/marcosvb1/google-ads-mcp-worker) | 0 | 0 | TypeScript | 2026-08-09 | Remote MCP server for the Google Ads API on Cloudflare Worke |
| 116 | [`nishiura-procmo/google-ads-mcp-readonly`](https://github.com/nishiura-procmo/google-ads-mcp-readonly) | 0 | 0 | Python | 2026-04-22 | Google Ads MCP Server (Read-Only) - AIと会話するだけでGoogle広告データを分析 |
| 117 | [`dulanp18/google-ads-agency-mcp`](https://github.com/dulanp18/google-ads-agency-mcp) | 0 | 0 | TypeScript | 2026-06-06 | Remote MCP server for querying Google Ads data from Claude D |
| 118 | [`paperbook-api/paperbook-google-ads-mcp`](https://github.com/paperbook-api/paperbook-google-ads-mcp) | 0 | 0 | None | 2026-08-12 | MCP server for PaperBook Google Ads API |
| 119 | [`flin-agency/flin-google-ads-mcp`](https://github.com/flin-agency/flin-google-ads-mcp) | 0 | 0 | Python | 2026-08-04 | No description provided |
| 120 | [`smileCompiler/google-ads-mcp-server`](https://github.com/smileCompiler/google-ads-mcp-server) | 0 | 0 | Python | 2026-06-30 | A Model Context Protocol (MCP) server that provides access t |
| 121 | [`clientskatbi/google-ads-campaign-mcp`](https://github.com/clientskatbi/google-ads-campaign-mcp) | 0 | 0 | Python | 2026-08-09 | MCP server for managing Google Ads campaigns: accounts, camp |
| 122 | [`EmilyThaHuman/google-ads-mcp-server`](https://github.com/EmilyThaHuman/google-ads-mcp-server) | 0 | 0 | None | 2026-05-02 | Model Context Protocol server for Google Ads integration |
| 123 | [`pralayasimha23/google-ads-mcp-connector`](https://github.com/pralayasimha23/google-ads-mcp-connector) | 0 | 0 | Python | 2026-08-16 | No description provided |
| 124 | [`ctrlswing/google-ads-mcp-server`](https://github.com/ctrlswing/google-ads-mcp-server) | 0 | 0 | JavaScript | 2026-01-09 | No description provided |
| 125 | [`maimaiyeuem12009/google-ads-mcp-complete`](https://github.com/maimaiyeuem12009/google-ads-mcp-complete) | 0 | 0 | Python | 2026-03-22 | No description provided |
| 126 | [`YerayRodri/google-ads-write-mcp`](https://github.com/YerayRodri/google-ads-write-mcp) | 0 | 0 | Python | 2026-08-30 | No description provided |
| 127 | [`quannguyen2702/pmax-google-ads-mcp`](https://github.com/quannguyen2702/pmax-google-ads-mcp) | 1 | 0 | Python | 2026-05-12 | No description provided |
| 128 | [`anegash/google-ads-mcp-server`](https://github.com/anegash/google-ads-mcp-server) | 0 | 0 | TypeScript | 2025-09-14 | 🚀 Google Ads MCP Server - AI-powered Google Ads management f |
| 129 | [`0-shiv/google-ads-gateway-mcp`](https://github.com/0-shiv/google-ads-gateway-mcp) | 0 | 0 | JavaScript | 2026-06-10 | MCP server for Codex to query a Google Ads MCC via the Cloud |
| 130 | [`YaroslavFm/google-ads-mcp-extended`](https://github.com/YaroslavFm/google-ads-mcp-extended) | 0 | 0 | Python | 2026-09-10 | No description provided |
| 131 | [`C0TB/google-ads-mcp-server`](https://github.com/C0TB/google-ads-mcp-server) | 0 | 0 | Python | 2026-09-14 | No description provided |
| 132 | [`guruguruman/google-ads-keyword-mcp`](https://github.com/guruguruman/google-ads-keyword-mcp) | 0 | 0 | TypeScript | 2026-08-10 | No description provided |
| 133 | [`LuckSigog/google-ads-mcp-coolify`](https://github.com/LuckSigog/google-ads-mcp-coolify) | 0 | 0 | Python | 2026-05-25 | Self-hosted Google Ads MCP server for Coolify, Docker, and a |
| 134 | [`vent3r/google-ads-mcp-railway`](https://github.com/vent3r/google-ads-mcp-railway) | 0 | 0 | Python | 2026-02-20 | No description provided |
| 135 | [`shariqriazz/google-ads-mcp-modularized`](https://github.com/shariqriazz/google-ads-mcp-modularized) | 0 | 0 | TypeScript | 2026-08-11 | MCP server for Google Ads reporting, diagnostics, keyword pl |
| 136 | [`luizclaudioralile-web/google-ads-mcp-showcase`](https://github.com/luizclaudioralile-web/google-ads-mcp-showcase) | 0 | 0 | Python | 2026-06-06 | Google Ads MCP server + analytics toolkit in Python: weekly  |
| 137 | [`jkvistborg/google-ads-mcp-setup`](https://github.com/jkvistborg/google-ads-mcp-setup) | 0 | 0 | None | 2026-03-25 | No description provided |
| 138 | [`marcofrasson/vibe-google-ads-mcp`](https://github.com/marcofrasson/vibe-google-ads-mcp) | 0 | 0 | Python | 2026-09-21 | Fork Vibe do google-ads-mcp: leitura + escrita (mutate) + ke |
| 139 | [`Luxand/google-ads-write-mcp`](https://github.com/Luxand/google-ads-write-mcp) | 1 | 1 | Python | 2026-09-16 | Allow-listed write-side MCP server for Google Ads (dry run b |
| 140 | [`wvuhskr/mcp-google-ads-safe`](https://github.com/wvuhskr/mcp-google-ads-safe) | 0 | 0 | Python | 2026-09-14 | Safety-first Google Ads MCP server: draft/confirm writes, pe |
| 141 | [`Gatescrispy/mcp-google-ads-ultimate`](https://github.com/Gatescrispy/mcp-google-ads-ultimate) | 0 | 0 | Python | 2025-08-07 | The most comprehensive Google Ads MCP server - 145 specializ |
| 142 | [`octadigitalia/google-ads-mcp-server`](https://github.com/octadigitalia/google-ads-mcp-server) | 0 | 0 | Python | 2026-05-22 | No description provided |
| 143 | [`matteomilonekr/google-ads-manager-mcp`](https://github.com/matteomilonekr/google-ads-manager-mcp) | 0 | 0 | Python | 2026-03-22 | No description provided |
| 144 | [`jamescroall/google-ads-mcp-local`](https://github.com/jamescroall/google-ads-mcp-local) | 0 | 0 | Python | 2026-04-28 | No description provided |
| 145 | [`s2003zy/google-ads-mcp-server`](https://github.com/s2003zy/google-ads-mcp-server) | 0 | 0 | Python | 2025-08-06 | No description provided |
| 146 | [`manak-debug/google-ads-mcp-cloud`](https://github.com/manak-debug/google-ads-mcp-cloud) | 0 | 0 | JavaScript | 2026-03-30 | No description provided |
| 147 | [`jacsander/google-ads-mcp-server`](https://github.com/jacsander/google-ads-mcp-server) | 0 | 0 | Python | 2025-11-17 | No description provided |
| 148 | [`SuperFreelas/fastapi-google-ads-mcp`](https://github.com/SuperFreelas/fastapi-google-ads-mcp) | 1 | 0 | Python | 2025-04-17 | No description provided |
| 149 | [`PlatAid/google-ads-mcp-cloudrun`](https://github.com/PlatAid/google-ads-mcp-cloudrun) | 0 | 0 | Shell | 2026-07-05 | Team-shared deployment template for hosting the official Goo |
| 150 | [`CoraCote/google-ads-mcp-server`](https://github.com/CoraCote/google-ads-mcp-server) | 1 | 0 | Python | 2026-06-17 | No description provided |
| 151 | [`marketing245/google-ads-mcp-cloud`](https://github.com/marketing245/google-ads-mcp-cloud) | 0 | 0 | JavaScript | 2026-04-03 | No description provided |
| 152 | [`imjustanamateur/google-ads-mcp-server`](https://github.com/imjustanamateur/google-ads-mcp-server) | 0 | 0 | Python | 2026-02-22 | No description provided |
| 153 | [`juanesmb/google-ads-mcp-server`](https://github.com/juanesmb/google-ads-mcp-server) | 0 | 0 | Go | 2026-04-22 | No description provided |
| 154 | [`tolkozin/google-ads-mcp-server`](https://github.com/tolkozin/google-ads-mcp-server) | 0 | 0 | Python | 2026-07-21 | MCP server for Google Ads (Search + App/UAC) with guarded wr |
| 155 | [`folox/mcp-google-ads-app`](https://github.com/folox/mcp-google-ads-app) | 0 | 0 | HTML | 2026-08-21 | No description provided |
| 156 | [`burhan29ee/google-ads-mcp-server`](https://github.com/burhan29ee/google-ads-mcp-server) | 0 | 0 | Python | 2026-08-13 | A Google Ads MCP server with read and write access — GAQL re |
| 157 | [`contentkueche/google-ads-mcp-render`](https://github.com/contentkueche/google-ads-mcp-render) | 0 | 0 | Python | 2026-07-13 | Patched Google Ads MCP for persistent OAuth client storage o |
| 158 | [`phwtsp/google-ads-mcp-cloudflare`](https://github.com/phwtsp/google-ads-mcp-cloudflare) | 0 | 0 | TypeScript | 2026-08-13 | Servidor MCP remoto, somente leitura, para conectar o Google |
| 159 | [`phwtsp/google-ads-mcp-server`](https://github.com/phwtsp/google-ads-mcp-server) | 0 | 0 | Python | 2026-03-10 | No description provided |
| 160 | [`Insightful-Pipe/google-ads-mcp-server`](https://github.com/Insightful-Pipe/google-ads-mcp-server) | 0 | 0 | None | 2026-09-14 | Google Ads MCP server: connect Google Ads to Claude, ChatGPT |
| 161 | [`isaganiesteron/google-ads-mcp-cs`](https://github.com/isaganiesteron/google-ads-mcp-cs) | 0 | 0 | TypeScript | 2026-07-29 | Google Ads MCP server for TypingMind - Access campaigns, per |
| 162 | [`adeshsarwan/google-ads-mcp-client`](https://github.com/adeshsarwan/google-ads-mcp-client) | 0 | 0 | Python | 2026-08-31 | No description provided |
| 163 | [`jomiferse/google-ads-mcp-admin`](https://github.com/jomiferse/google-ads-mcp-admin) | 0 | 0 | Python | 2026-08-30 | No description provided |
| 164 | [`jonathanrinehart/google-ads-library-mcp`](https://github.com/jonathanrinehart/google-ads-library-mcp) | 0 | 0 | Python | 2026-02-25 | No description provided |
| 165 | [`haiquannguyen-ai/pmax-google-ads-mcp`](https://github.com/haiquannguyen-ai/pmax-google-ads-mcp) | 0 | 0 | None | 2026-04-23 | No description provided |
| 166 | [`RoyAzran/google-ads-mcp-server`](https://github.com/RoyAzran/google-ads-mcp-server) | 0 | 0 | Python | 2026-03-23 | No description provided |
| 167 | [`creativedesignseo/google-ads-mcp-nodejs`](https://github.com/creativedesignseo/google-ads-mcp-nodejs) | 0 | 0 | JavaScript | 2026-02-02 | Enhanced Google Ads MCP Server Core in Node.js for Antigravi |
| 168 | [`Matheus-soier/google-ads-mcp-guide`](https://github.com/Matheus-soier/google-ads-mcp-guide) | 0 | 0 | HTML | 2026-03-13 | Guia: Google Ads + Claude Code via MCP — @eusoier |
| 169 | [`molishashah/google-ads-write-mcp`](https://github.com/molishashah/google-ads-write-mcp) | 0 | 1 | TypeScript | 2026-08-20 | MCP server for Google Ads write operations: create RSAs, run |
| 170 | [`YerayRodri/google-ads-kw-mcp`](https://github.com/YerayRodri/google-ads-kw-mcp) | 1 | 0 | Python | 2026-08-30 | No description provided |
| 171 | [`Choizapp/choiz-google-ads-mcp`](https://github.com/Choizapp/choiz-google-ads-mcp) | 0 | 0 | Python | 2026-04-28 | No description provided |
| 172 | [`marketing7s/google-ads-mcp-3`](https://github.com/marketing7s/google-ads-mcp-3) | 0 | 0 | Python | 2026-03-06 | No description provided |
| 173 | [`DS-WEB1/google-ads-mcp-complete`](https://github.com/DS-WEB1/google-ads-mcp-complete) | 0 | 0 | Python | 2026-09-02 | No description provided |
| 174 | [`jeison-platah/platah-google-ads-mcp`](https://github.com/jeison-platah/platah-google-ads-mcp) | 0 | 0 | Python | 2026-08-12 | No description provided |
| 175 | [`AleemHaider/google-ads-manager-mcp`](https://github.com/AleemHaider/google-ads-manager-mcp) | 0 | 0 | TypeScript | 2026-08-13 | Unofficial MCP server for reading and managing Google Ads ac |
| 176 | [`georgebrinckmann/google-ads-mcp-write`](https://github.com/georgebrinckmann/google-ads-mcp-write) | 0 | 0 | Python | 2026-07-20 | No description provided |
| 177 | [`ahhhcantagalo/ahhhcantagalo-google-ads-mcp`](https://github.com/ahhhcantagalo/ahhhcantagalo-google-ads-mcp) | 0 | 0 | Python | 2026-03-11 | No description provided |
| 178 | [`martechery/mcp-google-ads-ts`](https://github.com/martechery/mcp-google-ads-ts) | 0 | 0 | TypeScript | 2025-09-15 | No description provided |
| 179 | [`Malvisse-Silverhand/claude-google-ads-mcp`](https://github.com/Malvisse-Silverhand/claude-google-ads-mcp) | 0 | 0 | Python | 2026-09-07 | No description provided |
| 180 | [`Raffaele86/adsense-mcp`](https://github.com/Raffaele86/adsense-mcp) | 0 | 0 | Python | 2026-07-08 | Google AdSense MCP server (revenue/reporting) |
| 181 | [`n-asuy/_gads`](https://github.com/n-asuy/_gads) | 0 | 0 | Rust | 2026-02-11 | Google Ads MCP server & CLI |
| 182 | [`Milastream/google-ads-transparency-mcp-server`](https://github.com/Milastream/google-ads-transparency-mcp-server) | 0 | 0 | None | 2026-06-25 | Apify actor: google-ads-transparency-mcp-server |
| 183 | [`salnikova-web/google-ads-mcp-extended-private`](https://github.com/salnikova-web/google-ads-mcp-extended-private) | 0 | 0 | Python | 2026-08-28 | No description provided |
| 184 | [`revspace7777/google-ads-mcp-official_main`](https://github.com/revspace7777/google-ads-mcp-official_main) | 0 | 0 | Python | 2025-11-18 | No description provided |
| 185 | [`vibeads/mcp`](https://github.com/vibeads/mcp) | 0 | 0 | TypeScript | 2026-09-04 | MCP Server for VibeAds — talk to your Google Ads from Claude |
| 186 | [`treetank-net/google-ads-baby`](https://github.com/treetank-net/google-ads-baby) | 0 | 0 | JavaScript | 2026-08-19 | MCP server for safe and secure campaign management in claude |
| 187 | [`onlyzmmr-source/google-ads-reporting`](https://github.com/onlyzmmr-source/google-ads-reporting) | 0 | 0 | None | 2026-07-22 | Read-only Google Ads reporting workflow built on the officia |
| 188 | [`phanindraintelligenzit-afk/mcp-server-for-google-ads-meta-ads-ga4`](https://github.com/phanindraintelligenzit-afk/mcp-server-for-google-ads-meta-ads-ga4) | 0 | 0 | Python | 2026-06-29 | MCP Server for Google Ads Meta Ads GA4. Built by AIdentify — |
| 189 | [`arshow/google-ads-analytics-dashboard`](https://github.com/arshow/google-ads-analytics-dashboard) | 0 | 0 | TypeScript | 2026-07-27 | Internal Google Ads analytics dashboard powered by the Googl |
| 190 | [`ceotind/open-google-mcp`](https://github.com/ceotind/open-google-mcp) | 0 | 1 | Python | 2026-08-24 | Feed data from Google Ads, G4 Analytics and Google Search Co |
| 191 | [`gabriele81benedetti/Antigravity-google-ads-mcp-for-windows`](https://github.com/gabriele81benedetti/Antigravity-google-ads-mcp-for-windows) | 0 | 0 | Python | 2026-02-19 | Antigraviti configuration to use google ads mcp server via a |
| 192 | [`mugheerasadiq-astera/google-ads-ga4-mcp-gateway`](https://github.com/mugheerasadiq-astera/google-ads-ga4-mcp-gateway) | 0 | 0 | Python | 2026-05-13 | No description provided |
| 193 | [`robinhoodanalytics/ra-google-ads-mcp-v23`](https://github.com/robinhoodanalytics/ra-google-ads-mcp-v23) | 0 | 0 | Python | 2026-02-17 | Google Ads API v23 MCP server for Claude Desktop. OAuth 2.0  |
| 194 | [`ElMonarca-ldz/google-ads-wrapper`](https://github.com/ElMonarca-ldz/google-ads-wrapper) | 0 | 0 | Python | 2026-08-16 | Wrapper HTTP (FastAPI) para google-ads-transparency-mcp — st |
| 195 | [`Synter-Media-AI/google-ads-agent`](https://github.com/Synter-Media-AI/google-ads-agent) | 0 | 0 | None | 2026-03-23 | Manage Google Ads campaigns with AI agents via MCP (Amp, Cur |
| 196 | [`Raffaele86/keyword-planner-mcp`](https://github.com/Raffaele86/keyword-planner-mcp) | 0 | 0 | Python | 2026-07-08 | Google Ads Keyword Planner MCP server (KeywordPlanIdeaServic |
| 197 | [`danielpopamd/google-ads-assistant`](https://github.com/danielpopamd/google-ads-assistant) | 0 | 0 | None | 2026-06-21 | Google Ads Assistant: connect your AI assistant to Google Ad |
| 198 | [`wilderness-interactive/herald`](https://github.com/wilderness-interactive/herald) | 0 | 0 | Rust | 2026-04-30 | Sovereign ad intelligence MCP server — Google Ads data tools |
| 199 | [`pijusz/mcp-gads`](https://github.com/pijusz/mcp-gads) | 1 | 0 | TypeScript | 2026-07-31 | Google Ads MCP server — query campaigns, keywords, assets &  |
| 200 | [`Xaena53/xaena53.github.io`](https://github.com/Xaena53/xaena53.github.io) | 0 | 0 | HTML | 2026-08-13 | AdsPilot project site and privacy policy — safety-gated Goog |
| 201 | [`rablab-mtl/mcp-gads`](https://github.com/rablab-mtl/mcp-gads) | 0 | 0 | TypeScript | 2026-06-17 | Read-only Google Ads MCP server on Cloudflare Workes. Built  |
| 202 | [`aiebrain/google-ads-demandgen-kit`](https://github.com/aiebrain/google-ads-demandgen-kit) | 0 | 0 | Python | 2026-07-11 | Claude Code로 Google Ads 디멘드젠 광고 생성 — UI 코파일럿(A) + API/MCP 자동 |
| 203 | [`lucagalvani/google-ads-agent`](https://github.com/lucagalvani/google-ads-agent) | 0 | 0 | Python | 2026-09-08 | MCP server and autonomous agent for Google Ads Search: polic |
| 204 | [`digitalmakery/digitalmakery-google-ads`](https://github.com/digitalmakery/digitalmakery-google-ads) | 0 | 0 | Makefile | 2026-08-28 | Sets up a Google Ads MCP server inside a Docker container to |
| 205 | [`eneelkant/google-ads-claude-plugin`](https://github.com/eneelkant/google-ads-claude-plugin) | 1 | 0 | Python | 2026-08-21 | Claude Cowork MCP plugin for managing Google Ads campaigns,  |
| 206 | [`praveengp-git/google-ads-ai-manager`](https://github.com/praveengp-git/google-ads-ai-manager) | 0 | 0 | Python | 2026-05-10 | Manage Google Ads with AI. MCP for reads, dated Python scrip |
| 207 | [`trackdolphin/mcp`](https://github.com/trackdolphin/mcp) | 0 | 0 | TypeScript | 2026-09-11 | Trackdolphin MCP server & CLI — server-side conversion track |
| 208 | [`sunamtaran92-a11y/google-ads-api-tools`](https://github.com/sunamtaran92-a11y/google-ads-api-tools) | 0 | 0 | Python | 2026-07-21 | Private MCP server exposing the Google Ads API to Claude for |
| 209 | [`jisimonslabolsa/mcp_googleads`](https://github.com/jisimonslabolsa/mcp_googleads) | 0 | 0 | Dockerfile | 2026-06-18 | No description provided |
| 210 | [`rohanbuild/googleads-mcp`](https://github.com/rohanbuild/googleads-mcp) | 0 | 0 | None | 2026-09-21 | No description provided |
| 211 | [`primrose-mcp/primrose-mcp-googleads`](https://github.com/primrose-mcp/primrose-mcp-googleads) | 0 | 0 | TypeScript | 2026-01-30 | No description provided |
| 212 | [`crlcrlcrlcrl/sinos-mcp-googleads`](https://github.com/crlcrlcrlcrl/sinos-mcp-googleads) | 0 | 0 | JavaScript | 2026-07-02 | No description provided |
| 213 | [`sujayrittikar/adsmith`](https://github.com/sujayrittikar/adsmith) | 0 | 0 | Python | 2026-08-07 | Google Ads MCP server that can actually change your ads — wi |
| 214 | [`bryangoncalvespro-hub/google-tag-manager-mcp-server`](https://github.com/bryangoncalvespro-hub/google-tag-manager-mcp-server) | 0 | 0 | TypeScript | 2026-04-21 | MCP server for Google Tag Manager API v2 — 15 tools includin |
| 215 | [`backspacevenkat/algoads`](https://github.com/backspacevenkat/algoads) | 0 | 0 | TypeScript | 2026-04-22 | Retention-safe YouTube ad launcher — Next.js 16 + Google Ads |
| 216 | [`Bmiller4evr/google-marketing-mcp`](https://github.com/Bmiller4evr/google-marketing-mcp) | 0 | 0 | TypeScript | 2026-07-20 | Read-only MCP server for the Google Ads API: campaigns, metr |
| 217 | [`HarrisonHesslink/burnr8`](https://github.com/HarrisonHesslink/burnr8) | 1 | 1 | Python | 2026-09-12 | Stop burning money on Google Ads. Manage everything from you |
| 218 | [`optiwebopz/optimcp`](https://github.com/optiwebopz/optimcp) | 0 | 0 | JavaScript | 2026-04-10 | Self-hosted MCP server suite for Claude — file access, MySQL |
| 219 | [`lionkiii/gads-transparency-mcp`](https://github.com/lionkiii/gads-transparency-mcp) | 1 | 0 | TypeScript | 2026-03-09 | MCP server for Google Ads Transparency Center — research com |
| 220 | [`marilynceo/adwise-mcp`](https://github.com/marilynceo/adwise-mcp) | 0 | 0 | None | 2026-05-19 | AI Agent Ad Spend Manager u2014 manage Google Ads campaigns, |
| 221 | [`cpinto/mcp--google-adwords`](https://github.com/cpinto/mcp--google-adwords) | 0 | 0 | Python | 2026-03-22 | No description provided |
| 222 | [`codeChap/mcp-server-google-adwords`](https://github.com/codeChap/mcp-server-google-adwords) | 0 | 0 | Rust | 2026-08-26 | No description provided |
| 223 | [`CDataSoftware/google-adwords-mcp-server-by-cdata`](https://github.com/CDataSoftware/google-adwords-mcp-server-by-cdata) | 1 | 0 | Java | 2025-10-18 | This read-only MCP Server allows you to connect to Google Ad |
| 224 | [`LuanVelo/mcp-mkt-gads`](https://github.com/LuanVelo/mcp-mkt-gads) | 0 | 0 | Python | 2026-04-14 | Servidor MCP local para integrar o Claude com a Google Ads A |
| 225 | [`abjohnson5f/ppc-intel-agent`](https://github.com/abjohnson5f/ppc-intel-agent) | 0 | 1 | TypeScript | 2026-01-12 | Autonomous PPC Management Agent - Create Google Ads campaign |
| 226 | [`zeisoft/heymetra-mcp`](https://github.com/zeisoft/heymetra-mcp) | 0 | 0 | None | 2026-09-19 | Remote MCP server for marketing and revenue data — ads, anal |
| 227 | [`nowork-studio/adsagent-mcp`](https://github.com/nowork-studio/adsagent-mcp) | 0 | 0 | None | 2026-03-26 | Connect your Google Ads to Claude, Codex, or any MCP-compati |
| 228 | [`goagentcy/agentcy-connect`](https://github.com/goagentcy/agentcy-connect) | 4 | 0 | Shell | 2026-04-12 | A managed AI marketing agent that plugs into all your AI too |
| 229 | [`romek-rozen/bdos-ai-extensions`](https://github.com/romek-rozen/bdos-ai-extensions) | 5 | 1 | Python | 2026-07-02 | Community extensions for BDOS AI (Google Ads management) - w |
| 230 | [`amekala/ads-mcp`](https://github.com/amekala/ads-mcp) | 94 | 19 | Jupyter Notebook | 2026-09-13 | MCP server for managing ad campaigns across Google Ads, Meta |
| 231 | [`markifact/markifact-mcp`](https://github.com/markifact/markifact-mcp) | 48 | 8 | Shell | 2026-09-20 | MCP server for Google Ads, Meta Ads, GA4, TikTok Ads, and Li |
| 232 | [`Draivix/aidvertaiser`](https://github.com/Draivix/aidvertaiser) | 20 | 7 | Python | 2026-09-16 | AI-powered advertising management MCP server — 180+ tools ac |
| 233 | [`irinabuht12-oss/n8n-google-meta-ads`](https://github.com/irinabuht12-oss/n8n-google-meta-ads) | 6 | 3 | None | 2026-09-09 | n8n workflows: AI agent on your Google Ads + Meta Ads via th |
| 234 | [`itallstartedwithaidea/advertising-hub`](https://github.com/itallstartedwithaidea/advertising-hub) | 42 | 17 | Markdown | 2026-08-20 | The open-source one-stop shop for advertising platform APIs, |
| 235 | [`adkit/ads-mcp`](https://github.com/adkit/ads-mcp) | 13 | 0 | None | 2026-09-06 | Ads MCP - manage Google, Meta, TikTok, LinkedIn, Microsoft,  |
| 236 | [`Harungokc/ai-ads-manager-kit`](https://github.com/Harungokc/ai-ads-manager-kit) | 7 | 0 | None | 2026-06-14 | Open-source AI Ads Manager Kit — Claude Code, n8n, MCP. 600+ |
| 237 | [`channel47/mcps`](https://github.com/channel47/mcps) | 4 | 1 | JavaScript | 2026-07-11 | MCP servers for Google Ads, Bing Ads, and Meta Ads by Channe |
| 238 | [`amekala/adspirer-mcp-plugin`](https://github.com/amekala/adspirer-mcp-plugin) | 5 | 0 | None | 2026-08-04 | Adspirer MCP plugin for Claude Code - cross-platform ad mana |
| 239 | [`MAhmed004/ad-ops-mcp-hub`](https://github.com/MAhmed004/ad-ops-mcp-hub) | 2 | 2 | HTML | 2026-09-21 | AI-Powered Ads Manager 2026: Google, Meta, TikTok & LinkedIn |
| 240 | [`twominutereports/twominutereports-mcp`](https://github.com/twominutereports/twominutereports-mcp) | 3 | 0 | None | 2026-04-20 | Analyse SEO, PPC, E-Commerce from 30+ marketing sources. Con |
| 241 | [`fourdots/Google-Marketing-MCPs-G.Ads-GA4-GSC-GTM`](https://github.com/fourdots/Google-Marketing-MCPs-G.Ads-GA4-GSC-GTM) | 3 | 1 | Python | 2026-08-22 | 146 tools across 4 Google MCP servers (Ads, GA4, Search Cons |
| 242 | [`HYPD-AI/ads-mcp-plugin`](https://github.com/HYPD-AI/ads-mcp-plugin) | 2 | 1 | None | 2026-08-24 | HYPD AI plugin for Claude Code and Cowork. Google Ads, Meta  |
| 243 | [`itallstartedwithaidea/ad-creative-mcp`](https://github.com/itallstartedwithaidea/ad-creative-mcp) | 4 | 0 | JavaScript | 2026-03-18 | MCP server that validates, resizes, and optimizes advertisin |
| 244 | [`adcrunchdev/mcp`](https://github.com/adcrunchdev/mcp) | 1 | 0 | None | 2026-06-11 | Ask AI about your ads — remote MCP server connecting Meta, T |
| 245 | [`DaisukeHori/ad-ops-mcp`](https://github.com/DaisukeHori/ad-ops-mcp) | 0 | 0 | TypeScript | 2026-04-17 | 広告運用オートメーション MCP サーバー (Google Ads / Meta Ads / GBP / X Ads) |
| 246 | [`christophertanenso/mcp-marketing-analytics`](https://github.com/christophertanenso/mcp-marketing-analytics) | 0 | 0 | TypeScript | 2026-02-26 | MCP server giving Claude access to GA4, Google Search Consol |
| 247 | [`ryohasegawaaduno-crypto/ads-mcp-server`](https://github.com/ryohasegawaaduno-crypto/ads-mcp-server) | 0 | 0 | JavaScript | 2026-04-13 | Meta Ads + Google Ads MCP Server for Claude Code / Claude De |
| 248 | [`1clickreport/mcp`](https://github.com/1clickreport/mcp) | 0 | 0 | None | 2026-09-13 | 1ClickReport MCP Server — 75 tools for marketing analytics,  |
| 249 | [`Ryzon-Performance-Sports-Apparel/mcp-hub`](https://github.com/Ryzon-Performance-Sports-Apparel/mcp-hub) | 0 | 0 | Shell | 2026-06-01 | Unified installer for Meta Ads & Google Ads MCP servers for  |
| 250 | [`openairlabs/flyweel-mcp-deep-ad-analysis`](https://github.com/openairlabs/flyweel-mcp-deep-ad-analysis) | 2 | 0 | None | 2026-03-11 |   Analyse Google Ads and Meta Ads with the Flyweel MCP. Batc |
| 251 | [`automatiabcn/adops-mcp`](https://github.com/automatiabcn/adops-mcp) | 0 | 0 | TypeScript | 2026-09-13 | AI-powered cross-platform ad management MCP server for Googl |
| 252 | [`igor1000rr/ads-mcp`](https://github.com/igor1000rr/ads-mcp) | 0 | 0 | JavaScript | 2026-07-12 | MCP-комбайн рекламы на Cloudflare Workers: Яндекс Директ + V |
| 253 | [`jhatfield80/hattysites-mcp`](https://github.com/jhatfield80/hattysites-mcp) | 0 | 0 | Python | 2026-07-03 | Hatty.ai MCP Server — Agentic Google Ads & Meta Ads automati |
| 254 | [`cdgutierrez6/mcp-reportes`](https://github.com/cdgutierrez6/mcp-reportes) | 0 | 0 | Python | 2026-07-31 | Servidor MCP para reportes automáticos de marketing digital  |
| 255 | [`adrex-ai/adrex-ai`](https://github.com/adrex-ai/adrex-ai) | 3 | 0 | TypeScript | 2026-09-08 | Open-source MCP server to manage Google Ads from Claude, Cur |
| 256 | [`superbolt-x/Talk-to-Google-SB-remote`](https://github.com/superbolt-x/Talk-to-Google-SB-remote) | 0 | 0 | Python | 2026-07-22 | AdLoop MCP server (Google Ads + GA4) — remote Railway deploy |
| 257 | [`cfelipemoreira/ads-manager`](https://github.com/cfelipemoreira/ads-manager) | 0 | 0 | JavaScript | 2026-06-05 | Sistema de gestão de campanhas Meta Ads e Google Ads via Cla |
| 258 | [`gnoah241201/ga4-mcp`](https://github.com/gnoah241201/ga4-mcp) | 0 | 0 | TypeScript | 2026-05-21 | MCP server for Google Analytics 4 — run reports, realtime, f |
| 259 | [`opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms`](https://github.com/opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms) | 0 | 0 | None | 2026-09-21 | Hosted MCP connector to manage Google Ads, Meta Ads, Microso |
| 260 | [`zurychhh/genactiv-klaviyo`](https://github.com/zurychhh/genactiv-klaviyo) | 0 | 0 | HTML | 2026-09-11 | GenActiv Online — AI marketing assistant with 6 MCP integrat |
| 261 | [`AINative-Studio/ainative-gtm-mcp`](https://github.com/AINative-Studio/ainative-gtm-mcp) | 0 | 0 | TypeScript | 2026-08-01 | The Google Ads + Analytics + Tag Manager MCP for AI agents — |
| 262 | [`AgenticAdvertising/adside-mcp`](https://github.com/AgenticAdvertising/adside-mcp) | 1 | 1 | None | 2026-07-28 | Adside MCP server — AI agents that manage paid ads on Meta,  |
| 263 | [`RoyAzran/mcp-ads`](https://github.com/RoyAzran/mcp-ads) | 1 | 0 | Python | 2026-09-07 | The open-source marketing MCP server -- Google Ads, Meta Ads |
| 264 | [`PaidSync/paidsync-mcp-examples`](https://github.com/PaidSync/paidsync-mcp-examples) | 0 | 0 | None | 2026-04-08 | Example configurations and prompts for PaidSync.ai MCP serve |
| 265 | [`jmacaggi-gfm/ads-mcp-server`](https://github.com/jmacaggi-gfm/ads-mcp-server) | 0 | 0 | Python | 2026-08-05 | Local MCP server exposing Google Ads + Meta Marketing data t |
| 266 | [`ynnickw/adport`](https://github.com/ynnickw/adport) | 6 | 7 | TypeScript | 2026-09-19 | Open-source multi-platform ads management for AI agents — co |
| 267 | [`Mohit4022-cloud/Marketing-Automation-MCP-Server`](https://github.com/Mohit4022-cloud/Marketing-Automation-MCP-Server) | 3 | 4 | Python | 2026-04-15 | 🚀 AI-powered marketing automation with 75% time reduction &  |
| 268 | [`getDynamoi/mcp`](https://github.com/getDynamoi/mcp) | 3 | 1 | TypeScript | 2026-09-20 | Promote music on Spotify and grow YouTube channels through A |
| 269 | [`bfroos/myhb-ads-mcp`](https://github.com/bfroos/myhb-ads-mcp) | 0 | 0 | Python | 2026-06-25 | Google Ads MCP Server for My Health & Beauty (30 tools, Clau |
| 270 | [`at-dan/ad-library-mcp`](https://github.com/at-dan/ad-library-mcp) | 0 | 0 | TypeScript | 2026-04-16 | MCP server for searching competitor ads across Meta Ad Libra |
| 271 | [`thidebrito/hotmart-mcp`](https://github.com/thidebrito/hotmart-mcp) | 0 | 0 | JavaScript | 2026-05-07 | MCP server for Claude Code + Vercel webhook → Meta CAPI + Go |
| 272 | [`DanielSylvester/marketing-ops-mcp`](https://github.com/DanielSylvester/marketing-ops-mcp) | 0 | 0 | TypeScript | 2026-09-05 | MCP server for Meta Ads + Google Ads operations. Campaign in |
| 273 | [`thedavidquan01/ad-library-mcp`](https://github.com/thedavidquan01/ad-library-mcp) | 1 | 0 | TypeScript | 2026-05-25 | Zero-auth MCP server for searching competitor ads across Met |
| 274 | [`Jluethke/marketing-mcp`](https://github.com/Jluethke/marketing-mcp) | 0 | 0 | Python | 2026-06-22 | Multi-channel marketing MCP server: Google Ads, Meta Ads, GA |
| 275 | [`Adsroid/adsroid-mcp`](https://github.com/Adsroid/adsroid-mcp) | 0 | 0 | None | 2026-08-26 | Documentation for Adsroid MCP — connect Claude, ChatGPT, and |
| 276 | [`Overcast-Solutions/ads-mcp`](https://github.com/Overcast-Solutions/ads-mcp) | 0 | 0 | Python | 2026-09-19 | Self-hosted Google Ads MCP server with operator-owned OAuth, |
| 277 | [`Insightful-Pipe/ads-libraries-mcp-server`](https://github.com/Insightful-Pipe/ads-libraries-mcp-server) | 0 | 0 | None | 2026-09-14 | Ads Libraries MCP server: connect Ads Libraries to Claude, C |
| 278 | [`Daubthi/attache-mcp`](https://github.com/Daubthi/attache-mcp) | 1 | 0 | None | 2026-08-06 | Docs for Attaché — a hosted, multi-tenant MCP server giving  |
| 279 | [`mharnett/mcp-marketing-suite`](https://github.com/mharnett/mcp-marketing-suite) | 1 | 0 | TypeScript | 2026-09-04 | Production MCP servers for performance marketing: Google Ads |
| 280 | [`Agent-Prod/muze-mcp-connector`](https://github.com/Agent-Prod/muze-mcp-connector) | 0 | 0 | None | 2026-07-24 | Public connector manifest + docs for the hosted Muze MCP ser |
| 281 | [`Dweeb1578/marketing-analytics-mcp`](https://github.com/Dweeb1578/marketing-analytics-mcp) | 0 | 0 | Python | 2026-06-29 | MCP server giving an LLM live read-only access to a marketin |
| 282 | [`ad-vertly/adextract-mcp-server`](https://github.com/ad-vertly/adextract-mcp-server) | 0 | 0 | HTML | 2026-08-30 | MCP server for AI agents - search Meta, Google Ads, LinkedIn |
| 283 | [`loomascale/ads-mcp`](https://github.com/loomascale/ads-mcp) | 0 | 0 | Java | 2026-09-07 | Self-hostable MCP server for Google Ads. Let ChatGPT or Clau |
| 284 | [`SHAHINOOOO/whathead-mcp`](https://github.com/SHAHINOOOO/whathead-mcp) | 0 | 0 | Shell | 2026-07-11 | Manage paid media across Meta, Google, TikTok, Snapchat, Ama |
| 285 | [`teachskillofskills-ai/TechshuMCP`](https://github.com/teachskillofskills-ai/TechshuMCP) | 0 | 0 | JavaScript | 2026-05-06 | SyncMaster is a deploy-ready MCP hub that connects Google Ad |
| 286 | [`converlyio/converly-mcp`](https://github.com/converlyio/converly-mcp) | 0 | 0 | None | 2026-08-18 | MCP server for setting up server-side conversion tracking. S |
| 287 | [`code-ashish-singh/ai-marketing-server`](https://github.com/code-ashish-singh/ai-marketing-server) | 0 | 0 | JavaScript | 2026-07-11 | Node.js & Express.js backend API server for the AI Marketing |
| 288 | [`alexpilotto/splitlaunch-dev`](https://github.com/alexpilotto/splitlaunch-dev) | 0 | 0 | None | 2026-07-23 | Package-first A/B testing MCP server for PPC and paid social |
| 289 | [`RoASr-com/roasr-mcp`](https://github.com/RoASr-com/roasr-mcp) | 0 | 0 | TypeScript | 2026-08-04 | MCP server for RoASr — connect Claude, ChatGPT, Codex or Cur |
| 290 | [`trackian/cursor-plugin`](https://github.com/trackian/cursor-plugin) | 0 | 0 | JavaScript | 2026-05-13 | Official Cursor plugin for Trackian. Brings GA4, Facebook Ad |
| 291 | [`trackian/claude-plugin`](https://github.com/trackian/claude-plugin) | 0 | 0 | JavaScript | 2026-05-13 | Official Claude Code plugin for Trackian. Brings GA4, Facebo |
| 292 | [`Casius999/quantum-ads-mcp`](https://github.com/Casius999/quantum-ads-mcp) | 0 | 0 | Python | 2026-08-05 | Sovereign Google marketing-agency control plane over MCP — 2 |
| 293 | [`PaidSync/paidsync-mcp`](https://github.com/PaidSync/paidsync-mcp) | 3 | 1 | None | 2026-09-01 | 460+ tools across 14 ad platforms via one MCP endpoint. Full |
| 294 | [`traffiy/paidsync-mcp`](https://github.com/traffiy/paidsync-mcp) | 2 | 0 | None | 2026-05-11 | [Moved] Canonical home is github.com/PaidSync/paidsync-mcp |
| 295 | [`samarthanalytics-sj/samarth-analytics-mcp`](https://github.com/samarthanalytics-sj/samarth-analytics-mcp) | 2 | 0 | TypeScript | 2026-09-21 | MCP server for Samarth Analytics Google Tag Manager operatio |
| 296 | [`somosmaqui/maqui-mcp`](https://github.com/somosmaqui/maqui-mcp) | 0 | 0 | None | 2026-07-08 | All-in-one marketing analytics MCP — Instagram, ads, web tra |
| 297 | [`vizuh/clicktrail-mcp`](https://github.com/vizuh/clicktrail-mcp) | 0 | 0 | JavaScript | 2026-09-16 | MCP stdio server for ClickTrail attribution schemas, diagnos |
| 298 | [`Insightful-Pipe/insightfulpipe-mcp-server`](https://github.com/Insightful-Pipe/insightfulpipe-mcp-server) | 0 | 0 | None | 2026-09-14 | InsightfulPipe MCP server: connect InsightfulPipe to Claude, |
| 299 | [`maximskorohod/roasr-mcp`](https://github.com/maximskorohod/roasr-mcp) | 0 | 0 | TypeScript | 2026-06-16 | MCP server for RoASr — Meta/Google ad-audit findings, KPIs,  |
| 300 | [`arcticgreyy/paid-media-mcp`](https://github.com/arcticgreyy/paid-media-mcp) | 0 | 0 | TypeScript | 2026-06-10 | MCP server template for paid media teams — connect Claude to |
| 301 | [`auditsocials/auditsocials-compliance-mcp`](https://github.com/auditsocials/auditsocials-compliance-mcp) | 0 | 0 | TypeScript | 2026-09-16 | Pre-publish compliance check for AI-generated social & ad co |
| 302 | [`Ryze-AI-Adgent/cursor-plugin`](https://github.com/Ryze-AI-Adgent/cursor-plugin) | 0 | 0 | None | 2026-09-21 | Ryze AI Cursor plugin: Google Ads, Meta Ads, GA4, Search Con |
| 303 | [`The-Detail-Department/ai-paid-media-tools`](https://github.com/The-Detail-Department/ai-paid-media-tools) | 0 | 0 | JavaScript | 2026-09-05 | Production-readiness index for AI paid-media tools, advertis |
| 304 | [`faiyazmn/ad-analytics`](https://github.com/faiyazmn/ad-analytics) | 0 | 0 | Shell | 2026-06-11 | Cross-channel ad analytics workspace for Claude Code: Google |
| 305 | [`lucaspaesbrazil-lab/agencia-digital-showcase`](https://github.com/lucaspaesbrazil-lab/agencia-digital-showcase) | 0 | 0 | None | 2026-07-27 | Sistema de gestao de trafego pago e organico em Claude Code  |
| 306 | [`advisorppc-org/advisorppc-plugin`](https://github.com/advisorppc-org/advisorppc-plugin) | 0 | 0 | None | 2026-08-28 | Official AdvisorPPC plugin for Claude Code — audit and manag |
| 307 | [`redwoodmeridian/ranql-skills`](https://github.com/redwoodmeridian/ranql-skills) | 1 | 0 | None | 2026-07-24 | Claude Code plugin: turn Claude into your law firm's marketi |
| 308 | [`benheis/ads-mcp-connector`](https://github.com/benheis/ads-mcp-connector) | 1 | 0 | Python | 2026-04-23 | Connect Claude Code to Meta Ads and Google Ads. One-command  |
| 309 | [`kiarashedraki/google-ads-mcp`](https://github.com/kiarashedraki/google-ads-mcp) | 0 | 0 | TypeScript | 2025-10-12 | Single-commit scaffold with no tests, no documentation, and zero maintenance since creation |
| 310 | [`Lazare-42/google-ads-mcp`](https://github.com/Lazare-42/google-ads-mcp) | 0 | 0 | Rust | 2025-11-04 | Incomplete 5-commit Rust scaffold with broken gRPC stubs |
| 311 | [`zelentsov-dev/google-ads-mcp`](https://github.com/zelentsov-dev/google-ads-mcp) | 0 | 0 | Python | 2025-09-18 | Minimal 4-commit script without tests or active usage |
| 312 | [`x777/mcp-google-ads`](https://github.com/x777/mcp-google-ads) | 1 | 0 | Python | 2025-10-22 | 2-commit prototype without error handling or active maintenance |
| 313 | [`yeswanthreddyk/Google-ads-MCP`](https://github.com/yeswanthreddyk/Google-ads-MCP) | 0 | 0 | Python | 2025-10-15 | 2-commit prototype redundant with established FastMCP servers |
| 314 | [`ThainaJardim/google-ads-mcp`](https://github.com/ThainaJardim/google-ads-mcp) | 0 | 0 | Python | 2025-10-09 | 2-commit prototype with only 3 basic tools |

### Category: `EMPTY_OR_UNMODIFIED_FORK` (1 repository)

| # | Repository | Stars | Forks | Language | Last Push | Exclusion Reason |
|---|---|---|---|---|---|---|
| 1 | [`iflow-mcp/itallstartedwithaidea-google-ads-mcp`](https://github.com/iflow-mcp/itallstartedwithaidea-google-ads-mcp) | 0 | 0 | Python | 2026-04-14 | Exact downstream fork duplicate of itallstartedwithaidea/google-ads-mcp with zero architectural divergence |

### Category: `NON_MCP_STANDALONE_SCRIPT` (30 repositories)

| # | Repository | Stars | Forks | Language | Last Push | Exclusion Reason |
|---|---|---|---|---|---|---|
| 1 | [`DataLeadsPRO/google-ads-transparency`](https://github.com/DataLeadsPRO/google-ads-transparency) | 0 | 0 | Python | 2026-09-17 | No description provided |
| 2 | [`khanmo248/open-seo`](https://github.com/khanmo248/open-seo) | 0 | 0 | None | 2026-09-21 | Manage your SEO data with this open-source tool. Connect you |
| 3 | [`unempyd/revenueos`](https://github.com/unempyd/revenueos) | 7 | 0 | Python | 2026-09-14 | Connect your business. RevenueOS finds opportunities, execut |
| 4 | [`egoring/adpolicy-precheck`](https://github.com/egoring/adpolicy-precheck) | 0 | 0 | Python | 2026-09-17 | 광고 집행 전 정책 위반을 잡아내는 사전 점검 시스템 |
| 5 | [`orbotshq/google-ads-transparency-scraper`](https://github.com/orbotshq/google-ads-transparency-scraper) | 0 | 0 | None | 2026-09-06 | Google Ads Transparency Center Scraper on Apify: every ad an |
| 6 | [`googleads/google-ads-api-developer-assistant`](https://github.com/googleads/google-ads-api-developer-assistant) | 99 | 14 | Python | 2026-09-16 | No description provided |
| 7 | [`itallstartedwithaidea/google-ads-api-agent`](https://github.com/itallstartedwithaidea/google-ads-api-agent) | 29 | 12 | Python | 2026-07-17 | The Agent is an enterprise-grade Google Ads management agent |
| 8 | [`plasdigital/google-ads-kit-aluno`](https://github.com/plasdigital/google-ads-kit-aluno) | 4 | 4 | Python | 2026-09-14 | Opere sua conta de Google Ads conversando em portugues com o |
| 9 | [`mardab96/google-ads-skills`](https://github.com/mardab96/google-ads-skills) | 7 | 3 | Python | 2026-08-04 | No description provided |
| 10 | [`eliasmalmsandberg/google-ads-skills`](https://github.com/eliasmalmsandberg/google-ads-skills) | 14 | 0 | None | 2026-07-27 | No description provided |
| 11 | [`optmyzr-skills/google-ads-audit`](https://github.com/optmyzr-skills/google-ads-audit) | 12 | 0 | None | 2026-05-04 | Do a full audit of your Google Ads PPC account |
| 12 | [`itsAR-VR/google-ads-cowork-OS`](https://github.com/itsAR-VR/google-ads-cowork-OS) | 5 | 1 | TypeScript | 2026-03-25 | No description provided |
| 13 | [`universal-mcp/google-ads`](https://github.com/universal-mcp/google-ads) | 1 | 0 | Shell | 2025-06-14 | No description provided |
| 14 | [`openclaw-mcp-vps/google-ads-budget-optimizer`](https://github.com/openclaw-mcp-vps/google-ads-budget-optimizer) | 0 | 0 | TypeScript | 2026-05-05 | OpenClaw auto-generated tool: google-ads-budget-optimizer |
| 15 | [`openclaw-mcp-vps/google-ads-waste-scanner`](https://github.com/openclaw-mcp-vps/google-ads-waste-scanner) | 0 | 0 | TypeScript | 2026-06-07 | OpenClaw auto-generated tool: google-ads-waste-scanner |
| 16 | [`openclaw-mcp-vps/google-ads-competitor-bid-tracker`](https://github.com/openclaw-mcp-vps/google-ads-competitor-bid-tracker) | 0 | 0 | TypeScript | 2026-05-28 | OpenClaw auto-generated tool: google-ads-competitor-bid-trac |
| 17 | [`openclaw-mcp-vps/google-ads-negative-keyword-miner`](https://github.com/openclaw-mcp-vps/google-ads-negative-keyword-miner) | 0 | 0 | TypeScript | 2026-05-03 | OpenClaw auto-generated tool: google-ads-negative-keyword-mi |
| 18 | [`openclaw-mcp-vps/google-ads-negative-keyword-finder`](https://github.com/openclaw-mcp-vps/google-ads-negative-keyword-finder) | 0 | 0 | TypeScript | 2026-05-08 | OpenClaw auto-generated tool: google-ads-negative-keyword-fi |
| 19 | [`logly/mureo`](https://github.com/logly/mureo) | 44 | 6 | Python | 2026-09-21 | Your local-first AI ad ops crew. Works with Claude Code, Cur |
| 20 | [`adplane/claude-plugin`](https://github.com/adplane/claude-plugin) | 0 | 0 | Python | 2026-09-11 | Adplane plugin for Claude: Google Ads and Meta Ads reporting |
| 21 | [`lumination-ai-ltd/paid-ads-autopilot`](https://github.com/lumination-ai-ltd/paid-ads-autopilot) | 0 | 0 | None | 2026-03-26 | Claude Code plugin for managing Google Ads, Meta Ads, and Ap |
| 22 | [`Aditi-Bahalkar/ads-autopilot-llm-agent`](https://github.com/Aditi-Bahalkar/ads-autopilot-llm-agent) | 1 | 0 | HTML | 2026-09-21 | AI-Powered Paid Ads Optimizer 2026 - Google, Meta & Apple Se |
| 23 | [`converlyio/converly-cli`](https://github.com/converlyio/converly-cli) | 0 | 0 | JavaScript | 2026-08-18 | Command line tool for Converly conversion tracking — set up  |
| 24 | [`uppifyagency/seo-master-2026`](https://github.com/uppifyagency/seo-master-2026) | 0 | 1 | Shell | 2026-06-02 | The complete AI SEO & GEO stack for Claude Code — keyword re |
| 25 | [`Xaena53/aegis`](https://github.com/Xaena53/aegis) | 0 | 0 | TypeScript | 2026-09-17 | Aegis — network-verified trust for AI agents that spend mone |
| 26 | [`perceptiv-digital/ecommerce-operator-playbooks`](https://github.com/perceptiv-digital/ecommerce-operator-playbooks) | 1 | 0 | JavaScript | 2026-07-20 | Evidence-first AI playbooks for ecommerce operators — free t |
| 27 | [`api-evangelist/cogny`](https://github.com/api-evangelist/cogny) | 0 | 0 | None | 2026-09-20 | Cogny — independent third-party profile of a public API surf |
| 28 | [`pipeboard-co/pipeboard-cli`](https://github.com/pipeboard-co/pipeboard-cli) | 22 | 2 | Go | 2026-09-07 | Command-line tool for managing Meta Ads, Google Ads, and Tik |
| 29 | [`langchain-ai/paid-media-agent`](https://github.com/langchain-ai/paid-media-agent) | 61 | 16 | Python | 2026-09-14 | Open-source paid media agent for Google Ads, Meta Ads, Reddi |
| 30 | [`cassiorox/ClaudePRO`](https://github.com/cassiorox/ClaudePRO) | 7 | 2 | Python | 2026-09-21 | Framework Claude Code pra gestores de trafego (agencias e eu |

### Category: `SHALLOW_MARKETING_STUB` (46 repositories)

| # | Repository | Stars | Forks | Language | Last Push | Exclusion Reason |
|---|---|---|---|---|---|---|
| 1 | [`itallstartedwithaidea/google-ads-skills`](https://github.com/itallstartedwithaidea/google-ads-skills) | 38 | 8 | None | 2026-04-12 | Google Ads Agent Skills for Claude — campaign analysis, acco |
| 2 | [`itallstartedwithaidea/claude-googleadsagent`](https://github.com/itallstartedwithaidea/claude-googleadsagent) | 2 | 2 | JavaScript | 2026-07-17 | Google Ads Agent — Buddy. The most comprehensive Google Ads  |
| 3 | [`itallstartedwithaidea/google-ads-claudecodeskill`](https://github.com/itallstartedwithaidea/google-ads-claudecodeskill) | 2 | 1 | Python | 2026-04-12 | A Claude Code skill + MCP server setup for expert-level Goog |
| 4 | [`itallstartedwithaidea/gemini-cli-googleadsagent`](https://github.com/itallstartedwithaidea/gemini-cli-googleadsagent) | 6 | 0 | TypeScript | 2026-05-12 | Google Ads commands & AI agent skills for Gemini CLI — analy |
| 5 | [`nickyc1/google-ads-mcp-setup`](https://github.com/nickyc1/google-ads-mcp-setup) | 0 | 0 | Shell | 2026-05-27 | Claude Code skill: set up a local Google Ads MCP server conn |
| 6 | [`Alitaliani/xtropy-google-ads`](https://github.com/Alitaliani/xtropy-google-ads) | 0 | 0 | None | 2026-04-23 | Xtropy Google Ads plugin for Claude Code — 19 slash commands |
| 7 | [`christyandas/google-ads-brasil`](https://github.com/christyandas/google-ads-brasil) | 0 | 0 | JavaScript | 2026-08-17 | Setup de Google Ads + Merchant Center para Claude Code — 17  |
| 8 | [`Vibha-Ramprakash/automate-google-ads`](https://github.com/Vibha-Ramprakash/automate-google-ads) | 0 | 0 | Python | 2026-09-14 | Five-layer Google Ads AI workspace with the official MCP, 12 |
| 9 | [`portermetricsample/porter-metrics-google-ads`](https://github.com/portermetricsample/porter-metrics-google-ads) | 0 | 0 | HTML | 2026-06-26 | Porter Metrics — Google Ads report & analysis frameworks (sk |
| 10 | [`FuturizeRush/google-ads-agent-kit`](https://github.com/FuturizeRush/google-ads-agent-kit) | 0 | 0 | Python | 2026-09-20 | Agent skill and Traditional Chinese guide for Google Ads MCP |
| 11 | [`joevilcai666/google-ads-agent-skill`](https://github.com/joevilcai666/google-ads-agent-skill) | 0 | 0 | Python | 2026-05-29 | 🤖 AI agent skill: automate Google Ads account setup, billing |
| 12 | [`juliandickie/google-ads-playbook`](https://github.com/juliandickie/google-ads-playbook) | 0 | 0 | Python | 2026-09-21 | Audit and rebuild a Google Ads account with the $100M GADs p |
| 13 | [`chanktb/claude-google-ads`](https://github.com/chanktb/claude-google-ads) | 12 | 4 | Python | 2026-07-09 | Find where your Google Ads budget leaks, cut waste, and scal |
| 14 | [`kelpi-ai/google-ads-skills`](https://github.com/kelpi-ai/google-ads-skills) | 2 | 2 | None | 2026-07-13 | 12 free, installable Google Ads skills for Claude and other  |
| 15 | [`itallstartedwithaidea/google-ads-gemini-extension`](https://github.com/itallstartedwithaidea/google-ads-gemini-extension) | 8 | 1 | JavaScript | 2026-07-17 | Gemini CLI extension for Google Ads management — campaign an |
| 16 | [`Dataslayer-AI/Marketing-skills`](https://github.com/Dataslayer-AI/Marketing-skills) | 23 | 4 | Python | 2026-03-23 | Marketing agent skills powered by real data. Connect Claude  |
| 17 | [`adsagents/adsagent-ai-skills`](https://github.com/adsagents/adsagent-ai-skills) | 3 | 2 | Python | 2026-09-17 | AdsAgent hosted MCP for Meta, Google Ads & TikTok — public C |
| 18 | [`bsisduck/google-search-ads-analytics-docs`](https://github.com/bsisduck/google-search-ads-analytics-docs) | 2 | 0 | Python | 2026-06-10 | Official Google docs (Search/SEO, Search Console, Ads, GA4)  |
| 19 | [`jdeportugal/marketing-skills`](https://github.com/jdeportugal/marketing-skills) | 4 | 0 | Python | 2026-03-20 | The only marketing skills library for Claude with live data  |
| 20 | [`alexpilotto/uxon-ai`](https://github.com/alexpilotto/uxon-ai) | 13 | 0 | None | 2026-07-31 | MCP server and Claude skills for PPC landing pages, A/B expe |
| 21 | [`stranity/ecommerce-ads-skill`](https://github.com/stranity/ecommerce-ads-skill) | 0 | 0 | None | 2026-07-10 | Claude Code skill for generating e-commerce promotional stat |
| 22 | [`Dallenlol/ripple-ads-skills`](https://github.com/Dallenlol/ripple-ads-skills) | 0 | 0 | None | 2026-09-21 | Skills, slash commands and the MCP connector for Ripple Ads  |
| 23 | [`harrisonjdahl3/agency-mcp-plugin`](https://github.com/harrisonjdahl3/agency-mcp-plugin) | 0 | 0 | None | 2026-09-18 | Agency MCP plugin for Claude Code: SEO, Google Ads, Meta Ads |
| 24 | [`hyperfx-ai/marketing-skills`](https://github.com/hyperfx-ai/marketing-skills) | 89 | 16 | Python | 2026-09-21 | Marketing skills for AI agents — paid ads, social media, SEO |
| 25 | [`itallstartedwithaidea/MiniAgent`](https://github.com/itallstartedwithaidea/MiniAgent) | 10 | 2 | Python | 2026-07-20 | The Cowork Agent for Everything — trainable advertising AI + |
| 26 | [`1clickreport/skills`](https://github.com/1clickreport/skills) | 0 | 0 | None | 2026-09-13 | 15 Claude Agent Skills for marketing analytics — Google Ads, |
| 27 | [`tjdotwal/paid-ads-skills`](https://github.com/tjdotwal/paid-ads-skills) | 0 | 0 | Python | 2026-08-24 | Claude Code plugins for running paid advertising: Google Ads |
| 28 | [`twominutereports/marketing-skills`](https://github.com/twominutereports/marketing-skills) | 8 | 1 | JavaScript | 2026-09-08 | Claude Marketing Skills for SEO, PPC, and ecommerce reportin |
| 29 | [`ruslan2027/adako-mcp`](https://github.com/ruslan2027/adako-mcp) | 0 | 0 | JavaScript | 2026-09-19 | Adako (アダコ) — careful ad ops for AI agents. Skills, client c |
| 30 | [`Ad-Superpowers/ad-superpowers-plugin`](https://github.com/Ad-Superpowers/ad-superpowers-plugin) | 5 | 1 | Python | 2026-09-17 | Manage, analyze, and optimize your ad campaigns across 8 pla |
| 31 | [`chjm-ai/google-marketing-ops`](https://github.com/chjm-ai/google-marketing-ops) | 2 | 0 | None | 2026-04-29 | Claude Code skill that orchestrates Google Ads + GA4 + GTM i |
| 32 | [`mattzimak/marketing-handbook`](https://github.com/mattzimak/marketing-handbook) | 0 | 0 | Python | 2026-09-21 | A founder's handbook for running marketing with AI agents -  |
| 33 | [`converlyio/converly-agent`](https://github.com/converlyio/converly-agent) | 0 | 0 | None | 2026-08-18 | Converly conversion-tracking skill for AI agents — drives th |
| 34 | [`Hainrixz/claude-ads`](https://github.com/Hainrixz/claude-ads) | 81 | 15 | Python | 2026-05-13 | Self-updating multi-platform paid advertising audit & optimi |
| 35 | [`itallstartedwithaidea/agent-skills`](https://github.com/itallstartedwithaidea/agent-skills) | 39 | 8 | Shell | 2026-04-12 | The definitive open-source agent skills library for AI-power |
| 36 | [`alphaparkinc/genpark-unified-marketing-analyst-skill`](https://github.com/alphaparkinc/genpark-unified-marketing-analyst-skill) | 9 | 0 | Python | 2026-07-10 | Unified Marketing Analyst agent skill designed to integrate  |
| 37 | [`datablogin/PaidSearchNav-MCP`](https://github.com/datablogin/PaidSearchNav-MCP) | 2 | 0 | Python | 2025-12-04 | Lightweight MCP server providing Google Ads and BigQuery dat |
| 38 | [`Onurcanozer/klienta-plugin`](https://github.com/Onurcanozer/klienta-plugin) | 0 | 0 | None | 2026-07-17 | Klienta — manage your own Google Ads account through AI chat |
| 39 | [`coffeegrind123/adsense-skill`](https://github.com/coffeegrind123/adsense-skill) | 0 | 0 | None | 2026-07-22 | Agent Skill: put Google ads (AdSense/GPT) on a content site  |
| 40 | [`AtromxIntelligence/adcopilot-mcp`](https://github.com/AtromxIntelligence/adcopilot-mcp) | 0 | 0 | None | 2026-08-25 | Hosted Google Ads MCP server — 32 read/write tools inside Cl |
| 41 | [`itallstartedwithaidea/ai-agents-crash-course`](https://github.com/itallstartedwithaidea/ai-agents-crash-course) | 13 | 0 | HTML | 2026-04-12 | Free 42-page AI agents crash course v5.0 — 5 days, 3 learnin |
| 42 | [`Tymyopp/MazyOS-Rework`](https://github.com/Tymyopp/MazyOS-Rework) | 0 | 2 | JavaScript | 2026-08-14 | MazyOS-Rework — sistema operacional do negocio em agentes de |
| 43 | [`Satori-L/ads-agent-brain`](https://github.com/Satori-L/ads-agent-brain) | 0 | 0 | None | 2026-06-12 | The judgment layer of a production Google Ads agent — operat |
| 44 | [`irinabuht12-oss/marketing-skills`](https://github.com/irinabuht12-oss/marketing-skills) | 1638 | 210 | Markdown | 2026-03-25 | Pure Markdown prompt/skill repository without executable MCP server code; retained irinabuht12-oss/google-meta-ads-ga4-mcp |
| 45 | [`saifshabsug/google-ads-mcp-pro`](https://github.com/saifshabsug/google-ads-mcp-pro) | 1 | 0 | Python | 2025-10-18 | Single-commit marketing README with trivial wrapper code |
| 46 | [`VidenGrowth/public-google-ads-mcp`](https://github.com/VidenGrowth/public-google-ads-mcp) | 2 | 0 | Python | 2025-11-01 | 3-commit thin agency wrapper, lowest benchmark composite score (44.9%) |
