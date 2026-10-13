# FGRibreau/mcp-google-ads tools

[Main list](../../README.md) · [Search every tool](../TOOLS.md) · [Upstream](https://github.com/FGRibreau/mcp-google-ads)

**Inventory:** 63 tools. **Default tools/list:** 63. **Checked:** 2026-10-13.

**Source:** [commit 5e8d073](https://github.com/FGRibreau/mcp-google-ads/tree/5e8d073b76bc723cfdb1978a345add69f3412a73). Built locked source; stdio initialize + tools/list in normal and read-only modes.

All 63 tools remain listed when `GOOGLE_ADS_READ_ONLY=true`; 43 are blocked at invocation. Change tools generally stage in-memory plans, and `confirm_and_apply` performs the apply. Its default dry run returns a local preview, not Google Ads API validation; plans do not survive a restart.

Descriptions and parameter JSON below preserve the registered MCP interface. Open each parameter block for required fields, defaults, enums, nested objects, and references. Prose-only restrictions and free-form objects remain as upstream declares them. No tool was invoked and no live account operation was tested.

## Tools

- [Accounts, queries, and performance (9)](#accounts-queries-and-performance)
- [Keyword research and search terms (18)](#keyword-research-and-search-terms)
- [Campaigns, budgets, bidding, and targeting (18)](#campaigns-budgets-bidding-and-targeting)
- [Ads and creative assets (9)](#ads-and-creative-assets)
- [Audiences and audience insights (1)](#audiences-and-audience-insights)
- [Conversions and measurement (3)](#conversions-and-measurement)
- [Experiments and recommendations (3)](#experiments-and-recommendations)
- [Previews, validation, and local helpers (2)](#previews-validation-and-local-helpers)

## Accounts, queries, and performance

<a id="tool-get-account-info"></a>

### `get_account_info`

Get detailed information about a Google Ads account (currency, timezone, status).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L830)

<a id="tool-get-ad-performance"></a>

### `get_ad_performance`

Get ad-level performance metrics including headlines, descriptions, and final URLs. Defaults to last 30 days if no dates given.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_end": {
      "description": "End date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_start": {
      "description": "Start date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L862)

<a id="tool-get-campaign-performance"></a>

### `get_campaign_performance`

Get campaign-level performance metrics (impressions, clicks, cost, conversions, CTR, CPC, CPA). Defaults to last 30 days if no dates given.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_end": {
      "description": "End date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_start": {
      "description": "Start date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L843)

<a id="tool-get-keyword-forecasts"></a>

### `get_keyword_forecasts`

**Behavior:** Despite its name, this reads existing keyword_view metrics for LAST_30_DAYS. It does not call the Keyword Plan forecasting API.

Get historical keyword performance metrics for forecasting.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "keyword_texts": {
      "description": "Keywords to get forecasts for.",
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [
    "keyword_texts"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2050)

<a id="tool-get-policy-issues"></a>

### `get_policy_issues`

Get policy issues for ads (disapproved, limited, under review).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2064)

<a id="tool-list-accounts"></a>

### `list_accounts`

List all accessible Google Ads accounts. If a Manager (MCC) account is configured, lists all sub-accounts.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L819)

<a id="tool-list-extensions"></a>

### `list_extensions`

List campaign-level extensions (sitelinks, callouts, structured snippets). Returns up to 500 non-removed extensions.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L959)

<a id="tool-remove-extension"></a>

### `remove_extension`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft REMOVING a campaign extension (IRREVERSIBLE). Specify campaign_id, asset_id, and field_type (SITELINK, CALLOUT, or STRUCTURED_SNIPPET).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "asset_id": {
      "description": "The asset ID of the extension.",
      "type": "string"
    },
    "campaign_id": {
      "description": "The campaign ID the extension is linked to.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "field_type": {
      "description": "Extension type: SITELINK, CALLOUT, or STRUCTURED_SNIPPET.",
      "type": "string"
    }
  },
  "required": [
    "campaign_id",
    "asset_id",
    "field_type"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1631)

<a id="tool-run-gaql"></a>

### `run_gaql`

Execute an arbitrary GAQL (Google Ads Query Language) query. Supports json, table, and csv output formats.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "format": {
      "description": "Output format: json (default), table, or csv",
      "type": [
        "string",
        "null"
      ]
    },
    "query": {
      "description": "GAQL query string (e.g. SELECT campaign.id, campaign.name FROM campaign)",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L972)

## Keyword research and search terms

<a id="tool-add-negative-keywords"></a>

### `add_negative_keywords`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft negative keyword additions to prevent ads from showing for irrelevant searches.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to add negative keywords to.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "keywords": {
      "description": "Keywords to add as negatives.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "match_type": {
      "description": "Match type for all keywords (default \"EXACT\"). One of: EXACT, PHRASE, BROAD.",
      "type": [
        "string",
        "null"
      ]
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1246)

<a id="tool-add-to-negative-keyword-list"></a>

### `add_to_negative_keyword_list`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Add keywords to an existing negative keyword list. Adding a keyword the list already holds fails the whole batch — check get_negative_keyword_list first. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "keywords": {
      "description": "Keywords to add.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "match_type": {
      "description": "Match type for all keywords (default \"PHRASE\"). One of: EXACT, PHRASE, BROAD.",
      "type": [
        "string",
        "null"
      ]
    },
    "shared_set_id": {
      "description": "Numeric ID of the negative keyword list (shared set).",
      "type": "string"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1301)

<a id="tool-attach-negative-keyword-list"></a>

### `attach_negative_keyword_list`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Attach a negative keyword list to one or more campaigns. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_ids": {
      "description": "Campaign IDs to attach to / detach from.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "shared_set_id": {
      "description": "Numeric ID of the negative keyword list (shared set).",
      "type": "string"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1351)

<a id="tool-create-negative-keyword-list"></a>

### `create_negative_keyword_list`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Create a negative keyword list (shared set) and, in the same atomic mutate, seed it with keywords and attach it to campaigns. Use this instead of repeating the same negatives on every campaign: one list edited once propagates to every campaign it is attached to. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_ids": {
      "description": "Campaign IDs to attach the new list to. May be empty.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "keywords": {
      "description": "Keywords to seed the list with. May be empty.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "match_type": {
      "description": "Match type for all keywords (default \"PHRASE\"). One of: EXACT, PHRASE, BROAD.",
      "type": [
        "string",
        "null"
      ]
    },
    "name": {
      "description": "Name for the list. Must be unique within the account.",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1274)

<a id="tool-delete-negative-keyword-list"></a>

### `delete_negative_keyword_list`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Delete a negative keyword list entirely (IRREVERSIBLE). Every campaign attached to it loses those exclusions.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "shared_set_id": {
      "description": "Numeric ID of the negative keyword list (shared set).",
      "type": "string"
    }
  },
  "required": [
    "shared_set_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1399)

<a id="tool-detach-negative-keyword-list"></a>

### `detach_negative_keyword_list`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Detach a negative keyword list from one or more campaigns (IRREVERSIBLE link removal). Those campaigns immediately lose every exclusion the list carries; the list itself is kept.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_ids": {
      "description": "Campaign IDs to attach to / detach from.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "shared_set_id": {
      "description": "Numeric ID of the negative keyword list (shared set).",
      "type": "string"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1375)

<a id="tool-discover-keywords"></a>

### `discover_keywords`

Discover keyword ideas from seed keywords using the Keyword Planner.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "seed_keywords": {
      "description": "Seed keywords to generate ideas from.",
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [
    "seed_keywords"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2038)

<a id="tool-draft-keywords"></a>

### `draft_keywords`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft keyword additions with match types (EXACT, PHRASE, BROAD). Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "KeywordInput": {
      "description": "Input for a keyword to add during campaign drafting.",
      "properties": {
        "final_url": {
          "description": "Optional keyword-level final URL override. When set, clicks on this\nkeyword route to this landing page (`ad_group_criterion.final_urls`)\ninstead of inheriting the ad's final URL. Must be an absolute http(s)\nURL. Omit to inherit the ad's final URL.",
          "type": [
            "string",
            "null"
          ]
        },
        "match_type": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "text",
        "match_type"
      ],
      "type": "object"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID to add keywords to.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "keywords": {
      "description": "Keywords with match types to add.",
      "items": {
        "$ref": "#/$defs/KeywordInput"
      },
      "type": "array"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1217)

<a id="tool-get-keyword-performance"></a>

### `get_keyword_performance`

Get keyword-level performance metrics including quality score, match type, CPC, and conversions. Defaults to last 30 days if no dates given.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_end": {
      "description": "End date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_start": {
      "description": "Start date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L877)

<a id="tool-get-negative-keyword-list"></a>

### `get_negative_keyword_list`

Get the keywords inside one negative keyword list, with the criterion_id of each — the handle remove_from_negative_keyword_list needs.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "shared_set_id": {
      "description": "Numeric ID of the negative keyword list (shared set).",
      "type": "string"
    }
  },
  "required": [
    "shared_set_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L942)

<a id="tool-get-negative-keywords"></a>

### `get_negative_keywords`

Get all campaign-level negative keywords. These are negatives written directly on a campaign — exclusions coming from a shared negative keyword list are NOT included here; call list_negative_keyword_lists for those. A campaign's effective exclusions are the union of both.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L912)

<a id="tool-get-search-terms"></a>

### `get_search_terms`

Get search terms report showing actual user queries that triggered your ads. Window: date_range_start/date_range_end, defaulting to the last 30 days. Rows: limit, 1 to 10000, defaulting to the top 200 by clicks.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_end": {
      "description": "End date YYYY-MM-DD.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_start": {
      "description": "Start date YYYY-MM-DD. Both dates must be given, or the default\n30-day window applies.",
      "type": [
        "string",
        "null"
      ]
    },
    "limit": {
      "description": "Rows to return, ordered by clicks descending. 1 to 10000, default 200.",
      "format": "uint32",
      "minimum": 0,
      "type": [
        "integer",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L894)

<a id="tool-list-negative-keyword-lists"></a>

### `list_negative_keyword_lists`

List the account's negative keyword lists (shared sets), each with its member count and the campaigns it is attached to. A list with zero attached campaigns excludes nothing.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L928)

<a id="tool-remove-from-negative-keyword-list"></a>

### `remove_from_negative_keyword_list`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Remove keywords from a negative keyword list by criterion ID (IRREVERSIBLE). Every campaign using the list loses these exclusions.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "criterion_ids": {
      "description": "Criterion IDs to remove, as returned by get_negative_keyword_list.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "shared_set_id": {
      "description": "Numeric ID of the negative keyword list (shared set).",
      "type": "string"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1327)

<a id="tool-remove-keywords"></a>

### `remove_keywords`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft REMOVING keywords from an ad group by criterion IDs (IRREVERSIBLE).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID containing the keywords.",
      "type": "string"
    },
    "criterion_ids": {
      "description": "Criterion IDs to remove.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "ad_group_id",
    "criterion_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1656)

<a id="tool-remove-negative-keywords"></a>

### `remove_negative_keywords`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft REMOVING negative keywords from a campaign by criterion IDs (IRREVERSIBLE).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "The campaign ID containing the negative keywords.",
      "type": "string"
    },
    "criterion_ids": {
      "description": "Criterion IDs to remove.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "campaign_id",
    "criterion_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1680)

<a id="tool-update-keyword-bid"></a>

### `update_keyword_bid`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Update a keyword's CPC bid. Checks bid increase safety limit. Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID containing the keyword.",
      "type": "string"
    },
    "criterion_id": {
      "description": "Criterion ID of the keyword.",
      "type": "string"
    },
    "current_bid": {
      "description": "Current bid in dollars (for safety check).",
      "format": "double",
      "type": "number"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "new_bid": {
      "description": "New bid in dollars.",
      "format": "double",
      "type": "number"
    }
  },
  "required": [
    "ad_group_id",
    "criterion_id",
    "current_bid",
    "new_bid"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1862)

<a id="tool-update-keyword-final-url"></a>

### `update_keyword_final_url`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Update an existing keyword's landing page (ad_group_criterion.final_urls) in place via an update with field mask — preserves quality score history, unlike remove + re-create. Use to route a keyword to a page whose title matches its vocabulary. Returns a preview; call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID containing the keyword.",
      "type": "string"
    },
    "criterion_id": {
      "description": "Criterion ID of the keyword.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "final_url": {
      "description": "New landing page for clicks on this keyword. Absolute http(s) URL,\nbounded to 2048 characters. Sets `ad_group_criterion.final_urls`.",
      "type": "string"
    }
  },
  "required": [
    "ad_group_id",
    "criterion_id",
    "final_url"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1888)

