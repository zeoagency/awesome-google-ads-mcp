# kLOsk/adloop tools

[Main list](../../README.md) · [Search every tool](../TOOLS.md) · [Upstream](https://github.com/kLOsk/adloop)

**Inventory:** 124 tools. **Default tools/list:** 123. **Checked:** 2026-10-13.

**Source:** [commit ef26cef](https://github.com/kLOsk/adloop/tree/ef26cefaf0e6704c458f846f15d066ba44b432bf). Offline FastMCP registration + protocol tools/list, full and Ads-only configurations; FastMCP 4.1.0.

The complete registration has 124 tools: 63 Google Ads tools, 3 shared helpers, and 58 other-platform tools shown in a separate section. Ordinary default clients see 123; `approve_change` is app-only. `ADLOOP_TOOLSETS=ads` selects 66 registrations and exposes 65 to ordinary clients. Draft tools stage plans; `confirm_and_apply` uses Google Ads `validate_only` for eligible plan steps. Safety configuration and approval rules govern real apply.

Descriptions and parameter JSON below preserve the registered MCP interface. Open each parameter block for required fields, defaults, enums, nested objects, and references. Prose-only restrictions and free-form objects remain as upstream declares them. No tool was invoked and no live account operation was tested.

## Tools

- [Accounts, queries, and performance (7)](#accounts-queries-and-performance)
- [Keyword research and search terms (25)](#keyword-research-and-search-terms)
- [Campaigns, budgets, bidding, and targeting (11)](#campaigns-budgets-bidding-and-targeting)
- [Ads and creative assets (8)](#ads-and-creative-assets)
- [Audiences and audience insights (1)](#audiences-and-audience-insights)
- [Conversions and measurement (10)](#conversions-and-measurement)
- [Experiments and recommendations (1)](#experiments-and-recommendations)
- [Previews, validation, and local helpers (3)](#previews-validation-and-local-helpers)
- [Other platform tools (58)](#other-platform-tools)

## Accounts, queries, and performance

<a id="tool-get-ad-performance"></a>

### `get_ad_performance`

Get ad-level performance data including headlines, descriptions, and metrics.

Returns ad type, headlines, descriptions, final URL, impressions,
clicks, CTR, conversions, cost for each ad, plus its policy approval
status, review status and policy topic names. Disapproved and
limited-by-policy ads are listed under policy_issues with their spend.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "compact": {
      "default": false,
      "type": "boolean",
      "description": "When true (for audits/overviews), returns totals, the top-10\nads with headline/description COUNTS instead of full asset lists,\nplus incomplete-RSA, single-ad ad-group and policy findings with\napproval-status counts (~90% smaller)."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1226)

<a id="tool-get-ai-max-settings"></a>

### `get_ai_max_settings`

Read the AI Max controls of Search campaigns, per campaign and ad group.

Returns for every campaign: id, name, status, advertising channel type,
campaign.ai_max_setting.enable_ai_max, campaign.ai_max_setting.bundling_required
(output only) and the full campaign.asset_automation_settings list. Each
campaign also carries its non-REMOVED ad groups with
ad_group.ai_max_ad_group_setting.disable_search_term_matching.

Shows the current state ahead of draft_ai_max_settings, and what the
account actually looks like after confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Numeric campaign ID. When omitted, every non-removed\nSearch campaign in the account is listed."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3383)

<a id="tool-get-campaign-performance"></a>

### `get_campaign_performance`

Get campaign-level performance metrics for a date range.

Returns campaign name, status, type, impressions, clicks, cost,
conversions, CPA, ROAS, CTR for each campaign, plus Search impression
share and the share lost to budget and to ad rank (fractions with
matching *_pct percentages; null for campaigns that do not serve on
Search or had no impressions). Insights flag converting campaigns that
lose a significant share of impressions to budget.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "compact": {
      "default": false,
      "type": "boolean",
      "description": "When true (for audits/overviews on large accounts), returns\naccount totals, status/type breakdowns, the top-10 spenders,\nzero-conversion offenders and budget-limited converters instead\nof every row (~90% smaller)."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1187)

<a id="tool-get-change-history"></a>

### `get_change_history`

List recent account changes: who changed what, when, and through which tool.

Answers "what changed before the drop?". Returns each change newest
first with its time, the user's email, the client it came through
(Google Ads UI, API, Google Ads scripts, Editor, automated rules,
auto-applied recommendations, ...), the changed resource type, the
operation (CREATE, UPDATE, REMOVE), the changed field paths, and the
campaign and ad group names. Also returns counts by resource type,
client, user and day, plus insights on auto-applied recommendations
and budget or bidding changes. Google Ads keeps change history for 30
days, so older start dates are moved to the earliest available day.

Reads the change_event resource:
<https://developers.google.com/google-ads/api/docs/change-event>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\", at most 30 days back.\nEmpty starts at the oldest day Google Ads still keeps."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive). Empty means today."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Optional numeric campaign ID; only changes attributed to\nthat campaign are returned."
    },
    "resource_types": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional filter of ChangeEventResourceType names,\ne.g. [\"CAMPAIGN\", \"CAMPAIGN_BUDGET\", \"AD_GROUP_AD\",\n\"AD_GROUP_CRITERION\"]. Empty = all types."
    },
    "limit": {
      "default": 1000,
      "type": "integer",
      "description": "Maximum number of changes returned, newest first (1 to\n10000; default 1000). The response is marked truncated when\nthe limit is reached."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1654)

<a id="tool-get-pmax-performance"></a>

### `get_pmax_performance`

Get Performance Max campaign and asset group performance.

Returns two result sets. campaigns: PMax campaign metrics broken down by
ad_network_type (SEARCH, CONTENT, YOUTUBE_SEARCH, YOUTUBE_WATCH, MIXED).
MIXED is a catch-all that Google uses for most PMax traffic — full channel
splits are not available via the API. asset_groups: per-asset-group
metrics including ad_strength (EXCELLENT, GOOD, AVERAGE, POOR).

Includes insights flagging weak ad strength, zero-conversion asset groups,
and network type distribution.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1481)

<a id="tool-list-accounts"></a>

### `list_accounts`

List accessible Google Ads accounts.

Returns account names, IDs, status, and whether each is a manager account.
When more accounts exist than `limit`, the response has
'truncated: true'; a much higher limit (e.g. list_accounts(limit=1000))
returns the full list. Workflows that target a specific account need no
enumeration at all: get_campaign_performance, run_gaql, etc. take
customer_id directly.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "limit": {
      "default": 200,
      "type": "integer",
      "description": "Maximum number of accounts listed under the manager (MCC)\naccount. The default cap of 200 covers the vast majority of agency\nMCCs in one call."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1165)

<a id="tool-run-gaql"></a>

### `run_gaql`

Execute an arbitrary GAQL (Google Ads Query Language) query.

For queries beyond the dedicated report tools. Returns the result rows
in the requested format with the query echoed back; cost fields stay in
raw micros (cost_micros / 1,000,000 = account currency). A failing query
returns an error with a hint.

Queries the Google Ads API. GAQL syntax and fields:
<https://developers.google.com/google-ads/api/docs/query/overview>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "query": {
      "type": "string",
      "description": "The GAQL query, e.g. \"SELECT campaign.name, metrics.clicks\nFROM campaign WHERE segments.date DURING LAST_7_DAYS\"."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(123-456-7890). Empty uses the configured default account."
    },
    "format": {
      "default": "table",
      "type": "string",
      "description": "Output format: \"table\" (default, readable), \"json\"\n(structured), or \"csv\" (exportable)."
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2584)

## Keyword research and search terms

<a id="tool-add-negative-keywords"></a>

### `add_negative_keywords`

Draft negative keyword additions — returns a PREVIEW.

Negative keywords prevent your ads from showing for irrelevant searches.
They are added at campaign level. Returns a preview with a plan_id; nothing
changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the campaign that gets the negatives."
    },
    "keywords": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Negative keyword texts; at least one is required. All share\nthe same match_type."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    },
    "match_type": {
      "default": "EXACT",
      "type": "string",
      "description": "\"EXACT\" (default), \"PHRASE\", or \"BROAD\"."
    }
  },
  "required": [
    "campaign_id",
    "keywords"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3173)

<a id="tool-add-to-brand-list"></a>

### `add_to_brand_list`

Append brands to an EXISTING brand list — returns a PREVIEW.

For a list that already exists and only needs more brands
(propose_brand_list creates a new list instead). The shared_set_id comes
from get_brand_lists; get_brand_list_brands shows the brands already in
the list, which makes a brand that would be added twice visible.

Returns a preview with a plan_id; nothing changes until the returned
plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric list ID from get_brand_lists."
    },
    "brand_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Commercial Knowledge Graph MIDs from suggest_brands."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "shared_set_id",
    "brand_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5967)

<a id="tool-add-to-negative-keyword-list"></a>

### `add_to_negative_keyword_list`

Append keywords to an EXISTING shared negative keyword list — returns a PREVIEW.

Adds terms to a list that already exists (propose_negative_keyword_list
creates a new list instead); get_negative_keyword_list_keywords shows the
terms already in a list. Returns a preview with a plan_id; nothing changes
until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric ID of the list (shared_set.id from\nget_negative_keyword_lists)."
    },
    "keywords": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Keyword strings to append. Blank entries are dropped and\nduplicates in the input list are collapsed (case-insensitive)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    },
    "match_type": {
      "default": "EXACT",
      "type": "string",
      "description": "Match type applied to every keyword: \"EXACT\" (default),\n\"PHRASE\", or \"BROAD\" (case-insensitive)."
    }
  },
  "required": [
    "shared_set_id",
    "keywords"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3281)

<a id="tool-attach-brand-list-to-campaigns"></a>

### `attach_brand_list_to_campaigns`

Attach an existing brand list to one or more campaigns — returns a PREVIEW.

Creates a CampaignCriterion.brand_list per campaign. This is NOT the
CampaignSharedSet linkage used for negative keyword lists — brand lists are
criteria, and `negative` decides the role. The shared_set_id comes from
get_brand_lists; get_brand_list_campaigns lists existing attachments.

Returns a preview with a plan_id; nothing changes until the returned
plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric list ID from get_brand_lists."
    },
    "campaign_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Numeric campaign IDs to attach the list to."
    },
    "negative": {
      "default": true,
      "type": "boolean",
      "description": "True (default) excludes the brands from those campaigns;\nFalse restricts targeting to them instead."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "shared_set_id",
    "campaign_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L6029)

<a id="tool-attach-shared-set-to-campaigns"></a>

### `attach_shared_set_to_campaigns`

Attach an existing shared set to one or more campaigns — returns a PREVIEW.

Creates CampaignSharedSet linkages so the campaigns inherit the shared
set's criteria (e.g. negative keywords). Most commonly used to attach a
shared negative keyword list to newly-built campaigns;
get_negative_keyword_list_campaigns lists existing attachments. Returns a
preview with a plan_id; nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric ID of the shared set (from\nget_negative_keyword_lists)."
    },
    "campaign_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Numeric campaign IDs to attach the set to (at least one).\nBlank entries are dropped and duplicates collapsed."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "shared_set_id",
    "campaign_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3317)

<a id="tool-check-brand-names"></a>

### `check_brand_names`

Check a list of brand names against Google's brand knowledge graph.

One SuggestBrands call per name, for the case where a shortlist has to be
triaged instead of a single name resolved: which of these brands does
Google know at all, and what is the ID of each?

Returns checked / matched / no_match counts and one result per name with
status "matched" (with a best-match brand plus all candidates) or
"no_match" (empty candidate list — a normal answer, not an error).
exact_match marks a candidate whose name matches the query apart from case
and punctuation; anything else is a Google suggestion, not a guarantee.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "brand_names": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "The names to triage, at most 25 per call — the API\nresolves one prefix per request, so longer lists take several calls."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "brand_names"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5823)

<a id="tool-detach-brand-list-from-campaigns"></a>

### `detach_brand_list_from_campaigns`

Detach a brand list from one or more campaigns — returns a PREVIEW.

Removes the CampaignCriterion rows linking the list to those campaigns; the
list itself and its brands are unchanged. get_brand_list_campaigns lists
the existing attachments.

Returns a preview with a plan_id; nothing changes until the returned
plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric list ID from get_brand_lists."
    },
    "campaign_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Numeric campaign IDs to detach the list from. Campaigns\nthat do not carry the list are reported as `not_attached` in the\napply result instead of failing the batch."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "shared_set_id",
    "campaign_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L6064)

<a id="tool-detach-shared-set-from-campaigns"></a>

### `detach_shared_set_from_campaigns`

Detach a shared set from one or more campaigns — returns a PREVIEW.

Removes CampaignSharedSet linkages so the campaigns no longer inherit the
shared set's criteria. The shared set itself is unchanged; only the
per-campaign attachment is removed. get_negative_keyword_list_campaigns
lists the existing attachments. Returns a preview with a plan_id; nothing
changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric ID of the shared set (from\nget_negative_keyword_lists)."
    },
    "campaign_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Numeric campaign IDs to detach the set from (at least one).\nBlank entries are dropped and duplicates collapsed."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "shared_set_id",
    "campaign_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3350)

<a id="tool-discover-keywords"></a>

### `discover_keywords`

Discover new keyword ideas using Google Ads Keyword Planner.

Mirrors the "Discover new keywords" UI in Keyword Planner: start with
keywords (seed_keywords), start with a website (url), or both together
for more targeted ideas. At least one of seed_keywords or url is required.

Returns keyword ideas sorted by avg monthly search volume, with
competition level (LOW/MEDIUM/HIGH) and top-of-page bid range, plus the
seeds used and insights.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "seed_keywords": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Seed terms, e.g. [\"running shoes\", \"trail running\"]."
    },
    "url": {
      "default": "",
      "type": "string",
      "description": "A landing page or site URL to extract ideas from, e.g.\n\"https://example.com/products\"."
    },
    "geo_target_id": {
      "default": "2276",
      "type": "string",
      "description": "Geo target constant ID (2276=Germany, 2840=USA, 2826=UK).\nDefaults to 2276."
    },
    "language_id": {
      "default": "1000",
      "type": "string",
      "description": "Language constant ID (1000=English, 1001=German,\n1002=French). Defaults to 1000."
    },
    "page_size": {
      "default": 50,
      "type": "integer",
      "description": "Max keyword ideas to return (default 50, clamped to 1-1000)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes allowed). Defaults\nto the configured account."
    },
    "include_monthly_volumes": {
      "default": false,
      "type": "boolean",
      "description": "true adds per-month search history (last 24\nmonths, top-20 ideas) plus a seasonality insight — relevant to\nquestions about demand trends, seasonality, or \"when should I ramp\nbudget\"."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5732)

<a id="tool-draft-keywords"></a>

### `draft_keywords`

Draft keyword additions — returns a PREVIEW, does NOT add keywords.

Returns a preview with a plan_id, plus a warning when BROAD keywords go into
a campaign without Smart Bidding; nothing changes until confirm_and_apply
applies the returned plan_id.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "type": "string",
      "description": "Numeric ID of the ad group that gets the keywords."
    },
    "keywords": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "type": "array",
      "description": "List of {\"text\": \"keyword phrase\", \"match_type\":\n\"EXACT|PHRASE|BROAD\"}; at least one is required."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    }
  },
  "required": [
    "ad_group_id",
    "keywords"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2957)

<a id="tool-draft-prepare-brand-exclusions"></a>

### `draft_prepare_brand_exclusions`

Draft the safe standard state for brand exclusions — returns a PREVIEW.

Exactly one combination, nothing else: enable_ai_max = true,
disable_search_term_matching = true (all non-removed ad groups),
TEXT_ASSET_AUTOMATION = OPTED_OUT and
FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION = OPTED_OUT.

No bidding, keyword, match type, ad, URL or budget change, and no brand list
is attached — attaching stays a separate step with propose_brand_list /
attach_brand_list_to_campaigns once this state is verified in the account.

Returns a preview with a plan_id (purpose brand_exclusions); nothing changes
until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the Search campaign to prepare."
    },
    "include_paused_ad_groups": {
      "default": true,
      "type": "boolean",
      "description": "Default true — paused ad groups are set too,\nso re-enabling one later cannot silently restore search term\nmatching."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3483)

<a id="tool-estimate-budget"></a>

### `estimate_budget`

Forecast clicks, cost, and conversions for a set of keywords.

Uses Google Ads Keyword Planner to estimate campaign performance without
creating anything. Essential for budget planning before launching campaigns.
Per-keyword max_cpc values are collapsed to a campaign-level manual CPC
cap (the highest one) — the Ads API forecast takes no per-keyword bids.
Returns estimated clicks, cost, avg CPC, conversions and avg CPA for the
forecast period, daily estimates, and insights.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "keywords": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "type": "array",
      "description": "List of {\"text\": \"keyword\", \"match_type\": \"EXACT|PHRASE|BROAD\",\n\"max_cpc\": 1.50}. match_type defaults to BROAD; max_cpc is optional\n(defaults to 1.00 in account currency, not micros). At least one\nkeyword is required."
    },
    "daily_budget": {
      "default": 0,
      "type": "number",
      "description": "Daily budget in account currency. If provided, insights\nwill show what % of traffic the budget captures. 0 = no budget\ncomparison."
    },
    "geo_target_id": {
      "default": "2276",
      "type": "string",
      "description": "Geo target constant ID (2276=Germany, 2840=USA, 2826=UK,\n2250=France). Defaults to 2276."
    },
    "language_id": {
      "default": "1000",
      "type": "string",
      "description": "Language constant ID (1000=English, 1001=German,\n1002=French, 1003=Spanish). Defaults to 1000."
    },
    "forecast_days": {
      "default": 30,
      "type": "integer",
      "description": "Forecast horizon in days, starting tomorrow (default 30)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes allowed). Defaults\nto the configured account."
    }
  },
  "required": [
    "keywords"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5684)

<a id="tool-get-brand-list-brands"></a>

### `get_brand_list_brands`

List the brands inside a brand list.

Returns the brands and their total. Each entry carries brand.entity_id
(the Commercial KG MID that suggest_brands returns as id), the display
name, primary URL, status and a criterion_id — the latter is what
remove_from_brand_list needs.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric list ID from get_brand_lists (shared_set.id)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "shared_set_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5875)

<a id="tool-get-brand-list-campaigns"></a>

### `get_brand_list_campaigns`

List which campaigns a brand list is attached to.

