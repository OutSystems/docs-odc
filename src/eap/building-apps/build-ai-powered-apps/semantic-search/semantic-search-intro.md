---
guid: fda3c696-646f-4935-908f-cb175a85c55f
locale: en-us
summary: Implement AI-powered semantic search in ODC apps using vector embeddings to understand user intent, context, and meaning for accurate search results.
figma:
coverage-type:
  - understand
  - evaluate
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Tech lead
  - Developer
tags:
  - AI
  - Entities
  - Indexes
  - Multi-language
outsystems-tools:
  - odc studio
  - odc portal
helpids:
isautopublish: true
---
# Semantic search in ODC apps

<div class="info" markdown="1">

Semantic search is in Beta. For more information about Beta features, refer to [OutSystems product releases](https://success.outsystems.com/support/release_notes/outsystems_product_releases/#beta). If you want to try this new capability contact your OutSystems account team.

</div>

ODC provides built-in semantic search over your app data in every app, removing the need for external search services.

## What's semantic search?

Semantic search eliminates the constraints of keyword-based queries. It converts words into vector embeddings, stores them in a vector database, and matches them by proximity to return the best conceptual matches.

Semantic search relies on three core principles:  

* **Intent**: The specific goals or tasks users aim to achieve.
* **Context**: The situational relationships between words in a dataset.  
* **Meaning**: The deeper understanding of synonyms and linguistic associations.  

## When should you use semantic search

Semantic search performs particularly well for:  

* **Chatbots**: Applies natural language understanding to navigate user intent and context, overcoming the limitations of traditional keyword matching.  
* **Recommendation engines**: Excels at identifying conceptual relationships and synonyms to surface relevant products or content, particularly in e-commerce environments.  

Semantic search excels at conceptual, meaning-based matching over text attributes. Scenarios that require absolute precision, such as serial numbers and error codes, call for exact keyword matching.

## The importance of chunking in semantic search

To understand the importance of chunking, consider how semantic search processes data: it converts text into vectors that represent its meaning.

A single vector for a large dataset obscures its meaning. Chunking breaks the data into smaller, meaningful pieces, letting the search engine find what's inside.

In ODC, you select the entities and attributes to include in semantic search, and choose a chunking method for each:

* **Smart chunking (default)**: Adapts automatically to the specific content found within searchable fields. This chunking method combines recursive chunking with default separators.

* **Fixed-sized chunking**: Defines a specific maximum character count per chunk and a set overlap between them.  
* **Sentence-based**: With this chunking method, you explicitly define how many sentences your chunks are allowed to have, and also the maximum number of characters and overlap for your chunks.
* **Recursive chunking**: Defines character limits and overlaps while prioritizing a hierarchy of specific characters as delimiters.  

## Indexing lifecycle

Semantic search keeps vector embeddings synchronized with your entity data at two points: when you publish your app, and while your app runs.

### Initial indexing at publish

Publishing an app with searchable entities creates the embedding schema and the database triggers that keep future embeddings in sync. The initial indexing time depends on the amount of data in the entity: the semantic search service processes records in batches, so entities with more data take longer to index.

### Runtime indexing

After publish, semantic search keeps embeddings synchronized with your entity data as your app runs. Creating, updating, or deleting a record in a searchable entity generates, updates, or deletes that record's embeddings automatically.

### Full reindex

Some actions trigger a full reindex, covering every existing record in an entity:

* Enabling semantic search on an attribute for the first time.
* Changing the chunking configuration on an attribute that already has semantic search enabled.

## Regional availability and limitations

Semantic search relies on cloud AI infrastructure. Due to regional differences in service availability, semantic search functions differently in the way it handles data, depending on where your ODC environment is hosted.

<div class="info" markdown="1">

**Semantic search is available for all customers in all regions.** This section covers regional constraints that might affect your environment.

</div>

### Unsupported regions

ODC semantic search triggers cross-region data transfers in the following regions:

* Cape Town (`af-south-1`)
* Hong Kong (`ap-east-1`)
* Jakarta (`ap-southeast-3`)
* Singapore (`ap-southeast-1`)
* Tel Aviv (`il-central-1`)
* UAE (`me-central-1`)

To maintain data residency compliance, deploy semantic search outside these territories. If you use semantic search in one of these regions, requests route through the European region (`eu-central-1`) for processing, then return to your region. Storage remains within your region throughout. This limitation exists because the embedding model is available only in supported regions.

<div class="info" markdown="1">

To determine your ODC environment's region, refer to the information provided when you purchased ODC or contact your account manager.

</div>

### Usage of multiple languages

Semantic search over app data supports most languages. The following languages have dictionaries that improve result accuracy:

* English
* Czech
* Danish
* Dutch
* Estonian
* Finnish
* French
* German
* Italian
* Norwegian
* Polish
* Portuguese
* Slovene
* Spanish
* Swedish

These dictionaries address language-specific nuances, such as acronyms and cultural context, improving how the system interprets phrases. In all other languages, punctuation divides sentences instead, which might lead to less accurate results. The system recognizes supported languages automatically and defaults to English for the rest.