## Campaigns, budgets, bidding, and targeting

<a id="tool-create-ad-group"></a>

### `create_ad_group`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft a new ad group in an existing campaign. Defaults to PAUSED — pass status='ENABLED' to start serving immediately. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "AdStatus": {
      "description": "Lifecycle status for an ad, ad group, campaign, or asset group.\n\nSerialized as `\"ENABLED\"`, `\"PAUSED\"`, or `\"REMOVED\"` to match the\nGoogle Ads API enum strings.\n\nDefault is [`AdStatus::Paused`] — newly drafted entities ship paused\nso an agent can review before traffic flows. Pass `status: \"ENABLED\"`\nexplicitly to opt out of this safety default.",
      "enum": [
        "ENABLED",
        "PAUSED",
        "REMOVED"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_name": {
      "description": "Name for the new ad group.",
      "type": "string"
    },
    "campaign_id": {
      "description": "Campaign ID to create the ad group in.",
      "type": "string"
    },
    "cpc_bid_micros": {
      "description": "Optional CPC bid in micros (1 dollar = 1_000_000 micros).",
      "format": "int64",
      "type": [
        "integer",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "status": {
      "anyOf": [
        {
          "$ref": "#/$defs/AdStatus"
        },
        {
          "type": "null"
        }
      ],
      "description": "Lifecycle status. Defaults to `PAUSED` for safety (was `ENABLED` in\nv0.2.x — corrected for consistency with the other write tools)."
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1014)

<a id="tool-create-pmax-campaign"></a>

### `create_pmax_campaign`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Create a Performance Max campaign with text assets. Image assets require separate upload. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "bidding_strategy": {
      "description": "Bidding strategy (e.g. MAXIMIZE_CONVERSIONS, MAXIMIZE_CONVERSION_VALUE).",
      "type": "string"
    },
    "business_name": {
      "description": "Business name (max 25 chars).",
      "type": "string"
    },
    "campaign_name": {
      "description": "Campaign name.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "daily_budget": {
      "description": "Daily budget in dollars.",
      "format": "double",
      "type": "number"
    },
    "descriptions": {
      "description": "Descriptions (2-5, max 90 chars each).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "final_urls": {
      "description": "Final URLs for the asset group.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "geo_target_ids": {
      "description": "Geographic target IDs.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "headlines": {
      "description": "Headlines (3-15, max 30 chars each).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "long_headlines": {
      "description": "Long headlines (1-5, max 90 chars each).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "start_paused": {
      "description": "If true, campaign starts PAUSED (default true).",
      "type": [
        "boolean",
        "null"
      ]
    }
  },
  "required": [
    "campaign_name",
    "daily_budget",
    "bidding_strategy",
    "final_urls",
    "headlines",
    "long_headlines",
    "descriptions",
    "business_name",
    "geo_target_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1774)

<a id="tool-create-portfolio-bidding-strategy"></a>

### `create_portfolio_bidding_strategy`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Create a portfolio bidding strategy (TARGET_CPA, TARGET_ROAS, TARGET_IMPRESSION_SHARE). Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "name": {
      "description": "Strategy name.",
      "type": "string"
    },
    "strategy_type": {
      "description": "Strategy type: TARGET_CPA, TARGET_ROAS, or TARGET_IMPRESSION_SHARE.",
      "type": "string"
    },
    "target_cpa": {
      "description": "Target CPA in dollars (required for TARGET_CPA).",
      "format": "double",
      "type": [
        "number",
        "null"
      ]
    },
    "target_roas": {
      "description": "Target ROAS (required for TARGET_ROAS).",
      "format": "double",
      "type": [
        "number",
        "null"
      ]
    }
  },
  "required": [
    "name",
    "strategy_type"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1836)

