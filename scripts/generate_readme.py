#!/usr/bin/env python3
"""Generate README.md for awesome-google-ads-mcp from data/registry.json."""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "registry.json")
README_PATH = os.path.join(BASE_DIR, "README.md")

def slugify(title):
    s = title.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s).strip('-')
    return s

def build_readme():
    with open(DATA_PATH) as f:
        registry = json.load(f)

    total_projects = registry["total_projects"]
    categories = registry["categories"]
    projects = {p["slug"]: p for p in registry["projects"]}

    lines = []

    # Title & Badge
    lines.append("# Awesome Google Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append("> A curated developer index and technical comparison of Model Context Protocol (MCP) servers and agentic tooling for **[Google Ads](https://ads.google.com/)**.")
    lines.append("")
    lines.append("Official links: [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/first-call/overview) · [Google Cloud Console](https://console.cloud.google.com/) · [Model Context Protocol](https://modelcontextprotocol.io/) · [Google Ads API Changelog](https://developers.google.com/google-ads/api/docs/release-notes) · [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Contents
    lines.append("## Contents")
    lines.append("")
    for cat in categories:
        cat_anchor = f"{cat['number']}-{slugify(cat['name'])}"
        lines.append(f"{cat['number']}. [{cat['name']} ({cat['count']})](#{cat_anchor})")
        for sub in cat["subcategories"]:
            sub_anchor = slugify(sub["name"])
            lines.append(f"   - [{sub['name']} ({sub['count']})](#{sub_anchor})")
    
    # Non-category sections in Contents
    matrix_num = len(categories) + 1
    resources_num = len(categories) + 2
    reference_num = len(categories) + 3
    lines.append(f"{matrix_num}. [Developer comparison matrix ({total_projects})](#developer-comparison-matrix)")
    lines.append(f"{resources_num}. [Resources](#resources)")
    lines.append(f"{reference_num}. [Reference](#reference)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Developer Comparison Matrix
    lines.append("## Developer Comparison Matrix")
    lines.append("")
    lines.append(f"*{total_projects} projects. Side-by-side technical capability comparison across runtime, authentication, persistence, token formatting, and API coverage. Project names link internally to detailed listings below.*")
    lines.append("")

    # 20 Columns
    cols = [
        "Project", "Role", "Runtime", "Transport", "SearchStream", "Dry-Run",
        "Mutations", "Search", "PMax/Shop", "Video/Disp", "Offline Conv",
        "GAQL Refl", "SQLite Cache", "Latency", "MCP Apps", "HITL Appr",
        "MCC Multi", "Refresh Daemon", "Footprint", "Stars / Cadence"
    ]
    lines.append("| " + " | ".join(cols) + " |")
    lines.append("|" + "|".join(["---"] * len(cols)) + "|")

    # Sort projects deterministically: Tier 1/2 first, then by stars desc
    sorted_projs = sorted(
        registry["projects"],
        key=lambda x: (
            0 if "DevRel" in x["role"] or "Platform" in x["role"] else 1,
            -x["stars"]
        )
    )

    for p in sorted_projs:
        p_anchor = p["slug"]
        row = [
            f"[{p['repo']}](#{p_anchor})",
            f"`{p['role']}`",
            f"`{p['runtime']}`",
            f"`{p['transport']}`",
            "Full" if p["search_stream"] else "No",
            "Yes" if p["dry_run"] else "No",
            "Yes" if p["live_mutations"] else "Read-Only",
            "Yes" if p["search_ads"] else "No",
            "Yes" if p["pmax_shopping"] else "No",
            "Yes" if p["video_display"] else "No",
            "Yes" if p["offline_conversions"] else "No",
            "Yes" if p["gaql_reflection"] else "No",
            "WAL" if p["sqlite_wal_cache"] else "No",
            p["query_latency"],
            "React" if p["mcp_apps_ui"] else "No",
            "Modal" if p["hitl_approval"] else "No",
            "Dynamic" if p["mcc_hierarchy"] else "Single",
            "Auto" if p["token_refresh_daemon"] else "Manual",
            p["est_token_footprint"].split()[0],
            f"{p['stars']}★ ({p['recency']})"
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Categorized Sections
    for cat in categories:
        cat_count_str = f"*{cat['count']} projects. {cat['description']}*" if cat['count'] != 1 else f"*1 project. {cat['description']}*"
        lines.append(f"## {cat['number']}. {cat['name']}")
        lines.append("")
        lines.append(cat_count_str)
        lines.append("")

        for sub in cat["subcategories"]:
            sub_count_str = f"*{sub['count']} projects. {sub['description']}*" if sub['count'] != 1 else f"*1 project. {sub['description']}*"
            lines.append(f"### {sub['name']}")
            lines.append("")
            lines.append(sub_count_str)
            lines.append("")
            lines.append("| Project | What it does |")
            lines.append("|---|---|")

            for slug in sub["tool_slugs"]:
                p = projects[slug]
                # Two-stage anchor: <a id="slug"></a>[**owner/repo**](URL)
                row_project = f"<a id=\"{p['slug']}\"></a>[**{p['repo']}**]({p['url']})"
                row_desc = p['description']
                lines.append(f"| {row_project} | {row_desc} |")
            
            lines.append("")
        
        lines.append("---")
        lines.append("")

    # Resources
    lines.append("## Resources")
    lines.append("")
    lines.append("- **[Google Ads API Developer Documentation](https://developers.google.com/google-ads/api/docs/first-call/overview)**: The official manual for REST and gRPC API integration, resource schemas, and service definitions.")
    lines.append("- **[Google Ads Query Language (GAQL) Reference](https://developers.google.com/google-ads/api/docs/query/overview)**: The definitive syntax reference for constructing GAQL query strings across resources and metrics.")
    lines.append("- **[Model Context Protocol Specification](https://modelcontextprotocol.io/)**: Protocol documentation for JSON-RPC 2.0 messages over stdio, SSE, and Streamable HTTP.")
    lines.append("- **[Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials)**: Developer portal for configuring OAuth 2.0 Client IDs, redirect URIs, and Google Ads API scopes.")
    lines.append("- **[Google Ads Python SDK GitHub](https://github.com/googleads/google-ads-python)**: Official Google-supported client library featuring gRPC bindings and protobuf stubs.")
    lines.append("- **[Google Ads Node.js Client GitHub](https://github.com/googleads/google-ads-nodejs)**: Official TypeScript/Node client library for executing searchStream and mutate queries.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Reference
    lines.append("## Reference")
    lines.append("")
    lines.append("- **gRPC SearchStream vs. Paged Search:** The Google Ads API provides two distinct query endpoints: `GoogleAdsService.Search` (paged, subject to page-token boundaries and higher round-trip latency) and `GoogleAdsService.SearchStream` (HTTP/2 gRPC streaming, yielding continuous chunks for lower latency and memory overhead). Production gateways should prefer `SearchStream`.")
    lines.append("- **Meta-MCP SQLite Ingestion Pattern:** Servers that initialize an embedded SQLite database in WAL mode and spin up a background worker thread (`kLOsk/adloop`, `akelaonline/MCP-Google-Ads`) execute local analytical queries in 1.8ms–4.2ms (over 300x faster than live GAQL) while consuming zero daily API quota.")
    lines.append("- **MCP Apps Spend Approvals:** Direct text-based mutation tools expose ad accounts to prompt injection and accidental micro-unit decimal errors. MCP Apps (`nowork-studio/notfair-plugin`, `ameydabhade/google-ads-mcp`) render sandboxed React widgets directly within chat; clicking an approval slider fires JSON-RPC commits via `window.postMessage`, completely bypassing the LLM on financial commit.")
    lines.append("- **Proactive Token Refresh Daemons:** Google OAuth access tokens expire after 3,600 seconds (1 hour). Unhandled token expiration causes agent sessions to crash mid-workflow. Production implementations (`gomarble-ai`, `googleads`) maintain background refresh daemons that renew tokens proactively.")
    lines.append("- **Currency Micros Conversion:** Google Ads represents monetary values as integer micros ($1.00 = 1,000,000 micros). Specialized helpers convert between micros and standard currency to prevent catastrophic budget inflation.")
    lines.append("- **Manager Account (MCC) Hierarchy Routing:** Multi-account agency deployments require dynamic routing via the `login-customer-id` HTTP header, allowing an agent to manage hundreds of client accounts under a single authenticated developer token.")
    lines.append("")

    with open(README_PATH, "w") as f:
        f.write("\n".join(lines))

    print(f"✓ Successfully generated README.md ({len(lines)} lines)")

if __name__ == "__main__":
    build_readme()
