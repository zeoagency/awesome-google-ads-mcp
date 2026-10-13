# growmedevelopment/google-ads-mcp tools

[Main list](../../README.md) · [Search every tool](../TOOLS.md) · [Upstream](https://github.com/growmedevelopment/google-ads-mcp)

**Inventory:** 5 tools. **Default tools/list:** 5. **Checked:** 2026-10-13.

**Source:** [commit 515ab86](https://github.com/growmedevelopment/google-ads-mcp/tree/515ab86f6b5fd0bfe7ebe13bfaab983768bf59a4). Offline in-process MCP tools/list; FastMCP 4.1.0, google-ads 33.0.0.

All 5 tools are read-only. Keyword ideas come from KeywordPlanIdeaService; there are no campaign mutation or keyword forecast tools. Explicit v24 imports and discovery metadata coexist with SDK-default service selection (v25 in this capture).

Descriptions and parameter JSON below preserve the registered MCP interface. Open each parameter block for required fields, defaults, enums, nested objects, and references. Prose-only restrictions and free-form objects remain as upstream declares them. No tool was invoked and no live account operation was tested.

## Tools

- [Accounts, queries, and performance (4)](#accounts-queries-and-performance)
- [Keyword research and search terms (1)](#keyword-research-and-search-terms)

## Accounts, queries, and performance

<a id="tool-get-resource-metadata"></a>

### `get_resource_metadata`

Retrieves the selectable, filterable, and sortable fields for a specific Google Ads resource,
including compatible metrics and segments.

Use this tool to find out which fields you can select, filter by, or sort by
when querying a specific resource (e.g., 'campaign', 'ad_group').
This tool also returns metrics and segments that can be selected with the resource.
Their names start with 'metrics.' and 'segments.' respectively.

Do not guess fields, you MUST use this tool to discover them before constructing a query for the
`search` tool.

The responses of this tool should be cached, as they don't change frequently.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "resource_name": {
      "type": "string",
      "description": "The name of the Google Ads resource (e.g., 'campaign', 'ad_group')."
    }
  },
  "required": [
    "resource_name"
  ]
}
```

</details>

[Source](https://github.com/growmedevelopment/google-ads-mcp/blob/515ab86f6b5fd0bfe7ebe13bfaab983768bf59a4/ads_mcp/tools/get_resource_metadata.py#L23)

<a id="tool-list-accessible-customers"></a>

### `list_accessible_customers`

Returns customer IDs where the authenticating user has DIRECT access.

IMPORTANT — what this does NOT return: customers linked through a Manager
(MCC) account via the manager hierarchy. If the authenticating user is a
member of an MCC but does not have a direct user grant on each child
account, those child accounts will NOT appear here. The result count will
be much smaller than "all accounts under the MCC."

For "show me every account under our MCC" use `list_customer_clients`
instead — that one walks the manager hierarchy via the `customer_client`
resource and returns every linked account (including ones inherited
through MCC access).

Use this tool when you specifically need the list of customers the
OAuth user has direct user-level access on (e.g., to confirm the
refresh-token user is set up correctly).

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

[Source](https://github.com/growmedevelopment/google-ads-mcp/blob/515ab86f6b5fd0bfe7ebe13bfaab983768bf59a4/ads_mcp/tools/core.py#L31)

<a id="tool-list-customer-clients"></a>

### `list_customer_clients`

List every customer account linked under a Manager (MCC) account.

Use this tool — NOT `list_accessible_customers` — whenever the user asks
for "all client accounts under our MCC," "every account we manage," or
similar. It walks the manager hierarchy via the `customer_client`
resource so child accounts inherited through MCC access are included.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "manager_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "10-digit MCC ID, no dashes. If omitted, defaults\nto the GOOGLE_ADS_LOGIN_CUSTOMER_ID environment variable the\nserver was launched with (the org's primary MCC)."
    }
  }
}
```

</details>

[Source](https://github.com/growmedevelopment/google-ads-mcp/blob/515ab86f6b5fd0bfe7ebe13bfaab983768bf59a4/ads_mcp/tools/core.py#L64)

<a id="tool-search"></a>

### `search`

Fetches data from the Google Ads API using the search method

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string",
      "description": "The id of the customer"
    },
    "fields": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "The fields to fetch"
    },
    "resource": {
      "type": "string",
      "description": "The resource to return fields from"
    },
    "conditions": {
      "default": null,
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "List of conditions to filter the data, combined using AND clauses"
    },
    "orderings": {
      "default": null,
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "How the data is ordered"
    },
    "limit": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "string"
        }
      ],
      "default": null,
      "description": "The maximum number of rows to return"
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