<a id="tool-draft-campaign"></a>

### `draft_campaign`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft a new campaign (PAUSED) with budget, ad group, and optional keywords. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "AdStatus": {
      "description": "Lifecycle status for an ad, ad group, campaign, or asset group.\n\nSerialized as `\"ENABLED\"`, `\"PAUSED\"`, or `\"REMOVED\"` to match the\nGoogle Ads API enum strings.\n\nDefault is [`AdStatus::Paused`] — newly drafted entities ship paused\nso an agent can review before traffic flows. Pass `status: \"ENABLED\"`\nexplicitly to opt out of this safety default.",
      "enum": [
        "ENABLED",
        "PAUSED",
        "REMOVED"
      ],
      "type": "string"
    },
    "KeywordInput": {
      "description": "Input for a keyword to add during campaign drafting.",
      "properties": {
        "final_url": {
          "description": "Optional keyword-level final URL override. When set, clicks on this\nkeyword route to this landing page (`ad_group_criterion.final_urls`)\ninstead of inheriting the ad's final URL. Must be an absolute http(s)\nURL. Omit to inherit the ad's final URL.",
          "type": [
            "string",
            "null"
          ]
        },
        "match_type": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "text",
        "match_type"
      ],
      "type": "object"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_name": {
      "description": "Name for the default ad group.",
      "type": [
        "string",
        "null"
      ]
    },
    "bidding_strategy": {
      "description": "Bidding strategy (e.g. MAXIMIZE_CONVERSIONS, TARGET_CPA, MANUAL_CPC).",
      "type": "string"
    },
    "campaign_name": {
      "description": "Name for the new campaign.",
      "type": "string"
    },
    "channel_type": {
      "description": "Channel type (default \"SEARCH\").",
      "type": [
        "string",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "daily_budget": {
      "description": "Daily budget in dollars (e.g. 50.0).",
      "format": "double",
      "type": "number"
    },
    "geo_target_ids": {
      "description": "Geographic target IDs for campaign targeting.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "keywords": {
      "description": "Optional keywords to add to the ad group.",
      "items": {
        "$ref": "#/$defs/KeywordInput"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "language_ids": {
      "description": "Language IDs for campaign targeting.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "status": {
      "anyOf": [
        {
          "$ref": "#/$defs/AdStatus"
        },
        {
          "type": "null"
        }
      ],
      "description": "Lifecycle status for the new campaign + ad group. Defaults to `PAUSED`\nfor safety; pass `ENABLED` to start serving immediately."
    },
    "target_cpa": {
      "description": "Target CPA in dollars, if using TARGET_CPA or MAXIMIZE_CONVERSIONS.",
      "format": "double",
      "type": [
        "number",
        "null"
      ]
    },
    "target_roas": {
      "description": "Target ROAS, if using TARGET_ROAS or MAXIMIZE_CONVERSION_VALUE.",
      "format": "double",
      "type": [
        "number",
        "null"
      ]
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1066)

<a id="tool-enable-entity"></a>

### `enable_entity`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft enabling a paused campaign, ad group, ad, or keyword.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "entity_id": {
      "description": "The entity ID.",
      "type": "string"
    },
    "entity_type": {
      "description": "Entity type: campaign, ad_group, ad, or keyword.",
      "type": "string"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1724)

<a id="tool-exclude-demographics"></a>

### `exclude_demographics`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Exclude demographic tiers (household income band, age bracket, gender) from ad groups. Writes one NEGATIVE ad_group_criterion per ad group × tier — excluded users never see the ad, which is absolute, not a bid adjustment. Demographic criteria are ad-group scoped: there is no campaign-level equivalent, so pass every ad group the exclusion should cover. Common clinic cut: income_ranges=["INCOME_RANGE_0_50","INCOME_RANGE_UNDETERMINED"]. If a tier already exists as a POSITIVE row on the ad group the create collides on the shared resource name — clear it first with remove_demographic_criterion. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "AgeRange": {
      "description": "Age bracket, as used by `AdGroupCriterion.age_range`.\n\nExplicit renames for the same reason as [`IncomeRange`] — serde would derive\n`AGE_RANGE18_24` without them.",
      "oneOf": [
        {
          "enum": [
            "AGE_RANGE_18_24",
            "AGE_RANGE_25_34",
            "AGE_RANGE_35_44",
            "AGE_RANGE_45_54",
            "AGE_RANGE_55_64",
            "AGE_RANGE_65_UP"
          ],
          "type": "string"
        },
        {
          "const": "AGE_RANGE_UNDETERMINED",
          "description": "\"Unknown\" — age could not be determined for the user.",
          "type": "string"
        }
      ]
    },
    "Gender": {
      "description": "Gender, as used by `AdGroupCriterion.gender`.\n\nNote the JSON surface is prefixed (`GENDER_MALE`) but the API wire value is\nnot (`MALE`) — see [`Gender::as_api_str`].",
      "oneOf": [
        {
          "enum": [
            "GENDER_MALE",
            "GENDER_FEMALE"
          ],
          "type": "string"
        },
        {
          "const": "GENDER_UNDETERMINED",
          "description": "\"Unknown\" — gender could not be determined for the user.",
          "type": "string"
        }
      ]
    },
    "IncomeRange": {
      "description": "Household income percentile band, as used by `AdGroupCriterion.income_range`.\n\nBands are expressed as percentile of household income **within the targeted\ncountry**, top-down: `INCOME_RANGE_90_UP` is the top 10% of earners,\n`INCOME_RANGE_0_50` the lower 50%. `INCOME_RANGE_UNDETERMINED` is the\n\"Unknown\" bucket — users Google could not place in a band, which in small\nor rural markets is frequently the largest single bucket.\n\nEvery variant carries an explicit `#[serde(rename)]`. Do not replace them\nwith `rename_all = \"SCREAMING_SNAKE_CASE\"`: serde does not insert a separator\nbefore a digit, so `IncomeRange0_50` would derive to `INCOME_RANGE0_50` and\nevery income mutate would be rejected.",
      "oneOf": [
        {
          "const": "INCOME_RANGE_0_50",
          "description": "Lower 50% of household income.",
          "type": "string"
        },
        {
          "const": "INCOME_RANGE_50_60",
          "description": "41-50% band.",
          "type": "string"
        },
        {
          "const": "INCOME_RANGE_60_70",
          "description": "31-40% band.",
          "type": "string"
        },
        {
          "const": "INCOME_RANGE_70_80",
          "description": "21-30% band.",
          "type": "string"
        },
        {
          "const": "INCOME_RANGE_80_90",
          "description": "11-20% band.",
          "type": "string"
        },
        {
          "const": "INCOME_RANGE_90_UP",
          "description": "Top 10% of household income.",
          "type": "string"
        },
        {
          "const": "INCOME_RANGE_UNDETERMINED",
          "description": "\"Unknown\" — income band could not be determined for the user.",
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_ids": {
      "description": "Ad group IDs to exclude the tiers from. Demographic criteria are\nad-group scoped — there is no campaign-level equivalent — so list every\nad group the exclusion should cover. Find them with\n`run_gaql(\"SELECT ad_group.id FROM ad_group WHERE campaign.id = ...\")`.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "age_ranges": {
      "description": "Age brackets to exclude, e.g. `[\"AGE_RANGE_18_24\", \"AGE_RANGE_65_UP\"]`.",
      "items": {
        "$ref": "#/$defs/AgeRange"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "genders": {
      "description": "Genders to exclude, e.g. `[\"GENDER_MALE\"]`. At most two of the three.",
      "items": {
        "$ref": "#/$defs/Gender"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "income_ranges": {
      "description": "Household income bands to exclude, e.g.\n`[\"INCOME_RANGE_0_50\", \"INCOME_RANGE_UNDETERMINED\"]` for the common\n\"lower 50% + unknown\" cut. Bands are percentiles: `INCOME_RANGE_90_UP`\nis the top 10%. Note `INCOME_RANGE_UNDETERMINED` (\"Unknown\") is often the\nlargest bucket in small or rural markets — excluding it can cut a lot of\nvolume, so check the distribution first on a small budget.",
      "items": {
        "$ref": "#/$defs/IncomeRange"
      },
      "type": [
        "array",
        "null"
      ]
    }
  },
  "required": [
    "ad_group_ids"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1497)

<a id="tool-exclude-geo-target"></a>

### `exclude_geo_target`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Exclude a geographic location from a campaign (negative location criterion — the inverse of update_campaign's positive geo targeting). Ads stop serving in that location. geo_target_id accepts a bare numeric ID or geoTargetConstants/{id}; find IDs via search_geo_targets. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to exclude the location from.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "geo_target_id": {
      "description": "Geo target constant ID to exclude — bare numeric (\"2276\") or full\nresource name (\"geoTargetConstants/2276\"). Find IDs via search_geo_targets.",
      "type": "string"
    }
  },
  "required": [
    "campaign_id",
    "geo_target_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1422)

<a id="tool-get-demographics"></a>

### `get_demographics`

List the demographic criteria (income band, age bracket, gender) currently on the account's ad groups, positive and negative alike — the `negative` flag distinguishes them. Use it to verify an exclusion landed, or to find a positive row blocking one. Ad groups with no rows do not appear: absence means the ad group serves to everyone, which is the API default and not a misconfiguration.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "Optional campaign ID to scope the read to a single campaign.",
      "type": [
        "string",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1547)

<a id="tool-get-geo-performance"></a>

### `get_geo_performance`

Get geographic performance data showing metrics broken down by location.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_end": {
      "description": "End date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    },
    "date_range_start": {
      "description": "Start date YYYY-MM-DD",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L999)

<a id="tool-pause-entity"></a>

### `pause_entity`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft pausing a campaign, ad group, ad, or keyword.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "entity_id": {
      "description": "The entity ID.",
      "type": "string"
    },
    "entity_type": {
      "description": "Entity type: campaign, ad_group, ad, or keyword.",
      "type": "string"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1702)

<a id="tool-remove-demographic-criterion"></a>

### `remove_demographic_criterion`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Remove a demographic criterion from an ad group. Two uses: undoing an exclusion, and clearing a positive row that blocks exclude_demographics. Destructive — removing a negative row re-opens the ad group to that tier — so requires confirmed_twice. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID holding the criterion.",
      "type": "string"
    },
    "criterion_id": {
      "description": "Fixed criterion ID of the tier — read it from `get_demographics`.\nIncome: 510000 Unknown, 510001 lower 50%, 510002-510006 upward.\nAge: 503001-503006 by bracket, 503999 Unknown.\nGender: 10 male, 11 female, 20 unknown.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "ad_group_id",
    "criterion_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1523)

<a id="tool-remove-entity"></a>

### `remove_entity`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft REMOVING an entity (IRREVERSIBLE). Use pause_entity instead if temporary.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "entity_id": {
      "description": "The entity ID.",
      "type": "string"
    },
    "entity_type": {
      "description": "Entity type: campaign, ad_group, ad, or keyword.",
      "type": "string"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1748)

<a id="tool-remove-geo-target"></a>

### `remove_geo_target`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Remove a positively-targeted geographic location from a campaign (stop serving in a location that is currently an included target — e.g. trimming one country out of a multi-country campaign). Use this rather than exclude_geo_target when the location is already targeted: a negative criterion would collide with the existing positive one. Destructive — requires confirmed_twice. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to remove the location target from.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "geo_target_id": {
      "description": "Geo target constant ID currently targeted — bare numeric (\"2276\") or full\nresource name (\"geoTargetConstants/2276\").",
      "type": "string"
    }
  },
  "required": [
    "campaign_id",
    "geo_target_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1446)

<a id="tool-search-geo-targets"></a>

### `search_geo_targets`

Search for geographic target constants by name. Useful for finding location IDs for geo-targeting.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "query": {
      "description": "Location name to search for (e.g. 'Paris', 'France', 'New York')",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L987)

<a id="tool-set-campaign-geo-target-type"></a>

### `set_campaign_geo_target_type`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Set a campaign's geo target type. positive_geo_target_type=PRESENCE restricts serving to people physically in (or regularly in) the targeted locations; PRESENCE_OR_INTEREST (the API default) also serves people who show interest in them. Optionally also set negative_geo_target_type. At least one must be provided. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "GeoTargetType": {
      "description": "Geo target type for a campaign's `geo_target_type_setting`.\n\nSerialized as `\"PRESENCE_OR_INTEREST\"` or `\"PRESENCE\"` to match the\nGoogle Ads API enum values. Applies to both the positive and the negative\ngeo target type fields.\n\n- `PRESENCE_OR_INTEREST` (the API default): ads can serve to people who are\n  in, regularly in, OR who show interest in the targeted locations.\n- `PRESENCE`: ads serve only to people who are physically in (or regularly\n  in) the targeted locations — \"Presence: People in or regularly in your\n  targeted locations\" in the Google Ads UI. The tighter setting most\n  advertisers want to avoid paying for out-of-area interest traffic.",
      "oneOf": [
        {
          "const": "PRESENCE_OR_INTEREST",
          "description": "People in, regularly in, or interested in the targeted locations.",
          "type": "string"
        },
        {
          "const": "PRESENCE",
          "description": "Only people physically in (or regularly in) the targeted locations.",
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "The campaign ID whose geo target type setting to change.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "negative_geo_target_type": {
      "anyOf": [
        {
          "$ref": "#/$defs/GeoTargetType"
        },
        {
          "type": "null"
        }
      ],
      "description": "Negative geo target type. `PRESENCE` or `PRESENCE_OR_INTEREST`."
    },
    "positive_geo_target_type": {
      "anyOf": [
        {
          "$ref": "#/$defs/GeoTargetType"
        },
        {
          "type": "null"
        }
      ],
      "description": "Positive geo target type. `PRESENCE` serves only to people physically\nin (or regularly in) the targeted locations; `PRESENCE_OR_INTEREST`\n(the API default) also serves people who show interest in them."
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1470)

<a id="tool-set-campaign-schedule"></a>

### `set_campaign_schedule`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Set ad schedule for a campaign (day-of-week + time windows). Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "ScheduleEntry": {
      "description": "A schedule entry for ad scheduling.",
      "properties": {
        "day_of_week": {
          "type": "string"
        },
        "end_hour": {
          "format": "uint32",
          "minimum": 0,
          "type": "integer"
        },
        "end_minute": {
          "format": "uint32",
          "minimum": 0,
          "type": "integer"
        },
        "start_hour": {
          "format": "uint32",
          "minimum": 0,
          "type": "integer"
        },
        "start_minute": {
          "format": "uint32",
          "minimum": 0,
          "type": "integer"
        }
      },
      "required": [
        "day_of_week",
        "start_hour",
        "start_minute",
        "end_hour",
        "end_minute"
      ],
      "type": "object"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "Campaign ID to set schedule for.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "schedules": {
      "description": "Schedule entries (day, start/end times).",
      "items": {
        "$ref": "#/$defs/ScheduleEntry"
      },
      "type": "array"
    }
  },
  "required": [
    "campaign_id",
    "schedules"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2014)

<a id="tool-update-ad-group"></a>

### `update_ad_group`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft ad group updates (name, CPC bid, ad rotation mode). ad_rotation_mode=ROTATE_FOREVER is 'Rotate indefinitely' in the UI. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "AdRotationMode": {
      "description": "Ad rotation mode for an ad group.\n\nSerialized as `\"OPTIMIZE\"` or `\"ROTATE_FOREVER\"` to match the\nGoogle Ads API enum values. There is no default: rotation mode is\nonly written when explicitly requested.",
      "oneOf": [
        {
          "const": "OPTIMIZE",
          "description": "Google optimizes serving toward the best-performing ad.",
          "type": "string"
        },
        {
          "const": "ROTATE_FOREVER",
          "description": "Ads rotate evenly without end (\"Rotate indefinitely\" in the UI).",
          "type": "string"
        }
      ]
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID to update.",
      "type": "string"
    },
    "ad_rotation_mode": {
      "anyOf": [
        {
          "$ref": "#/$defs/AdRotationMode"
        },
        {
          "type": "null"
        }
      ],
      "description": "Ad rotation mode: OPTIMIZE (serve best-performing ad) or\nROTATE_FOREVER (\"Rotate indefinitely\" in the Google Ads UI)."
    },
    "cpc_bid_micros": {
      "description": "New CPC bid in micros.",
      "format": "int64",
      "type": [
        "integer",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "name": {
      "description": "New name for the ad group.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "ad_group_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1039)

<a id="tool-update-campaign"></a>

### `update_campaign`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft campaign updates (budget, bidding, targeting). Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "bidding_strategy": {
      "description": "New bidding strategy (e.g. MAXIMIZE_CONVERSIONS, TARGET_CPA, MANUAL_CPC).",
      "type": [
        "string",
        "null"
      ]
    },
    "campaign_id": {
      "description": "The campaign ID to update.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "daily_budget": {
      "description": "New daily budget in dollars.",
      "format": "double",
      "type": [
        "number",
        "null"
      ]
    },
    "geo_target_ids": {
      "description": "Geographic target IDs to add.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "language_ids": {
      "description": "Language IDs to add.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "target_cpa": {
      "description": "Target CPA in dollars.",
      "format": "double",
      "type": [
        "number",
        "null"
      ]
    },
    "target_roas": {
      "description": "Target ROAS.",
      "format": "double",
      "type": [
        "number",
        "null"
      ]
    }
  },
  "required": [
    "campaign_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1106)

## Ads and creative assets

<a id="tool-add-asset-group-signal"></a>

### `add_asset_group_signal`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Add search themes and/or audience signals to a Performance Max asset group. Use this for PMax audiences — add_audience_targeting writes a campaign criterion, which PMax rejects. Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "asset_group_id": {
      "description": "The asset group ID to add signals to.",
      "type": "string"
    },
    "audience_ids": {
      "description": "Audience IDs referencing customers/{cid}/audiences/{id}.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "search_themes": {
      "description": "Search themes (max 80 chars each) telling PMax what queries to look for.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    }
  },
  "required": [
    "asset_group_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1987)

<a id="tool-create-callouts"></a>

### `create_callouts`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft callout extensions for a campaign.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "callouts": {
      "description": "Callout texts (max 25 chars each).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "campaign_id": {
      "description": "The campaign ID to add callouts to.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1582)

<a id="tool-create-structured-snippets"></a>

### `create_structured_snippets`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft structured snippet extensions for a campaign. The header must be one of Google's predefined types IN THE ACCOUNT'S LANGUAGE (e.g. 'Serviços', not 'Service catalog', on a Portuguese account) — accents included. An unrecognized header is not blocked; it is sent to Google, and the preview carries a header_note listing known-good values.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to add snippets to.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "header": {
      "description": "Snippet header, in the account's language (e.g. \"Serviços\" on a\npt-BR account, \"Service catalog\" on an en account). Must match one of\nGoogle's predefined headers exactly, accents included.",
      "type": "string"
    },
    "values": {
      "description": "Snippet values.",
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [
    "campaign_id",
    "header",
    "values"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1606)

<a id="tool-draft-responsive-search-ad"></a>

### `draft_responsive_search_ad`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft a Responsive Search Ad. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "AdStatus": {
      "description": "Lifecycle status for an ad, ad group, campaign, or asset group.\n\nSerialized as `\"ENABLED\"`, `\"PAUSED\"`, or `\"REMOVED\"` to match the\nGoogle Ads API enum strings.\n\nDefault is [`AdStatus::Paused`] — newly drafted entities ship paused\nso an agent can review before traffic flows. Pass `status: \"ENABLED\"`\nexplicitly to opt out of this safety default.",
      "enum": [
        "ENABLED",
        "PAUSED",
        "REMOVED"
      ],
      "type": "string"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID to create the ad in.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "descriptions": {
      "description": "Descriptions (2-4, max 90 chars each).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "final_url": {
      "description": "Final URL for the ad.",
      "type": "string"
    },
    "headlines": {
      "description": "Headlines (3-15, max 30 chars each).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "path1": {
      "description": "Display URL path 1.",
      "type": [
        "string",
        "null"
      ]
    },
    "path2": {
      "description": "Display URL path 2.",
      "type": [
        "string",
        "null"
      ]
    },
    "status": {
      "anyOf": [
        {
          "$ref": "#/$defs/AdStatus"
        },
        {
          "type": "null"
        }
      ],
      "description": "Lifecycle status for the new ad. One of `ENABLED`, `PAUSED`, `REMOVED`.\nDefaults to `PAUSED` for safety — the response will include a\n`next_action_hint` describing how to call `enable_entity` via MCP."
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1160)

<a id="tool-draft-sitelinks"></a>

### `draft_sitelinks`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Draft sitelink extensions for a campaign. Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$defs": {
    "SitelinkInput": {
      "description": "Input for a sitelink extension.",
      "properties": {
        "description1": {
          "type": "string"
        },
        "description2": {
          "type": "string"
        },
        "final_url": {
          "type": "string"
        },
        "link_text": {
          "type": "string"
        }
      },
      "required": [
        "link_text",
        "final_url",
        "description1",
        "description2"
      ],
      "type": "object"
    }
  },
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to add sitelinks to.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "sitelinks": {
      "description": "Sitelink definitions.",
      "items": {
        "$ref": "#/$defs/SitelinkInput"
      },
      "type": "array"
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

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1560)

<a id="tool-link-asset-to-asset-group"></a>

### `link_asset_to_asset_group`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Link an uploaded asset to a Performance Max asset group. Required for images to serve — upload_image_asset alone leaves the asset unattached. Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "asset_group_id": {
      "description": "The asset group ID to link the asset to.",
      "type": "string"
    },
    "asset_id": {
      "description": "The asset ID to link (from upload_image_asset / upload_text_asset).",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "field_type": {
      "description": "Field type: MARKETING_IMAGE, SQUARE_MARKETING_IMAGE, PORTRAIT_MARKETING_IMAGE,\nLOGO, LANDSCAPE_LOGO, YOUTUBE_VIDEO, HEADLINE, DESCRIPTION, LONG_HEADLINE,\nBUSINESS_NAME, CALL_TO_ACTION_SELECTION.",
      "type": "string"
    }
  },
  "required": [
    "asset_group_id",
    "asset_id",
    "field_type"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1960)

