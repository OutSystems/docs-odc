---
summary: The properties of the Semantic Search node, the request fields and filters of the knowledge base search action, and the results that each returns in ODC.
tags:
  - AI
  - Data
  - Entities
  - Indexes
  - Pagination
guid: 95911935-7901-4167-a8ba-898b0a4bf105
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - remember
topic:
  - configure-search-inputs
  - interpret-search-results
audience:
  - Developer
  - Tech lead
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Semantic search inputs and results

Use this reference when you configure the Semantic Search node to search entity attributes, or when you call the `SearchKB<KnowledgeBaseName>` action to search a knowledge base. It lists the inputs that each one accepts and the results that each one returns. To add either element to a server action, refer to [Add semantic search to your app](add-semantic-search.md).

## Semantic search node properties

The Semantic Search node queries the searchable attributes of an entity. A node targets either text attributes or File attributes, so an entity with both kinds needs a separate node for each. The following table lists the properties of the node. **Filters**, **Page Size**, **Page Number**, and **Minimum Score** are optional.

| Property | Description |
| --- | --- |
| **Search Query** | The text to search for. |
| **Source** | The entity that holds the searchable attributes. |
| **Searchable attributes** | The attributes to search. A node targets either text attributes or File attributes. |
| **Filters** | A condition on the attributes of the source entity, written the same way as an Aggregate filter. The search returns only the chunks from the records that meet the condition. The condition can use the variables and input parameters of the server action. |
| **Page Size** | Sets the number of results on each page. The default is 50. |
| **Page Number** | Sets the page of results that the node returns. |
| **Minimum Score** | Excludes the results with a score below the value. The default is 0. |

<div class="warning" markdown="1">

The Semantic Search node doesn't check whether the end user can access a record or a file. To limit the results to the records that a user can access, set **Filters**.

</div>

## Semantic search node results

The Semantic Search node returns the results in the `Records` output list. Each item in the list holds one chunk that matches the query, and it has the following parts:

* The record of the source entity that holds the chunk. The part has the name of the entity, such as `MaintenanceRecord` for the `MaintenanceRecord` entity.
* A `SearchResult` structure that describes the match.

The following table lists the fields of the `SearchResult` structure.

| Field | Data type | Description |
| --- | --- | --- |
| `Score` | Decimal | The relevance score of the chunk. A higher score means a closer match. |
| `MatchingContent` | Text | The text of the chunk. For a File attribute, the content is text that the platform extracted from the file. |
| `MatchingAttribute` | Text | The name of the searchable attribute that holds the chunk. |
| `ChunkNumber` | Integer | The position of the chunk in the content of the attribute. For a File attribute, the first chunk of a file is `1`. |

A record can appear more than once in the list, once for each chunk that matches the query. Because each item includes the entity record, you can use the other attributes of the record in your logic. To combine the results with data from other entities, use an Aggregate.

## Knowledge base search action request

For each knowledge base, the platform generates a server action named `SearchKB<KnowledgeBaseName>`, which is `SearchKB` followed by the name of the knowledge base. The **Element** field on the details page of the knowledge base in the ODC Portal shows the exact name. The action takes a mandatory `Request` structure. The following table lists the fields of the request in the order that ODC Studio shows them. `TopK`, `MinimumScore`, and `Filters` are optional.

| Field | Description |
| --- | --- |
| `Query` | The text to search for, up to 8192 characters. |
| `TopK` | Sets the maximum number of results, from 1 to 50. The default is 5. |
| `MinimumScore` | Excludes the results with a score below the value, from 0 to 1. The default is 0. The action applies the minimum score to the `TopK` results, so a search can return fewer results than `TopK`. |
| `Filters` | A list of `Name` and `Value` pairs that limits the search to the chunks whose metadata matches every pair. The following section describes the filters. |

## Knowledge base search filters

When your app or agent already knows which document holds the answer, a filter limits the search to the chunks of that document. For example, an app limits the search to the manual of the product that a user selects.

Each item in `Filters` is a `Name` and `Value` pair. `Name` is the name of a metadata field of the chunks, and `Value` is the value that the field must equal exactly, including letter case. When `Filters` has several items, a chunk must match all of them.

The following examples show how to narrow a search by document, file type, language, or position in a file.

| Name | Value |
| --- | --- |
| `"filename"` | The name of a file in the knowledge base, such as `"HRPolicies.pdf"`. The `Title` field of a result shows it. |
| `"documentId"` | The identifier of a file in the knowledge base. The `Attributes` field of a result shows it. |
| `"mimeType"` | The media type of a file, such as `"application/pdf"`. |
| `"language"` | The language code of the content, such as `"en"`. |
| `"pageNumber"` | The page of the file that the chunk comes from, such as `"3"`. The value is `"0"` when the file has no pages. |
| `"chunkPosition"` | The position of the chunk in the file, starting at `"1"`. |

In ODC Studio, `Name` and `Value` are expressions, so you enter text values in quotes. The names are case-sensitive and use camelCase, such as `"documentId"` and `"mimeType"`.

## Knowledge base search action results

The `SearchKB<KnowledgeBaseName>` action returns a list of documents in the `Documents` output, ranked by score. Each document is one chunk that matches the query. The following table lists the fields of each document.

| Field | Description |
| --- | --- |
| `Id` | The identifier of the chunk. |
| `Title` | The name of the file that holds the chunk. |
| `Content` | The text of the chunk. |
| `Score` | The relevance score of the chunk, from 0 to 1, rounded to three decimal places. A higher score means a closer match. |
| `Attributes` | A list of `Name` and `Value` pairs with the other metadata of the chunk, such as `documentId`, `mimeType`, `pageNumber`, and `language`. |
