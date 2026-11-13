---
summary: Knowledge bases in ODC index curated documents so agents and apps ground their answers in them. Learn about indexing, search results, file types, and stages.
tags:
  - AI
  - Agentic
  - Architecture
  - Data
  - Infrastructure
  - Indexes
guid: aa426959-c1c6-474e-b905-8d96e799a15f
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - understand
topic:
  - kb-region-data-residency-limits
  - kb-stage-isolation
  - knowledge-base-overview
audience:
  - Developer
  - Platform administrator
  - Tech lead
isautopublish: true
outsystems-tools:
  - odc portal
---

# Knowledge bases in ODC

An AI model answers from its general training data. To ground the answers of agents and apps in your organization's documents, such as policies, manuals, and product guides, store the documents in a knowledge base. A knowledge base is a curated set of documents that an administrator uploads and manages in the ODC Portal, separate from the app data. The platform indexes the documents and generates a search action that agents and apps call at runtime.

This page describes how the platform indexes and searches a knowledge base, the files it accepts, and how stages affect it. For a comparison with semantic search over app data and app files, refer to [Semantic search in ODC](../semantic-search/semantic-search-overview.md).

<div class="info" markdown="1">

Knowledge bases aren't available in every region, and the language of a document affects the results. Before you create a knowledge base, check your region and your content language in [Regions and languages for semantic search](../semantic-search/search-regions-languages.md).

</div>

## Knowledge base use cases

Use a knowledge base when an administrator curates the documents and keeps them separate from the records that your app creates. Several agents or apps can answer from the same set. The following scenarios use a knowledge base:

* An HR assistant answers employee questions from the company policies.
* Several support agents ground their answers in the same set of product guides.
* An app answers questions about internal standards that a documentation team maintains.

## Knowledge base structure

A knowledge base is one asset that exists in every stage. You create it once, and its configuration applies to all stages, such as Development, QA, and Production. The content differs by stage. Each stage has its own files, storage area, and search index, so the documents that you upload in one stage appear only in the search results of that stage.

Entities follow the same model. An entity has the same attributes in every stage, and the database of each stage holds its own records.

The shared configuration keeps an app consistent when you deploy it. An app that calls the `SearchKB<KnowledgeBaseName>` action in the Development stage calls the same action, with the same parameters, after you deploy it to the QA and Production stages. In each stage, the action searches the files indexed in that stage.

Each part of a knowledge base is either shared by all stages or separate in each stage. The following table shows the scope of each part.

| Part | Contains | Scope |
| --- | --- | --- |
| Knowledge base | The name, the description, and the generated `SearchKB<KnowledgeBaseName>` action | Shared by all stages |
| Data source | The data source configuration: the name, the description, the data source type **Upload files**, and the chunk method | Shared by all stages |
| Files | The files that an administrator uploads to the data source, their status, and the search index | Separate in each stage |

The platform doesn't copy files between stages. To use the same documents in several stages, upload them to the data source in each stage. In the ODC Portal, select a stage in the stage selector to see the files of that stage and their status. For more information, refer to [Upload files to a knowledge base](create-manage-knowledge-base.md#upload-files-to-a-knowledge-base).

## Indexing for knowledge bases

When an administrator uploads a file to a knowledge base, the platform extracts the text and splits it into chunks. The platform then generates an embedding for each chunk and stores the embeddings in a vector store. The platform processes each file in the background and indexes it completely or not at all, so a file is either fully searchable or absent from the results. The ODC Portal shows the status of each file. For more information, refer to [Upload files to a knowledge base](create-manage-knowledge-base.md#upload-files-to-a-knowledge-base).

The chunk method sets how the platform splits the text of each file. You choose the chunk method in the data source configuration when you create the knowledge base. The chunk method applies to all stages, and you can't change it afterward. Knowledge bases offer the same chunk methods as File attributes. For more information, refer to [Chunk methods in ODC](../semantic-search/chunk-methods.md).

## Search results for knowledge bases

For each knowledge base, the platform generates a server action named `SearchKB<KnowledgeBaseName>`. An agent or app calls the action with a query, and the action returns the chunks whose meaning is closest to the query, ranked by score. Using the retrieved chunks as context for the answers of an AI model is called retrieval-augmented generation (RAG).

To add the action to an app and call it, refer to [Search a knowledge base](../semantic-search/add-semantic-search.md#search-a-knowledge-base). For the fields of the request and the results, refer to [Semantic search inputs and results](../semantic-search/search-inputs-results.md).

## File types and sizes for knowledge bases

Knowledge bases accept the same file types as File attributes, such as PDF, Microsoft Word, and Markdown files. For the full list, refer to [File types for File attributes](../semantic-search/search-over-files.md#file-types-for-file-attributes).

For the maximum file size, refer to [Semantic search and knowledge bases in OutSystems system requirements for ODC](../../../getting-started/system-requirements.md#semantic-search-and-knowledge-bases).