<a id="tool-update-responsive-search-ad"></a>

### `update_responsive_search_ad`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Update an existing Responsive Search Ad in place (headlines, descriptions, final URL, display paths) via an update with field mask — preserves the ad's ID and its asset performance history, unlike remove + re-create. Only the fields provided are written; omitted fields are left untouched. Returns a preview; call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "ad_id": {
      "description": "Numeric ID of the ad to edit (`ad.id`), not a resource name.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "descriptions": {
      "description": "Replacement descriptions (2-4, max 90 chars each). Omit to keep the\nad's current descriptions.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "final_url": {
      "description": "Replacement landing page. Absolute http(s) URL, max 2048 characters.",
      "type": [
        "string",
        "null"
      ]
    },
    "headlines": {
      "description": "Replacement headlines (3-15, max 30 chars each). Omit to keep the\nad's current headlines.",
      "items": {
        "type": "string"
      },
      "type": [
        "array",
        "null"
      ]
    },
    "path1": {
      "description": "Display URL path 1, max 15 characters. Empty string clears it.",
      "type": [
        "string",
        "null"
      ]
    },
    "path2": {
      "description": "Display URL path 2, max 15 characters. Empty string clears it.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "ad_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1189)

<a id="tool-upload-image-asset"></a>

### `upload_image_asset`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Upload an image asset (base64-encoded). Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "asset_name": {
      "description": "Name for the asset.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "image_data_base64": {
      "description": "Base64-encoded image data.",
      "type": "string"
    }
  },
  "required": [
    "asset_name",
    "image_data_base64"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1913)

