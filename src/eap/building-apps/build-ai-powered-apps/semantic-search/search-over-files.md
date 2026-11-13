---
summary: Semantic search over files in ODC finds passages in files stored in entities. Learn how the platform indexes File attributes and what a search returns.
tags:
  - AI
  - Data
  - Data Model
  - Entities
  - Indexes
guid: 3413323d-64c2-4a3d-8fa5-04e2fc60ed2c
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - understand
topic:
  - configure-file-attributes
  - understand-file-search
audience:
  - Architect
  - Developer
  - Tech lead
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Semantic search over files

Apps store app files in entities, such as service reports, contracts, or manuals that users upload, and the answer to a question is often one passage inside one file. To search the content of those files by meaning, make the File attribute that holds them searchable. ODC extracts the text of each file, indexes it, and keeps the index current as users and app logic upload, replace, and delete files. Each result links to the entity record that holds the file, so you can filter the results and combine them with the rest of your app data.

You configure the searchable File attributes in ODC Studio and query them with the Semantic Search node. This page describes the file types that the platform indexes, how it indexes File attributes, and what a search returns. For app data stored as text in entity attributes, refer to [Semantic search over text attributes](search-over-text-attributes.md).

<div class="info" markdown="1">

Semantic search over File attributes isn't available in every region, and the language of a file affects the results. Before you make File attributes searchable, check your region and your content language in [Regions and languages for semantic search](search-regions-languages.md).

</div>

## File attribute use cases

Use File attributes when the answer is in a document that belongs to an entity record, such as a technician's report or a customer's contract. The following scenarios use File attributes:

* A maintenance app finds the service reports that describe a failure similar to the one a technician reports.
* A support agent answers customer questions from the manuals attached to product records.
* A review app finds clauses with a similar meaning across the contracts that users upload to customer records.

In each example, the files belong to entity records, and users or app logic add and change them as the app runs. For documents that an administrator curates separately from the app data, refer to [Knowledge bases in ODC](../knowledge-base/knowledge-bases-overview.md).

## Searchable File attributes

In ODC Studio, you select the File attributes of an entity to include in semantic search, and you choose a chunk method for each attribute. The chunk method sets how the platform splits the text of each file into chunks, and each chunk is one search result. Because files have structure, such as pages, paragraphs, and section headers, File attributes also offer methods that split content at that structure. The following chunk methods are available for File attributes:

* Smart, the default
* Fixed-size
* Recursive
* By page
* By paragraph
* By section-header
* None

The Sentence-based method is available for text attributes only, because splitting a file by sentence produces a large number of chunks. For the parameters of each method and guidance on choosing one, refer to [Chunk methods in ODC](chunk-methods.md).

To select the searchable attributes and set their chunk methods in ODC Studio, refer to [Make entity attributes searchable](make-attributes-searchable.md).

## File types for File attributes

A File attribute stores files of any type, and the platform indexes the files of the following types. Knowledge bases accept the same types.

| File type | Extension |
| --- | --- |
| Comma-separated values | `.csv` |
| Markdown | `.md` |
| Microsoft PowerPoint | `.pptx` |
| Microsoft Word | `.docx` |
| PDF | `.pdf` |
| Plain text | `.txt` |
| Web pages | `.html`, `.htm` |

The platform skips files of other types, such as Microsoft Excel workbooks and image files, and writes an entry in the app logs. The other files in the attribute stay searchable. To make the content of an image searchable, store it in a PDF file. The platform extracts the text of images in PDF files.

The platform also skips files larger than the maximum file size. For the limit, refer to [Semantic search and knowledge bases in OutSystems system requirements for ODC](../../../getting-started/system-requirements.md#semantic-search-and-knowledge-bases). To find the entries for skipped files, search the app logs in the ODC Portal under **Monitor** > **Logs**.

## Indexing for File attributes

The platform extracts, chunks, and embeds each file in the background, and keeps the index synchronized with the files in the attribute. The platform indexes each file completely or not at all, so a file is either fully searchable or absent from the results. For the indexing steps that all search options share, refer to [Indexing and search flow](semantic-search-overview.md#indexing-and-search-flow).

A search reflects a change to a file only after the platform finishes processing it. The following table shows what the platform does for each event and what a search returns in the meantime.

| Event | Platform action | Effect on search |
| --- | --- | --- |
| You mark the attribute as searchable and publish the app | Indexes the files that already exist in the entity | Each file becomes searchable after its processing finishes. |
| A user or the app uploads a file | Extracts, chunks, and embeds the file, and adds the embeddings to the index | The file becomes searchable after its processing finishes. |
| A user or the app replaces a file | Generates embeddings for the new content and removes the embeddings of the previous content | The previous version stays searchable while the platform extracts the text of the new version. While the platform generates the embeddings, results can include passages from both versions. |
| A user or the app deletes a file, or the record that holds the file | Removes the embeddings of the file | The file is absent from the results. |
| A user or the app uploads a file larger than the maximum file size, or of a type that the platform doesn't index | Skips the file and writes an entry in the app logs | The file is absent from the results. The other files in the attribute stay searchable. |
| You change the chunk method or its parameters | Reindexes every file in the attribute | Results reflect the new chunks after the reindexing finishes. |
| You remove the attribute from semantic search and publish the app | Deletes the embeddings of every file in the attribute | The files of the attribute are absent from the results. |

No indicator in the ODC Portal shows when the platform finishes indexing a file. To confirm that a file is searchable, run a search for content in the file. For the steps, refer to [Test the search](add-semantic-search.md#test-the-search).

## Search results for File attributes

A search over a File attribute returns the chunks that match the query, ranked by score. Each result contains a passage of file content and links to the entity record that holds the file.

Because results link to entity records, you can filter a search on other attributes of the entity and combine the results with data from other entities. For the properties of the node and the structure of the results, refer to [Semantic search inputs and results](search-inputs-results.md).
