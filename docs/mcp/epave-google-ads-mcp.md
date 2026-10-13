# epave/google-ads-mcp tools

[Main list](../../README.md) · [Search every tool](../TOOLS.md) · [Upstream](https://github.com/epave/google-ads-mcp)

**Inventory:** 59 tools. **Default tools/list:** 49. **Checked:** 2026-10-13.

**Source:** [commit 3462203](https://github.com/epave/google-ads-mcp/tree/34622039bde2882ccef27bdaa28c68024220a670). Locked dependencies; offline in-process tools/list in default and audience-enabled modes; FastMCP 4.0.3, google-ads 32.0.0.

Default clients see 49 tools. `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` adds 10 audience/creator insight tools that also require Google allowlisting. Write tools stay listed when writes are disabled; apply requires `GOOGLE_ADS_WRITE_ENABLED=true` and confirmation by default. Previews and audit records use local DuckDB.

Descriptions and parameter JSON below preserve the registered MCP interface. Open each parameter block for required fields, defaults, enums, nested objects, and references. Prose-only restrictions and free-form objects remain as upstream declares them. No tool was invoked and no live account operation was tested.

## Tools

- [Accounts, queries, and performance (13)](#accounts-queries-and-performance)
- [Keyword research and search terms (6)](#keyword-research-and-search-terms)
- [Campaigns, budgets, bidding, and targeting (11)](#campaigns-budgets-bidding-and-targeting)
- [Ads and creative assets (10)](#ads-and-creative-assets)
- [Audiences and audience insights (14)](#audiences-and-audience-insights)
- [Conversions and measurement (1)](#conversions-and-measurement)
- [Experiments and recommendations (1)](#experiments-and-recommendations)
- [Previews, validation, and local helpers (3)](#previews-validation-and-local-helpers)

## Accounts, queries, and performance

<a id="tool-get-campaign"></a>

### `get_campaign`

Get one campaign plus its budget and recent 7-day performance.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/campaigns.py#L49)

<a id="tool-get-campaign-dashboard"></a>

### `get_campaign_dashboard`

Compact live dashboard of campaigns for an agent to read and act on.

Returns status, daily budget, today and last-7-day spend/clicks/conversions,
CPA, ROAS, serving alerts, and deltas versus the previous local snapshot.
This is an MCP tool, not a web UI.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "include_paused": {
      "default": false,
      "type": "boolean"
    },
    "persist_snapshot": {
      "default": true,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/dashboard.py#L31)

<a id="tool-get-campaign-diagnostics"></a>

### `get_campaign_diagnostics`

One-call campaign health: status, performance, IS, ads, keywords, assets, findings.

Findings use severity critical/warning/opportunity/informational and origin
GOOGLE_API (pending Google recommendations) or LOCAL_DIAGNOSTIC (observed issues).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/diagnostics.py#L13)

<a id="tool-get-campaign-hints"></a>

### `get_campaign_hints`

**Behavior:** Computes local diagnostic hints from fetched Google Ads data; these are not Google recommendation-service results.

Combine Google API recommendations with local diagnostic findings.

Google items use origin=GOOGLE_API. Observed problems (IS lost, missing
callouts, policy review, learning, no delivery, etc.) use origin=LOCAL_DIAGNOSTIC.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L461)

<a id="tool-get-change-events"></a>

### `get_change_events`

Recent account change events (last 7 days).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "limit": {
      "default": 50,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L278)

<a id="tool-get-demand-gen-readiness"></a>

### `get_demand_gen_readiness`

Check a Demand Gen campaign before enabling it.

Fails when no audience is attached, lists are ineligible or under 100 Display
users, optimized targeting is unexpectedly on, extra channels are enabled,
Stockholm (or requested) geo is missing, Purchase is not the custom goal, or
required assets are missing/disapproved.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "expected_channels": {
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
      "default": null
    },
    "expected_geo_target_constant_ids": {
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
      "default": null
    },
    "purchase_action_ids": {
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
      "default": null
    },
    "expect_optimized_targeting": {
      "default": false,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/demand_gen.py#L215)

<a id="tool-get-impression-share-summary"></a>

### `get_impression_share_summary`

Search impression share, top/absolute-top share, and lost share from budget vs rank.

Returns account and campaign rows for the current window plus deltas versus the
previous equal-length period. Shares are percents (0-100). Defaults to SEARCH
campaigns. The account row is customer-level Search impression share (all Search
inventory); campaign rows use `channel` and status filters. Windows use the Ads
account timezone and are clamped to yesterday because impression share is not
available for the current day.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "date_range": {
      "default": "LAST_7_DAYS",
      "type": "string"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "include_paused": {
      "default": false,
      "type": "boolean"
    },
    "channel": {
      "default": "SEARCH",
      "type": "string"
    },
    "limit": {
      "default": 100,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L180)

<a id="tool-get-resource-metadata"></a>

### `get_resource_metadata`

Describe selectable fields for a Google Ads resource such as campaign or ad_group.

Mirrors the official `get_resource_metadata` tool so an agent can discover
valid GAQL fields before calling search.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "resource": {
      "type": "string"
    },
    "limit": {
      "default": 200,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "resource"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/query.py#L60)

<a id="tool-list-accessible-customers"></a>

### `list_accessible_customers`

List Google Ads accounts the authenticated user can access.

Returns customer IDs and, when queryable, descriptive names. Use a returned
customer_id on every later tool call. If you access accounts through a
manager (MCC), pass login_customer_id or set GOOGLE_ADS_LOGIN_CUSTOMER_ID.
Pass login_customer_id="none" to omit a cached MCC header.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  }
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/accounts.py#L15)

<a id="tool-list-ad-groups"></a>

### `list_ad_groups`

List ad groups, optionally filtered to one campaign.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "limit": {
      "default": 100,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/campaigns.py#L78)

<a id="tool-list-ads"></a>

### `list_ads`

List ads with type, status, and policy summary.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_group_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "limit": {
      "default": 50,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/campaigns.py#L100)

<a id="tool-list-campaigns"></a>

### `list_campaigns`

List campaigns with status, channel, budget, and bidding strategy.

status can be ENABLED, PAUSED, REMOVED, or ALL.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "ENABLED"
    },
    "limit": {
      "default": 100,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/campaigns.py#L14)

<a id="tool-search"></a>

### `search`

Run a Google Ads Query Language (GAQL) search.

Same capability as the official Google Ads MCP `search` tool. Example:
fields=["campaign.id", "campaign.name", "metrics.clicks"], resource="campaign",
conditions=["campaign.status = 'ENABLED'", "segments.date DURING LAST_7_DAYS"].
Use get_resource_metadata first if you are unsure which fields exist.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "fields": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "resource": {
      "type": "string"
    },
    "conditions": {
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
      "default": null
    },
    "orderings": {
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
      "default": null
    },
    "limit": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 100
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "fields",
    "resource"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/query.py#L32)

## Keyword research and search terms

<a id="tool-add-keywords"></a>

### `add_keywords`

Add keywords to an existing ad group. match_type: BROAD, PHRASE, or EXACT.

Keywords are created PAUSED so they do not serve on a live campaign until
you enable them with set_keyword_status. Pass status=ENABLED to serve immediately.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_group_id": {
      "type": "string"
    },
    "keywords": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "match_type": {
      "default": "BROAD",
      "type": "string"
    },
    "status": {
      "default": "PAUSED",
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "ad_group_id",
    "keywords"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L268)

<a id="tool-get-search-term-insight-terms"></a>

### `get_search_term_insight_terms`

Search terms inside one Search term insights category.

campaign_id plus insight_id is required for campaign-level / PMax terms.
Account-level categories only need insight_id. GAQL cannot LIMIT or ORDER BY
while segmenting by search term, so `limit` is applied after ranking by
impressions.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "insight_id": {
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "date_range": {
      "default": "LAST_7_DAYS",
      "type": "string"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "limit": {
      "default": 100,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "insight_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L144)

<a id="tool-get-search-term-insights"></a>

### `get_search_term_insights`

Search term insight categories with volume, clicks, conversions, and emerging demand.

Pass campaign_id for campaign_search_term_insight (needed for Performance Max).
Omit it for account-level customer_search_term_insight. Then call
get_search_term_insight_terms with a returned insight id to list terms
inside one category. Empty Google catch-all labels are returned as
Uncategorized. Search volume is a {min, max} range when Google sends bounds.
Emerging categories are new versus the previous equal window, or grew
search volume by 25%+.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "date_range": {
      "default": "LAST_7_DAYS",
      "type": "string"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "limit": {
      "default": 50,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L88)

<a id="tool-get-search-terms"></a>

### `get_search_terms`

Top raw search terms for the last 7 days from search_term_view.

For category-level Search term insights (PMax included), use
get_search_term_insights instead.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "limit": {
      "default": 50,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L61)

<a id="tool-list-keywords"></a>

### `list_keywords`

List keywords with match type, status, and bid.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_group_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "limit": {
      "default": 200,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/campaigns.py#L123)

<a id="tool-set-keyword-status"></a>

### `set_keyword_status`

Set a keyword criterion to ENABLED, PAUSED, or REMOVED.

REMOVED permanently deletes the keyword and requires force=true.
Detects state drift between preview and apply: if the keyword was removed
in the UI, apply fails without consuming the confirm_token. If the keyword
is already at the target status, apply is an idempotent no-op.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_group_id": {
      "type": "string"
    },
    "criterion_id": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "force": {
      "default": false,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "ad_group_id",
    "criterion_id",
    "status"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/writes.py#L231)

## Campaigns, budgets, bidding, and targeting

<a id="tool-add-campaign-languages"></a>

### `add_campaign_languages`

Add language targeting to a campaign using language constant IDs (e.g. 1000 for English).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "language_constant_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id",
    "language_constant_ids"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L482)

<a id="tool-add-campaign-locations"></a>

### `add_campaign_locations`

Add location targeting to a campaign using geo target constant IDs (e.g. 2840 for US).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "geo_target_constant_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id",
    "geo_target_constant_ids"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L442)

<a id="tool-create-ad-group"></a>

### `create_ad_group`

Create a PAUSED ad group under an existing campaign.

Defaults to PAUSED so expanding a live campaign cannot spend until you
enable the ad group. Pass status=ENABLED only when that is intentional.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "status": {
      "default": "PAUSED",
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id",
    "name"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L327)

<a id="tool-create-demand-gen-campaign"></a>

### `create_demand_gen_campaign`

Create a paused Demand Gen campaign in one atomic mutate.

Does not use the legacy Display builder. Campaign, ad group, and ad stay
PAUSED. Defaults to Display-only channel controls, optimized targeting off,
Stockholm County geo (21000) and Swedish (1015) at the ad group. Maximize
Clicks does not set a CPC ceiling unless target_cpc is provided. Pass an
Audience id from create_audience. conversion_action_ids become a campaign
custom goal (Purchase-only bidding).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "daily_budget": {
      "type": "number"
    },
    "final_url": {
      "type": "string"
    },
    "business_name": {
      "type": "string"
    },
    "headlines": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "descriptions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "marketing_image_assets": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "square_marketing_image_assets": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "logo_image_assets": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "audience_id": {
      "type": "string"
    },
    "geo_target_constant_ids": {
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
      "default": null
    },
    "language_constant_ids": {
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
      "default": null
    },
    "channels": {
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
      "default": null
    },
    "optimized_targeting_enabled": {
      "default": false,
      "type": "boolean"
    },
    "bidding_strategy": {
      "default": "MAXIMIZE_CLICKS",
      "type": "string"
    },
    "target_cpc": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "target_cpa": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "conversion_action_ids": {
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
      "default": null
    },
    "contains_eu_political": {
      "default": false,
      "type": "boolean"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "name",
    "daily_budget",
    "final_url",
    "business_name",
    "headlines",
    "descriptions",
    "marketing_image_assets",
    "square_marketing_image_assets",
    "logo_image_assets",
    "audience_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/demand_gen.py#L30)

<a id="tool-create-display-campaign"></a>

### `create_display_campaign`

Create a paused Display campaign with a Responsive Display Ad.

Upload images first with upload_image_asset. Marketing image must be 1.91:1
(min 600x314). Square marketing image must be 1:1 (min 300x300).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "daily_budget": {
      "type": "number"
    },
    "final_url": {
      "type": "string"
    },
    "business_name": {
      "type": "string"
    },
    "headlines": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "long_headline": {
      "type": "string"
    },
    "descriptions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "marketing_image_asset": {
      "type": "string"
    },
    "square_marketing_image_asset": {
      "type": "string"
    },
    "logo_image_asset": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "bidding_strategy": {
      "default": "MAXIMIZE_CONVERSIONS",
      "type": "string"
    },
    "target_cpa": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "contains_eu_political": {
      "default": false,
      "type": "boolean"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "name",
    "daily_budget",
    "final_url",
    "business_name",
    "headlines",
    "long_headline",
    "descriptions",
    "marketing_image_asset",
    "square_marketing_image_asset"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L110)

<a id="tool-create-pmax-campaign"></a>

### `create_pmax_campaign`

Create a paused standard Performance Max campaign (not retail/Merchant Center).

Requires a logo asset plus landscape and square marketing images. Upload those
with upload_image_asset first. Brand guidelines are on by default.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "daily_budget": {
      "type": "number"
    },
    "final_url": {
      "type": "string"
    },
    "business_name": {
      "type": "string"
    },
    "headlines": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "long_headline": {
      "type": "string"
    },
    "descriptions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "logo_asset": {
      "type": "string"
    },
    "marketing_image_asset": {
      "type": "string"
    },
    "square_marketing_image_asset": {
      "type": "string"
    },
    "bidding_strategy": {
      "default": "MAXIMIZE_CONVERSIONS",
      "type": "string"
    },
    "target_cpa": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "brand_guidelines_enabled": {
      "default": true,
      "type": "boolean"
    },
    "contains_eu_political": {
      "default": false,
      "type": "boolean"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "name",
    "daily_budget",
    "final_url",
    "business_name",
    "headlines",
    "long_headline",
    "descriptions",
    "logo_asset",
    "marketing_image_asset",
    "square_marketing_image_asset"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L186)

<a id="tool-create-search-campaign"></a>

### `create_search_campaign`

Create a paused Search campaign with budget, ad group, RSA, and keywords.

Requires at least 3 headlines (≤30 chars) and 2 descriptions (≤90 chars).
The campaign is always created PAUSED. Enable it separately after review.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "daily_budget": {
      "type": "number"
    },
    "final_url": {
      "type": "string"
    },
    "headlines": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "descriptions": {
      "items": {
        "type": "string"
      },
      "type": "array"
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
      "default": null
    },
    "bidding_strategy": {
      "default": "MAXIMIZE_CLICKS",
      "type": "string"
    },
    "target_cpa": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "ad_group_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "path1": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "path2": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "contains_eu_political": {
      "default": false,
      "type": "boolean"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "name",
    "daily_budget",
    "final_url",
    "headlines",
    "descriptions"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L28)

<a id="tool-set-ad-group-status"></a>

### `set_ad_group_status`

Set an ad group to ENABLED, PAUSED, or REMOVED.

REMOVED permanently deletes the ad group and requires force=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_group_id": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "force": {
      "default": false,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "ad_group_id",
    "status"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/writes.py#L92)

<a id="tool-set-campaign-status"></a>

### `set_campaign_status`

Set a campaign to ENABLED, PAUSED, or REMOVED.

Defaults to dry_run. Re-call with the returned confirm_token to apply.
Writes require GOOGLE_ADS_WRITE_ENABLED=true.
REMOVED permanently deletes the campaign via CampaignOperation.remove and
requires force=true. ENABLED/PAUSED update campaign.status.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "force": {
      "default": false,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id",
    "status"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/writes.py#L41)

<a id="tool-update-campaign-bidding"></a>

### `update_campaign_bidding`

Update a campaign bidding strategy.

bidding_strategy: MANUAL_CPC, MAXIMIZE_CLICKS, MAXIMIZE_CONVERSIONS,
TARGET_CPA, or MAXIMIZE_CONVERSION_VALUE.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "bidding_strategy": {
      "type": "string"
    },
    "target_cpa": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id",
    "bidding_strategy"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/writes.py#L444)

<a id="tool-update-campaign-budget"></a>

### `update_campaign_budget`

Change a campaign's daily budget. Amount is in account currency, not micros.

Increases above GOOGLE_ADS_BUDGET_INCREASE_CAP (default 20%) require force=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "daily_budget": {
      "type": "number"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "force": {
      "default": false,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id",
    "daily_budget"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/writes.py#L383)

## Ads and creative assets

<a id="tool-add-asset-group-text"></a>

### `add_asset_group_text`

Add headline/description text assets to an existing Performance Max asset group.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "asset_group_id": {
      "type": "string"
    },
    "headlines": {
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
      "default": null
    },
    "descriptions": {
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
      "default": null
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "asset_group_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L521)

<a id="tool-add-campaign-callouts"></a>

### `add_campaign_callouts`

Create or reuse callout assets and attach them to one or more campaigns.

Idempotent: re-running the same request does not create duplicate assets or links.
Defaults to dry_run; re-call with confirm_token to apply. Multi-campaign attaches
are one atomic GoogleAdsService.mutate.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "callouts": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "reuse_existing": {
      "default": true,
      "type": "boolean"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_ids",
    "callouts"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/assets.py#L497)

<a id="tool-add-campaign-structured-snippet"></a>

### `add_campaign_structured_snippet`

Create or reuse a structured snippet and attach it to campaigns atomically.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "header": {
      "type": "string"
    },
    "values": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "reuse_existing": {
      "default": true,
      "type": "boolean"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_ids",
    "header",
    "values"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/assets.py#L563)

<a id="tool-attach-campaign-assets"></a>

### `attach_campaign_assets`

Attach existing assets to campaigns. Skips links that already exist.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "asset_resource_names": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "field_type": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_ids",
    "asset_resource_names",
    "field_type"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/assets.py#L662)

<a id="tool-detach-campaign-asset"></a>

### `detach_campaign_asset`

Detach an asset from a campaign (reversible). Does not delete the asset globally.

Uses CampaignAsset remove (status REMOVED), so force=true is required.
Idempotent: if the link is already REMOVED or missing, returns a no-op apply.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_asset_resource_name": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "force": {
      "default": false,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_asset_resource_name"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/assets.py#L735)

<a id="tool-get-asset-review-status"></a>

### `get_asset_review_status`

Return policy / review status for assets (read-only; does not mutate).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "asset_ids": {
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
      "default": null
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/assets.py#L200)

<a id="tool-list-campaign-assets"></a>

### `list_campaign_assets`

List campaign-level assets (callouts, structured snippets, sitelinks, …).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "field_types": {
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
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/assets.py#L170)

<a id="tool-set-ad-status"></a>

### `set_ad_status`

Set an ad to ENABLED, PAUSED, or REMOVED.

REMOVED permanently deletes the ad and requires force=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_group_id": {
      "type": "string"
    },
    "ad_id": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "force": {
      "default": false,
      "type": "boolean"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "ad_group_id",
    "ad_id",
    "status"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/writes.py#L136)

<a id="tool-update-responsive-search-ad"></a>

### `update_responsive_search_ad`

Replace headlines and descriptions on an existing responsive search ad.

Pass the full headline and description lists. Google Ads replaces the set.
Headlines must be ≤30 characters; descriptions ≤90.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_id": {
      "type": "string"
    },
    "headlines": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "descriptions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "final_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "path1": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "path2": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "ad_id",
    "headlines",
    "descriptions"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/creates.py#L376)

<a id="tool-upload-image-asset"></a>

### `upload_image_asset`

Upload an image asset from a local file path or HTTPS URL.

Local paths must stay under GOOGLE_ADS_ASSET_ROOT (cwd by default).
HTTPS URLs must resolve to a public IP; redirects are rejected.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "source": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "name",
    "source"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/assets.py#L124)

## Audiences and audience insights

<a id="tool-attach-audience-to-ad-group"></a>

### `attach_audience_to_ad_group`

Attach an Audience to a Demand Gen ad group.

Sets ad_group.audience_setting.use_audience_grouped=true and creates an
audience AdGroupCriterion.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "ad_group_id": {
      "type": "string"
    },
    "audience_id": {
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "ad_group_id",
    "audience_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/audiences.py#L139)

<a id="tool-create-audience"></a>

### `create_audience`

Create a reusable Audience from included/excluded user-list IDs.

Demand Gen targets this Audience via attach_audience_to_ad_group or
create_demand_gen_campaign(audience_id=...). GA4 event lists must already
exist in Google Ads (imported from GA4).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "included_user_list_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "excluded_user_list_ids": {
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
      "default": null
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "name",
    "included_user_list_ids"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/audiences.py#L85)

<a id="tool-generate-audience-composition-insights"></a>

### `generate_audience_composition_insights`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

Compare an audience's affinities and demographics against a baseline.

Allowlisted. attributes are compact objects such as {"entity": "/m/014trl"} or
items returned by list_audience_insights_attributes. data_month is YYYY-MM.
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "country_locations": {
      "items": {
        "type": "string"
      },
      "type": "array"
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
      "default": null
    },
    "gender": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "age_ranges": {
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
      "default": null
    },
    "parental_status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "attributes": {
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
      "default": null
    },
    "attribute_groups": {
      "anyOf": [
        {
          "items": {
            "items": {
              "additionalProperties": true,
              "type": "object"
            },
            "type": "array"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "data_month": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "country_locations"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L597)

<a id="tool-generate-audience-definition"></a>

### `generate_audience_definition`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

Turn a text audience description into ranked audience attributes.

Allowlisted. country_location is a geo target ID such as 2840 (United States).
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "country_location": {
      "type": "string"
    },
    "audience_description": {
      "type": "string"
    },
    "marketing_objective": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "country_location",
    "audience_description"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L573)

<a id="tool-generate-audience-overlap-insights"></a>

### `generate_audience_overlap_insights`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

Estimate YouTube reach overlap between a primary attribute and other audiences.

Allowlisted. primary_attribute example: {"user_interest": "80428"} or {"entity": "/m/014trl"}.
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "country_location": {
      "type": "string"
    },
    "primary_attribute": {
      "additionalProperties": true,
      "type": "object"
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
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "country_location",
    "primary_attribute"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L632)

<a id="tool-generate-creator-insights"></a>

### `generate_creator_insights`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

Discover YouTube creators or fetch insights for specific channels.

ContentCreatorInsightsService is allowlisted and in beta. Provide exactly one of:
audience_attributes (optionally with creator_attributes), topics (knowledge-graph
IDs from list_audience_insights_attributes), or youtube_channel_ids.
Topic search allows one country only. supplemental_data: LOCAL_CREATOR_DATA.
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "country_locations": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "audience_attributes": {
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
      "default": null
    },
    "creator_attributes": {
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
      "default": null
    },
    "topics": {
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
      "default": null
    },
    "youtube_channel_ids": {
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
      "default": null
    },
    "sub_country_locations": {
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
      "default": null
    },
    "supplemental_data": {
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
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "country_locations"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L742)

<a id="tool-generate-insights-finder-report"></a>

### `generate_insights_finder_report`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

**Behavior:** Creates a remote saved report and is write-gated, despite the generate prefix. Requires both the audience-insights flag and Google allowlisting.

Create a saved Insights Finder report and return its URL.

Allowlisted. Creates a remote report, so this goes through SafetyGate: preview
with dry_run=true, then apply with confirm_token. Writes need
GOOGLE_ADS_WRITE_ENABLED=true. Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "country_locations": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "attributes": {
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
      "default": null
    },
    "gender": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "age_ranges": {
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
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "country_locations"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L685)

<a id="tool-generate-suggested-targeting-insights"></a>

### `generate_suggested_targeting_insights`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

Suggest targetable YouTube audiences from a text description or structured audience.

Allowlisted. Pass audience_description plus country_location (e.g. 2840), or an
audience object with country_locations and optional gender/age_ranges/attributes.
marketing_objective: AWARENESS, CONSIDERATION, or RESEARCH.
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "country_location": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "audience_description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "audience": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "marketing_objective": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
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
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L543)

<a id="tool-generate-targeting-suggestion-metrics"></a>

### `generate_targeting_suggestion_metrics`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

Estimate YouTube reach for one or more audience definitions.

Allowlisted. Each audience needs country_locations (geo IDs). You can pass a
list of audiences or a single audience via country_locations plus filters.
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "audiences": {
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
      "default": null
    },
    "country_locations": {
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
      "default": null
    },
    "gender": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "age_ranges": {
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
      "default": null
    },
    "attributes": {
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
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L656)

<a id="tool-generate-trending-insights"></a>

### `generate_trending_insights`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

YouTube trending insights for an audience or a list of topics.

Allowlisted. Provide audience_attributes or topics (knowledge-graph IDs), not both.
supplemental_data: LOCAL_CREATOR_DATA, BRAND_SENTIMENT_DATA.
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "country_location": {
      "type": "string"
    },
    "audience_attributes": {
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
      "default": null
    },
    "topics": {
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
      "default": null
    },
    "supplemental_data": {
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
      "default": null
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "country_location"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L777)

<a id="tool-list-audience-insights-attributes"></a>

### `list_audience_insights_attributes`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

List audience attributes you can pass into other Insights tools.

AudienceInsightsService is allowlisted. dimensions examples: AFFINITY_USER_INTEREST,
IN_MARKET_USER_INTEREST, CATEGORY, AGE_RANGE, GENDER, KNOWLEDGE_GRAPH.
query_text is required for KNOWLEDGE_GRAPH topic search. entity_capabilities
filters topics (CREATOR_TOPIC_INSIGHTS, CONTENT_TRENDING_INSIGHTS, BRAND,
CREATOR_ATTRIBUTE). country_location is a geo target ID such as 2840 (US).
Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
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
      "default": null
    },
    "query_text": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "country_location": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "location_country_filters": {
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
      "default": null
    },
    "entity_capabilities": {
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
      "default": null
    },
    "get_all_creator_attributes": {
      "default": false,
      "type": "boolean"
    },
    "insights_group": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L500)

<a id="tool-list-audiences"></a>

### `list_audiences`

List reusable Audience resources (Demand Gen / Performance Max targeting).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "limit": {
      "default": 100,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/audiences.py#L67)

<a id="tool-list-insights-eligible-dates"></a>

### `list_insights_eligible_dates`

Requires `GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true` and Google allowlisting.

Months that have audience composition data, plus the current last-30-days window.

Requires GOOGLE_ADS_AUDIENCE_INSIGHTS_ENABLED=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  }
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L534)

<a id="tool-list-user-lists"></a>

### `list_user_lists`

List remarketing / customer-match user lists and Display eligibility.

Returns size_for_display and eligible_for_display so you can see when a list
reaches Google's 100-user Display serving threshold. Ads API v25 no longer
exposes prepopulation_status; that field is always null. GA4 event audiences
should be created in GA4 and imported — this tool only reads Ads user lists.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "limit": {
      "default": 100,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/audiences.py#L26)

## Conversions and measurement

<a id="tool-set-campaign-conversion-actions"></a>

### `set_campaign_conversion_actions`

Apply a custom conversion goal so the campaign bids only on these actions.

Use this to bid toward Purchase and ignore lead-form or analysis-start events.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "type": "string"
    },
    "conversion_action_ids": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "dry_run": {
      "default": true,
      "type": "boolean"
    },
    "confirm_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id",
    "campaign_id",
    "conversion_action_ids"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/demand_gen.py#L154)

## Experiments and recommendations

<a id="tool-get-recommendations"></a>

### `get_recommendations`

Google Ads optimization recommendations that are still pending.

Optional campaign_id and types filters. Each item is tagged origin=GOOGLE_API
with type-specific details when the API returns them. Google Ads UI and API
recommendations may differ or update at different times.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "types": {
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
      "default": null
    },
    "limit": {
      "default": 25,
      "type": "integer"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "customer_id"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L295)

## Previews, validation, and local helpers

<a id="tool-get-local-audit"></a>

### `get_local_audit`

**Behavior:** Reads local DuckDB audit records; it does not fetch Google Ads change history.

Read recent mutations and previews stored in the local DuckDB 2.0 audit log.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "limit": {
      "default": 20,
      "type": "integer"
    }
  }
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/insights.py#L495)

<a id="tool-get-server-info"></a>

### `get_server_info`

Return server version, API version, write state, tools, and credential health.

Credential fields are booleans only — secrets are never returned. Safe to call
when writes are disabled or Ads credentials are missing.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {}
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/server_info.py#L217)

<a id="tool-refresh-preview"></a>

### `refresh_preview`

**Behavior:** Extends local preview expiry and audit state. Keyword preview refresh can also reread the current keyword state from Google Ads.

Extend an unused preview token's expiry and re-snapshot observed state when possible.

Re-call with the same confirm_token; the token value does not change.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "confirm_token": {
      "type": "string"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    }
  },
  "required": [
    "confirm_token"
  ]
}
```

</details>

[Source](https://github.com/epave/google-ads-mcp/blob/34622039bde2882ccef27bdaa28c68024220a670/src/google_ads_mcp/tools/writes.py#L353)

## Attribution

Tool descriptions and schemas are extracted from the pinned upstream source under its [license](../licenses/epave-MIT.txt). See [upstream notices](../licenses/NOTICE.txt). Catalog navigation and behavior notes were added here.