Brand lists attach as CampaignCriterion rows of type BRAND_LIST (not as
CampaignSharedSet like negative keyword lists). Returns each attachment's
campaign ID, name and status, the criterion, and `role`: "excluded" when
the criterion is negative, "targeted" when it restricts targeting to the
list.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "default": "",
      "type": "string",
      "description": "Numeric list ID from get_brand_lists. When omitted,\nall brand-list attachments in the account are returned."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5900)

<a id="tool-get-brand-lists"></a>

### `get_brand_lists`

List all brand lists (SharedSets of type BRANDS) in the account.

Returns each list's ID, name, status, and member count, plus the total —
the basis for reusing an existing list with add_to_brand_list instead of
duplicating it with propose_brand_list.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5854)

<a id="tool-get-keyword-performance"></a>

### `get_keyword_performance`

Get keyword metrics including quality scores and competitive data.

Returns keyword text, match type, quality score, impressions,
clicks, CTR, CPC, conversions for each keyword.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "compact": {
      "default": false,
      "type": "boolean",
      "description": "When true (for audits/overviews), returns totals, match-type\ndistribution, the top-10 spenders, low-quality-score keywords, and\nzero-conversion spenders instead of every row (~90% smaller)."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1263)

<a id="tool-get-negative-keyword-list-campaigns"></a>

### `get_negative_keyword_list_campaigns`

List which campaigns a shared negative keyword list is attached to.

Returns each list-to-campaign attachment with the list and campaign IDs
and names.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "default": "",
      "type": "string",
      "description": "Numeric ID from get_negative_keyword_lists. When\nomitted, returns all list-to-campaign attachments across the account."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1417)

<a id="tool-get-negative-keyword-list-keywords"></a>

### `get_negative_keyword_list_keywords`

List the keywords inside a shared negative keyword list.

Returns each negative keyword's text, match type, and a resource_id
("sharedSetId~criterionId"), with the total keyword count.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric ID from get_negative_keyword_lists (shared_set.id)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    }
  },
  "required": [
    "shared_set_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1388)

<a id="tool-get-negative-keyword-lists"></a>

### `get_negative_keyword_lists`

List all shared negative keyword lists (SharedSets) in the account.

Returns each list's ID, name, status, and keyword count. Useful before
propose_negative_keyword_list: a suitable list may already exist and
just need attaching to a campaign.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1364)

<a id="tool-get-negative-keywords"></a>

### `get_negative_keywords`

List existing negative keywords for a campaign or all campaigns.

Shows the existing negatives, which reveals duplicates before new
negative keywords are added. Returns each negative's campaign, keyword
text, match type, and a resource_id ("campaignId~criterionId") as taken
by remove_entity, plus the total count.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Numeric campaign ID to filter by. If empty, returns\nnegatives across all campaigns."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1332)

<a id="tool-get-search-terms"></a>

### `get_search_terms`

Get search terms report — what users actually typed before clicking your ads.

Critical for finding negative keyword opportunities and understanding user
intent. Returns search term, campaign, ad group, impressions, clicks,
conversions.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "compact": {
      "default": false,
      "type": "boolean",
      "description": "When true (for audits/overviews), returns totals, the top-10\nterms by clicks, ready-made negative-keyword waste candidates\n(5+ clicks, zero conversions), and top converters (~90% smaller)."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1297)

<a id="tool-propose-brand-list"></a>

### `propose_brand_list`

Draft a brand list and optionally attach it to campaigns — returns a PREVIEW.

Creates a SharedSet of type BRANDS, fills it with brands, and — when
campaign_ids is given — attaches it to those campaigns.

Returns a preview with a plan_id; nothing changes until the returned
plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "list_name": {
      "type": "string",
      "description": "Name for the new list, as it should appear in Google Ads."
    },
    "brand_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Commercial Knowledge Graph MIDs — the `id` field from\nsuggest_brands / check_brand_names, which resolve names; a\ndisplay name alone cannot be written. Duplicates are dropped."
    },
    "campaign_ids": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Optional numeric campaign IDs. When omitted, the list is\ncreated without being used yet; attach_brand_list_to_campaigns\nattaches it later."
    },
    "negative": {
      "default": true,
      "type": "boolean",
      "description": "True (default) excludes the brands from those campaigns;\nFalse restricts targeting to them instead."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "list_name",
    "brand_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5927)

<a id="tool-propose-negative-keyword-list"></a>

### `propose_negative_keyword_list`

Draft a shared negative keyword list and attach it to a campaign — returns a PREVIEW.

Creates a reusable negative keyword list (shared set) that can later be
applied to multiple campaigns, whereas add_negative_keywords adds negatives
directly to one campaign. Returns a preview with a plan_id; nothing changes
until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the campaign the new list is attached to."
    },
    "list_name": {
      "type": "string",
      "description": "Name of the new shared negative keyword list."
    },
    "keywords": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Negative keyword texts to put in the list (at least one)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    },
    "match_type": {
      "default": "EXACT",
      "type": "string",
      "description": "Match type applied to every keyword: \"EXACT\" (default),\n\"PHRASE\", or \"BROAD\" (case-insensitive)."
    }
  },
  "required": [
    "campaign_id",
    "list_name",
    "keywords"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3240)

<a id="tool-remove-from-brand-list"></a>

### `remove_from_brand_list`

Remove brands from a brand list — returns a PREVIEW.

SharedCriteria have no status field, so removal is the only way to take a
brand out of a list — there is nothing to pause. Removing a brand does not
detach the list from any campaign.

Returns a preview with a plan_id; nothing changes until the returned
plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "shared_set_id": {
      "type": "string",
      "description": "Numeric list ID from get_brand_lists."
    },
    "criterion_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Numeric criterion_id values from get_brand_list_brands.\nThis is irreversible — the brand leaves the list immediately."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "shared_set_id",
    "criterion_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5998)

<a id="tool-suggest-brands"></a>

### `suggest_brands`

Resolve a brand name to the brands Google recognizes for it.

Mirrors the brand picker in the Google Ads UI
(BrandSuggestionService.SuggestBrands): takes a free-text name such as
"EscapeGame München" or "NoWayOut" and returns the matching brands with
their ID, display name, state, and associated URLs.

The returned brand ID is the Commercial Knowledge Graph ID. Brand
criteria — brand lists, brand exclusions — target that ID, not a display
name, so a name is resolved here before it can go into a brand list.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "brand_prefix": {
      "type": "string",
      "description": "The brand name to look up, free text (e.g. \"NoWayOut\")."
    },
    "selected_brand_ids": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Commercial Knowledge Graph MIDs already picked,\nhanded back so Google keeps them in the suggestion set while the\nprefix narrows. Optional."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "brand_prefix"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5788)

## Campaigns, budgets, bidding, and targeting

<a id="tool-add-negative-locations"></a>

### `add_negative_locations`

Draft negative geo location additions — returns a PREVIEW.

Excludes cities/regions from a campaign while keeping broader positive
targets such as State of Sao Paulo. Returns a preview with a plan_id;
nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the campaign to add the location exclusions to."
    },
    "geo_target_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Numeric Google geo target constant IDs to exclude (e.g.\n\"1001773\"). Duplicates are collapsed; non-numeric IDs are rejected."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "campaign_id",
    "geo_target_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3206)

<a id="tool-draft-ad-group"></a>

### `draft_ad_group`

Draft a new ad group within an existing campaign — returns a PREVIEW, does NOT create.

Creates an ad group (ENABLED, type SEARCH_STANDARD) in the specified campaign,
optionally with keywords in the same atomic operation. Only SEARCH campaigns
are supported. Ads are not included, so the ad group cannot serve until one
of its ads is created and enabled.

Returns a preview with a plan_id plus warnings (BROAD keywords on a
non-Smart-Bidding campaign, a duplicate ad group name, a CPC bid that Smart
Bidding ignores); nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "The campaign to add the ad group to (numeric ID as returned\nby get_campaign_performance)."
    },
    "ad_group_name": {
      "type": "string",
      "description": "Name for the new ad group."
    },
    "keywords": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional list of {\"text\": \"keyword\", \"match_type\":\n\"EXACT|PHRASE|BROAD\"}."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    },
    "cpc_bid_micros": {
      "default": 0,
      "type": "integer",
      "description": "Optional ad group CPC bid in micros (1,000,000 = one\nunit of the account's currency); only used by MANUAL_CPC campaigns.\n0 means no ad-group bid; must not be negative."
    }
  },
  "required": [
    "campaign_id",
    "ad_group_name"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2718)

<a id="tool-draft-ai-max-settings"></a>

### `draft_ai_max_settings`

Draft AI Max controls for a Search campaign — returns a PREVIEW.

AI Max is the container that makes brand exclusions usable in Search:
Google rejects a brand list on a plain Search campaign ("For search
advertising channel, brand lists can only be applied to exclusive
targeting, broad match campaigns for inclusive targeting or PMax generated
campaigns"). Turning AI Max on while leaving its automations running is the
trap, so both belong to the same plan. An automation the caller never mentioned is
refused outright (the plan says which switch to pass); one named explicitly
(disable_search_term_matching=False, text_asset_automation="OPTED_IN") is
planned with requires_double_confirm=True, because switching to AI Max with
its automations is a real configuration some accounts want.

Reads the campaign and its ad groups first, so the preview names concrete
ad groups and shows current values per knob. Returns a preview with a
plan_id; nothing is written until confirm_and_apply runs.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the Search campaign to prepare."
    },
    "enable_ai_max": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Value for campaign.ai_max_setting.enable_ai_max. When\nomitted, it stays untouched."
    },
    "disable_search_term_matching": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Value for\nad_group.ai_max_ad_group_setting.disable_search_term_matching on the\nselected ad groups. When omitted, they stay untouched."
    },
    "ad_group_ids": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Explicit ad group IDs. Empty means every non-removed ad\ngroup of the campaign."
    },
    "include_paused_ad_groups": {
      "default": true,
      "type": "boolean",
      "description": "Default true — paused groups are set as well,\nso re-enabling one later cannot silently restore search term\nmatching. REMOVED ad groups are never touched."
    },
    "text_asset_automation": {
      "default": "UNCHANGED",
      "type": "string",
      "description": "OPTED_IN, OPTED_OUT or UNCHANGED (default) for\nTEXT_ASSET_AUTOMATION."
    },
    "final_url_expansion": {
      "default": "UNCHANGED",
      "type": "string",
      "description": "OPTED_IN, OPTED_OUT or UNCHANGED (default) for\nFINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION (the v25 field name for\nfinal URL expansion)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3414)

<a id="tool-draft-campaign"></a>

### `draft_campaign`

Draft a full campaign structure — returns a PREVIEW, does NOT create anything.

Creates: CampaignBudget + Campaign (PAUSED) + AdGroup + optional Keywords
\+ geo targeting + language targeting.
Ads are NOT included — draft_responsive_search_ad adds them once the
campaign exists. Only SEARCH campaigns can be created: Performance Max
needs an asset group with all its assets in one request, and DISPLAY,
SHOPPING and VIDEO need channel-specific settings and ad group types, so
the draft refuses them.

Returns a preview with a plan_id plus any warnings (e.g. a daily budget
below 5x target CPA, MANUAL_CPC); nothing changes until confirm_and_apply
applies the returned plan_id.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_name": {
      "type": "string",
      "description": "Name of the new campaign."
    },
    "daily_budget": {
      "type": "number",
      "description": "Daily budget in the account's currency (not micros);\nmust be greater than 0 and at most the config's max_daily_budget."
    },
    "bidding_strategy": {
      "type": "string",
      "description": "MAXIMIZE_CONVERSIONS | TARGET_CPA | TARGET_ROAS |\nMAXIMIZE_CONVERSION_VALUE | TARGET_SPEND | MANUAL_CPC. BROAD\nkeywords require a Smart Bidding strategy (MAXIMIZE_CONVERSIONS,\nMAXIMIZE_CONVERSION_VALUE, TARGET_CPA, TARGET_ROAS)."
    },
    "geo_target_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "REQUIRED list of geo target constant IDs.\nCommon: \"2276\" Germany, \"2040\" Austria, \"2756\" Switzerland, \"2840\" USA,\n\"2826\" UK, \"2250\" France. Full list: Google Ads API geo target constants."
    },
    "language_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "REQUIRED list of language constant IDs.\nCommon: \"1001\" German, \"1000\" English, \"1002\" French, \"1003\" Spanish,\n\"1004\" Italian, \"1014\" Portuguese. Full list: Google Ads API\nlanguage constants."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    },
    "target_cpa": {
      "default": 0,
      "type": "number",
      "description": "Target cost per acquisition in the account's currency;\nrequired if bidding_strategy is TARGET_CPA, optional target for\nMAXIMIZE_CONVERSIONS. 0 means none."
    },
    "target_roas": {
      "default": 0,
      "type": "number",
      "description": "Target return on ad spend as a ratio (e.g. 4.0 = 400%);\nrequired if bidding_strategy is TARGET_ROAS, optional target for\nMAXIMIZE_CONVERSION_VALUE. 0 means none."
    },
    "channel_type": {
      "default": "SEARCH",
      "type": "string",
      "description": "SEARCH (default). DISPLAY, SHOPPING, VIDEO and\nPERFORMANCE_MAX are refused with the reason (see above)."
    },
    "ad_group_name": {
      "default": "",
      "type": "string",
      "description": "Name of the initial ad group. Empty uses campaign_name."
    },
    "keywords": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional list of {\"text\": \"keyword\", \"match_type\":\n\"EXACT|PHRASE|BROAD\"} added to the initial ad group."
    },
    "search_partners_enabled": {
      "default": false,
      "type": "boolean",
      "description": "Include ads on Search partners (SEARCH\ncampaigns only)."
    },
    "display_network_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Enable Search campaign display expansion\n(SEARCH campaigns only). Defaults to off."
    },
    "display_expansion_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Alias for display_network_enabled; both must\nmatch when both are given."
    },
    "max_cpc": {
      "default": 0,
      "type": "number",
      "description": "In the account's currency: the manual CPC bid for the initial\nad group when bidding_strategy is MANUAL_CPC, or the Maximize Clicks\nCPC cap when bidding_strategy is TARGET_SPEND. Not allowed with\nother strategies; 0 means none."
    }
  },
  "required": [
    "campaign_name",
    "daily_budget",
    "bidding_strategy",
    "geo_target_ids",
    "language_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2624)

<a id="tool-draft-demographic-targeting"></a>

### `draft_demographic_targeting`

Draft demographic targeting (age/gender/parental status/income) — returns a PREVIEW.

By default, Google Ads serves to all demographic segments. This tool adds
criteria that EXCLUDE a segment (negative=True, default) or NARROW
targeting to it (negative=False — uncommon). Takes exactly one of
ad_group_id or campaign_id, and at least one of the four demographic lists
must contain a value.

Returns a preview with a plan_id, plus warnings when the change narrows
targeting, excludes 'undetermined' users, or excludes nearly a whole
dimension; nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    },
    "ad_group_id": {
      "default": "",
      "type": "string",
      "description": "Numeric ad group ID to add the criteria to. Mutually\nexclusive with campaign_id."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Numeric campaign ID to add the criteria to. Mutually\nexclusive with ad_group_id; campaign-level criteria can only be\nexclusions (negative=True)."
    },
    "age_ranges": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Age buckets '18-24', '25-34', '35-44', '45-54', '55-64',\n'65+', 'undetermined' (or canonical names such as AGE_RANGE_18_24).\nGoogle's buckets are FIXED — 'Exclude 23-35' has no exact mapping\nand needs a choice of buckets."
    },
    "genders": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "'female', 'male', 'undetermined'."
    },
    "parental_statuses": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "'parent', 'not_a_parent', 'undetermined'."
    },
    "income_ranges": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "PERCENTILES (not currency): 'top-10', '11-20', '21-30',\n'31-40', '41-50', 'lower-50', 'undetermined'. Available in select\ncountries only (US, AU, JP, etc.)."
    },
    "negative": {
      "default": true,
      "type": "boolean",
      "description": "True (default) excludes the listed segments; False adds\npositive criteria that narrow an ad group's targeting to them."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3521)

<a id="tool-enable-entity"></a>

### `enable_entity`

Draft enabling a paused campaign, ad group, ad, or keyword — returns a PREVIEW.

