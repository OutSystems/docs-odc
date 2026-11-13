---
guid: fda3c696-646f-4935-908f-cb175a85c55f
locale: en-us
summary: Semantic search over text attributes in ODC finds entity records by meaning. Learn how the platform indexes the text, how to check the indexing, and what a search returns.
figma:
coverage-type:
  - understand
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Tech lead
  - Developer
tags:
  - AI
  - Asynchronous Processes
  - Batch Processing
  - Data Synchronization
  - Entities
  - Indexes
outsystems-tools:
  - odc studio
  - odc portal
helpids:
isautopublish: true
---

# Semantic search over text attributes

Apps often store app data as text in entities, such as product descriptions, support notes, or case summaries. Users and agents need to find those records by what the text means rather than by the exact words it contains. To search that text by meaning, make the entity attributes that hold it searchable. ODC generates embeddings for the text of each record, keeps them synchronized as your app creates, updates, and deletes records, and returns the passages that match a query.

You configure the searchable attributes in ODC Studio and query them with the Semantic Search node. This page describes how the platform indexes text attributes and what a search returns. For app files stored in entities, refer to [Semantic search over files](search-over-files.md).

<div class="info" markdown="1">

In some regions, the platform processes semantic search requests in Europe, and the language of your content affects the results. Before you make text attributes searchable, check your region and your content language in [Regions and languages for semantic search](search-regions-languages.md).

</div>

## Text attribute use cases

Use text attributes when the content is text that your app and its users create and update as entity records. The following scenarios use text attributes:

* A store app finds products whose descriptions match a shopper's question, even when the question uses other words.
* A support agent finds past cases with a similar problem description, and grounds its answer in how the team resolved them.
* An app extracts Markdown from uploaded documents, stores it in a text attribute, and searches the stored Markdown.

## Searchable text attributes

In ODC Studio, you select the entities and the text attributes to include in semantic search, and you choose a chunk method for each attribute. The chunk method sets how the platform splits the text of each record into chunks. A single embedding for a long text represents its meaning poorly, so the platform generates one embedding for each chunk, and a search returns the chunk that matches the query.

Text attributes offer the following chunk methods:

* Smart, the default
* Fixed-size
* Sentence-based
* Recursive

The Sentence-based method is available for text attributes only. For the parameters of each method and guidance on choosing one, refer to [Chunk methods in ODC](chunk-methods.md).

To select the searchable attributes and set their chunk methods in ODC Studio, refer to [Make entity attributes searchable](make-attributes-searchable.md).

## Indexing for text attributes

The platform keeps the embeddings synchronized with your entity data when you publish your app and while your app runs. The platform processes changes asynchronously, so a change appears in search results after the platform finishes processing it.

### Indexing events

A full reindex processes every existing record in an entity. The following table shows what the platform does for each event and what a search returns afterward.

| Event | Platform action | Effect on search |
| --- | --- | --- |
| You enable semantic search on an attribute for the first time and publish the app | Creates the embedding schema and the database triggers that keep future embeddings in sync, and runs a full reindex | Existing records become searchable after the platform processes them in batches. The initial indexing time grows with the amount of data in the entity. |
| A record in a searchable entity is created, updated, or deleted | Generates, updates, or deletes the embeddings of the record | The change appears in results after the platform finishes processing its embeddings. Record operations in your app complete without waiting for the embeddings. |
| You change the chunk method or its parameters for an attribute that has semantic search enabled | Runs a full reindex | Results reflect the new chunks after the reindex finishes. |
| You remove an attribute from semantic search and publish the app | Deletes the embeddings of the attribute | The content of the attribute is absent from the results. |

### Indexing time and status

The platform applies per-tenant rate limits to indexing requests to protect the platform during large loads, so indexing time grows with the number of records. Each stage holds its own entity data and its own embeddings. To finish indexing before users search, load large datasets into the entity of a stage before users search in that stage.

ODC writes an information log when a full reindex starts and when it completes. Runtime indexing of individual record changes doesn't produce logs, so these logs are the only indexing status information in the ODC Portal. To check the status of a full reindex, in the ODC Portal, go to **Monitor** > **Logs** and search for `Embedding sync`.

The logs of a full reindex have the following format:

```
Embedding sync started for searchable attribute "Product.Description" due to configuration change
Embedding sync completed for searchable attribute "Product.Description" (10 records, 1s)
```

The completed log shows the number of records and the time the sync took. For an entity without records, it shows `(entity has no records)` instead.

## Search results for text attributes

A search over text attributes returns the chunks that match the query, ranked by score. Each result is a passage of text from one record of the entity.

To limit a search to the records that meet a condition on other attributes of the entity, use the **Filters** property of the Semantic Search node. For the properties of the node and the structure of the results, refer to [Semantic search inputs and results](search-inputs-results.md).