<a id="tool-upload-text-asset"></a>

### `upload_text_asset`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Upload a reusable text asset. Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "asset_name": {
      "description": "Name for the asset.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "text_content": {
      "description": "Text content for the asset.",
      "type": "string"
    }
  },
  "required": [
    "asset_name",
    "text_content"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1935)

## Audiences and audience insights

<a id="tool-add-audience-targeting"></a>

### `add_audience_targeting`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Add audience targeting (TARGETING or OBSERVATION) to a campaign. Returns a preview.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "audience_id": {
      "description": "Audience/user list ID.",
      "type": "string"
    },
    "campaign_id": {
      "description": "Campaign ID to add targeting to.",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "targeting_mode": {
      "description": "Targeting mode: TARGETING or OBSERVATION.",
      "type": "string"
    }
  },
  "required": [
    "campaign_id",
    "audience_id",
    "targeting_mode"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L1809)

## Conversions and measurement

<a id="tool-create-conversion-action"></a>

### `create_conversion_action`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Create a conversion action for server-side click uploads (type UPLOAD_CLICKS, gclid-based offline conversion import). Use this to create a 'Signup' or 'Activation' conversion. Returns a preview — call confirm_and_apply to execute. After apply, the numeric ID (for a *_CONVERSION_ACTION_ID env var) is the trailing segment of the returned conversionAction resourceName.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "category": {
      "description": "Conversion category (default \"SIGNUP\"). E.g. SIGNUP, LEAD, DEFAULT.",
      "type": [
        "string",
        "null"
      ]
    },
    "click_through_lookback_window_days": {
      "description": "Click-through attribution window in days, 1-90 (default 30).",
      "format": "int64",
      "type": [
        "integer",
        "null"
      ]
    },
    "counting_type": {
      "description": "Counting type (default \"ONE_PER_CLICK\"). One of ONE_PER_CLICK, MANY_PER_CLICK.",
      "type": [
        "string",
        "null"
      ]
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "name": {
      "description": "Name of the conversion action (e.g. \"Activation\").",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2087)

<a id="tool-get-conversion-actions"></a>

### `get_conversion_actions`

List all conversion actions configured in the account.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2073)