Returns a preview with a plan_id (target status ENABLED); nothing changes
until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "\"campaign\", \"ad_group\", \"ad\", or \"keyword\"."
    },
    "entity_id": {
      "type": "string",
      "description": "ID in the format for its type. campaign: campaign ID (e.g.\n\"12345678\"); ad_group: ad group ID (e.g. \"12345678\"); ad:\n\"adGroupId~adId\" (e.g. \"12345678~987654\"; a bare ad ID is resolved\nto its ad group at apply time); keyword: \"adGroupId~criterionId\"\n(e.g. \"12345678~987654\")."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "entity_type",
    "entity_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3752)

<a id="tool-get-demographic-targeting"></a>

### `get_demographic_targeting`

List demographic targeting criteria (age, gender, parental status, income).

Takes exactly one of ad_group_id or campaign_id. Returns each
criterion's value, whether it's negative (excluded) or positive
(narrowing), status, and a remove_id (composite resource ID) that
can be passed directly to remove_entity with
entity_type='ad_group_criterion' or 'campaign_criterion'.

By default, Google Ads serves ads to ALL demographic segments — a
criterion only appears here once a segment has been actively excluded
or narrowed.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "default": "",
      "type": "string",
      "description": "Numeric ad group ID. Mutually exclusive with campaign_id."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Numeric campaign ID. Mutually exclusive with ad_group_id."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1619)

<a id="tool-pause-entity"></a>

### `pause_entity`

Draft pausing a campaign, ad group, ad, or keyword — returns a PREVIEW.

Pausing is reversible with enable_entity. Returns a preview with a plan_id
(target status PAUSED); nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "\"campaign\", \"ad_group\", \"ad\", or \"keyword\"."
    },
    "entity_id": {
      "type": "string",
      "description": "ID in the format for its type. campaign: campaign ID (e.g.\n\"12345678\"); ad_group: ad group ID (e.g. \"12345678\"); ad:\n\"adGroupId~adId\" (e.g. \"12345678~987654\"; a bare ad ID is resolved\nto its ad group at apply time); keyword: \"adGroupId~criterionId\"\n(e.g. \"12345678~987654\")."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "entity_type",
    "entity_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3720)

<a id="tool-remove-entity"></a>

### `remove_entity`

Draft REMOVING an entity — returns a PREVIEW. This is IRREVERSIBLE.

Removed entities cannot be re-enabled; pause_entity is the reversible way
to temporarily disable something. Returns a preview with a plan_id and
requires_double_confirm=true; nothing changes until confirm_and_apply
applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "\"campaign\", \"ad_group\", \"ad\", \"keyword\", \"negative_keyword\",\n\"shared_criterion\", \"campaign_asset\", \"asset\", \"customer_asset\",\n\"ad_group_criterion\", or \"campaign_criterion\"."
    },
    "entity_id": {
      "type": "string",
      "description": "The resource ID. campaign / ad_group / asset: simple numeric\nID. ad: \"adGroupId~adId\" (a bare ad ID is resolved to its ad group).\nkeyword and ad_group_criterion: \"adGroupId~criterionId\".\nnegative_keyword and campaign_criterion: \"campaignId~criterionId\"\n(the resource_id field from get_negative_keywords).\nshared_criterion: \"sharedSetId~criterionId\" (the resource_id field\nfrom get_negative_keyword_list_keywords). campaign_asset:\n\"campaignId~assetId~fieldType\". customer_asset: \"assetId~fieldType\"."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "entity_type",
    "entity_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3784)

<a id="tool-update-ad-group"></a>

### `update_ad_group`

Draft an ad group update for name and/or manual CPC bid — returns a PREVIEW.

A bid change applies only when the campaign uses MANUAL_CPC: automated
bidding strategies ignore ad-group CPC bids, so such a change is refused
(for Maximize Clicks the campaign cpc_bid_ceiling, set through
update_campaign, is the active constraint). Bid increases above the
configured safety.max_bid_increase_pct are refused. Returns a preview with
a plan_id; nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "type": "string",
      "description": "Numeric ID of the ad group to update."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    },
    "ad_group_name": {
      "default": "",
      "type": "string",
      "description": "New ad group name. Empty leaves the name unchanged."
    },
    "max_cpc": {
      "default": 0,
      "type": "number",
      "description": "New maximum CPC bid in the account's currency (an amount, not\nmicros). 0 leaves the bid unchanged; negative values are rejected.\nAt least one of ad_group_name or max_cpc is required."
    }
  },
  "required": [
    "ad_group_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3584)

<a id="tool-update-campaign"></a>

### `update_campaign`

Draft an update to an existing campaign — returns a PREVIEW, does NOT apply.

Only the parameters passed are changed; omitted ones stay as they are, and at
least one change is required. Replacing geo targets keeps the campaign's
negative geo exclusions (the preview lists them).

Returns a preview with a plan_id plus any warnings; nothing changes until
confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "The numeric ID of the campaign to update (required)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    },
    "bidding_strategy": {
      "default": "",
      "type": "string",
      "description": "MAXIMIZE_CONVERSIONS | TARGET_CPA | TARGET_ROAS |\nMAXIMIZE_CONVERSION_VALUE | TARGET_SPEND | MANUAL_CPC. Empty leaves\nthe strategy unchanged."
    },
    "target_cpa": {
      "default": 0,
      "type": "number",
      "description": "Target CPA in the account's currency; required if\nbidding_strategy is TARGET_CPA. 0 leaves it unchanged."
    },
    "target_roas": {
      "default": 0,
      "type": "number",
      "description": "Target ROAS as a ratio (e.g. 4.0 = 400%); required if\nbidding_strategy is TARGET_ROAS. 0 leaves it unchanged."
    },
    "daily_budget": {
      "default": 0,
      "type": "number",
      "description": "New daily budget in the account's currency (not micros),\nat most the config's max_daily_budget. 0 leaves it unchanged."
    },
    "geo_target_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "REPLACES all positive geo targets; must not be empty\nwhen given. Common IDs: \"2276\" Germany, \"2040\" Austria, \"2756\"\nSwitzerland, \"2840\" USA, \"2826\" UK."
    },
    "language_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "REPLACES all language targets; must not be empty when\ngiven. Common IDs: \"1001\" German, \"1000\" English, \"1002\" French,\n\"1003\" Spanish, \"1004\" Italian."
    },
    "search_partners_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Include ads on Search partners. Omitted leaves\nthe setting unchanged."
    },
    "display_network_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Enable Search campaign display expansion.\nOmitted leaves the setting unchanged."
    },
    "display_expansion_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Alias for display_network_enabled; both must\nmatch when both are given."
    },
    "max_cpc": {
      "default": 0,
      "type": "number",
      "description": "Maximize Clicks CPC cap in the account's currency when\nbidding_strategy is TARGET_SPEND, or when the existing campaign\nalready uses TARGET_SPEND. Increases are limited by the config's\nmax_bid_increase_pct. 0 leaves it unchanged."
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2762)

## Ads and creative assets

<a id="tool-draft-callouts"></a>

### `draft_callouts`

Draft campaign callout assets — returns a PREVIEW.

Creates callout assets and links them to the campaign. Returns a preview
with a plan_id; nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the campaign to attach the callouts to."
    },
    "callouts": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Callout texts (at least one), each non-empty and at most 25\ncharacters after trimming."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "campaign_id",
    "callouts"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3621)

<a id="tool-draft-image-assets"></a>

### `draft_image_assets`

Draft campaign image assets from local files or public image URLs — returns a PREVIEW.

At least one image in total is required across image_paths and image_urls.
Images must be PNG, JPEG or GIF and at most 5120 KB (Google's limit).
URL images are downloaded now and checked; applying re-downloads them
and refuses if the image changed since the preview. Returns a preview with
a plan_id and a per-image summary; nothing changes until confirm_and_apply
applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the campaign to attach the images to."
    },
    "image_paths": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Local PNG/JPEG/GIF file paths on the machine running\nAdLoop. Not available on a hosted server, where image_urls\napplies instead."
    },
    "image_urls": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Public http(s) URLs of PNG/JPEG/GIF images. Links to\nprivate, local or internal addresses are refused."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3682)

<a id="tool-draft-responsive-search-ad"></a>

### `draft_responsive_search_ad`

Draft a Responsive Search Ad — returns a PREVIEW, does NOT create the ad.

The preview shows exactly what will be created; confirm_and_apply executes
the returned plan_id. The ad is created PAUSED. final_url is checked for
reachability first and an unreachable URL is refused. Google caps: at most
2 headlines per pin slot, at most 1 description per pin slot. Mixed
plain-string and dict entries are allowed within a single call (e.g. brand
pinned to HEADLINE_1, the rest unpinned). Warnings note fewer than 8
headlines or 3 descriptions.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "type": "string",
      "description": "Numeric ID of the ad group that gets the ad."
    },
    "headlines": {
      "items": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "additionalProperties": true,
            "type": "object"
          }
        ]
      },
      "type": "array",
      "description": "3-15 headlines, max 30 chars each. Each entry is a plain\nstring (unpinned) or {\"text\": \"...\", \"pinned_field\": \"HEADLINE_1\"};\nvalid pins are HEADLINE_1, HEADLINE_2, HEADLINE_3."
    },
    "descriptions": {
      "items": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "additionalProperties": true,
            "type": "object"
          }
        ]
      },
      "type": "array",
      "description": "2-4 descriptions, max 90 chars each. Each entry is a plain\nstring (unpinned) or {\"text\": \"...\", \"pinned_field\": \"DESCRIPTION_1\"};\nvalid pins are DESCRIPTION_1, DESCRIPTION_2."
    },
    "final_url": {
      "type": "string",
      "description": "Landing page URL the ad links to; must be reachable."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    },
    "path1": {
      "default": "",
      "type": "string",
      "description": "Optional first display-URL path segment (Google allows up to 15\nchars)."
    },
    "path2": {
      "default": "",
      "type": "string",
      "description": "Optional second display-URL path segment (Google allows up to 15\nchars)."
    }
  },
  "required": [
    "ad_group_id",
    "headlines",
    "descriptions",
    "final_url"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2836)

<a id="tool-draft-sitelinks"></a>

### `draft_sitelinks`

Draft sitelink extensions for a campaign — returns a PREVIEW.

Sitelinks appear as additional links below your ad, increasing click area
and directing users to specific pages. Every final_url is fetched and an
unreachable URL (HTTP 4xx/5xx) blocks the draft. Google recommends at least
4 sitelinks per campaign; fewer than 2 may not show. Returns a preview with
a plan_id and any warnings; nothing changes until confirm_and_apply applies
it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the campaign to attach sitelinks to."
    },
    "sitelinks": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "type": "array",
      "description": "List of dicts (at least one), each with link_text (str,\nrequired, max 25 chars) — the clickable text shown; final_url (str,\nrequired) — destination URL for this sitelink; description1 (str,\noptional, max 35 chars) — first description line; description2\n(str, optional, max 35 chars) — second description line."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "campaign_id",
    "sitelinks"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3823)

<a id="tool-draft-structured-snippets"></a>

### `draft_structured_snippets`

Draft campaign structured snippet assets — returns a PREVIEW.

Creates structured snippet assets and links them to the campaign. Returns a
preview with a plan_id; nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric ID of the campaign to attach the snippets to."
    },
    "snippets": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "type": "array",
      "description": "At least one dict with \"header\" and \"values\". header is one of\nAmenities, Brands, Courses, Degree programs, Destinations, Featured\nHotels, Insurance coverage, Models, Neighborhoods, Services, Shows,\nStyles, Types (exact spelling). values is a list of 3-10 non-empty\nstrings, each at most 25 characters."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes optional). Defaults to\nthe configured account."
    }
  },
  "required": [
    "campaign_id",
    "snippets"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3650)

<a id="tool-get-detailed-asset-performance"></a>

### `get_detailed_asset_performance`

Get top-performing asset combinations for Performance Max campaigns.

Shows which headline + description + image combinations Google selects
most often. Returns each combination with the assets used and their field
types. This data helps identify which creative elements work well together.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Optional numeric ID to filter to a single PMax campaign."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1556)

<a id="tool-get-pmax-assets"></a>

### `get_pmax_assets`

List the assets of Performance Max campaigns with type, status and content.

Returns each asset's field_type (HEADLINE, DESCRIPTION, MARKETING_IMAGE,
YOUTUBE_VIDEO, etc.), primary_status (ELIGIBLE, NOT_ELIGIBLE, PAUSED,
PENDING), and content (text or image URL), plus by_status and
by_field_type summaries.

Per-asset performance labels (BEST/GOOD/LOW) are not available for
PMax assets in the Google Ads API. get_detailed_asset_performance reports
which asset combinations Google selects most — the closest proxy for
individual asset quality.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Optional numeric ID to filter to a single PMax campaign."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1520)

<a id="tool-update-responsive-search-ad"></a>

### `update_responsive_search_ad`

Update mutable fields on an existing RSA in place — returns a PREVIEW.

Edits an existing RSA without creating a new ad; the ad keeps its ID.
Google Ads API v23 (``AdService.MutateAds``) permits in-place mutation of
``final_urls``, ``path1``, ``path2``, ``headlines``, and ``descriptions``.
At least one mutation must be requested.

IMPORTANT: replacing headlines or descriptions is NOT a free in-place
edit. Even though the ad ID is preserved, swapping the creative text
RESETS the ad's asset-combination learning and performance history and
sends the ad BACK THROUGH Google policy review — Google treats the
creative as new for optimization. URL-only and path-only edits do not
incur this. When headlines/descriptions change, the returned preview
includes a ``warnings`` entry stating this trade-off before anything
is applied.

