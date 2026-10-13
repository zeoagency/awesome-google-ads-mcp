# googleads/google-ads-mcp tools

[Main list](../../README.md) · [Search every tool](../TOOLS.md) · [Upstream](https://github.com/googleads/google-ads-mcp)

**Inventory:** 3 tools. **Default tools/list:** 3. **Checked:** 2026-10-13.

**Source:** [commit 9a78cbd](https://github.com/googleads/google-ads-mcp/tree/9a78cbdceebae71a6bc8483bdec333695834ef9c). Offline in-process MCP tools/list; FastMCP 4.1.0, google-ads 33.0.0.

All 3 tools are read-only and enabled by the bundled configuration. Custom YAML can disable tools or change namespace prefixes; these are the default exported names. The server collects SearchStream results before returning them through MCP.

Descriptions and parameter JSON below preserve the registered MCP interface. Open each parameter block for required fields, defaults, enums, nested objects, and references. Prose-only restrictions and free-form objects remain as upstream declares them. No tool was invoked and no live account operation was tested.

## Tools

- [Accounts, queries, and performance (3)](#accounts-queries-and-performance)

## Accounts, queries, and performance

<a id="tool-customers-list-accessible-customers"></a>

### `customers_list_accessible_customers`

Returns ids of customers directly accessible by the user authenticating the call.

Use this tool first to discover available customer IDs if the user hasn't
provided one. Most other tools require a valid customer ID as input.

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

[Source](https://github.com/googleads/google-ads-mcp/blob/9a78cbdceebae71a6bc8483bdec333695834ef9c/ads_mcp/tools/core.py#L30)

<a id="tool-metadata-get-resource-metadata"></a>

### `metadata_get_resource_metadata`

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
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional manager customer ID to use as the login-customer-id header."
    }
  },
  "required": [
    "resource_name"
  ]
}
```

</details>

[Source](https://github.com/googleads/google-ads-mcp/blob/9a78cbdceebae71a6bc8483bdec333695834ef9c/ads_mcp/tools/get_resource_metadata.py#L25)

<a id="tool-search-search"></a>

### `search_search`

Fetches data from the Google Ads API using the search method

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "integer"
        }
      ],
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
      "default": [],
      "items": {
        "type": "string"
      },
      "type": "array",
      "description": "List of conditions to filter the data, combined using AND clauses"
    },
    "orderings": {
      "default": [],
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
          "type": "null"
        }
      ],
      "default": null,
      "description": "The maximum number of rows to return"
    },
    "login_customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional manager customer ID to use as the login-customer-id header."
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

[Source](https://github.com/googleads/google-ads-mcp/blob/9a78cbdceebae71a6bc8483bdec333695834ef9c/ads_mcp/tools/search.py#L150)

## Attribution

Tool descriptions and schemas are extracted from the pinned upstream source under its [license](../licenses/Apache-2.0.txt). See [upstream notices](../licenses/NOTICE.txt). Catalog navigation and behavior notes were added here.