<a id="tool-set-conversion-action-primary-status"></a>

### `set_conversion_action_primary_status`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Set a conversion action as primary (counts in the Conversions column and Smart Bidding) or secondary (observation only, excluded from the bidding signal). Use it to demote a value-0 signup event so it stops diluting a Maximize Conversions / Target CPA goal without losing its reporting. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "conversion_action_id": {
      "description": "The conversion action ID (numeric — the trailing segment of the\nconversionAction resource name).",
      "type": "string"
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "primary": {
      "description": "true = primary (counts in the Conversions column and Smart Bidding);\nfalse = secondary (observation only, excluded from the bidding signal).",
      "type": "boolean"
    }
  },
  "required": [
    "conversion_action_id",
    "primary"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2118)

## Experiments and recommendations

<a id="tool-apply-recommendation"></a>

### `apply_recommendation`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Apply a recommendation, optionally with type-specific apply_parameters. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "apply_parameters": {
      "description": "Type-specific `apply_parameters`, as a single-key object naming one\nvariant of the oneof — for example\n`{\"campaignBudget\": {\"newBudgetAmountMicros\": \"15000000\"}}` or\n`{\"sitelinkAsset\": {\"adAssetApplyParameters\": {\"newAssets\": [...],\n\"scope\": \"CAMPAIGN\"}}}`.\n\nOmit it to let Google apply the values it recommended. Supply it for\nthe types that cannot be applied from a bare resource name, or to\noverride what Google proposed. Valid keys: callAsset, callExtension,\ncalloutAsset, calloutExtension, campaignBudget, forecastingSetTargetCpa,\nforecastingSetTargetRoas, keyword, leadFormAsset, lowerTargetRoas,\nmoveUnusedBudget, raiseTargetCpa, raiseTargetCpaBidTooLow,\nresponsiveSearchAd, responsiveSearchAdAsset,\nresponsiveSearchAdImproveAdStrength, sitelinkAsset, sitelinkExtension,\ntargetCpaOptIn, targetRoasOptIn, textAd, useBroadMatchKeyword."
    },
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "recommendation_id": {
      "description": "Recommendation resource ID.",
      "type": "string"
    }
  },
  "required": [
    "recommendation_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2156)

<a id="tool-dismiss-recommendation"></a>

### `dismiss_recommendation`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

Dismiss a recommendation. Returns a preview — call confirm_and_apply to execute.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    },
    "recommendation_id": {
      "description": "Recommendation resource ID.",
      "type": "string"
    }
  },
  "required": [
    "recommendation_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2180)

<a id="tool-list-recommendations"></a>

### `list_recommendations`

List active (non-dismissed) recommendations for the account.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 123-456-7890). Defaults to configured customer_id.",
      "type": [
        "string",
        "null"
      ]
    }
  },
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2142)