Returns a preview with a plan_id; nothing changes until confirm_and_apply
applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Numeric ID of the existing responsive search ad."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    },
    "headlines": {
      "anyOf": [
        {
          "items": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "LIST-REPLACE: None or [] means no change; a non-empty list\nfully swaps in for the existing headlines. Google's RSA constraints\napply: 3-15 headlines, max 30 chars each, at most 2 per pin slot.\nEach entry is a plain string (unpinned) or {\"text\": \"...\",\n\"pinned_field\": \"HEADLINE_1\"} (HEADLINE_1-3)."
    },
    "descriptions": {
      "anyOf": [
        {
          "items": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "LIST-REPLACE: None or [] means no change; a non-empty list\nfully swaps in. 2-4 descriptions, max 90 chars each, at most 1 per\npin slot (DESCRIPTION_1, DESCRIPTION_2). Same entry format as\nheadlines."
    },
    "final_url": {
      "default": "",
      "type": "string",
      "description": "Empty means no change; non-empty replaces the final URL and\nis checked for reachability."
    },
    "path1": {
      "default": "",
      "type": "string",
      "description": "Empty means no change; non-empty sets the first display path\n(max 15 chars)."
    },
    "path2": {
      "default": "",
      "type": "string",
      "description": "Empty means no change; non-empty sets the second display path\n(max 15 chars)."
    },
    "clear_path1": {
      "default": false,
      "type": "boolean",
      "description": "True sets path1 to an empty string (overrides path1)."
    },
    "clear_path2": {
      "default": false,
      "type": "boolean",
      "description": "True sets path2 to an empty string (overrides path2)."
    }
  },
  "required": [
    "ad_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2887)

## Audiences and audience insights

<a id="tool-get-audience-performance"></a>

### `get_audience_performance`

Get audience segment performance metrics.

Returns performance by audience type — remarketing lists (USER_LIST),
in-market segments (USER_INTEREST), affinity, demographics (AGE_RANGE,
GENDER), etc. Shows display_name, impressions, clicks, cost, conversions,
CTR, and CPC for each audience.

Works for campaigns with explicit audience targeting (Search, Display).
PMax audience targeting is automatic and may not appear in this report.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Optional numeric ID to filter to a single campaign."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1582)

## Conversions and measurement

<a id="tool-draft-assign-custom-conversion-goal"></a>

### `draft_assign_custom_conversion_goal`

Point a campaign at a custom conversion goal — returns a PREVIEW.

Sets goal_config_level=CAMPAIGN and the goal on that campaign's conversion
goal config. Nothing else changes: conversion actions, bidding, budgets and
the account-level goals stay as they are.

A campaign must have at least one goal configured when it switches to
campaign level — Google answers EMPTY_CONVERSION_GOALS otherwise. That is
why this tool assigns a goal instead of clearing goals;
draft_clear_custom_conversion_goal goes back to the account level.

If the campaign already uses exactly this goal, nothing is planned and the
result says `already_configured`. The preview carries a note that changing
what a campaign optimises for restarts its Smart Bidding learning period.

The returned plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric campaign ID to configure."
    },
    "custom_conversion_goal_id": {
      "type": "string",
      "description": "Numeric goal ID from get_custom_conversion_goals."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "campaign_id",
    "custom_conversion_goal_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3103)

<a id="tool-draft-clear-custom-conversion-goal"></a>

### `draft_clear_custom_conversion_goal`

Put a campaign back on the account-level goals — returns a PREVIEW.

Sets goal_config_level=CUSTOMER and clears the custom goal: the rollback for
draft_assign_custom_conversion_goal. The account-level goals themselves are
not touched.

The returned plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Numeric campaign ID to reset."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3146)

<a id="tool-draft-create-conversion-action"></a>

### `draft_create_conversion_action`

Draft a new Google Ads ConversionAction — returns a PREVIEW.

Returns a preview with a plan_id (plus warnings where relevant); nothing
changes until confirm_and_apply applies it. SMART_CAMPAIGN_* and
GOOGLE_HOSTED types are auto-managed by Google and rejected with
MUTATE_NOT_ALLOWED.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "name": {
      "type": "string",
      "description": "Conversion action name as it appears in Google Ads. Required."
    },
    "type_": {
      "type": "string",
      "description": "ConversionActionType enum value, e.g. AD_CALL, WEBSITE_CALL,\nWEBPAGE, WEBPAGE_CODELESS, GOOGLE_ANALYTICS_4_CUSTOM,\nGOOGLE_ANALYTICS_4_PURCHASE, UPLOAD_CALLS, UPLOAD_CLICKS."
    },
    "category": {
      "default": "DEFAULT",
      "type": "string",
      "description": "ConversionActionCategory enum value, e.g. PHONE_CALL_LEAD,\nSUBMIT_LEAD_FORM, PURCHASE, ... (default DEFAULT)."
    },
    "default_value": {
      "default": 0,
      "type": "number",
      "description": "Value attributed to each conversion, in currency_code\nunits (not micros). Must be >= 0. A positive default_value with\nalways_use_default_value=False is a legal \"fallback\" config: the\npreview warns but does NOT flip the flag."
    },
    "currency_code": {
      "default": "USD",
      "type": "string",
      "description": "3-letter ISO 4217 currency code for default_value\n(default USD)."
    },
    "always_use_default_value": {
      "default": false,
      "type": "boolean",
      "description": "True ignores transaction values from the\ntag/import and always uses default_value; False uses default_value\nonly as a fallback when no value is supplied."
    },
    "counting_type": {
      "default": "ONE_PER_CLICK",
      "type": "string",
      "description": "ONE_PER_CLICK (default; one conversion per click, typical\nfor lead gen) or MANY_PER_CLICK (every conversion counts, typical\nfor ecommerce)."
    },
    "phone_call_duration_seconds": {
      "default": 0,
      "type": "integer",
      "description": "Minimum call length in seconds for a call\nto count; only meaningful for call conversions (PHONE_CALL_LEAD\ncategory). 0 leaves Google's default."
    },
    "primary_for_goal": {
      "default": true,
      "type": "boolean",
      "description": "True (default) makes it a Primary action that Smart\nBidding optimizes toward; False makes it Secondary (recorded only)."
    },
    "include_in_conversions_metric": {
      "default": true,
      "type": "boolean",
      "description": "IMMUTABLE on create — Google derives it\nfrom the category, so this value is not sent; change it later via\ndraft_update_conversion_action."
    },
    "click_through_window_days": {
      "default": 0,
      "type": "integer",
      "description": "Click-through attribution window in days,\n1-90. 0 leaves Google's default."
    },
    "view_through_window_days": {
      "default": 0,
      "type": "integer",
      "description": "View-through attribution window in days,\n1-30. 0 leaves Google's default."
    },
    "attribution_model": {
      "default": "",
      "type": "string",
      "description": "AttributionModel enum value, e.g.\nGOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN. Empty leaves Google's default."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes allowed). Defaults\nto the configured account."
    }
  },
  "required": [
    "name",
    "type_"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5272)

<a id="tool-draft-custom-conversion-goal"></a>

### `draft_custom_conversion_goal`

Create a custom conversion goal — returns a PREVIEW.

The goal bundles conversion actions into a named set that campaigns can
then be pointed at with draft_assign_custom_conversion_goal. Only the goal
is created: conversion actions are read for validation and never modified.
It is always created ENABLED — a goal created as REMOVED would be invisible
to every other tool, so there is nothing to plan.

If a goal with the same name and exactly the same conversion actions
already exists, nothing is planned and the result says `already_exists`
with that goal's ID (REMOVED goals do not count). A name that exists with
different actions is changed with draft_update_custom_conversion_goal.

The returned plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "name": {
      "type": "string",
      "description": "Name for the new goal, e.g. \"OHL | Kauf + qualifizierte Anrufe\"."
    },
    "conversion_action_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Numeric conversion action IDs. Duplicates are\ncollapsed; unknown or REMOVED actions are refused."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "name",
    "conversion_action_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3021)

<a id="tool-draft-remove-conversion-action"></a>

### `draft_remove_conversion_action`

Draft a REMOVAL of a ConversionAction — returns a PREVIEW.

Removal stops counting and drops the action from goal lists; historical
data is preserved but the action is irreversible. SMART_CAMPAIGN_* and
GOOGLE_HOSTED types reject removal with MUTATE_NOT_ALLOWED. Returns a
preview with a plan_id; nothing changes until confirm_and_apply applies it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "conversion_action_id": {
      "type": "string",
      "description": "Numeric ConversionAction ID, e.g. from SELECT\nconversion_action.id, conversion_action.name FROM conversion_action."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes allowed). Defaults\nto the configured account."
    }
  },
  "required": [
    "conversion_action_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5436)

<a id="tool-draft-update-conversion-action"></a>

### `draft_update_conversion_action`

Draft a partial UPDATE of an existing ConversionAction — returns PREVIEW.

Only parameters passed non-empty/non-default are sent to the API.
Covers renaming, demoting a Primary to Secondary, changing value,
adjusting the call-duration threshold, or changing attribution.
SMART_CAMPAIGN_* and GOOGLE_HOSTED types reject mutations with
MUTATE_NOT_ALLOWED at apply time. Returns a preview with a plan_id (plus
warnings where relevant); nothing changes until confirm_and_apply applies
it.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "conversion_action_id": {
      "type": "string",
      "description": "Numeric ConversionAction ID. It comes from:\nSELECT conversion_action.id, conversion_action.name FROM\nconversion_action."
    },
    "name": {
      "default": "",
      "type": "string",
      "description": "New name. Empty keeps the current name."
    },
    "primary_for_goal": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "True makes it Primary (Smart Bidding optimizes toward\nit); False demotes it to Secondary. Omit to leave unchanged."
    },
    "default_value": {
      "default": 0,
      "type": "number",
      "description": "New default value in the action's currency (not micros),\n>= 0. 0 leaves it unchanged."
    },
    "currency_code": {
      "default": "",
      "type": "string",
      "description": "New 3-letter ISO 4217 currency code. Empty leaves it\nunchanged."
    },
    "always_use_default_value": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "True always uses default_value; False uses\nit only as a fallback when the tag/import supplies no value (the\npreview warns when combined with a positive default_value). Omit to\nleave unchanged."
    },
    "counting_type": {
      "default": "",
      "type": "string",
      "description": "ONE_PER_CLICK or MANY_PER_CLICK. Empty leaves it\nunchanged."
    },
    "phone_call_duration_seconds": {
      "default": 0,
      "type": "integer",
      "description": "Minimum call length in seconds for a call\nto count. 0 leaves it unchanged."
    },
    "include_in_conversions_metric": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "True shows the action in the\n\"Conversions\" column; False in \"All conversions\" only. Mutable here\n(unlike on create). Omit to leave unchanged."
    },
    "click_through_window_days": {
      "default": 0,
      "type": "integer",
      "description": "Click-through attribution window in days,\n1-90. 0 leaves it unchanged."
    },
    "view_through_window_days": {
      "default": 0,
      "type": "integer",
      "description": "View-through attribution window in days,\n1-30. 0 leaves it unchanged."
    },
    "attribution_model": {
      "default": "",
      "type": "string",
      "description": "AttributionModel enum value, e.g.\nGOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN. Empty leaves it unchanged."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, dashes allowed). Defaults\nto the configured account."
    }
  },
  "required": [
    "conversion_action_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5356)

<a id="tool-draft-update-custom-conversion-goal"></a>

### `draft_update_custom_conversion_goal`

Rename and/or re-scope an existing custom conversion goal — PREVIEW.

conversion_action_ids REPLACES the whole action list, it does not append.
An empty parameter stays unchanged. The preview shows the action
list before and after.

The returned plan_id is applied with confirm_and_apply.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "custom_conversion_goal_id": {
      "type": "string",
      "description": "Numeric goal ID from get_custom_conversion_goals."
    },
    "name": {
      "default": "",
      "type": "string",
      "description": "New name. Empty leaves the name unchanged."
    },
    "conversion_action_ids": {
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "The complete new action list. Empty leaves the\nactions unchanged."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "required": [
    "custom_conversion_goal_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3065)

<a id="tool-draft-upload-call-conversions"></a>

### `draft_upload_call_conversions`

Draft an offline CALL-conversion upload from a CSV — returns a PREVIEW.

Uploads call conversions via ConversionUploadService.UploadCallConversions,
matching the call against the ad click by the caller's phone number.
The CSV must have columns: Caller's Phone Number,
Call Start Time, Conversion Name, Conversion Time, Conversion Value,
Conversion Currency. The Conversion Name must match an existing
UPLOAD_CALLS-type conversion action — verified against the account while
drafting, so a typo fails here rather than after the upload. Optional
`Ad User Data` and `Ad Personalization` columns carry consent per row.

Local file only: on the hosted server this tool refuses, because it would
read a path on the server rather than the caller's machine.

PII: the caller phone number is required RAW by Google (it cannot be
hashed), so it lives in the plan's apply-only payload — the preview shows
redacted ids and counts, the audit log and `plan.changes` show neither.
Apply uploads exactly what you previewed (no CSV re-read).

Phone numbers are normalized with libphonenumber semantics: a number
carries no country code needs ``default_region``, an extension is dropped,
and the German trunk marker in "+49 (0)89 …" is handled. Rows whose number
stays unusable are skipped and reported in `skipped_rows` instead of being
uploaded to no effect.

Rows that repeat inside one file are named in `dedup_warnings`. A call
upload has no dedup key at Google, so each of them still goes out as its
own conversion — the warning is the only place that says so.

Returns a preview with a plan_id, the row counts, the consent the rows
actually carry (`consent_summary`) and the skipped rows; nothing is
uploaded until that preview is confirmed.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "csv_path": {
      "type": "string",
      "description": "Path of the CSV file holding the upload rows, read on the\nmachine that runs AdLoop. The hosted server refuses this tool\nrather than reading a path of its own."
    },
    "default_region": {
      "default": "",
      "type": "string",
      "description": "ISO 3166-1 alpha-2 country assumed for phone numbers\nthat carry no country code, e.g. \"DE\" for \"0151 12345678\". Empty\nleaves such numbers unusable and the row is skipped."
    },
    "consent": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Consent signals for GDPR/EEA, as an object with \"ad_user_data\"\nand/or \"ad_personalization\", each \"GRANTED\", \"DENIED\" or\n\"UNSPECIFIED\". None sends UNSPECIFIED. A row whose own \"Ad User\nData\" / \"Ad Personalization\" columns are filled in overrides this\nfor that row; empty cells fall back to it."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    }
  },
  "required": [
    "csv_path"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5466)

<a id="tool-draft-upload-enhanced-conversions-for-leads"></a>

### `draft_upload_enhanced_conversions_for_leads`

Draft an Enhanced Conversions for LEADS upload from a CSV — PREVIEW.

Uploads lead conversions via
ConversionUploadService.UploadClickConversions with user_identifiers,
matching hashed customer PII back to the Google users who clicked the ads.
The CSV holds RAW PII in columns: Email, Phone
Number, First Name, Last Name (plus Conversion Name, Conversion Time,
Conversion Value, Conversion Currency; optional Order ID dedup key, and
optional `Ad User Data` / `Ad Personalization` consent columns).

PII is normalized and SHA-256-hashed AT PREVIEW TIME — only the hashes are
stored in the plan. Raw email/phone/name never land in the plan or the
audit log. The target conversion action must be UPLOAD_CLICKS-type.

An Order ID column makes re-uploads dedup instead of double-counting.

Rows that repeat inside one file are named in `dedup_warnings`. Rows
sharing an Order ID count once at Google; two rows with different Order
IDs are two real orders and are not reported.

Local file only: on the hosted server this tool refuses, because it would
read a path on the server rather than the caller's machine.

Returns a preview with a plan_id, the row counts, the consent the rows
actually carry (`consent_summary`) and the skipped rows; nothing is
uploaded until that preview is confirmed.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "csv_path": {
      "type": "string",
      "description": "Path of the CSV file holding the upload rows, read on the\nmachine that runs AdLoop. The hosted server refuses this tool\nrather than reading a path of its own."
    },
    "default_region": {
      "default": "",
      "type": "string",
      "description": "ISO 3166-1 alpha-2 country assumed for phone numbers\nthat carry no country code, e.g. \"DE\" for \"0151 12345678\". Empty\nleaves such numbers unusable; the row still uploads when its email\nor its complete address identifies the lead."
    },
    "consent": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Consent signals for GDPR/EEA, as an object with \"ad_user_data\"\nand/or \"ad_personalization\", each \"GRANTED\", \"DENIED\" or\n\"UNSPECIFIED\". None sends UNSPECIFIED. A row whose own \"Ad User\nData\" / \"Ad Personalization\" columns are filled in overrides this\nfor that row; empty cells fall back to it."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID (digits, e.g. \"1234567890\"). Empty\nuses the configured default account."
    }
  },
  "required": [
    "csv_path"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5535)

<a id="tool-get-custom-conversion-goals"></a>

### `get_custom_conversion_goals`

Read the custom conversion goals and the campaign goal configuration.

Returns every custom goal with its name, status and conversion actions,
plus — optionally for one campaign — the goal config the campaign uses
(`goal_config_level` CUSTOMER or CAMPAIGN and the assigned custom goal).

A custom conversion goal bundles conversion actions into a named set that a
campaign can be pointed at. Ahead of drafting, this shows which goals
exist, which actions they contain and what a campaign currently uses.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Numeric campaign ID. When omitted, the campaign config\nis skipped."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Ads account ID. Defaults to the configured account."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2987)

## Experiments and recommendations

<a id="tool-get-recommendations"></a>

### `get_recommendations`

Retrieve Google's auto-generated recommendations with estimated impact.

Returns each recommendation's type, associated campaign/ad group, current
(base) and projected (potential) metrics, and the estimated improvement.
Includes insights that flag budget-increase recommendations (their projected
gain comes from spending more) and highlight high-impact suggestions.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "recommendation_types": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional filter of Google Ads RecommendationType\nnames, e.g. [\"KEYWORD\", \"TARGET_CPA_OPT_IN\",\n\"MAXIMIZE_CONVERSIONS_OPT_IN\", \"RESPONSIVE_SEARCH_AD\"].\nEmpty = all types."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Optional numeric campaign ID to scope to a single campaign."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1448)

## Previews, validation, and local helpers

<a id="tool-approve-change"></a>

### `approve_change`

**Behavior:** App-only: ordinary model tool lists omit this registration. The approval card calls it with its plan code; it can test, apply, or discard a plan.

Run, apply or discard a previewed change from its approval card.

Called only by the AdLoop approval card when the user clicks a button;
AI apps keep this tool out of the model's tool list.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>, Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "plan_id": {
      "type": "string",
      "description": "The plan shown on the card."
    },
    "code": {
      "type": "string",
      "description": "The card's approval code for this plan."
    },
    "action": {
      "default": "test",
      "type": "string",
      "description": "\"test\" (dry run), \"apply\" (real change) or \"discard\"."
    },
    "acknowledged": {
      "default": false,
      "type": "boolean",
      "description": "The user ticked \"cannot be undone\"; required to apply a\nplan that needs double confirmation."
    }
  },
  "required": [
    "plan_id",
    "code"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3935)

<a id="tool-confirm-and-apply"></a>

### `confirm_and_apply`

**Behavior:** For Google Ads plans, dry runs send eligible operations with validate_only=True; dependent steps can be skipped. Workspace configuration can force dry runs or require a successful validation before apply.

Execute a previously previewed change.

IMPORTANT: Defaults to dry_run=True (validate only). Only an explicit
dry_run=false applies the change to the ad account (Google Ads or Reddit
Ads — the plan knows which platform it targets).

Forced dry runs: when real changes are switched off (live changes off
for the workspace in AdLoop Cloud, or safety.require_dry_run in a
self-hosted config), dry_run=false is IGNORED and the result is still
DRY_RUN_SUCCESS, with 'dry_run_forced_by' and 'remediation' fields.
'remediation' says how the user switches that setting; until it is
changed, repeated calls with dry_run=false change nothing.

Two-phase apply: if 'safety.two_phase_apply: true' is set (always on
for AdLoop Cloud tenants), dry_run=false is REFUSED with status
DRY_RUN_REQUIRED until this plan_id has completed one dry_run=true
pass. The sequence is: dry run, review of its result, then the real
apply.

Google Ads plans: the dry run sends the exact mutates to Google with
validate_only=True, so Google checks the change and executes nothing
(`checks` counts the validated calls). Steps that build on an object an
earlier step would create cannot be validated and are counted as skipped.

Reddit plans: Reddit has no validate-only mode, so the dry run re-reads
the target entity and re-checks the safety caps (returned as `checks`).

A DRY_RUN_FAILED result means the change does not go through as previewed.
The real apply fails the same way, unless Google rejected only part of the
request: then it carries out the rest and reports those operations again.

Returns a status with the plan_id and operation: DRY_RUN_SUCCESS,
DRY_RUN_FAILED, DRY_RUN_REQUIRED, APPLIED, PARTIAL_UPLOAD or
APPLY_IN_PROGRESS. APPLIED results carry the created or changed resource
names under 'result'. PARTIAL_UPLOAD belongs to the upload tools: the
batches it lists are already in the account, so the plan is retired.
'sent_total', 'accepted_total', 'rejected_total' and 'resume_from_line'
say how far the upload got and at which CSV line a new draft continues;
when a batch's fate is unknown, 'unknown_status', 'uncertain_lines' and
'row_errors' name the rows whose outcome has to be checked first.
APPLY_IN_PROGRESS means an earlier call claimed this plan first, so this
call executed nothing.

Approval cards: in AI apps that show AdLoop's approval card with the
preview, dry_run=false is REFUSED with status APPROVE_ON_CARD, because
only the user's click on the card applies the change. Dry runs still
work. The workspace owner can allow approval in chat as well.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>, Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "plan_id": {
      "type": "string",
      "description": "The plan_id returned by a prior draft_*, update_*, add_*,\npause/enable/remove or other preview tool call. An unknown or\nexpired plan_id returns an error."
    },
    "dry_run": {
      "default": true,
      "type": "boolean",
      "description": "True (default) validates without changing anything; false\napplies the change for real."
    }
  },
  "required": [
    "plan_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L3859)

<a id="tool-health-check"></a>

### `health_check`

Test AdLoop connectivity — checks OAuth token, GA4 API, Google Ads API,
and (when configured) the Reddit Ads API.

Returns the status of each service and actionable guidance when something
is broken, which makes it the diagnostic for failures in other tools.

Google Ads API: <https://developers.google.com/google-ads/api/docs/start>, Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L615)

## Other platform tools

These are the same server’s tools for other platforms. They are searchable here but do not determine its Google Ads grouping.

<a id="tool-draft-delete-key-event"></a>

### `draft_delete_key_event`

**Platform:** Google Analytics.

Draft removing a GA4 key event so the event no longer counts as a conversion, returning a PREVIEW.

The event itself keeps firing and stays in event reports; only its
key-event status goes, for future data (key events already recorded are
not reclassified). The draft resolves the event name against the
property's key events (keyEvents.list), so the preview names the exact
key event, its counting method and create time; an unknown name returns
the existing key events, and one GA4 marks as not deletable is refused.
Returns a preview with a plan_id and warnings; nothing changes until
confirm_and_apply applies it (GA4 Admin API keyEvents.delete).

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Admin API: <https://developers.google.com/analytics/devguides/config/admin/v1>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "event_name": {
      "type": "string",
      "description": "Event name of the key event to remove, exactly as listed\nby list_key_events (e.g. \"sign_up\"). Required."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GA4 property ID, with or without the \"properties/\"\nprefix. If empty, uses the default from config."
    }
  },
  "required": [
    "event_name"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5240)

<a id="tool-draft-key-event"></a>

### `draft_key_event`

**Platform:** Google Analytics.

Draft marking a GA4 event as a key event (conversion) — returns a PREVIEW.

The fix for "the event fires but isn't tracked as a conversion":
attribution_check / validate_tracking diagnose it, this closes the loop.
Applies to future data only. Returns a preview with a plan_id and warnings;
nothing changes until confirm_and_apply applies it.

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Admin API: <https://developers.google.com/analytics/devguides/config/admin/v1>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "event_name": {
      "type": "string",
      "description": "Name of the GA4 event to mark as a key event, exactly as it\nfires (e.g. \"sign_up\", \"purchase\"). Required."
    },
    "counting_method": {
      "default": "ONCE_PER_EVENT",
      "type": "string",
      "description": "ONCE_PER_EVENT (counts every occurrence, e.g.\npurchases) or ONCE_PER_SESSION (counts once per session, e.g.\nsign-ups). Defaults to ONCE_PER_EVENT."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GA4 property ID, with or without the \"properties/\"\nprefix. If empty, uses the default from config."
    }
  },
  "required": [
    "event_name"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5207)

<a id="tool-get-account-summaries"></a>

### `get_account_summaries`

**Platform:** Google Analytics.

List all GA4 accounts and properties accessible by the authenticated user.

Serves as the discovery step for which GA4 properties are available.
Returns account names, property names, and property IDs.

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Admin API: <https://developers.google.com/analytics/devguides/config/admin/v1>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L781)

<a id="tool-get-tracking-events"></a>

### `get_tracking_events`

**Platform:** Google Analytics.

List all GA4 events and their volume for the given date range.