[Source](https://github.com/growmedevelopment/google-ads-mcp/blob/515ab86f6b5fd0bfe7ebe13bfaab983768bf59a4/ads_mcp/tools/search.py#L27)

## Keyword research and search terms

<a id="tool-generate-keyword-ideas"></a>

### `generate_keyword_ideas`

Generate keyword ideas with historical metrics via KeywordPlanIdeaService.

Use this when a marketer needs search volume, competition level, and
top-of-page CPC bid ranges for a list of seed keywords — typical
use case is scoping a new client brief or expanding a keyword list
during campaign planning.

RATE LIMIT — READ BEFORE CALLING: Google allows 1 Keyword Planning
request per second per customer account (about 4 in flight at once,
then rejections). Never call this tool several
times in parallel; call it once, wait for the result, then call again.
Put up to 20 seed keywords in ONE call rather than one call per seed
(more than 20 seeds are sent as consecutive batches of 20, paced 1 s
apart, and the results are merged). The server paces calls and retries
a rate rejection for you, so a returned error means the limit was hit
persistently or the daily quota is gone — the error text says which.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "type": "string",
      "description": "10-digit Google Ads customer ID without dashes\n(e.g. \"1234567890\"). Must be a customer the OAuth user\nhas access to — typically the MCC, or any child account.\nPrefer the client's own account for research: the planning\nrate limit is per customer account, so calls against the MCC\nshare one bucket with every other tool and teammate using it."
    },
    "seed_keywords": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "list of seed terms to expand from. Example:\n[\"criminal defense lawyer Calgary\", \"DUI lawyer Calgary\"].\nUp to 20 per API request; longer lists are batched."
    },
    "geo_target_ids": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "list of geo target constant IDs (numeric strings).\nCommon values:\n  \"2840\" = United States\n  \"2124\" = Canada\n  \"2826\" = United Kingdom\n  \"2036\" = Australia\n  \"2356\" = India\nPass multiple to broaden geographic scope, e.g.\n[\"2124\", \"2840\"] for Canada + US."
    },
    "language_id": {
      "default": "1000",
      "type": "string",
      "description": "language constant ID (numeric string). Defaults to\n\"1000\" = English. Other useful values:\n  \"1003\" = Spanish\n  \"1001\" = German\n  \"1002\" = French\n  \"1019\" = Portuguese"
    },
    "network": {
      "default": "GOOGLE_SEARCH",
      "type": "string",
      "description": "which Google network to source data from. Options:\n  \"GOOGLE_SEARCH\" (default, Search only)\n  \"GOOGLE_SEARCH_AND_PARTNERS\" (includes Search Network partners)"
    },
    "page_size": {
      "default": 1000,
      "type": "integer",
      "description": "rows per PAGE, not a cap on the result (the API's\ndocumented maximum is 10,000). The tool walks every page and\nmerges them, so a broad seed set can return a lot; results are\ntruncated at 2,000 rows and a warning is logged when that fires.\nEach page is its own request, so it costs its own operation and\nits own slot against the per-second limit — a smaller page_size\nmeans MORE requests, not fewer."
    }
  },
  "required": [
    "customer_id",
    "seed_keywords",
    "geo_target_ids"
  ]
}
```

</details>

[Source](https://github.com/growmedevelopment/google-ads-mcp/blob/515ab86f6b5fd0bfe7ebe13bfaab983768bf59a4/ads_mcp/tools/keyword_planner.py#L324)

## Attribution

Tool descriptions and schemas are extracted from the pinned upstream source under its [license](../licenses/Apache-2.0.txt). See [upstream notices](../licenses/NOTICE.txt). Catalog navigation and behavior notes were added here.