## Previews, validation, and local helpers

<a id="tool-confirm-and-apply"></a>

### `confirm_and_apply`

Listed in read-only mode, but calling it requires `GOOGLE_ADS_READ_ONLY=false`.

**Behavior:** dry_run=true returns the stored preview without a Google Ads request. Live apply dispatches mutation or recommendation RPCs; configured dry-run and destructive-action guards must also pass.

Execute a previously previewed change. IMPORTANT: defaults to dry_run=true. Set dry_run=false to make real changes. If config.safety.require_dry_run is true, dry_run=false will be rejected unless bypass_require_dry_run=true is also set. If the mutate is rejected by Google ad policy, the error lists the offending text and policy; when those violations are exemptible (common for medical/health keywords), retry the same plan_id with exempt_policy_violations=true.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "properties": {
    "bypass_require_dry_run": {
      "description": "One-shot opt out of the `require_dry_run` safety guard for THIS apply.\nDefaults to `false`. Does NOT mutate the global config. Use this only\nwhen you explicitly know you want to apply without a prior dry-run.",
      "type": [
        "boolean",
        "null"
      ]
    },
    "confirmed_twice": {
      "description": "Acknowledgement for plans flagged `requires_double_confirm`. Without\n`confirmed_twice=true`, those plans return an error and do nothing.",
      "type": [
        "boolean",
        "null"
      ]
    },
    "dry_run": {
      "description": "If true (default), returns a preview without executing. Set to false to apply changes.",
      "type": [
        "boolean",
        "null"
      ]
    },
    "exempt_policy_violations": {
      "description": "Request a Google ad policy exemption if the mutate is rejected with\n*exemptible* violations (e.g. `HEALTH_IN_PERSONALIZED_ADS`, which nearly\nevery medical/health keyword triggers). The operations are resubmitted\nonce with `exemptPolicyViolationKeys` — the same thing the Google Ads UI\ndoes automatically. Defaults to `false`; when a mutate fails this way the\nerror lists the exact policies and offending text, and the plan is kept\nso you can retry with this flag. Only keywords can be exempted —\nresponsive search ads cannot.",
      "type": [
        "boolean",
        "null"
      ]
    },
    "plan_id": {
      "description": "The plan ID returned from a draft/preview operation.",
      "type": "string"
    }
  },
  "required": [
    "plan_id"
  ],
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L2205)

<a id="tool-health-check"></a>

### `health_check`

Check the health of the MCP Google Ads server and its configuration

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "properties": {},
  "type": "object"
}
```

</details>

[Source](https://github.com/FGRibreau/mcp-google-ads/blob/5e8d073b76bc723cfdb1978a345add69f3412a73/src/lib.rs#L776)

## Attribution

Tool descriptions and schemas are extracted from the pinned upstream source under its [license](../licenses/rust-MIT.txt). See [upstream notices](../licenses/NOTICE.txt). Catalog navigation and behavior notes were added here.