Returns every distinct event name with its total event count, sorted by
count (highest first). Shows what tracking is configured and active.

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Admin API: <https://developers.google.com/analytics/devguides/config/admin/v1>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "date_range_start": {
      "default": "28daysAgo",
      "type": "string",
      "description": "Start date: \"today\", \"yesterday\", \"NdaysAgo\" (e.g.\n\"28daysAgo\"), or \"YYYY-MM-DD\"."
    },
    "date_range_end": {
      "default": "today",
      "type": "string",
      "description": "End date, same formats as date_range_start."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" (see\nget_account_summaries). If empty, uses the default from config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L909)

<a id="tool-list-ga4-dimensions-and-metrics"></a>

### `list_ga4_dimensions_and_metrics`

**Platform:** Google Analytics.

List the dimensions and metrics a GA4 property can report on, including custom ones.

Returns the exact API names valid in run_ga4_report for this property:
each with its UI name, category, whether it is a custom definition
(customEvent:..., customUser:...), and deprecated API names; metrics
also carry their type and, for calculated metrics, the expression.
Reads the GA4 Data API metadata (properties.getMetadata), which uses no
report quota.

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Admin API: <https://developers.google.com/analytics/devguides/config/admin/v1>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "search": {
      "default": "",
      "type": "string",
      "description": "Case-insensitive text matched against API name, UI name,\ncategory, description and deprecated API names (e.g. \"channel\",\n\"revenue\", or the legacy \"conversions\", which finds keyEvents).\nEmpty returns everything."
    },
    "kind": {
      "default": "all",
      "type": "string",
      "description": "\"all\" (default), \"dimensions\" or \"metrics\"."
    },
    "custom_only": {
      "default": false,
      "type": "boolean",
      "description": "True returns only the property's custom dimensions and\nmetrics."
    },
    "include_descriptions": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Include each field's description. Defaults to\ntrue when search is set and false otherwise (the full list is\nlong)."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" or the bare\nnumeric ID. If empty, uses the default from config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L961)

<a id="tool-list-key-events"></a>

### `list_key_events`

**Platform:** Google Analytics.

List the key events (conversions) configured on a GA4 property.

Returns each key event's event name, counting method (ONCE_PER_EVENT or
ONCE_PER_SESSION), create time, whether GA4 allows deleting it, whether
it is a custom event, and its resource name, sorted by event name, plus
the total. Reads the GA4 Admin API (keyEvents.list).

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Admin API: <https://developers.google.com/analytics/devguides/config/admin/v1>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" or the bare\nnumeric ID (see get_account_summaries). If empty, uses the\ndefault from config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L938)

<a id="tool-run-ga4-report"></a>

### `run_ga4_report`

**Platform:** Google Analytics.

Run a custom GA4 report with optional filters, ordering, paging and a comparison period.

Returns the property, the date range, the dimension and metric headers,
one row per dimension combination (values as strings), row_count and
total_row_count (plus next_offset while more rows remain). At least one
dimension or metric is required. With compare_start/compare_end the
comparison period is a second date range: every row then carries a
dateRange value of "current" or "comparison", and date_ranges maps both
labels to their dates. Invalid filters or ordering return "Validation
failed" with details, before anything is sent.

Queries the GA4 Data API. Dimensions and metrics:
<https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "dimensions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "GA4 dimension API names, e.g. date, pagePath,\nsessionSource, sessionMedium, country, deviceCategory, eventName.\nCustom ones (customEvent:...) and every valid name are listed by\nlist_ga4_dimensions_and_metrics."
    },
    "metrics": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "GA4 metric API names, e.g. sessions, totalUsers, newUsers,\nscreenPageViews, keyEvents, eventCount, bounceRate."
    },
    "date_range_start": {
      "default": "7daysAgo",
      "type": "string",
      "description": "Start date: \"today\", \"yesterday\", \"NdaysAgo\" (e.g.\n\"7daysAgo\", \"28daysAgo\", \"90daysAgo\"), or \"YYYY-MM-DD\"."
    },
    "date_range_end": {
      "default": "today",
      "type": "string",
      "description": "End date, same formats as date_range_start."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" (see\nget_account_summaries). If empty, uses the default from config."
    },
    "limit": {
      "default": 100,
      "type": "integer",
      "description": "Maximum number of rows returned (positive)."
    },
    "dimension_filter": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conditions on dimensions, all of which must hold\n(AND). Each is {\"field\": <dimension>, \"op\": <match>, \"value\":\n<string>}; op is EXACT (default), BEGINS_WITH, ENDS_WITH,\nCONTAINS, FULL_REGEXP, PARTIAL_REGEXP, or IN_LIST with \"values\":\n[<strings>]. Optional keys: \"case_sensitive\" (default false) and\n\"not\": true to exclude matches. Example: [{\"field\":\n\"sessionDefaultChannelGroup\", \"op\": \"EXACT\", \"value\": \"Paid\nSearch\"}]."
    },
    "metric_filter": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conditions on metrics, applied after aggregation, all\nof which must hold (AND). Each is {\"field\": <metric>, \"op\": <op>,\n\"value\": <number>}; op is EQUAL, LESS_THAN, LESS_THAN_OR_EQUAL,\nGREATER_THAN, GREATER_THAN_OR_EQUAL (or =, <, <=, >, >=), or\nBETWEEN with \"value\": [from, to]. Optional \"not\": true.\nExample: [{\"field\": \"sessions\", \"op\": \">\", \"value\": 100}]."
    },
    "order_by": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Sort order as [{\"field\": <name>, \"desc\": true|false}]; each\nfield must be one of the requested dimensions or metrics."
    },
    "offset": {
      "default": 0,
      "type": "integer",
      "description": "Zero-based row offset for paging; pass next_offset from the\nprevious result to get the following page."
    },
    "compare_start": {
      "default": "",
      "type": "string",
      "description": "Start of the comparison period (same formats as\ndate_range_start). Set together with compare_end."
    },
    "compare_end": {
      "default": "",
      "type": "string",
      "description": "End of the comparison period."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L794)

<a id="tool-run-realtime-report"></a>

### `run_realtime_report`

**Platform:** Google Analytics.

Run a GA4 realtime report showing current active users and events.

Useful for checking if tracking is firing correctly after code changes.
Returns the dimension and metric headers and one row per dimension
combination over the realtime window (the last 30 minutes).

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Admin API: <https://developers.google.com/analytics/devguides/config/admin/v1>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "dimensions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "GA4 realtime dimension API names, e.g. unifiedScreenName,\neventName, country, deviceCategory."
    },
    "metrics": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "GA4 realtime metric API names, e.g. activeUsers, eventCount.\nDefaults to [\"activeUsers\"]."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" (see\nget_account_summaries). If empty, uses the default from config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L878)

<a id="tool-list-gsc-sites"></a>

### `list_gsc_sites`

**Platform:** Search Console.

List all Google Search Console properties the authenticated user can access.

Serves as the discovery step for the site URLs that search analytics
reports (run_gsc_report) take. Returns the site URL and permission level
for each property.

Search Console API: <https://developers.google.com/webmaster-tools>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1010)

<a id="tool-run-gsc-report"></a>

### `run_gsc_report`

**Platform:** Search Console.

Run a Google Search Console search analytics report.

Returns clicks, impressions, CTR, and average position broken down by
the requested dimensions. Useful for diagnosing organic traffic drops,
finding keyword opportunities, and cross-referencing with GA4 and Ads data.
One request returns at most 25,000 rows; a full page carries
next_start_row for the following request. With data_state "all" the
response metadata names the first date whose data is still incomplete.

Queries the Search Console API:
<https://developers.google.com/webmaster-tools/v1/searchanalytics/query>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "site_url": {
      "default": "",
      "type": "string",
      "description": "The GSC property URL (e.g. \"https://example.com/\" or\n\"sc-domain:example.com\"), as listed by list_gsc_sites. Defaults to\nthe configured Search Console site (gsc.site_url)."
    },
    "dimensions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "One or more of \"query\", \"page\", \"country\", \"device\",\n\"date\", \"searchAppearance\" (search result feature, e.g. rich\nresults) or \"hour\" (hourly rows for roughly the last 10 days;\nswitches data_state to \"hourly_all\"). Defaults to [\"query\"]."
    },
    "date_range_start": {
      "default": "7daysAgo",
      "type": "string",
      "description": "Start date as ISO \"YYYY-MM-DD\" or a relative value\nlike \"7daysAgo\", \"30daysAgo\", \"today\"."
    },
    "date_range_end": {
      "default": "today",
      "type": "string",
      "description": "End date, same formats as date_range_start."
    },
    "limit": {
      "default": 100,
      "type": "integer",
      "description": "Maximum rows to return (default 100, max 25000 per request;\nhigher values are capped at 25000)."
    },
    "search_type": {
      "default": "web",
      "type": "string",
      "description": "\"web\" (default), \"image\", \"video\", \"news\", \"discover\",\nor \"googleNews\"."
    },
    "dimension_filter_groups": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional list of GSC DimensionFilterGroup\nobjects to filter by query, page, country, or device, e.g.\n[{\"filters\": [{\"dimension\": \"query\", \"operator\": \"contains\",\n\"expression\": \"analytics\"}]}]. searchAppearance is filterable too."
    },
    "data_state": {
      "default": "final",
      "type": "string",
      "description": "\"final\" (default) returns finalized data only; \"all\"\nadds fresh data from the last days that can still change;\n\"hourly_all\" is the state the hour dimension uses."
    },
    "aggregation_type": {
      "default": "auto",
      "type": "string",
      "description": "\"auto\" (default), \"byPage\" (aggregate by canonical\nURL) or \"byProperty\" (aggregate by property; not combinable with\ngrouping or filtering by page)."
    },
    "start_row": {
      "default": 0,
      "type": "integer",
      "description": "Zero-based offset of the first row, for paging past the\n25,000-row cap (pass the previous response's next_start_row)."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1024)

<a id="tool-audit-event-coverage"></a>

### `audit_event_coverage`

**Platform:** Google Tag Manager.

Three-way audit: codebase events ↔ GTM tags ↔ GA4 actual fires.

Fetches the LIVE GTM container, joins it against GA4 event counts for the
date range, and returns a per-event matrix with one of these statuses:
  ok                          — tag active and event firing
  ok_auto_collected           — GA4 Enhanced Measurement event, no tag needed
  no_tag_no_fire              — codebase event, no GTM tag, never fires
  tag_paused                  — GTM tag exists but is paused
  tag_active_but_not_firing   — tag is active but no GA4 hits
  gtm_only_firing             — GA4 event from a tag, not in codebase
  gtm_paused_but_firing       — only paused tag(s), not in codebase, yet
                                GA4 still fires (event comes from elsewhere)
  gtm_only_not_firing         — tag exists, not in codebase, no fires
  ga4_only                    — fires in GA4, no tag, no codebase ref
  ga4_fires_no_tag            — codebase event firing without a GTM tag
  auto_event_only             — Enhanced Measurement event with no codebase ref

The result also lists dynamic-event tags ({{Event}} variables) and Custom
HTML tags that the audit cannot interpret automatically.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "expected_events": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Distinct event names found in the codebase's\ngtag('event', ...) and dataLayer.push({event: ...}) calls."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (Tag Manager UI → Admin →\nContainer Settings, or list_gtm_accounts). Empty uses\ngtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (not the GTM-XXXXXXX public\nID; see list_gtm_containers). Empty uses gtm.container_id from the\nconfig."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\". Empty uses the\ndefault from config."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date \"YYYY-MM-DD\". Empty (or an empty\ndate_range_end) means the last 30 days."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date \"YYYY-MM-DD\". Empty (or an empty\ndate_range_start) means the last 30 days."
    }
  },
  "required": [
    "expected_events"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1832)

<a id="tool-draft-delete-gtm-entity"></a>

### `draft_delete_gtm_entity`

**Platform:** Google Tag Manager.

Invocation requires `gtm.write_enabled=true`; Custom HTML has an additional opt-in.

Draft deleting a Tag Manager tag or trigger — returns a PREVIEW.

