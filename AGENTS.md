# AGENTS.md

Working rules and language guidelines for anyone — human or agent — editing this repository. It is a curated, plain-English index and technical comparison of Model Context Protocol (MCP) servers and agentic tooling for **[Google Ads](https://ads.google.com/)**. Keep it lean, minimalist, and immediately useful.

---

## 1. Project Philosophy & Minimalist Structure

- **No Onboarding Essays:** Keep the catalog root focused: Title, official links, Contents with counts, direct jump links into tables, and the Developer Comparison Matrix.
- **Fast Jump Navigation:** Readers should jump directly to the relevant problem domain from the Table of Contents or Comparison Matrix in 1 click.
- **Strict Scope Boundary:** Exclusively Google Ads API surface (Search, Display, Shopping, Performance Max, Video, App, Demand Gen, Local). Legacy AdWords API belongs exclusively in `docs/EXCLUSIONS.md`.

---

## 2. Project Language & Voice Values

- **Plain-English, Verb-First Prose:** Lead with active verbs (*Executes*, *Synchronizes*, *Streams*, *Caches*, *Mutates*, *Protects*, *Inspects*).
- **The 1–2 Sentence Rule:** Every project entry must be strictly 1 or 2 concise sentences (never exceeding 3 sentences).
  - *Sentence 1:* What the tool specifically does for a developer or agent.
  - *Sentence 2:* How it differs from its closest alternatives (e.g. gRPC streaming, SQLite caching, MCP Apps sandboxed UI, or MCC switching).
- **Subcategory Header & Table Standards:** Each subcategory begins with a count and a 1-sentence summary, followed by a clean 2-column markdown table.

---

## 3. Two-Stage Jump-Linking Model

- The Developer Comparison Matrix links internally via anchor tags (`[owner/repo](#project-slug)`).
- Project tables embed `<a id="project-slug"></a>` anchors and supply the verified external GitHub URL.

---

## 4. Strict Exclusion Criteria (What NEVER Belongs in Active Tables)

To maintain a high-signal catalog, the following must **never** be added to active tables:

1. **NO Sunset AdWords API Tools:** Only tools built against the modern Google Ads API qualify.
2. **NO Empty Scaffolds or Incomplete Stubs:** Repositories without working tool handlers or broken builds.
3. **NO Generic Non-Ads Wrappers:** Generic multi-platform directories qualify only if they provide a distinct, first-class Google Ads API toolset.
4. **NO Marketing Hype or AI Filler:** Descriptions must remain factual, concise, and neutral.

---

## 5. Before Committing

1. Run `npx markdownlint-cli2 "**/*.md"` — it must exit clean with **0 issues** (same check CI runs).
2. Ensure mathematical count integrity across all categories and subcategories.
