# AGENTS.md

This document provides architectural, operational, and evidentiary guidance for AI coding and research agents working in the **`awesome-google-ads-mcp`** repository.

---

## 1. Repository Architecture & Scope

This repository is a **curated, developer-focused index and technical benchmark** of Model Context Protocol (MCP) servers and agentic tooling for the **Google Ads API**.

### Core Invariants:
1. **Strict Google Ads Scope:** Exclusively the Google Ads API surface (Search, Display, Shopping, Performance Max, Video, App, Demand Gen, Local). Legacy AdWords API tools belong in `docs/EXCLUSIONS.md`, never as active entries.
2. **Structural Parity with `awesome-herdr`:** Preserves exact AST hierarchy:
   `# Awesome Google Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)`
   $\to$ Positioning Quote
   $\to$ Official Links
   $\to$ `## Contents` (numbered categories with `(N)`, nested subcategories with `(M)`)
   $\to$ `## Developer Comparison Matrix` (20 Columns $\times$ 200 Rows max)
   $\to$ Numbered `##` Categories $\to$ Italicized summaries
   $\to$ `###` Subcategories $\to$ Italicized summaries
   $\to$ Two-column tables `| Project | What it does |`
   $\to$ `## Resources` $\to$ `## Reference`
3. **Data Plane as Single Source of Truth:** `data/registry.json` is the authoritative ledger governed by `data/schema.json`. `README.md` is compiled via `python3 scripts/generate_readme.py`.
4. **Mathematical Count Integrity:**
   $$\text{Contents top count} \equiv \sum \text{Subcategory counts} \equiv \text{Table rows} \equiv \text{Registry count}$$
5. **Two-Stage Jump-Linking:** Comparison Table project links point internally to `<a id="project-slug"></a>` in detailed tables, which provide the verified outbound GitHub link.

---

## 2. Maintenance & Validation Commands

Always run the mechanical validation suite before proposing or committing changes:

```bash
# 1. Regenerate README from registry.json
python3 scripts/generate_readme.py

# 2. Run mechanical validation suite
python3 scripts/validate_awesome.py --strict
```