The entity is removed from a workspace and stays on the site until the
workspace is published. A trigger that any tag still references is
refused up front, with the referencing tags named. Refused unless
gtm.write_enabled is set. Returns the entity that would be deleted, the
resolved workspace and a plan_id.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "\"tag\" or \"trigger\"."
    },
    "entity_id": {
      "type": "string",
      "description": "Numeric ID of the entity (see list_gtm_tags and\nlist_gtm_triggers)."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to edit (see list_gtm_workspaces). Empty uses\nthe Default Workspace, or the only workspace there is."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "required": [
    "entity_type",
    "entity_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2458)

<a id="tool-draft-gtm-tag"></a>

### `draft_gtm_tag`

**Platform:** Google Tag Manager.

Invocation requires `gtm.write_enabled=true`; Custom HTML has an additional opt-in.

Draft creating or updating a Tag Manager tag — returns a PREVIEW.

Without tag_id this creates a tag in a workspace; with tag_id it updates
the existing tag. The edit lands in the workspace and changes nothing on
the site until the workspace is published. Refused unless
gtm.write_enabled is set, and Custom HTML (html) is refused as well
unless gtm.allow_custom_html is set. Returns the resolved workspace, the
tag type, the fields that would change and a plan_id.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "name": {
      "default": "",
      "type": "string",
      "description": "Tag name, 1-200 characters. Required when creating a tag."
    },
    "tag_type": {
      "default": "",
      "type": "string",
      "description": "Tag type, required when creating a tag because GTM cannot\nchange a tag's type later: googtag, gaawe (GA4 event), awct (Ads\nconversion), awcc, awud, sp (Ads remarketing), gclidw, flc, fls,\nimg, html (Custom HTML) or cvt_<id> for a Community Gallery\ntemplate."
    },
    "parameters": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "GTM parameter dicts with at least \"type\" and \"key\", for\nexample gaawe [{\"type\": \"TEMPLATE\", \"key\": \"eventName\", \"value\":\n\"form_submit\"}] or awct [{\"type\": \"TEMPLATE\", \"key\":\n\"conversionId\", \"value\": \"123456789\"}, {\"type\": \"TEMPLATE\",\n\"key\": \"conversionLabel\", \"value\": \"AbC-dEf\"}]. On update they\nmerge by key: passed keys replace, other keys stay."
    },
    "firing_trigger_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Trigger IDs that fire the tag (see\nlist_gtm_triggers). The built-in All Pages trigger is\n\"2147479553\"."
    },
    "blocking_trigger_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Trigger IDs that must not fire the tag."
    },
    "paused": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "True stores the tag paused instead of deleting it. None keeps\nthe current state."
    },
    "notes": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Free-form note stored on the tag. None keeps the current note."
    },
    "tag_id": {
      "default": "",
      "type": "string",
      "description": "Existing tag ID to update (see list_gtm_tags). Empty creates\na new tag."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to edit (see list_gtm_workspaces). Empty uses\nthe Default Workspace, or the only workspace there is."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2307)

<a id="tool-draft-gtm-trigger"></a>

### `draft_gtm_trigger`

**Platform:** Google Tag Manager.

Invocation requires `gtm.write_enabled=true`; Custom HTML has an additional opt-in.

Draft creating or updating a Tag Manager trigger — returns a PREVIEW.

Without trigger_id this creates a trigger in a workspace; with trigger_id
it updates the existing one. The edit lands in the workspace and changes
nothing on the site until the workspace is published. Refused unless
gtm.write_enabled is set. Returns the resolved workspace, the trigger
fields that would change and a plan_id.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "name": {
      "default": "",
      "type": "string",
      "description": "Trigger name, 1-200 characters. Required when creating a\ntrigger."
    },
    "trigger_type": {
      "default": "",
      "type": "string",
      "description": "Trigger type, required when creating a trigger and\nrejected on an existing one, because GTM cannot change it later:\npageview, domReady, windowLoaded, click, linkClick,\nformSubmission, customEvent, elementVisibility, scrollDepth,\nyouTubeVideo, historyChange, timer, jsError or triggerGroup."
    },
    "custom_event_name": {
      "default": "",
      "type": "string",
      "description": "The dataLayer event name. Required for trigger type\ncustomEvent, rejected for every other type, and rejected on an\nexisting trigger, where the event name sits in its custom event\nfilter."
    },
    "filters": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "GTM conditions, each a dict with \"type\" (EQUALS, CONTAINS,\nMATCH_REGEX, ...) and \"parameter\" (arg0 = variable, arg1 =\nvalue), for example clicks on tel: links [{\"type\": \"CONTAINS\",\n\"parameter\": [{\"type\": \"TEMPLATE\", \"key\": \"arg0\", \"value\":\n\"{{Click URL}}\"}, {\"type\": \"TEMPLATE\", \"key\": \"arg1\", \"value\":\n\"tel:\"}]}]. On update the list replaces the existing one."
    },
    "custom_event_filters": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conditions on custom event parameters, same\nshape as filters. On update the list replaces the existing one."
    },
    "auto_event_filters": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conditions on automatic event parameters, same\nshape as filters. On update the list replaces the existing one."
    },
    "parameters": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "GTM parameter dicts with at least \"type\" and \"key\". On\nupdate they merge by key: passed keys replace, other keys stay."
    },
    "notes": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Free-form note stored on the trigger. None keeps the current\nnote."
    },
    "trigger_id": {
      "default": "",
      "type": "string",
      "description": "Existing trigger ID to update (see list_gtm_triggers).\nEmpty creates a new trigger."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to edit (see list_gtm_workspaces). Empty uses\nthe Default Workspace, or the only workspace there is."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2379)

<a id="tool-draft-publish-gtm-workspace"></a>

### `draft_publish_gtm_workspace`

**Platform:** Google Tag Manager.

Invocation requires `gtm.write_enabled=true`; Custom HTML has an additional opt-in.

Draft publishing a Tag Manager workspace LIVE — returns a PREVIEW.

Every pending change in the workspace goes live, including changes other
people made in the GTM UI; the preview lists them all. Apply refuses when
the workspace changed after the preview, has merge conflicts, or reports
compiler errors in a quick preview, and it refuses a Custom HTML tag
being added or changed while gtm.allow_custom_html is off. Refused unless
gtm.write_enabled is set. Returns the pending changes, the version that
is live now (for a one-step rollback), the version name that would be
created and a plan_id. That gate matches the tag type html; a Custom
JavaScript variable or a custom template tag (cvt_…), which can inject a
script, is not covered and needs review in the GTM UI.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "version_name": {
      "default": "",
      "type": "string",
      "description": "Name of the container version created by the publish.\nEmpty uses \"AdLoop publish <UTC timestamp>\"."
    },
    "version_notes": {
      "default": "",
      "type": "string",
      "description": "Notes stored on the created version. Empty leaves them\nout."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to publish (see list_gtm_workspaces). Empty\nuses the Default Workspace, or the only workspace there is."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2499)

<a id="tool-draft-rollback-gtm-version"></a>

### `draft_rollback_gtm_version`

**Platform:** Google Tag Manager.

Invocation requires `gtm.write_enabled=true`; Custom HTML has an additional opt-in.

Draft republishing an older Tag Manager version LIVE; returns a PREVIEW.

A rollback publishes an existing container version again. The preview
diffs the live version against the target, so it lists every tag,
trigger and variable that changes on the site, and it pins the live
version: apply refuses when another version went live after the
preview, or when the target was modified or archived. Workspaces are not
changed. Refused unless gtm.write_enabled is set, and refused when the
target adds or changes a Custom HTML tag while gtm.allow_custom_html is
off. Returns the diff, previous_live_version_id (the version that
restores today's state), the target version and a plan_id.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "version_id": {
      "type": "string",
      "description": "Container version ID to make live again (see\nlist_gtm_versions and get_gtm_version_diff)."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "required": [
    "version_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2546)

<a id="tool-get-gtm-tag"></a>

### `get_gtm_tag`

**Platform:** Google Tag Manager.

Get the full RAW configuration for a single GTM tag.

Includes every parameter, firing/blocking triggers (with their filter
conditions resolved to text), priority, pause status, sampling, and
monitoring metadata. Suited to inspecting a tag flagged by
audit_event_coverage. An unknown tag_id returns an error with the
available tag IDs. Reads the live container, or a workspace's
unpublished state when workspace_id is set.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "tag_id": {
      "type": "string",
      "description": "Numeric GTM tag ID, as listed by list_gtm_tags."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to read (see list_gtm_workspaces), which\nincludes drafted changes that are not published yet. Empty reads\nthe live (published) container version."
    }
  },
  "required": [
    "tag_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1975)

<a id="tool-get-gtm-trigger"></a>

### `get_gtm_trigger`

**Platform:** Google Tag Manager.

Get the full RAW configuration for a single GTM trigger.

Includes filters, auto-event filters, custom-event filters, validation
settings, and a list of every tag that uses this trigger. Helps
diagnose why a tag with a specific trigger ID does or doesn't fire. An
unknown trigger_id returns an error with the available trigger IDs.
Reads the live container, or a workspace's unpublished state when
workspace_id is set.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "trigger_id": {
      "type": "string",
      "description": "Numeric GTM trigger ID, as listed by list_gtm_triggers or\na tag's firing/blocking triggers."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to read (see list_gtm_workspaces), which\nincludes drafted changes that are not published yet. Empty reads\nthe live (published) container version."
    }
  },
  "required": [
    "trigger_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2052)

<a id="tool-get-gtm-version"></a>

### `get_gtm_version`

**Platform:** Google Tag Manager.

Get metadata + entity counts for a single GTM container version.

Returns name, description (the version notes), fingerprint, and lists of
tag/trigger/variable names at that point in time. The API returns no
timestamps or author for a version.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "container_version_id": {
      "type": "string",
      "description": "Numeric container version ID from\nlist_gtm_versions."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "required": [
    "container_version_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2226)

<a id="tool-get-gtm-version-diff"></a>

### `get_gtm_version_diff`

**Platform:** Google Tag Manager.

Compare two GTM container versions: what a publish changed.

Returns added, removed and changed tags, triggers and variables (with
names, types and the changed fields; parameters and trigger conditions
are diffed key by key), plus built-in variables enabled or disabled. By
default compares the live version with the version created before it.
The Tag Manager API does not mark which versions were published, so that
default "before" version may never have been live. Makes two or three
Tag Manager API calls.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "from_version_id": {
      "default": "",
      "type": "string",
      "description": "Older version ID (see list_gtm_versions). Empty uses\nthe newest non-archived version created before to_version_id."
    },
    "to_version_id": {
      "default": "",
      "type": "string",
      "description": "Newer version ID. Empty uses the live (published)\nversion."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2259)

<a id="tool-get-gtm-workspace-diff"></a>

### `get_gtm_workspace_diff`

**Platform:** Google Tag Manager.

Show drafted-but-not-published changes in a GTM workspace.

Returns the list of entities (tags, triggers, variables) added,
modified, or deleted relative to the live published version, plus
any merge conflicts. Common cause of "I edited a tag but nothing
happened" — the workspace was never published. is_clean=true means
no pending changes and no conflicts.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "workspace_id": {
      "type": "string",
      "description": "Numeric GTM workspace ID from list_gtm_workspaces."
    },
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "required": [
    "workspace_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2158)

<a id="tool-list-gtm-accounts"></a>

### `list_gtm_accounts`

**Platform:** Google Tag Manager.

List all GTM accounts the AdLoop service account / OAuth user can read.

The first-time discovery step: provides the account_id that
audit_event_coverage takes. Returns each account's ID and name. An empty
list means the service account hasn't been added to any GTM container
with at least Read permission.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1895)

<a id="tool-list-gtm-containers"></a>

### `list_gtm_containers`

**Platform:** Google Tag Manager.

List all containers under a GTM account.

Returns container_id (the numeric ID needed by audit_event_coverage),
public_id (the GTM-XXXXXXX string shown in the UI), name, and usage
context (web / iOS / Android / amp / server).

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID from list_gtm_accounts. Empty\nuses gtm.account_id from the config; the tool errors when neither\nis set."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1910)

<a id="tool-list-gtm-tags"></a>

### `list_gtm_tags`

**Platform:** Google Tag Manager.

List every tag in the LIVE GTM container, or in one workspace.

Each tag includes type, status, parsed parameters, the GA4 event name
(for GA4 event tags), and resolved firing/blocking trigger names.
Complements audit_event_coverage for inspecting specific tags. With
workspace_id the list shows that workspace's unpublished state, so a
just-drafted tag is visible; `source` says which state was read.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers),\nnot the GTM-XXXXXXX public ID. Empty uses gtm.container_id from\nthe config."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to read (see list_gtm_workspaces), which\nincludes drafted changes that are not published yet. Empty reads\nthe live (published) container version."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1938)

<a id="tool-list-gtm-triggers"></a>

### `list_gtm_triggers`

**Platform:** Google Tag Manager.

List every trigger in the LIVE GTM container, or in one workspace.

Each trigger has its filter conditions parsed to readable text
(e.g. "{{Page Path}} matches RegExp ^/service-promotions/"). Helps
diagnose why a tag fires or doesn't fire on specific pages. With
workspace_id the list shows that workspace's unpublished state.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to read (see list_gtm_workspaces), which\nincludes drafted changes that are not published yet. Empty reads\nthe live (published) container version."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2017)

<a id="tool-list-gtm-variables"></a>

### `list_gtm_variables`

**Platform:** Google Tag Manager.

List GTM variables — both custom and enabled built-in.

Without workspace_id both come from the live container version (the
Default Workspace supplies the built-ins only when the live version lists
none; built_in_source names where they came from). With workspace_id both
come from that workspace's unpublished state. Variables matter because
triggers reference them: if a trigger uses {{Form ID}} but Form ID isn't
enabled, the trigger never matches.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    },
    "workspace_id": {
      "default": "",
      "type": "string",
      "description": "Workspace to read (see list_gtm_workspaces), which\nincludes drafted changes that are not published yet. Empty reads\nthe live (published) container version."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2095)

<a id="tool-list-gtm-versions"></a>

### `list_gtm_versions`

**Platform:** Google Tag Manager.

List GTM container version headers (newest first).

Version headers include version_id, name, archived flag and entity
counts. The Tag Manager API returns no creation or publish time and no
author for a version, and does not mark which versions were published;
get_gtm_version returns a version's notes and get_gtm_version_diff what
changed between two versions.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    },
    "page_size": {
      "default": 50,
      "type": "integer",
      "description": "Maximum number of version headers returned (newest first)."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2192)

<a id="tool-list-gtm-workspaces"></a>

### `list_gtm_workspaces`

**Platform:** Google Tag Manager.

List workspaces (drafts) under a GTM container.

Returns each workspace's ID, name and description; the IDs are what
`get_gtm_workspace_diff` takes. Most containers have a single Default
Workspace; multiple workspaces appear when the team uses parallel drafts.

Tag Manager API: <https://developers.google.com/tag-platform/tag-manager/api/v2>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "gtm_account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM account ID (see list_gtm_accounts). Empty\nuses gtm.account_id from the config."
    },
    "gtm_container_id": {
      "default": "",
      "type": "string",
      "description": "Numeric GTM container ID (see list_gtm_containers).\nEmpty uses gtm.container_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L2132)

<a id="tool-get-merchant-feed-health"></a>

### `get_merchant_feed_health`

**Platform:** Merchant Center.

Merchant Center feed health — disapproved products + account issues.

Disapproved feed items silently starve Shopping and Performance Max
campaigns; this reports approved/pending/disapproved counts per
reporting context (Shopping ads, free listings, ...), the top product
issues by affected products (with documentation links), and
account-level issues — CRITICAL ones stop offers serving entirely.
Product-status data lags reality by ~30 minutes.

Merchant API: <https://developers.google.com/merchant/api/overview>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "account_id": {
      "default": "",
      "type": "string",
      "description": "Numeric Merchant Center ID from list_merchant_accounts.\nDefaults to merchant.account_id in the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1144)

<a id="tool-list-merchant-accounts"></a>

### `list_merchant_accounts`

**Platform:** Merchant Center.

List Google Merchant Center accounts the connected user can access.

Returns each account's numeric ID, name and whether it is a test
account. Provides the account_id used by get_merchant_feed_health;
not needed when merchant.account_id is set in the config.

Merchant API: <https://developers.google.com/merchant/api/overview>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1130)

<a id="tool-draft-reddit-ad"></a>

### `draft_reddit_ad`

**Platform:** Reddit Ads.

Draft a Reddit ad: creates a post on the profile, then the ad (PAUSED) — PREVIEW.

click_url and the media URLs are checked before drafting, so ads do not
point at unverified pages and Reddit gets real image and video files. Comments are public on Reddit
ads. With post_id an EXISTING post is promoted instead, keeping its
upvotes and comments: no post is created and the copy arguments are
ignored. Returns a preview with a plan_id; nothing changes until
confirm_and_apply applies it. Once enabled, the ad goes through Reddit
policy review (PENDING_APPROVAL).

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "type": "string",
      "description": "Reddit ad group id (from get_reddit_ad_groups)."
    },
    "profile_id": {
      "default": "",
      "type": "string",
      "description": "Reddit profile that authors the post, from\nlist_reddit_funding_instruments (profiles). Required for a new\npost; with post_id it defaults to the post's."
    },
    "headline": {
      "default": "",
      "type": "string",
      "description": "Post headline, required for a new post, at most 300\ncharacters."
    },
    "click_url": {
      "default": "",
      "type": "string",
      "description": "Landing page (http:// or https://). Required for a new\npost. TEXT posts open themselves, so the full click_url must also\nappear in body. With post_id, TEXT posts take no click_url and\nmedia posts default it to the post's destination."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "ad_name": {
      "default": "",
      "type": "string",
      "description": "Ad name; empty uses the headline. Truncated to 200\ncharacters."
    },
    "post_type": {
      "default": "TEXT",
      "type": "string",
      "description": "TEXT (headline + optional body; default), IMAGE\n(public image_url), VIDEO (public video_url + thumbnail_url) or\nCAROUSEL (2 to 6 carousel_cards)."
    },
    "body": {
      "default": "",
      "type": "string",
      "description": "Post body text, up to 40,000 characters. Optional for media\nposts."
    },
    "image_url": {
      "default": "",
      "type": "string",
      "description": "Publicly reachable image URL, required for IMAGE posts."
    },
    "call_to_action": {
      "default": "",
      "type": "string",
      "description": "One of Reddit's fixed labels for media posts: Apply\nNow, Book Now, Buy Tickets, Contact Us, Donate Now, Download, Get\na Quote, Get Directions, Get Showtimes, Install, Learn More,\nListen Now, Order Now, Play Now, Pre-order Now, Read More, Remind\nMe, See Menu, Shop Now, Sign Up, Subscribe, View More, Visit\nStore, Watch Now. On a carousel it is the default for every card."
    },
    "display_url": {
      "default": "",
      "type": "string",
      "description": "Optional display URL shown with media posts; must be on\nthe click_url's domain."
    },
    "allow_comments": {
      "default": true,
      "type": "boolean",
      "description": "Whether Redditors can comment publicly on the ad\n(default true); false disables them."
    },
    "post_id": {
      "default": "",
      "type": "string",
      "description": "Existing post to promote (t3_...); headline, body, the\nmedia arguments, call_to_action and display_url are then ignored.\nEmpty creates a new post."
    },
    "video_url": {
      "default": "",
      "type": "string",
      "description": "Direct link to the video file (MP4 or MOV, up to 1 GB),\nrequired for VIDEO posts. Reddit downloads it when the post is\ncreated; a page that embeds the video does not work."
    },
    "thumbnail_url": {
      "default": "",
      "type": "string",
      "description": "Publicly reachable image Reddit shows before the video\nplays, required for VIDEO posts."
    },
    "carousel_cards": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For CAROUSEL posts, 2 to 6 cards, each\n{\"image_url\": \"...\", \"caption\": \"...\", \"click_url\": \"...\",\n\"call_to_action\": \"...\"}. Only image_url is required; caption is\nat most 180 characters, click_url and call_to_action default to\nthe ad's."
    }
  },
  "required": [
    "ad_group_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5104)

<a id="tool-draft-reddit-ad-group"></a>

### `draft_reddit_ad_group`

**Platform:** Reddit Ads.

Draft a new Reddit ad group (created PAUSED) — returns a PREVIEW.

Required: campaign_id, ad_group_name, conversion_pixel_id and at least
one targeting list (geolocations, communities, interests or keywords —
ids/names from search_reddit_targeting). For non-CBO campaigns also
daily_budget (or lifetime_budget + end_time), bid_strategy and bid_type.
Budgets are checked against max_daily_budget; keywords and geolocations
are pre-validated with Reddit. Returns a preview with a plan_id, the
payload and warnings; nothing changes until confirm_and_apply applies it.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Reddit campaign id (from get_reddit_campaigns)."
    },
    "ad_group_name": {
      "type": "string",
      "description": "Name of the new ad group."
    },
    "conversion_pixel_id": {
      "type": "string",
      "description": "Pixel id (Reddit rule; from get_reddit_pixels)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in account currency (positive). Required\nfor non-CBO campaigns unless lifetime_budget is given; not allowed\nin CBO campaigns. Mutually exclusive with lifetime_budget."
    },
    "lifetime_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in account currency (positive);\nrequires end_time and is compared to max_daily_budget by its\nper-day share."
    },
    "bid_strategy": {
      "default": "",
      "type": "string",
      "description": "BIDLESS, MANUAL_BIDDING, MAXIMIZE_VOLUME or TARGET_CPX.\nRequired for non-CBO campaigns; in CBO campaigns it must match the\ncampaign's."
    },
    "bid_type": {
      "default": "",
      "type": "string",
      "description": "CPC, CPM, CPV, CPV6 or CPV15. Required for non-CBO\ncampaigns."
    },
    "bid_value": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Bid in account currency; MANUAL_BIDDING and TARGET_CPX\n(target cost per result) need it."
    },
    "optimization_goal": {
      "default": "",
      "type": "string",
      "description": "The pixel event to optimize for (PURCHASE,\nSIGN_UP, LEAD, PAGE_VISIT, ...). Empty in a CBO campaign inherits\nthe campaign's."
    },
    "geolocations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geolocation ids to target (e.g. \"DE\" or \"DE:2874225\")."
    },
    "excluded_geolocations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geolocation ids to exclude."
    },
    "communities": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Community (subreddit) names to target."
    },
    "excluded_communities": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Community names to exclude."
    },
    "interests": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Interest ids to target."
    },
    "keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Keywords to target; Reddit refuses keywords that are not\nbrand-safe."
    },
    "excluded_keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Keywords to exclude."
    },
    "languages": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Language codes (ISO 639-1, upper-cased automatically,\ne.g. \"DE\"). Empty means every language."
    },
    "gender": {
      "default": "",
      "type": "string",
      "description": "FEMALE or MALE; empty means all genders."
    },
    "platforms": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ALL, DESKTOP, DESKTOP_LEGACY, MOBILE_NATIVE, MOBILE_WEB,\nMOBILE_WEB_3X or SHREDTOP."
    },
    "expand_targeting": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Whether Reddit may expand delivery beyond the\ntargeting; omitted uses Reddit's default."
    },
    "start_time": {
      "default": "",
      "type": "string",
      "description": "Start, ISO 8601 (e.g. 2026-10-01T00:00:00Z); a bare\nYYYY-MM-DD means 00:00 UTC that day. Empty means now."
    },
    "end_time": {
      "default": "",
      "type": "string",
      "description": "End, same formats as start_time."
    },
    "schedule": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Weekly delivery windows (\"time of day\" in Ads Manager), a\nlist of blocks like {\"days\": \"MON-FRI\", \"start_hour\": 13,\n\"end_hour\": 23} (day names, hours 0-23, end_hour inclusive) or the\nnative {\"start_day\": \"FRI\", \"start_hour\": 22, \"end_day\": \"SAT\",\n\"end_hour\": 3}. Omitted means delivery at any time. Hours apply in\neach viewer's local time, not the account time zone. Not allowed\nin CBO campaigns, whose schedule overrides every ad group."
    },
    "locations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Placements, FEED and/or COMMENTS_PAGE (conversation\npages); cannot be an empty list."
    },
    "excluded_interests": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Interest ids to exclude (Reddit marks this field\ndeprecated)."
    },
    "devices": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Device targets, objects like {\"type\": \"MOBILE\", \"os\":\n\"IOS\", \"min_version\": \"16\"} (type DESKTOP or MOBILE; optional os\nANDROID or IOS, major OS versions with iOS at least 14, and\nlabel_map {make: [models]} with makes/models from\nsearch_reddit_targeting kind \"devices\"). Omitted means every\ndevice; APP_INSTALLS campaigns take exactly one."
    },
    "carriers": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Mobile carrier ids (from search_reddit_targeting kind\n\"carriers\", e.g. \"O2_DEUTSCHLAND\"), checked against Reddit's\ncarrier list. Omitted means every carrier."
    },
    "view_modes": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Feed layouts: ALL, CARD, CLASSIC, COMPACT or IMMERSIVE.\nOmitted uses Reddit's default."
    },
    "custom_audience_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom audiences to target (from\nget_reddit_audiences), e.g. website visitors for retargeting."
    },
    "excluded_custom_audience_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom audiences to exclude, e.g.\npeople who already bought."
    }
  },
  "required": [
    "campaign_id",
    "ad_group_name",
    "conversion_pixel_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4954)

<a id="tool-draft-reddit-campaign"></a>

### `draft_reddit_campaign`

**Platform:** Reddit Ads.

Draft a new Reddit campaign (created PAUSED) — returns a PREVIEW.

By default the budget lives on the ad groups; campaign_budget_optimization
holds it on the campaign. Budgets are checked against max_daily_budget.
Ad groups are added with draft_reddit_ad_group. Returns a preview with a
plan_id, the payload and warnings; nothing changes until
confirm_and_apply applies it.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_name": {
      "type": "string",
      "description": "Name of the new campaign."
    },
    "objective": {
      "type": "string",
      "description": "CLICKS, CONVERSIONS, IMPRESSIONS, LEAD_GENERATION,\nAPP_INSTALLS, CATALOG_SALES or VIDEO_VIEWABLE_IMPRESSIONS. Other\nvalues only produce a warning, since Reddit is rolling out new\nobjective enums."
    },
    "funding_instrument_id": {
      "type": "string",
      "description": "Servable funding instrument id from\nlist_reddit_funding_instruments."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "campaign_budget_optimization": {
      "default": false,
      "type": "boolean",
      "description": "true holds the budget on the campaign\n(then daily_budget or lifetime_budget, bid_strategy, bid_type and\nconversion_pixel_id are required). false (default) leaves budget\nand bids to the ad groups, and none of the budget or bid\nparameters may be passed."
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in account currency (positive; CBO only).\nMutually exclusive with lifetime_budget."
    },
    "lifetime_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in account currency (positive; CBO\nonly); requires end_time and is compared to max_daily_budget by\nits per-day share."
    },
    "bid_strategy": {
      "default": "",
      "type": "string",
      "description": "BIDLESS, MAXIMIZE_VOLUME or TARGET_CPX (CBO only)."
    },
    "bid_type": {
      "default": "",
      "type": "string",
      "description": "CPC, CPM, CPV, CPV6 or CPV15 (CBO only)."
    },
    "bid_value": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Bid in account currency (CBO only)."
    },
    "optimization_goal": {
      "default": "",
      "type": "string",
      "description": "Pixel event to optimize for (PURCHASE, SIGN_UP,\nLEAD, PAGE_VISIT, ...); used with CBO only."
    },
    "conversion_pixel_id": {
      "default": "",
      "type": "string",
      "description": "Pixel id from get_reddit_pixels; required with\nCBO, optional otherwise."
    },
    "spend_cap": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign spend cap in account currency; 0 or empty means\nnone."
    },
    "start_time": {
      "default": "",
      "type": "string",
      "description": "Start, ISO 8601 (e.g. 2026-10-01T00:00:00Z); a bare\nYYYY-MM-DD means 00:00 UTC that day."
    },
    "end_time": {
      "default": "",
      "type": "string",
      "description": "End, same formats as start_time."
    },
    "schedule": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Weekly delivery windows (\"time of day\" in Ads Manager; CBO\nonly), a list of blocks like {\"days\": \"MON-FRI\", \"start_hour\": 13,\n\"end_hour\": 23} (day names, hours 0-23, end_hour inclusive) or the\nnative {\"start_day\": \"FRI\", \"start_hour\": 22, \"end_day\": \"SAT\",\n\"end_hour\": 3}. [] clears it (deliver at any time). Hours apply in\neach viewer's local time, not the account time zone. A campaign\nschedule replaces every ad group's."
    }
  },
  "required": [
    "campaign_name",
    "objective",
    "funding_instrument_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4863)

<a id="tool-draft-reddit-custom-audience"></a>

### `draft_reddit_custom_audience`

**Platform:** Reddit Ads.

Draft a Reddit retargeting audience (website visitors or engaged people) — PREVIEW.

Builds the audience from data Reddit already has: people the pixel saw
on the website, or people who saw or engaged with the account's
campaigns. No personal data is uploaded. Nothing changes until
confirm_and_apply applies the plan_id; Reddit then fills the audience
(status PENDING, up to a day), and an ad group uses it through
update_reddit_ad_group custom_audience_ids (target) or
excluded_custom_audience_ids (exclude).

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "name": {
      "type": "string",
      "description": "Audience name, 3 to 500 characters."
    },
    "audience_type": {
      "type": "string",
      "description": "PIXEL_RETARGETING (website visitors, from the pixel)\nor ENGAGEMENT_RETARGETING (people who saw or engaged with\ncampaigns)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "pixel_id": {
      "default": "",
      "type": "string",
      "description": "Pixel to build a website audience from (get_reddit_pixels)."
    },
    "events": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Website audiences: the pixel events that qualify, any of\nPAGE_VISIT (default), VIEW_CONTENT, SEARCH, ADD_TO_CART,\nADD_TO_WISHLIST, PURCHASE, LEAD, SIGN_UP, CUSTOM."
    },
    "custom_events": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Website audiences: custom pixel event names to\ninclude (adds CUSTOM to events), at most 50."
    },
    "campaign_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Engagement audiences: the campaigns whose audience to\nreuse (get_reddit_campaigns)."
    },
    "engagements": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Engagement audiences: what people did, any of CLICKS\n(default), IMPRESSIONS, UPVOTES, COMMENT_SUBMISSIONS,\nVIDEO_STARTED, VIDEO_WATCHED_50_PERCENT,\nVIDEO_WATCHED_100_PERCENT."
    },
    "lookback_window_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "How far back an action counts: 1 to 90 days for\nwebsite audiences (default 30), 1 to 180 for engagement audiences\n(default 90)."
    }
  },
  "required": [
    "name",
    "audience_type"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4801)

