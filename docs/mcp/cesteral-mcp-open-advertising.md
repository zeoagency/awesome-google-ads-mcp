# cesteral/mcp-open-advertising tools

[Main list](../../README.md) · [Search every tool](../TOOLS.md) · [Upstream](https://github.com/cesteral/mcp-open-advertising)

**Inventory:** 24 tools. **Default tools/list:** 18. **Checked:** 2026-10-13.

**Source:** [commit 1a567c3](https://github.com/cesteral/mcp-open-advertising/tree/1a567c3baeee018ee1f6572065f17e459bfa7977). Built locked source; production factory + MCP SDK 1.31.0 tools/list over in-memory transport, without bootstrap OAuth exchange.

The Google Ads package has 18 production tools and 6 optional protocol-test tools shown in a separate section. Set `MCP_INCLUDE_CONFORMANCE_TOOLS=true` to expose the test fixtures; default clients see 18 tools. Entity CRUD supports campaign, adGroup, ad, keyword, campaignBudget, and asset. Create/update/remove and duplication dry runs use API `validateOnly`; bulk, bid, and media dry runs are symbolic previews. Bootstrap authentication is required for real use.

Descriptions and parameter JSON below preserve the registered MCP interface. Open each parameter block for required fields, defaults, enums, nested objects, and references. Prose-only restrictions and free-form objects remain as upstream declares them. No tool was invoked and no live account operation was tested.

## Tools

- [Accounts, queries, and performance (6)](#accounts-queries-and-performance)
- [Campaigns, budgets, bidding, and targeting (8)](#campaigns-budgets-bidding-and-targeting)
- [Ads and creative assets (2)](#ads-and-creative-assets)
- [Previews, validation, and local helpers (2)](#previews-validation-and-local-helpers)
- [Protocol test tools (6)](#protocol-test-tools)

## Accounts, queries, and performance

<a id="tool-gads-gaql-search"></a>

### `gads_gaql_search`

Execute a Google Ads Query Language (GAQL) query against any Google Ads resource. Supports resource fields, segment fields, and metrics with SQL-like syntax. See `gaql-reference://syntax` resource for full reference.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "query": {
      "type": "string",
      "minLength": 1,
      "description": "GAQL query string (must include SELECT and FROM clauses)"
    },
    "pageToken": {
      "type": "string",
      "description": "Page token for pagination (from previous response). This tool pages across result sets via pageToken; offset is not supported."
    },
    "mode": {
      "type": "string",
      "enum": [
        "summary",
        "rows"
      ],
      "default": "summary",
      "description": "Return mode. summary returns counts, columns, and previewRows. rows returns a bounded page of rows. Default: summary"
    },
    "columns": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "description": "Optional list of columns to include in returned row payloads"
    },
    "maxRows": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10000,
      "description": "Maximum rows to return before the server cap is applied (default: 10 for summary, 50 for rows; hard cap: 200)"
    },
    "aggregateBy": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "description": "Group rows by these column values before pagination. Non-grouping columns are aggregated per group. totalRows reflects the post-aggregation row count."
    },
    "aggregateMetrics": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "enum": [
          "sum",
          "avg",
          "count",
          "min",
          "max"
        ]
      },
      "description": "Aggregation function per non-grouping column (sum/avg/count/min/max). Columns not listed default to sum. Non-numeric values are treated as 0 with a warning."
    }
  },
  "required": [
    "customerId",
    "query"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/gaql-search.tool.ts#L17)

<a id="tool-gads-get-ad-preview"></a>

### `gads_get_ad_preview`

**Behavior:** Returns ad type, final URLs, and resource name. It does not render an ad or generate a shareable preview URL.

Get preview information for a Google Ads ad.

Fetches the ad entity via GAQL and returns its type, resource name, and final URLs.
This is entity data, not a rendered preview: the Google Ads API has no ad-render endpoint.
Its only preview method, customers:generateShareablePreviews, returns shareable preview URLs
for asset groups (UI preview) or ad group ads (YouTube live preview) and is not called here.

**Usage:** Use adId from gads_list_entities with entityType=ad or gads_create_entity.
The adId is the numeric ID, not the resource name.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "adId": {
      "type": "string",
      "minLength": 1,
      "description": "Google Ads Ad ID"
    }
  },
  "required": [
    "customerId",
    "adId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/get-ad-preview.tool.ts#L11)

<a id="tool-gads-get-entity"></a>

### `gads_get_entity`

Get a single Google Ads entity by type and ID using a GAQL query.

**Supported entity types:** campaign, adGroup, ad, keyword, campaignBudget, asset

Returns all default fields for the entity type. Use `gads_gaql_search` for custom field selection.

**Note on entity IDs:** For `ad` entities, use the ad's simple ID. For `keyword` entities, use the criterion ID. GAQL queries filter by the simple ID field, so composite IDs are not needed for reads.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entity to retrieve"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "entityId": {
      "type": "string",
      "minLength": 1,
      "description": "The entity ID to retrieve"
    }
  },
  "required": [
    "entityType",
    "customerId",
    "entityId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/get-entity.tool.ts#L12)

<a id="tool-gads-get-insights"></a>

### `gads_get_insights`

Get performance insights for Google Ads entities using preset parameters.

Convenience wrapper around GAQL that constructs queries from simple inputs. For ad-hoc queries, use `gads_gaql_search` directly.

**Supported entity types:** campaign, adGroup, ad, keyword

**Default metrics:** impressions, clicks, cost_micros, conversions, ctr, average_cpc

**Date ranges:** Preset (TODAY, YESTERDAY, LAST_7_DAYS, etc.) OR custom (startDate + endDate)

**Computed metrics:** Set includeComputedMetrics=true for derived CPA, ROAS, CPM

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword"
      ],
      "description": "Type of entity to get insights for"
    },
    "entityId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Filter to a specific entity ID"
    },
    "dateRange": {
      "type": "string",
      "enum": [
        "TODAY",
        "YESTERDAY",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "THIS_MONTH",
        "LAST_MONTH",
        "LAST_90_DAYS"
      ],
      "description": "Preset date range for metrics (use this OR startDate+endDate)"
    },
    "startDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Custom start date (YYYY-MM-DD) — requires endDate"
    },
    "endDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Custom end date (YYYY-MM-DD) — requires startDate"
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^(metrics\\.)?[a-z_][a-z0-9_]*$"
      },
      "description": "Metrics to include (defaults to impressions, clicks, cost_micros, conversions, ctr, average_cpc)"
    },
    "includeComputedMetrics": {
      "type": "boolean",
      "default": false,
      "description": "Include computed CPA, ROAS, CPM derived from raw metrics"
    },
    "mode": {
      "type": "string",
      "enum": [
        "summary",
        "rows"
      ],
      "default": "summary",
      "description": "Return mode. summary returns counts, columns, and previewRows. rows returns a bounded page of rows. Default: summary"
    },
    "columns": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "description": "Optional list of columns to include in returned row payloads"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Zero-based row offset for previewRows or rows pagination (default: 0)"
    },
    "maxRows": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10000,
      "description": "Maximum rows to return before the server cap is applied (default: 10 for summary, 50 for rows; hard cap: 200)"
    },
    "aggregateBy": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "description": "Group rows by these column values before pagination. Non-grouping columns are aggregated per group. totalRows reflects the post-aggregation row count."
    },
    "aggregateMetrics": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "enum": [
          "sum",
          "avg",
          "count",
          "min",
          "max"
        ]
      },
      "description": "Aggregation function per non-grouping column (sum/avg/count/min/max). Columns not listed default to sum. Non-numeric values are treated as 0 with a warning."
    }
  },
  "required": [
    "customerId",
    "entityType"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/get-insights.tool.ts#L20)

<a id="tool-gads-list-accounts"></a>

### `gads_list_accounts`

List all Google Ads customer accounts accessible to the authenticated user.

Returns resource names in the format `customers/{customerId}`. Use the customer IDs from this list for all other Google Ads tools.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {},
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/list-accounts.tool.ts#L10)

<a id="tool-gads-list-entities"></a>

### `gads_list_entities`

List Google Ads entities of a given type with optional GAQL filters. Filters are applied as GAQL WHERE conditions. For complex queries, use `gads_gaql_search` directly.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entity to list"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "filters": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      },
      "description": "GAQL filter conditions as field:value pairs (e.g., { 'campaign.status': '= \\'ENABLED\\'' })"
    },
    "pageSize": {
      "type": "number",
      "minimum": 1,
      "maximum": 10000,
      "default": 100,
      "description": "Number of results per page (default 100)"
    },
    "pageToken": {
      "type": "string",
      "description": "Page token for pagination"
    },
    "orderBy": {
      "type": "string",
      "description": "GAQL ORDER BY clause (e.g., 'campaign.name ASC')"
    }
  },
  "required": [
    "entityType",
    "customerId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/list-entities.tool.ts#L17)

## Campaigns, budgets, bidding, and targeting

<a id="tool-gads-adjust-bids"></a>

### `gads_adjust_bids`

Batch adjust ad group bids with safe read-modify-write pattern.

For each ad group, the tool:

1. Reads the current ad group to capture previous bid values
2. Applies the new CPC and/or CPM bid amounts
3. Writes the update via the :mutate endpoint with a targeted updateMask

Returns both previous and new values for audit trail.

**Bid amounts are in micros** (1,000,000 = $1.00 USD). For example:

- $1.50 CPC = "1500000"
- $5.00 CPM = "5000000"

Up to 50 ad groups can be adjusted in a single call.

**Note:** Uses a read-modify-write pattern. Concurrent bid adjustments to the same ad group may cause one update to overwrite the other. Avoid adjusting the same ad group in parallel.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "adjustments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "adGroupId": {
            "type": "string",
            "minLength": 1,
            "description": "Ad group ID"
          },
          "cpcBidMicros": {
            "type": "string",
            "description": "New CPC bid in micros (1,000,000 = $1.00)"
          },
          "cpmBidMicros": {
            "type": "string",
            "description": "New CPM bid in micros (1,000,000 = $1.00)"
          }
        },
        "required": [
          "adGroupId"
        ],
        "additionalProperties": false
      },
      "minItems": 1,
      "maxItems": 50,
      "description": "Array of bid adjustments (max 50)"
    },
    "reason": {
      "type": "string",
      "description": "Optional reason for the bid adjustment (for audit trail)"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, validates the bid adjustments and returns an EffectDryRunResult under `dryRun` (expected effect = the would-be bid-adjustment batch) without calling the Google Ads API or prompting for confirmation. No bids are changed."
    }
  },
  "required": [
    "customerId",
    "adjustments"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/adjust-bids.tool.ts#L26)

<a id="tool-gads-bulk-create-entities"></a>

### `gads_bulk_create_entities`

Batch create multiple entities of the same type in a single API call.

**Supported entity types:** campaign, adGroup, ad, keyword, campaignBudget, asset

Simpler alternative to `gads_bulk_mutate` when you only need to create entities.
Each item in `items` is the entity data object (same format as `gads_create_entity`).

- Max 50 items per call.
- Uses `partialFailure: true` so individual items can fail without aborting the batch.
- Returns per-item success/failure results.

**Important**: For campaigns, create campaignBudgets first and reference them via the `campaignBudget` field.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entities to create"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {}
      },
      "minItems": 1,
      "maxItems": 50,
      "description": "Array of entity data objects to create (max 50). Each object has the same shape as gads_create_entity data."
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, symbolically validates the batch and returns an EffectDryRunResult under `dryRun` (expected effect = the would-be bulk create) without calling the Google Ads API. No entities are created."
    }
  },
  "required": [
    "entityType",
    "customerId",
    "items"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/bulk-create-entities.tool.ts#L28)

<a id="tool-gads-bulk-mutate"></a>

### `gads_bulk_mutate`

Execute multiple create/update/remove operations in a single API call.

**Supported entity types:** campaign, adGroup, ad, keyword, campaignBudget, asset

All operations must target the same entity type and customer. By default, all operations
succeed or all fail atomically. Set `partialFailure: true` to allow partial success.

Each operation object must contain exactly one of:

- `{ create: { ...fields } }` — create a new entity
- `{ update: { ...fields, resourceName: "customers/{id}/{type}/{entityId}" }, updateMask: "field1,field2" }` — update
- `{ remove: "customers/{id}/{type}/{entityId}" }` — remove

Maximum: thousands of operations per call (subject to Google Ads API limits).

**Composite resource names required for:** `ad` → use `customers/{id}/adGroupAds/{adGroupId}~{adId}`, `keyword` → use `customers/{id}/adGroupCriteria/{adGroupId}~{criterionId}`.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entities to mutate"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "operations": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": {}
      },
      "minItems": 1,
      "maxItems": 5000,
      "description": "Array of mutate operation objects (create/update/remove)"
    },
    "partialFailure": {
      "type": "boolean",
      "default": false,
      "description": "Allow partial success (default: false = atomic)"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, symbolically validates the batch and returns an EffectDryRunResult under `dryRun` (expected effect = the would-be bulk mutation) without calling the Google Ads API. No entities are mutated."
    }
  },
  "required": [
    "entityType",
    "customerId",
    "operations"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/bulk-mutate.tool.ts#L26)

<a id="tool-gads-bulk-update-status"></a>

### `gads_bulk_update_status`

Batch update the status for multiple Google Ads entities of the same type.

**Supported entity types:** campaign, adGroup, ad, keyword

**Available statuses:**

- `ENABLED` — active and eligible for delivery
- `PAUSED` — temporarily stopped (can be re-enabled)
- `REMOVED` — permanently removed (cannot be un-removed)

Use this tool for batch pause/resume operations across campaigns, ad groups, or ads.

**Composite entityId required for:** `ad` → use `{adGroupId}~{adId}`, `keyword` → use `{adGroupId}~{criterionId}`. Other entity types use simple IDs.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword"
      ],
      "description": "Type of entities to update (only types with a status field)"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "entityIds": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "minItems": 1,
      "maxItems": 100,
      "description": "Array of entity IDs to update (max 100)"
    },
    "status": {
      "type": "string",
      "enum": [
        "ENABLED",
        "PAUSED",
        "REMOVED"
      ],
      "description": "New entity status"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, symbolically validates the batch and returns an EffectDryRunResult under `dryRun` (expected effect = the would-be bulk status change) without prompting for confirmation or calling the Google Ads API. No statuses are changed."
    }
  },
  "required": [
    "entityType",
    "customerId",
    "entityIds",
    "status"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/bulk-update-status.tool.ts#L27)

<a id="tool-gads-create-entity"></a>

### `gads_create_entity`

Create a new Google Ads entity using the :mutate API.

**Supported entity types:** campaign, adGroup, ad, keyword, campaignBudget, asset

Provide entity data in the Google Ads REST field format (camelCase JSON) of the server's pinned API version.
Refer to `entity-schema://{entityType}` resources for field reference.

**Important**: For campaigns, create a campaignBudget first and reference it via the `campaignBudget` field.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entity to create"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "data": {
      "type": "object",
      "additionalProperties": {},
      "description": "Entity data to create (fields vary by entity type — see entity-schema resources)"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, validates the creation natively (Google Ads validateOnly) and returns a DryRunResult under `dryRun` (expected post-state = the would-be-created entity) without creating it."
    }
  },
  "required": [
    "entityType",
    "customerId",
    "data"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/create-entity.tool.ts#L25)

<a id="tool-gads-duplicate-entity"></a>

### `gads_duplicate_entity`

Duplicate a Google Ads entity (copy it).

**Supported entity types:** campaign

Creates a copy of the entity (clone via read + create — Google Ads has no native copy op).
Reads the source with GAQL, strips the server-assigned id/resourceName, and creates a new
entity via the :mutate endpoint. The copy reuses the source's shared budget. Use `options`
(e.g. `{ "name": "Copy of …" }`) to rename or re-state the copy; a `null` value removes a field.

**The copy is always created `PAUSED`**, whatever the source's status, so it cannot spend
until you enable it with `gads_update_entity` or `gads_bulk_update_status`. A `status` in
`options` is ignored.

**Bidding** is copied: the source's portfolio `biddingStrategy`, or its standard scheme with
its parameters (e.g. `targetCpa.targetCpaMicros`). A bidding scheme in `options` replaces it.
Strategy types that cannot be copied faithfully (e.g. TARGET_CPM, FIXED_CPM) are refused.

**Dates:** a source `startDateTime` that may already have passed is omitted (Google applies
its default start). A source `endDateTime` that may already have passed is refused unless
`options.endDateTime` sets a future end, or `null` to run indefinitely. Every change made
to the source's values is listed in `copyAdjustments`.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign"
      ],
      "description": "Type of entity to duplicate"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "entityId": {
      "type": "string",
      "minLength": 1,
      "description": "ID of the entity to duplicate"
    },
    "options": {
      "type": "object",
      "additionalProperties": {},
      "description": "Optional copy overrides (e.g., a new name, a future endDateTime, or a bidding scheme). A null value removes the field. A status here is ignored: the copy is always PAUSED."
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, validates the duplication with Google Ads' native validateOnly mutate and returns a DryRunResult under `dryRun` (expected post-state = the would-be-created copy, with `status` forced to `PAUSED`) without creating anything. No copy is created."
    }
  },
  "required": [
    "entityType",
    "customerId",
    "entityId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/duplicate-entity.tool.ts#L29)

<a id="tool-gads-remove-entity"></a>

### `gads_remove_entity`

**Behavior:** Its dry-run path sends a non-persisting validateOnly removal request, despite source prose suggesting the mutate endpoint is not called.

Remove a Google Ads entity using the :mutate API.

**Supported entity types:** campaign, adGroup, ad, keyword, campaignBudget, asset

**Warning**: This is a destructive operation. For campaigns and ad groups, consider using `gads_bulk_update_status` with status `PAUSED` instead of removing.

Note: In Google Ads, "remove" sets the entity status to REMOVED. The entity data is retained but the entity becomes inactive and cannot be re-enabled.

**Composite entityId required for:** `ad` → use `{adGroupId}~{adId}`, `keyword` → use `{adGroupId}~{criterionId}`. Other entity types use simple IDs.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entity to remove"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "entityId": {
      "type": "string",
      "minLength": 1,
      "description": "The entity ID to remove"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, validates the removal and returns a DryRunResult under `dryRun` (expected post-state = the entity with canonical status `deleted`, i.e. Google Ads REMOVED) without calling the :mutate API. The entity is never removed."
    }
  },
  "required": [
    "entityType",
    "customerId",
    "entityId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/remove-entity.tool.ts#L25)

<a id="tool-gads-update-entity"></a>

### `gads_update_entity`

Update an existing Google Ads entity using the :mutate API with updateMask discipline.

**Supported entity types:** campaign, adGroup, ad, keyword, campaignBudget, asset

**updateMask is required** — specify which fields to update as a comma-separated string.
Only fields listed in updateMask will be modified. This prevents accidental overwrites.

Example updateMask: "name,status" or "campaignBudget,endDateTime"

**Composite entityId required for:** `ad` → use `{adGroupId}~{adId}`, `keyword` → use `{adGroupId}~{criterionId}`. Other entity types use simple IDs.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entity to update"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "entityId": {
      "type": "string",
      "minLength": 1,
      "description": "The entity ID to update"
    },
    "data": {
      "type": "object",
      "additionalProperties": {},
      "description": "Entity data fields to update"
    },
    "updateMask": {
      "type": "string",
      "minLength": 1,
      "description": "Comma-separated list of fields to update (e.g., 'name,status')"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, validates the proposed mutation via the Google Ads native `validateOnly` flag and returns a DryRunResult under `dryRun` without applying the mutation. The underlying entity is never modified."
    }
  },
  "required": [
    "entityType",
    "customerId",
    "entityId",
    "data",
    "updateMask"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/update-entity.tool.ts#L21)

## Ads and creative assets

<a id="tool-gads-upload-image"></a>

### `gads_upload_image`

Upload an image to Google Ads as an ImageAsset from a URL.

The server downloads the image and creates an ImageAsset via AssetService (`assets:mutate`,
base64 `imageAsset.data`). The returned asset resource name is referenced by image ads and
extensions. This is a convenience wrapper over `gads_create_entity` (entityType `asset`) that
handles the download + base64 encoding for you.

**Image requirements:**

- Formats: JPEG, PNG, GIF
- Max file size: 5MB

Note: video assets reference a YouTube video ID rather than uploaded bytes; create them with
`gads_upload_video` (or `gads_create_entity`, entityType `asset`, `youtubeVideoAsset`).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Asset name (unique within the account)"
    },
    "mediaUrl": {
      "type": "string",
      "format": "uri",
      "description": "Publicly accessible URL of the image to upload"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, validates the upload request and returns an EffectDryRunResult under `dryRun` (expected effect = the would-be image asset) without downloading or creating anything. No asset is created."
    }
  },
  "required": [
    "customerId",
    "name",
    "mediaUrl"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/upload-image.tool.ts#L27)

<a id="tool-gads-upload-video"></a>

### `gads_upload_video`

**Behavior:** Creates a Google Ads asset referencing an existing YouTube video ID. It does not upload video bytes to YouTube.

Create a video asset in Google Ads from a YouTube video ID.

**This tool uploads no video file.** A Google Ads video asset is a `YouTubeVideoAsset`
that *references* a video already hosted on YouTube — you provide the YouTube video ID,
not a file. Google Ads' YouTubeVideoUploadService (`youTubeVideoUploads:create`) can
upload a file to YouTube, but no tool on this server wraps it, so host the video on
YouTube first, then pass its ID here.

This tool creates the asset via AssetService (`assets:mutate`, `type: YOUTUBE_VIDEO`,
`youtubeVideoAsset.youtubeVideoId`) and returns the asset resource name, which video
ads (`VIDEO_RESPONSIVE_AD`, bumper, in-stream, etc.) reference. It is a convenience
wrapper over `gads_create_entity` (entityType `asset`) that fixes the asset type and
shape for you.

**Requirements:**

- The video must already be uploaded to YouTube and be public or unlisted.
- `youtubeVideoId` is the 11-character ID from the watch URL
  (`https://www.youtube.com/watch?v=<id>`), not the full URL.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Asset name (unique within the account)"
    },
    "youtubeVideoId": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{11}$",
      "description": "The 11-character YouTube video ID (e.g. `dQw4w9WgXcQ`) of a public/unlisted video already hosted on YouTube"
    },
    "dry_run": {
      "type": "boolean",
      "default": false,
      "description": "When true, validates the request and returns an EffectDryRunResult under `dryRun` (expected effect = the would-be video asset) without creating anything. No asset is created."
    }
  },
  "required": [
    "customerId",
    "name",
    "youtubeVideoId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/upload-video.tool.ts#L24)

## Previews, validation, and local helpers

<a id="tool-gads-get-pacing-status"></a>

### `gads_get_pacing_status`

**Behavior:** Calculates pacing from caller-provided spend, budget, and dates; no Google Ads request is made.

Client-side pacing calculator — does NOT call the Google Ads API. Computes actual vs expected delivery given caller-supplied budget, spend-to-date, and flight dates. To populate spend, first call `gads_get_insights`; to populate budget and flight dates, first call `gads_get_entity` for the campaign. Note: spendToDate should be in actual currency units (not micros).

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "campaignId": {
      "type": "string",
      "description": "Google Ads Campaign ID"
    },
    "spendToDate": {
      "type": "number",
      "minimum": 0,
      "description": "Total spend to date in account currency (not micros — actual currency units)"
    },
    "budgetTotal": {
      "type": "number",
      "minimum": 0,
      "description": "Total campaign budget in account currency"
    },
    "flightStartDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Flight start date (YYYY-MM-DD)"
    },
    "flightEndDate": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Flight end date (YYYY-MM-DD)"
    },
    "currency": {
      "type": "string",
      "default": "USD",
      "description": "Currency code (default: USD)"
    }
  },
  "required": [
    "customerId",
    "campaignId",
    "spendToDate",
    "budgetTotal",
    "flightStartDate",
    "flightEndDate"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/get-pacing-status.tool.ts#L10)

<a id="tool-gads-validate-entity"></a>

### `gads_validate_entity`

**Behavior:** Calls Google Ads validateOnly for create/update. Update mode needs entityId and updateMask at runtime, although these are not unconditional required fields in the emitted schema.

Validate an entity payload without creating or modifying it. Uses Google Ads `validateOnly` mode for true server-side validation.

**Supported entity types:** campaign, adGroup, ad, keyword, campaignBudget, asset

Sends the payload to the Google Ads :mutate endpoint with `validateOnly: true`, which performs full server-side validation without any side effects.

**Modes:**

- **create**: Validates a create operation payload
- **update**: Validates an update operation payload (requires `entityId` and `updateMask`)

**Composite entityId required for:** `ad` -> use `{adGroupId}~{adId}`, `keyword` -> use `{adGroupId}~{criterionId}`. Other entity types use simple IDs.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "entityType": {
      "type": "string",
      "enum": [
        "campaign",
        "adGroup",
        "ad",
        "keyword",
        "campaignBudget",
        "asset"
      ],
      "description": "Type of entity to validate"
    },
    "customerId": {
      "type": "string",
      "pattern": "^\\d+$",
      "description": "Google Ads customer ID (no dashes)"
    },
    "mode": {
      "type": "string",
      "enum": [
        "create",
        "update"
      ],
      "description": "Validation mode: 'create' for new entity, 'update' for existing"
    },
    "data": {
      "type": "object",
      "additionalProperties": {},
      "description": "Entity data payload to validate (fields vary by entity type — see entity-schema resources)"
    },
    "entityId": {
      "type": "string",
      "description": "Entity ID (required for update mode)"
    },
    "updateMask": {
      "type": "string",
      "description": "Comma-separated list of fields to update (required for update mode, e.g., 'name,status')"
    }
  },
  "required": [
    "entityType",
    "customerId",
    "mode",
    "data"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/gads-mcp/src/mcp-server/tools/definitions/validate-entity.tool.ts#L16)

## Protocol test tools

Optional MCP protocol fixtures, not advertising operations. They test transport, logging, and elicitation behavior.

<a id="tool-echo"></a>

### `echo`

Only registered when `MCP_INCLUDE_CONFORMANCE_TOOLS=true`; not a Google Ads operation.

Echoes back the provided message. Used for connectivity testing and conformance validation.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string",
      "description": "Message to echo back"
    }
  },
  "required": [
    "message"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/shared/src/utils/conformance/conformance-echo-tool.ts#L29)

<a id="tool-test-elicitation"></a>

### `test_elicitation`

Only registered when `MCP_INCLUDE_CONFORMANCE_TOOLS=true`; not a Google Ads operation.

Requests user input via MCP elicitation. Used by MCP conformance tests.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string",
      "description": "The message to show the user"
    }
  },
  "required": [
    "message"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/shared/src/utils/conformance/conformance-echo-tool.ts#L111)

<a id="tool-test-elicitation-sep1034-defaults"></a>

### `test_elicitation_sep1034_defaults`

Only registered when `MCP_INCLUDE_CONFORMANCE_TOOLS=true`; not a Google Ads operation.

Tests elicitation with default values for all primitive types. Used by MCP conformance tests.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {},
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/shared/src/utils/conformance/conformance-echo-tool.ts#L152)

<a id="tool-test-elicitation-sep1330-enums"></a>

### `test_elicitation_sep1330_enums`

Only registered when `MCP_INCLUDE_CONFORMANCE_TOOLS=true`; not a Google Ads operation.

Tests all 5 enum variants in elicitation schemas. Used by MCP conformance tests.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {},
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/shared/src/utils/conformance/conformance-echo-tool.ts#L195)

<a id="tool-test-simple-text"></a>

### `test_simple_text`

Only registered when `MCP_INCLUDE_CONFORMANCE_TOOLS=true`; not a Google Ads operation.

Returns a fixed text response. Used by MCP conformance tests.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {},
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/shared/src/utils/conformance/conformance-echo-tool.ts#L48)

<a id="tool-test-tool-with-logging"></a>

### `test_tool_with_logging`

Only registered when `MCP_INCLUDE_CONFORMANCE_TOOLS=true`; not a Google Ads operation.

Sends structured log notifications during execution. Used by MCP conformance tests.

<details>
<summary>Parameters — full input schema</summary>

```json
{
  "type": "object",
  "properties": {},
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

[Source](https://github.com/cesteral/mcp-open-advertising/blob/1a567c3baeee018ee1f6572065f17e459bfa7977/packages/shared/src/utils/conformance/conformance-echo-tool.ts#L68)

## Attribution

Tool descriptions and schemas are extracted from the pinned upstream source under its [license](../licenses/Apache-2.0.txt). See [upstream notices](../licenses/NOTICE.txt). Catalog navigation and behavior notes were added here.