<a id="tool-enable-reddit-entity"></a>

### `enable_reddit_entity`

**Platform:** Reddit Ads.

Draft enabling (configured_status=ACTIVE) a Reddit campaign, ad group or ad — PREVIEW.

Enabling a new ad sends it to Reddit policy review (PENDING_APPROVAL).
Returns a preview with a plan_id, the current and target status and
warnings (e.g. an effective_status of REJECTED or PENDING_BILLING_INFO
that keeps it from serving); nothing changes until confirm_and_apply
applies the plan_id.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "\"campaign\", \"ad_group\" or \"ad\"."
    },
    "entity_id": {
      "type": "string",
      "description": "Reddit id of the entity, from the read tools\n(get_reddit_campaigns, get_reddit_ad_groups, get_reddit_ads)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    }
  },
  "required": [
    "entity_type",
    "entity_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4494)

<a id="tool-estimate-reddit-ad-group"></a>

### `estimate_reddit_ad_group`

**Platform:** Reddit Ads.

Audience size, delivery estimate and Reddit's suggested bid for a planned ad group — read-only.

Reddit's counterpart of estimate_budget: takes the same targeting and
budget as draft_reddit_ad_group, ahead of drafting. Returns the reachable
and targetable audience (fixed 30-day basis), estimated
impressions/clicks/reach for the schedule, the minimum/suggested bid
range for bid_type in account currency, and insights (audience under
10,000 people, bid_value below the suggested minimum). Nothing is
created. At least one of geolocations, communities, interests or keywords
is required.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in account currency (positive). One of\ndaily_budget or lifetime_budget is required; daily_budget wins\nwhen both are given."
    },
    "lifetime_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in account currency (positive),\nused when daily_budget is not given."
    },
    "objective": {
      "default": "CLICKS",
      "type": "string",
      "description": "Campaign objective the estimate assumes, e.g. CLICKS\n(default), CONVERSIONS, IMPRESSIONS, LEAD_GENERATION,\nAPP_INSTALLS, CATALOG_SALES or VIDEO_VIEWABLE_IMPRESSIONS."
    },
    "bid_type": {
      "default": "CPC",
      "type": "string",
      "description": "CPC (default), CPM, CPV, CPV6 or CPV15; the bid suggestion\nis for this bid type."
    },
    "bid_strategy": {
      "default": "",
      "type": "string",
      "description": "BIDLESS, MANUAL_BIDDING, MAXIMIZE_VOLUME or TARGET_CPX.\nEmpty means BIDLESS."
    },
    "bid_value": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Planned bid in account currency; compared with Reddit's\nsuggested minimum."
    },
    "optimization_goal": {
      "default": "",
      "type": "string",
      "description": "Pixel event to optimize for (PURCHASE, SIGN_UP,\nLEAD, PAGE_VISIT, ...). Empty means none."
    },
    "start_time": {
      "default": "",
      "type": "string",
      "description": "Schedule start, ISO 8601 (e.g. 2026-10-01T00:00:00Z).\nEmpty means tomorrow 00:00 UTC."
    },
    "end_time": {
      "default": "",
      "type": "string",
      "description": "Schedule end, ISO 8601. Empty means 30 days after the\ndefault start."
    },
    "geolocations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geolocation ids to target (e.g. \"DE\" or \"DE:2874225\",\nfrom search_reddit_targeting kind \"geolocations\")."
    },
    "excluded_geolocations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geolocation ids to exclude."
    },
    "communities": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Community (subreddit) names to target."
    },
    "excluded_communities": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Community names to exclude."
    },
    "interests": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Interest ids to target (from search_reddit_targeting kind\n\"interests\")."
    },
    "keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Keywords to target."
    },
    "languages": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Language codes (ISO 639-1, upper-cased automatically,\ne.g. \"DE\"). Empty means all languages."
    },
    "gender": {
      "default": "",
      "type": "string",
      "description": "FEMALE or MALE; empty means all genders."
    },
    "platforms": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Platforms to target, e.g. ALL, DESKTOP, MOBILE_NATIVE,\nMOBILE_WEB. Empty means no platform restriction."
    },
    "devices": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Device targets, objects like {\"type\": \"MOBILE\", \"os\":\n\"IOS\", \"min_version\": \"16\"} (type DESKTOP or MOBILE; optional os\nANDROID or IOS, major OS versions, and label_map {make: [models]}\nwith makes/models from search_reddit_targeting kind \"devices\").\nEmpty means every device."
    },
    "carriers": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Mobile carrier ids (from search_reddit_targeting kind\n\"carriers\", e.g. \"O2_DEUTSCHLAND\"). Empty means every carrier."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4355)

<a id="tool-get-reddit-account-history"></a>

### `get_reddit_account_history`

**Platform:** Reddit Ads.

Who changed what in the Reddit ad account: field, before/after, member, time.

Returns the changes, most recent first, with changed_at, by, entity type,
id and name, field, and before/after values. The first thing to check
when performance moves. Child entities are included when filtering by
entity. Changes made through AdLoop show under the connected Reddit user,
like changes made in Ads Manager. Money fields are in account currency.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "First day, YYYY-MM-DD (account-local day). Empty\nmeans 29 days before date_range_end (default window is the last\n30 days)."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "Last day (inclusive), YYYY-MM-DD (account-local day).\nEmpty means today."
    },
    "entity_type": {
      "default": "",
      "type": "string",
      "description": "Optional filter to one entity type: \"campaign\",\n\"ad_group\" or \"ad\". Requires entity_ids."
    },
    "entity_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Ids of the entities of entity_type to filter to; required\nwhen entity_type is set."
    },
    "limit": {
      "default": 100,
      "type": "integer",
      "description": "Maximum number of changes returned, clamped to 1-500."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4310)

<a id="tool-get-reddit-ad-groups"></a>

### `get_reddit_ad_groups`

**Platform:** Reddit Ads.

List Reddit ad groups (budget, bid, pixel, weekly schedule, targeting summary), optionally per campaign.

Returns the account currency, the ad groups, and insights. Reddit
requires conversion_pixel_id on every ad group; insights flag ad groups
without one and name ad groups that run on a weekly schedule.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Reddit campaign id (from get_reddit_campaigns) to limit\nthe list to; empty lists every ad group of the account."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4068)

<a id="tool-get-reddit-ads"></a>

### `get_reddit_ads`

**Platform:** Reddit Ads.

List Reddit ads with status, rejection_reason, post and click URL.

Returns the ads and insights: insights flag REJECTED ads (policy review)
and ads still PENDING_APPROVAL.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "ad_group_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad group id (from get_reddit_ad_groups) to limit\nthe list to; empty means no ad group filter."
    },
    "campaign_id": {
      "default": "",
      "type": "string",
      "description": "Reddit campaign id (from get_reddit_campaigns) to limit\nthe list to; empty means no campaign filter."
    },
    "include_copy": {
      "default": false,
      "type": "boolean",
      "description": "When true, adds each ad's post: type (TEXT, IMAGE,\nVIDEO, CAROUSEL), headline, body, destination and media, one\nrequest per distinct post (at most 50 posts per call), so creative\ncan be reviewed without opening Reddit."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4092)

<a id="tool-get-reddit-audiences"></a>

### `get_reddit_audiences`

**Platform:** Reddit Ads.

Reddit custom and saved audiences of the account, and which ad groups use them.

Returns each custom audience's audience_id, name, type (PIXEL_RETARGETING,
ENGAGEMENT_RETARGETING, CUSTOMER_LIST, LOOKALIKE, ...), status, estimated
size_range, its source (pixel events or campaigns, lookback days) and the
ad groups that target or exclude it; saved audiences with their
targeting; and insights that flag audiences Reddit cannot use yet or that
are too small to deliver. The audience_id goes into custom_audience_ids or
excluded_custom_audience_ids on an ad group.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4245)

<a id="tool-get-reddit-campaigns"></a>

### `get_reddit_campaigns`

**Platform:** Reddit Ads.

List Reddit campaigns with status, objective, budget mode and bids.

Returns the account currency, the campaigns, and insights for campaigns
blocked by account state. Each campaign carries configured_status (what
was set) and effective_status (what Reddit computes: PENDING_APPROVAL,
REJECTED, PENDING_BILLING_INFO, ...). Money is in account currency.
Budgets live on ad groups unless is_campaign_budget_optimization is true.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "include_archived": {
      "default": false,
      "type": "boolean",
      "description": "Include ARCHIVED and DELETED campaigns, which are\nleft out by default."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4042)

<a id="tool-get-reddit-performance"></a>

### `get_reddit_performance`

**Platform:** Reddit Ads.

Reddit Ads performance: spend, impressions, clicks, CTR, CPC, conversions, CPA, ROAS.

Returns rows per entity for the chosen level with names joined, plus
totals and insights[] (zero-conversion spenders, rejected ads, empty
windows). 'conversions' is the account's key conversion event. Money is
in account currency. Data lags up to 6 hours.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "level": {
      "default": "campaign",
      "type": "string",
      "description": "Row granularity: \"account\", \"campaign\" (default), \"ad_group\"\nor \"ad\"."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "First day, YYYY-MM-DD, in the account's time zone.\nEmpty means 29 days before date_range_end (a 30-day window)."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "Last day (inclusive), YYYY-MM-DD, in the account's\ntime zone. Empty means today."
    },
    "breakdown": {
      "default": "",
      "type": "string",
      "description": "Optional extra dimension: \"date\", \"hour\", \"country\",\n\"region\", \"community\", \"keyword\", \"interest\", \"placement\",\n\"gender\" or \"os_type\". Empty means none."
    },
    "compact": {
      "default": false,
      "type": "boolean",
      "description": "When true, returns totals + top-10 rows by spend + offender\nlists instead of every row."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4128)

<a id="tool-get-reddit-pixels"></a>

### `get_reddit_pixels`

**Platform:** Reddit Ads.

Reddit pixels of the account and when each event (purchase, sign_up, lead, ...) last fired.

Returns each pixel's pixel_id, name, last_fired_at per standard event,
custom events and a never_fired flag, plus insights. Relevant before
conversion-optimized campaigns: insights flag pixels that never fired and
ad groups optimizing for an event their pixel has never sent. Every new
ad group needs a conversion_pixel_id from here.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4225)

<a id="tool-list-reddit-accounts"></a>

### `list_reddit_accounts`

**Platform:** Reddit Ads.

List Reddit businesses and ad accounts the connected Reddit user can access.

Returns the Reddit username, the businesses, and per ad account the
ad_account_id values (plus currency, time zone and approval state) that
every other Reddit tool takes. Requires the Reddit Ads connection
(adloop init → Reddit step, or Settings → Reddit Ads in Cloud).

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4005)

<a id="tool-list-reddit-funding-instruments"></a>

### `list_reddit_funding_instruments`

**Platform:** Reddit Ads.

Funding instruments (billing) and posting profiles of a Reddit ad account.

Returns funding_instruments (funding_instrument_id, currency, is_servable,
reasons_not_servable, credit limit and billable amount in account
currency) and profiles (profile_id, username). draft_reddit_campaign needs
a servable funding_instrument_id; draft_reddit_ad needs the profile_id
that authors the post. Both come from here.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4022)

<a id="tool-pause-reddit-entity"></a>

### `pause_reddit_entity`

**Platform:** Reddit Ads.

Draft pausing a Reddit campaign, ad group or ad — returns a PREVIEW.

Returns a preview with a plan_id, the current and target status (PAUSED)
and warnings (e.g. already paused); nothing changes until
confirm_and_apply applies the plan_id.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "\"campaign\", \"ad_group\" or \"ad\"."
    },
    "entity_id": {
      "type": "string",
      "description": "Reddit id of the entity, from the read tools\n(get_reddit_campaigns, get_reddit_ad_groups, get_reddit_ads)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    }
  },
  "required": [
    "entity_type",
    "entity_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4466)

<a id="tool-remove-reddit-entity"></a>

### `remove_reddit_entity`

**Platform:** Reddit Ads.

Draft ARCHIVING a Reddit campaign, ad group or ad — irreversible, PREVIEW.

Reddit has no hard delete for entities that ran; ARCHIVED is permanent.
pause_reddit_entity is the reversible alternative when the entity does
not need to be gone. Returns a preview with a plan_id that requires
double confirmation; confirm_and_apply executes it.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "\"campaign\", \"ad_group\" or \"ad\"."
    },
    "entity_id": {
      "type": "string",
      "description": "Reddit id of the entity, from the read tools\n(get_reddit_campaigns, get_reddit_ad_groups, get_reddit_ads)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    }
  },
  "required": [
    "entity_type",
    "entity_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4524)

<a id="tool-run-reddit-report"></a>

### `run_reddit_report`

**Platform:** Reddit Ads.

Run a custom Reddit Ads report for metrics get_reddit_performance omits.

Returns the requested fields per breakdown row, the date range and the
account currency. Microcurrency and cent fields are converted to
currency amounts.

Queries the Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Reddit report field names (required), e.g. [\"SPEND\",\n\"CLICKS\", \"REACH\", \"VIDEO_STARTED\",\n\"CONVERSION_PURCHASE_TOTAL_VALUE\", \"KEY_CONVERSION_TOTAL_COUNT\"]."
    },
    "breakdowns": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Up to 3 of DATE, HOUR, CAMPAIGN_ID, AD_GROUP_ID, AD_ID,\nCOUNTRY, REGION, COMMUNITY, KEYWORD, INTEREST, PLACEMENT, GENDER,\nOS_TYPE (4 when COUNTRY and REGION are both included; HOUR and\nDATE cannot be combined)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "First day, YYYY-MM-DD (account-local day). Empty\nmeans 29 days before date_range_end (a 30-day window)."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "Last day (inclusive), YYYY-MM-DD (account-local day).\nEmpty means today."
    },
    "filter": {
      "default": "",
      "type": "string",
      "description": "Reddit filter expression (e.g. \"campaign_id==abc123\"). Empty\nmeans no filter."
    },
    "time_zone_id": {
      "default": "",
      "type": "string",
      "description": "IANA time zone for the day boundaries and DATE/HOUR\nrows, e.g. \"Europe/Berlin\". Empty uses the ad account's time zone."
    }
  },
  "required": [
    "fields"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4173)

<a id="tool-search-reddit-targeting"></a>

### `search_reddit_targeting`

**Platform:** Reddit Ads.

Look up targeting options for draft_reddit_ad_group.

Returns ids/names to pass into the targeting lists, with the kind, the
query and the total number of matches. Communities target by name,
interests by id, geolocations by id (e.g. "DE" or "DE:2874225"),
languages by code (e.g. "DE"), carriers by id (e.g. "O2_DEUTSCHLAND").
Devices come back as make/model pairs for the label_map of a device
target. Keyword suggestions carry Reddit-wide monthly views, not search
volume.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "kind": {
      "type": "string",
      "description": "What to look up: \"communities\" (subreddits; query required),\n\"interests\" (query filters by name), \"geolocations\" (country ISO\ncode and/or city query), \"languages\" (upper-case ISO 639-1\ncodes), \"keywords\" (comma-separated seed terms → suggestions with\nReddit-wide monthly views), \"community_suggestions\" (Reddit's\nrelated-community picks for seed communities in query and/or a\nwebsite_url), \"devices\" (device makes and models; query filters\nby make or model) or \"carriers\" (mobile carrier ids; query\nfilters by name, country by country code)."
    },
    "query": {
      "default": "",
      "type": "string",
      "description": "Search text for the chosen kind: a community search term, an\ninterest or language name filter, a city name, comma-separated\nseed keywords, comma-separated seed communities for\ncommunity_suggestions (e.g. \"PPC,googleads\"), a device make or\nmodel filter, or a carrier name filter."
    },
    "country": {
      "default": "",
      "type": "string",
      "description": "Country ISO code (e.g. \"DE\") for kinds \"geolocations\" and\n\"carriers\"; ignored for other kinds."
    },
    "website_url": {
      "default": "",
      "type": "string",
      "description": "Website for kind \"community_suggestions\"; ignored for\nother kinds."
    },
    "limit": {
      "default": 25,
      "type": "integer",
      "description": "Maximum number of results, clamped to 1-100."
    }
  },
  "required": [
    "kind"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4267)

<a id="tool-update-reddit-ad"></a>

### `update_reddit_ad`

**Platform:** Reddit Ads.

Draft changes to a Reddit ad — name, landing URL (click_url), comments on/off.

The headline and body of a live Reddit post cannot be edited; new copy
means a new ad via draft_reddit_ad, with the old ad paused. Returns a
preview with a plan_id showing old → new; nothing changes until
confirm_and_apply executes it.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Reddit ad id (from get_reddit_ads)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "name": {
      "default": "",
      "type": "string",
      "description": "New ad name; empty keeps the current one."
    },
    "click_url": {
      "default": "",
      "type": "string",
      "description": "New landing URL (http:// or https://), verified to be\nreachable. TEXT (free-form) ads open the post itself and take no\nclick_url."
    },
    "allow_comments": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "true or false turns comments on the ad's post on or\noff; omitted leaves them unchanged."
    }
  },
  "required": [
    "ad_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4762)

<a id="tool-update-reddit-ad-group"></a>

### `update_reddit_ad_group`

**Platform:** Reddit Ads.

Draft changes to a Reddit ad group — budget, bid, run dates, weekly schedule, targeting.

Budget (daily_budget or lifetime_budget + end_time) is checked against
max_daily_budget; bid_value against max_bid_increase_pct. Targeting lists
REPLACE the current value of each key passed (each takes the full list);
omitted keys are preserved. Ids/names come from search_reddit_targeting.
Budget and schedule of an ad group in a campaign-budget-optimization
campaign are set on the campaign (update_reddit_campaign). Returns a
preview with a plan_id showing old → new per field; nothing changes until
confirm_and_apply applies it.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "type": "string",
      "description": "Reddit ad group id (from get_reddit_ad_groups)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "name": {
      "default": "",
      "type": "string",
      "description": "New ad group name; empty keeps the current one."
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New daily budget in account currency (positive).\nMutually exclusive with lifetime_budget; the budget type (daily vs\nlifetime) cannot change after publishing."
    },
    "lifetime_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New lifetime budget in account currency (positive).\nNeeds an end_time (passed or already set); compared to\nmax_daily_budget by its per-day share."
    },
    "bid_value": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New bid in account currency."
    },
    "bid_strategy": {
      "default": "",
      "type": "string",
      "description": "BIDLESS, MANUAL_BIDDING, MAXIMIZE_VOLUME or TARGET_CPX."
    },
    "bid_type": {
      "default": "",
      "type": "string",
      "description": "CPC, CPM, CPV, CPV6 or CPV15."
    },
    "start_time": {
      "default": "",
      "type": "string",
      "description": "New start, ISO 8601 (e.g. 2026-10-01T00:00:00Z); a bare\nYYYY-MM-DD means 00:00 UTC that day."
    },
    "end_time": {
      "default": "",
      "type": "string",
      "description": "New end, same formats as start_time."
    },
    "geolocations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of geolocation ids to target (e.g. \"DE\" or\n\"DE:2874225\")."
    },
    "excluded_geolocations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of geolocation ids to exclude."
    },
    "communities": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of community (subreddit) names to target."
    },
    "excluded_communities": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of community names to exclude."
    },
    "interests": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of interest ids to target."
    },
    "keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of keywords to target."
    },
    "excluded_keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of keywords to exclude."
    },
    "languages": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of language codes (ISO 639-1, upper-cased\nautomatically, e.g. \"DE\")."
    },
    "gender": {
      "default": "",
      "type": "string",
      "description": "FEMALE or MALE; empty leaves gender targeting unchanged."
    },
    "platforms": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of platforms: ALL, DESKTOP, DESKTOP_LEGACY,\nMOBILE_NATIVE, MOBILE_WEB, MOBILE_WEB_3X or SHREDTOP."
    },
    "expand_targeting": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Whether Reddit may expand delivery beyond the\ntargeting; omitted leaves it unchanged."
    },
    "schedule": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Weekly delivery windows (\"time of day\" in Ads Manager), a\nlist of blocks like {\"days\": \"MON-FRI\", \"start_hour\": 13,\n\"end_hour\": 23} (day names, hours 0-23, end_hour inclusive) or the\nnative {\"start_day\": \"FRI\", \"start_hour\": 22, \"end_day\": \"SAT\",\n\"end_hour\": 3}. [] clears it (deliver at any time). Hours apply in\neach viewer's local time, not the account time zone."
    },
    "locations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Placements, FEED and/or COMMENTS_PAGE (conversation\npages); cannot be an empty list."
    },
    "excluded_interests": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of interest ids to exclude (Reddit\nmarks this field deprecated). [] clears it."
    },
    "devices": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of device targets, objects like {\"type\":\n\"MOBILE\", \"os\": \"IOS\", \"min_version\": \"16\"} (type DESKTOP or\nMOBILE; optional os ANDROID or IOS, major OS versions with iOS at\nleast 14, and label_map {make: [models]} with makes/models from\nsearch_reddit_targeting kind \"devices\"). [] clears it (every\ndevice)."
    },
    "carriers": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of mobile carrier ids (from\nsearch_reddit_targeting kind \"carriers\", e.g. \"O2_DEUTSCHLAND\"),\nchecked against Reddit's carrier list. [] clears it."
    },
    "view_modes": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of feed layouts: ALL, CARD, CLASSIC, COMPACT\nor IMMERSIVE. [] clears it."
    },
    "custom_audience_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of custom audiences to target (from\nget_reddit_audiences). It narrows the ad group to those people.\n[] clears it."
    },
    "excluded_custom_audience_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Full list of custom audiences to\nexclude, e.g. existing customers. [] clears it."
    }
  },
  "required": [
    "ad_group_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4623)

<a id="tool-update-reddit-campaign"></a>

### `update_reddit_campaign`

**Platform:** Reddit Ads.

Draft changes to a Reddit campaign — name, run dates, spend cap, and (CBO only) budget/bid/schedule.

daily_budget / lifetime_budget / bid_* / schedule apply only when the
campaign uses campaign budget optimization; otherwise the budget lives on
its ad groups (changed via update_reddit_ad_group). Budgets are in
account currency and checked against max_daily_budget; bid_value against
max_bid_increase_pct. Returns a preview with a plan_id showing old → new
per field; nothing changes until confirm_and_apply applies it.

Reddit Ads API: <https://ads-api.reddit.com/docs/v3/>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Reddit campaign id (from get_reddit_campaigns)."
    },
    "ad_account_id": {
      "default": "",
      "type": "string",
      "description": "Reddit ad account id (from list_reddit_accounts).\nEmpty uses reddit.ad_account_id from the config."
    },
    "name": {
      "default": "",
      "type": "string",
      "description": "New campaign name; empty keeps the current one."
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New daily budget in account currency (positive; CBO\nonly). Mutually exclusive with lifetime_budget; the budget type\n(daily vs lifetime) cannot change after publishing."
    },
    "lifetime_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New lifetime budget in account currency (positive;\nCBO only). Needs an end_time (passed or already set); compared to\nmax_daily_budget by its per-day share."
    },
    "spend_cap": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign spend cap in account currency; 0 removes it."
    },
    "bid_strategy": {
      "default": "",
      "type": "string",
      "description": "BIDLESS, MAXIMIZE_VOLUME or TARGET_CPX (CBO only)."
    },
    "bid_type": {
      "default": "",
      "type": "string",
      "description": "CPC, CPM, CPV, CPV6 or CPV15 (CBO only)."
    },
    "bid_value": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New bid in account currency (CBO only)."
    },
    "start_time": {
      "default": "",
      "type": "string",
      "description": "New start, ISO 8601 (e.g. 2026-10-01T00:00:00Z); a bare\nYYYY-MM-DD means 00:00 UTC that day."
    },
    "end_time": {
      "default": "",
      "type": "string",
      "description": "New end, same formats as start_time."
    },
    "schedule": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Weekly delivery windows (\"time of day\" in Ads Manager; CBO\nonly), a list of blocks like {\"days\": \"MON-FRI\", \"start_hour\": 13,\n\"end_hour\": 23} (day names, hours 0-23, end_hour inclusive) or the\nnative {\"start_day\": \"FRI\", \"start_hour\": 22, \"end_day\": \"SAT\",\n\"end_hour\": 3}. [] clears it (deliver at any time). Hours apply in\neach viewer's local time, not the account time zone. A campaign\nschedule replaces every ad group's."
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L4553)

<a id="tool-analyze-campaign-conversions"></a>

### `analyze_campaign_conversions`

**Platform:** Tracking.

Campaign clicks → GA4 conversions mapping — the real cost-per-conversion.

Combines Google Ads campaign metrics with GA4 session/conversion data to
reveal click-to-session ratios (GDPR indicator), compare Ads-reported vs
GA4-reported conversions, and compute cost-per-GA4-conversion.
Also returns non-paid channel conversion rates for comparison context.
GA4 conversions are the property's key events (GA4 metric keyEvents).

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" (see\nget_account_summaries). If empty, uses the default from config."
    },
    "campaign_name": {
      "default": "",
      "type": "string",
      "description": "Optional case-insensitive substring; only campaigns\nwhose name contains it are included. Empty = all campaigns."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1716)

<a id="tool-attribution-check"></a>

### `attribution_check`

**Platform:** Tracking.

Compare Ads-reported conversions vs GA4 — find tracking discrepancies.

Checks whether conversions reported by Google Ads match what GA4 records,
diagnoses GDPR consent gaps, attribution model differences, and missing
conversion event configuration. Returns both sides' totals with the
discrepancy and diagnostic insights. GA4 conversions are the property's
key events (GA4 metric keyEvents).

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" (see\nget_account_summaries). If empty, uses the default from config."
    },
    "conversion_events": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional list of GA4 event names to specifically\ncheck (e.g. [\"sign_up\", \"purchase\"]). If omitted, compares\naggregate totals only."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1791)

<a id="tool-generate-tracking-code"></a>

### `generate_tracking_code`

**Platform:** Tracking.

Generate a GA4 event tracking JavaScript snippet.

Produces ready-to-paste gtag code for the specified event. Includes
recommended parameters for well-known GA4 events (sign_up, purchase, etc.).
Optionally checks GA4 to warn if the event already fires. Returns the
javascript snippet, already_exists / existing_count from GA4, and notes
(duplicates, marking it as a key event, GDPR consent).

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "event_name": {
      "type": "string",
      "description": "GA4 event name for the snippet, e.g. \"sign_up\" or\n\"generate_lead\"."
    },
    "event_params": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Event parameters as a name-to-value object, e.g.\n{\"method\": \"email\"}. Missing recommended parameters for well-known\nevents are added as typed placeholders."
    },
    "trigger": {
      "default": "",
      "type": "string",
      "description": "\"form_submit\", \"button_click\", or \"page_load\" — wraps the gtag\ncall in an appropriate event listener (with a YOUR_SELECTOR\nplaceholder for forms and buttons). Empty = bare gtag call."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" used for the\nexisting-event check. If empty, uses the default from config."
    },
    "check_existing": {
      "default": true,
      "type": "boolean",
      "description": "When true (default), looks up the last 28 days of GA4\nevents to report whether this event already fires."
    }
  },
  "required": [
    "event_name"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5636)

<a id="tool-landing-page-analysis"></a>

### `landing_page_analysis`

**Platform:** Tracking.

Analyze which landing pages convert and which don't.

Combines ad final URLs with GA4 page-level data. Returns paid traffic
sessions, conversion rates, bounce rates, and engagement per landing page,
and identifies pages that get ad clicks but zero conversions and orphaned
URLs.

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "date_range_start": {
      "default": "",
      "type": "string",
      "description": "Start date as \"YYYY-MM-DD\". Both dates must be set\nto apply a range; if either is empty, the last 30 days are used."
    },
    "date_range_end": {
      "default": "",
      "type": "string",
      "description": "End date as \"YYYY-MM-DD\" (inclusive)."
    },
    "customer_id": {
      "default": "",
      "type": "string",
      "description": "Google Ads customer ID, digits with or without dashes\n(e.g. \"123-456-7890\"). Defaults to the configured ads.customer_id."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" (see\nget_account_summaries). If empty, uses the default from config."
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1756)

<a id="tool-validate-tracking"></a>

### `validate_tracking`

**Platform:** Tracking.

Compare tracking events found in the codebase against actual GA4 data.

Takes the event names found in the codebase's gtag('event', ...) or
dataLayer.push calls and checks which ones actually fire in GA4.

Returns matched events with their GA4 counts, events missing from GA4,
unexpected GA4 events, auto-collected events (page_view, session_start,
etc.), insights on likely causes, and the date range.

Google Analytics Data API: <https://developers.google.com/analytics/devguides/reporting/data/v1> and Google Ads API: <https://developers.google.com/google-ads/api/docs/start>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "expected_events": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "Event names found in the codebase, e.g. [\"sign_up\",\n\"purchase\"]."
    },
    "property_id": {
      "default": "",
      "type": "string",
      "description": "GA4 property as \"properties/123456789\" (see\nget_account_summaries). If empty, uses the default from config."
    },
    "date_range_start": {
      "default": "28daysAgo",
      "type": "string",
      "description": "Start date: \"today\", \"yesterday\", \"NdaysAgo\" (e.g.\n\"28daysAgo\"), or \"YYYY-MM-DD\"."
    },
    "date_range_end": {
      "default": "today",
      "type": "string",
      "description": "End date, same formats as date_range_start."
    }
  },
  "required": [
    "expected_events"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L5599)

<a id="tool-analyze-page-speed"></a>

### `analyze_page_speed`

**Platform:** Web performance.

Run PageSpeed Insights for a landing page — Lighthouse + real-user data.

Returns the performance score (0-100), lab Core Web Vitals (LCP, CLS,
TBT, FCP), CrUX field data from real Chrome users where available
(p75 LCP/INP/CLS/FCP/TTFB + FAST/AVERAGE/SLOW ratings), and the top
improvement opportunities with estimated savings. When the page itself
has too little traffic for field data, the origin-wide field data is
returned instead, marked field.scope="origin".

Typical input is an ad final_url: slow landing pages depress Quality
Score and waste paid clicks. Takes 10-30s; that is normal for a
Lighthouse run.

PageSpeed Insights API: <https://developers.google.com/speed/docs/insights/v5/about>

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "url": {
      "type": "string",
      "description": "Full URL of the page to analyze, e.g. an ad's final_url\n(\"https://example.com/landing\")."
    },
    "strategy": {
      "default": "mobile",
      "type": "string",
      "description": "\"mobile\" (default — most paid traffic) or \"desktop\"."
    }
  },
  "required": [
    "url"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/kLOsk/adloop/blob/ef26cefaf0e6704c458f846f15d066ba44b432bf/src/adloop/server.py#L1100)

## Attribution

Tool descriptions and schemas are extracted from the pinned upstream source under its [license](../licenses/adloop-MIT.txt). See [upstream notices](../licenses/NOTICE.txt). Catalog navigation and behavior notes were added here.
